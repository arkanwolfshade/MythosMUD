"""
NPC Test database initialization for MythosMUD.

This module provides functions to initialize the test database specifically
for NPC testing scenarios.
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


def init_npc_test_database():
    """Initialize the NPC test database with schema and test data."""

    # NPC Test database path
    NPC_TEST_DB_PATH = Path(__file__).parent / "data" / "npcs" / "test_npcs.db"

    print(f"Initializing NPC test database at: {NPC_TEST_DB_PATH}")

    # Ensure the data directory exists
    NPC_TEST_DB_PATH.parent.mkdir(parents=True, exist_ok=True)

    # Create database and schema
    with sqlite3.connect(NPC_TEST_DB_PATH) as conn:
        conn.execute("PRAGMA foreign_keys = ON")
        conn.executescript(load_npc_schema())
        conn.commit()

    print("✓ NPC Database schema created")
    print("✓ NPC Test database initialization completed successfully")


if __name__ == "__main__":
    init_npc_test_database()
