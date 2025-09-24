#!/usr/bin/env python3
"""
MythosMUD Database Initialization Script

Python script to create and initialize both production and test databases
with FastAPI Users v14 compatible schema.
"""

import asyncio
import os
import shutil
from datetime import datetime
from pathlib import Path

import aiosqlite

# Schema SQL for FastAPI Users v14 compatibility
SCHEMA_SQL = """
-- MythosMUD Database Schema
-- SQLite DDL for users, players, professions, and invites tables
-- Users table for authentication (FastAPI Users v14 compatible)
CREATE TABLE IF NOT EXISTS users (
    id TEXT PRIMARY KEY NOT NULL,
    -- UUID as TEXT for SQLite compatibility
    email TEXT UNIQUE NOT NULL,
    username TEXT UNIQUE NOT NULL,
    hashed_password TEXT NOT NULL,
    is_active BOOLEAN NOT NULL DEFAULT 1,
    is_superuser BOOLEAN NOT NULL DEFAULT 0,
    is_verified BOOLEAN NOT NULL DEFAULT 0,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- Professions table for character professions
CREATE TABLE IF NOT EXISTS professions (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL UNIQUE,
    description TEXT NOT NULL,
    flavor_text TEXT NOT NULL,
    stat_requirements TEXT NOT NULL, -- JSON: {"strength": 12, "intelligence": 10}
    mechanical_effects TEXT NOT NULL, -- JSON: future bonuses/penalties
    is_available BOOLEAN NOT NULL DEFAULT 1
);

-- Insert MVP professions (Tramp and Gutter Rat)
INSERT OR IGNORE INTO professions (id, name, description, flavor_text, stat_requirements, mechanical_effects) VALUES
(0, 'Tramp', 'A wandering soul with no fixed abode', 'You have learned to survive on the streets, finding shelter where you can and making do with what you have.', '{}', '{}'),
(1, 'Gutter Rat', 'A street-smart survivor of the urban underbelly', 'You know the hidden passages and dark corners of the city, where others fear to tread.', '{}', '{}');

-- Players table for game data
CREATE TABLE IF NOT EXISTS players (
    player_id TEXT PRIMARY KEY NOT NULL,
    user_id TEXT NOT NULL UNIQUE,
    name TEXT UNIQUE NOT NULL,
    stats TEXT NOT NULL DEFAULT '{"health": 100, "sanity": 100, "strength": 10}',
    inventory TEXT NOT NULL DEFAULT '[]',
    status_effects TEXT NOT NULL DEFAULT '[]',
    current_room_id TEXT NOT NULL DEFAULT 'earth_arkham_city_intersection_derby_high',
    experience_points INTEGER NOT NULL DEFAULT 0,
    level INTEGER NOT NULL DEFAULT 1,
    profession_id INTEGER NOT NULL DEFAULT 0,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    last_active DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY (profession_id) REFERENCES professions(id)
);

-- Invites table for invite-only registration
CREATE TABLE IF NOT EXISTS invites (
    id TEXT PRIMARY KEY NOT NULL,
    invite_code TEXT UNIQUE NOT NULL,
    created_by_user_id TEXT,
    used_by_user_id TEXT,
    used BOOLEAN NOT NULL DEFAULT 0,
    expires_at DATETIME,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (created_by_user_id) REFERENCES users(id) ON DELETE SET NULL,
    FOREIGN KEY (used_by_user_id) REFERENCES users(id) ON DELETE SET NULL
);

-- Create indexes for better performance
CREATE INDEX IF NOT EXISTS idx_users_username ON users(username);
CREATE INDEX IF NOT EXISTS idx_users_email ON users(email);
CREATE INDEX IF NOT EXISTS idx_professions_available ON professions(is_available);
CREATE INDEX IF NOT EXISTS idx_players_name ON players(name);
CREATE INDEX IF NOT EXISTS idx_players_user_id ON players(user_id);
CREATE INDEX IF NOT EXISTS idx_players_profession_id ON players(profession_id);
CREATE INDEX IF NOT EXISTS idx_invites_code ON invites(invite_code);
CREATE INDEX IF NOT EXISTS idx_invites_used_by_user_id ON invites(used_by_user_id);
"""


async def init_database(db_path: str, db_name: str):
    """Initialize a database with the schema."""
    print(f"Initializing {db_name} database: {db_path}")

    # Create backup if database exists
    if os.path.exists(db_path):
        print(f"⚠️  {db_name} database already exists. Backing up...")
        backup_path = f"{db_path}.backup.{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        shutil.copy2(db_path, backup_path)
        print(f"✓ Backup created: {backup_path}")

    # Create database directory if it doesn't exist
    os.makedirs(os.path.dirname(db_path), exist_ok=True)

    # Initialize database with schema
    async with aiosqlite.connect(db_path) as db:
        # Drop existing tables
        await db.execute("DROP TABLE IF EXISTS invites")
        await db.execute("DROP TABLE IF EXISTS players")
        await db.execute("DROP TABLE IF EXISTS users")

        # Create schema
        for statement in SCHEMA_SQL.split(";"):
            statement = statement.strip()
            if statement:
                await db.execute(statement)

        await db.commit()

    print(f"✓ {db_name} database initialized successfully")


async def verify_database(db_path: str, db_name: str):
    """Verify database schema."""
    print(f"\n{db_name} database verification:")

    async with aiosqlite.connect(db_path) as db:
        # Check tables
        cursor = await db.execute("SELECT name FROM sqlite_master WHERE type='table'")
        tables = await cursor.fetchall()
        print(f"Tables: {[table[0] for table in tables]}")

        # Check users table schema
        cursor = await db.execute("PRAGMA table_info(users)")
        columns = await cursor.fetchall()
        print(f"Users table columns: {[col[1] for col in columns]}")


async def main():
    """Main initialization function."""
    print("Initializing MythosMUD databases...")

    # Define database paths
    script_dir = Path(__file__).parent
    project_root = script_dir.parent.parent
    prod_db = project_root / "data" / "players" / "players.db"
    test_db = script_dir / "tests" / "data" / "players" / "test_players.db"

    try:
        # Initialize production database
        await init_database(str(prod_db), "Production")

        # Initialize test database
        await init_database(str(test_db), "Test")

        # Verify both databases
        print("\nVerifying database schemas...")
        await verify_database(str(prod_db), "Production")
        await verify_database(str(test_db), "Test")

        print("\n🎉 Database initialization completed successfully!")
        print("Both databases now contain: users, players, invites tables")
        print("✓ FastAPI Users v14 compatible schema with UUID primary keys")
        print("✓ Bogus email generation system ready for privacy protection")

    except Exception as e:
        print(f"❌ Database initialization failed: {e}")
        return 1

    return 0


if __name__ == "__main__":
    exit_code = asyncio.run(main())
    exit(exit_code)
