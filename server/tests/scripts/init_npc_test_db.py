"""
NPC Test database initialization for MythosMUD.

This module provides functions to initialize the test database specifically
for NPC testing scenarios with schema and seed data from the local database.
"""

import sqlite3
from pathlib import Path


def load_npc_schema():
    """Load the NPC test database schema from SQL files."""

    # Get the project root directory (go up from server/tests to project root)
    project_root = Path(__file__).parent.parent.parent
    schema_file = project_root / "server" / "sql" / "npc_schema.sql"

    if not schema_file.exists():
        raise FileNotFoundError(f"NPC Schema file not found: {schema_file}")

    with open(schema_file, encoding="utf-8") as f:
        return f.read()


def get_npc_seed_data():
    """Extract seed data from the local NPC database."""
    project_root = Path(__file__).parent.parent.parent
    local_db = project_root / "data" / "local" / "npcs" / "local_npcs.db"

    if not local_db.exists():
        print(f"  [WARNING] Local NPC database not found at {local_db}, skipping seed data")
        return None, None

    try:
        conn = sqlite3.connect(local_db)
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
    (id, npc_definition_id, sub_zone_id, min_population, max_population, spawn_conditions)
    VALUES (?, ?, ?, ?, ?, ?)
    """
    cursor.executemany(insert_rule_sql, npc_spawn_rules)

    conn.commit()
    print(f"  [OK] Populated {len(npc_definitions)} NPC definitions")
    print(f"  [OK] Populated {len(npc_spawn_rules)} NPC spawn rules")


def init_npc_test_database():
    """Initialize the NPC test database with schema and test data."""

    # NPC Test database path - use project root relative path
    project_root = Path(__file__).parent.parent.parent
    NPC_TEST_DB_PATH = project_root / "data" / "unit_test" / "npcs" / "unit_test_npcs.db"

    print(f"Initializing NPC test database at: {NPC_TEST_DB_PATH}")

    # Ensure the data directory exists
    NPC_TEST_DB_PATH.parent.mkdir(parents=True, exist_ok=True)

    # Create database and schema
    with sqlite3.connect(NPC_TEST_DB_PATH) as conn:
        conn.execute("PRAGMA foreign_keys = ON")
        conn.executescript(load_npc_schema())
        conn.commit()
        print("  [OK] NPC Database schema created")

        # Populate with seed data from local database
        npc_definitions, npc_spawn_rules = get_npc_seed_data()
        populate_npc_data(conn, npc_definitions, npc_spawn_rules)

    print("[OK] NPC Test database initialization completed successfully")


if __name__ == "__main__":
    init_npc_test_database()
