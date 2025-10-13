#!/usr/bin/env python3
"""
Populate Test NPC Databases

This script populates the e2e_test and unit_test NPC databases with the same
data that exists in the local NPC database.

Usage:
    python scripts/populate_test_npc_databases.py
"""

import sqlite3
import sys
from pathlib import Path


def get_npc_data_from_local():
    """Extract NPC data from the local database."""
    local_db = Path("data/local/npcs/local_npcs.db")

    if not local_db.exists():
        print(f"[ERROR] Local NPC database not found: {local_db}")
        return None, None

    print(f"Reading data from {local_db}...")

    conn = sqlite3.connect(local_db)
    cursor = conn.cursor()

    # Get all NPC definitions
    cursor.execute("SELECT * FROM npc_definitions")
    npc_definitions = cursor.fetchall()

    # Get all NPC spawn rules
    cursor.execute("SELECT * FROM npc_spawn_rules")
    npc_spawn_rules = cursor.fetchall()

    conn.close()

    print(f"  Found {len(npc_definitions)} NPC definitions")
    print(f"  Found {len(npc_spawn_rules)} NPC spawn rules")

    return npc_definitions, npc_spawn_rules


def populate_database(db_path: Path, npc_definitions, npc_spawn_rules):
    """Populate a database with NPC data."""
    print(f"\nPopulating {db_path}...")

    if not db_path.exists():
        print(f"  [ERROR] Database file not found: {db_path}")
        return False

    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # Clear existing data
        cursor.execute("DELETE FROM npc_spawn_rules")
        cursor.execute("DELETE FROM npc_definitions")

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
        conn.close()

        print(f"  [OK] Inserted {len(npc_definitions)} NPC definitions")
        print(f"  [OK] Inserted {len(npc_spawn_rules)} NPC spawn rules")
        return True

    except Exception as e:
        print(f"  [ERROR] Failed to populate database: {e}")
        return False


def main():
    """Main function to populate test NPC databases."""
    print("=" * 60)
    print("Populating Test NPC Databases")
    print("=" * 60)

    # Get data from local database
    npc_definitions, npc_spawn_rules = get_npc_data_from_local()

    if npc_definitions is None or npc_spawn_rules is None:
        print("\n[ERROR] Failed to read data from local database!")
        sys.exit(1)

    # Populate e2e_test database
    # CRITICAL: Use approved database location per DATABASE PLACEMENT RULES
    e2e_db = Path("data/e2e_test/npcs/e2e_test_npcs.db")
    e2e_success = populate_database(e2e_db, npc_definitions, npc_spawn_rules)

    # Populate unit_test database
    unit_db = Path("data/unit_test/npcs/unit_test_npcs.db")
    unit_success = populate_database(unit_db, npc_definitions, npc_spawn_rules)

    print("\n" + "=" * 60)
    if e2e_success and unit_success:
        print("[SUCCESS] All test databases populated successfully!")
        sys.exit(0)
    else:
        print("[ERROR] Some databases failed to populate!")
        sys.exit(1)


if __name__ == "__main__":
    main()
