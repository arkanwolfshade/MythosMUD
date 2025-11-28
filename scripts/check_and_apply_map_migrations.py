#!/usr/bin/env python3
"""
Check and apply map editor migrations to mythos_dev database.

This script verifies if migrations 013 and 014 have been applied,
and applies them if they haven't been.

Migrations:
- 013: Add map_x and map_y columns to rooms table
- 014: Create player_exploration table
"""

import os
import sys
from pathlib import Path

# Add server directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent / "server"))

import asyncio

from sqlalchemy import text
from sqlalchemy.ext.asyncio import create_async_engine

# Database connection from environment
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql+asyncpg://postgres:Cthulhu1@localhost:5432/mythos_dev")


async def check_migration_013(engine):
    """Check if migration 013 (map_x/map_y columns) has been applied."""
    async with engine.begin() as conn:
        result = await conn.execute(
            text("""
                SELECT column_name
                FROM information_schema.columns
                WHERE table_schema = 'public'
                    AND table_name = 'rooms'
                    AND column_name IN ('map_x', 'map_y')
            """)
        )
        columns = [row[0] for row in result.fetchall()]

        has_map_x = 'map_x' in columns
        has_map_y = 'map_y' in columns

        return has_map_x and has_map_y, columns


async def check_migration_014(engine):
    """Check if migration 014 (player_exploration table) has been applied."""
    async with engine.begin() as conn:
        result = await conn.execute(
            text("""
                SELECT table_name
                FROM information_schema.tables
                WHERE table_schema = 'public'
                    AND table_name = 'player_exploration'
            """)
        )
        tables = [row[0] for row in result.fetchall()]

        return 'player_exploration' in tables


async def apply_migration_013(engine):
    """Apply migration 013: Add map_x and map_y columns."""
    migration_file = Path(__file__).parent.parent / "db" / "migrations" / "013_add_map_coordinates_to_rooms.sql"

    if not migration_file.exists():
        print(f"[ERROR] Migration file not found: {migration_file}")
        return False

    print(f"[INFO] Reading migration file: {migration_file}")
    with open(migration_file, encoding='utf-8') as f:
        migration_sql = f.read()

    try:
        async with engine.begin() as conn:
            await conn.execute(text(migration_sql))
        print("[OK] Migration 013 applied successfully")
        return True
    except Exception as e:
        print(f"[ERROR] Failed to apply migration 013: {e}")
        return False


async def apply_migration_014(engine):
    """Apply migration 014: Create player_exploration table."""
    migration_file = Path(__file__).parent.parent / "db" / "migrations" / "014_create_player_exploration_table.sql"

    if not migration_file.exists():
        print(f"[ERROR] Migration file not found: {migration_file}")
        return False

    print(f"[INFO] Reading migration file: {migration_file}")
    with open(migration_file, encoding='utf-8') as f:
        migration_sql = f.read()

    try:
        async with engine.begin() as conn:
            await conn.execute(text(migration_sql))
        print("[OK] Migration 014 applied successfully")
        return True
    except Exception as e:
        print(f"[ERROR] Failed to apply migration 014: {e}")
        return False


async def main():
    """Main function to check and apply migrations."""
    print("=== MythosMUD Map Editor Migrations Check ===")
    print(f"Database: {DATABASE_URL.split('@')[-1] if '@' in DATABASE_URL else DATABASE_URL}")
    print()

    # Create database engine
    try:
        engine = create_async_engine(DATABASE_URL, echo=False)
    except Exception as e:
        print(f"[ERROR] Failed to create database engine: {e}")
        sys.exit(1)

    try:
        # Check migration 013
        print("Checking migration 013 (map_x/map_y columns)...")
        migration_013_applied, existing_columns = await check_migration_013(engine)

        if migration_013_applied:
            print("[OK] Migration 013 already applied (map_x and map_y columns exist)")
        else:
            print(f"[INFO] Migration 013 not applied (found columns: {existing_columns})")
            print("[INFO] Applying migration 013...")
            if await apply_migration_013(engine):
                print("[OK] Migration 013 completed")
            else:
                print("[ERROR] Migration 013 failed")
                sys.exit(1)

        print()

        # Check migration 014
        print("Checking migration 014 (player_exploration table)...")
        migration_014_applied = await check_migration_014(engine)

        if migration_014_applied:
            print("[OK] Migration 014 already applied (player_exploration table exists)")
        else:
            print("[INFO] Migration 014 not applied")
            print("[INFO] Applying migration 014...")
            if await apply_migration_014(engine):
                print("[OK] Migration 014 completed")
            else:
                print("[ERROR] Migration 014 failed")
                sys.exit(1)

        print()
        print("=== All migrations verified/applied successfully ===")

    except Exception as e:
        print(f"[ERROR] Unexpected error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
    finally:
        await engine.dispose()


if __name__ == "__main__":
    asyncio.run(main())
