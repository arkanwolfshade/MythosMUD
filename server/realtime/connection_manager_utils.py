"""
Utility functions and module-level code for ConnectionManager.

This module contains helper functions and lazy import logic that were extracted
from connection_manager.py to reduce its line count.
"""

import inspect
from collections.abc import Callable
from typing import Any, cast

from ..container import ApplicationContainer

# Constants for async compatibility
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
    Ensure connection manager methods are awaitable.

    Wraps synchronous callables in async wrappers to ensure production code
    can await methods that might be synchronous (e.g., in test scenarios).
    Uses duck typing to detect mock-like objects without importing test utilities.
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

        # Wrap any callable (including mock-like objects) in an async wrapper
        # This works for both real methods and test mocks without importing Mock types
        if callable(attr):

            async def _async_wrapper(*args: Any, _attr: Any = attr, **kwargs: Any) -> Any:
                result = _attr(*args, **kwargs)
                if inspect.isawaitable(result):
                    return await result
                return result

            setattr(manager, method_name, _async_wrapper)

    return manager


def resolve_connection_manager(candidate: "Any | None" = None) -> "Any | None":
    """
    Resolve a connection manager instance.

    Prefers explicitly supplied candidate, then tries to resolve from:
    1. FastAPI app state container (if available in context)
    2. ApplicationContainer.get_instance() (for background tasks)

    Args:
        candidate: Explicit connection manager to prefer.

    Returns:
        Optional[ConnectionManager]: The resolved connection manager instance (if any)
    """
    if candidate is not None:
        return _ensure_async_compat(candidate)

    # Try to get from app state (for API routes)
    # This requires accessing the current request context, which is not always available
    # For now, try ApplicationContainer.get_instance() as fallback
    try:
        container = ApplicationContainer.get_instance()
        if container is not None:
            manager = getattr(container, "connection_manager", None)
            if manager is not None:
                return _ensure_async_compat(manager)
    except (AttributeError, RuntimeError, ImportError):
        # Container not available or not initialized
        pass

    return None


def lazy_import_api_function(name: str) -> Any:
    """
    Lazy import for API utility functions to avoid circular dependencies.

    Args:
        name: Name of the function to import

    Returns:
        The imported function, cast to Callable

    Raises:
        AttributeError: If the function name is not recognized
    """
    if name == "broadcast_game_event":
        from .connection_manager_api import (  # pylint: disable=import-outside-toplevel  # Reason: Lazy import to avoid circular dependencies
            broadcast_game_event,
        )

        return cast(Callable[..., Any], broadcast_game_event)
    if name == "send_game_event":
        from .connection_manager_api import (  # pylint: disable=import-outside-toplevel  # Reason: Lazy import to avoid circular dependencies
            send_game_event,
        )

        return cast(Callable[..., Any], send_game_event)
    if name == "send_player_status_update":
        from .connection_manager_api import (  # pylint: disable=import-outside-toplevel  # Reason: Lazy import to avoid circular dependencies
            send_player_status_update,
        )

        return cast(Callable[..., Any], send_player_status_update)
    if name == "send_room_description":
        from .connection_manager_api import (  # pylint: disable=import-outside-toplevel  # Reason: Lazy import to avoid circular dependencies
            send_room_description,
        )

        return cast(Callable[..., Any], send_room_description)
    if name == "send_room_event":
        from .connection_manager_api import (  # pylint: disable=import-outside-toplevel  # Reason: Lazy import to avoid circular dependencies
            send_room_event,
        )

        return cast(Callable[..., Any], send_room_event)
    if name == "send_system_notification":
        from .connection_manager_api import (  # pylint: disable=import-outside-toplevel  # Reason: Lazy import to avoid circular dependencies
            send_system_notification,
        )

        return cast(Callable[..., Any], send_system_notification)
    raise AttributeError(f"Unknown API function: {name}")
