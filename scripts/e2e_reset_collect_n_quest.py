#!/usr/bin/env python3
"""Ensure example collect_n quest + item prototype exist in E2E DB; clear player instances.

Seed IDs below are content (gather_sanitarium_daisies via NPC 54), not engine coupling.
"""

from __future__ import annotations

import json
import os

import asyncpg
from anyio import run

# Example collect_n seed content (DB migrations / DML). Swap these to exercise another quest.
QUEST_ID = "gather_sanitarium_daisies"
NPC_SPAWN_ID = "54"
ITEM_PROTOTYPE_ID = "misc.herb.sanitarium_daisy"
QUEST_DEFINITION = {
    "name": QUEST_ID,
    "goals": [
        {"type": "collect_n", "config": {"count": 3}, "target": ITEM_PROTOTYPE_ID}
    ],
    "title": "Gather Sanitarium Daisies",
    "rewards": [{"type": "xp", "config": {"amount": 15}}],
    "triggers": [{"type": "npc", "entity_id": NPC_SPAWN_ID}],
    "description": (
        "Dr. Morgan needs three sanitarium daisies for a calming infusion. "
        "Collect them from the foyer tray and turn them in."
    ),
    "requires_all": [],
    "requires_any": [],
    "auto_complete": False,
    "turn_in_entities": [NPC_SPAWN_ID],
}


async def _reset_collect_n_quest() -> None:
    database_url = os.environ.get("DATABASE_URL", "").strip()
    if not database_url:
        database_url = "postgresql://postgres:Cthulhu1@localhost:5432/mythos_e2e"
    url = database_url.replace("postgresql+asyncpg://", "postgresql://")
    search_path = os.environ.get("POSTGRES_SEARCH_PATH", "").strip() or "mythos_e2e"
    conn = await asyncpg.connect(url, server_settings={"search_path": search_path})
    try:
        # mythos_e2e can be bootstrapped without quest/item DML; upsert so ask/summon is self-healing.
        # Note: item prototypes are also loaded into the server registry at startup — restart E2E API
        # after first seed if summon still says prototype not found.
        _ = await conn.execute(
            """
            INSERT INTO item_prototypes (
              prototype_id, name, short_description, long_description, item_type,
              weight, base_value, durability, flags, wear_slots, stacking_rules,
              usage_restrictions, effect_components, metadata, tags
            ) VALUES (
              $1, 'Sanitarium Daisy', 'a pale sanitarium daisy',
              'A wan white daisy from the sanitarium courtyard; Dr. Morgan uses them in calming tisanes.',
              'quest', 0.05, 1, NULL, '[]'::jsonb, '[]'::jsonb, '{"max_stack": 50}'::jsonb,
              '{}'::jsonb, '[]'::jsonb,
              '{"lore": "Cultivated in the sanitarium courtyard for medicinal infusions"}'::jsonb,
              '["misc", "herb", "quest"]'::jsonb
            )
            ON CONFLICT (prototype_id) DO UPDATE SET
              name = EXCLUDED.name,
              short_description = EXCLUDED.short_description,
              long_description = EXCLUDED.long_description,
              item_type = EXCLUDED.item_type,
              weight = EXCLUDED.weight,
              base_value = EXCLUDED.base_value,
              stacking_rules = EXCLUDED.stacking_rules,
              metadata = EXCLUDED.metadata,
              tags = EXCLUDED.tags
            """,
            ITEM_PROTOTYPE_ID,
        )
        _ = await conn.execute(
            """
            INSERT INTO quest_definitions (id, definition)
            VALUES ($1, $2::jsonb)
            ON CONFLICT (id) DO UPDATE SET
              definition = EXCLUDED.definition,
              updated_at = now()
            """,
            QUEST_ID,
            json.dumps(QUEST_DEFINITION),
        )
        _ = await conn.execute(
            """
            INSERT INTO quest_offers (quest_id, offer_entity_type, offer_entity_id)
            VALUES ($1, 'npc', $2)
            ON CONFLICT (quest_id, offer_entity_type, offer_entity_id) DO NOTHING
            """,
            QUEST_ID,
            NPC_SPAWN_ID,
        )
        _ = await conn.execute(
            """
            DELETE FROM quest_instances
            WHERE quest_id = $1
              AND player_id IN (
                SELECT player_id FROM players WHERE name IN ('ArkanWolfshade', 'Ithaqua')
              )
            """,
            QUEST_ID,
        )
    finally:
        await conn.close()


def main() -> None:
    """Entry point: ensure collect_n quest seed and clear instances via anyio."""
    run(_reset_collect_n_quest)


if __name__ == "__main__":
    main()
