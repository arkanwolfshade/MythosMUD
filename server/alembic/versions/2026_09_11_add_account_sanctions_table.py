"""Add account_sanctions table (account-level moderation: bans, kick cooldowns)

Revision ID: add_account_sanctions_table
Revises: align_room_environment_enum
Create Date: 2026-09-11

Formalizes schema that had been created ad hoc directly against mythos_unit only (found while
auditing schema parity for #824) -- the table, its indexes, and the four supporting functions in
db/procedures/account_sanctions.sql now have a real migration/apply path instead of living only
as untracked manual DDL in one environment.
"""
# pylint: disable=invalid-name

from __future__ import annotations

import sqlalchemy as sa

# Alembic is available at runtime when running `alembic upgrade`; linters may not see it.
from alembic import op  # pyright: ignore[reportMissingImports]  # pylint: disable=import-error
from sqlalchemy.dialects import postgresql

revision = "add_account_sanctions_table"
down_revision = "align_room_environment_enum"
branch_labels = None
depends_on = None


def upgrade() -> None:
    """Create account_sanctions table and its index."""
    op.create_table(
        "account_sanctions",
        sa.Column("id", postgresql.UUID(as_uuid=False), primary_key=True, nullable=False),
        sa.Column(
            "user_id",
            postgresql.UUID(as_uuid=False),
            sa.ForeignKey("users.id", ondelete="CASCADE"),
            nullable=False,
        ),
        sa.Column("sanction_type", sa.Text(), nullable=False),
        sa.Column("tier", sa.Text(), nullable=True),
        sa.Column("reason", sa.Text(), nullable=False),
        sa.Column(
            "issued_by_player_id",
            postgresql.UUID(as_uuid=False),
            sa.ForeignKey("players.player_id", ondelete="SET NULL"),
            nullable=True,
        ),
        sa.Column("issued_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.text("now()")),
        sa.Column("expires_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("lifted_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column(
            "lifted_by_player_id",
            postgresql.UUID(as_uuid=False),
            sa.ForeignKey("players.player_id", ondelete="SET NULL"),
            nullable=True,
        ),
        sa.Column("ip_address", postgresql.INET(), nullable=True),
        sa.CheckConstraint(
            "sanction_type = ANY (ARRAY['kick_cooldown'::text, 'ban'::text])",
            name="account_sanctions_sanction_type_check",
        ),
        sa.CheckConstraint(
            "(tier IS NULL) OR (tier = ANY (ARRAY['1h'::text, '24h'::text, '7d'::text, 'permanent'::text]))",
            name="account_sanctions_tier_check",
        ),
    )
    op.create_index(
        "idx_account_sanctions_user_active",
        "account_sanctions",
        ["user_id"],
        postgresql_where=sa.text("lifted_at IS NULL"),
    )
    op.execute("COMMENT ON TABLE account_sanctions IS 'Account-level kick cooldowns and bans for admin moderation.'")


def downgrade() -> None:
    """Drop account_sanctions table and its index."""
    op.drop_index("idx_account_sanctions_user_active", table_name="account_sanctions")
    op.drop_table("account_sanctions")
