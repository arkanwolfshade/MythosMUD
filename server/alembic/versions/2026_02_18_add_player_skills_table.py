"""Add player_skills table (character creation revamp 4.3)

Revision ID: add_player_skills_table
Revises: add_profession_modifiers_cols
Create Date: 2026-02-18

Creates player_skills table: player_id (FK players), skill_id (FK skills), value.
Idempotent: uses IF NOT EXISTS so safe after running db/migrations/025 manually.
"""
# Module name comes from filename; Alembic uses date-prefixed migration filenames by convention.
# pylint: disable=invalid-name

from __future__ import annotations

from alembic import op

revision = "add_player_skills_table"
down_revision = "add_profession_modifiers_cols"
branch_labels = None
depends_on = None


def upgrade() -> None:
    """Create player_skills table if not exists (matches db/migrations/025)."""
    op.execute("""
        CREATE TABLE IF NOT EXISTS player_skills (
            player_id UUID NOT NULL REFERENCES players (player_id) ON DELETE CASCADE,
            skill_id BIGINT NOT NULL REFERENCES skills (id) ON DELETE CASCADE,
            value INTEGER NOT NULL CHECK (value >= 0 AND value <= 100),
            PRIMARY KEY (player_id, skill_id)
        )
    """)
    op.execute("CREATE INDEX IF NOT EXISTS idx_player_skills_player_id ON player_skills (player_id)")
    op.execute("CREATE INDEX IF NOT EXISTS idx_player_skills_skill_id ON player_skills (skill_id)")
    op.execute(
        "COMMENT ON TABLE player_skills IS 'Per-character skill values; created at character creation and updated on level-up improvement.'"
    )
    op.execute("COMMENT ON COLUMN player_skills.value IS 'Skill percentage 0-100; max 99 for improvement cap.'")


def downgrade() -> None:
    """Drop player_skills table."""
    op.execute("DROP TABLE IF EXISTS player_skills CASCADE")
