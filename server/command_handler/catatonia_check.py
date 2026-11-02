"""
Catatonia Checking Logic for MythosMUD.

This module handles checking whether a player is in a catatonic state
and should have their commands blocked. When a player's lucidity drops
to zero, they enter catatonia and can only execute limited commands
until another player helps them recover (or they restore their own
mind with an item: ``use`` is allowed, and the use command refuses the rest)."""

# pylint: disable=too-many-return-statements  # Reason: Catatonia checking requires multiple return statements for different command validation states and permission checks

from __future__ import annotations

import uuid
from typing import Protocol, cast

from structlog.stdlib import BoundLogger

from ..commands.inventory_command_helpers import player_registry
from ..game.player_registry import LucidityData
from ..services.catatonia_state import CATATONIA_BLOCK_MESSAGE, is_catatonic_lucidity
from ..structured_logging.enhanced_logging_config import get_logger
from ..utils.command_parser import USE_ALIASES
from ..utils.player_cache import cache_player, get_cached_player
from .command_execution_request import CommandExecutionRequest, command_request_app_state

logger: BoundLogger = get_logger(__name__)

# Commands that are allowed even during catatonia
# ``use`` and its verbs pass: the use command itself refuses anything that does not restore LCD (#1148).
CATATONIA_ALLOWED_COMMANDS = frozenset({"help", "who", "status", "time", "use", *USE_ALIASES})


class _PersistenceGetPlayerByName(Protocol):  # pylint: disable=too-few-public-methods
    """Minimal persistence surface used by catatonia load path."""

    async def get_player_by_name(self, player_name: str) -> object | None: ...  # pylint: disable=missing-function-docstring


async def _load_player_for_catatonia_check(
    request: CommandExecutionRequest, player_name: str, persistence: _PersistenceGetPlayerByName
) -> object | None:
    """Load player for catatonia check, using cache if available."""
    player = get_cached_player(request, player_name)
    if player is None:
        try:
            player = await persistence.get_player_by_name(player_name)
            cache_player(request, player_name, player)
        except Exception:  # pylint: disable=broad-except  # pragma: no cover - defensive
            # Catch all exceptions to prevent catatonia check from blocking commands
            # when database/persistence errors occur
            logger.debug(
                "Failed to load player for catatonia check",
                player=player_name,
                exc_info=True,
            )
            return None
    return player


def _registry_player_id_value(raw: object) -> uuid.UUID | str:
    """Normalize player_id for CatatoniaRegistry.is_catatonic (uuid.UUID | str)."""
    if isinstance(raw, uuid.UUID | str):
        return raw
    return str(raw)


def _check_catatonia_registry(state: object, player_id: uuid.UUID | str, player_name: str) -> tuple[bool, str | None]:
    """Check catatonia status via registry."""
    # getattr: works with __slots__ / Starlette State; avoid probing raw __dict__.
    registry: object | None = cast(object | None, getattr(state, "catatonia_registry", None))
    if registry is None:
        return False, None
    # Explicit None branch before callable(): cast(object|None)+callable-only made mypy mark try as unreachable.
    raw_is_cat: object | None = cast(object | None, getattr(registry, "is_catatonic", None))
    if raw_is_cat is None:
        return False, None
    if not callable(raw_is_cat):
        return False, None
    try:
        if raw_is_cat(player_id):
            logger.info(
                "Catatonic player command blocked via registry",
                player=player_name,
            )
            return True, CATATONIA_BLOCK_MESSAGE
    except ImportError, AttributeError, TypeError, RuntimeError:  # pragma: no cover - defensive
        logger.exception("Catatonia registry lookup failed", player=player_name)
    return False, None


async def _query_lucidity_record(player_id_uuid: uuid.UUID, player_name: str) -> LucidityData | None:
    """The player's lucidity from the player registry, or None if it cannot be read."""
    try:
        player = await player_registry().get(player_id_uuid)
    except (ImportError, AttributeError, TypeError, RuntimeError) as e:
        logger.warning(
            "Failed to check catatonia status",
            player=player_name,
            error=str(e),
            error_type=type(e).__name__,
        )
        return None
    lucidity = player.lucidity.data if player is not None else None
    logger.debug(
        "Lucidity record retrieved",
        player=player_name,
        player_id=player_id_uuid,
        lucidity_record_exists=lucidity is not None,
        current_lcd=lucidity.lcd if lucidity else None,
        current_tier=lucidity.tier if lucidity else None,
    )
    return lucidity


async def _check_catatonia_database(player_id_uuid: uuid.UUID, player_name: str) -> tuple[bool, str | None]:
    """Check catatonia status via database."""
    lucidity_record = await _query_lucidity_record(player_id_uuid, player_name)
    if lucidity_record and is_catatonic_lucidity(lucidity_record):
        logger.info(
            "Catatonic player command blocked",
            player=player_name,
            lucidity=lucidity_record.lcd,
            tier=lucidity_record.tier,
        )
        return True, CATATONIA_BLOCK_MESSAGE
    return False, None


def _convert_player_id_to_uuid(player_id: object, player_name: str) -> uuid.UUID | None:
    """Convert player_id to UUID, returning None if conversion fails."""
    try:
        if isinstance(player_id, uuid.UUID):
            return player_id
        if isinstance(player_id, str) and len(player_id) == 36:  # Valid UUID string length
            return uuid.UUID(player_id)
        # Invalid player_id format, skip database check
        logger.debug(
            "Skipping catatonia database check - invalid player_id format",
            player=player_name,
            player_id_type=type(player_id).__name__,
        )
        return None
    except (ValueError, AttributeError, TypeError) as e:
        # Invalid UUID format, skip database check
        logger.debug(
            "Skipping catatonia database check - UUID conversion failed",
            player=player_name,
            error=str(e),
        )
        return None


async def check_catatonia_block(
    player_name: str, command: str, request: CommandExecutionRequest
) -> tuple[bool, str | None]:
    """
    Determine whether to block command execution due to catatonia.

    A catatonic player has lost all lucidity and cannot take most actions
    until another player helps ground them back to reality.

    Args:
        player_name: The name of the player
        command: The command being executed
        request: HTTP Request or WebSocketRequestContext (CommandExecutionRequest)

    Returns:
        Tuple of (should_block, blocking_message)
    """
    if command in CATATONIA_ALLOWED_COMMANDS:
        return False, None

    state = command_request_app_state(request)
    if state is None:
        return False, None

    persistence = getattr(state, "persistence", None)
    if persistence is None:
        return False, None

    persistence_typed = cast(_PersistenceGetPlayerByName, persistence)
    player = await _load_player_for_catatonia_check(request, player_name, persistence_typed)
    if not player:
        return False, None

    player_obj: object = player
    player_id_raw: object | None = getattr(player_obj, "player_id", None)
    if player_id_raw is None:
        return False, None

    registry_key = _registry_player_id_value(player_id_raw)

    # Check registry first
    blocked, message = _check_catatonia_registry(state, registry_key, player_name)
    if blocked:
        return blocked, message

    # Check database - convert player_id to UUID if needed
    player_id_uuid = _convert_player_id_to_uuid(player_id_raw, player_name)
    if player_id_uuid is None:
        return False, None

    logger.debug(
        "Starting catatonia check",
        player=player_name,
        command=command,
        player_id=player_id_uuid,
    )
    return await _check_catatonia_database(player_id_uuid, player_name)
