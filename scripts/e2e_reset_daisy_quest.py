#!/usr/bin/env python3
"""Clear gather_sanitarium_daisies quest instances for E2E test players (repeatable ask/turnin)."""

from __future__ import annotations

import os

import asyncpg
from anyio import run


async def _reset_daisy_quest() -> None:
    database_url = os.environ.get("DATABASE_URL", "").strip()
    if not database_url:
        database_url = "postgresql://postgres:Cthulhu1@localhost:5432/mythos_e2e"
    url = database_url.replace("postgresql+asyncpg://", "postgresql://")
    search_path = os.environ.get("POSTGRES_SEARCH_PATH", "").strip() or "mythos_e2e"
    conn = await asyncpg.connect(url, server_settings={"search_path": search_path})
    try:
        _ = await conn.execute(
            """
            DELETE FROM quest_instances
            WHERE quest_id = 'gather_sanitarium_daisies'
              AND player_id IN (
                SELECT player_id FROM players WHERE name IN ('ArkanWolfshade', 'Ithaqua')
              )
            """
        )
    finally:
        await conn.close()


def main() -> None:
    """Entry point: clear daisy quest instances via anyio."""
    run(_reset_daisy_quest)


if __name__ == "__main__":
    main()
