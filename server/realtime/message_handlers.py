"""
Message handler implementations for WebSocket message routing.

This module contains the actual implementations of message handlers,
separated from the factory to avoid circular imports.
"""

import uuid
from typing import Any

from fastapi import WebSocket

from ..structured_logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)


async def handle_command_message(websocket: WebSocket, player_id: str, data: dict[str, Any]) -> None:
    """Handle command message type."""
    command = data.get("command", "")
    args = data.get("args", [])

    # Import here to avoid circular imports
    from .websocket_handler import handle_game_command

    await handle_game_command(websocket, player_id, command, args)


async def handle_chat_message(websocket: WebSocket, player_id: str, data: dict[str, Any]) -> None:
    """Handle chat message type."""
    chat_message = data.get("message", "")

    # Import here to avoid circular imports
    from .websocket_handler import handle_chat_message as handle_chat

    await handle_chat(websocket, player_id, chat_message)


async def handle_ping_message(websocket: WebSocket, player_id: str, _data: dict[str, Any]) -> None:  # pylint: disable=unused-argument  # Reason: Parameter required for message handler interface, data not used for ping
    """Handle ping message type."""
    from .envelope import build_event

    logger.debug("🔍 DEBUG: Received ping", player_id=player_id)
    pong_event = build_event("pong", {}, player_id=player_id)
    await websocket.send_json(pong_event)
    logger.debug("🔍 DEBUG: Sent pong", player_id=player_id)


async def handle_follow_response_message(websocket: WebSocket, player_id: str, data: dict[str, Any]) -> None:
    """Handle follow_response message (accept/decline follow request)."""
    from .connection_manager_api import send_game_event
    from .envelope import build_event

    request_id = data.get("request_id")
    accept = data.get("accept", False)
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
        result = await follow_service.accept_follow(player_id, str(request_id))
        requestor_id = result.get("requestor_id")
        if result.get("success") and requestor_id:
            followee_name = None
            persistence = getattr(container, "async_persistence", None)
            if persistence:
                try:
                    player_uuid = uuid.UUID(player_id) if isinstance(player_id, str) else player_id
                    followee = await persistence.get_player_by_id(player_uuid)
                    followee_name = getattr(followee, "name", None) if followee else str(player_id)
                except (ValueError, TypeError, AttributeError):
                    followee_name = str(player_id)
            if followee_name:
                await send_game_event(
                    requestor_id,
                    "follow_state",
                    {"following": {"target_name": followee_name, "target_type": "player"}},
                )
    else:
        result = await follow_service.decline_follow(player_id, str(request_id))
        requestor_id = result.get("requestor_id")
        if requestor_id:
            await send_game_event(
                requestor_id,
                "follow_state",
                {"following": None},
            )
    await websocket.send_json(
        build_event("command_response", {"result": result.get("result", "Done.")}, player_id=player_id)
    )


async def handle_party_invite_response_message(websocket: WebSocket, player_id: str, data: dict[str, Any]) -> None:
    """Handle party_invite_response message (accept/decline party invite)."""
    from .envelope import build_event

    invite_id = data.get("invite_id")
    accept = data.get("accept", False)
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
        result = await party_service.accept_party_invite(player_id, str(invite_id))
    else:
        result = await party_service.decline_party_invite(player_id, str(invite_id))
    await websocket.send_json(
        build_event("command_response", {"result": result.get("result", "Done.")}, player_id=player_id)
    )
