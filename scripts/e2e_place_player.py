#!/usr/bin/env python3
"""
Move one E2E character to a room (for Playwright setup). Only valid while they are logged out.

Usage: uv run python scripts/e2e_place_player.py <character name> <room stable id>

The server keeps a logged-in player's room in memory and saves it back on logout, so this must run
between logout and login. Refuses a room that does not exist, so a typo fails loudly instead of
stranding the character.

Uses DATABASE_URL and POSTGRES_SEARCH_PATH from the environment (defaults to mythos_e2e), like
e2e_reset_players.py.
"""

import os
import sys

import asyncpg
from anyio import run


async def _place(name: str, room_id: str) -> None:
    database_url = (
        os.environ.get("DATABASE_URL", "").strip() or "postgresql://postgres:Cthulhu1@localhost:5432/mythos_e2e"
    )
    url = database_url.replace("postgresql+asyncpg://", "postgresql://")
    search_path = os.environ.get("POSTGRES_SEARCH_PATH", "").strip() or "mythos_e2e"
    conn = await asyncpg.connect(url, server_settings={"search_path": search_path})
    try:
        if await conn.fetchval("SELECT 1 FROM rooms WHERE stable_id = $1", room_id) is None:
            print(f"[ERROR] No room with stable id {room_id}", file=sys.stderr)
            sys.exit(1)
        updated = await conn.fetchval(
            "UPDATE players SET current_room_id = $2 WHERE name = $1 RETURNING player_id", name, room_id
        )
    finally:
        await conn.close()
    if updated is None:
        print(f"[ERROR] No player named {name}", file=sys.stderr)
        sys.exit(1)


def main() -> None:
    """Entry point."""
    if len(sys.argv) != 3:
        print("Usage: e2e_place_player.py <character name> <room stable id>", file=sys.stderr)
        sys.exit(2)
    run(_place, sys.argv[1], sys.argv[2])


if __name__ == "__main__":
    main()
