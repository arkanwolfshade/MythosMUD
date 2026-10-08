#!/usr/bin/env python3
"""
E2E test teardown: reset ArkanWolfshade and Ithaqua to starting room and set current_dp to 50.

With --tutorial it also puts E2ETutorial back at the start of the tutorial (see
_reset_tutorial_character), empties the lost-and-found chest and E2ETutorial's bank deposit box;
the tutorial specs call that.

Invoked from Playwright global-teardown so that after make test-playwright, both test players
are returned to DEFAULT_RESPAWN_ROOM (see server/constants/spawn_defaults.py) with
stats.current_dp = 50, regardless of test pass/fail.

Uses DATABASE_URL from environment (e.g. from .env.e2e_test); defaults to mythos_e2e if unset.
"""

import importlib.util
import json
import os
import sys
import uuid

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


TUTORIAL_CHARACTER = "E2ETutorial"
TUTORIAL_BEDROOM = "earth_arkhamcity_sanitarium_room_tutorial_bedroom_001"
TUTORIAL_ITEM_PROTOTYPE = "pack_dark_ages.weapon.sling"


async def _reset_tutorial_character(conn: asyncpg.Connection) -> None:
    """Put E2ETutorial back at the start of the tutorial, holding one Sling, with nothing banked.

    Saved in the bedroom template with no instance, so login goes through the re-entry repair and
    gets a fresh instance; quest rows are deleted so leave_the_tutorial starts again on spawn.
    Both the shared lost-and-found chest and E2ETutorial's deposit box are emptied: what the tutorial
    leaves behind lands in the box, and it would otherwise carry over into the next test.
    """
    player_id: object = await conn.fetchval("SELECT player_id FROM players WHERE name = $1", TUTORIAL_CHARACTER)
    if player_id is None:
        raise RuntimeError(f"{TUTORIAL_CHARACTER} is not seeded; run scripts/seed_e2e_users.py first")
    sling = {
        "item_id": TUTORIAL_ITEM_PROTOTYPE,
        "prototype_id": TUTORIAL_ITEM_PROTOTYPE,
        "item_instance_id": f"e2e-tutorial-sling-{uuid.uuid4().hex[:12]}",
        "item_name": "Sling",
        "slot_type": "backpack",
        "quantity": 1,
    }
    inventory = json.dumps([sling])
    # Both inventory copies, as upsert_player writes them: Player.get_inventory() reads the
    # players.inventory column, while player_inventories.inventory_json is the row joined on load.
    _ = await conn.execute(
        """
        UPDATE players
        SET
            current_room_id = $2,
            respawn_room_id = $2,
            tutorial_instance_id = NULL,
            inventory = $3,
            stats = jsonb_set(
                jsonb_set(COALESCE(stats, '{}'::jsonb), '{current_dp}', '50'::jsonb),
                '{position}',
                '"standing"'::jsonb
            )
        WHERE player_id = $1
        """,
        player_id,
        TUTORIAL_BEDROOM,
        inventory,
    )
    _ = await conn.execute("DELETE FROM quest_instances WHERE player_id = $1", player_id)
    _ = await conn.execute(
        """
        INSERT INTO player_inventories (player_id, inventory_json, equipped_json)
        VALUES ($1, $2, '{}')
        ON CONFLICT (player_id) DO UPDATE SET inventory_json = EXCLUDED.inventory_json, equipped_json = '{}'
        """,
        player_id,
        inventory,
    )
    _ = await conn.execute(
        "SELECT clear_container_contents(container_instance_id) FROM containers "
        "WHERE metadata_json ->> 'role' = 'lost_and_found'"
    )
    _ = await conn.execute(
        "SELECT clear_container_contents(container_instance_id) FROM containers "
        "WHERE source_type = 'bank' AND owner_id = $1",
        player_id,
    )


FOLK_TONIC_COOLDOWN_KEY = "folk_tonic"


async def _clear_folk_tonic_cooldowns(conn: asyncpg.Connection) -> None:
    """Forget the folk tonic cooldown (30 min) for the shared E2E players, so reruns can drink again."""
    _ = await conn.execute(
        """
        DELETE FROM lucidity_cooldowns
        WHERE action_code = $1
            AND player_id IN (SELECT player_id FROM players WHERE name IN ('ArkanWolfshade', 'Ithaqua'))
        """,
        FOLK_TONIC_COOLDOWN_KEY,
    )


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
        # Reset room, DP, and posture. Exit→/rest leaves sitting; cancel does not stand;
        # co-locate DB resets without posture left movement/chat E2E poisoned.
        # Omit is_deleted filter: E2E DB may use an older schema without that column (migration 016).
        _ = await conn.execute(
            """
            UPDATE players
            SET
                current_room_id = $1,
                stats = jsonb_set(
                    jsonb_set(COALESCE(stats, '{}'::jsonb), '{current_dp}', '50'::jsonb),
                    '{position}',
                    '"standing"'::jsonb
                )
            WHERE name IN ('ArkanWolfshade', 'Ithaqua')
            """,
            room_id,
        )
        await _clear_folk_tonic_cooldowns(conn)
        # Opt-in: ordinary resets run on every relog and must not empty the chest mid-test.
        if "--tutorial" in sys.argv[1:]:
            await _reset_tutorial_character(conn)
    finally:
        await conn.close()


def main() -> None:
    """Entry point: run E2E player reset via anyio."""
    run(_reset_e2e_players)


if __name__ == "__main__":
    main()
