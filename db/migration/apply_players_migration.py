#!/usr/bin/env python3
"""
Apply players table migration to align with SQLAlchemy model.
This script applies the migration using Python/asyncpg instead of requiring psql.
"""

import asyncio
import sys
from pathlib import Path

import asyncpg

# Default connection parameters
DEFAULT_HOST = "localhost"
DEFAULT_PORT = 5432
DEFAULT_USER = "postgres"
DEFAULT_PASSWORD = "Cthulhu1"

DATABASES = ["mythos_dev", "mythos_unit", "mythos_e2e"]


async def apply_migration(db_name: str, host: str, port: int, user: str, password: str) -> bool:
    """Apply migration to a single database."""
    print(f"\n[INFO] Applying migration to database: {db_name}")

    try:
        # Connect to database
        conn = await asyncpg.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            database=db_name
        )

        try:
            # Read migration SQL file
            script_dir = Path(__file__).parent
            migration_file = script_dir / "migrate_players_to_correct_schema.sql"

            if not migration_file.exists():
                print(f"[ERROR] Migration file not found: {migration_file}")
                return False

            migration_sql = migration_file.read_text(encoding="utf-8")

            # Execute migration
            print("   Executing migration SQL...")
            await conn.execute(migration_sql)

            print(f"[OK] Migration applied successfully to {db_name}")
            return True

        finally:
            await conn.close()

    except asyncpg.exceptions.InvalidCatalogNameError:
        print(f"[WARN] Database {db_name} does not exist. Skipping...")
        return True  # Not an error, just skip
    except Exception as e:
        print(f"[ERROR] Migration failed for {db_name}: {e}")
        return False


async def main():
    """Main function."""
    import argparse

    parser = argparse.ArgumentParser(description="Apply players table migration")
    parser.add_argument(
        "--database",
        "-d",
        default="all",
        help="Database to migrate (mythos_dev, mythos_unit, mythos_e2e, or 'all')"
    )
    parser.add_argument("--host", default=DEFAULT_HOST, help="PostgreSQL host")
    parser.add_argument("--port", type=int, default=DEFAULT_PORT, help="PostgreSQL port")
    parser.add_argument("--user", "-U", default=DEFAULT_USER, help="PostgreSQL user")
    parser.add_argument("--password", "-P", default=DEFAULT_PASSWORD, help="PostgreSQL password")

    args = parser.parse_args()

    # Determine which databases to migrate
    if args.database.lower() == "all":
        databases = DATABASES
    else:
        databases = [args.database]

    # Apply migration to each database
    success = True
    for db in databases:
        result = await apply_migration(
            db,
            args.host,
            args.port,
            args.user,
            args.password
        )
        if not result:
            success = False

    if success:
        print("\n[SUCCESS] All migrations completed successfully!")
        return 0
    else:
        print("\n[ERROR] Some migrations failed!")
        return 1


if __name__ == "__main__":
    sys.exit(asyncio.run(main()))
