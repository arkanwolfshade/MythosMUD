#!/usr/bin/env python3
"""Load world seed data (rooms, zones, zone configs, holidays, schedules, emotes) into PostgreSQL database.

WARNING: This script applies the environment-specific DDL (db/mythos_<dbname>_ddl.sql) FIRST,
which DROPS ALL TABLES (rooms, zones, players, users, etc.) and recreates an empty schema,
then loads the environment DML (world, professions, items, NPCs, etc.). Running it against a
database that has data you care about will DESTROY that data. Use a separate DB for seeding,
or run only the DML file: psql -d your_db -f data/db/mythos_<env>_dml.sql

DDL and DML run via psql -f: DDL first kicks other backends then applies drops/creates; DML is
pg_dump format (COPY ... FROM stdin) and cannot be executed reliably with asyncpg.execute.

The DDL and DML files are chosen from DATABASE_URL: mythos_dev -> db/mythos_dev_ddl.sql +
data/db/mythos_dev_dml.sql, mythos_unit -> mythos_unit_ddl + mythos_unit_dml, mythos_e2e ->
mythos_e2e_ddl + mythos_e2e_dml.

asyncpg table counts use POSTGRES_SEARCH_PATH if set, else the database name as schema (see .env.e2e_test).
"""

import os
import shutil
import subprocess  # nosec B404: psql must be invoked for DDL/DML; argv is built from resolved psql + URL parts
import sys
from pathlib import Path
from typing import cast
from urllib.parse import unquote, urlparse

import asyncpg
from anyio import run
from dotenv import load_dotenv

_ = load_dotenv()


def _validate_environment_and_files() -> tuple[str, Path, Path]:
    """Validate DATABASE_URL and required files exist."""
    database_url = os.getenv("DATABASE_URL", "")
    if not database_url:
        print("ERROR: DATABASE_URL not set")
        sys.exit(1)

    db_name = database_url.split("/")[-1].split("?")[0].strip()
    allowed = ("mythos_dev", "mythos_unit", "mythos_e2e")
    if db_name not in allowed:
        print(f"ERROR: DATABASE_URL database name must be one of {allowed!r}, got {db_name!r}")
        sys.exit(1)

    # Require explicit confirmation: this script DROPS ALL TABLES
    if os.getenv("CONFIRM_LOAD_WORLD_SEED") != "1":
        print("=" * 60)
        print("DESTRUCTIVE: This script applies the environment DDL which")
        print("DROPS ALL TABLES (rooms, zones, players, users, etc.) then loads")
        print("world seed. All existing data in the database will be LOST.")
        print("")
        print(f"Database: {db_name}")
        print("")
        print("To run anyway, set: CONFIRM_LOAD_WORLD_SEED=1")
        print("  e.g. CONFIRM_LOAD_WORLD_SEED=1 python scripts/load_world_seed.py")
        print("=" * 60)
        sys.exit(1)

    schema_file = Path(f"db/{db_name}_ddl.sql")
    dml_file = Path(f"data/db/{db_name}_dml.sql")

    if not schema_file.exists():
        print(f"ERROR: DDL file not found: {schema_file}")
        print("       Use db/mythos_dev_ddl.sql, db/mythos_unit_ddl.sql, or db/mythos_e2e_ddl.sql")
        sys.exit(1)

    if not dml_file.exists():
        print(f"ERROR: DML file not found: {dml_file}")
        print("       Use data/db/mythos_dev_dml.sql, mythos_unit_dml.sql, or mythos_e2e_dml.sql")
        sys.exit(1)

    return database_url, schema_file, dml_file


async def _print_current_table_counts(conn: asyncpg.Connection) -> None:
    """Print current table counts, handling missing tables gracefully."""
    print("\nCurrent table counts:")
    try:
        zone_count = cast(int | None, await conn.fetchval("SELECT COUNT(*) FROM zones"))
        print(f"  Zones: {zone_count}")
    except asyncpg.UndefinedTableError:
        print("  Zones: Table does not exist yet")

    try:
        room_count = cast(int | None, await conn.fetchval("SELECT COUNT(*) FROM rooms"))
        print(f"  Rooms: {room_count}")
    except asyncpg.UndefinedTableError:
        print("  Rooms: Table does not exist yet")

    try:
        holiday_count = cast(int | None, await conn.fetchval("SELECT COUNT(*) FROM calendar_holidays"))
        print(f"  Holidays: {holiday_count}")
    except asyncpg.UndefinedTableError:
        print("  Holidays: Table does not exist yet")

    try:
        schedule_count = cast(int | None, await conn.fetchval("SELECT COUNT(*) FROM calendar_npc_schedules"))
        print(f"  Schedules: {schedule_count}")
    except asyncpg.UndefinedTableError:
        print("  Schedules: Table does not exist yet")

    try:
        zone_config_count = cast(int | None, await conn.fetchval("SELECT COUNT(*) FROM zone_configurations"))
        print(f"  Zone Configurations: {zone_config_count}")
    except asyncpg.UndefinedTableError:
        print("  Zone Configurations: Table does not exist yet")


def _database_url_for_cli(database_url: str) -> str:
    """Normalize SQLAlchemy/async driver URLs to a plain postgresql:// form for tools."""
    return database_url.replace("postgresql+asyncpg://", "postgresql://", 1)


def _parse_pg_url_for_psql(database_url: str) -> tuple[str, int, str, str, str]:
    """Return (host, port, user, password, dbname) from DATABASE_URL. Password may be empty."""
    parsed = urlparse(_database_url_for_cli(database_url))
    if not parsed.hostname or not parsed.path:
        msg = "DATABASE_URL must include host and database path for psql."
        raise ValueError(msg)
    dbname = parsed.path.lstrip("/").split("?")[0]
    user = unquote(parsed.username or "")
    password = unquote(parsed.password or "") if parsed.password is not None else ""
    host = parsed.hostname
    port = int(parsed.port or 5432)
    return host, port, user, password, dbname


def _resolve_psql_executable() -> str:
    """Locate psql for DDL (pg_dump files are meant for psql, not one asyncpg.execute blob)."""
    override = os.environ.get("PSQL_EXE") or os.environ.get("PSQL_PATH")
    if override and Path(override).is_file():
        return str(Path(override).resolve())
    which = shutil.which("psql")
    if which:
        return which
    msg = (
        "psql not found on PATH. Install PostgreSQL client tools or set PSQL_EXE "
        "to the full path of psql.exe (see apply_procedures.ps1)."
    )
    raise FileNotFoundError(msg)


def _asyncpg_server_settings(database_url: str) -> dict[str, str]:
    """Match app/e2e search_path: tables live in schema mythos_*; default public would miss zone_configurations."""
    db_name = database_url.split("/")[-1].split("?")[0].strip()
    search_path = os.getenv("POSTGRES_SEARCH_PATH", db_name)
    return {"search_path": search_path}


_PSQL_KICK_OTHER_BACKENDS = (
    "SELECT pg_terminate_backend(pid) FROM pg_stat_activity "
    "WHERE datname = current_database()::name AND pid <> pg_backend_pid()"
)


def _psql_heartbeat_wait(proc: subprocess.Popen[str], phase: str) -> None:
    while True:
        try:
            _ = proc.wait(timeout=60)
            return
        except subprocess.TimeoutExpired:
            print(f"  ... psql still running ({phase}) ...", flush=True)


def _psql_exit_code_extra(exit_code: int) -> str:
    """Human hint when psql exits with code 3 (common for interrupt / server error)."""
    if exit_code != 3:
        return ""
    return (
        " This often means psql was interrupted (Ctrl+C) or the server reported an error; "
        + "re-run after fixing SQL or use a fresh DB."
    )


def _run_psql_file(
    database_url: str,
    sql_file: Path,
    *,
    kick_other_backends: bool,
    preamble: str,
    heartbeat_phase: str,
    failure_label: str,
) -> None:
    """Run a .sql file with psql (-q). Optionally kick competitors before -f (same session, no gap)."""
    host, port, user, password, dbname = _parse_pg_url_for_psql(database_url)
    psql_exe = _resolve_psql_executable()
    env = os.environ.copy()
    if password:
        env["PGPASSWORD"] = password
    cmd: list[str] = [
        psql_exe,
        "-q",
        "-h",
        host,
        "-p",
        str(port),
        "-U",
        user,
        "-d",
        dbname,
        "-v",
        "ON_ERROR_STOP=1",
    ]
    if kick_other_backends:
        cmd.extend(["-c", _PSQL_KICK_OTHER_BACKENDS])
    cmd.extend(["-f", str(sql_file.resolve())])
    print(preamble, flush=True)
    proc: subprocess.Popen[str] = subprocess.Popen(
        cmd, env=env, stdout=None, stderr=None, text=True
    )  # nosemgrep: python.lang.security.audit.dangerous-subprocess-use-tainted-env-args.dangerous-subprocess-use-tainted-env-args  # nosec B603: argv list + no shell; psql path from _resolve_psql_executable
    _psql_heartbeat_wait(proc, heartbeat_phase)
    if proc.returncode != 0:
        msg = f"psql failed on {failure_label} {sql_file} (exit {proc.returncode}).{_psql_exit_code_extra(proc.returncode)}"
        raise RuntimeError(msg)


def _apply_schema_with_psql(database_url: str, schema_file: Path) -> None:
    """Apply DDL using psql -f (reliable for large multi-statement dumps; avoids long silent asyncpg runs)."""
    _run_psql_file(
        database_url,
        schema_file,
        kick_other_backends=True,
        preamble=(
            "  Applying schema via psql (-q): disconnects other clients on this DB first, then DDL; "
            "heartbeat every 60s. Do not press Ctrl+C unless you mean to stop (partial DDL is unsafe)."
        ),
        heartbeat_phase="DDL in progress",
        failure_label="schema",
    )


def _load_dml_with_psql(database_url: str, dml_file: Path) -> None:
    """Load pg_dump-style DML (COPY ... FROM stdin) via psql; asyncpg cannot drive COPY stdin."""
    _run_psql_file(
        database_url,
        dml_file,
        kick_other_backends=True,
        preamble=(
            "  Loading DML via psql (-q): disconnects other clients first; pg_dump COPY format; heartbeat every 60s."
        ),
        heartbeat_phase="DML in progress",
        failure_label="DML",
    )


def _apply_schema(database_url: str, schema_file: Path) -> None:
    """Apply database schema from file via psql (not asyncpg.execute for full dumps)."""
    print(f"\nApplying schema from {schema_file}...")
    _apply_schema_with_psql(database_url, schema_file)
    print("  [OK] Schema applied successfully")


async def _print_final_table_counts(conn: asyncpg.Connection) -> None:
    """Print final table counts after loading."""
    print("\nFinal table counts:")
    zone_count = cast(int | None, await conn.fetchval("SELECT COUNT(*) FROM zones"))
    print(f"  Zones: {zone_count}")

    room_count = cast(int | None, await conn.fetchval("SELECT COUNT(*) FROM rooms"))
    print(f"  Rooms: {room_count}")

    holiday_count = cast(int | None, await conn.fetchval("SELECT COUNT(*) FROM calendar_holidays"))
    print(f"  Holidays: {holiday_count}")

    schedule_count = cast(int | None, await conn.fetchval("SELECT COUNT(*) FROM calendar_npc_schedules"))
    print(f"  Schedules: {schedule_count}")

    zone_config_count = cast(int | None, await conn.fetchval("SELECT COUNT(*) FROM zone_configurations"))
    print(f"  Zone Configurations: {zone_config_count}")


async def main():
    """Load world seed data and verify."""
    print("=" * 60)
    print("MYTHOSMUD WORLD SEED DATA LOADER")
    print("=" * 60)

    database_url, schema_file, dml_file = _validate_environment_and_files()

    # Convert asyncpg URL to connection params
    url = database_url.replace("postgresql+asyncpg://", "postgresql://")
    print(f"Database URL: {url[:50]}...")

    server_settings = _asyncpg_server_settings(database_url)
    conn = await asyncpg.connect(url, server_settings=server_settings)
    try:
        await _print_current_table_counts(conn)
    finally:
        await conn.close()

    # Close before psql DDL so Ctrl+C during psql does not leave this connection half-closed (CancelError on close).
    _apply_schema(database_url, schema_file)

    print(f"\nLoading DML from {dml_file}...")
    _load_dml_with_psql(database_url, dml_file)
    print("  [OK] DML loaded successfully")

    conn = await asyncpg.connect(url, server_settings=server_settings)
    try:
        await _print_final_table_counts(conn)

        print("\n" + "=" * 60)
        print("WORLD SEED DATA LOADING COMPLETE")
        print("=" * 60)

    finally:
        await conn.close()


if __name__ == "__main__":
    run(main)
