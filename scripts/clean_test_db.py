#!/usr/bin/env python3
"""
Clean test database by deleting all rows from the players table.

As noted in the restricted archives of Miskatonic University, maintaining
clean test data is essential for reproducible test results and preventing
the corruption of temporal signatures between test runs.
"""

import os
import sqlite3
from pathlib import Path


def clean_test_database():
    """Clean the test database by deleting all rows from the players table."""
    # Use environment variable for test database path - require it to be set
    test_db_url = os.getenv("DATABASE_URL")
    if not test_db_url:
        raise ValueError(
            "DATABASE_URL environment variable must be set. See server/env.example for configuration template."
        )

    if test_db_url.startswith("sqlite+aiosqlite:///"):
        test_db_path = Path(test_db_url.replace("sqlite+aiosqlite:///", ""))
    else:
        raise ValueError(f"Unsupported database URL format: {test_db_url}")

    if not test_db_path.exists():
        print(f"Warning: Test database not found at {test_db_path}")
        return

    try:
        # Connect to the test database
        conn = sqlite3.connect(test_db_path)
        cursor = conn.cursor()

        # Check if the players table exists
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='players'")
        if not cursor.fetchone():
            print("Warning: Players table not found in test database")
            conn.close()
            return

        # Get the count of rows before deletion
        cursor.execute("SELECT COUNT(*) FROM players")
        row_count = cursor.fetchone()[0]

        if row_count == 0:
            print("Info: Players table is already empty")
        else:
            # Delete all rows from the players table
            cursor.execute("DELETE FROM players")
            conn.commit()
            print(f"Deleted {row_count} rows from players table")

        conn.close()
        print("Test database cleaned successfully")

    except sqlite3.Error as e:
        print(f"Error cleaning test database: {e}")
        return False
    except Exception as e:
        print(f"Unexpected error: {e}")
        return False

    return True


if __name__ == "__main__":
    print("Cleaning test database...")
    success = clean_test_database()
    if not success:
        exit(1)
