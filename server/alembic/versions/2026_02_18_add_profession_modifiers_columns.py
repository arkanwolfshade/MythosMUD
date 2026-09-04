"""Add stat_modifiers and skill_modifiers to professions (character creation revamp 4.3/4.4)

Revision ID: add_profession_modifiers_cols
Revises: add_player_effects_table
Create Date: 2026-02-18

Adds TEXT columns for profession stat and skill modifiers; seed data in
data/db/05_profession_modifiers.sql populates them.
"""
# Module name comes from filename; Alembic uses date-prefixed migration filenames by convention.
# pylint: disable=invalid-name

from __future__ import annotations

import sqlalchemy as sa
from alembic import op

revision = "add_profession_modifiers_cols"
down_revision = "add_player_effects_table"
branch_labels = None
depends_on = None


def upgrade() -> None:
    """Add stat_modifiers and skill_modifiers columns to professions table."""
    op.add_column(
        "professions",
        sa.Column(
            "stat_modifiers",
            sa.Text(),
            nullable=False,
            server_default=sa.text("'[]'"),
        ),
    )
    op.add_column(
        "professions",
        sa.Column(
            "skill_modifiers",
            sa.Text(),
            nullable=False,
            server_default=sa.text("'[]'"),
        ),
    )


def downgrade() -> None:
    """Remove stat_modifiers and skill_modifiers columns from professions table."""
    op.drop_column("professions", "skill_modifiers")
    op.drop_column("professions", "stat_modifiers")
