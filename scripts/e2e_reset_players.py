#!/usr/bin/env python3
"""
E2E test teardown: reset ArkanWolfshade and Ithaqua to starting room and set current_dp to 50.

Invoked from Playwright global-teardown so that after make test-playwright, both test players
are returned to DEFAULT_RESPAWN_ROOM (see server/constants/spawn_defaults.py) with
stats.current_dp = 50, regardless of test pass/fail.

Uses DATABASE_URL from environment (e.g. from .env.e2e_test); defaults to mythos_e2e if unset.
"""

import importlib.util
import os

import asyncpg
from anyio import run

# Project root is parent of scripts/
_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
_PROJECT_ROOT = os.path.dirname(_SCRIPT_DIR)


def _load_default_respawn_room() -> str:
    """Load DEFAULT_RESPAWN_ROOM from disk so analyzers do not need to resolve the server package."""
    path = os.path.join(_PROJECT_ROOT, "server", "constants", "spawn_defaults.py")
    spec = importlib.util.spec_from_file_location("_mythos_spawn_defaults_exec", path)
    if spec is None or spec.loader is None:
        raise ImportError("Cannot load spawn_defaults from " + path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    # Exec-loaded module has no static attribute types; narrowed by isinstance below.
    raw: object = module.DEFAULT_RESPAWN_ROOM  # pyright: ignore[reportAny]
    if not isinstance(raw, str):
        raise TypeError("DEFAULT_RESPAWN_ROOM must be str")
    return raw


async def _reset_e2e_players() -> None:
    database_url = os.environ.get("DATABASE_URL", "").strip()
    if not database_url:
        database_url = "postgresql://postgres:Cthulhu1@localhost:5432/mythos_e2e"
    # asyncpg expects postgresql://, not postgresql+asyncpg://
    url = database_url.replace("postgresql+asyncpg://", "postgresql://")

    search_path = os.environ.get("POSTGRES_SEARCH_PATH", "").strip() or "mythos_e2e"
    server_settings: dict[str, str] = {"search_path": search_path}

    conn = await asyncpg.connect(url, server_settings=server_settings)
    try:
        room_id: str = _load_default_respawn_room()
        # Reset room and current_dp for E2E test players (by character name).
        # Omit is_deleted filter: E2E DB may use an older schema without that column (migration 016).
        _ = await conn.execute(
            """
            UPDATE players
            SET
                current_room_id = $1,
                stats = jsonb_set(COALESCE(stats, '{}'::jsonb), '{current_dp}', '50'::jsonb)
            WHERE name IN ('ArkanWolfshade', 'Ithaqua')
            """,
            room_id,
        )
    finally:
        await conn.close()


def main() -> None:
    """Entry point: run E2E player reset via anyio."""
    run(_reset_e2e_players)


if __name__ == "__main__":
    main()
