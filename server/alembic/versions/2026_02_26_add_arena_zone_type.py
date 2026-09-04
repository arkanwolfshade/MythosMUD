"""Add 'arena' to zones.zone_type CHECK (Gladiator Ring)

Revision ID: add_arena_zone_type
Revises: seed_quest_leave_tutorial
Create Date: 2026-02-26

Allows zone_type = 'arena' for the limbo/arena zone. No data inserted here;
arena zone, subzone, rooms, and room_links are added via DML (mythos_dev_dml,
mythos_unit_dml, mythos_e2e_dml).
"""
# pylint: disable=invalid-name  # Alembic convention

from __future__ import annotations

from alembic import op  # pyright: ignore[reportMissingImports]  # pylint: disable=import-error

revision = "add_arena_zone_type"
down_revision = "seed_quest_leave_tutorial"
branch_labels = None
depends_on = None


def upgrade() -> None:
    """Allow zone_type 'arena' in zones CHECK."""
    op.execute("ALTER TABLE zones DROP CONSTRAINT IF EXISTS chk_zones_zone_type")
    op.execute(
        """
        ALTER TABLE zones ADD CONSTRAINT chk_zones_zone_type CHECK (
            (zone_type IS NULL) OR (zone_type = ANY(ARRAY[
                'city'::text, 'countryside'::text, 'mountains'::text,
                'swamp'::text, 'tundra'::text, 'desert'::text, 'death'::text, 'arena'::text
            ]))
        )
        """
    )


def downgrade() -> None:
    """Remove 'arena' from zones.zone_type CHECK (fails if arena zone exists)."""
    op.execute("ALTER TABLE zones DROP CONSTRAINT IF EXISTS chk_zones_zone_type")
    op.execute(
        """
        ALTER TABLE zones ADD CONSTRAINT chk_zones_zone_type CHECK (
            (zone_type IS NULL) OR (zone_type = ANY(ARRAY[
                'city'::text, 'countryside'::text, 'mountains'::text,
                'swamp'::text, 'tundra'::text, 'desert'::text, 'death'::text
            ]))
        )
        """
    )
