"""
Command blocking guards for unified command processing.

Grace-period and casting-state checks share app.state Protocols so the
unified handler stays under module size limits without losing typing.
"""

from __future__ import annotations

import uuid
from typing import Protocol, cast

from ..realtime.disconnect_grace_period import is_player_in_grace_period
from ..structured_logging.enhanced_logging_config import get_logger
from .command_execution_request import CommandExecutionRequest, command_request_app_state

logger = get_logger(__name__)

ALLOWED_DURING_CASTING = ("stop", "interrupt", "status")


class _PlayerLookup(Protocol):  # pylint: disable=too-few-public-methods
    """Player service surface for name lookup in command guards."""

    async def get_player_by_name(self, player_name: str) -> object | None: ...  # pylint: disable=missing-function-docstring


class _AppStateCommandGuards(Protocol):
    """App state fields used by grace-period and casting command guards."""

    connection_manager: object | None
    player_service: _PlayerLookup | None
    magic_service: object | None


class _CastingStateView(Protocol):  # pylint: disable=too-few-public-methods
    """Casting state fields read when blocking commands mid-cast."""

    spell_name: str


class _CastingStateManagerView(Protocol):
    """Casting manager methods used by command casting guards."""

    def is_casting(self, player_id: object) -> bool: ...  # pylint: disable=missing-function-docstring

    def get_casting_state(self, player_id: object) -> _CastingStateView | None: ...  # pylint: disable=missing-function-docstring


class _MagicServiceView(Protocol):  # pylint: disable=too-few-public-methods
    """Magic service surface for casting-state command guards."""

    casting_state_manager: _CastingStateManagerView


def _raw_player_id(player: object) -> uuid.UUID | str | None:
    """Return player.id or player.player_id when it is a UUID or str.

    Skips non-id stubs (e.g. MagicMock auto-attrs) so player_id can still win.
    """
    for name in ("id", "player_id"):
        value = cast(object | None, getattr(player, name, None))
        if isinstance(value, uuid.UUID):
            return value
        if isinstance(value, str) and value:
            return value
    return None


def _coerce_player_uuid(player: object) -> uuid.UUID | None:
    """Resolve a player object's id/player_id attribute to a UUID."""
    raw = _raw_player_id(player)
    if raw is None:
        return None
    if isinstance(raw, uuid.UUID):
        return raw
    return uuid.UUID(raw)


async def _get_grace_check_context(
    player_name: str, request: CommandExecutionRequest
) -> tuple[uuid.UUID, object] | None:
    """Resolve player_id and connection_manager for grace period check. Returns None if unavailable."""
    state = command_request_app_state(request)
    if state is None:
        return None
    app_state = cast(_AppStateCommandGuards, state)
    connection_manager = app_state.connection_manager
    player_service = app_state.player_service
    if not connection_manager or not player_service:
        return None

    player = await player_service.get_player_by_name(player_name)
    if not player:
        return None

    player_id = _coerce_player_uuid(player)
    if player_id is None:
        return None

    return (player_id, connection_manager)


async def check_grace_period_block(player_name: str, request: CommandExecutionRequest) -> dict[str, object] | None:
    """
    Check if player is in grace period and block commands.

    Players in grace period (disconnected but still in-game) cannot execute commands,
    but can still auto-attack when attacked in combat.

    Returns:
        Block result if player is in grace period, None otherwise
    """
    try:
        context = await _get_grace_check_context(player_name, request)
        if context is None:
            return None

        player_id, connection_manager = context
        if not is_player_in_grace_period(player_id, connection_manager):
            return None

        logger.info("Command blocked - player is in grace period (disconnected)", player=player_name)
        return {"result": "You are disconnected and cannot perform actions. You will be removed from the game shortly."}

    except (AttributeError, ValueError, TypeError, ImportError) as e:
        logger.debug("Error checking grace period", player=player_name, error=str(e))
        # Don't block on error - allow command to proceed

    return None


async def _get_casting_block_result(
    request: CommandExecutionRequest, player_name: str, magic_service: _MagicServiceView
) -> dict[str, object] | None:
    """Return block result if player is currently casting, else None."""
    state = command_request_app_state(request)
    if state is None:
        return None
    app_state = cast(_AppStateCommandGuards, state)
    player_service = app_state.player_service
    if not player_service:
        return None
    player = await player_service.get_player_by_name(player_name)
    if not player:
        return None
    player_id = _raw_player_id(player)
    if not player_id or not magic_service.casting_state_manager.is_casting(player_id):
        return None
    casting_state = magic_service.casting_state_manager.get_casting_state(player_id)
    if not casting_state:
        return None
    return {"result": f"You are casting {casting_state.spell_name}. Use 'stop' to interrupt."}


async def check_casting_state(cmd: str, player_name: str, request: CommandExecutionRequest) -> dict[str, object] | None:
    """Check if player is casting and should be blocked. Returns result if blocked."""
    if cmd in ALLOWED_DURING_CASTING:
        return None
    try:
        state = command_request_app_state(request)
        if state is None:
            return None
        app_state = cast(_AppStateCommandGuards, state)
        magic_raw = app_state.magic_service
        if magic_raw is None:
            return None
        magic_service = cast(_MagicServiceView, magic_raw)
        if not magic_service.casting_state_manager:
            return None
        return await _get_casting_block_result(request, player_name, magic_service)
    except (AttributeError, OSError, TypeError, RuntimeError) as e:
        logger.debug("Could not check casting state", player=player_name, error=str(e))
        return None
