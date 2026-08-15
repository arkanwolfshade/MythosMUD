"""Game tick processing functions.

This module handles all game tick processing logic, including status effects,
combat, death processing, and periodic maintenance tasks.
"""

# pylint: disable=too-many-lines,missing-class-docstring,missing-function-docstring,too-few-public-methods  # Reason: One tick module; Protocol stubs (PEP 544) are not classes with docs/methods

from __future__ import annotations

import asyncio
import datetime
import uuid
from collections.abc import Mapping
from typing import TYPE_CHECKING, Protocol, cast

from anyio import sleep
from fastapi import FastAPI
from sqlalchemy.ext.asyncio import AsyncSession

from ..config import get_config
from ..config.npc_config import NPCMaintenanceConfig
from ..constants.spawn_defaults import LIMBO_ROOM_ID
from ..database import get_async_session
from ..events.event_types import PlayerDPUpdated
from ..models.combat import CombatInstance, CombatStatus
from ..realtime.connection_manager_api import broadcast_game_event
from ..realtime.envelope import build_event
from ..realtime.login_grace_period import (
    get_login_grace_period_remaining,
    handle_login_grace_period_expiration,
    is_player_in_login_grace_period,
)
from ..services.combat_messaging_integration import combat_messaging_integration
from ..structured_logging.enhanced_logging_config import get_logger
from ..time.time_service import get_mythos_chronicle
from ..utils.int_coercion import coerce_int
from .game_tick_corpses import cleanup_decayed_corpses
from .game_tick_counter import get_current_tick, reset_current_tick, set_current_tick

if TYPE_CHECKING:
    from ..async_persistence import AsyncPersistenceLayer
    from ..models.player import Player
    from ..services.passive_lucidity_flux_service import PassiveLucidityFluxService


class _TickConnectionManager(Protocol):
    online_players: dict[uuid.UUID, dict[str, object]]
    player_websockets: dict[uuid.UUID, list[str]]

    async def send_personal_message(self, player_id: uuid.UUID, event: dict[str, object]) -> dict[str, object]: ...


class _TickCombatService(Protocol):
    async def process_game_tick(self, current_tick: int) -> None: ...

    async def get_combat_by_participant(self, participant_id: uuid.UUID) -> CombatInstance | None: ...


class _TickMagicService(Protocol):
    async def check_casting_progress(self, current_tick: int) -> None: ...


class _TickDeathService(Protocol):
    async def handle_player_death(
        self,
        player_id: uuid.UUID,
        death_location: str,
        killer_info: Mapping[str, object] | None,
        session: AsyncSession,
    ) -> bool: ...

    async def process_mortally_wounded_tick(self, player_id: uuid.UUID, session: AsyncSession) -> bool: ...

    async def get_mortally_wounded_players(self, session: AsyncSession) -> list[Player]: ...

    async def get_dead_players(self, session: AsyncSession) -> list[Player]: ...


class _TickRespawnService(Protocol):
    async def move_player_to_limbo(self, player_id: uuid.UUID, death_location: str, session: AsyncSession) -> bool: ...


class _TickEventBus(Protocol):
    def publish(self, event: object) -> None: ...


class _TickMpRegen(Protocol):
    async def process_tick_regeneration(self, player_id: uuid.UUID) -> Mapping[str, object]: ...


class _TickNpcLifecycle(Protocol):
    respawn_queue: dict[str, Mapping[str, object]]

    def periodic_maintenance(self) -> dict[str, object]: ...


class _TickContainer(Protocol):
    async_persistence: AsyncPersistenceLayer | None
    connection_manager: _TickConnectionManager | None
    combat_service: _TickCombatService | None
    magic_service: _TickMagicService | None
    player_death_service: _TickDeathService | None
    player_respawn_service: _TickRespawnService | None
    event_bus: _TickEventBus | None
    passive_lucidity_flux_service: PassiveLucidityFluxService | None
    mp_regeneration_service: _TickMpRegen | None
    npc_lifecycle_manager: _TickNpcLifecycle | None


logger = get_logger("server.game_tick")

__all__ = [
    "get_current_tick",
    "reset_current_tick",
    "set_current_tick",
]


def _app_container(app: FastAPI) -> _TickContainer | None:
    """Return the DI container from app.state, or None if missing."""
    raw = getattr(app.state, "container", None)
    if raw is None:
        return None
    return cast(_TickContainer, raw)


def get_tick_interval() -> float:
    """Get the server tick interval from configuration.

    Returns:
        float: Tick interval in seconds
    """
    config = get_config()
    return config.game.server_tick_rate


def _validate_app_state_for_status_effects(app: FastAPI) -> tuple[bool, _TickContainer | None]:
    """Validate app state has required components for status effect processing.

    Returns:
        Tuple of (is_valid, container) where is_valid indicates if processing can proceed.
    """
    container = _app_container(app)
    if container is None or not container.async_persistence or not container.connection_manager:
        return False, None
    return True, container


async def _process_damage_over_time_effect(  # pylint: disable=too-many-arguments,too-many-positional-arguments  # Reason: Effect processing requires many parameters for game state and effect context
    _app: FastAPI,
    container: _TickContainer,
    player: Player,
    effect: dict[str, object],
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
            player_uuid = uuid.UUID(player_id)
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

    damage = coerce_int(effect.get("damage", 0), default=0)
    if damage > 0 and container.async_persistence is not None:
        await container.async_persistence.damage_player(player, damage, "status_effect")
        logger.debug("Applied damage over time", player_id=player_id, damage=damage, effect_type=effect.get("type", ""))
        return True
    return False


async def _process_heal_over_time_effect(
    container: _TickContainer, player: Player, effect: dict[str, object], remaining: int, player_id: str
) -> bool:
    """Process a heal over time effect.

    Returns:
        True if effect was applied, False otherwise.
    """
    if remaining <= 0:
        return False

    healing = coerce_int(effect.get("healing", 0), default=0)
    if healing > 0 and container.async_persistence is not None:
        await container.async_persistence.heal_player(player, healing)
        logger.debug("Applied heal over time", player_id=player_id, healing=healing, effect_type=effect.get("type", ""))
        return True
    return False


async def _process_single_effect(
    app: FastAPI, container: _TickContainer, player: Player, effect: dict[str, object], player_id: str
) -> tuple[dict[str, object] | None, bool]:
    """Process a single status effect.

    Returns:
        Tuple of (updated_effect_dict or None if expired, effect_applied) where effect_applied indicates if the effect had an impact.
    """
    effect_type = str(effect.get("type", ""))
    duration = coerce_int(effect.get("duration", 0), default=0)
    remaining = coerce_int(effect.get("remaining", duration), default=duration) - 1
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
    container: _TickContainer,
    player: Player,
    updated_effects: list[dict[str, object]],
    original_count: int,
    effect_applied: bool,
) -> bool:
    """Update and save player status effects if changes occurred.

    Returns:
        True if player was updated, False otherwise.
    """
    effects_changed = len(updated_effects) != original_count
    if (effects_changed or effect_applied) and container.async_persistence is not None:
        player.set_status_effects(updated_effects)
        await container.async_persistence.save_player(player)
        return True
    return False


async def _validate_and_get_player(container: _TickContainer, player_id: str) -> tuple[Player | None, uuid.UUID | None]:
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
        player_uuid = uuid.UUID(player_id)
    except (ValueError, AttributeError):
        logger.warning("Invalid player_id format", player_id=player_id)
        return None, None

    player = await container.async_persistence.get_player_by_id(player_uuid)
    return player, player_uuid


async def _process_all_status_effects(
    app: FastAPI, container: _TickContainer, player: Player, player_id: str
) -> tuple[list[dict[str, object]], bool, int]:
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

    updated_effects: list[dict[str, object]] = []
    effect_applied = False
    original_count = len(status_effects)

    for effect in status_effects:
        updated_effect, was_applied = await _process_single_effect(app, container, player, effect, player_id)
        if updated_effect is not None:
            updated_effects.append(updated_effect)
        if was_applied:
            effect_applied = True

    return updated_effects, effect_applied, original_count


async def _process_player_status_effects(app: FastAPI, container: _TickContainer, player_id: str) -> bool:
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
                    player_uuid = uuid.UUID(player_id_str)
                    await handle_login_grace_period_expiration(player_uuid, container.connection_manager)
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


async def _player_in_active_combat(container: _TickContainer, player: Player) -> bool:
    """Return True when the player is in an active combat (skip passive DP decay)."""
    if container.combat_service is None:
        return False

    combat_service = container.combat_service
    combat = await combat_service.get_combat_by_participant(uuid.UUID(str(player.player_id)))
    if combat and combat.status == CombatStatus.ACTIVE:
        logger.debug(
            "Skipping DP decay for mortally wounded player in active combat",
            player_id=player.player_id,
            player_name=player.name,
            combat_id=combat.combat_id,
        )
        return True
    return False


async def _handle_player_death_threshold(
    container: _TickContainer, player: Player, session: AsyncSession, new_dp: int, stats: dict[str, object]
) -> None:
    """Move player to limbo and publish authoritative DP when death threshold is reached."""
    logger.info(
        "Player reached death threshold",
        player_id=player.player_id,
        player_name=player.name,
        current_dp=new_dp,
    )
    if not container.player_respawn_service or not container.player_death_service:
        return

    death_service = container.player_death_service
    respawn_service = container.player_respawn_service
    player_uuid = uuid.UUID(str(player.player_id))
    _ = await death_service.handle_player_death(player_uuid, str(player.current_room_id), None, session)
    _ = await respawn_service.move_player_to_limbo(player_uuid, str(player.current_room_id), session)

    if not container.event_bus:
        return

    container.event_bus.publish(
        PlayerDPUpdated(
            player_id=player_uuid,
            old_dp=new_dp + 1,
            new_dp=new_dp,
            max_dp=coerce_int(stats.get("max_dp", 100), default=100),
        )
    )


async def _process_mortally_wounded_player(container: _TickContainer, player: Player, session: AsyncSession) -> None:
    """
    Process a single mortally wounded player's DP decay and death check.

    CRITICAL: Skip DP decay if player is in active combat - NPCs should deal damage instead.
    DP decay should only occur when player is mortally wounded but NOT in combat.
    """
    if not container.player_death_service:
        return

    if await _player_in_active_combat(container, player):
        return

    death_service = container.player_death_service
    _ = await death_service.process_mortally_wounded_tick(uuid.UUID(str(player.player_id)), session)

    await session.refresh(player)
    stats = player.get_stats()
    new_dp = coerce_int(stats.get("current_dp", 0), default=0)

    if container.combat_service:
        _ = await combat_messaging_integration.send_dp_decay_message(str(player.player_id), new_dp)

    if new_dp <= -10:
        await _handle_player_death_threshold(container, player, session, new_dp, stats)


async def _process_mortally_wounded_players(container: _TickContainer, session: AsyncSession, tick_count: int) -> None:
    """Process all mortally wounded players."""
    if not container.player_death_service:
        return

    death_service = container.player_death_service
    mortally_wounded = await death_service.get_mortally_wounded_players(session)

    if not mortally_wounded:
        return

    logger.debug(
        "Processing DP decay for mortally wounded players",
        tick_count=tick_count,
        player_count=len(mortally_wounded),
    )

    for player in mortally_wounded:
        await _process_mortally_wounded_player(container, player, session)


async def _process_passive_lucidity_flux(container: _TickContainer, session: AsyncSession, tick_count: int) -> None:
    """Process passive lucidity flux service if available."""
    if not container.passive_lucidity_flux_service:
        return

    try:
        lucidity_flux = container.passive_lucidity_flux_service
        _ = await lucidity_flux.process_tick(
            session=session, tick_count=tick_count, now=datetime.datetime.now(datetime.UTC)
        )
    except (AttributeError, KeyError, TypeError, ValueError, RuntimeError) as lcd_flux_error:
        logger.error("Error processing passive LCD flux", tick_count=tick_count, error=str(lcd_flux_error))


def _validate_mp_regeneration_services(container: _TickContainer) -> bool:
    """
    Validate that required services exist for MP regeneration.

    Args:
        container: Application container

    Returns:
        True if services are available, False otherwise
    """
    return container.mp_regeneration_service is not None and container.connection_manager is not None


async def _process_single_player_mp_regeneration(mp_service: _TickMpRegen, player_id_str: str) -> bool:
    """
    Process MP regeneration for a single player.

    Args:
        mp_service: MP regeneration service instance
        player_id_str: Player ID as string

    Returns:
        True if MP was restored, False otherwise
    """
    try:
        player_uuid = uuid.UUID(player_id_str)
        result = await mp_service.process_tick_regeneration(player_uuid)
        return coerce_int(result.get("mp_restored", 0), default=0) > 0
    except (ValueError, AttributeError, TypeError) as e:
        logger.warning("Error processing MP regeneration for player", player_id=player_id_str, error=str(e))
        return False


async def _process_mp_regeneration(container: _TickContainer, _session: AsyncSession, tick_count: int) -> None:
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


async def _process_dead_players(container: _TickContainer, session: AsyncSession) -> None:
    """Process dead players and move them to limbo if needed."""
    if not container.player_death_service or not container.player_respawn_service:
        return

    death_service = container.player_death_service
    respawn_service = container.player_respawn_service
    dead_players = await death_service.get_dead_players(session)

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

            _ = await respawn_service.move_player_to_limbo(
                uuid.UUID(str(player.player_id)), str(player.current_room_id), session
            )


async def _process_session_dp_decay_and_death(
    container: _TickContainer, session: AsyncSession, tick_count: int
) -> None:
    """Process DP decay and death for a single database session."""
    await _process_mortally_wounded_players(container, session, tick_count)
    await _process_passive_lucidity_flux(container, session, tick_count)
    await _process_mp_regeneration(container, session, tick_count)
    await _process_dead_players(container, session)


async def process_dp_decay_and_death(app: FastAPI, tick_count: int) -> None:
    """Process DP decay for mortally wounded players and handle deaths."""
    container = _app_container(app)
    if container is None or container.player_death_service is None:
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
