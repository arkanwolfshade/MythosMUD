#!/usr/bin/env python3
"""
NPC Database Initialization Script

This script initializes the NPC database schema for both production and test databases.

Usage:
    python scripts/init_npc_database.py [--test-only] [--prod-only]
"""

import argparse
import sqlite3
import sys
from pathlib import Path


def init_database_schema(database_path: str, database_name: str) -> bool:
    """
    Initialize a database with the NPC schema.

    Args:
        database_path: The path to the SQLite database file
        database_name: Human-readable name for logging

    Returns:
        True if successful, False otherwise
    """
    print(f"Initializing {database_name} database schema...")

    try:
        # Ensure the database directory exists
        db_path = Path(database_path)
        db_path.parent.mkdir(parents=True, exist_ok=True)

        # Read the schema SQL file
        schema_file = Path(__file__).parent.parent / "server" / "sql" / "npc_schema.sql"
        with open(schema_file, encoding="utf-8") as f:
            schema_content = f.read()

        # Connect to the database
        conn = sqlite3.connect(database_path)
        conn.execute("PRAGMA foreign_keys = ON")  # Enable foreign key constraints

        try:
            # Execute the schema creation
            conn.executescript(schema_content)
            conn.commit()

            # Verify tables were created
            cursor = conn.execute("SELECT name FROM sqlite_master WHERE type='table' AND name LIKE 'npc_%'")
            tables = cursor.fetchall()
            table_names = [table[0] for table in tables]

            print(f"[OK] Successfully initialized {database_name} database")
            print(f"  Created tables: {', '.join(table_names)}")
            return True

        finally:
            conn.close()

    except Exception as e:
        print(f"[ERROR] Error initializing {database_name} database: {e}")
        return False


def main():
    """Main function to initialize NPC database schema."""
    parser = argparse.ArgumentParser(description="Initialize NPC database schema")
    parser.add_argument("--test-only", action="store_true", help="Only initialize test database")
    parser.add_argument("--prod-only", action="store_true", help="Only initialize production database")

    args = parser.parse_args()

    # Determine which databases to initialize
    init_test = not args.prod_only
    init_prod = not args.test_only

    success = True

    # Initialize test database
    if init_test:
        test_db_path = "data/unit_test/npcs/test_npcs.db"
        success &= init_database_schema(test_db_path, "test")

    # Initialize production database
    if init_prod:
        prod_db_path = "data/local/npcs/npcs.db"
        success &= init_database_schema(prod_db_path, "production")

    if success:
        print("\n[SUCCESS] All databases initialized successfully!")
        sys.exit(0)
    else:
        print("\n[ERROR] Some databases failed to initialize!")
        sys.exit(1)


if __name__ == "__main__":
    main()
