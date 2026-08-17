"""Status-effect processing for the game tick loop."""

from __future__ import annotations

import uuid
from typing import TYPE_CHECKING

from fastapi import FastAPI

from ..realtime.login_grace_period import handle_login_grace_period_expiration, is_player_in_login_grace_period
from ..structured_logging.enhanced_logging_config import get_logger
from ..utils.int_coercion import coerce_int
from .game_tick_protocols import (
    _app_container,
    _online_player_ids,
    _tick_online_players,
    _TickConnectionManager,
    _TickContainer,
)

logger = get_logger("server.game_tick")

if TYPE_CHECKING:
    from ..models.player import Player

__all__ = [
    "_handle_login_warded_expirations",
    "_process_all_status_effects",
    "_process_damage_over_time_effect",
    "_process_heal_over_time_effect",
    "_process_player_status_effects",
    "_process_single_effect",
    "_update_player_status_effects",
    "_validate_and_get_player",
    "_validate_app_state_for_status_effects",
    "process_player_effects_expiration",
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


async def process_player_effects_expiration(app: FastAPI, tick_count: int) -> None:
    """Expire player_effects for this tick; for LOGIN_WARDED clear in-memory state and trigger room update."""
    is_valid, container = _validate_app_state_for_status_effects(app)
    if not is_valid or not container or not container.async_persistence or not container.connection_manager:
        return

    try:
        expired = await container.async_persistence.expire_player_effects_for_tick(tick_count)
        await _handle_login_warded_expirations(expired, container.connection_manager)
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
        await _tick_online_players(
            _online_player_ids(container),
            tick_count,
            "Processed status effects",
            lambda player_id_str: _process_player_status_effects(app, container, player_id_str),
        )
    except (AttributeError, KeyError, TypeError, ValueError, RuntimeError) as e:
        logger.warning("Error processing status/effect ticks", tick_count=tick_count, error=str(e))
