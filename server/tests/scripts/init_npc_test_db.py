"""
NPC Test database initialization for MythosMUD.

DEPRECATED: This script is for SQLite initialization only.
We now use PostgreSQL exclusively. SQLite databases have been removed.

This module is kept for reference only and should not be used.
All NPC data is now stored in PostgreSQL via SQLAlchemy models.
"""

from pathlib import Path

# DEPRECATED: This script is no longer functional
# NPC databases are now managed via PostgreSQL SQL schema files in db/schema/


def load_npc_schema():
    """
    Load the NPC test database schema from SQL files.

    DEPRECATED: This function is no longer used.
    NPC schema is now defined in db/schema/02_items_and_npcs.sql
    """
    raise DeprecationWarning(
        "This function is deprecated. NPC schema is now managed via PostgreSQL SQL files in db/schema/"
    )


def get_npc_seed_data():
    """
    Extract seed data from the local NPC database.

    DEPRECATED: This function is no longer used.
    NPC data is now loaded from PostgreSQL database.
    """
    raise DeprecationWarning("This function is deprecated. NPC data is now stored in PostgreSQL database.")


def populate_npc_data(conn, npc_definitions, npc_spawn_rules):
    """
    Populate the database with NPC seed data.

    DEPRECATED: This function is no longer used.
    NPC data is now managed via SQLAlchemy models and PostgreSQL.
    """
    raise DeprecationWarning("This function is deprecated. NPC data is now managed via SQLAlchemy models.")


def _resolve_target_path() -> Path:
    """
    Determine the NPC test database path from environment configuration.

    DEPRECATED: This function is no longer used.
    NPC databases are now PostgreSQL databases accessed via DATABASE_NPC_URL.
    """
    raise DeprecationWarning("This function is deprecated. NPC databases are now PostgreSQL databases.")


def init_npc_test_database():
    """
    Initialize the NPC test database with schema and test data.

    DEPRECATED: This function is no longer used.
    NPC test databases are now PostgreSQL databases initialized via db/schema/ SQL files.
    """
    print(
        "[DEPRECATED] init_npc_test_database() is deprecated. "
        "NPC databases are now PostgreSQL databases managed via db/schema/ SQL files."
    )
    print(
        "To initialize NPC test database, use PostgreSQL SQL schema files in db/schema/ "
        "and ensure DATABASE_NPC_URL is set to a PostgreSQL URL."
    )
    raise DeprecationWarning("This function is deprecated. Use PostgreSQL SQL schema files in db/schema/ instead.")


if __name__ == "__main__":
    print(
        "[DEPRECATED] This script is deprecated. "
        "NPC databases are now PostgreSQL databases managed via db/schema/ SQL files."
    )
    print("This script will not execute. Use PostgreSQL schema files instead.")
