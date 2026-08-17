"""
Lazy attribute resolution for connection_manager module exports.

Kept separate so connection_manager.py stays under Codacy file-nloc limits.
Utils must not import connection_manager_api; this module owns that edge.
"""

from __future__ import annotations


def resolve_lazy_attr(name: str, module_name: str) -> object:
    """Resolve lazy API helpers (broadcast_game_event, send_*, etc.)."""
    if name == "broadcast_game_event":
        from .connection_manager_api import broadcast_game_event

        return broadcast_game_event
    if name == "send_game_event":
        from .connection_manager_api import send_game_event

        return send_game_event
    if name == "send_player_status_update":
        from .connection_manager_api import send_player_status_update

        return send_player_status_update
    if name == "send_room_description":
        from .connection_manager_api import send_room_description

        return send_room_description
    if name == "send_room_event":
        from .connection_manager_api import send_room_event

        return send_room_event
    if name == "send_system_notification":
        from .connection_manager_api import send_system_notification

        return send_system_notification
    raise AttributeError(f"module {module_name!r} has no attribute {name!r}")
