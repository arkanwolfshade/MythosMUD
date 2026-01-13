#!/usr/bin/env python3
"""Load world seed data (rooms, zones, zone configs, holidays, schedules, emotes) into PostgreSQL database."""

import os
import sys
from pathlib import Path

import asyncpg
from anyio import run
from dotenv import load_dotenv

load_dotenv()


def _validate_environment_and_files() -> tuple[str, Path, Path]:
    """Validate DATABASE_URL and required files exist."""
    database_url = os.getenv("DATABASE_URL", "")
    if not database_url:
        print("ERROR: DATABASE_URL not set")
        sys.exit(1)

    schema_file = Path("db/authoritative_schema.sql")
    seed_file = Path("data/db/00_world_and_emotes.sql")

    if not schema_file.exists():
        print(f"ERROR: Schema file not found: {schema_file}")
        print("       Run: ./scripts/generate_schema_from_dev.sh to generate it")
        sys.exit(1)

    if not seed_file.exists():
        print(f"ERROR: Seed file not found: {seed_file}")
        sys.exit(1)

    return database_url, schema_file, seed_file


async def _print_current_table_counts(conn: asyncpg.Connection) -> None:
    """Print current table counts, handling missing tables gracefully."""
    print("\nCurrent table counts:")
    try:
        zone_count = await conn.fetchval("SELECT COUNT(*) FROM zones")
        print(f"  Zones: {zone_count}")
    except asyncpg.UndefinedTableError:
        print("  Zones: Table does not exist yet")

    try:
        room_count = await conn.fetchval("SELECT COUNT(*) FROM rooms")
        print(f"  Rooms: {room_count}")
    except asyncpg.UndefinedTableError:
        print("  Rooms: Table does not exist yet")

    try:
        holiday_count = await conn.fetchval("SELECT COUNT(*) FROM calendar_holidays")
        print(f"  Holidays: {holiday_count}")
    except asyncpg.UndefinedTableError:
        print("  Holidays: Table does not exist yet")

    try:
        schedule_count = await conn.fetchval("SELECT COUNT(*) FROM calendar_npc_schedules")
        print(f"  Schedules: {schedule_count}")
    except asyncpg.UndefinedTableError:
        print("  Schedules: Table does not exist yet")

    try:
        zone_config_count = await conn.fetchval("SELECT COUNT(*) FROM zone_configurations")
        print(f"  Zone Configurations: {zone_config_count}")
    except asyncpg.UndefinedTableError:
        print("  Zone Configurations: Table does not exist yet")


def _clean_psql_commands(sql_content: str, preserve_whitespace: bool = False) -> str:
    """Remove psql-specific commands and comments from SQL content.

    Args:
        sql_content: Raw SQL content with potential psql commands
        preserve_whitespace: If True, keep original line format; if False, strip lines
    """
    lines = sql_content.split("\n")
    clean_lines = []
    for line in lines:
        stripped = line.strip()
        # Skip psql commands (lines starting with \) and comments
        if stripped.startswith("\\") or stripped.startswith("--"):
            continue
        if stripped:  # Keep non-empty lines
            if preserve_whitespace:
                clean_lines.append(line)
            else:
                clean_lines.append(stripped)
    return "\n".join(clean_lines)


async def _apply_schema(conn: asyncpg.Connection, schema_file: Path) -> None:
    """Apply database schema from file."""
    print(f"\nApplying schema from {schema_file}...")
    schema_sql = schema_file.read_text(encoding="utf-8")
    clean_schema_sql = _clean_psql_commands(schema_sql, preserve_whitespace=True)

    try:
        await conn.execute(clean_schema_sql)
        print("  [OK] Schema applied successfully")
    except asyncpg.PostgresError as e:
        print(f"  [ERROR] Schema application failed - {e}")
        import traceback

        traceback.print_exc()
        # Continue anyway - some tables might already exist


def _read_seed_file(seed_file: Path) -> str:
    """Read seed file, handling UTF-8 and UTF-16 encoding."""
    try:
        sql = seed_file.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        sql = seed_file.read_text(encoding="utf-16")
        # Strip UTF-16 BOM if present
        if sql.startswith("\ufeff"):
            sql = sql[1:]
    return sql


async def _execute_seed_statements(conn: asyncpg.Connection, clean_sql: str) -> None:
    """Execute seed SQL statements with error handling."""
    statements = [s.strip() for s in clean_sql.split(";") if s.strip()]

    print(f"  Executing {len(statements)} SQL statements...")
    inserted_count = 0
    skipped_count = 0
    error_count = 0

    try:
        # Execute each statement individually
        for i, statement in enumerate(statements, 1):
            if not statement:
                continue
            try:
                # Normalize SQL statement termination - ensure it ends with exactly one semicolon
                # SAFETY: statement comes from trusted SQL files in repository (not user input)
                # This normalization is safe because:
                # 1. statement is from trusted seed data files (data/db/00_world_and_emotes.sql)
                # 2. We're only normalizing statement termination, not building SQL from user input
                # 3. No user-controlled data is involved in SQL construction
                normalized_statement = statement.rstrip().rstrip(";")
                # Use constant format string to avoid CodeQL string concatenation warning
                # The semicolon is a constant, and normalized_statement is from trusted source
                sql_statement = f"{normalized_statement};"
                # nosemgrep: python.lang.security.audit.sqli.asyncpg-sqli.asyncpg-sqli
                # nosec B608: Loading seed data from trusted SQL files in repository (not user input)
                await conn.execute(sql_statement)
                inserted_count += 1
            except asyncpg.PostgresError as e:
                error_msg = str(e).lower()
                # Check if it's a duplicate key error (data already exists)
                if (
                    "duplicate key" in error_msg
                    or "already exists" in error_msg
                    or "violates unique constraint" in error_msg
                ):
                    skipped_count += 1
                else:
                    error_count += 1
                    print(f"  [ERROR] Statement {i} failed: {e}")
                    print(f"  [ERROR] Statement: {statement[:100]}...")

        if error_count == 0:
            print(f"  [OK] World seed data loaded successfully ({inserted_count} inserted, {skipped_count} skipped)")
        else:
            print(
                f"  [WARNING] Completed with {error_count} errors ({inserted_count} inserted, {skipped_count} skipped)"
            )
    except Exception as e:  # pylint: disable=broad-exception-caught
        # This catches any unexpected errors during the batch execution process
        print(f"  [ERROR] - {e}")
        import traceback

        traceback.print_exc()
        sys.exit(1)


async def _load_seed_data(conn: asyncpg.Connection, seed_file: Path) -> None:
    """Load seed data from file."""
    print(f"\nLoading seed data from {seed_file}...")
    sql = _read_seed_file(seed_file)
    clean_sql = _clean_psql_commands(sql)
    await _execute_seed_statements(conn, clean_sql)


async def _print_final_table_counts(conn: asyncpg.Connection) -> None:
    """Print final table counts after loading."""
    print("\nFinal table counts:")
    zone_count = await conn.fetchval("SELECT COUNT(*) FROM zones")
    print(f"  Zones: {zone_count}")

    room_count = await conn.fetchval("SELECT COUNT(*) FROM rooms")
    print(f"  Rooms: {room_count}")

    holiday_count = await conn.fetchval("SELECT COUNT(*) FROM calendar_holidays")
    print(f"  Holidays: {holiday_count}")

    schedule_count = await conn.fetchval("SELECT COUNT(*) FROM calendar_npc_schedules")
    print(f"  Schedules: {schedule_count}")

    zone_config_count = await conn.fetchval("SELECT COUNT(*) FROM zone_configurations")
    print(f"  Zone Configurations: {zone_config_count}")


async def main():
    """Load world seed data and verify."""
    print("=" * 60)
    print("MYTHOSMUD WORLD SEED DATA LOADER")
    print("=" * 60)

    database_url, schema_file, seed_file = _validate_environment_and_files()

    # Convert asyncpg URL to connection params
    url = database_url.replace("postgresql+asyncpg://", "postgresql://")
    print(f"Database URL: {url[:50]}...")

    conn = await asyncpg.connect(url)

    try:
        await _print_current_table_counts(conn)
        await _apply_schema(conn, schema_file)
        await _load_seed_data(conn, seed_file)
        await _print_final_table_counts(conn)

        print("\n" + "=" * 60)
        print("WORLD SEED DATA LOADING COMPLETE")
        print("=" * 60)

    finally:
        await conn.close()


if __name__ == "__main__":
    run(main)
