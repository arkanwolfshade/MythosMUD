#!/usr/bin/env python3
"""
Test database initialization for MythosMUD.

This module provides utilities for setting up test databases with sample data.
"""

import sqlite3
from pathlib import Path

# Test database path
TEST_DB_PATH = Path(__file__).parent / "data" / "players" / "test_players.db"

# Test database schema is now loaded from server/sql/schema.sql


def load_schema():
    """Load the test database schema from SQL files."""
    from pathlib import Path

    # Get the project root directory (go up from server/tests to project root)
    project_root = Path(__file__).parent.parent.parent
    schema_file = project_root / "server" / "sql" / "schema.sql"

    if not schema_file.exists():
        raise FileNotFoundError(f"Schema file not found: {schema_file}")

    with open(schema_file, encoding="utf-8") as f:
        return f.read()


# Sample test user data
SAMPLE_USERS = [
    {
        "id": "test-user-1",
        "email": "test1@example.com",
        "username": "test1",
        "hashed_password": "hashed_password_1",
        "is_active": True,
        "is_superuser": False,
        "is_verified": True,
    },
    {
        "id": "test-user-2",
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
        "current_room_id": "earth_arkhamcity_intersection_derby_high",
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
        conn.execute("PRAGMA foreign_keys = ON")
        conn.executescript(load_schema())
        conn.commit()

    print("✓ Database schema created")

    # Insert sample test players into database
    with sqlite3.connect(TEST_DB_PATH) as conn:
        conn.execute("PRAGMA foreign_keys = ON")
        for user_data in SAMPLE_USERS:
            conn.execute(
                """
                INSERT OR REPLACE INTO users (
                    id, email, username, hashed_password, is_active, is_superuser, is_verified
                ) VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
                (
                    user_data["id"],
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

    print("✓ Test database initialization completed successfully")


if __name__ == "__main__":
    init_test_database()
