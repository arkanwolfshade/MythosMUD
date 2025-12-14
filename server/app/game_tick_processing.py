"""Game tick processing functions.

This module handles all game tick processing logic, including status effects,
combat, death processing, and periodic maintenance tasks.
"""

import datetime
import uuid
from typing import TYPE_CHECKING

from fastapi import FastAPI
from sqlalchemy.ext.asyncio import AsyncSession

from ..config import get_config
from ..logging.enhanced_logging_config import get_logger
from ..realtime.connection_manager_api import broadcast_game_event
from ..services.player_respawn_service import LIMBO_ROOM_ID
from ..time.time_service import get_mythos_chronicle

if TYPE_CHECKING:
    from ..container import ApplicationContainer
    from ..models.player import Player

logger = get_logger("server.game_tick")

# Global tick counter for combat system
# NOTE: This remains global for now as it's shared state needed by combat system
# FUTURE: Move to domain layer when implementing Phase 3.3
_current_tick = 0


def get_current_tick() -> int:
    """Get the current game tick."""
    return _current_tick


def reset_current_tick() -> None:
    """Reset the current tick for testing."""
    global _current_tick  # pylint: disable=global-statement
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

    if not (hasattr(app.state, "connection_manager") and app.state.connection_manager):
        return False, None

    return True, container


async def _process_damage_over_time_effect(
    app: FastAPI, container: "ApplicationContainer", player: "Player", effect: dict, remaining: int, player_id: str
) -> bool:
    """Process a damage over time effect.

    Returns:
        True if effect was applied, False otherwise.
    """
    if remaining <= 0:
        return False

    damage = effect.get("damage", 0)
    if damage > 0 and hasattr(app.state, "player_death_service") and container.async_persistence:
        await container.async_persistence.damage_player(player, damage, "status_effect")
        logger.debug("Applied damage over time", player_id=player_id, damage=damage, effect_type=effect.get("type", ""))
        return True
    return False


async def _process_heal_over_time_effect(
    container: "ApplicationContainer", player: "Player", effect: dict, remaining: int, player_id: str
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
    app: FastAPI, container: "ApplicationContainer", player: "Player", effect: dict, player_id: str
) -> tuple[dict | None, bool]:
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
    elif effect_type == "heal_over_time":
        effect_applied = await _process_heal_over_time_effect(container, player, effect, remaining, player_id)
        if remaining > 0:
            return {**effect, "remaining": remaining}, effect_applied
        return None, effect_applied
    elif remaining > 0:
        return {**effect, "remaining": remaining}, False

    return None, False


async def _update_player_status_effects(
    container: "ApplicationContainer",
    player: "Player",
    updated_effects: list,
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


async def _process_player_status_effects(app: FastAPI, container: "ApplicationContainer", player_id: str) -> bool:
    """Process status effects for a single player.

    Returns:
        True if player was processed and updated, False otherwise.
    """
    try:
        if not container.async_persistence:
            return False
        # Convert player_id from str to UUID
        try:
            player_uuid = uuid.UUID(player_id) if isinstance(player_id, str) else player_id
        except (ValueError, AttributeError):
            logger.warning("Invalid player_id format", player_id=player_id)
            return False
        player = await container.async_persistence.get_player_by_id(player_uuid)
        if not player:
            return False

        status_effects = player.get_status_effects()
        if not status_effects:
            return False

        updated_effects = []
        effect_applied = False
        original_count = len(status_effects)

        for effect in status_effects:
            updated_effect, was_applied = await _process_single_effect(app, container, player, effect, player_id)
            if updated_effect is not None:
                updated_effects.append(updated_effect)
            if was_applied:
                effect_applied = True

        return await _update_player_status_effects(container, player, updated_effects, original_count, effect_applied)
    except (AttributeError, KeyError, TypeError, ValueError, RuntimeError) as e:
        logger.warning("Error processing status effects for player", player_id=player_id, error=str(e))
        return False


async def process_status_effects(app: FastAPI, tick_count: int) -> None:
    """Process status effects for online players."""
    is_valid, container = _validate_app_state_for_status_effects(app)
    if not is_valid:
        return

    try:
        online_player_ids = list(app.state.connection_manager.online_players.keys())
        if not online_player_ids:
            return

        processed_count = 0
        if container:
            for player_id in online_player_ids:
                if await _process_player_status_effects(app, container, player_id):
                    processed_count += 1

        if processed_count > 0:
            logger.debug("Processed status effects", tick_count=tick_count, players_processed=processed_count)
    except (AttributeError, KeyError, TypeError, ValueError, RuntimeError) as e:
        logger.warning("Error processing status/effect ticks", tick_count=tick_count, error=str(e))


async def process_combat_tick(app: FastAPI, tick_count: int) -> None:
    """Process combat auto-progression."""
    if hasattr(app.state, "combat_service"):
        try:
            await app.state.combat_service.process_game_tick(tick_count)
        except (AttributeError, KeyError, TypeError, ValueError, RuntimeError) as e:
            logger.error("Error processing combat tick", tick_count=tick_count, error=str(e))


async def process_casting_progress(app: FastAPI, tick_count: int) -> None:
    """Process casting progress for all active spell castings."""
    if hasattr(app.state, "magic_service") and app.state.magic_service:
        try:
            await app.state.magic_service.check_casting_progress(tick_count)
        except (AttributeError, KeyError, TypeError, ValueError, RuntimeError) as e:
            logger.error("Error processing casting progress", tick_count=tick_count, error=str(e))


async def _process_mortally_wounded_player(app: FastAPI, player: "Player", session: AsyncSession) -> None:
    """Process a single mortally wounded player's DP decay and death check."""
    await app.state.player_death_service.process_mortally_wounded_tick(player.player_id, session)

    await session.refresh(player)
    stats = player.get_stats()
    new_dp = stats.get("current_dp", 0)

    if hasattr(app.state, "combat_service"):
        from ..services.combat_messaging_integration import combat_messaging_integration

        await combat_messaging_integration.send_dp_decay_message(str(player.player_id), new_dp)

    if new_dp <= -10:
        logger.info(
            "Player reached death threshold",
            player_id=player.player_id,
            player_name=player.name,
            current_dp=new_dp,
        )

        await app.state.player_death_service.handle_player_death(
            player.player_id, player.current_room_id, None, session
        )

        await app.state.player_respawn_service.move_player_to_limbo(player.player_id, player.current_room_id, session)


async def _process_mortally_wounded_players(app: FastAPI, session: AsyncSession, tick_count: int) -> None:
    """Process all mortally wounded players."""
    mortally_wounded = await app.state.player_death_service.get_mortally_wounded_players(session)

    if not mortally_wounded:
        return

    logger.debug(
        "Processing DP decay for mortally wounded players",
        tick_count=tick_count,
        player_count=len(mortally_wounded),
    )

    for player in mortally_wounded:
        await _process_mortally_wounded_player(app, player, session)


async def _process_passive_lucidity_flux(app: FastAPI, session: AsyncSession, tick_count: int) -> None:
    """Process passive lucidity flux service if available."""
    if not hasattr(app.state, "passive_lucidity_flux_service"):
        return

    try:
        await app.state.passive_lucidity_flux_service.process_tick(
            session=session, tick_count=tick_count, now=datetime.datetime.now(datetime.UTC)
        )
    except (AttributeError, KeyError, TypeError, ValueError, RuntimeError) as lcd_flux_error:
        logger.error("Error processing passive LCD flux", tick_count=tick_count, error=str(lcd_flux_error))


async def _process_mp_regeneration(app: FastAPI, _session: AsyncSession, tick_count: int) -> None:
    """Process MP regeneration for online players."""
    if not hasattr(app.state, "mp_regeneration_service"):
        return

    if not hasattr(app.state, "connection_manager"):
        return

    try:
        online_player_ids = list(app.state.connection_manager.online_players.keys())
        if not online_player_ids:
            return

        mp_service = app.state.mp_regeneration_service
        processed_count = 0

        for player_id_str in online_player_ids:
            try:
                player_uuid = uuid.UUID(player_id_str) if isinstance(player_id_str, str) else player_id_str
                result = await mp_service.process_tick_regeneration(player_uuid)
                if result.get("mp_restored", 0) > 0:
                    processed_count += 1
            except (ValueError, AttributeError, TypeError) as e:
                logger.warning("Error processing MP regeneration for player", player_id=player_id_str, error=str(e))
                continue

        if processed_count > 0:
            logger.debug("Processed MP regeneration", tick_count=tick_count, players_processed=processed_count)
    except (AttributeError, KeyError, TypeError, ValueError, RuntimeError) as mp_regen_error:
        logger.error("Error processing MP regeneration", tick_count=tick_count, error=str(mp_regen_error))


async def _process_dead_players(app: FastAPI, session: AsyncSession) -> None:
    """Process dead players and move them to limbo if needed."""
    dead_players = await app.state.player_death_service.get_dead_players(session)

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

            await app.state.player_respawn_service.move_player_to_limbo(
                player.player_id, player.current_room_id, session
            )


async def _process_session_dp_decay_and_death(app: FastAPI, session: AsyncSession, tick_count: int) -> None:
    """Process DP decay and death for a single database session."""
    await _process_mortally_wounded_players(app, session, tick_count)
    await _process_passive_lucidity_flux(app, session, tick_count)
    await _process_mp_regeneration(app, session, tick_count)
    await _process_dead_players(app, session)


async def process_dp_decay_and_death(app: FastAPI, tick_count: int) -> None:
    """Process DP decay for mortally wounded players and handle deaths."""
    if not hasattr(app.state, "player_death_service"):
        return

    try:
        from ..database import get_async_session

        async for session in get_async_session():
            try:
                await _process_session_dp_decay_and_death(app, session, tick_count)
            except (AttributeError, KeyError, TypeError, ValueError, RuntimeError) as e:
                logger.error("Error in DP decay processing", tick_count=tick_count, error=str(e))
    except (AttributeError, KeyError, TypeError, ValueError, RuntimeError) as e:
        logger.error("Error getting database session for DP decay", tick_count=tick_count, error=str(e))


async def process_npc_maintenance(app: FastAPI, tick_count: int) -> None:
    """Process NPC lifecycle maintenance (every 60 ticks = 1 minute)."""
    from ..config.npc_config import NPCMaintenanceConfig

    if NPCMaintenanceConfig.should_run_maintenance(tick_count) and hasattr(app.state, "npc_lifecycle_manager"):
        try:
            logger.debug(
                "Running NPC maintenance",
                tick_count=tick_count,
                has_lifecycle_manager=True,
                respawn_queue_size=len(app.state.npc_lifecycle_manager.respawn_queue),
            )
            maintenance_results = app.state.npc_lifecycle_manager.periodic_maintenance()
            logger.info("NPC maintenance completed", tick_count=tick_count, **maintenance_results)
        except (AttributeError, KeyError, TypeError, ValueError, RuntimeError) as e:
            logger.error("Error during NPC maintenance", tick_count=tick_count, error=str(e))


async def cleanup_decayed_corpses(app: FastAPI, tick_count: int) -> None:
    """Cleanup decayed corpse containers (every 60 ticks = 1 minute)."""
    if tick_count % 60 != 0:
        return

    try:
        from ..services.corpse_lifecycle_service import CorpseLifecycleService

        persistence = app.state.container.persistence
        connection_manager = app.state.container.connection_manager
        time_service = get_mythos_chronicle()

        corpse_service = CorpseLifecycleService(
            persistence=persistence,
            connection_manager=connection_manager,
            time_service=time_service,
        )

        decayed = await corpse_service.get_all_decayed_corpses()
        cleaned_count = 0

        for corpse in decayed:
            try:
                if connection_manager and corpse.room_id:
                    from ..services.container_websocket_events import emit_container_decayed

                    await emit_container_decayed(
                        connection_manager=connection_manager,
                        container_id=corpse.container_id,
                        room_id=corpse.room_id,
                    )

                await corpse_service.cleanup_decayed_corpse(corpse.container_id)
                cleaned_count += 1
            except (AttributeError, KeyError, TypeError, ValueError, RuntimeError) as cleanup_error:
                logger.error(
                    "Error cleaning up individual decayed corpse",
                    error=str(cleanup_error),
                    container_id=str(corpse.container_id),
                    exc_info=True,
                )
                continue

        if cleaned_count > 0:
            logger.info(
                "Decayed corpses cleaned up",
                tick_count=tick_count,
                cleaned_count=cleaned_count,
                total_decayed=len(decayed),
            )
    except (AttributeError, KeyError, TypeError, ValueError, RuntimeError) as corpse_cleanup_error:
        logger.warning(
            "Error cleaning up decayed corpses",
            error=str(corpse_cleanup_error),
            tick_count=tick_count,
            exc_info=True,
        )


async def broadcast_tick_event(app: FastAPI, tick_count: int) -> None:
    """Broadcast game tick event to all connected players."""
    tick_data = {
        "tick_number": tick_count,
        "timestamp": datetime.datetime.now(datetime.UTC).isoformat(),
        "active_players": len(app.state.container.connection_manager.player_websockets),
    }
    logger.debug(
        "Broadcasting game tick",
        tick_count=tick_count,
        player_count=len(app.state.container.connection_manager.player_websockets),
    )
    await broadcast_game_event("game_tick", tick_data)
    logger.debug("Game tick broadcast completed", tick_count=tick_count)


async def game_tick_loop(app: FastAPI):
    """Main game tick loop.

    This function runs continuously and handles periodic game updates,
    including broadcasting tick information to connected players.
    """
    import asyncio

    global _current_tick  # pylint: disable=global-statement
    tick_count = 0
    tick_interval = get_tick_interval()
    logger.info("Game tick loop started", tick_interval=tick_interval)

    while True:
        try:
            await process_status_effects(app, tick_count)
            logger.debug("Game tick", tick_count=tick_count)
            _current_tick = tick_count
            await process_combat_tick(app, tick_count)
            await process_casting_progress(app, tick_count)
            await process_dp_decay_and_death(app, tick_count)
            await process_npc_maintenance(app, tick_count)
            await cleanup_decayed_corpses(app, tick_count)
            await broadcast_tick_event(app, tick_count)

            # Sleep for tick interval
            await asyncio.sleep(tick_interval)
            tick_count += 1
        except asyncio.CancelledError:
            logger.info("Game tick loop cancelled")
            break
        except (AttributeError, KeyError, TypeError, ValueError, RuntimeError) as e:
            logger.error("Error in game tick loop", tick_count=tick_count, error=str(e), exc_info=True)
            try:
                await asyncio.sleep(tick_interval)
            except asyncio.CancelledError:
                logger.info("Game tick loop cancelled during error recovery")
                break
            tick_count += 1
