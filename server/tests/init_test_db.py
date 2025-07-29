#!/usr/bin/env python3
"""
Initialize test database with schema and test player data.

This script creates a SQLite database in server/tests/data/ with the same schema
as the production database and populates it with test player data.
"""

import json
import sqlite3
from datetime import datetime
from pathlib import Path

# Test database path
TEST_DB_PATH = Path(__file__).parent / "data" / "players" / "test_players.db"

# Room data paths
ROOMS_DIR = Path(__file__).parent.parent.parent / "data" / "rooms"

# Database schema (same as production)
SCHEMA = """
CREATE TABLE IF NOT EXISTS players (
    id TEXT PRIMARY KEY,
    name TEXT UNIQUE NOT NULL,
    strength INTEGER,
    dexterity INTEGER,
    constitution INTEGER,
    intelligence INTEGER,
    wisdom INTEGER,
    charisma INTEGER,
    sanity INTEGER,
    occult_knowledge INTEGER,
    fear INTEGER,
    corruption INTEGER,
    cult_affiliation INTEGER,
    current_room_id TEXT,
    created_at TEXT,
    last_active TEXT,
    experience_points INTEGER,
    level INTEGER
);

CREATE TABLE IF NOT EXISTS rooms (
    id TEXT PRIMARY KEY,
    name TEXT,
    description TEXT,
    exits TEXT,
    zone TEXT
);
"""

# Sample test player data
SAMPLE_PLAYERS = [
    {
        "id": "test-player-1",
        "name": "TestPlayer1",
        "strength": 12,
        "dexterity": 14,
        "constitution": 10,
        "intelligence": 16,
        "wisdom": 8,
        "charisma": 10,
        "sanity": 100,
        "occult_knowledge": 0,
        "fear": 0,
        "corruption": 0,
        "cult_affiliation": 0,
        "current_room_id": "arkham_001",
        "created_at": datetime.utcnow().isoformat(),
        "last_active": datetime.utcnow().isoformat(),
        "experience_points": 0,
        "level": 1,
    },
    {
        "id": "test-player-2",
        "name": "TestPlayer2",
        "strength": 10,
        "dexterity": 12,
        "constitution": 14,
        "intelligence": 10,
        "wisdom": 16,
        "charisma": 8,
        "sanity": 85,
        "occult_knowledge": 5,
        "fear": 15,
        "corruption": 0,
        "cult_affiliation": 0,
        "current_room_id": "arkham_002",
        "created_at": datetime.utcnow().isoformat(),
        "last_active": datetime.utcnow().isoformat(),
        "experience_points": 100,
        "level": 2,
    },
]


def load_room_data():
    """Load room data from JSON files into the database."""
    room_count = 0

    if not ROOMS_DIR.exists():
        print(f"⚠ Rooms directory not found: {ROOMS_DIR}")
        return room_count

    with sqlite3.connect(TEST_DB_PATH) as conn:
        # Load rooms from each zone directory
        for zone_dir in ROOMS_DIR.iterdir():
            if zone_dir.is_dir():
                print(f"Loading rooms from zone: {zone_dir.name}")

                for room_file in zone_dir.glob("*.json"):
                    try:
                        with open(room_file, encoding="utf-8") as f:
                            room_data = json.load(f)

                        # Insert room into database
                        conn.execute(
                            """
                            INSERT OR REPLACE INTO rooms (
                                id, name, description, exits, zone
                            ) VALUES (?, ?, ?, ?, ?)
                            """,
                            (
                                room_data["id"],
                                room_data["name"],
                                room_data["description"],
                                json.dumps(room_data["exits"]),  # Store exits as JSON string
                                room_data["zone"],
                            ),
                        )
                        room_count += 1
                        print(f"  ✓ Loaded room: {room_data['name']} ({room_data['id']})")

                    except Exception as e:
                        print(f"  ✗ Failed to load room {room_file}: {e}")

        conn.commit()

    return room_count


def init_test_database():
    """Initialize the test database with schema and test data."""
    print(f"Initializing test database at: {TEST_DB_PATH}")

    # Ensure the data directory exists
    TEST_DB_PATH.parent.mkdir(parents=True, exist_ok=True)

    # Create database and schema
    with sqlite3.connect(TEST_DB_PATH) as conn:
        conn.executescript(SCHEMA)
        conn.commit()

    print("✓ Database schema created")

    # Load room data from JSON files
    room_count = load_room_data()
    print(f"✓ Loaded {room_count} rooms from JSON files")

    # Insert sample test players into database
    with sqlite3.connect(TEST_DB_PATH) as conn:
        for player_data in SAMPLE_PLAYERS:
            conn.execute(
                """
                INSERT OR REPLACE INTO players (
                    id, name, strength, dexterity, constitution, intelligence,
                    wisdom, charisma, sanity, occult_knowledge, fear, corruption,
                    cult_affiliation, current_room_id, created_at, last_active,
                    experience_points, level
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
                (
                    player_data["id"],
                    player_data["name"],
                    player_data["strength"],
                    player_data["dexterity"],
                    player_data["constitution"],
                    player_data["intelligence"],
                    player_data["wisdom"],
                    player_data["charisma"],
                    player_data["sanity"],
                    player_data["occult_knowledge"],
                    player_data["fear"],
                    player_data["corruption"],
                    player_data["cult_affiliation"],
                    player_data["current_room_id"],
                    player_data["created_at"],
                    player_data["last_active"],
                    player_data["experience_points"],
                    player_data["level"],
                ),
            )

        conn.commit()

    print(f"✓ Loaded {len(SAMPLE_PLAYERS)} sample test players")

    # Verify the database was created successfully
    with sqlite3.connect(TEST_DB_PATH) as conn:
        cursor = conn.execute("SELECT COUNT(*) FROM players")
        player_count = cursor.fetchone()[0]
        print(f"✓ Test database contains {player_count} players")

        cursor = conn.execute("SELECT COUNT(*) FROM rooms")
        room_count = cursor.fetchone()[0]
        print(f"✓ Test database contains {room_count} rooms")

    print("✓ Test database initialization complete!")


if __name__ == "__main__":
    init_test_database()
