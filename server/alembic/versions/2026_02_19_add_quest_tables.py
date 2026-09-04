"""Add quest_definitions, quest_instances, quest_offers tables (quest subsystem)

Revision ID: add_quest_tables
Revises: add_player_skills_table
Create Date: 2026-02-19

Creates quest subsystem tables: quest_definitions (id, definition JSONB),
quest_instances (per-character quest state), quest_offers (junction for NPC/room offerers).
"""
# pylint: disable=invalid-name  # Reason: Module name comes from filename; Alembic uses date-prefixed migration filenames by convention

from __future__ import annotations

# Reason: Alembic available at runtime when running `alembic upgrade`; linters may not have it
from alembic import op  # pyright: ignore[reportMissingImports]  # pylint: disable=import-error

revision = "add_quest_tables"
down_revision = "add_player_skills_table"
branch_labels = None
depends_on = None


def upgrade() -> None:
    """Create quest_definitions, quest_instances, quest_offers tables."""
    op.execute("""
        CREATE TABLE IF NOT EXISTS quest_definitions (
            id TEXT NOT NULL PRIMARY KEY,
            definition JSONB NOT NULL,
            created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
            updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
        )
    """)
    op.execute(
        "COMMENT ON TABLE quest_definitions IS 'Quest templates; definition JSONB holds name, title, goals, rewards, triggers, requires_all/requires_any, auto_complete, turn_in_entities.'"
    )

    op.execute("""
        CREATE TABLE IF NOT EXISTS quest_instances (
            id UUID NOT NULL PRIMARY KEY DEFAULT gen_random_uuid(),
            player_id UUID NOT NULL REFERENCES players (player_id) ON DELETE CASCADE,
            quest_id TEXT NOT NULL REFERENCES quest_definitions (id) ON DELETE CASCADE,
            state TEXT NOT NULL CHECK (state IN ('active', 'completed', 'abandoned')),
            progress JSONB NOT NULL DEFAULT '{}',
            accepted_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
            completed_at TIMESTAMPTZ,
            UNIQUE (player_id, quest_id)
        )
    """)
    op.execute("CREATE INDEX IF NOT EXISTS idx_quest_instances_player_id ON quest_instances (player_id)")
    op.execute("CREATE INDEX IF NOT EXISTS idx_quest_instances_quest_id ON quest_instances (quest_id)")
    op.execute("CREATE INDEX IF NOT EXISTS idx_quest_instances_state ON quest_instances (state)")
    op.execute(
        "COMMENT ON TABLE quest_instances IS 'Per-character quest state; one row per character per quest (active/completed/abandoned).'"
    )

    op.execute("""
        CREATE TABLE IF NOT EXISTS quest_offers (
            quest_id TEXT NOT NULL REFERENCES quest_definitions (id) ON DELETE CASCADE,
            offer_entity_type TEXT NOT NULL,
            offer_entity_id TEXT NOT NULL,
            PRIMARY KEY (quest_id, offer_entity_type, offer_entity_id)
        )
    """)
    op.execute(
        "CREATE INDEX IF NOT EXISTS idx_quest_offers_entity ON quest_offers (offer_entity_type, offer_entity_id)"
    )
    op.execute(
        "COMMENT ON TABLE quest_offers IS 'Links quests to NPCs or rooms that offer them; offer_entity_type in (npc, room).'"
    )


def downgrade() -> None:
    """Drop quest tables (order matters for FKs)."""
    op.execute("DROP TABLE IF EXISTS quest_offers CASCADE")
    op.execute("DROP TABLE IF EXISTS quest_instances CASCADE")
    op.execute("DROP TABLE IF EXISTS quest_definitions CASCADE")
