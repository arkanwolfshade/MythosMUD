#!/usr/bin/env python3
"""
MythosMUD NPC Database Migration Script
Applies the rename_players_to_population migration to NPC databases
This renames min_players/max_players to min_population/max_population in npc_spawn_rules
"""

import argparse
import shutil
import sqlite3
import sys
from datetime import datetime
from pathlib import Path


def check_schema(cursor: sqlite3.Cursor) -> str:
    """Check current schema of npc_spawn_rules table"""
    cursor.execute("PRAGMA table_info(npc_spawn_rules);")
    columns = cursor.fetchall()
    column_names = [col[1] for col in columns]

    if "min_players" in column_names:
        return "old"
    elif "min_population" in column_names:
        return "new"
    else:
        return "unknown"


def apply_migration(db_path: Path) -> bool:
    """Apply the migration to rename columns"""
    migration_sql = """
-- Create temporary table with new column names
CREATE TABLE npc_spawn_rules_new (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    npc_definition_id INTEGER NOT NULL,
    sub_zone_id TEXT NOT NULL,
    min_population INTEGER DEFAULT 0 NOT NULL,
    max_population INTEGER DEFAULT 999 NOT NULL,
    spawn_conditions TEXT NOT NULL DEFAULT '{}',
    FOREIGN KEY (npc_definition_id) REFERENCES npc_definitions(id) ON DELETE CASCADE
);

-- Copy data from old table to new table
INSERT INTO npc_spawn_rules_new (id, npc_definition_id, sub_zone_id, min_population, max_population, spawn_conditions)
SELECT id, npc_definition_id, sub_zone_id, min_players, max_players, spawn_conditions
FROM npc_spawn_rules;

-- Drop old table
DROP TABLE npc_spawn_rules;

-- Rename new table to old table name
ALTER TABLE npc_spawn_rules_new RENAME TO npc_spawn_rules;

-- Recreate indexes
CREATE INDEX IF NOT EXISTS idx_npc_spawn_rules_sub_zone ON npc_spawn_rules(sub_zone_id);
CREATE INDEX IF NOT EXISTS idx_npc_spawn_rules_npc_def ON npc_spawn_rules(npc_definition_id);
"""

    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.executescript(migration_sql)
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print(f"Error applying migration: {e}")
        return False


def main():
    parser = argparse.ArgumentParser(description="Migrate NPC database schema")
    parser.add_argument(
        "--environment",
        "-e",
        default="local",
        choices=["local", "e2e_test", "unit_test"],
        help="Environment to migrate (default: local)"
    )
    args = parser.parse_args()

    print("=== MythosMUD NPC Database Migration ===")
    print("Applying rename_players_to_population migration")
    print()

    # Determine database path based on environment
    db_paths = {
        "local": Path("data/local/npcs/local_npcs.db"),
        "e2e_test": Path("data/e2e_test/npcs/e2e_test_npcs.db"),
        "unit_test": Path("data/unit_test/npcs/unit_test_npcs.db"),
    }

    db_path = db_paths[args.environment]

    # Check if database exists
    if not db_path.exists():
        print(f"[ERROR] Database not found: {db_path}")
        sys.exit(1)

    print(f"[OK] Found database: {db_path}")

    # Create backup
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = db_path.with_suffix(f".db.backup.{timestamp}")
    shutil.copy2(db_path, backup_path)
    print(f"[OK] Backup created: {backup_path}")

    # Check current schema
    print()
    print("Checking current schema...")
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    schema_status = check_schema(cursor)
    conn.close()

    if schema_status == "old":
        print("[OK] Found old schema with min_players/max_players columns")
    elif schema_status == "new":
        print("[WARNING] Database already has min_population/max_population columns")
        print("Migration may have already been applied")
        response = input("Continue anyway? (y/n): ")
        if response.lower() != "y":
            print("Migration cancelled")
            sys.exit(0)
    else:
        print("[ERROR] npc_spawn_rules table not found or has unexpected schema")
        sys.exit(1)

    # Apply migration
    print()
    print("Applying migration...")
    if not apply_migration(db_path):
        print("[ERROR] Migration failed")
        print("Restoring from backup...")
        shutil.copy2(backup_path, db_path)
        print("[OK] Database restored from backup")
        sys.exit(1)

    print("[OK] Migration applied successfully")

    # Verify new schema
    print()
    print("Verifying new schema...")
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    schema_status = check_schema(cursor)
    conn.close()

    if schema_status == "new":
        print("[OK] Schema verified: min_population/max_population columns present")
    else:
        print("[ERROR] Schema verification failed")
        print("Restoring from backup...")
        shutil.copy2(backup_path, db_path)
        print("[OK] Database restored from backup")
        sys.exit(1)

    print()
    print("=== Migration Complete ===")
    print(f"Backup retained at: {backup_path}")


if __name__ == "__main__":
    main()
