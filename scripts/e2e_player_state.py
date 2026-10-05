#!/usr/bin/env python3
"""
Print one E2E character's location state as JSON (read-only; for Playwright assertions).

Usage: uv run python scripts/e2e_player_state.py <character name>
Output: {"current_room_id": ..., "respawn_room_id": ..., "tutorial_instance_id": ...}

Uses DATABASE_URL and POSTGRES_SEARCH_PATH from the environment (defaults to mythos_e2e), like
e2e_reset_players.py.
"""

import json
import os
import sys

import asyncpg
from anyio import run


async def _print_state(name: str) -> None:
    database_url = (
        os.environ.get("DATABASE_URL", "").strip() or "postgresql://postgres:Cthulhu1@localhost:5432/mythos_e2e"
    )
    url = database_url.replace("postgresql+asyncpg://", "postgresql://")
    search_path = os.environ.get("POSTGRES_SEARCH_PATH", "").strip() or "mythos_e2e"
    conn = await asyncpg.connect(url, server_settings={"search_path": search_path})
    try:
        row = await conn.fetchrow(
            "SELECT current_room_id, respawn_room_id, tutorial_instance_id FROM players WHERE name = $1", name
        )
    finally:
        await conn.close()
    if row is None:
        print(f"[ERROR] No player named {name}", file=sys.stderr)
        sys.exit(1)
    print(json.dumps({key: row[key] for key in ("current_room_id", "respawn_room_id", "tutorial_instance_id")}))


def main() -> None:
    """Entry point."""
    if len(sys.argv) != 2:
        print("Usage: e2e_player_state.py <character name>", file=sys.stderr)
        sys.exit(2)
    run(_print_state, sys.argv[1])


if __name__ == "__main__":
    main()
