#!/usr/bin/env python3
"""
E2E test setup: clear ArkanWolfshade's corruption recovery cooldowns (e.g. `/cleanse`).

`corruption-cleanse.spec.ts` seeds corruption and performs a real cleanse, which sets a 6-hour
DB-persisted cooldown (server/services/corruption_service.py's RECOVERY_ACTIONS; table
corruption_cooldowns). That cooldown outlives the test run -- a full `mythos_e2e` bootstrap
clears it, but re-running this spec (or the full suite) without one hits the still-active
cooldown and the "crosses a tier" test fails looking for a success message the server never
sends. Invoked from the spec's beforeAll so repeat runs are idempotent without a DB recreate.

Uses DATABASE_URL from environment (e.g. from .env.e2e_test); defaults to mythos_e2e if unset.
"""

import os

import asyncpg
from anyio import run


async def _reset_corruption_cooldowns() -> None:
    database_url = os.environ.get("DATABASE_URL", "").strip()
    if not database_url:
        database_url = "postgresql://postgres:Cthulhu1@localhost:5432/mythos_e2e"
    # asyncpg expects postgresql://, not postgresql+asyncpg://
    url = database_url.replace("postgresql+asyncpg://", "postgresql://")

    search_path = os.environ.get("POSTGRES_SEARCH_PATH", "").strip() or "mythos_e2e"
    server_settings: dict[str, str] = {"search_path": search_path}

    conn = await asyncpg.connect(url, server_settings=server_settings)
    try:
        _ = await conn.execute(
            """
            DELETE FROM corruption_cooldowns
            WHERE player_id IN (SELECT player_id FROM players WHERE name = 'ArkanWolfshade')
            """
        )
    finally:
        await conn.close()


def main() -> None:
    """Entry point: run corruption cooldown reset via anyio."""
    run(_reset_corruption_cooldowns)


if __name__ == "__main__":
    main()
