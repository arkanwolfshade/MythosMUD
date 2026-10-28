#!/usr/bin/env python3
"""
Print one E2E character's state as JSON (read-only; for Playwright assertions).

Usage: uv run python scripts/e2e_player_state.py <character name>
Output: {"current_room_id": ..., "respawn_room_id": ..., "tutorial_instance_id": ..., "bank_items": [item name, ...],
"current_dp": ..., "corruption": ..., "current_lcd": ..., "inventory_items": [item name, ...],
"quests": {quest id: state}, "debrief_pending": bool}
where bank_items is what is in the character's bank deposit box (empty when they have none).

Uses DATABASE_URL and POSTGRES_SEARCH_PATH from the environment (defaults to mythos_e2e), like
e2e_reset_players.py.
"""

import json
import os
import sys

import asyncpg
from anyio import run

LOCATION_KEYS = ("current_room_id", "respawn_room_id", "tutorial_instance_id")


def _json_list(raw: object) -> list[dict[str, object]]:
    """A list of dicts from a JSON text column (empty for NULL or anything else)."""
    loaded: object = json.loads(raw) if isinstance(raw, str) else []
    if not isinstance(loaded, list):
        return []
    return [{str(k): v for k, v in item.items()} for item in loaded if isinstance(item, dict)]


def _stat(stats: object, key: str) -> object:
    parsed: object = json.loads(stats) if isinstance(stats, str) else stats
    return parsed.get(key) if isinstance(parsed, dict) else None


async def _print_state(name: str) -> None:
    database_url = (
        os.environ.get("DATABASE_URL", "").strip() or "postgresql://postgres:Cthulhu1@localhost:5432/mythos_e2e"
    )
    url = database_url.replace("postgresql+asyncpg://", "postgresql://")
    search_path = os.environ.get("POSTGRES_SEARCH_PATH", "").strip() or "mythos_e2e"
    conn = await asyncpg.connect(url, server_settings={"search_path": search_path})
    try:
        row = await conn.fetchrow(
            "SELECT player_id, current_room_id, respawn_room_id, tutorial_instance_id, inventory, stats "
            "FROM players WHERE name = $1",
            name,
        )
        contents: object = None
        lcd: object = None
        quests: list[asyncpg.Record] = []
        debrief_pending = False
        if row is not None:
            contents = await conn.fetchval(
                "SELECT get_container_contents_json(container_instance_id) FROM containers "
                "WHERE source_type = 'bank' AND owner_id = $1",
                row["player_id"],
            )
            lcd = await conn.fetchval("SELECT current_lcd FROM player_lucidity WHERE player_id = $1", row["player_id"])
            quests = await conn.fetch(
                "SELECT quest_id, state FROM quest_instances WHERE player_id = $1", row["player_id"]
            )
            debrief_pending = bool(
                await conn.fetchval(
                    "SELECT 1 FROM lucidity_cooldowns WHERE player_id = $1 AND action_code = 'debrief_pending'",
                    row["player_id"],
                )
            )
    finally:
        await conn.close()
    if row is None:
        print(f"[ERROR] No player named {name}", file=sys.stderr)
        sys.exit(1)
    # asyncpg returns jsonb as text; no box at all means nothing is banked.
    stacks = _json_list(contents)
    state: dict[str, object] = {key: row[key] for key in LOCATION_KEYS}
    state["bank_items"] = [str(stack["item_name"]) for stack in stacks]
    state["current_dp"] = _stat(row["stats"], "current_dp")
    state["corruption"] = _stat(row["stats"], "corruption")
    state["current_lcd"] = lcd
    state["inventory_items"] = [
        str(stack.get("item_name", stack.get("item_id"))) for stack in _json_list(row["inventory"])
    ]
    state["quests"] = {str(quest["quest_id"]): str(quest["state"]) for quest in quests}
    state["debrief_pending"] = debrief_pending
    print(json.dumps(state))


def main() -> None:
    """Entry point."""
    if len(sys.argv) != 2:
        print("Usage: e2e_player_state.py <character name>", file=sys.stderr)
        sys.exit(2)
    run(_print_state, sys.argv[1])


if __name__ == "__main__":
    main()
