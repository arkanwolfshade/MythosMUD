"""
Communication commands for MythosMUD.

Handlers delegate heavy logic to communication_commands_flows for Lizard limits.
"""

# pylint: disable=too-many-return-statements  # Reason: Command handlers require multiple return statements for early validation returns.

from collections.abc import Mapping
from typing import cast

from structlog.stdlib import BoundLogger

from ..alias_storage import AliasStorage
from ..structured_logging.enhanced_logging_config import get_logger
from ..utils.command_parser import get_username_from_user
from .communication_commands_flows import (
    flow_global_command,
    flow_local_command,
    flow_reply_command,
    flow_say_command,
    flow_system_command,
    flow_whisper_command,
)
from .communication_commands_support import (
    PlayerWithPose,
    app_from_request,
    get_pose_persistence,
)

logger: BoundLogger = get_logger(__name__)


async def handle_say_command(
    command_data: Mapping[str, object],
    _current_user: Mapping[str, object],
    request: object | None,
    _alias_storage: AliasStorage | None,
    player_name: str,
) -> dict[str, str]:
    """Room-wide say; returns user-facing result dict."""
    return await flow_say_command(command_data, request, player_name)


async def handle_me_command(
    command_data: Mapping[str, object],
    _current_user: Mapping[str, object],
    _request: object | None,
    _alias_storage: AliasStorage | None,
    player_name: str,
) -> dict[str, str]:
    """Emote / me line."""
    logger.debug("Processing me command", player_name=player_name, command_data=command_data)
    action = command_data.get("action")
    if not isinstance(action, str) or not action:
        logger.warning("Me command with no action", player_name=player_name, command_data=command_data)
        return {"result": "Do what? Usage: me <action>"}
    logger.debug("Player performing action", player_name=player_name, action=action)
    return {"result": f"{player_name} {action}"}


async def handle_pose_command(
    command_data: Mapping[str, object],
    current_user: Mapping[str, object],
    request: object | None,
    _alias_storage: AliasStorage | None,
    player_name: str,
) -> dict[str, str]:
    """Set or clear persistent pose text."""
    logger.debug("Processing pose command", player_name=player_name, command_data=command_data)
    persistence = get_pose_persistence(app_from_request(request))
    if not persistence:
        logger.warning("Pose command failed - no persistence layer", player_name=player_name)
        return {"result": "You cannot set your pose right now."}
    player_raw = await persistence.get_player_by_name(get_username_from_user(current_user))
    player = cast(PlayerWithPose | None, player_raw)
    if not player:
        logger.warning("Pose command failed - player not found", player_name=player_name)
        return {"result": "You cannot set your pose right now."}
    pose = command_data.get("pose")
    if not pose:
        player.pose = None
        await persistence.save_player(player)
        logger.info("Player cleared pose", player_name=player_name)
        return {"result": "Your pose has been cleared."}
    pose_description = pose if isinstance(pose, str) else str(pose)
    logger.debug("Player setting pose", player_name=player_name, pose_description=pose_description)
    player.pose = pose_description
    await persistence.save_player(player)
    logger.info("Player pose set", player_name=player_name, pose_description=pose_description)
    return {"result": f"Your pose is now: {pose_description}"}


async def handle_local_command(
    command_data: Mapping[str, object],
    _current_user: Mapping[str, object],
    request: object | None,
    _alias_storage: AliasStorage | None,
    player_name: str,
) -> dict[str, str]:
    """Local channel message."""
    return await flow_local_command(command_data, request, player_name)


async def handle_global_command(
    command_data: Mapping[str, object],
    _current_user: Mapping[str, object],
    request: object | None,
    _alias_storage: AliasStorage | None,
    player_name: str,
) -> dict[str, str]:
    """Global channel message (level-gated in flow)."""
    return await flow_global_command(command_data, request, player_name)


async def handle_system_command(
    command_data: Mapping[str, object],
    _current_user: Mapping[str, object],
    request: object | None,
    _alias_storage: AliasStorage | None,
    player_name: str,
) -> dict[str, str]:
    """Admin-only system broadcast."""
    return await flow_system_command(command_data, request, player_name)


async def handle_whisper_command(
    command_data: Mapping[str, object],
    _current_user: Mapping[str, object],
    request: object | None,
    _alias_storage: AliasStorage | None,
    player_name: str,
) -> dict[str, str]:
    """Directed whisper."""
    return await flow_whisper_command(command_data, request, player_name)


async def handle_reply_command(
    command_data: Mapping[str, object],
    _current_user: Mapping[str, object],
    request: object | None,
    _alias_storage: AliasStorage | None,
    player_name: str,
) -> dict[str, str]:
    """Reply to last whisper sender."""
    return await flow_reply_command(command_data, request, player_name)
