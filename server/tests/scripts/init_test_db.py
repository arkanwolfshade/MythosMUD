#!/usr/bin/env python3
"""
Test database initialization for MythosMUD.

DEPRECATED: This script is for SQLite initialization only.
We now use PostgreSQL exclusively. SQLite databases have been removed.

This module is kept for reference only and should not be used.
All test data is now stored in PostgreSQL via SQLAlchemy models.
"""

from pathlib import Path

# DEPRECATED: This script is no longer functional
# Test databases are now managed via PostgreSQL SQL schema files in db/schema/

# Test database path - use project root relative path
# from server/tests/scripts -> server/tests -> server -> project_root
# NOTE: This script is deprecated - we now use PostgreSQL exclusively.
project_root = Path(__file__).parent.parent.parent.parent
TEST_DB_PATH = project_root / "data" / "unit_test" / "players" / "unit_test_players.db"

# Test database schema is now loaded from db/schema/ SQL files


def load_schema():
    """
    Load the test database schema from SQL files.

    DEPRECATED: This function is no longer used.
    Database schema is now defined in db/schema/ SQL files.
    """
    raise DeprecationWarning(
        "This function is deprecated. Database schema is now managed via PostgreSQL SQL files in db/schema/"
    )


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
        "stats": '{"health": 100, "sanity": 100, "strength": 12, "dexterity": 14, "constitution": 10, "intelligence": 16, "wisdom": 8, "charisma": 10, "occult_knowledge": 0, "fear": 0, "corruption": 0, "cult_affiliation": 0, "position": "standing"}',
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
        "stats": '{"health": 100, "sanity": 85, "strength": 10, "dexterity": 12, "constitution": 14, "intelligence": 10, "wisdom": 16, "charisma": 8, "occult_knowledge": 5, "fear": 15, "corruption": 0, "cult_affiliation": 0, "position": "standing"}',
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
    """
    Initialize the test database with schema and test data.

    DEPRECATED: This function is no longer used.
    Test databases are now PostgreSQL databases initialized via db/schema/ SQL files.
    """
    print(
        "[DEPRECATED] init_test_database() is deprecated. "
        "Test databases are now PostgreSQL databases managed via db/schema/ SQL files."
    )
    print(
        "To initialize test database, use PostgreSQL SQL schema files in db/schema/ "
        "and ensure DATABASE_URL is set to a PostgreSQL URL."
    )
    raise DeprecationWarning("This function is deprecated. Use PostgreSQL SQL schema files in db/schema/ instead.")


if __name__ == "__main__":
    print(
        "[DEPRECATED] This script is deprecated. "
        "Test databases are now PostgreSQL databases managed via db/schema/ SQL files."
    )
    print("This script will not execute. Use PostgreSQL schema files instead.")
