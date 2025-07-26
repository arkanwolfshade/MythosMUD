#!/usr/bin/env python3
"""
Initialize test database with schema and test player data.

This script creates a SQLite database in server/tests/data/ with the same schema
as the production database and populates it with test player data from the JSON file.
"""

import sqlite3
import json
from datetime import datetime
from pathlib import Path

# Test database path
TEST_DB_PATH = Path(__file__).parent / "data" / "test_players.db"
TEST_JSON_PATH = Path(__file__).parent / "data" / "players.json"

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

    # Load test player data from JSON
    if TEST_JSON_PATH.exists():
        with open(TEST_JSON_PATH, "r", encoding="utf-8") as f:
            test_players = json.load(f)

        # Insert test players into database
        with sqlite3.connect(TEST_DB_PATH) as conn:
            for player_id, player_data in test_players.items():
                # Extract stats from the nested structure
                stats = player_data.get("stats", {})

                # Prepare player data for database insertion
                db_player = {
                    "id": player_data["id"],
                    "name": player_data["name"],
                    "strength": stats.get("strength", 10),
                    "dexterity": stats.get("dexterity", 10),
                    "constitution": stats.get("constitution", 10),
                    "intelligence": stats.get("intelligence", 10),
                    "wisdom": stats.get("wisdom", 10),
                    "charisma": stats.get("charisma", 10),
                    "sanity": stats.get("sanity", 100),
                    "occult_knowledge": stats.get("occult_knowledge", 0),
                    "fear": stats.get("fear", 0),
                    "corruption": stats.get("corruption", 0),
                    "cult_affiliation": stats.get("cult_affiliation", 0),
                    "current_room_id": player_data.get("current_room_id", "arkham_001"),
                    "created_at": player_data.get(
                        "created_at", datetime.utcnow().isoformat()
                    ),
                    "last_active": player_data.get(
                        "last_active", datetime.utcnow().isoformat()
                    ),
                    "experience_points": player_data.get("experience_points", 0),
                    "level": player_data.get("level", 1),
                }

                # Insert player into database
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
                        db_player["id"],
                        db_player["name"],
                        db_player["strength"],
                        db_player["dexterity"],
                        db_player["constitution"],
                        db_player["intelligence"],
                        db_player["wisdom"],
                        db_player["charisma"],
                        db_player["sanity"],
                        db_player["occult_knowledge"],
                        db_player["fear"],
                        db_player["corruption"],
                        db_player["cult_affiliation"],
                        db_player["current_room_id"],
                        db_player["created_at"],
                        db_player["last_active"],
                        db_player["experience_points"],
                        db_player["level"],
                    ),
                )

            conn.commit()

        print(f"✓ Loaded {len(test_players)} test players from JSON")
    else:
        print("⚠ No test players JSON file found")

    # Verify the database was created successfully
    with sqlite3.connect(TEST_DB_PATH) as conn:
        cursor = conn.execute("SELECT COUNT(*) FROM players")
        player_count = cursor.fetchone()[0]
        print(f"✓ Test database contains {player_count} players")

    print("✓ Test database initialization complete!")


if __name__ == "__main__":
    init_test_database()
