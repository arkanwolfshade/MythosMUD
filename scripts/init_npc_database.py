#!/usr/bin/env python3
"""
NPC Database Initialization Script

This script initializes the NPC database schema for production and test databases,
and populates test databases with seed data from the local database.

Usage:
    python scripts/init_npc_database.py [--test-only] [--prod-only] [--e2e-only] [--unit-only]
"""

import argparse
import sqlite3
import sys
from pathlib import Path


def get_npc_seed_data(local_db_path: Path):
    """Extract seed data from the local NPC database."""
    if not local_db_path.exists():
        print(f"  [WARNING] Local NPC database not found at {local_db_path}, skipping seed data")
        return None, None

    try:
        conn = sqlite3.connect(local_db_path)
        cursor = conn.cursor()

        # Get all NPC definitions
        cursor.execute("SELECT * FROM npc_definitions")
        npc_definitions = cursor.fetchall()

        # Get all NPC spawn rules
        cursor.execute("SELECT * FROM npc_spawn_rules")
        npc_spawn_rules = cursor.fetchall()

        conn.close()

        return npc_definitions, npc_spawn_rules
    except Exception as e:
        print(f"  [WARNING] Failed to read seed data from local database: {e}")
        return None, None


def populate_npc_data(conn, npc_definitions, npc_spawn_rules):
    """Populate the database with NPC seed data."""
    if npc_definitions is None or npc_spawn_rules is None:
        return

    cursor = conn.cursor()

    # Clear existing data (respecting foreign key constraints)
    cursor.execute("DELETE FROM npc_spawn_rules")
    cursor.execute("DELETE FROM npc_definitions")
    conn.commit()

    # Insert NPC definitions
    insert_def_sql = """
    INSERT INTO npc_definitions
    (id, name, description, npc_type, sub_zone_id, room_id, required_npc,
     max_population, spawn_probability, base_stats, behavior_config,
     ai_integration_stub, created_at, updated_at)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """
    cursor.executemany(insert_def_sql, npc_definitions)

    # Insert NPC spawn rules
    insert_rule_sql = """
    INSERT INTO npc_spawn_rules
    (id, npc_definition_id, sub_zone_id, min_players, max_players, spawn_conditions)
    VALUES (?, ?, ?, ?, ?, ?)
    """
    cursor.executemany(insert_rule_sql, npc_spawn_rules)

    conn.commit()
    print(f"  [OK] Populated {len(npc_definitions)} NPC definitions")
    print(f"  [OK] Populated {len(npc_spawn_rules)} NPC spawn rules")


def init_database_schema(database_path: str, database_name: str, populate_seed: bool = False) -> bool:
    """
    Initialize a database with the NPC schema.

    Args:
        database_path: The path to the SQLite database file
        database_name: Human-readable name for logging
        populate_seed: Whether to populate with seed data from local database

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

            print(f"  [OK] Successfully initialized {database_name} database")
            print(f"  [OK] Created tables: {', '.join(table_names)}")

            # Populate with seed data if requested
            if populate_seed:
                local_db_path = Path(__file__).parent.parent / "data" / "local" / "npcs" / "local_npcs.db"
                npc_definitions, npc_spawn_rules = get_npc_seed_data(local_db_path)
                populate_npc_data(conn, npc_definitions, npc_spawn_rules)

            return True

        finally:
            conn.close()

    except Exception as e:
        print(f"[ERROR] Error initializing {database_name} database: {e}")
        return False


def main():
    """Main function to initialize NPC database schema."""
    parser = argparse.ArgumentParser(description="Initialize NPC database schema")
    parser.add_argument("--test-only", action="store_true", help="Only initialize test databases")
    parser.add_argument("--prod-only", action="store_true", help="Only initialize production database")
    parser.add_argument("--e2e-only", action="store_true", help="Only initialize e2e test database")
    parser.add_argument("--unit-only", action="store_true", help="Only initialize unit test database")

    args = parser.parse_args()

    # Determine which databases to initialize
    if args.e2e_only:
        init_e2e = True
        init_unit = False
        init_prod = False
    elif args.unit_only:
        init_e2e = False
        init_unit = True
        init_prod = False
    elif args.test_only:
        init_e2e = True
        init_unit = True
        init_prod = False
    elif args.prod_only:
        init_e2e = False
        init_unit = False
        init_prod = True
    else:
        # Default: initialize all
        init_e2e = True
        init_unit = True
        init_prod = True

    success = True

    # Initialize e2e test database
    if init_e2e:
        e2e_db_path = "data/e2e_test/npcs/e2e_npcs.db"
        success &= init_database_schema(e2e_db_path, "e2e_test", populate_seed=True)

    # Initialize unit test database
    if init_unit:
        unit_db_path = "data/unit_test/npcs/unit_test_npcs.db"
        success &= init_database_schema(unit_db_path, "unit_test", populate_seed=True)

    # Initialize local/production database (no seed data needed - this is the source)
    if init_prod:
        prod_db_path = "data/local/npcs/local_npcs.db"
        success &= init_database_schema(prod_db_path, "local", populate_seed=False)

    if success:
        print("\n[SUCCESS] All databases initialized successfully!")
        sys.exit(0)
    else:
        print("\n[ERROR] Some databases failed to initialize!")
        sys.exit(1)


if __name__ == "__main__":
    main()
