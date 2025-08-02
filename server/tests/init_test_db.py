#!/usr/bin/env python3
"""
Initialize test database with schema and test player data.

This script creates a SQLite database using the TEST_DATABASE_URL environment variable
with the same schema as the production database and populates it with test player data.
"""

import os
import sqlite3
from pathlib import Path

# Get test database path from environment variable
TEST_DATABASE_URL = os.getenv("TEST_DATABASE_URL", "sqlite+aiosqlite:///./tests/data/test_players.db")

# Extract file path from SQLite URL
if TEST_DATABASE_URL.startswith("sqlite+aiosqlite:///"):
    db_path = TEST_DATABASE_URL.replace("sqlite+aiosqlite:///", "")
    # Handle relative paths
    if db_path.startswith("./"):
        db_path = db_path[2:]  # Remove "./"
    TEST_DB_PATH = Path(db_path)
else:
    # Fallback to default location
    TEST_DB_PATH = Path(__file__).parent / "data" / "test_players.db"

# Load the production schema
SCHEMA_PATH = Path(__file__).parent.parent / "sql" / "schema.sql"


def load_schema():
    """Load the production database schema."""
    if SCHEMA_PATH.exists():
        return SCHEMA_PATH.read_text()
    else:
        # Fallback schema if the file doesn't exist
        return """
-- Users table for authentication
CREATE TABLE IF NOT EXISTS users (
    user_id TEXT PRIMARY KEY NOT NULL,
    email TEXT UNIQUE NOT NULL,
    hashed_password TEXT NOT NULL,
    is_active BOOLEAN NOT NULL DEFAULT 1,
    is_superuser BOOLEAN NOT NULL DEFAULT 0,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- Players table for game data
CREATE TABLE IF NOT EXISTS players (
    player_id TEXT PRIMARY KEY NOT NULL,
    user_id TEXT NOT NULL UNIQUE,
    name TEXT UNIQUE NOT NULL,
    stats TEXT NOT NULL DEFAULT '{"health": 100, "sanity": 100, "strength": 10}',
    inventory TEXT NOT NULL DEFAULT '[]',
    status_effects TEXT NOT NULL DEFAULT '[]',
    current_room_id TEXT NOT NULL DEFAULT 'arkham_001',
    experience_points INTEGER NOT NULL DEFAULT 0,
    level INTEGER NOT NULL DEFAULT 1,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    last_active DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
);

-- Invites table for invite-only registration
CREATE TABLE IF NOT EXISTS invites (
    id TEXT PRIMARY KEY NOT NULL,
    invite_code TEXT UNIQUE NOT NULL,
    used_by_user_id TEXT,
    is_used BOOLEAN NOT NULL DEFAULT 0,
    expires_at DATETIME,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (used_by_user_id) REFERENCES users(user_id) ON DELETE SET NULL
);

-- Create indexes for better performance
CREATE INDEX IF NOT EXISTS idx_users_email ON users(email);
CREATE INDEX IF NOT EXISTS idx_players_name ON players(name);
CREATE INDEX IF NOT EXISTS idx_players_user_id ON players(user_id);
CREATE INDEX IF NOT EXISTS idx_invites_code ON invites(invite_code);
CREATE INDEX IF NOT EXISTS idx_invites_used_by_user_id ON invites(used_by_user_id);
"""


# Sample test user data
SAMPLE_USERS = [
    {
        "user_id": "test-user-1",
        "email": "test1@example.com",
        "hashed_password": "hashed_password_1",
        "is_active": True,
        "is_superuser": False,
    },
    {
        "user_id": "test-user-2",
        "email": "test2@example.com",
        "hashed_password": "hashed_password_2",
        "is_active": True,
        "is_superuser": False,
    },
]

# Sample test player data
SAMPLE_PLAYERS = [
    {
        "player_id": "test-player-1",
        "user_id": "test-user-1",
        "name": "TestPlayer1",
        "stats": (
            '{"health": 100, "sanity": 100, "strength": 12, "dexterity": 14, '
            '"constitution": 10, "intelligence": 16, "wisdom": 8, "charisma": 10, '
            '"occult_knowledge": 0, "fear": 0, "corruption": 0, "cult_affiliation": 0}'
        ),
        "inventory": "[]",
        "status_effects": "[]",
        "current_room_id": "arkham_001",
        "experience_points": 0,
        "level": 1,
    },
    {
        "player_id": "test-player-2",
        "user_id": "test-user-2",
        "name": "TestPlayer2",
        "stats": (
            '{"health": 100, "sanity": 85, "strength": 10, "dexterity": 12, '
            '"constitution": 14, "intelligence": 10, "wisdom": 16, "charisma": 8, '
            '"occult_knowledge": 5, "fear": 15, "corruption": 0, "cult_affiliation": 0}'
        ),
        "inventory": "[]",
        "status_effects": "[]",
        "current_room_id": "arkham_002",
        "experience_points": 100,
        "level": 2,
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
                    user_id, email, hashed_password, is_active, is_superuser
                ) VALUES (?, ?, ?, ?, ?)
            """,
                (
                    user_data["user_id"],
                    user_data["email"],
                    user_data["hashed_password"],
                    user_data["is_active"],
                    user_data["is_superuser"],
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

    # Verify the database was created successfully
    with sqlite3.connect(TEST_DB_PATH) as conn:
        cursor = conn.execute("SELECT COUNT(*) FROM users")
        user_count = cursor.fetchone()[0]
        print(f"✓ Test database contains {user_count} users")

        cursor = conn.execute("SELECT COUNT(*) FROM players")
        player_count = cursor.fetchone()[0]
        print(f"✓ Test database contains {player_count} players")

    print("✓ Test database initialization complete!")


if __name__ == "__main__":
    init_test_database()
