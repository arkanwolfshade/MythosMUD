"""
System commands for MythosMUD.

This module contains handlers for system-level commands like help.
"""

from typing import Any

from ..alias_storage import AliasStorage
from ..help.help_content import get_help_content
from ..logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)


async def handle_help_command(
    args: list, current_user: dict, request: Any, alias_storage: AliasStorage, player_name: str
) -> dict[str, str]:
    """
    Handle the help command.

    Args:
        args: Command arguments
        current_user: Current user information
        request: FastAPI request object
        alias_storage: Alias storage instance
        player_name: Player name for logging

    Returns:
        dict: Help content result
    """
    logger.debug("Processing help command", player_name=player_name, args=args)

    if len(args) > 1:
        logger.warning("Help command with too many arguments", player_name=player_name, args=args)
        return {"result": "Usage: help [command]"}

    command_name = args[0] if args else None
    help_content = get_help_content(command_name)

    logger.debug("Help content generated", player_name=player_name, command=command_name)
    return {"result": help_content}
