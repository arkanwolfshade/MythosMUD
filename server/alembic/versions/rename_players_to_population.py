"""Rename min_players/max_players to min_population/max_population

Revision ID: rename_players_to_population
Revises:
Create Date: 2025-10-14

This migration renames the columns in npc_spawn_rules to better reflect
that they control NPC/mob population counts, not player counts.
"""

from alembic import op

# revision identifiers, used by Alembic.
revision = "rename_players_to_population"
down_revision = None  # Update this to your latest migration
branch_labels = None
depends_on = None


def upgrade() -> None:
    """Rename columns from min_players/max_players to min_population/max_population."""
    # SQLite doesn't support ALTER COLUMN RENAME directly, so we need to:
    # 1. Create a new table with the new column names
    # 2. Copy data from the old table
    # 3. Drop the old table
    # 4. Rename the new table to the old table name

    # Create temporary table with new column names
    op.execute("""
        CREATE TABLE npc_spawn_rules_new (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            npc_definition_id INTEGER NOT NULL,
            sub_zone_id TEXT NOT NULL,
            min_population INTEGER DEFAULT 0 NOT NULL,
            max_population INTEGER DEFAULT 999 NOT NULL,
            spawn_conditions TEXT NOT NULL DEFAULT '{}',
            FOREIGN KEY (npc_definition_id) REFERENCES npc_definitions(id) ON DELETE CASCADE
        )
    """)

    # Copy data from old table to new table
    op.execute("""
        INSERT INTO npc_spawn_rules_new (id, npc_definition_id, sub_zone_id, min_population, max_population, spawn_conditions)
        SELECT id, npc_definition_id, sub_zone_id, min_players, max_players, spawn_conditions
        FROM npc_spawn_rules
    """)

    # Drop old table
    op.execute("DROP TABLE npc_spawn_rules")

    # Rename new table to old table name
    op.execute("ALTER TABLE npc_spawn_rules_new RENAME TO npc_spawn_rules")

    # Recreate indexes
    op.execute("CREATE INDEX IF NOT EXISTS idx_npc_spawn_rules_sub_zone ON npc_spawn_rules(sub_zone_id)")
    op.execute("CREATE INDEX IF NOT EXISTS idx_npc_spawn_rules_npc_def ON npc_spawn_rules(npc_definition_id)")


def downgrade() -> None:
    """Revert column names back to min_players/max_players."""
    # Create temporary table with old column names
    op.execute("""
        CREATE TABLE npc_spawn_rules_old (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            npc_definition_id INTEGER NOT NULL,
            sub_zone_id TEXT NOT NULL,
            min_players INTEGER DEFAULT 0 NOT NULL,
            max_players INTEGER DEFAULT 999 NOT NULL,
            spawn_conditions TEXT NOT NULL DEFAULT '{}',
            FOREIGN KEY (npc_definition_id) REFERENCES npc_definitions(id) ON DELETE CASCADE
        )
    """)

    # Copy data from current table to old table
    op.execute("""
        INSERT INTO npc_spawn_rules_old (id, npc_definition_id, sub_zone_id, min_players, max_players, spawn_conditions)
        SELECT id, npc_definition_id, sub_zone_id, min_population, max_population, spawn_conditions
        FROM npc_spawn_rules
    """)

    # Drop current table
    op.execute("DROP TABLE npc_spawn_rules")

    # Rename old table to current table name
    op.execute("ALTER TABLE npc_spawn_rules_old RENAME TO npc_spawn_rules")

    # Recreate indexes
    op.execute("CREATE INDEX IF NOT EXISTS idx_npc_spawn_rules_sub_zone ON npc_spawn_rules(sub_zone_id)")
    op.execute("CREATE INDEX IF NOT EXISTS idx_npc_spawn_rules_npc_def ON npc_spawn_rules(npc_definition_id)")
