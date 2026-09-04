"""Seed first quest: leave_the_tutorial (quest subsystem)

Revision ID: seed_quest_leave_tutorial
Revises: add_quest_tables
Create Date: 2026-02-19

Inserts quest definition for leave_the_tutorial and one quest_offers row.
Trigger: room (tutorial bedroom). Goal: complete_activity exit that room. Reward: XP.
"""
# pylint: disable=invalid-name  # Reason: Module name comes from filename; Alembic uses date-prefixed migration filenames by convention

from __future__ import annotations

# Reason: Alembic available at runtime when running `alembic upgrade`; linters may not have it
from alembic import op  # pyright: ignore[reportMissingImports]  # pylint: disable=import-error

# Tutorial bedroom room id used by character creation / player_repository (single source of truth in code).
TUTORIAL_ROOM_ID = "earth_arkhamcity_sanitarium_room_tutorial_bedroom_001"

revision = "seed_quest_leave_tutorial"
down_revision = "add_quest_tables"
branch_labels = None
depends_on = None


def upgrade() -> None:
    """Insert leave_the_tutorial quest and quest_offers row."""
    exit_target = f"exit_{TUTORIAL_ROOM_ID}"
    definition_json = (
        '{"name": "leave_the_tutorial", "title": "Leave the tutorial", '
        '"description": "Find your way out of the tutorial room.", '
        '"goals": [{"type": "complete_activity", "target": "' + exit_target + '"}], '
        '"rewards": [{"type": "xp", "amount": 10}], '
        '"triggers": [{"type": "room", "entity_id": "' + TUTORIAL_ROOM_ID + '"}], '
        '"requires_all": [], "requires_any": [], "auto_complete": true, "turn_in_entities": []}'
    )
    # Escape single quotes for use inside SQL literal.
    escaped = definition_json.replace("'", "''")
    op.execute(
        f"""
        INSERT INTO quest_definitions (id, definition, created_at, updated_at)
        VALUES ('leave_the_tutorial', '{escaped}'::jsonb, NOW(), NOW())
        ON CONFLICT (id) DO NOTHING
        """
    )
    op.execute(
        f"""
        INSERT INTO quest_offers (quest_id, offer_entity_type, offer_entity_id)
        VALUES ('leave_the_tutorial', 'room', '{TUTORIAL_ROOM_ID}')
        ON CONFLICT (quest_id, offer_entity_type, offer_entity_id) DO NOTHING
        """
    )


def downgrade() -> None:
    """Remove seed quest and its offer."""
    op.execute("DELETE FROM quest_offers WHERE quest_id = 'leave_the_tutorial'")
    op.execute("DELETE FROM quest_definitions WHERE id = 'leave_the_tutorial'")
