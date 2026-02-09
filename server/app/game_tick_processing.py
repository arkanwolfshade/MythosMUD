"""Game tick processing functions.

This module handles all game tick processing logic, including status effects,
combat, death processing, and periodic maintenance tasks.
"""

# pylint: disable=too-many-lines  # Reason: Game tick processing module requires extensive logic for status effects, MP regeneration, corpse cleanup, death processing, and all periodic game maintenance tasks

import asyncio
import datetime
import uuid
from typing import TYPE_CHECKING, Any, cast

from anyio import sleep
from fastapi import FastAPI
from sqlalchemy.ext.asyncio import AsyncSession

from ..config import get_config
from ..config.npc_config import NPCMaintenanceConfig
from ..database import get_async_session
from ..realtime.connection_manager_api import broadcast_game_event
from ..realtime.login_grace_period import (
    _grace_period_expiration_handler,
    get_login_grace_period_remaining,
    is_player_in_login_grace_period,
)
from ..services.combat_messaging_integration import combat_messaging_integration
from ..services.container_websocket_events import emit_container_decayed
from ..services.corpse_lifecycle_service import CorpseLifecycleService
from ..services.player_respawn_service import LIMBO_ROOM_ID
from ..structured_logging.enhanced_logging_config import get_logger
from ..time.time_service import get_mythos_chronicle

if TYPE_CHECKING:
    from ..container import ApplicationContainer
    from ..models.player import Player

logger = get_logger("server.game_tick")

# Global tick counter for combat system
# NOTE: This remains global for now as it's shared state needed by combat system
# FUTURE: Move to domain layer when implementing Phase 3.3
_current_tick = 0  # pylint: disable=invalid-name  # noqa: N816  # Reason: Mutable module-level variable, not a constant


def get_current_tick() -> int:
    """Get the current game tick."""
    return _current_tick


def reset_current_tick() -> None:
    """Reset the current tick for testing."""
    global _current_tick  # pylint: disable=global-statement  # Reason: Module-level tick counter must be mutable for testing and game state tracking
    _current_tick = 0


def get_tick_interval() -> float:
    """Get the server tick interval from configuration.

    Returns:
        float: Tick interval in seconds
    """
    config = get_config()
    return config.game.server_tick_rate


def _validate_app_state_for_status_effects(app: FastAPI) -> tuple[bool, "ApplicationContainer | None"]:
    """Validate app state has required components for status effect processing.

    Returns:
        Tuple of (is_valid, container) where is_valid indicates if processing can proceed.
    """
    if not (hasattr(app.state, "container") and app.state.container):
        return False, None

    container = app.state.container
    if not container.async_persistence:
        return False, None

    if not container.connection_manager:
        return False, None

    return True, container


async def _process_damage_over_time_effect(  # pylint: disable=too-many-arguments,too-many-positional-arguments  # Reason: Effect processing requires many parameters for game state and effect context
    _app: FastAPI,
    container: "ApplicationContainer",
    player: "Player",
    effect: dict[str, Any],
    remaining: int,
    player_id: str,
) -> bool:
    """Process a damage over time effect.

    Returns:
        True if effect was applied, False otherwise.
    """
    if remaining <= 0:
        return False

    # Check if player is in login grace period - block negative effects
    try:
        if container.connection_manager:
            player_uuid = uuid.UUID(player_id) if isinstance(player_id, str) else player_id
            if is_player_in_login_grace_period(player_uuid, container.connection_manager):
                logger.debug(
                    "Damage over time effect blocked - player in login grace period",
                    player_id=player_id,
                    effect_type=effect.get("type", ""),
                )
                return False  # Effect blocked
    except (AttributeError, ImportError, TypeError, ValueError) as e:
        # If we can't check grace period, proceed with effect (fail open)
        logger.debug("Could not check login grace period for damage over time", player_id=player_id, error=str(e))

    damage = effect.get("damage", 0)
    if damage > 0 and container.async_persistence:
        await container.async_persistence.damage_player(player, damage, "status_effect")
        logger.debug("Applied damage over time", player_id=player_id, damage=damage, effect_type=effect.get("type", ""))
        return True
    return False


async def _process_heal_over_time_effect(
    container: "ApplicationContainer", player: "Player", effect: dict[str, Any], remaining: int, player_id: str
) -> bool:
    """Process a heal over time effect.

    Returns:
        True if effect was applied, False otherwise.
    """
    if remaining <= 0:
        return False

    healing = effect.get("healing", 0)
    if healing > 0 and container.async_persistence:
        await container.async_persistence.heal_player(player, healing)
        logger.debug("Applied heal over time", player_id=player_id, healing=healing, effect_type=effect.get("type", ""))
        return True
    return False


async def _process_single_effect(
    app: FastAPI, container: "ApplicationContainer", player: "Player", effect: dict[str, Any], player_id: str
) -> tuple[dict[str, Any] | None, bool]:
    """Process a single status effect.

    Returns:
        Tuple of (updated_effect_dict or None if expired, effect_applied) where effect_applied indicates if the effect had an impact.
    """
    effect_type = effect.get("type", "")
    duration = effect.get("duration", 0)
    remaining = effect.get("remaining", duration) - 1
    effect_applied = False

    if effect_type == "damage_over_time":
        effect_applied = await _process_damage_over_time_effect(app, container, player, effect, remaining, player_id)
        if remaining > 0:
            return {**effect, "remaining": remaining}, effect_applied
        return None, effect_applied
    if effect_type == "heal_over_time":
        effect_applied = await _process_heal_over_time_effect(container, player, effect, remaining, player_id)
        if remaining > 0:
            return {**effect, "remaining": remaining}, effect_applied
        return None, effect_applied
    if remaining > 0:
        return {**effect, "remaining": remaining}, False

    return None, False


async def _update_player_status_effects(
    container: "ApplicationContainer",
    player: "Player",
    updated_effects: list[dict[str, Any]],
    original_count: int,
    effect_applied: bool,
) -> bool:
    """Update and save player status effects if changes occurred.

    Returns:
        True if player was updated, False otherwise.
    """
    effects_changed = len(updated_effects) != original_count
    if (effects_changed or effect_applied) and container.async_persistence:
        player.set_status_effects(updated_effects)
        await container.async_persistence.save_player(player)
        return True
    return False


async def _validate_and_get_player(
    container: "ApplicationContainer", player_id: str
) -> tuple["Player | None", uuid.UUID | None]:
    """
    Validate container and retrieve player by ID.

    Args:
        container: Application container
        player_id: Player ID as string

    Returns:
        Tuple of (player object or None, player_uuid or None)
    """
    if not container.async_persistence:
        return None, None

    # Convert player_id from str to UUID
    try:
        player_uuid = uuid.UUID(player_id) if isinstance(player_id, str) else player_id
    except (ValueError, AttributeError):
        logger.warning("Invalid player_id format", player_id=player_id)
        return None, None

    player = await container.async_persistence.get_player_by_id(player_uuid)
    return player, player_uuid


async def _process_all_status_effects(
    app: FastAPI, container: "ApplicationContainer", player: "Player", player_id: str
) -> tuple[list[dict[str, Any]], bool, int]:
    """
    Process all status effects for a player.

    Args:
        app: FastAPI application
        container: Application container
        player: Player object
        player_id: Player ID as string

    Returns:
        Tuple of (updated_effects list, effect_applied bool, original_count int)
    """
    status_effects = player.get_status_effects()
    if not status_effects:
        return [], False, 0

    updated_effects = []
    effect_applied = False
    original_count = len(status_effects)

    for effect in status_effects:
        updated_effect, was_applied = await _process_single_effect(app, container, player, effect, player_id)
        if updated_effect is not None:
            updated_effects.append(updated_effect)
        if was_applied:
            effect_applied = True

    return updated_effects, effect_applied, original_count


async def _process_player_status_effects(app: FastAPI, container: "ApplicationContainer", player_id: str) -> bool:
    """Process status effects for a single player.

    Returns:
        True if player was processed and updated, False otherwise.
    """
    try:
        player, _ = await _validate_and_get_player(container, player_id)
        if not player:
            return False

        updated_effects, effect_applied, original_count = await _process_all_status_effects(
            app, container, player, player_id
        )

        return await _update_player_status_effects(container, player, updated_effects, original_count, effect_applied)
    except (AttributeError, KeyError, TypeError, ValueError, RuntimeError) as e:
        logger.warning("Error processing status effects for player", player_id=player_id, error=str(e))
        return False


async def process_player_effects_expiration(app: FastAPI, tick_count: int) -> None:
    """Expire player_effects for this tick; for LOGIN_WARDED clear in-memory state and trigger room update."""
    is_valid, container = _validate_app_state_for_status_effects(app)
    if not is_valid or not container or not container.async_persistence or not container.connection_manager:
        return

    try:
        expired = await container.async_persistence.expire_player_effects_for_tick(tick_count)
        for player_id_str, effect_type in expired:
            if effect_type == "login_warded":
                try:
                    player_uuid = uuid.UUID(player_id_str) if isinstance(player_id_str, str) else player_id_str
                    await _grace_period_expiration_handler(player_uuid, container.connection_manager)
                except (ValueError, AttributeError, TypeError) as e:
                    logger.warning(
                        "Error handling LOGIN_WARDED expiration",
                        player_id=player_id_str,
                        error=str(e),
                    )
    except (AttributeError, KeyError, TypeError, ValueError, RuntimeError) as e:
        logger.warning(
            "Error processing player effects expiration",
            tick_count=tick_count,
            error=str(e),
        )


async def process_status_effects(app: FastAPI, tick_count: int) -> None:
    """Process status effects for online players."""
    is_valid, container = _validate_app_state_for_status_effects(app)
    if not is_valid or not container or not container.connection_manager:
        return

    try:
        online_player_ids = list(container.connection_manager.online_players.keys())
        if not online_player_ids:
            return

        processed_count = 0
        for player_id in online_player_ids:
            # Convert player_id to string (online_players.keys() returns UUIDs)
            player_id_str = str(player_id)
            if await _process_player_status_effects(app, container, player_id_str):
                processed_count += 1

        if processed_count > 0:
            logger.debug("Processed status effects", tick_count=tick_count, players_processed=processed_count)
    except (AttributeError, KeyError, TypeError, ValueError, RuntimeError) as e:
        logger.warning("Error processing status/effect ticks", tick_count=tick_count, error=str(e))


async def process_combat_tick(app: FastAPI, tick_count: int) -> None:
    """Process combat auto-progression."""
    if not (hasattr(app.state, "container") and app.state.container and app.state.container.combat_service):
        return

    try:
        await app.state.container.combat_service.process_game_tick(tick_count)
    except (AttributeError, KeyError, TypeError, ValueError, RuntimeError) as e:
        logger.error("Error processing combat tick", tick_count=tick_count, error=str(e))


async def process_casting_progress(app: FastAPI, tick_count: int) -> None:
    """Process casting progress for all active spell castings."""
    if not (hasattr(app.state, "container") and app.state.container and app.state.container.magic_service):
        return

    try:
        await app.state.container.magic_service.check_casting_progress(tick_count)
    except (AttributeError, KeyError, TypeError, ValueError, RuntimeError) as e:
        logger.error("Error processing casting progress", tick_count=tick_count, error=str(e))


async def _process_mortally_wounded_player(
    container: "ApplicationContainer", player: "Player", session: AsyncSession
) -> None:
    """Process a single mortally wounded player's DP decay and death check."""
    if not container.player_death_service:
        return

    await container.player_death_service.process_mortally_wounded_tick(player.player_id, session)

    await session.refresh(player)
    stats = player.get_stats()
    new_dp = stats.get("current_dp", 0)

    if container.combat_service:
        await combat_messaging_integration.send_dp_decay_message(str(player.player_id), new_dp)

    if new_dp <= -10:
        logger.info(
            "Player reached death threshold",
            player_id=player.player_id,
            player_name=player.name,
            current_dp=new_dp,
        )

        if not container.player_respawn_service:
            return

        await container.player_death_service.handle_player_death(
            player.player_id, player.current_room_id, None, session
        )

        await container.player_respawn_service.move_player_to_limbo(player.player_id, player.current_room_id, session)


async def _process_mortally_wounded_players(
    container: "ApplicationContainer", session: AsyncSession, tick_count: int
) -> None:
    """Process all mortally wounded players."""
    if not container.player_death_service:
        return

    mortally_wounded = await container.player_death_service.get_mortally_wounded_players(session)

    if not mortally_wounded:
        return

    logger.debug(
        "Processing DP decay for mortally wounded players",
        tick_count=tick_count,
        player_count=len(mortally_wounded),
    )

    for player in mortally_wounded:
        await _process_mortally_wounded_player(container, player, session)


async def _process_passive_lucidity_flux(
    container: "ApplicationContainer", session: AsyncSession, tick_count: int
) -> None:
    """Process passive lucidity flux service if available."""
    if not container.passive_lucidity_flux_service:
        return

    try:
        await container.passive_lucidity_flux_service.process_tick(
            session=session, tick_count=tick_count, now=datetime.datetime.now(datetime.UTC)
        )
    except (AttributeError, KeyError, TypeError, ValueError, RuntimeError) as lcd_flux_error:
        logger.error("Error processing passive LCD flux", tick_count=tick_count, error=str(lcd_flux_error))


def _validate_mp_regeneration_services(container: "ApplicationContainer") -> bool:
    """
    Validate that required services exist for MP regeneration.

    Args:
        container: Application container

    Returns:
        True if services are available, False otherwise
    """
    return container.mp_regeneration_service is not None and container.connection_manager is not None


async def _process_single_player_mp_regeneration(mp_service: Any, player_id_str: str) -> bool:
    """
    Process MP regeneration for a single player.

    Args:
        mp_service: MP regeneration service instance
        player_id_str: Player ID as string

    Returns:
        True if MP was restored, False otherwise
    """
    try:
        player_uuid = uuid.UUID(player_id_str) if isinstance(player_id_str, str) else player_id_str
        result = await mp_service.process_tick_regeneration(player_uuid)
        return cast(bool, result.get("mp_restored", 0) > 0)
    except (ValueError, AttributeError, TypeError) as e:
        logger.warning("Error processing MP regeneration for player", player_id=player_id_str, error=str(e))
        return False


async def _process_mp_regeneration(container: "ApplicationContainer", _session: AsyncSession, tick_count: int) -> None:
    """Process MP regeneration for online players."""
    if not _validate_mp_regeneration_services(container) or not container.connection_manager:
        return

    try:
        online_player_ids = list(container.connection_manager.online_players.keys())
        if not online_player_ids:
            return

        mp_service = container.mp_regeneration_service
        if not mp_service:
            return

        processed_count = 0

        for player_id in online_player_ids:
            # Convert player_id to string (online_players.keys() returns UUIDs)
            player_id_str = str(player_id)
            if await _process_single_player_mp_regeneration(mp_service, player_id_str):
                processed_count += 1

        if processed_count > 0:
            logger.debug("Processed MP regeneration", tick_count=tick_count, players_processed=processed_count)
    except (AttributeError, KeyError, TypeError, ValueError, RuntimeError) as mp_regen_error:
        logger.error("Error processing MP regeneration", tick_count=tick_count, error=str(mp_regen_error))


async def _process_dead_players(container: "ApplicationContainer", session: AsyncSession) -> None:
    """Process dead players and move them to limbo if needed."""
    if not container.player_death_service or not container.player_respawn_service:
        return

    dead_players = await container.player_death_service.get_dead_players(session)

    if not dead_players:
        return

    logger.debug("Found dead players", count=len(dead_players), player_ids=[p.player_id for p in dead_players])

    for player in dead_players:
        if str(player.current_room_id) != LIMBO_ROOM_ID:
            logger.info(
                "Moving dead player to limbo",
                player_id=player.player_id,
                player_name=player.name,
                current_room_id=player.current_room_id,
            )

            await container.player_respawn_service.move_player_to_limbo(
                player.player_id, player.current_room_id, session
            )


async def _process_session_dp_decay_and_death(
    container: "ApplicationContainer", session: AsyncSession, tick_count: int
) -> None:
    """Process DP decay and death for a single database session."""
    await _process_mortally_wounded_players(container, session, tick_count)
    await _process_passive_lucidity_flux(container, session, tick_count)
    await _process_mp_regeneration(container, session, tick_count)
    await _process_dead_players(container, session)


async def process_dp_decay_and_death(app: FastAPI, tick_count: int) -> None:
    """Process DP decay for mortally wounded players and handle deaths."""
    if not (hasattr(app.state, "container") and app.state.container):
        return

    container = app.state.container
    if not container.player_death_service:
        return

    try:
        async for session in get_async_session():
            try:
                await _process_session_dp_decay_and_death(container, session, tick_count)
            except (AttributeError, KeyError, TypeError, ValueError, RuntimeError) as e:
                logger.error("Error in DP decay processing", tick_count=tick_count, error=str(e))
    except (AttributeError, KeyError, TypeError, ValueError, RuntimeError) as e:
        logger.error("Error getting database session for DP decay", tick_count=tick_count, error=str(e))


async def process_npc_maintenance(app: FastAPI, tick_count: int) -> None:
    """Process NPC lifecycle maintenance (every 60 ticks = 1 minute)."""
    if not (hasattr(app.state, "container") and app.state.container and app.state.container.npc_lifecycle_manager):
        return

    if not NPCMaintenanceConfig.should_run_maintenance(tick_count):
        return

    try:
        npc_lifecycle_manager = app.state.container.npc_lifecycle_manager
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


def _create_corpse_lifecycle_service(app: FastAPI) -> CorpseLifecycleService | None:
    """
    Create and initialize CorpseLifecycleService.

    Args:
        app: FastAPI application

    Returns:
        CorpseLifecycleService instance or None if persistence is unavailable
    """
    persistence = app.state.container.persistence
    if persistence is None:
        return None

    connection_manager = app.state.container.connection_manager
    time_service = get_mythos_chronicle()

    return CorpseLifecycleService(
        persistence=persistence,
        connection_manager=connection_manager,
        time_service=time_service,
    )


async def _cleanup_single_decayed_corpse(
    corpse_service: CorpseLifecycleService,
    connection_manager: Any,
    corpse: Any,
    tick_count: int,
) -> bool:
    """
    Cleanup a single decayed corpse.

    Args:
        corpse_service: Corpse lifecycle service instance
        connection_manager: Connection manager instance
        corpse: Decayed corpse container object
        tick_count: Current game tick count

    Returns:
        True if cleanup was successful, False otherwise
    """
    try:
        if connection_manager and corpse.room_id:
            await emit_container_decayed(
                connection_manager=connection_manager,
                container_id=corpse.container_id,
                room_id=corpse.room_id,
            )

        await corpse_service.cleanup_decayed_corpse(corpse.container_id)
        logger.debug(
            "Cleaned up decayed corpse",
            tick_count=tick_count,
            container_id=str(corpse.container_id),
            room_id=corpse.room_id,
        )
        return True
    except (AttributeError, KeyError, TypeError, ValueError, RuntimeError) as cleanup_error:
        logger.error(
            "Error cleaning up individual decayed corpse",
            error=str(cleanup_error),
            container_id=str(corpse.container_id),
            tick_count=tick_count,
            exc_info=True,
        )
        return False


def _log_cleanup_results(tick_count: int, cleaned_count: int, total_decayed: int) -> None:
    """
    Log the results of corpse cleanup.

    Args:
        tick_count: Current game tick count
        cleaned_count: Number of corpses successfully cleaned
        total_decayed: Total number of decayed corpses found
    """
    if cleaned_count > 0:
        logger.info(
            "Decayed corpses cleaned up",
            tick_count=tick_count,
            cleaned_count=cleaned_count,
            total_decayed=total_decayed,
        )
    elif total_decayed > 0:
        logger.warning(
            "Found decayed corpses but none were cleaned",
            tick_count=tick_count,
            total_decayed=total_decayed,
            cleaned_count=cleaned_count,
        )


async def cleanup_decayed_corpses(app: FastAPI, tick_count: int) -> None:
    """Cleanup decayed corpse containers (every 60 ticks = 1 minute)."""
    if tick_count % 60:
        return

    logger.debug("Running decayed corpse cleanup check", tick_count=tick_count)

    try:
        corpse_service = _create_corpse_lifecycle_service(app)
        if corpse_service is None:
            logger.warning("Persistence layer not available for corpse cleanup", tick_count=tick_count)
            return

        decayed = await corpse_service.get_all_decayed_corpses()
        logger.debug(
            "Decayed corpses check completed",
            tick_count=tick_count,
            decayed_count=len(decayed),
        )

        cleaned_count = 0
        connection_manager = app.state.container.connection_manager

        for corpse in decayed:
            if await _cleanup_single_decayed_corpse(corpse_service, connection_manager, corpse, tick_count):
                cleaned_count += 1

        _log_cleanup_results(tick_count, cleaned_count, len(decayed))
    except (AttributeError, KeyError, TypeError, ValueError, RuntimeError) as corpse_cleanup_error:
        logger.error(
            "Error during decayed corpse cleanup",
            error=str(corpse_cleanup_error),
            tick_count=tick_count,
            exc_info=True,
        )


async def broadcast_tick_event(app: FastAPI, tick_count: int) -> None:
    """Broadcast game tick event to all connected players."""
    # Get current mythos time for UI updates
    chronicle = get_mythos_chronicle()
    mythos_dt = chronicle.get_current_mythos_datetime()
    components = chronicle.get_calendar_components(mythos_dt)
    mythos_clock = chronicle.format_clock(mythos_dt)

    tick_data = {
        "tick_number": tick_count,
        "timestamp": datetime.datetime.now(datetime.UTC).isoformat(),
        "active_players": len(app.state.container.connection_manager.player_websockets),
        # Include mythos time data for UI updates
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
        player_count=len(app.state.container.connection_manager.player_websockets),
    )
    await broadcast_game_event("game_tick", tick_data)

    # Send per-player effects update so client can show countdown and remove effect when expired
    manager = app.state.container.connection_manager
    if manager and getattr(manager, "player_websockets", None):
        from ..realtime.envelope import build_event

        for player_id in list(manager.player_websockets.keys()):
            try:
                active = is_player_in_login_grace_period(player_id, manager)
                remaining = get_login_grace_period_remaining(player_id, manager)
                effects_data = {
                    "login_grace_period_active": active,
                    "login_grace_period_remaining": round(remaining, 1),
                }
                event = build_event("effects_update", effects_data, player_id=player_id)
                await manager.send_personal_message(player_id, event)
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
    global _current_tick  # pylint: disable=global-statement  # Reason: Module-level tick counter must be mutable for game state tracking and synchronization
    tick_count = 0
    tick_interval = get_tick_interval()
    logger.info("Game tick loop started", tick_interval=tick_interval)

    while True:
        try:
            await process_player_effects_expiration(app, tick_count)
            await process_status_effects(app, tick_count)
            logger.debug("Game tick", tick_count=tick_count)
            _current_tick = tick_count
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
