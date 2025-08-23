"""
Message handler implementations for WebSocket message routing.

This module contains the actual implementations of message handlers,
separated from the factory to avoid circular imports.
"""

from typing import Any

from fastapi import WebSocket

from ..logging_config import get_logger

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


async def handle_ping_message(websocket: WebSocket, player_id: str, data: dict[str, Any]) -> None:
    """Handle ping message type."""
    await websocket.send_json({"type": "pong"})
