"""
Message handler implementations for WebSocket message routing.

This module contains the actual implementations of message handlers,
separated from the factory to avoid circular imports.
"""

from typing import Any

from fastapi import WebSocket

from ..logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)


async def handle_command_message(websocket: WebSocket, player_id: str, data: dict[str, Any]) -> None:
    """Handle command message type."""
    command = data.get("command", "")
    args = data.get("args", [])

    logger.info(
        "🚨 SERVER DEBUG: handle_command_message called",
        command=command,
        args=args,
        player_id=player_id,
        data=data,
    )

    # Import here to avoid circular imports
    from .websocket_handler import handle_game_command

    await handle_game_command(websocket, player_id, command, args)


async def handle_chat_message(websocket: WebSocket, player_id: str, data: dict[str, Any]) -> None:
    """Handle chat message type."""
    chat_message = data.get("message", "")

    # Import here to avoid circular imports
    from .websocket_handler import handle_chat_message as handle_chat

    await handle_chat(websocket, player_id, chat_message)


async def handle_ping_message(websocket: WebSocket, player_id: str, data: dict[str, Any]) -> None:
    """Handle ping message type."""
    from .envelope import build_event

    logger.debug(f"🔍 DEBUG: Received ping from player {player_id}")
    pong_event = build_event("pong", {}, player_id=player_id)
    await websocket.send_json(pong_event)
    logger.debug(f"🔍 DEBUG: Sent pong to player {player_id}")
