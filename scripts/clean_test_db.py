#!/usr/bin/env python3
"""
Clean test database by deleting all rows from the players table.

As noted in the restricted archives of Miskatonic University, maintaining
clean test data is essential for reproducible test results and preventing
the corruption of temporal signatures between test runs.
"""

import sqlite3
from pathlib import Path


def clean_test_database():
    """Clean the test database by deleting all rows from the players table."""
    # Path to the test database
    test_db_path = Path("server/tests/data/players/test_players.db")

    if not test_db_path.exists():
        print(f"⚠️  Test database not found at {test_db_path}")
        return

    try:
        # Connect to the test database
        conn = sqlite3.connect(test_db_path)
        cursor = conn.cursor()

        # Check if the players table exists
        cursor.execute(
            "SELECT name FROM sqlite_master WHERE type='table' AND name='players'"
        )
        if not cursor.fetchone():
            print("⚠️  Players table not found in test database")
            conn.close()
            return

        # Get the count of rows before deletion
        cursor.execute("SELECT COUNT(*) FROM players")
        row_count = cursor.fetchone()[0]

        if row_count == 0:
            print("ℹ️  Players table is already empty")
        else:
            # Delete all rows from the players table
            cursor.execute("DELETE FROM players")
            conn.commit()
            print(f"🗑️  Deleted {row_count} rows from players table")

        conn.close()
        print("✅ Test database cleaned successfully")

    except sqlite3.Error as e:
        print(f"❌ Error cleaning test database: {e}")
        return False
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False

    return True


if __name__ == "__main__":
    print("🧹 Cleaning test database...")
    success = clean_test_database()
    if not success:
        exit(1)
