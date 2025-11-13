#!/usr/bin/env python3
"""Verify the test database was created correctly."""

import os
import sqlite3
from pathlib import Path

# Use environment variable for test database path - require it to be set
TEST_DATABASE_URL = os.getenv("DATABASE_URL")
if not TEST_DATABASE_URL:
    raise ValueError(
        "DATABASE_URL environment variable must be set. See server/env.example for configuration template."
    )

if TEST_DATABASE_URL.startswith("sqlite+aiosqlite:///"):
    TEST_DB_PATH = Path(TEST_DATABASE_URL.replace("sqlite+aiosqlite:///", ""))
else:
    raise ValueError(f"Unsupported database URL format: {TEST_DATABASE_URL}")


def verify_test_database():
    """Verify the test database contains the expected data."""
    if not TEST_DB_PATH.exists():
        print("❌ Test database not found!")
        return

    print(f"✓ Test database found at: {TEST_DB_PATH}")

    with sqlite3.connect(TEST_DB_PATH) as conn:
        # Check tables exist
        cursor = conn.execute("SELECT name FROM sqlite_master WHERE type='table'")
        tables = [row[0] for row in cursor.fetchall()]
        print(f"✓ Tables found: {tables}")
        if "player_inventories" not in tables:
            print("❌ player_inventories table missing!")
            return

        # Check player data
        cursor = conn.execute("SELECT name, current_room_id FROM players")
        players = cursor.fetchall()
        print(f"✓ Players found: {len(players)}")
        for name, room_id in players:
            print(f"  - {name} in {room_id}")

        # Ensure player inventories present for each player
        cursor = conn.execute("SELECT COUNT(*) FROM player_inventories")
        inventory_rows = cursor.fetchone()[0]
        print(f"✓ player_inventories rows: {inventory_rows}")
        if inventory_rows != len(players):
            print("❌ player_inventories row count mismatch!")
            return
        cursor = conn.execute("SELECT inventory_json, equipped_json FROM player_inventories LIMIT 1")
        row = cursor.fetchone()
        if row:
            print(f"  Sample inventory payloads: inventory={row[0]}, equipped={row[1]}")

        # Check schema
        cursor = conn.execute("PRAGMA table_info(players)")
        columns = [row[1] for row in cursor.fetchall()]
        print(f"✓ Player table columns: {columns}")


if __name__ == "__main__":
    verify_test_database()
