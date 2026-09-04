"""DP decay, death, and MP regeneration for the game tick loop."""

from __future__ import annotations

import datetime
import uuid
from typing import TYPE_CHECKING

from fastapi import FastAPI
from sqlalchemy.ext.asyncio import AsyncSession

from ..constants.spawn_defaults import LIMBO_ROOM_ID
from ..database import get_async_session
from ..events.event_types import PlayerDPDecayEvent, PlayerDPUpdated
from ..models.combat import CombatStatus
from ..services.combat_messaging_integration import combat_messaging_integration
from ..structured_logging.enhanced_logging_config import get_logger
from ..utils.int_coercion import coerce_int
from .game_tick_protocols import (
    _app_container,
    _online_player_ids,
    _tick_online_players,
    _TickContainer,
    _TickMpRegen,
)

logger = get_logger("server.game_tick")

if TYPE_CHECKING:
    from ..models.player import Player

__all__ = [
    "_handle_player_death_threshold",
    "_player_in_active_combat",
    "_process_dead_players",
    "_process_mortally_wounded_player",
    "_process_mortally_wounded_players",
    "_process_mp_regeneration",
    "_process_passive_lucidity_flux",
    "_process_session_dp_decay_and_death",
    "_process_single_player_mp_regeneration",
    "_validate_mp_regeneration_services",
    "process_dp_decay_and_death",
]


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
    old_dp = coerce_int(player.get_stats().get("current_dp", 0), default=0)
    _ = await death_service.process_mortally_wounded_tick(uuid.UUID(str(player.player_id)), session)

    await session.refresh(player)
    stats = player.get_stats()
    new_dp = coerce_int(stats.get("current_dp", 0), default=0)

    if container.combat_service:
        _ = await combat_messaging_integration.send_dp_decay_message(str(player.player_id), new_dp)
        # NATS-consumable in addition to the direct personal message above (#634)
        _ = await container.combat_service.publish_player_dp_decay_event_to_nats(
            PlayerDPDecayEvent(
                player_id=uuid.UUID(str(player.player_id)),
                old_dp=old_dp,
                new_dp=new_dp,
                decay_amount=old_dp - new_dp,
                room_id=player.current_room_id,
            )
        )

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
        mp_service = container.mp_regeneration_service
        if not mp_service:
            return

        await _tick_online_players(
            _online_player_ids(container),
            tick_count,
            "Processed MP regeneration",
            lambda player_id_str: _process_single_player_mp_regeneration(mp_service, player_id_str),
        )
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
