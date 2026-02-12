"""
Follow commands for MythosMUD.

Handlers for /follow, /unfollow, and /following.
Uses the same target resolution as combat (TargetResolutionService) for consistent naming.
"""

from __future__ import annotations

from typing import Any, Literal

from ..alias_storage import AliasStorage
from ..schemas.shared import TargetType as SchemaTargetType
from ..services.target_resolution_service import TargetResolutionService
from ..structured_logging.enhanced_logging_config import get_logger
from ..utils.command_parser import get_username_from_user

logger = get_logger(__name__)

TargetType = Literal["player", "npc"]


def _get_container(request: Any) -> Any:
    """Get application container from request."""
    app = getattr(request, "app", None) if request else None
    if not app or not hasattr(app, "state"):
        return None
    return getattr(app.state, "container", None)


async def handle_follow_command(
    command_data: dict[str, Any],
    current_user: dict[str, Any],
    request: Any,
    alias_storage: AliasStorage | None,
    player_name: str,
) -> dict[str, Any]:
    """Handle /follow <target>. Target must be a player or NPC in the same room."""
    _ = (alias_storage, player_name)
    container = _get_container(request)
    if not container or not getattr(container, "follow_service", None):
        return {"result": "Follow is not available."}
    async_persistence = getattr(container, "async_persistence", None)
    if not async_persistence:
        return {"result": "Follow is not available."}

    target_identifier = command_data.get("target")
    if not target_identifier or not str(target_identifier).strip():
        return {"result": "Follow who? Usage: follow <player or NPC name>"}

    username = get_username_from_user(current_user)
    player = await async_persistence.get_player_by_name(username)
    if not player:
        return {"result": "You are not in the game."}
    requestor_id = getattr(player, "player_id", None)
    if not requestor_id:
        return {"result": "Unable to identify you."}
    requestor_name = getattr(player, "name", username) or username

    # Use same target resolution as combat (partial name match, disambiguation).
    player_service = getattr(container, "player_service", None)
    if not player_service:
        return {"result": "Follow is not available."}
    target_resolution = TargetResolutionService(async_persistence, player_service)
    target_result = await target_resolution.resolve_target(requestor_id, str(target_identifier).strip())
    if not target_result.success:
        return {"result": target_result.error_message or "No such player or NPC here."}
    match = target_result.get_single_match()
    if not match:
        return {"result": target_result.error_message or "No such player or NPC here."}

    target_id = match.target_id
    target_type_str: TargetType = "player" if match.target_type == SchemaTargetType.PLAYER else "npc"
    target_display_name = match.target_name

    follow_service = container.follow_service
    result = await follow_service.request_follow(
        requestor_id, target_id, target_type_str, requestor_name, target_display_name=target_display_name
    )
    return {"result": result.get("result", "Done.")}


async def handle_unfollow_command(
    command_data: dict[str, Any],
    current_user: dict[str, Any],
    request: Any,
    alias_storage: AliasStorage | None,
    player_name: str,
) -> dict[str, Any]:
    """Handle /unfollow."""
    _ = (alias_storage, command_data, player_name)
    container = _get_container(request)
    if not container or not getattr(container, "follow_service", None):
        return {"result": "Follow is not available."}

    username = get_username_from_user(current_user)
    async_persistence = getattr(container, "async_persistence", None)
    if not async_persistence:
        return {"result": "Unable to identify you."}
    player = await async_persistence.get_player_by_name(username)
    if not player:
        return {"result": "You are not in the game."}
    player_id = getattr(player, "player_id", None)
    if not player_id:
        return {"result": "Unable to identify you."}

    result = container.follow_service.unfollow(player_id)
    return {"result": result.get("result", "You are no longer following anyone.")}


async def handle_following_command(
    command_data: dict[str, Any],
    current_user: dict[str, Any],
    request: Any,
    alias_storage: AliasStorage | None,
    player_name: str,
) -> dict[str, Any]:
    """Handle /following - show who you follow and who follows you."""
    _ = (alias_storage, command_data, player_name)
    container = _get_container(request)
    if not container or not getattr(container, "follow_service", None):
        return {"result": "Follow is not available."}

    username = get_username_from_user(current_user)
    async_persistence = getattr(container, "async_persistence", None)
    if not async_persistence:
        return {"result": "Unable to identify you."}
    player = await async_persistence.get_player_by_name(username)
    if not player:
        return {"result": "You are not in the game."}
    player_id = getattr(player, "player_id", None)
    if not player_id:
        return {"result": "Unable to identify you."}

    follow_service = container.follow_service
    display = await follow_service.get_following_display(player_id, async_persistence)
    return {"result": display}
