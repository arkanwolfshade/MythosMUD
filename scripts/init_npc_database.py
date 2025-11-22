#!/usr/bin/env python3
"""
NPC Database Initialization Script

This script initializes the NPC database schema in PostgreSQL databases.

DEPRECATED: NPC databases are now managed via PostgreSQL SQL schema files in db/schema/.
This script is provided for backward compatibility but may be removed in the future.

Usage:
    python scripts/init_npc_database.py [--test-only] [--prod-only] [--e2e-only] [--unit-only]
"""

import argparse
import os
import sys
from pathlib import Path

from sqlalchemy import create_engine, text


def get_npc_database_url(environment: str = "default") -> str | None:
    """
    Get NPC database URL for the specified environment.

    Args:
        environment: Environment name ('test', 'e2e', 'unit', 'prod', or 'default')

    Returns:
        PostgreSQL database URL or None if not found
    """
    # Try environment-specific variables first
    env_var_map = {
        "test": "DATABASE_NPC_URL",
        "e2e": "DATABASE_NPC_URL",  # E2E uses same as test
        "unit": "DATABASE_NPC_URL",  # Unit uses same as test
        "prod": "DATABASE_NPC_URL",
        "default": "DATABASE_NPC_URL",
    }

    env_var = env_var_map.get(environment, "DATABASE_NPC_URL")
    npc_url = os.getenv(env_var) or os.getenv("NPC_DATABASE_URL") or os.getenv("DATABASE__NPC_URL")

    # Fallback: use main DATABASE_URL if NPC URL not set
    if not npc_url:
        npc_url = os.getenv("DATABASE_URL")

    if not npc_url or not npc_url.startswith("postgresql"):
        return None

    return npc_url


def get_npc_seed_data_from_postgresql(database_url: str):
    """
    Extract seed data from a PostgreSQL NPC database.

    DEPRECATED: NPC seed data is now managed via SQLAlchemy models and PostgreSQL.
    This function is provided for backward compatibility.

    Returns:
        Tuple of (npc_definitions, npc_spawn_rules) or (None, None) if unavailable
    """
    try:
        # Convert async URL to sync URL for create_engine
        sync_url = database_url.replace("+asyncpg", "")
        engine = create_engine(sync_url, echo=False)

        with engine.connect() as conn:
            # Get all NPC definitions
            result = conn.execute(text("SELECT * FROM npc_definitions"))
            npc_definitions = result.fetchall()
            # Get column names from result metadata (SQLAlchemy 2.0)
            try:
                column_names = list(result.keys())
            except AttributeError:
                # Fallback for older SQLAlchemy versions
                column_names = [desc[0] for desc in result.cursor.description]

            # Get all NPC spawn rules
            result = conn.execute(text("SELECT * FROM npc_spawn_rules"))
            npc_spawn_rules = result.fetchall()
            # Get column names from result metadata (SQLAlchemy 2.0)
            try:
                spawn_rule_columns = list(result.keys())
            except AttributeError:
                # Fallback for older SQLAlchemy versions
                spawn_rule_columns = [desc[0] for desc in result.cursor.description]

        return (npc_definitions, column_names), (npc_spawn_rules, spawn_rule_columns)
    except Exception as e:
        print(f"  [WARNING] Failed to read seed data from PostgreSQL database: {e}")
        return None, None


def populate_npc_data(engine, npc_data, npc_spawn_data):
    """
    Populate the database with NPC seed data.

    Args:
        engine: SQLAlchemy engine
        npc_data: Tuple of (npc_definitions rows, column_names)
        npc_spawn_data: Tuple of (npc_spawn_rules rows, column_names)
    """
    if npc_data is None or npc_spawn_data is None:
        return

    npc_definitions, def_columns = npc_data
    npc_spawn_rules, spawn_columns = npc_spawn_data

    with engine.connect() as conn:
        # Clear existing data (respecting foreign key constraints)
        conn.execute(text("DELETE FROM npc_spawn_rules"))
        conn.execute(text("DELETE FROM npc_definitions"))
        conn.commit()

        # Insert NPC definitions
        # Build INSERT statement dynamically based on columns
        if npc_definitions:
            placeholders = ", ".join([f":{col}" for col in def_columns])
            columns = ", ".join(def_columns)
            insert_def_sql = f"""
            INSERT INTO npc_definitions ({columns})
            VALUES ({placeholders})
            """

            # Convert rows to dictionaries
            for row in npc_definitions:
                row_dict = dict(zip(def_columns, row, strict=False))
                conn.execute(text(insert_def_sql), row_dict)
            conn.commit()

        # Insert NPC spawn rules
        if npc_spawn_rules:
            placeholders = ", ".join([f":{col}" for col in spawn_columns])
            columns = ", ".join(spawn_columns)
            insert_rule_sql = f"""
            INSERT INTO npc_spawn_rules ({columns})
            VALUES ({placeholders})
            """

            # Convert rows to dictionaries
            for row in npc_spawn_rules:
                row_dict = dict(zip(spawn_columns, row, strict=False))
                conn.execute(text(insert_rule_sql), row_dict)
            conn.commit()

        print(f"  [OK] Populated {len(npc_definitions) if npc_definitions else 0} NPC definitions")
        print(f"  [OK] Populated {len(npc_spawn_rules) if npc_spawn_rules else 0} NPC spawn rules")


def init_database_schema(database_url: str, database_name: str, populate_seed: bool = False) -> bool:
    """
    Initialize a PostgreSQL database with the NPC schema.

    Args:
        database_url: The PostgreSQL database URL
        database_name: Human-readable name for logging
        populate_seed: Whether to populate with seed data from another PostgreSQL database

    Returns:
        True if successful, False otherwise
    """
    print(f"Initializing {database_name} NPC database schema...")

    if not database_url or not database_url.startswith("postgresql"):
        print(f"  [ERROR] Invalid or missing PostgreSQL database URL for {database_name}")
        return False

    try:
        # Convert async URL to sync URL for create_engine
        sync_url = database_url.replace("+asyncpg", "")
        engine = create_engine(sync_url, echo=False)

        # Read the PostgreSQL schema file
        schema_file = Path(__file__).parent.parent / "db" / "schema" / "04_runtime_tables.sql"
        if not schema_file.exists():
            print(f"  [ERROR] Schema file not found: {schema_file}")
            return False

        with open(schema_file, encoding="utf-8") as f:
            schema_content = f.read()

        # Extract NPC-related schema (from "-- NPC Definitions" to end of NPC section)
        import re
        npc_schema_match = re.search(
            r"-- NPC Definitions.*?(?=--|\Z)",
            schema_content,
            re.IGNORECASE | re.DOTALL,
        )
        if not npc_schema_match:
            print(f"  [WARNING] NPC schema section not found in {schema_file}, using full schema")
            npc_schema = schema_content
        else:
            npc_schema = npc_schema_match.group(0)

        with engine.connect() as conn:
            # Execute the schema creation
            conn.execute(text(npc_schema))
            conn.commit()

            # Verify tables were created using PostgreSQL information_schema
            result = conn.execute(
                text("""
                SELECT table_name
                FROM information_schema.tables
                WHERE table_schema = 'public'
                AND table_name LIKE 'npc_%'
                ORDER BY table_name
                """)
            )
            tables = result.fetchall()
            table_names = [table[0] for table in tables]

            print(f"  [OK] Successfully initialized {database_name} database")
            print(f"  [OK] Created tables: {', '.join(table_names)}")

            # Populate with seed data if requested
            if populate_seed:
                # Get seed data from the same database or a source database
                source_url = database_url  # Use same database as source, or could be different
                npc_data, npc_spawn_data = get_npc_seed_data_from_postgresql(source_url)
                if npc_data and npc_spawn_data:
                    populate_npc_data(engine, npc_data, npc_spawn_data)
                else:
                    print(f"  [WARNING] No seed data available for {database_name}")

            return True

    except Exception as e:
        print(f"[ERROR] Error initializing {database_name} database: {e}")
        import traceback
        traceback.print_exc()
        return False


def main():
    """Main function to initialize NPC database schema."""
    parser = argparse.ArgumentParser(description="Initialize NPC database schema in PostgreSQL")
    parser.add_argument("--test-only", action="store_true", help="Only initialize test databases")
    parser.add_argument("--prod-only", action="store_true", help="Only initialize production database")
    parser.add_argument("--e2e-only", action="store_true", help="Only initialize e2e test database")
    parser.add_argument("--unit-only", action="store_true", help="Only initialize unit test database")

    args = parser.parse_args()

    print("[INFO] NPC Database Initialization Script")
    print("[INFO] NPC databases are now PostgreSQL databases managed via db/schema/ SQL files")
    print("[INFO] This script applies the NPC schema from db/schema/04_runtime_tables.sql\n")

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

    # Initialize databases using DATABASE_NPC_URL from environment
    # Note: In the new system, NPCs are typically in the same database or a separate NPC database
    # This script will use DATABASE_NPC_URL if set, otherwise fall back to DATABASE_URL

    if init_e2e:
        npc_url = get_npc_database_url("e2e")
        if npc_url:
            success &= init_database_schema(npc_url, "e2e_test", populate_seed=False)
        else:
            print("[WARNING] DATABASE_NPC_URL not set for e2e, skipping e2e database initialization")
            success = False

    if init_unit:
        npc_url = get_npc_database_url("unit")
        if npc_url:
            success &= init_database_schema(npc_url, "unit_test", populate_seed=False)
        else:
            print("[WARNING] DATABASE_NPC_URL not set for unit, skipping unit database initialization")
            success = False

    if init_prod:
        npc_url = get_npc_database_url("prod")
        if npc_url:
            success &= init_database_schema(npc_url, "production", populate_seed=False)
        else:
            print("[WARNING] DATABASE_NPC_URL not set for production, skipping production database initialization")
            success = False

    if success:
        print("\n[SUCCESS] All databases initialized successfully!")
        print("[INFO] NPC schema is now managed via PostgreSQL SQL files in db/schema/")
        sys.exit(0)
    else:
        print("\n[ERROR] Some databases failed to initialize!")
        print("[INFO] Ensure DATABASE_NPC_URL (or DATABASE_URL) is set to a PostgreSQL URL")
        sys.exit(1)


if __name__ == "__main__":
    main()
