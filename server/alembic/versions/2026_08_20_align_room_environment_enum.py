"""Align environment enum across zones, subzones, and rooms (#623)

Revision ID: align_room_environment_enum
Revises: add_arena_zone_type
Create Date: 2026-08-20

zones/subzones.environment had a CHECK restricting it to
{indoors, outdoors, underwater, void}; rooms.environment (a key inside the rooms.attributes
JSONB) had no constraint at all, so it drifted to 7 distinct values in live data, two of them
one-off typos. This adopts the live vocabulary -- indoors, outdoors, underwater, intersection,
street_paved, arena, void -- as canonical for all three levels (keeps the room -> subzone ->
zone inheritance chain in world_loader.get_room_environment() trivially valid), corrects the
two typo rows first so the new rooms constraint can never fail on legacy data, then widens the
zones/subzones constraints and adds a matching expression CHECK on rooms. See
docs/ROOM_ENVIRONMENT_REFERENCE.md.
"""
# pylint: disable=invalid-name  # Alembic convention

from __future__ import annotations

from alembic import op  # pyright: ignore[reportMissingImports]  # pylint: disable=import-error

revision = "align_room_environment_enum"
down_revision = "add_arena_zone_type"
branch_labels = None
depends_on = None

_ENVIRONMENT_ARRAY_SQL = (
    "ARRAY['indoors'::text, 'outdoors'::text, 'underwater'::text, 'intersection'::text, "
    "'street_paved'::text, 'arena'::text, 'void'::text]"
)


def upgrade() -> None:
    """Fix the two one-off room rows, then widen/add the environment CHECKs."""
    # limbo_death_void's own zone and subzone are already environment = 'void'; the room was
    # simply out of sync with its parents.
    op.execute(
        """
        UPDATE rooms
        SET attributes = jsonb_set(attributes, '{environment}', '"void"')
        WHERE stable_id = 'limbo_death_void'
          AND attributes->>'environment' = 'otherworldly'
        """
    )
    # A pier on the Innsmouth waterfront.
    op.execute(
        """
        UPDATE rooms
        SET attributes = jsonb_set(attributes, '{environment}', '"outdoors"')
        WHERE stable_id = 'earth_innsmouth_waterfront_room_waterfront_001'
          AND attributes->>'environment' = 'waterfront_misty'
        """
    )

    op.execute("ALTER TABLE zones DROP CONSTRAINT IF EXISTS chk_zones_environment")
    op.execute(
        f"""
        ALTER TABLE zones ADD CONSTRAINT chk_zones_environment CHECK (
            (environment IS NULL) OR (environment = ANY({_ENVIRONMENT_ARRAY_SQL}))
        )
        """
    )

    op.execute("ALTER TABLE subzones DROP CONSTRAINT IF EXISTS chk_subzones_environment")
    op.execute(
        f"""
        ALTER TABLE subzones ADD CONSTRAINT chk_subzones_environment CHECK (
            (environment IS NULL) OR (environment = ANY({_ENVIRONMENT_ARRAY_SQL}))
        )
        """
    )

    op.execute("ALTER TABLE rooms DROP CONSTRAINT IF EXISTS chk_rooms_environment")
    op.execute(
        f"""
        ALTER TABLE rooms ADD CONSTRAINT chk_rooms_environment CHECK (
            (attributes->>'environment' IS NULL)
            OR (attributes->>'environment' = ANY({_ENVIRONMENT_ARRAY_SQL}))
        )
        """
    )


def downgrade() -> None:
    """Restore the narrower zones/subzones CHECKs and drop the rooms CHECK.

    Does not restore the two corrected typo values -- they were errors, not data to preserve.
    """
    op.execute("ALTER TABLE rooms DROP CONSTRAINT IF EXISTS chk_rooms_environment")

    op.execute("ALTER TABLE subzones DROP CONSTRAINT IF EXISTS chk_subzones_environment")
    op.execute(
        """
        ALTER TABLE subzones ADD CONSTRAINT chk_subzones_environment CHECK (
            (environment IS NULL) OR (environment IN ('indoors', 'outdoors', 'underwater', 'void'))
        )
        """
    )

    op.execute("ALTER TABLE zones DROP CONSTRAINT IF EXISTS chk_zones_environment")
    op.execute(
        """
        ALTER TABLE zones ADD CONSTRAINT chk_zones_environment CHECK (
            (environment IS NULL) OR (environment IN ('indoors', 'outdoors', 'underwater', 'void'))
        )
        """
    )
