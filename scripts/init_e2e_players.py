#!/usr/bin/env python3
"""
E2E Test Database Initialization Script

This script initializes the E2E test database with test players for multiplayer scenarios.
It creates ArkanWolfshade (admin) and Ithaqua (regular player) with known credentials
for predictable test execution.

Usage:
    python scripts/init_e2e_players.py
"""

import sqlite3
import sys
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    from passlib.context import CryptContext
except ImportError:
    print("ERROR: passlib not installed. Install with: pip install passlib[argon2]")
    sys.exit(1)

# E2E test database path (matches .env.e2e_test configuration)
E2E_DB_PATH = project_root / "data" / "e2e_test" / "players.db"

# Password hashing context matching production configuration
pwd_context = CryptContext(
    schemes=["argon2"],
    deprecated="auto",
    argon2__memory_cost=65536,
    argon2__time_cost=3,
    argon2__parallelism=4,
)

# Test players configuration (using proper UUIDs)
TEST_PLAYERS = [
    {
        "user_id": "e2e00000-0000-0000-0000-000000000001",
        "player_id": "e2e10000-0000-0000-0000-000000000001",
        "username": "ArkanWolfshade",
        "email": "arkan@e2e.test",
        "password": "Cthulhu1",
        "is_admin": True,
        "is_superuser": False,
    },
    {
        "user_id": "e2e00000-0000-0000-0000-000000000002",
        "player_id": "e2e10000-0000-0000-0000-000000000002",
        "username": "Ithaqua",
        "email": "ithaqua@e2e.test",
        "password": "Cthulhu1",
        "is_admin": False,
        "is_superuser": False,
    },
]

# Default player stats
DEFAULT_STATS = {
    "strength": 10,
    "dexterity": 10,
    "constitution": 10,
    "intelligence": 10,
    "wisdom": 10,
    "charisma": 10,
    "sanity": 100,
    "occult_knowledge": 0,
    "fear": 0,
    "corruption": 0,
    "cult_affiliation": 0,
    "current_health": 100,
}

# Starting room
STARTING_ROOM = "earth_arkhamcity_sanitarium_room_foyer_001"


def initialize_e2e_database():
    """Initialize the E2E test database with schema and test players."""
    print("\n[E2E DB INIT] Initializing E2E Test Database")
    print(f"Database: {E2E_DB_PATH}")

    # Ensure database directory exists
    E2E_DB_PATH.parent.mkdir(parents=True, exist_ok=True)

    # First, initialize the database schema using the existing init_database script
    print("\n[SCHEMA] Creating database schema...")
    import subprocess

    result = subprocess.run(
        [sys.executable, str(project_root / "scripts" / "init_database.py"), str(E2E_DB_PATH)],
        capture_output=True,
        text=True,
    )

    if result.returncode != 0:
        print("[ERROR] Failed to create database schema:")
        print(result.stderr)
        sys.exit(1)

    print("[OK] Database schema created")

    # Now add test players
    print("\n[PLAYERS] Creating test players...")
    with sqlite3.connect(E2E_DB_PATH) as conn:
        for player_config in TEST_PLAYERS:
            # Hash password
            hashed_password = pwd_context.hash(player_config["password"])

            # Insert user
            conn.execute(
                """
                INSERT OR REPLACE INTO users
                (id, email, username, hashed_password, is_active, is_superuser, is_verified)
                VALUES (?, ?, ?, ?, 1, ?, 1)
                """,
                (
                    player_config["user_id"],
                    player_config["email"],
                    player_config["username"],
                    hashed_password,
                    1 if player_config["is_superuser"] else 0,
                ),
            )

            # Insert player
            import json

            stats_json = json.dumps(DEFAULT_STATS)

            conn.execute(
                """
                INSERT OR REPLACE INTO players
                (player_id, user_id, name, stats, inventory, status_effects,
                 current_room_id, experience_points, level, is_admin)
                VALUES (?, ?, ?, ?, '[]', '[]', ?, 0, 1, ?)
                """,
                (
                    player_config["player_id"],
                    player_config["user_id"],
                    player_config["username"],
                    stats_json,
                    STARTING_ROOM,
                    1 if player_config["is_admin"] else 0,
                ),
            )

            role = "Admin" if player_config["is_admin"] else "Player"
            print(f"  [OK] Created {player_config['username']} ({role})")

        conn.commit()

    # Verify the database
    print("\n[VERIFY] Verifying database...")
    with sqlite3.connect(E2E_DB_PATH) as conn:
        # Check users
        cursor = conn.execute("SELECT username, is_active FROM users ORDER BY username")
        users = cursor.fetchall()
        print(f"\n  Users ({len(users)}):")
        for username, is_active in users:
            status = "Active" if is_active else "Inactive"
            print(f"    - {username} ({status})")

        # Check players
        cursor = conn.execute("SELECT name, current_room_id, is_admin FROM players ORDER BY name")
        players = cursor.fetchall()
        print(f"\n  Players ({len(players)}):")
        for name, room_id, is_admin in players:
            role = "Admin" if is_admin else "Regular"
            print(f"    - {name} ({role}) in {room_id}")

    print("\n" + "=" * 60)
    print("[SUCCESS] E2E Test Database Initialized Successfully!")
    print("=" * 60)
    print("\nTest Players:")
    for player_config in TEST_PLAYERS:
        role = "Admin" if player_config["is_admin"] else "Regular Player"
        print(f"  - Username: {player_config['username']}")
        print(f"    Password: {player_config['password']}")
        print(f"    Role: {role}")
        print()

    print(f"Database Location: {E2E_DB_PATH}")
    print(f"Starting Room: {STARTING_ROOM}")
    print("\nYou can now run E2E tests using these credentials.")


if __name__ == "__main__":
    try:
        initialize_e2e_database()
    except Exception as e:
        print(f"\n[ERROR] Error initializing E2E database: {e}")
        import traceback

        traceback.print_exc()
        sys.exit(1)
