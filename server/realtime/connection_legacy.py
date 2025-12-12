"""
Legacy compatibility helpers for connection manager.

This module provides backward compatibility functions for the module-level
connection manager singleton pattern used by older tests and code.
"""

import inspect
from typing import Any
from unittest.mock import AsyncMock, Mock

from ..logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)

# Module-level connection manager for legacy compatibility
connection_manager: "Any | None" = None


_ASYNC_METHODS_REQUIRING_COMPAT: set[str] = {
    "handle_new_game_session",
    "force_cleanup",
    "check_connection_health",
    "cleanup_orphaned_data",
    "broadcast_room_event",
    "broadcast_global_event",
    "broadcast_global",
    "send_personal_message",
}


def _ensure_async_compat(manager: "Any | None") -> "Any | None":
    """
    Ensure mocked connection manager implementations expose awaitable methods.

    Many unit tests patch the module-level connection_manager with simple ``Mock``
    instances whose methods are synchronous. Production code awaits these methods,
    so this shim wraps them in AsyncMock/async functions when necessary.
    """
    if manager is None:
        return None

    for method_name in _ASYNC_METHODS_REQUIRING_COMPAT:
        if not hasattr(manager, method_name):
            continue

        attr = getattr(manager, method_name)

        # Already awaitable - nothing to do
        if inspect.iscoroutinefunction(attr) or inspect.isawaitable(attr):
            continue
        if isinstance(attr, AsyncMock):
            continue

        if isinstance(attr, Mock):
            async_mock = AsyncMock()
            # Preserve configured behaviour
            async_mock.side_effect = attr.side_effect
            async_mock.return_value = attr.return_value
            setattr(manager, method_name, async_mock)
            continue

        if callable(attr):

            async def _async_wrapper(*args, _attr=attr, **kwargs):
                result = _attr(*args, **kwargs)
                if inspect.isawaitable(result):
                    return await result
                return result

            setattr(manager, method_name, _async_wrapper)

    return manager


def set_global_connection_manager(manager: "Any | None") -> None:
    """
    Update the legacy module-level connection_manager reference.

    Args:
        manager: ConnectionManager instance to expose (or None to clear)
    """
    global connection_manager
    connection_manager = _ensure_async_compat(manager)


def get_global_connection_manager() -> "Any | None":
    """
    Retrieve the legacy module-level connection manager if one has been registered.

    Returns:
        Optional[ConnectionManager]: The module-level connection manager instance or None
    """
    return connection_manager


def resolve_connection_manager(candidate: "Any | None" = None) -> "Any | None":
    """
    Resolve a connection manager instance, preferring an explicitly supplied candidate
    and falling back to the legacy module-level reference.

    Args:
        candidate: Explicit connection manager to prefer.

    Returns:
        Optional[ConnectionManager]: The resolved connection manager instance (if any)
    """
    manager = candidate or connection_manager
    return _ensure_async_compat(manager)


def __getattr__(name: str) -> Any:
    """Lazy import for API utility functions to avoid circular dependencies."""
    if name == "broadcast_game_event":
        from .connection_manager_api import broadcast_game_event

        return broadcast_game_event
    elif name == "send_game_event":
        from .connection_manager_api import send_game_event

        return send_game_event
    elif name == "send_player_status_update":
        from .connection_manager_api import send_player_status_update

        return send_player_status_update
    elif name == "send_room_description":
        from .connection_manager_api import send_room_description

        return send_room_description
    elif name == "send_room_event":
        from .connection_manager_api import send_room_event

        return send_room_event
    elif name == "send_system_notification":
        from .connection_manager_api import send_system_notification

        return send_system_notification
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
