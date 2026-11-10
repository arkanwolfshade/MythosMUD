"""Status-effect processing for the game tick loop (ADR-029 steps 3b-i and 6d).

Every player status effect is a player_effects row, held by the player registry in the player's effects part. Once per
game second, each online player who has an effect gets one registry unit of work: every active effect runs its
per-second action (heal over time, damage over time, the lucidity drain), a finished effect ends, a changed one (the
drain's ``elapsed``) has its payload written back, and then the timed effects lose one second, the ones that run out
ending (a login ward among them). The DP and lucidity an effect moved and the effect rows commit together, so a
second is all there or not at all. Effects pause while a player is offline: only online players are processed.
"""

from __future__ import annotations

import uuid
from typing import TYPE_CHECKING, cast

from fastapi import FastAPI
from sqlalchemy.exc import SQLAlchemyError

from ..events.event_types import PlayerDPUpdated
from ..exceptions import DatabaseError
from ..game.effect_store import effect_dict, effect_payload
from ..game.player_registry import PlayerNotFoundError
from ..models.player_dp import DpChange, damaged, healed
from ..monitoring.exception_tracker import track_exception
from ..realtime.login_grace_period import handle_login_grace_period_expiration, is_player_in_login_grace_period
from ..services.lucidity_service import CatatoniaObserverProtocol
from ..services.player_health_service import PlayerHealthService
from ..structured_logging.enhanced_logging_config import get_logger
from ..utils.int_coercion import coerce_int
from .game_tick_death import is_game_second_tick
from .game_tick_lucidity_drain import LUCIDITY_DRAIN_EFFECT, drain_second
from .game_tick_protocols import (
    EffectSecond,
    _app_container,
    _online_player_ids,
    _TickConnectionManager,
    _TickContainer,
)

logger = get_logger("server.game_tick")

if TYPE_CHECKING:
    from ..game.player_registry import EffectData, PlayerAggregate, PlayerRegistry

__all__ = [
    "_handle_login_warded_expirations",
    "_process_damage_over_time_effect",
    "_process_heal_over_time_effect",
    "_process_player_status_effects",
    "_run_effect_second",
    "_validate_app_state_for_status_effects",
    "process_status_effects",
]

# What one player's second can raise without taking the others down: the registry's commit (SQLAlchemy, OSError) and
# an effect that is malformed or misbehaves.
_PLAYER_SECOND_ERRORS = (
    DatabaseError,
    SQLAlchemyError,
    OSError,
    AttributeError,
    KeyError,
    TypeError,
    ValueError,
    RuntimeError,
)


def _validate_app_state_for_status_effects(app: FastAPI) -> tuple[bool, _TickContainer | None]:
    """Validate app state has required components for status effect processing.

    Returns:
        Tuple of (is_valid, container) where is_valid indicates if processing can proceed.
    """
    container = _app_container(app)
    if (
        container is None
        or not container.async_persistence
        or not container.connection_manager
        or container.player_registry is None
    ):
        return False, None
    return True, container


def _emit_dp_change(player: PlayerAggregate, change: DpChange, source_id: str) -> None:
    """Queue the client's DP update for a change that moved DP; the registry sends it once the unit commits."""
    if change.new_dp == change.old_dp:
        return
    player.emit(
        PlayerDPUpdated(
            player_id=player.player_id,
            old_dp=change.old_dp,
            new_dp=change.new_dp,
            max_dp=change.max_dp,
            damage_taken=change.old_dp - change.new_dp,  # negative for healing
            source_id=source_id,
            room_id=player.row.current_room_id,
        )
    )


def _process_damage_over_time_effect(
    container: _TickContainer, player: PlayerAggregate, effect: dict[str, object]
) -> bool:
    """Apply one second of a damage over time effect in the player's unit; blocked during the login grace period.

    Returns:
        True if effect was applied, False otherwise.
    """
    player_id = str(player.player_id)
    # Check if player is in login grace period - block negative effects
    try:
        if container.connection_manager and is_player_in_login_grace_period(
            player.player_id, container.connection_manager
        ):
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
    if damage <= 0:
        return False
    change = PlayerHealthService.apply_in(player, damaged(player.row.stats, damage, "status_effect"))
    _emit_dp_change(player, change, "damage_over_time")
    logger.debug("Applied damage over time", player_id=player_id, damage=damage, effect_type=effect.get("type", ""))
    return True


def _process_heal_over_time_effect(player: PlayerAggregate, effect: dict[str, object]) -> bool:
    """Apply one second of a heal over time effect in the player's unit.

    Returns:
        True if effect was applied, False otherwise.
    """
    healing = coerce_int(effect.get("healing", 0), default=0)
    if healing <= 0:
        return False
    change = PlayerHealthService.apply_in(player, healed(player.row.stats, healing))
    _emit_dp_change(player, change, "heal_over_time")
    logger.debug(
        "Applied heal over time", player_id=str(player.player_id), healing=healing, effect_type=effect.get("type", "")
    )
    return True


def _run_effect_second(
    container: _TickContainer, registry: PlayerRegistry, player: PlayerAggregate, effect: dict[str, object]
) -> EffectSecond:
    """Run one second of one effect inside the player's unit.

    Returns:
        The effect as it stands, or None once it has finished; whether it had an impact; and what to run after the
        unit commits. Effects with no per-second action (spell effects, the login ward) come back unchanged: they
        only run out.
    """
    effect_type = str(effect.get("type", ""))
    if effect_type == LUCIDITY_DRAIN_EFFECT:
        observer = cast(CatatoniaObserverProtocol | None, getattr(container, "catatonia_registry", None))
        return drain_second(registry, observer, player, effect)
    if effect_type == "damage_over_time":
        return EffectSecond(effect, _process_damage_over_time_effect(container, player, effect))
    if effect_type == "heal_over_time":
        return EffectSecond(effect, _process_heal_over_time_effect(player, effect))
    return EffectSecond(effect, False)


def _store_effect_outcome(player: PlayerAggregate, stored: EffectData, updated: dict[str, object] | None) -> None:
    """End a finished effect, or write back its payload if the second changed it."""
    if updated is None:
        _ = player.effects.remove(stored.id)
        return
    _ = player.effects.set_payload(stored.id, effect_payload(updated))


async def _process_player_status_effects(
    container: _TickContainer, registry: PlayerRegistry, player_id: uuid.UUID
) -> tuple[bool, list[tuple[str, str]]]:
    """Run one second of every active effect on one online player, as one registry unit.

    Returns:
        Whether any effect had an impact, and the (player_id, effect_type) of each effect that ran out. A failed
        second changes nothing and is retried the next second.
    """
    after: list[EffectSecond] = []
    applied_any = False
    expired: list[tuple[str, str]] = []
    try:
        async with registry.mutate(player_id) as player:  # pylint: disable=contextmanager-generator-missing-cleanup  # Reason: @asynccontextmanager always drives this generator to completion; pylint cannot see through the wrapper
            for stored in player.effects.effects:
                second = _run_effect_second(container, registry, player, effect_dict(stored))
                applied_any = applied_any or second.applied
                after.append(second)
                _store_effect_outcome(player, stored, second.effect)
            expired = [(str(player_id), ended.effect_type) for ended in player.effects.advance_second()]
    except PlayerNotFoundError:
        return False, []  # deleted since the candidate query: nothing to run
    except _PLAYER_SECOND_ERRORS as e:
        # One player's failure must not stop the others' effects this second.
        logger.warning("Error processing status effects for player", player_id=str(player_id), error=str(e))
        return False, []
    for second in after:
        for action in second.after:
            try:
                await action()
            except _PLAYER_SECOND_ERRORS as e:  # the second has committed; a failed notification must not undo it
                logger.warning("Status effect follow-up failed", player_id=str(player_id), error=str(e))
    return applied_any, expired


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
    """Once per game second: run, advance and expire the effects of every online player who has any."""
    if not is_game_second_tick(tick_count):
        return
    is_valid, container = _validate_app_state_for_status_effects(app)
    if not is_valid or container is None or container.async_persistence is None or not container.connection_manager:
        return
    online = _online_player_ids(container)
    if not online:
        return
    registry = cast("PlayerRegistry", container.player_registry)
    try:
        candidates = await container.async_persistence.get_player_ids_with_effects(online)
        processed = 0
        expired: list[tuple[str, str]] = []
        for player_id in candidates:
            applied, ended = await _process_player_status_effects(container, registry, player_id)
            processed += applied
            expired.extend(ended)
        if processed:
            logger.debug("Processed status effects", tick_count=tick_count, players_processed=processed)
        await _handle_login_warded_expirations(expired, container.connection_manager)
    except Exception as e:  # pylint: disable=broad-exception-caught  # Reason: the candidate query raises DatabaseError (a plain Exception subclass); a narrower tuple once let it escape and kill the whole game_tick_loop
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
