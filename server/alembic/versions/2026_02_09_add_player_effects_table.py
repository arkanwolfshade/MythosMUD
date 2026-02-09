"""Add player_effects table (ADR-009 effects system)

Revision ID: add_player_effects_table
Revises: ensure_item_instance_fks
Create Date: 2026-02-09

"""
# Module name comes from filename; Alembic uses date-prefixed migration filenames by convention.
# pylint: disable=invalid-name

from __future__ import annotations

import sqlalchemy as sa

# Alembic is available at runtime when running `alembic upgrade`; linters may not see it.
from alembic import op  # pyright: ignore[reportMissingImports]  # pylint: disable=import-error
from sqlalchemy.dialects import postgresql

# Revision identifiers, used by Alembic (required names; see file-level invalid-name disable).
revision = "add_player_effects_table"
down_revision = "ensure_item_instance_fks"
branch_labels = None
depends_on = None


def upgrade() -> None:
    """Create player_effects table and indexes (ADR-009 effects system)."""
    op.create_table(
        "player_effects",
        sa.Column("id", postgresql.UUID(as_uuid=False), primary_key=True),
        sa.Column(
            "player_id",
            postgresql.UUID(as_uuid=False),
            sa.ForeignKey("players.player_id", ondelete="CASCADE"),
            nullable=False,
        ),
        sa.Column("effect_type", sa.String(length=64), nullable=False),
        sa.Column("category", sa.String(length=64), nullable=False),
        sa.Column("duration", sa.Integer(), nullable=False),
        sa.Column("applied_at_tick", sa.Integer(), nullable=False),
        sa.Column("intensity", sa.Integer(), nullable=False, server_default=sa.text("1")),
        sa.Column("source", sa.String(length=128), nullable=True),
        sa.Column(
            "visibility_level",
            sa.String(length=32),
            nullable=False,
            server_default=sa.text("'visible'"),
        ),
        sa.Column(
            "created_at",
            sa.DateTime(),
            nullable=False,
            server_default=sa.text("now()"),
        ),
    )
    op.create_index("ix_player_effects_player_id", "player_effects", ["player_id"])
    op.create_index("ix_player_effects_effect_type", "player_effects", ["effect_type"])
    op.create_index("ix_player_effects_category", "player_effects", ["category"])


def downgrade() -> None:
    """Drop player_effects table and indexes."""
    op.drop_index("ix_player_effects_category", table_name="player_effects")
    op.drop_index("ix_player_effects_effect_type", table_name="player_effects")
    op.drop_index("ix_player_effects_player_id", table_name="player_effects")
    op.drop_table("player_effects")
