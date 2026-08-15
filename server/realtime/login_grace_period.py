"""
Login grace period management for MythosMUD.

This module handles the 10-second grace period after a player logs in,
providing immunity to damage and negative effects while allowing movement.

As documented in "Protective Wards Upon Entering the Realms" - Dr. Armitage, 1930,
the grace period provides a brief window of protection for newly arrived characters.

Effects system (ADR-009): Grace period is implemented as LOGIN_WARDED effect in
player_effects table; tick processing expires it and clears in-memory state.
"""

# pylint: disable=missing-class-docstring,missing-function-docstring,too-few-public-methods  # Reason: Protocol stubs (PEP 544)

from __future__ import annotations

import asyncio
import time
import uuid
from collections.abc import Callable
from typing import Protocol, cast

from anyio import sleep

from ..structured_logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)

LOGIN_GRACE_PERIOD_DURATION = 10.0  # 10 seconds

GraceEntry = asyncio.Task[None] | bool


class _GracePlayer(Protocol):
    current_room_id: object


class _OccupantsHandler(Protocol):
    async def send_room_occupants_update(self, room_id: str, exclude_player: str | None = None) -> None: ...


class _GraceContainer(Protocol):
    real_time_event_handler: _OccupantsHandler | None


class _GraceAppState(Protocol):
    container: _GraceContainer | None


class _GraceApp(Protocol):
    state: _GraceAppState


class _GraceManager(Protocol):
    login_grace_period_players: dict[uuid.UUID, GraceEntry]
    login_grace_period_start_times: dict[uuid.UUID, float]
    async_persistence: object | None
    app: object | None

    async def get_player(self, player_id: uuid.UUID) -> _GracePlayer | None: ...


class _EffectPersistence(Protocol):
    async def add_player_effect(
        self,
        player_id: uuid.UUID | str,
        effect_type: str,
        category: str,
        duration: int,
        applied_at_tick: int,
        options: dict[str, object] | None = None,
    ) -> str: ...


def _as_grace(manager: object) -> _GraceManager:
    return cast(_GraceManager, manager)


def _remove_from_grace_period_tracking(player_id: uuid.UUID, manager: object) -> None:
    """Remove player from grace period tracking dictionaries."""
    mgr = _as_grace(manager)
    if player_id in mgr.login_grace_period_players:
        del mgr.login_grace_period_players[player_id]
    if hasattr(manager, "login_grace_period_start_times") and player_id in mgr.login_grace_period_start_times:
        del mgr.login_grace_period_start_times[player_id]


async def _trigger_room_occupants_update(player_id: uuid.UUID, manager: object) -> None:
    """Trigger room occupants update after grace period expiration."""
    try:
        mgr = _as_grace(manager)
        if mgr.async_persistence is None:
            return

        player = await mgr.get_player(player_id)
        if player is None or not player.current_room_id:
            return

        room_id = str(player.current_room_id)
        if mgr.app is None:
            return

        try:
            app = cast(_GraceApp, mgr.app)
            container = app.state.container
            if container is None:
                return
            event_handler = container.real_time_event_handler
            if event_handler is None:
                return

            await event_handler.send_room_occupants_update(room_id)
            logger.info(
                "Triggered room occupants update after grace period expiration", player_id=player_id, room_id=room_id
            )
        except (AttributeError, TypeError) as app_error:
            logger.debug("Could not access app state container", player_id=player_id, error=str(app_error))
    except (AttributeError, RuntimeError, ValueError, TypeError, KeyError) as e:
        logger.warning(
            "Could not trigger room occupants update after grace period expiration", player_id=player_id, error=str(e)
        )


async def handle_login_grace_period_expiration(player_id: uuid.UUID, manager: object) -> None:
    """Handle grace period expiration - remove tracking and trigger updates."""
    # Grace period expired - remove from tracking FIRST to prevent race condition
    # CRITICAL: Remove from tracking BEFORE triggering room occupants update
    # This ensures that when the update queries grace period status, it will correctly
    # return False, preventing "(warded)" from appearing after expiration
    logger.info("Login grace period expired", player_id=player_id)

    _remove_from_grace_period_tracking(player_id, manager)
    await _trigger_room_occupants_update(player_id, manager)


async def _grace_period_task(player_id: uuid.UUID, manager: object) -> None:
    """Internal task that waits for grace period duration and handles expiration."""
    try:
        await sleep(LOGIN_GRACE_PERIOD_DURATION)

        if player_id not in _as_grace(manager).login_grace_period_players:
            logger.debug("Login grace period cancelled", player_id=player_id)
            return

        await handle_login_grace_period_expiration(player_id, manager)

    except asyncio.CancelledError:
        logger.debug("Login grace period task cancelled", player_id=player_id)
    except (AttributeError, RuntimeError, ValueError, TypeError, KeyError) as e:
        # Catching broad exceptions here is necessary because cleanup operations
        # can fail for various reasons and we must ensure the grace period task
        # is always removed from tracking
        logger.error("Error in login grace period task", player_id=player_id, error=str(e), exc_info=True)
    finally:
        _remove_from_grace_period_tracking(player_id, manager)


async def start_login_grace_period(
    player_id: uuid.UUID,
    manager: object,
    async_persistence: object | None = None,
    get_current_tick: Callable[[], int] | None = None,
    get_tick_interval: Callable[[], float] | None = None,
) -> None:
    """
    Start a login grace period for a player.

    When async_persistence and get_current_tick are provided (effects system ADR-009),
    adds a LOGIN_WARDED effect to player_effects and sets in-memory state; expiration
    is handled by game tick processing. Otherwise falls back to asyncio task (legacy).

    During the grace period, the player:
    - Is immune to all damage and negative status effects
    - Cannot initiate combat
    - Hostile NPCs/mobs ignore them
    - Can move freely
    - Shows "(warded)" indicator to other players

    Args:
        player_id: The player's ID
        manager: ConnectionManager instance
        async_persistence: Optional async persistence layer for effect storage
        get_current_tick: Optional function returning current game tick
        get_tick_interval: Optional function returning tick interval in seconds (for duration_ticks)
    """
    mgr = _as_grace(manager)
    if player_id in mgr.login_grace_period_players:
        logger.debug("Player already in login grace period", player_id=player_id)
        return

    logger.info("Starting login grace period for player", player_id=player_id, duration=LOGIN_GRACE_PERIOD_DURATION)

    start_time = time.time()
    mgr.login_grace_period_start_times[player_id] = start_time

    if async_persistence and get_current_tick and get_tick_interval:
        try:
            tick_interval = get_tick_interval()
            duration_ticks = max(1, int(LOGIN_GRACE_PERIOD_DURATION / tick_interval))
            current_tick = get_current_tick()
            persistence = cast(_EffectPersistence, async_persistence)
            _ = await persistence.add_player_effect(
                player_id,
                effect_type="login_warded",
                category="entry_ward",
                duration=duration_ticks,
                applied_at_tick=current_tick,
                options={
                    "intensity": 1,
                    "source": "game_entry",
                    "visibility_level": "visible",
                },
            )
            mgr.login_grace_period_players[player_id] = True  # Sentinel: effect-based, no asyncio task
            return
        except (AttributeError, TypeError, ValueError) as e:
            logger.warning(
                "Failed to add LOGIN_WARDED effect, falling back to asyncio task",
                player_id=player_id,
                error=str(e),
            )

    task = asyncio.create_task(_grace_period_task(player_id, manager))
    mgr.login_grace_period_players[player_id] = task


async def cancel_login_grace_period(
    player_id: uuid.UUID,
    manager: object,
) -> None:
    """
    Cancel login grace period for a player (if needed).

    For effect-based grace (login_grace_period_players[player_id] is True), just clears
    in-memory state; the effect remains in DB until tick expiration (or could be removed
    by a future API). For task-based grace, cancels the asyncio task.
    """
    mgr = _as_grace(manager)
    if player_id not in mgr.login_grace_period_players:
        return

    logger.info("Cancelling login grace period for player", player_id=player_id)

    entry = mgr.login_grace_period_players[player_id]
    if entry is True:
        _remove_from_grace_period_tracking(player_id, manager)
        return

    if isinstance(entry, asyncio.Task):
        _ = entry.cancel()
        try:
            await entry
        except asyncio.CancelledError:
            pass
        except (AttributeError, RuntimeError, ValueError, TypeError) as e:
            logger.error("Error cancelling login grace period task", player_id=player_id, error=str(e), exc_info=True)
        finally:
            _remove_from_grace_period_tracking(player_id, manager)


def is_player_in_login_grace_period(player_id: uuid.UUID, manager: object) -> bool:
    """
    Check if a player is currently in login grace period.

    Args:
        player_id: The player's ID
        manager: ConnectionManager instance

    Returns:
        True if player is in login grace period, False otherwise
    """
    if not hasattr(manager, "login_grace_period_players"):
        return False

    return player_id in _as_grace(manager).login_grace_period_players


def get_login_grace_period_remaining(player_id: uuid.UUID, manager: object) -> float:
    """
    Get the remaining time in seconds for a player's login grace period.

    Args:
        player_id: The player's ID
        manager: ConnectionManager instance

    Returns:
        Remaining time in seconds, or 0.0 if not in grace period or start time not found
    """
    if not is_player_in_login_grace_period(player_id, manager):
        return 0.0

    if not hasattr(manager, "login_grace_period_start_times"):
        return 0.0

    mgr = _as_grace(manager)
    if player_id not in mgr.login_grace_period_start_times:
        return 0.0

    start_time = mgr.login_grace_period_start_times[player_id]
    elapsed = time.time() - start_time
    return max(0.0, LOGIN_GRACE_PERIOD_DURATION - elapsed)
