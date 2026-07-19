"""
WebSocket message validation, CSRF/JWT resolution, and rate limiting.

Extracted from websocket_handler for Lizard file-nloc limits.
"""

import json
import time
import uuid
from collections.abc import Mapping
from typing import TYPE_CHECKING, cast

from fastapi import WebSocket
from structlog.stdlib import BoundLogger

from ..error_types import ErrorMessages, ErrorType, create_websocket_error_response
from ..structured_logging.enhanced_logging_config import get_logger

if TYPE_CHECKING:
    from .connection_manager import ConnectionManager
    from .message_validator import WebSocketMessageValidator

logger: BoundLogger = get_logger(__name__)


async def check_websocket_message_rate_limit(
    websocket: WebSocket, connection_id: str | None, player_id_str: str, connection_manager: "ConnectionManager"
) -> bool:
    """
    Check rate limit and send error response if exceeded.

    Returns:
        True if rate limit check passed, False if exceeded
    """
    if not connection_id:
        return True

    if connection_manager.rate_limiter.check_message_rate_limit(connection_id):
        return True

    logger.warning("Message rate limit exceeded", player_id=player_id_str, connection_id=connection_id)
    rate_limit_info = connection_manager.rate_limiter.get_message_rate_limit_info(connection_id)
    rli: Mapping[str, object] = cast(Mapping[str, object], rate_limit_info)
    max_attempts_raw = rli.get("max_attempts", 0)
    reset_time_raw = rli.get("reset_time", 0.0)
    max_attempts = int(max_attempts_raw) if isinstance(max_attempts_raw, int | float) else 0
    reset_at = float(reset_time_raw) if isinstance(reset_time_raw, int | float) else 0.0
    retry_after = max(0, int(reset_at - time.time()))
    error_response = create_websocket_error_response(
        ErrorType.RATE_LIMIT_EXCEEDED,
        f"Message rate limit exceeded. Limit: {max_attempts} messages per minute. Try again in {retry_after} seconds.",
        ErrorMessages.RATE_LIMIT_EXCEEDED,
        {
            "player_id": player_id_str,
            "connection_id": connection_id,
            "rate_limit_info": rate_limit_info,
        },
    )
    await websocket.send_json(error_response)
    return False


def extract_csrf_token_from_raw(
    data: str,
    validator: "WebSocketMessageValidator",
) -> str | None:
    """Parse outer JSON once to read csrfToken/csrf_token when metadata lacks a stored JWT."""
    try:
        parsed = cast(object, json.loads(data))
    except json.JSONDecodeError:
        return None
    if not isinstance(parsed, dict):
        return None
    raw_token = validator._extract_csrf_token_string(cast(dict[str, object], parsed))  # noqa: SLF001
    return raw_token if isinstance(raw_token, str) else None


def get_connection_csrf_context(
    websocket: WebSocket,
    connection_manager: "ConnectionManager | None",
) -> tuple[str | None, str | None, object | None]:
    """Return stored JWT, connection_id, and metadata from the active WebSocket connection."""
    if connection_manager is None:
        return None, None, None

    connection_id = connection_manager.get_connection_id_from_websocket(websocket)
    if connection_id is None:
        return None, None, None

    metadata = connection_manager.connection_metadata.get(connection_id)
    token_raw = cast(object | None, getattr(metadata, "token", None))
    expected_token = token_raw if isinstance(token_raw, str) else None
    return expected_token, connection_id, metadata


def restore_csrf_on_connection_metadata(
    metadata: object,
    connection_id: str,
    csrf_token: str,
    player_id_str: str,
) -> None:
    """Persist a validated message JWT on connection metadata after reconnect edge cases."""
    setattr(metadata, "token", csrf_token)  # noqa: B010  # Reason: ConnectionMetadata is a mutable dataclass-like object updated in place on reconnect heal
    setattr(metadata, "last_token_validation", time.time())  # noqa: B010
    logger.info(
        "Restored CSRF token from message JWT on connection metadata",
        player_id=player_id_str,
        connection_id=connection_id,
    )


async def validate_message_csrf_and_restore_metadata(
    data: str,
    player_id_str: str,
    validator: "WebSocketMessageValidator",
    connection_manager: "ConnectionManager",
    connection_id: str | None,
    metadata: object | None,
) -> str | None:
    """Validate csrfToken from the message body and optionally heal connection metadata."""
    csrf_from_message = extract_csrf_token_from_raw(data, validator)
    if csrf_from_message is None:
        return None

    player_id_uuid = uuid.UUID(player_id_str)
    if not await connection_manager._validate_token(csrf_from_message, player_id_uuid):  # pylint: disable=protected-access  # Reason: JWT validation lives on ConnectionManager; handler must reuse it when metadata.token is missing
        return None

    if connection_id is not None and metadata is not None:
        restore_csrf_on_connection_metadata(metadata, connection_id, csrf_from_message, player_id_str)

    return csrf_from_message


async def resolve_expected_csrf_token(
    websocket: WebSocket,
    data: str,
    player_id_str: str,
    validator: "WebSocketMessageValidator",
    connection_manager: "ConnectionManager | None",
) -> str | None:
    """
    Resolve the CSRF/JWT token used for message validation.

    Prefer connection metadata from handshake. When metadata has no token but the client
    sends csrfToken (common after reconnect edge cases), validate the JWT and restore metadata.
    """
    expected_token, connection_id, metadata = get_connection_csrf_context(websocket, connection_manager)
    if expected_token is not None:
        return expected_token

    if connection_manager is None:
        return None

    return await validate_message_csrf_and_restore_metadata(
        data,
        player_id_str,
        validator,
        connection_manager,
        connection_id,
        metadata,
    )


async def validate_websocket_message(
    websocket: WebSocket,
    data: str,
    player_id_str: str,
    validator: "WebSocketMessageValidator",
    connection_manager: "ConnectionManager | None" = None,
) -> dict[str, object] | None:
    """
    Validate message and send error response if validation fails.

    Returns:
        Validated message dict if successful, None if validation failed
    """
    from .message_validator import MessageValidationError

    try:
        expected_token = await resolve_expected_csrf_token(
            websocket,
            data,
            player_id_str,
            validator,
            connection_manager,
        )
        message = validator.parse_and_validate(
            data=data,
            player_id=player_id_str,
            schema=None,
            csrf_token=expected_token,
        )
        return message
    except MessageValidationError as e:
        logger.warning(
            "Message validation failed",
            player_id=player_id_str,
            error_type=e.error_type,
            error_message=e.message,
        )
        error_response = create_websocket_error_response(
            ErrorType.INVALID_FORMAT,
            f"Message validation failed: {e.message}",
            ErrorMessages.INVALID_FORMAT,
            {"player_id": player_id_str, "error_type": e.error_type},
        )
        await websocket.send_json(error_response)
        return None
