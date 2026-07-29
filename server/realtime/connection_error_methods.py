"""
Error-handling method implementations for ConnectionManager.

Thin wrappers that delegate to ConnectionErrorHandler via connection_delegates.
"""

from typing import Any
from uuid import UUID

from .connection_delegates import delegate_error_handler


async def detect_and_handle_error_state_impl(
    manager: Any,
    player_id: UUID,
    error_type: str,
    error_details: str,
    connection_id: str | None = None,
) -> dict[str, Any]:
    """Detect when a client is in an error state and handle it appropriately."""
    return await delegate_error_handler(
        manager.error_handler,
        "detect_and_handle_error_state",
        {
            "player_id": player_id,
            "error_type": error_type,
            "success": False,
            "errors": ["Error handler not initialized"],
        },
        player_id,
        error_type,
        error_details,
        connection_id,
    )


async def handle_websocket_error_impl(
    manager: Any,
    player_id: UUID,
    connection_id: str,
    error_type: str,
    error_details: str,
) -> dict[str, Any]:
    """Handle WebSocket-specific errors."""
    return await delegate_error_handler(
        manager.error_handler,
        "handle_websocket_error",
        {
            "player_id": player_id,
            "success": False,
            "errors": ["Error handler not initialized"],
        },
        player_id,
        connection_id,
        error_type,
        error_details,
    )


async def handle_authentication_error_impl(
    manager: Any, player_id: UUID, error_type: str, error_details: str
) -> dict[str, Any]:
    """Handle authentication-related errors."""
    return await delegate_error_handler(
        manager.error_handler,
        "handle_authentication_error",
        {
            "player_id": player_id,
            "success": False,
            "errors": ["Error handler not initialized"],
        },
        player_id,
        error_type,
        error_details,
    )


async def handle_security_violation_impl(
    manager: Any, player_id: UUID, violation_type: str, violation_details: str
) -> dict[str, Any]:
    """Handle security violations."""
    return await delegate_error_handler(
        manager.error_handler,
        "handle_security_violation",
        {
            "player_id": player_id,
            "success": False,
            "errors": ["Error handler not initialized"],
        },
        player_id,
        violation_type,
        violation_details,
    )


async def recover_from_error_impl(manager: Any, player_id: UUID, recovery_type: str = "FULL") -> dict[str, Any]:
    """Attempt to recover from an error state for a player."""
    return await delegate_error_handler(
        manager.error_handler,
        "recover_from_error",
        {
            "player_id": player_id,
            "success": False,
            "errors": ["Error handler not initialized"],
        },
        player_id,
        recovery_type,
    )
