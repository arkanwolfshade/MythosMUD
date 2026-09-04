"""
Safe WebSocket close helpers for connection management.

Leaf module: no imports from connection_manager_methods or connection_disconnection,
so those packages can share close logic without an import cycle.
"""

from __future__ import annotations

import asyncio
from typing import Protocol

from fastapi import WebSocket
from starlette.websockets import WebSocketDisconnect, WebSocketState


class _CloseableWebSocketManager(Protocol):  # pylint: disable=too-few-public-methods  # Reason: PEP 544 Protocol stub
    def is_websocket_closed(self, ws_id: int) -> bool:
        """Return True if this WebSocket id was already marked closed."""
        ...  # pylint: disable=unnecessary-ellipsis  # Reason: Protocol stub body required by basedpyright

    def mark_websocket_closed(self, ws_id: int) -> None:
        """Record that this WebSocket id has been closed."""
        ...  # pylint: disable=unnecessary-ellipsis  # Reason: Protocol stub body required by basedpyright


def is_websocket_open_impl(_manager: object, websocket: WebSocket) -> bool:
    """Check if a WebSocket is open."""
    try:
        state: object | None = getattr(websocket, "application_state", None)
        return state != WebSocketState.DISCONNECTED
    except (AttributeError, ValueError, TypeError):
        return True


async def safe_close_websocket_impl(
    manager: _CloseableWebSocketManager,
    websocket: WebSocket,
    code: int = 1000,
    reason: str = "Connection closed",
) -> None:
    """Safely close a WebSocket connection."""
    ws_id = id(websocket)
    if manager.is_websocket_closed(ws_id):
        return
    if not is_websocket_open_impl(manager, websocket):
        manager.mark_websocket_closed(ws_id)
        return
    try:
        await asyncio.wait_for(websocket.close(code=code, reason=reason), timeout=2.0)
    except (AttributeError, ValueError, TypeError, RuntimeError, WebSocketDisconnect):
        pass
    finally:
        manager.mark_websocket_closed(ws_id)
