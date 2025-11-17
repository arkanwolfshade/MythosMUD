#!/usr/bin/env python3
"""
Populate Test NPC Databases

This script populates the e2e_test and unit_test NPC databases with the same
data that exists in the source (local/production) PostgreSQL NPC database.

Usage:
    python scripts/populate_test_npc_databases.py [--source-env SOURCE_ENV]

    SOURCE_ENV can be 'prod', 'local', or 'default' (defaults to 'prod')
"""

import argparse
import os
import sys

from sqlalchemy import create_engine, text


def get_npc_database_url(environment: str = "default") -> str | None:
    """
    Get NPC database URL for the specified environment.

    Args:
        environment: Environment name ('test', 'e2e', 'unit', 'prod', 'local', or 'default')

    Returns:
        PostgreSQL database URL or None if not found
    """
    # Try environment-specific variables first
    env_var_map = {
        "test": "DATABASE_NPC_URL",
        "e2e": "DATABASE_NPC_URL",  # E2E uses same as test
        "unit": "DATABASE_NPC_URL",  # Unit uses same as test
        "prod": "DATABASE_NPC_URL",
        "local": "DATABASE_NPC_URL",  # Local uses same as prod
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


def get_npc_data_from_source(source_url: str):
    """
    Extract NPC data from the source PostgreSQL database.

    Args:
        source_url: PostgreSQL database URL for the source database

    Returns:
        Tuple of (npc_definitions_data, npc_spawn_rules_data) or (None, None) on error
        Each data item is a tuple of (rows, column_names)
    """
    if not source_url or not source_url.startswith("postgresql"):
        print("[ERROR] Invalid source database URL")
        return None, None

    print("Reading data from source PostgreSQL database...")

    try:
        # Convert async URL to sync URL for create_engine
        sync_url = source_url.replace("+asyncpg", "")
        engine = create_engine(sync_url, echo=False)

        with engine.connect() as conn:
            # Get all NPC definitions
            result = conn.execute(text("SELECT * FROM npc_definitions ORDER BY id"))
            npc_definitions = result.fetchall()
            # Get column names from result metadata (SQLAlchemy 2.0)
            try:
                def_column_names = list(result.keys())
            except AttributeError:
                # Fallback for older SQLAlchemy versions
                def_column_names = [desc[0] for desc in result.cursor.description]

            # Get all NPC spawn rules
            result = conn.execute(text("SELECT * FROM npc_spawn_rules ORDER BY id"))
            npc_spawn_rules = result.fetchall()
            # Get column names from result metadata (SQLAlchemy 2.0)
            try:
                spawn_column_names = list(result.keys())
            except AttributeError:
                # Fallback for older SQLAlchemy versions
                spawn_column_names = [desc[0] for desc in result.cursor.description]

        print(f"  [OK] Found {len(npc_definitions)} NPC definitions")
        print(f"  [OK] Found {len(npc_spawn_rules)} NPC spawn rules")

        return (npc_definitions, def_column_names), (npc_spawn_rules, spawn_column_names)

    except Exception as e:
        print(f"[ERROR] Failed to read data from source database: {e}")
        import traceback
        traceback.print_exc()
        return None, None


def populate_database(target_url: str, database_name: str, npc_definitions_data, npc_spawn_rules_data) -> bool:
    """
    Populate a PostgreSQL database with NPC data.

    Args:
        target_url: PostgreSQL database URL for the target database
        database_name: Human-readable name for logging
        npc_definitions_data: Tuple of (npc_definitions rows, column_names)
        npc_spawn_rules_data: Tuple of (npc_spawn_rules rows, column_names)

    Returns:
        True if successful, False otherwise
    """
    print(f"\nPopulating {database_name} database...")

    if not target_url or not target_url.startswith("postgresql"):
        print(f"  [ERROR] Invalid or missing PostgreSQL database URL for {database_name}")
        return False

    if npc_definitions_data is None or npc_spawn_rules_data is None:
        print(f"  [ERROR] No data provided for {database_name}")
        return False

    npc_definitions, def_columns = npc_definitions_data
    npc_spawn_rules, spawn_columns = npc_spawn_rules_data

    try:
        # Convert async URL to sync URL for create_engine
        sync_url = target_url.replace("+asyncpg", "")
        engine = create_engine(sync_url, echo=False)

        with engine.connect() as conn:
            trans = conn.begin()
            try:
                # Clear existing data (respecting foreign key constraints)
                conn.execute(text("DELETE FROM npc_spawn_rules"))
                conn.execute(text("DELETE FROM npc_relationships"))
                conn.execute(text("DELETE FROM npc_definitions"))
                conn.commit()

                # Insert NPC definitions
                if npc_definitions:
                    # Build INSERT statement dynamically based on columns
                    # PostgreSQL uses :column_name for named parameters
                    placeholders = ", ".join([f":{col}" for col in def_columns])
                    columns = ", ".join(def_columns)
                    insert_def_sql = f"""
                    INSERT INTO npc_definitions ({columns})
                    VALUES ({placeholders})
                    """

                    # Convert rows to dictionaries for parameterized insertion
                    for row in npc_definitions:
                        row_dict = dict(zip(def_columns, row, strict=False))
                        conn.execute(text(insert_def_sql), row_dict)
                    conn.commit()
                    print(f"  [OK] Inserted {len(npc_definitions)} NPC definitions")

                # Insert NPC spawn rules
                if npc_spawn_rules:
                    # Build INSERT statement dynamically based on columns
                    placeholders = ", ".join([f":{col}" for col in spawn_columns])
                    columns = ", ".join(spawn_columns)
                    insert_rule_sql = f"""
                    INSERT INTO npc_spawn_rules ({columns})
                    VALUES ({placeholders})
                    """

                    # Convert rows to dictionaries for parameterized insertion
                    for row in npc_spawn_rules:
                        row_dict = dict(zip(spawn_columns, row, strict=False))
                        conn.execute(text(insert_rule_sql), row_dict)
                    conn.commit()
                    print(f"  [OK] Inserted {len(npc_spawn_rules)} NPC spawn rules")

                trans.commit()
                return True

            except Exception:
                trans.rollback()
                raise

    except Exception as e:
        print(f"  [ERROR] Failed to populate {database_name} database: {e}")
        import traceback
        traceback.print_exc()
        return False


def main():
    """Main function to populate test NPC databases."""
    parser = argparse.ArgumentParser(
        description="Populate test NPC databases from source PostgreSQL database"
    )
    parser.add_argument(
        "--source-env",
        choices=["prod", "local", "default"],
        default="prod",
        help="Source environment to read data from (default: prod)",
    )

    args = parser.parse_args()

    print("=" * 60)
    print("Populating Test NPC Databases")
    print("=" * 60)
    print(f"[INFO] Source environment: {args.source_env}")
    print("[INFO] NPC databases are now PostgreSQL databases\n")

    # Get data from source database
    source_url = get_npc_database_url(args.source_env)
    if not source_url:
        print(f"[ERROR] DATABASE_NPC_URL not set for source environment '{args.source_env}'")
        print("[INFO] Ensure DATABASE_NPC_URL (or DATABASE_URL) is set to a PostgreSQL URL")
        sys.exit(1)

    npc_definitions_data, npc_spawn_rules_data = get_npc_data_from_source(source_url)

    if npc_definitions_data is None or npc_spawn_rules_data is None:
        print("\n[ERROR] Failed to read data from source database!")
        sys.exit(1)

    # Get target database URLs
    e2e_url = get_npc_database_url("e2e")
    unit_url = get_npc_database_url("unit")

    if not e2e_url:
        print("[WARNING] DATABASE_NPC_URL not set for e2e, skipping e2e_test database")
        e2e_success = False
    else:
        e2e_success = populate_database(e2e_url, "e2e_test", npc_definitions_data, npc_spawn_rules_data)

    if not unit_url:
        print("[WARNING] DATABASE_NPC_URL not set for unit, skipping unit_test database")
        unit_success = False
    else:
        unit_success = populate_database(unit_url, "unit_test", npc_definitions_data, npc_spawn_rules_data)

    print("\n" + "=" * 60)
    if e2e_success and unit_success:
        print("[SUCCESS] All test databases populated successfully!")
        sys.exit(0)
    else:
        print("[ERROR] Some databases failed to populate!")
        print("[INFO] Ensure DATABASE_NPC_URL (or DATABASE_URL) is set to PostgreSQL URLs")
        sys.exit(1)


if __name__ == "__main__":
    main()
