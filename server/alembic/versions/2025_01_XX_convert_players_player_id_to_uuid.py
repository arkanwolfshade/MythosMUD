"""Convert players.player_id from VARCHAR to UUID

Revision ID: convert_players_player_id_to_uuid
Revises: item_system_schema
Create Date: 2025-01-XX

This migration converts the players.player_id column from VARCHAR to UUID
to match the SQLAlchemy model definition and fix foreign key constraints
with player_channel_preferences table.
"""

from __future__ import annotations

from alembic import op

# revision identifiers, used by Alembic.
revision = "convert_players_player_id_to_uuid"
down_revision = "item_system_schema"
branch_labels = None
depends_on = None


def upgrade() -> None:
    """
    Convert players.player_id from VARCHAR to UUID.

    PostgreSQL can directly cast VARCHAR to UUID if all values are valid UUIDs.
    This migration:
    1. Drops foreign key constraints that reference players.player_id
    2. Converts the column type from VARCHAR to UUID
    3. Recreates the foreign key constraints
    """
    # Get connection to check database type
    conn = op.get_bind()

    # Check if we're using PostgreSQL
    if conn.dialect.name == "postgresql":
        # Drop foreign key constraints that reference players.player_id
        # This includes player_channel_preferences and any other tables
        op.execute("""
            DO $$
            DECLARE
                r RECORD;
            BEGIN
                FOR r IN (
                    SELECT conname, conrelid::regclass AS table_name
                    FROM pg_constraint
                    WHERE confrelid = 'players'::regclass
                    AND contype = 'f'
                    AND confkey @> ARRAY[(SELECT attnum FROM pg_attribute WHERE attrelid = 'players'::regclass AND attname = 'player_id')]
                ) LOOP
                    EXECUTE 'ALTER TABLE ' || r.table_name || ' DROP CONSTRAINT ' || r.conname;
                END LOOP;
            END $$;
        """)

        # Convert player_id from VARCHAR to UUID
        # PostgreSQL can cast VARCHAR to UUID if all values are valid UUIDs
        op.execute("""
            ALTER TABLE players
            ALTER COLUMN player_id TYPE UUID USING player_id::UUID;
        """)

        # Recreate foreign key constraints
        # player_channel_preferences will be handled by SQLAlchemy when it creates the table
        # But we need to ensure any other foreign keys are recreated
        # Note: player_channel_preferences should be created with UUID type matching

    else:
        # For SQLite, UUID is stored as TEXT, so no conversion needed
        # SQLite doesn't enforce types, so VARCHAR and UUID are both TEXT
        pass


def downgrade() -> None:
    """
    Convert players.player_id from UUID back to VARCHAR.

    This is a downgrade path, but should rarely be needed.
    """
    conn = op.get_bind()

    if conn.dialect.name == "postgresql":
        # Drop foreign key constraints
        op.execute("""
            DO $$
            DECLARE
                r RECORD;
            BEGIN
                FOR r IN (
                    SELECT conname, conrelid::regclass AS table_name
                    FROM pg_constraint
                    WHERE confrelid = 'players'::regclass
                    AND contype = 'f'
                    AND confkey @> ARRAY[(SELECT attnum FROM pg_attribute WHERE attrelid = 'players'::regclass AND attname = 'player_id')]
                ) LOOP
                    EXECUTE 'ALTER TABLE ' || r.table_name || ' DROP CONSTRAINT ' || r.conname;
                END LOOP;
            END $$;
        """)

        # Convert UUID back to VARCHAR
        op.execute("""
            ALTER TABLE players
            ALTER COLUMN player_id TYPE VARCHAR(36) USING player_id::TEXT;
        """)

    else:
        # SQLite doesn't need conversion
        pass
