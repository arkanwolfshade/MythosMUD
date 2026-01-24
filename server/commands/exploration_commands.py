"""
Exploration commands for MythosMUD.

This module contains handlers for exploration-related commands like look and go.
This is a thin wrapper that imports and re-exports command handlers from separate modules.
"""

from typing import Any

from ..alias_storage import AliasStorage

# Import go command handler
from .go_command import handle_go_command

# Import look command handler
from .look_command import handle_look_command


async def handle_explore_command(
    command_data: dict[str, Any],
    current_user: dict[str, Any],
    request: Any,
    _alias_storage: AliasStorage | None,
    player_name: str,
) -> dict[str, str]:
    """
    Handle exploration requests by returning a simple message.

    This lightweight implementation keeps parity with existing unit tests and
    avoids side effects while broader exploration features live elsewhere.
    """
    app = getattr(request, "app", None) if request else None
    state = getattr(app, "state", None) if app else None
    persistence = getattr(state, "persistence", None) if state else None

    if not persistence or not hasattr(persistence, "get_player_by_name"):
        return {"result": "Exploration is not available at this time."}

    target_name = command_data.get("name") or player_name or current_user.get("name")
    player = await persistence.get_player_by_name(target_name)

    if player is None:
        return {"result": "Player not found for exploration."}

    return {"result": f"{target_name} explores the surrounding area."}


# Re-export public functions for backward compatibility
__all__ = ["handle_look_command", "handle_go_command", "handle_explore_command"]
