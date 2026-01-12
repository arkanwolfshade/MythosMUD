#!/usr/bin/env python3
"""
NPC Sample Data Population Script

This script populates PostgreSQL NPC databases with sample data
for testing and development purposes.

Usage:
    python scripts/populate_npc_sample_data.py [--test-only] [--prod-only]
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
        environment: Environment name ('test', 'prod', or 'default')

    Returns:
        PostgreSQL database URL or None if not found
    """
    # Try environment-specific variables first
    env_var_map = {
        "test": "DATABASE_NPC_URL",
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


def _validate_database_url(database_url: str, database_name: str) -> bool:
    """Validate database URL."""
    if not database_url or not database_url.startswith("postgresql"):
        print(f"  [ERROR] Invalid or missing PostgreSQL database URL for {database_name}")
        return False
    return True


def _read_sql_file(database_name: str) -> str | None:
    """Read SQL file content."""
    sql_file = Path(__file__).parent.parent / "server" / "sql" / "npc_sample_data.sql"
    if not sql_file.exists():
        print(f"  [ERROR] Sample data SQL file not found: {sql_file}")
        return None

    with open(sql_file, encoding="utf-8") as f:
        return f.read()


def _split_sql_statements(sql_content: str) -> list[str]:
    """Split SQL content into individual statements."""
    return [stmt.strip() for stmt in sql_content.split(";") if stmt.strip() and not stmt.strip().startswith("--")]


def _get_column_names(result) -> list[str]:
    """Get column names from result metadata."""
    try:
        return list(result.keys())
    except AttributeError:
        return [desc[0] for desc in result.cursor.description]


def _process_select_statement(conn, statement: str) -> None:
    """Process SELECT statement for verification."""
    result = conn.execute(text(statement))
    rows = result.fetchall()
    column_names = _get_column_names(result)

    print(f"  [VERIFY] {statement[:60]}...")
    for row in rows:
        row_dict = dict(zip(column_names, row, strict=False))
        print(f"    {row_dict}")


def _process_other_statement(conn, statement: str) -> None:
    """Process non-SELECT statements."""
    conn.execute(text(statement))
    display_stmt = statement[:60] + "..." if len(statement) > 60 else statement
    print(f"  [OK] Executed: {display_stmt}")


def _verify_foreign_keys(conn, database_name: str) -> None:
    """Verify foreign key constraints."""
    fk_check_result = conn.execute(
        text("""
        SELECT
            conname AS constraint_name,
            conrelid::regclass AS table_name
        FROM pg_constraint
        WHERE contype = 'f'
        AND NOT convalidated
        """)
    )
    invalid_fks = fk_check_result.fetchall()

    if invalid_fks:
        print(f"  [WARNING] Found {len(invalid_fks)} invalid foreign key constraints:")
        for fk in invalid_fks:
            print(f"    - {fk[0]} on {fk[1]}")
    else:
        print(f"  [OK] Foreign key constraints verified for {database_name} database")


def populate_database(database_url: str, database_name: str) -> bool:
    """
    Populate a PostgreSQL database with sample NPC data.

    Args:
        database_url: The PostgreSQL database URL
        database_name: Human-readable name for logging

    Returns:
        True if successful, False otherwise
    """
    print(f"Populating {database_name} database...")

    if not _validate_database_url(database_url, database_name):
        return False

    try:
        sql_content = _read_sql_file(database_name)
        if sql_content is None:
            return False

        sync_url = database_url.replace("+asyncpg", "")
        engine = create_engine(sync_url, echo=False)

        with engine.connect() as conn:
            trans = conn.begin()
            try:
                statements = _split_sql_statements(sql_content)

                for statement in statements:
                    if not statement or statement.strip().startswith("--"):
                        continue

                    if statement.upper().strip().startswith("SELECT"):
                        _process_select_statement(conn, statement)
                    else:
                        _process_other_statement(conn, statement)

                trans.commit()
                _verify_foreign_keys(conn, database_name)

                print(f"  [OK] Successfully populated {database_name} database")
                return True

            except Exception:
                trans.rollback()
                raise

    except Exception as e:
        print(f"  [ERROR] Error populating {database_name} database: {e}")
        import traceback

        traceback.print_exc()
        return False


def main():
    """Main function to populate NPC sample data."""
    parser = argparse.ArgumentParser(description="Populate PostgreSQL NPC databases with sample data")
    parser.add_argument("--test-only", action="store_true", help="Only populate test database")
    parser.add_argument("--prod-only", action="store_true", help="Only populate production database")

    args = parser.parse_args()

    print("[INFO] NPC Sample Data Population Script")
    print("[INFO] NPC databases are now PostgreSQL databases\n")

    # Determine which databases to populate
    populate_test = not args.prod_only
    populate_prod = not args.test_only

    success = True

    # Populate test database
    if populate_test:
        npc_url = get_npc_database_url("test")
        if npc_url:
            success &= populate_database(npc_url, "test")
        else:
            print("[WARNING] DATABASE_NPC_URL not set for test, skipping test database population")
            success = False

    # Populate production database
    if populate_prod:
        npc_url = get_npc_database_url("prod")
        if npc_url:
            success &= populate_database(npc_url, "production")
        else:
            print("[WARNING] DATABASE_NPC_URL not set for production, skipping production database population")
            success = False

    if success:
        print("\n[SUCCESS] All databases populated successfully!")
        sys.exit(0)
    else:
        print("\n[ERROR] Some databases failed to populate!")
        print("[INFO] Ensure DATABASE_NPC_URL (or DATABASE_URL) is set to a PostgreSQL URL")
        sys.exit(1)


if __name__ == "__main__":
    main()
