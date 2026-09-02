"""
Message handler implementations for WebSocket message routing.

This module contains the actual implementations of message handlers,
separated from the factory to avoid circular imports.

Each handler receives the full validated envelope (see `server/schemas/realtime/websocket_messages.py`,
`#765`), not a raw dict — field access is typed attribute access, and a missing/malformed field is
already impossible by the time a handler runs.
"""

import uuid
from typing import TYPE_CHECKING

from fastapi import WebSocket

from ..schemas.realtime.websocket_messages import (
    ChatMessage,
    ClientErrorReportMessage,
    CommandMessage,
    FollowResponseMessage,
    GameCommandMessage,
    PartyInviteResponseMessage,
    PingMessage,
)
from ..structured_logging.enhanced_logging_config import get_logger

if TYPE_CHECKING:
    from ..container.main import ApplicationContainer

logger = get_logger(__name__)


async def handle_client_error_report_message(
    _websocket: WebSocket, player_id: str, message: ClientErrorReportMessage
) -> None:  # pylint: disable=unused-argument  # Reason: _websocket required by handler interface, not used for fire-and-forget logging
    """Handle client_error_report: log client-reported errors to errors.log (via ERROR-level aggregator)."""
    logger.error(
        "Client-reported error",
        player_id=player_id,
        error_type=message.data.error_type or "unknown",
        message=message.data.message or "No message",
        context=message.data.context or {},
    )


async def handle_command_message(
    websocket: WebSocket, player_id: str, message: CommandMessage | GameCommandMessage
) -> None:
    """Handle command message type."""
    # Import here to avoid circular imports
    from .websocket_handler import handle_game_command

    args: list[object] = list(message.data.args)
    await handle_game_command(websocket, player_id, message.data.command, args)


async def handle_chat_message(websocket: WebSocket, player_id: str, message: ChatMessage) -> None:
    """Handle chat message type."""
    # Import here to avoid circular imports
    from .websocket_handler import handle_chat_message as handle_chat

    await handle_chat(websocket, player_id, message.data.message)


async def handle_ping_message(
    websocket: WebSocket,
    player_id: str,
    _message: PingMessage,  # pylint: disable=unused-argument  # Reason: Parameter required for handler interface; PingMessage carries no data
) -> None:
    """Handle ping message type."""
    from .envelope import build_event

    logger.debug("🔍 DEBUG: Received ping", player_id=player_id)
    pong_event = build_event("pong", {}, player_id=player_id)
    await websocket.send_json(pong_event)
    logger.debug("🔍 DEBUG: Sent pong", player_id=player_id)


async def _resolve_followee_display_name(container: "ApplicationContainer", player_id: str) -> str | None:
    """Resolve the accepting player's display name for a follow-accepted notification."""
    persistence = getattr(container, "async_persistence", None)
    if not persistence:
        return None
    try:
        player_uuid = uuid.UUID(player_id) if isinstance(player_id, str) else player_id
        followee = await persistence.get_player_by_id(player_uuid)
        return getattr(followee, "name", None) if followee else str(player_id)
    except (ValueError, TypeError, AttributeError):
        return str(player_id)


async def _notify_follow_accepted(container: "ApplicationContainer", player_id: str, result: dict[str, object]) -> None:
    """Send a follow_state event to the requestor once their follow request is accepted."""
    from .connection_manager_api import send_game_event

    requestor_id = result.get("requestor_id")
    if not (result.get("success") and isinstance(requestor_id, str)):
        return
    followee_name = await _resolve_followee_display_name(container, player_id)
    if followee_name:
        await send_game_event(
            requestor_id,
            "follow_state",
            {"following": {"target_name": followee_name, "target_type": "player"}},
        )


async def _notify_follow_declined(result: dict[str, object]) -> None:
    """Send a follow_state event clearing the requestor's pending follow."""
    from .connection_manager_api import send_game_event

    requestor_id = result.get("requestor_id")
    if isinstance(requestor_id, str):
        await send_game_event(requestor_id, "follow_state", {"following": None})


async def handle_follow_response_message(websocket: WebSocket, player_id: str, message: FollowResponseMessage) -> None:
    """Handle follow_response message (accept/decline follow request)."""
    from .envelope import build_event

    request_id = message.data.request_id
    accept = message.data.accept
    if not request_id:
        await websocket.send_json(
            build_event("command_response", {"result": "Invalid follow response."}, player_id=player_id)
        )
        return
    from ..container import get_container

    container = get_container()
    if not container or not getattr(container, "follow_service", None):
        await websocket.send_json(
            build_event("command_response", {"result": "Follow is not available."}, player_id=player_id)
        )
        return
    follow_service = container.follow_service
    if accept:
        result = await follow_service.accept_follow(player_id, request_id)
        await _notify_follow_accepted(container, player_id, result)
    else:
        result = await follow_service.decline_follow(player_id, request_id)
        await _notify_follow_declined(result)
    await websocket.send_json(
        build_event("command_response", {"result": result.get("result", "Done.")}, player_id=player_id)
    )


async def handle_party_invite_response_message(
    websocket: WebSocket, player_id: str, message: PartyInviteResponseMessage
) -> None:
    """Handle party_invite_response message (accept/decline party invite)."""
    from .envelope import build_event

    invite_id = message.data.invite_id
    accept = message.data.accept
    if not invite_id:
        await websocket.send_json(
            build_event("command_response", {"result": "Invalid party invite response."}, player_id=player_id)
        )
        return
    from ..container import get_container

    container = get_container()
    if not container or not getattr(container, "party_service", None):
        await websocket.send_json(
            build_event("command_response", {"result": "Party is not available."}, player_id=player_id)
        )
        return
    party_service = container.party_service
    if accept:
        result = await party_service.accept_party_invite(player_id, invite_id)
    else:
        result = await party_service.decline_party_invite(player_id, invite_id)
    await websocket.send_json(
        build_event("command_response", {"result": result.get("result", "Done.")}, player_id=player_id)
    )
