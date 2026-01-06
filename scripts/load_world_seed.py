#!/usr/bin/env python3
"""Load world seed data (rooms, zones, zone configs, holidays, schedules, emotes) into PostgreSQL database."""

import asyncio
import os
import sys
from pathlib import Path

import asyncpg
from dotenv import load_dotenv

load_dotenv()


async def main():
    """Load world seed data and verify."""
    print("=" * 60)
    print("MYTHOSMUD WORLD SEED DATA LOADER")
    print("=" * 60)

    # Get database URL from environment
    database_url = os.getenv("DATABASE_URL", "")
    if not database_url:
        print("ERROR: DATABASE_URL not set")
        sys.exit(1)

    # Convert asyncpg URL to connection params
    url = database_url.replace("postgresql+asyncpg://", "postgresql://")
    print(f"Database URL: {url[:50]}...")

    # Use authoritative schema instead of legacy schema files
    schema_file = Path("db/authoritative_schema.sql")
    seed_file = Path("data/db/00_world_and_emotes.sql")

    if not schema_file.exists():
        print(f"ERROR: Schema file not found: {schema_file}")
        print("       Run: ./scripts/generate_schema_from_dev.sh to generate it")
        sys.exit(1)

    if not seed_file.exists():
        print(f"ERROR: Seed file not found: {seed_file}")
        sys.exit(1)

    conn = await asyncpg.connect(url)

    try:
        # Check current counts
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

        # Apply schema first
        print(f"\nApplying schema from {schema_file}...")
        schema_sql = schema_file.read_text(encoding="utf-8")

        # Remove psql-specific commands
        lines = schema_sql.split("\n")
        schema_lines = []
        for line in lines:
            stripped = line.strip()
            # Skip psql commands (lines starting with \)
            if stripped.startswith("\\"):
                continue
            schema_lines.append(line)

        clean_schema_sql = "\n".join(schema_lines)
        try:
            await conn.execute(clean_schema_sql)
            print("  [OK] Schema applied successfully")
        except asyncpg.PostgresError as e:
            print(f"  [ERROR] Schema application failed - {e}")
            import traceback

            traceback.print_exc()
            # Continue anyway - some tables might already exist

        # Load seed file
        print(f"\nLoading seed data from {seed_file}...")
        # Try UTF-8 first, fall back to UTF-16 if needed
        try:
            sql = seed_file.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            sql = seed_file.read_text(encoding="utf-16")
            # Strip UTF-16 BOM if present
            if sql.startswith("\ufeff"):
                sql = sql[1:]

        # Remove psql-specific commands (like \set ON_ERROR_STOP on)
        # Split by lines and filter out psql commands
        lines = sql.split("\n")
        sql_lines = []
        for line in lines:
            line = line.strip()
            # Skip psql commands (lines starting with \)
            if line.startswith("\\") or line.startswith("--"):
                continue
            if line:  # Keep non-empty lines
                sql_lines.append(line)

        # Rejoin and split by semicolons to execute statements individually
        clean_sql = "\n".join(sql_lines)
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
                print(
                    f"  [OK] World seed data loaded successfully ({inserted_count} inserted, {skipped_count} skipped)"
                )
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

        # Verify final counts
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

        print("\n" + "=" * 60)
        print("WORLD SEED DATA LOADING COMPLETE")
        print("=" * 60)

    finally:
        await conn.close()


if __name__ == "__main__":
    asyncio.run(main())
