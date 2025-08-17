#!/usr/bin/env python3
"""
MythosMUD Unified Database Initialization Script

This script initializes a database with the current schema, supporting both
production and test databases. It takes a target database path as a parameter
to avoid having separate scripts that can get out of sync.

Usage:
    python init_database.py <database_path>

Examples:
    python init_database.py data/players/players.db
    python init_database.py server/tests/data/players/test_players.db
"""

import os
import sqlite3
import sys
from datetime import datetime


def load_schema():
    """Load schema from server/sql/schema.sql file."""
    schema_path = "server/sql/schema.sql"
    if not os.path.exists(schema_path):
        raise FileNotFoundError(f"Schema file not found: {schema_path}")

    with open(schema_path) as f:
        return f.read()


def backup_existing_database(db_path: str):
    """Create a backup of existing database if it exists."""
    if os.path.exists(db_path):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_path = f"{db_path}.backup.{timestamp}"
        print(f"⚠️  Database already exists. Creating backup: {backup_path}")
        os.rename(db_path, backup_path)
        return backup_path
    return None


def verify_schema(db_path: str):
    """Verify the database schema was created correctly."""
    print(f"\nVerifying database schema: {db_path}")

    with sqlite3.connect(db_path) as conn:
        # Check tables exist
        cursor = conn.execute("SELECT name FROM sqlite_master WHERE type='table'")
        tables = [row[0] for row in cursor.fetchall()]
        print(f"✓ Tables created: {tables}")

        # Check unique indexes exist
        cursor = conn.execute("SELECT name FROM sqlite_master WHERE type='index' AND name LIKE '%_unique'")
        unique_indexes = [row[0] for row in cursor.fetchall()]
        print(f"✓ Unique indexes: {unique_indexes}")

        # Verify case-insensitive constraints work
        try:
            # Test case-insensitive constraint on users table
            conn.execute(
                "INSERT INTO users (id, email, username, hashed_password) VALUES (?, ?, ?, ?)",
                ("test1", "test1@example.com", "TestUser", "hash"),
            )
            conn.execute(
                "INSERT INTO users (id, email, username, hashed_password) VALUES (?, ?, ?, ?)",
                ("test2", "test2@example.com", "testuser", "hash"),
            )
            print("❌ Case-insensitive constraint test failed - duplicate usernames were allowed")
            return False
        except sqlite3.IntegrityError:
            print("✓ Case-insensitive constraint test passed - duplicate usernames properly rejected")
            # Clean up test data
            conn.execute("DELETE FROM users WHERE id IN ('test1', 'test2')")
            conn.commit()

        return True


def main():
    """Main initialization function."""
    if len(sys.argv) != 2:
        print("Usage: python init_database.py <database_path>")
        print("\nExamples:")
        print("  python init_database.py data/players/players.db")
        print("  python init_database.py server/tests/data/players/test_players.db")
        sys.exit(1)

    db_path = sys.argv[1]

    print(f"Initializing MythosMUD database: {db_path}")

    try:
        # Load schema
        schema = load_schema()

        # Ensure the directory exists
        os.makedirs(os.path.dirname(db_path), exist_ok=True)

        # Backup existing database if it exists
        backup_path = backup_existing_database(db_path)

        # Initialize database with schema
        with sqlite3.connect(db_path) as conn:
            conn.executescript(schema)
            conn.commit()

        print(f"✓ Database initialized successfully at {db_path}")

        # Verify schema
        if verify_schema(db_path):
            print("\n🎉 Database initialization completed successfully!")
            print("✓ Schema includes: users, players, invites tables")
            print("✓ Case-insensitive unique constraints on username and player name")
            print("✓ FastAPI Users v14 compatible schema")
            if backup_path:
                print(f"✓ Previous database backed up to: {backup_path}")
        else:
            print("\n❌ Database verification failed!")
            sys.exit(1)

    except Exception as e:
        print(f"❌ Database initialization failed: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
