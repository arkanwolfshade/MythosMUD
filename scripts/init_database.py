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
    python init_database.py data/unit_test/players/unit_test_players.db
"""

import os
import sqlite3
import sys
from datetime import datetime

from server.logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)


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
        logger.warning("Database already exists, creating backup", backup_path=backup_path)
        os.rename(db_path, backup_path)
        return backup_path
    return None


def verify_schema(db_path: str):
    """Verify the database schema was created correctly."""
    logger.info("Verifying database schema", db_path=db_path)

    with sqlite3.connect(db_path) as conn:
        # Check tables exist
        cursor = conn.execute("SELECT name FROM sqlite_master WHERE type='table'")
        tables = [row[0] for row in cursor.fetchall()]
        logger.info("Tables created successfully", tables=tables)

        # Check unique indexes exist
        cursor = conn.execute("SELECT name FROM sqlite_master WHERE type='index' AND name LIKE '%_unique'")
        unique_indexes = [row[0] for row in cursor.fetchall()]
        logger.info("Unique indexes created", unique_indexes=unique_indexes)

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
            logger.error("Case-insensitive constraint test failed - duplicate usernames were allowed")
            return False
        except sqlite3.IntegrityError:
            logger.info("Case-insensitive constraint test passed - duplicate usernames properly rejected")
            # Clean up test data
            conn.execute("DELETE FROM users WHERE id IN ('test1', 'test2')")
            conn.commit()

        return True


def main():
    """Main initialization function."""
    if len(sys.argv) != 2:
        logger.error("Usage: python init_database.py <database_path>")
        logger.info("Examples:")
        logger.info("  python init_database.py data/local/players/local_players.db")
        logger.info("  python init_database.py data/unit_test/players/unit_test_players.db")
        sys.exit(1)

    db_path = sys.argv[1]

    logger.info("Initializing MythosMUD database", db_path=db_path)

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

        logger.info("Database initialized successfully", db_path=db_path)

        # Verify schema
        if verify_schema(db_path):
            logger.info("Database initialization completed successfully")
            logger.info("Schema includes: users, players, invites tables")
            logger.info("Case-insensitive unique constraints on username and player name")
            logger.info("FastAPI Users v14 compatible schema")
            if backup_path:
                logger.info("Previous database backed up", backup_path=backup_path)
        else:
            logger.error("Database verification failed")
            sys.exit(1)

    except Exception as e:
        logger.error("Database initialization failed", error=str(e), exc_info=True)
        sys.exit(1)


if __name__ == "__main__":
    main()
