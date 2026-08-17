"""Game tick processing functions.

This module handles all game tick processing logic, including status effects,
combat, death processing, and periodic maintenance tasks.
"""

from __future__ import annotations

import asyncio
import datetime

from anyio import sleep
from fastapi import FastAPI

from ..config import get_config
from ..config.npc_config import NPCMaintenanceConfig
from ..realtime.connection_manager_api import broadcast_game_event
from ..realtime.envelope import build_event
from ..realtime.login_grace_period import (
    get_login_grace_period_remaining,
    is_player_in_login_grace_period,
)
from ..structured_logging.enhanced_logging_config import get_logger
from ..time.time_service import get_mythos_chronicle
from .game_tick_corpses import cleanup_decayed_corpses
from .game_tick_counter import get_current_tick, reset_current_tick, set_current_tick
from .game_tick_death import (
    _process_dead_players,
    _process_mortally_wounded_player,
    _process_mp_regeneration,
    _process_passive_lucidity_flux,
    _process_single_player_mp_regeneration,
    _validate_mp_regeneration_services,
    process_dp_decay_and_death,
)
from .game_tick_protocols import _app_container
from .game_tick_status_effects import (
    _process_all_status_effects,
    _process_damage_over_time_effect,
    _process_heal_over_time_effect,
    _process_single_effect,
    _update_player_status_effects,
    _validate_and_get_player,
    _validate_app_state_for_status_effects,
    process_player_effects_expiration,
    process_status_effects,
)

logger = get_logger("server.game_tick")

__all__ = [
    "get_current_tick",
    "reset_current_tick",
    "set_current_tick",
    "_process_all_status_effects",
    "_process_damage_over_time_effect",
    "_process_dead_players",
    "_process_heal_over_time_effect",
    "_process_mortally_wounded_player",
    "_process_mp_regeneration",
    "_process_passive_lucidity_flux",
    "_process_single_effect",
    "_process_single_player_mp_regeneration",
    "_update_player_status_effects",
    "_validate_and_get_player",
    "_validate_app_state_for_status_effects",
    "_validate_mp_regeneration_services",
    "process_dp_decay_and_death",
    "process_player_effects_expiration",
    "process_status_effects",
]


def get_tick_interval() -> float:
    """Get the server tick interval from configuration.

    Returns:
        float: Tick interval in seconds
    """
    config = get_config()
    return config.game.server_tick_rate


async def process_combat_tick(app: FastAPI, tick_count: int) -> None:
    """Process combat auto-progression."""
    container = _app_container(app)
    if container is None or container.combat_service is None:
        return

    try:
        await container.combat_service.process_game_tick(tick_count)
    except (AttributeError, KeyError, TypeError, ValueError, RuntimeError) as e:
        logger.error("Error processing combat tick", tick_count=tick_count, error=str(e))


async def process_casting_progress(app: FastAPI, tick_count: int) -> None:
    """Process casting progress for all active spell castings."""
    container = _app_container(app)
    if container is None or container.magic_service is None:
        return

    try:
        await container.magic_service.check_casting_progress(tick_count)
    except (AttributeError, KeyError, TypeError, ValueError, RuntimeError) as e:
        logger.error("Error processing casting progress", tick_count=tick_count, error=str(e))


async def process_npc_maintenance(app: FastAPI, tick_count: int) -> None:
    """Process NPC lifecycle maintenance (every 60 ticks = 1 minute)."""
    container = _app_container(app)
    if container is None or container.npc_lifecycle_manager is None:
        return

    if not NPCMaintenanceConfig.should_run_maintenance(tick_count):
        return

    try:
        npc_lifecycle_manager = container.npc_lifecycle_manager
        logger.debug(
            "Running NPC maintenance",
            tick_count=tick_count,
            has_lifecycle_manager=True,
            respawn_queue_size=len(npc_lifecycle_manager.respawn_queue),
        )
        maintenance_results = npc_lifecycle_manager.periodic_maintenance()
        logger.info("NPC maintenance completed", tick_count=tick_count, **maintenance_results)
    except (AttributeError, KeyError, TypeError, ValueError, RuntimeError) as e:
        logger.error("Error during NPC maintenance", tick_count=tick_count, error=str(e))


async def broadcast_tick_event(app: FastAPI, tick_count: int) -> None:
    """Broadcast game tick event to all connected players."""
    chronicle = get_mythos_chronicle()
    mythos_dt = chronicle.get_current_mythos_datetime()
    components = chronicle.get_calendar_components(mythos_dt)
    mythos_clock = chronicle.format_clock(mythos_dt)

    container = _app_container(app)
    manager = None if container is None else container.connection_manager
    websocket_count = 0 if manager is None else len(manager.player_websockets)

    tick_data: dict[str, object] = {
        "tick_number": tick_count,
        "timestamp": datetime.datetime.now(datetime.UTC).isoformat(),
        "active_players": websocket_count,
        "mythos_datetime": mythos_dt.isoformat(),
        "mythos_clock": mythos_clock,
        "month_name": components.month_name,
        "day_of_month": components.day_of_month,
        "day_name": components.day_name,
        "week_of_month": components.week_of_month,
        "season": components.season,
        "daypart": components.daypart,
        "is_daytime": components.is_daytime,
        "is_witching_hour": components.is_witching_hour,
    }
    logger.debug(
        "Broadcasting game tick",
        tick_count=tick_count,
        player_count=websocket_count,
    )
    await broadcast_game_event("game_tick", tick_data)

    if manager is None:
        logger.debug("Game tick broadcast completed", tick_count=tick_count)
        return

    for player_id in list(manager.player_websockets.keys()):
        try:
            active = is_player_in_login_grace_period(player_id, manager)
            remaining = get_login_grace_period_remaining(player_id, manager)
            effects_data: dict[str, object] = {
                "login_grace_period_active": active,
                "login_grace_period_remaining": round(remaining, 1),
            }
            event = build_event("effects_update", effects_data, player_id=player_id)
            _ = await manager.send_personal_message(player_id, event)
        except (AttributeError, TypeError, ValueError) as e:
            logger.debug(
                "Skip effects_update for player",
                player_id=player_id,
                error=str(e),
            )

    logger.debug("Game tick broadcast completed", tick_count=tick_count)


async def game_tick_loop(app: FastAPI) -> None:
    """Main game tick loop.

    This function runs continuously and handles periodic game updates,
    including broadcasting tick information to connected players.
    """
    tick_count = 0
    tick_interval = get_tick_interval()
    logger.info("Game tick loop started", tick_interval=tick_interval)

    while True:
        try:
            await process_player_effects_expiration(app, tick_count)
            await process_status_effects(app, tick_count)
            logger.debug("Game tick", tick_count=tick_count)
            set_current_tick(tick_count)
            await process_combat_tick(app, tick_count)
            await process_casting_progress(app, tick_count)
            await process_dp_decay_and_death(app, tick_count)
            await process_npc_maintenance(app, tick_count)
            await cleanup_decayed_corpses(app, tick_count)
            # Broadcast tick event every 10 ticks (1 second at 100ms per tick)
            if not tick_count % 10:
                await broadcast_tick_event(app, tick_count)

            # Sleep for tick interval
            await sleep(tick_interval)
            tick_count += 1
        except asyncio.CancelledError:
            logger.info("Game tick loop cancelled")
            break
        except (AttributeError, KeyError, TypeError, ValueError, RuntimeError) as e:
            logger.error("Error in game tick loop", tick_count=tick_count, error=str(e), exc_info=True)
            try:
                await sleep(tick_interval)
            except asyncio.CancelledError:
                logger.info("Game tick loop cancelled during error recovery")
                break
            tick_count += 1
