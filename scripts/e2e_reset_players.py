#!/usr/bin/env python3
"""
E2E test teardown: reset ArkanWolfshade and Ithaqua to starting room and set current_dp to 50.

Invoked from Playwright global-teardown so that after make test-playwright, both test players
are returned to earth_arkhamcity_sanitarium_room_foyer_001 with stats.current_dp = 50,
regardless of test pass/fail.

Uses DATABASE_URL from environment (e.g. from .env.e2e_test); defaults to mythos_e2e if unset.
"""

import os
import sys

from anyio import run

# Project root is parent of scripts/
_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
_PROJECT_ROOT = os.path.dirname(_SCRIPT_DIR)
if _PROJECT_ROOT not in sys.path:
    sys.path.insert(0, _PROJECT_ROOT)


async def _reset_e2e_players() -> None:
    database_url = os.environ.get("DATABASE_URL", "").strip()
    if not database_url:
        database_url = "postgresql://postgres:Cthulhu1@localhost:5432/mythos_e2e"
    # asyncpg expects postgresql://, not postgresql+asyncpg://
    url = database_url.replace("postgresql+asyncpg://", "postgresql://")

    import asyncpg

    conn = await asyncpg.connect(url)
    try:
        # Reset room and current_dp for E2E test players (by character name).
        # Omit is_deleted filter: E2E DB may use an older schema without that column (migration 016).
        await conn.execute(
            """
            UPDATE players
            SET
                current_room_id = $1,
                stats = jsonb_set(COALESCE(stats, '{}'::jsonb), '{current_dp}', '50'::jsonb)
            WHERE name IN ('ArkanWolfshade', 'Ithaqua')
            """,
            "earth_arkhamcity_sanitarium_room_foyer_001",
        )
    finally:
        await conn.close()


def main() -> None:
    """Entry point: run E2E player reset via anyio."""
    run(_reset_e2e_players)


if __name__ == "__main__":
    main()
