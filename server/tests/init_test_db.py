#!/usr/bin/env python3
"""
Initialize test database with schema and test player data.

This script creates a SQLite database using the DATABASE_URL environment
variable with the same schema as the production database and populates it with
test player data.
"""

import os
import sqlite3
from pathlib import Path

# Get test database path from environment variable - require it to be set
DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise ValueError(
        "DATABASE_URL environment variable must be set. See server/env.example for configuration template."
    )

# Extract file path from SQLite URL
if DATABASE_URL.startswith("sqlite+aiosqlite:///"):
    db_path = DATABASE_URL.replace("sqlite+aiosqlite:///", "")
    # Handle relative paths by resolving from project root
    if db_path.startswith("./"):
        db_path = db_path[2:]  # Remove "./"

    # Resolve the path relative to the project root to prevent directory duplication
    project_root = Path(__file__).parent.parent.parent  # Go up to MythosMUD root
    TEST_DB_PATH = project_root / db_path
else:
    raise ValueError(f"Unsupported database URL format: {DATABASE_URL}")

# Load the production schema
SCHEMA_PATH = Path(__file__).parent.parent / "sql" / "schema.sql"

# Test database path
TEST_DB_PATH = Path(__file__).parent / "data" / "players" / "test_players.db"

# Room data paths
ROOMS_DIR = Path(__file__).parent / "data" / "rooms"


def load_schema():
    """Load the production database schema."""
    if SCHEMA_PATH.exists():
        return SCHEMA_PATH.read_text()
    else:
        # Fallback schema if the file doesn't exist
        return SCHEMA


# Database schema (same as production)
SCHEMA = (
    "-- Users table for authentication\n"
    "CREATE TABLE IF NOT EXISTS users (\n"
    "    user_id TEXT PRIMARY KEY NOT NULL,\n"
    "    email TEXT UNIQUE NOT NULL,\n"
    "    username TEXT UNIQUE NOT NULL,\n"
    "    hashed_password TEXT NOT NULL,\n"
    "    is_active BOOLEAN NOT NULL DEFAULT 1,\n"
    "    is_superuser BOOLEAN NOT NULL DEFAULT 0,\n"
    "    is_verified BOOLEAN NOT NULL DEFAULT 0,\n"
    "    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,\n"
    "    updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP\n"
    ");\n"
    "\n"
    "-- Players table for game data\n"
    "CREATE TABLE IF NOT EXISTS players (\n"
    "    player_id TEXT PRIMARY KEY NOT NULL,\n"
    "    user_id TEXT NOT NULL UNIQUE,\n"
    "    name TEXT UNIQUE NOT NULL,\n"
    '    stats TEXT NOT NULL DEFAULT \'{"health": 100, "sanity": 100, "strength": 10}\',\n'
    "    inventory TEXT NOT NULL DEFAULT '[]',\n"
    "    status_effects TEXT NOT NULL DEFAULT '[]',\n"
    "    current_room_id TEXT NOT NULL DEFAULT 'earth_arkham_city_intersection_derby_high',\n"
    "    experience_points INTEGER NOT NULL DEFAULT 0,\n"
    "    level INTEGER NOT NULL DEFAULT 1,\n"
    "    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,\n"
    "    last_active DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,\n"
    "    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE\n"
    ");\n"
    "\n"
    "-- Invites table for invite-only registration\n"
    "CREATE TABLE IF NOT EXISTS invites (\n"
    "    id TEXT PRIMARY KEY NOT NULL,\n"
    "    invite_code TEXT UNIQUE NOT NULL,\n"
    "    created_by_user_id TEXT,\n"
    "    used_by_user_id TEXT,\n"
    "    used BOOLEAN NOT NULL DEFAULT 0,\n"
    "    expires_at DATETIME,\n"
    "    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,\n"
    "    FOREIGN KEY (created_by_user_id) REFERENCES users(user_id) ON DELETE SET NULL,\n"
    "    FOREIGN KEY (used_by_user_id) REFERENCES users(user_id) ON DELETE SET NULL\n"
    ");\n"
    "\n"
    "-- Create indexes for better performance\n"
    "CREATE INDEX IF NOT EXISTS idx_users_username ON users(username);\n"
    "CREATE INDEX IF NOT EXISTS idx_players_name ON players(name);\n"
    "CREATE INDEX IF NOT EXISTS idx_players_user_id ON players(user_id);\n"
    "CREATE INDEX IF NOT EXISTS idx_invites_code ON invites(invite_code);\n"
    "CREATE INDEX IF NOT EXISTS idx_invites_used_by_user_id ON invites(used_by_user_id);\n"
)


# Sample test user data
SAMPLE_USERS = [
    {
        "user_id": "test-user-1",
        "email": "test1@example.com",
        "username": "test1",
        "hashed_password": "hashed_password_1",
        "is_active": True,
        "is_superuser": False,
        "is_verified": True,
    },
    {
        "user_id": "test-user-2",
        "email": "test2@example.com",
        "username": "test2",
        "hashed_password": "hashed_password_2",
        "is_active": True,
        "is_superuser": False,
        "is_verified": True,
    },
]

# Sample test player data
SAMPLE_PLAYERS = [
    {
        "player_id": "test-player-1",
        "user_id": "test-user-1",
        "name": "TestPlayer1",
        "stats": '{"health": 100, "sanity": 100, "strength": 12, "dexterity": 14, "constitution": 10, "intelligence": 16, "wisdom": 8, "charisma": 10, "occult_knowledge": 0, "fear": 0, "corruption": 0, "cult_affiliation": 0}',
        "inventory": "[]",
        "status_effects": "[]",
        "current_room_id": "earth_arkham_city_intersection_derby_high",
        "experience_points": 0,
        "level": 1,
    },
    {
        "player_id": "test-player-2",
        "user_id": "test-user-2",
        "name": "TestPlayer2",
        "stats": '{"health": 100, "sanity": 85, "strength": 10, "dexterity": 12, "constitution": 14, "intelligence": 10, "wisdom": 16, "charisma": 8, "occult_knowledge": 5, "fear": 15, "corruption": 0, "cult_affiliation": 0}',
        "inventory": "[]",
        "status_effects": "[]",
        "current_room_id": "arkham_002",
        "experience_points": 100,
        "level": 2,
    },
]

# Sample test invite data
SAMPLE_INVITES = [
    {
        "id": "test-invite-1",
        "invite_code": "TEST123",
        "created_by_user_id": "test-user-1",
        "used_by_user_id": None,
        "used": False,
        "expires_at": "2025-12-31 23:59:59",
        "created_at": "2024-01-01 00:00:00",
    },
    {
        "id": "test-invite-2",
        "invite_code": "TEST456",
        "created_by_user_id": "test-user-1",
        "used_by_user_id": None,
        "used": False,
        "expires_at": "2025-12-31 23:59:59",
        "created_at": "2024-01-01 00:00:00",
    },
]


def init_test_database():
    """Initialize the test database with schema and test data."""
    print(f"Initializing test database at: {TEST_DB_PATH}")

    # Ensure the data directory exists
    TEST_DB_PATH.parent.mkdir(parents=True, exist_ok=True)

    # Create database and schema
    with sqlite3.connect(TEST_DB_PATH) as conn:
        conn.executescript(load_schema())
        conn.commit()

    print("✓ Database schema created")

    # Insert sample test players into database
    with sqlite3.connect(TEST_DB_PATH) as conn:
        for user_data in SAMPLE_USERS:
            conn.execute(
                """
                INSERT OR REPLACE INTO users (
                    user_id, email, username, hashed_password, is_active, is_superuser, is_verified
                ) VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
                (
                    user_data["user_id"],
                    user_data["email"],
                    user_data["username"],
                    user_data["hashed_password"],
                    user_data["is_active"],
                    user_data["is_superuser"],
                    user_data["is_verified"],
                ),
            )

        for player_data in SAMPLE_PLAYERS:
            conn.execute(
                """
                INSERT OR REPLACE INTO players (
                    player_id, user_id, name, stats, inventory, status_effects,
                    current_room_id, experience_points, level
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
                (
                    player_data["player_id"],
                    player_data["user_id"],
                    player_data["name"],
                    player_data["stats"],
                    player_data["inventory"],
                    player_data["status_effects"],
                    player_data["current_room_id"],
                    player_data["experience_points"],
                    player_data["level"],
                ),
            )

        conn.commit()

    print(f"✓ Loaded {len(SAMPLE_PLAYERS)} sample test players")

    # Insert sample test invites into database
    with sqlite3.connect(TEST_DB_PATH) as conn:
        for invite_data in SAMPLE_INVITES:
            conn.execute(
                """
                INSERT OR REPLACE INTO invites (
                    id, invite_code, created_by_user_id, used_by_user_id, used, expires_at, created_at
                ) VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
                (
                    invite_data["id"],
                    invite_data["invite_code"],
                    invite_data["created_by_user_id"],
                    invite_data["used_by_user_id"],
                    invite_data["used"],
                    invite_data["expires_at"],
                    invite_data["created_at"],
                ),
            )

        conn.commit()

    print(f"✓ Loaded {len(SAMPLE_INVITES)} sample test invites")

    # Verify the database was created successfully
    with sqlite3.connect(TEST_DB_PATH) as conn:
        cursor = conn.execute("SELECT COUNT(*) FROM users")
        user_count = cursor.fetchone()[0]
        print(f"✓ Test database contains {user_count} users")

        cursor = conn.execute("SELECT COUNT(*) FROM players")
        player_count = cursor.fetchone()[0]
        print(f"✓ Test database contains {player_count} players")

        cursor = conn.execute("SELECT COUNT(*) FROM invites")
        invite_count = cursor.fetchone()[0]
        print(f"✓ Test database contains {invite_count} invites")

    print("✓ Test database initialization complete!")


if __name__ == "__main__":
    init_test_database()
