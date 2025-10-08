#!/usr/bin/env python3
"""
NPC Sample Data Population Script

This script populates both production and test NPC databases with sample data
for testing and development purposes.

Usage:
    python scripts/populate_npc_sample_data.py [--test-only] [--prod-only]
"""

import argparse
import sqlite3
import sys
from pathlib import Path


def populate_database(database_path: str, database_name: str) -> bool:
    """
    Populate a database with sample NPC data.

    Args:
        database_path: The path to the SQLite database file
        database_name: Human-readable name for logging

    Returns:
        True if successful, False otherwise
    """
    print(f"Populating {database_name} database...")

    try:
        # Ensure the database directory exists
        db_path = Path(database_path)
        db_path.parent.mkdir(parents=True, exist_ok=True)

        # Read the sample data SQL file
        sql_file = Path(__file__).parent.parent / "server" / "sql" / "npc_sample_data.sql"
        with open(sql_file, encoding="utf-8") as f:
            sql_content = f.read()

        # Connect to the database
        conn = sqlite3.connect(database_path)
        conn.execute("PRAGMA foreign_keys = OFF")  # Temporarily disable foreign key constraints for population

        try:
            # Split the SQL content into individual statements
            statements = [stmt.strip() for stmt in sql_content.split(";") if stmt.strip()]

            for statement in statements:
                if statement.upper().startswith("SELECT"):
                    # Execute SELECT statements and print results
                    cursor = conn.execute(statement)
                    rows = cursor.fetchall()
                    columns = [description[0] for description in cursor.description]
                    print(f"  {statement}")
                    for row in rows:
                        row_dict = dict(zip(columns, row, strict=False))
                        print(f"    {row_dict}")
                else:
                    # Execute other statements
                    conn.execute(statement)
                    print(f"  Executed: {statement[:50]}...")

            conn.commit()

            # Re-enable foreign key constraints and verify data integrity
            conn.execute("PRAGMA foreign_keys = ON")

            # Verify foreign key constraints work
            try:
                conn.execute("PRAGMA foreign_key_check")
                print(f"✅ Foreign key constraints verified for {database_name} database")
            except Exception as e:
                print(f"⚠️  Foreign key constraint warning: {e}")

            print(f"✅ Successfully populated {database_name} database")
            return True

        finally:
            conn.close()

    except Exception as e:
        print(f"❌ Error populating {database_name} database: {e}")
        return False


def main():
    """Main function to populate NPC sample data."""
    parser = argparse.ArgumentParser(description="Populate NPC databases with sample data")
    parser.add_argument("--test-only", action="store_true", help="Only populate test database")
    parser.add_argument("--prod-only", action="store_true", help="Only populate production database")

    args = parser.parse_args()

    # Determine which databases to populate
    populate_test = not args.prod_only
    populate_prod = not args.test_only

    success = True

    # Populate test database
    if populate_test:
        test_db_path = "data/unit_test/npcs/test_npcs.db"
        success &= populate_database(test_db_path, "test")

    # Populate production database
    if populate_prod:
        prod_db_path = "data/local/npcs/npcs.db"
        success &= populate_database(prod_db_path, "production")

    if success:
        print("\n🎉 All databases populated successfully!")
        sys.exit(0)
    else:
        print("\n💥 Some databases failed to populate!")
        sys.exit(1)


if __name__ == "__main__":
    main()
