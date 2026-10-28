"""Status-effect processing for the game tick loop (ADR-029 step 3b-i).

Every player status effect is a player_effects row. Once per game second, for each online player, each active effect
runs its per-second action (heal over time, damage over time, the lucidity drain); a finished effect is deleted and a
changed one (the drain's ``elapsed``) has its payload written back. Then every online player's timed effects lose one
second, and the ones that run out are deleted (ending a login ward among them). Effects pause while a player is
offline: only online players are advanced.
"""

from __future__ import annotations

import uuid
from typing import TYPE_CHECKING

from fastapi import FastAPI

from ..events.event_types import PlayerDPUpdated
from ..exceptions import DatabaseError
from ..game.effect_store import effect_dict, effect_payload
from ..monitoring.exception_tracker import track_exception
from ..realtime.login_grace_period import handle_login_grace_period_expiration, is_player_in_login_grace_period
from ..structured_logging.enhanced_logging_config import get_logger
from ..utils.int_coercion import coerce_int
from .game_tick_death import is_game_second_tick
from .game_tick_lucidity_drain import LUCIDITY_DRAIN_EFFECT, process_lucidity_drain
from .game_tick_protocols import (
    _app_container,
    _online_player_ids,
    _tick_online_players,
    _TickConnectionManager,
    _TickContainer,
)

logger = get_logger("server.game_tick")

if TYPE_CHECKING:
    from ..async_persistence import AsyncPersistenceLayer
    from ..models.player import Player
    from ..models.player_effect import PlayerEffect

__all__ = [
    "_handle_login_warded_expirations",
    "_process_damage_over_time_effect",
    "_process_heal_over_time_effect",
    "_process_player_status_effects",
    "_process_single_effect",
    "_validate_app_state_for_status_effects",
    "process_status_effects",
]


def _validate_app_state_for_status_effects(app: FastAPI) -> tuple[bool, _TickContainer | None]:
    """Validate app state has required components for status effect processing.

    Returns:
        Tuple of (is_valid, container) where is_valid indicates if processing can proceed.
    """
    container = _app_container(app)
    if container is None or not container.async_persistence or not container.connection_manager:
        return False, None
    return True, container


async def _process_damage_over_time_effect(
    container: _TickContainer, player: Player, effect: dict[str, object], player_id: str
) -> bool:
    """Apply one second of a damage over time effect; blocked during the login grace period.

    Returns:
        True if effect was applied, False otherwise.
    """
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


def _publish_heal_dp_update(container: _TickContainer, player: Player, old_dp: int) -> None:
    """Tell the client about a DP change from healing; heal_player only writes the database."""
    stats = player.get_stats()
    new_dp = coerce_int(stats.get("current_dp", 0), default=0)
    if new_dp == old_dp or not container.event_bus:
        return
    container.event_bus.publish(
        PlayerDPUpdated(
            player_id=uuid.UUID(str(player.player_id)),
            old_dp=old_dp,
            new_dp=new_dp,
            max_dp=coerce_int(stats.get("max_dp", 100), default=100),
            damage_taken=old_dp - new_dp,  # negative for healing
            source_id="heal_over_time",
            room_id=player.current_room_id,
        )
    )


async def _process_heal_over_time_effect(
    container: _TickContainer, player: Player, effect: dict[str, object], player_id: str
) -> bool:
    """Apply one second of a heal over time effect.

    Returns:
        True if effect was applied, False otherwise.
    """
    healing = coerce_int(effect.get("healing", 0), default=0)
    if healing > 0 and container.async_persistence is not None:
        old_dp = coerce_int(player.get_stats().get("current_dp", 0), default=0)
        await container.async_persistence.heal_player(player, healing)
        _publish_heal_dp_update(container, player, old_dp)
        logger.debug("Applied heal over time", player_id=player_id, healing=healing, effect_type=effect.get("type", ""))
        return True
    return False


async def _process_single_effect(
    container: _TickContainer, player: Player, effect: dict[str, object]
) -> tuple[dict[str, object] | None, bool]:
    """Run one second of one effect.

    Returns:
        (the effect, updated, or None once it has finished; whether it had an impact). Effects with no per-second
        action (spell effects, the login ward) come back unchanged: they only run out.
    """
    effect_type = str(effect.get("type", ""))
    player_id = str(player.player_id)
    if effect_type == LUCIDITY_DRAIN_EFFECT:
        return await process_lucidity_drain(container, player, effect)
    if effect_type == "damage_over_time":
        return effect, await _process_damage_over_time_effect(container, player, effect, player_id)
    if effect_type == "heal_over_time":
        return effect, await _process_heal_over_time_effect(container, player, effect, player_id)
    return effect, False


async def _store_effect_outcome(
    persistence: AsyncPersistenceLayer, stored: PlayerEffect, updated: dict[str, object] | None
) -> None:
    """Delete a finished effect, or write back its payload if the second changed it."""
    if updated is None:
        await persistence.remove_player_effect_by_id(stored.id)
        return
    payload = effect_payload(updated)
    if payload != stored.payload:
        await persistence.update_player_effect_payload(stored.id, payload)


async def _process_player_status_effects(container: _TickContainer, player_id: str) -> bool:
    """Run one second of every active effect on one online player.

    Returns:
        True if any effect had an impact, False otherwise.
    """
    persistence = container.async_persistence
    if persistence is None:
        return False
    try:
        player_uuid = uuid.UUID(player_id)
        effects = await persistence.get_active_player_effects(player_uuid)
        if not effects:
            return False
        player = await persistence.get_player_by_id(player_uuid)
        if player is None:
            return False
        applied_any = False
        for stored in effects:
            updated, applied = await _process_single_effect(container, player, effect_dict(stored))
            applied_any = applied_any or applied
            await _store_effect_outcome(persistence, stored, updated)
        return applied_any
    except (DatabaseError, AttributeError, KeyError, TypeError, ValueError, RuntimeError) as e:
        # One player's failure must not stop the others' effects this second.
        logger.warning("Error processing status effects for player", player_id=player_id, error=str(e))
        return False


async def _handle_login_warded_expirations(
    expired: list[tuple[str, str]],
    connection_manager: _TickConnectionManager,
) -> None:
    """Clear in-memory grace state for each expired LOGIN_WARDED effect."""
    for player_id_str, effect_type in expired:
        if effect_type != "login_warded":
            continue
        try:
            player_uuid = uuid.UUID(player_id_str)
            await handle_login_grace_period_expiration(player_uuid, connection_manager)
        except (ValueError, AttributeError, TypeError) as e:
            logger.warning(
                "Error handling LOGIN_WARDED expiration",
                player_id=player_id_str,
                error=str(e),
            )


async def process_status_effects(app: FastAPI, tick_count: int) -> None:
    """Once per game second: run every online player's effects, then advance and expire their timed effects."""
    if not is_game_second_tick(tick_count):
        return
    is_valid, container = _validate_app_state_for_status_effects(app)
    if not is_valid or container is None or container.async_persistence is None or not container.connection_manager:
        return
    online = _online_player_ids(container)
    if not online:
        return
    try:
        await _tick_online_players(
            online,
            tick_count,
            "Processed status effects",
            lambda player_id_str: _process_player_status_effects(container, player_id_str),
        )
        expired = await container.async_persistence.advance_player_effects(online)
        await _handle_login_warded_expirations(expired, container.connection_manager)
    except Exception as e:  # pylint: disable=broad-exception-caught  # Reason: the effect procedures raise DatabaseError (a plain Exception subclass); a narrower tuple once let it escape and kill the whole game_tick_loop
        logger.warning("Error processing status effects", tick_count=tick_count, error=str(e))
        _ = track_exception(
            e,
            {
                "severity": "error",
                "handled": True,
                "context": {"tick_count": tick_count},
                "metadata": {"component": "process_status_effects"},
            },
        )
