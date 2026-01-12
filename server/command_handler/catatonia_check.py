"""
Catatonia Checking Logic for MythosMUD.

This module handles checking whether a player is in a catatonic state
and should have their commands blocked. When a player's lucidity drops
to zero, they enter catatonia and can only execute limited commands
until another player helps them recover.
"""

# pylint: disable=too-many-return-statements  # Reason: Catatonia checking requires multiple return statements for different command validation states and permission checks

import uuid
from typing import TYPE_CHECKING, Any

from ..database import get_async_session
from ..models.lucidity import PlayerLucidity
from ..structured_logging.enhanced_logging_config import get_logger
from ..utils.player_cache import cache_player, get_cached_player

if TYPE_CHECKING:
    from fastapi import Request

logger = get_logger(__name__)

# Commands that are allowed even during catatonia
CATATONIA_ALLOWED_COMMANDS = {"help", "who", "status", "time"}


async def _load_player_for_catatonia_check(request: "Request", player_name: str, persistence: Any) -> Any | None:
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


def _check_catatonia_registry(state: Any, player_id: str | uuid.UUID, player_name: str) -> tuple[bool, str | None]:
    """Check catatonia status via registry."""
    registry = getattr(state, "__dict__", {}).get("catatonia_registry")
    if registry is not None and hasattr(registry, "is_catatonic"):
        try:
            if registry.is_catatonic(player_id):
                logger.info(
                    "Catatonic player command blocked via registry",
                    player=player_name,
                )
                return (
                    True,
                    "Your body lies unresponsive, trapped in catatonia. Another must ground you.",
                )
        except (ImportError, AttributeError, TypeError, RuntimeError):  # pragma: no cover - defensive
            logger.exception("Catatonia registry lookup failed", player=player_name)
    return False, None


def _is_catatonic(lucidity_record: PlayerLucidity | None) -> bool:
    """Check if player is catatonic based on lucidity record."""
    if not lucidity_record:
        return False
    return lucidity_record.current_tier == "catatonic" or lucidity_record.current_lcd <= 0


async def _fetch_lucidity_record(session: Any, player_id_uuid: uuid.UUID, player_name: str) -> PlayerLucidity | None:
    """Fetch lucidity record from database session."""
    lucidity_record = await session.get(PlayerLucidity, player_id_uuid)
    logger.debug(
        "Lucidity record retrieved",
        player=player_name,
        player_id=player_id_uuid,
        lucidity_record_exists=bool(lucidity_record),
        current_lcd=lucidity_record.current_lcd if lucidity_record else None,
        current_tier=lucidity_record.current_tier if lucidity_record else None,
    )
    return lucidity_record


async def _query_lucidity_record(player_id_uuid: uuid.UUID, player_name: str) -> PlayerLucidity | None:
    """Query lucidity record from database with error handling."""
    try:
        async for session in get_async_session():
            try:
                return await _fetch_lucidity_record(session, player_id_uuid, player_name)
            except (ImportError, AttributeError, TypeError, RuntimeError) as e:
                logger.warning(
                    "Failed to check catatonia status in database",
                    player=player_name,
                    error=str(e),
                    error_type=type(e).__name__,
                )
                return None
    except (ImportError, AttributeError, TypeError, RuntimeError) as e:
        logger.debug(
            "Database session unavailable for catatonia check",
            player=player_name,
            error=str(e),
        )
        return None
    return None


async def _check_catatonia_database(player_id_uuid: uuid.UUID, player_name: str) -> tuple[bool, str | None]:
    """Check catatonia status via database."""
    lucidity_record = await _query_lucidity_record(player_id_uuid, player_name)
    if lucidity_record and _is_catatonic(lucidity_record):
        logger.info(
            "Catatonic player command blocked",
            player=player_name,
            lucidity=lucidity_record.current_lcd,
            tier=lucidity_record.current_tier,
        )
        return (
            True,
            "Your body lies unresponsive, trapped in catatonia. Another must ground you.",
        )
    return False, None


def _convert_player_id_to_uuid(player_id: Any, player_name: str) -> uuid.UUID | None:
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


async def check_catatonia_block(player_name: str, command: str, request: "Request") -> tuple[bool, str | None]:
    """
    Determine whether to block command execution due to catatonia.

    A catatonic player has lost all lucidity and cannot take most actions
    until another player helps ground them back to reality.

    Args:
        player_name: The name of the player
        command: The command being executed
        request: The FastAPI request object

    Returns:
        Tuple of (should_block, blocking_message)
    """
    if command in CATATONIA_ALLOWED_COMMANDS:
        return False, None

    app = getattr(request, "app", None)
    state = getattr(app, "state", None) if app else None
    if state is None:
        return False, None

    persistence = getattr(state, "persistence", None)
    if persistence is None:
        return False, None

    player = await _load_player_for_catatonia_check(request, player_name, persistence)
    if not player:
        return False, None

    player_id = getattr(player, "player_id", None)
    if not player_id:
        return False, None

    # Check registry first
    blocked, message = _check_catatonia_registry(state, player_id, player_name)
    if blocked:
        return blocked, message

    # Check database - convert player_id to UUID if needed
    player_id_uuid = _convert_player_id_to_uuid(player_id, player_name)
    if player_id_uuid is None:
        return False, None

    logger.debug(
        "Starting catatonia check",
        player=player_name,
        command=command,
        player_id=player_id_uuid,
    )
    return await _check_catatonia_database(player_id_uuid, player_name)
