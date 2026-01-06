"""
System commands for MythosMUD.

This module contains handlers for system-level commands like help.
"""

from typing import Any

from ..alias_storage import AliasStorage
from ..help.help_content import get_help_content
from ..structured_logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)


async def handle_system_command(
    command_data: dict, _current_user: dict, request: Any, _alias_storage: AliasStorage | None, _player_name: str
) -> dict[str, str]:
    """
    Broadcast a system-level message via the chat service if available.
    """
    message = command_data.get("message")
    if not message:
        return {"result": "Usage: system <message>"}

    app = getattr(request, "app", None) if request else None
    state = getattr(app, "state", None) if app else None
    chat_service = getattr(state, "chat_service", None) if state else None

    if not chat_service or not hasattr(chat_service, "send_system_message"):
        return {"result": "System messaging is not available."}

    await chat_service.send_system_message(message)
    return {"result": f"System message sent: {message}"}


async def handle_help_command(
    command_data: dict, _current_user: dict, _request: Any, _alias_storage: AliasStorage | None, player_name: str
) -> dict[str, str]:
    """
    Handle the help command.

    Args:
        command_data: Command data dictionary containing args and other info
        current_user: Current user information
        request: FastAPI request object
        alias_storage: Alias storage instance
        player_name: Player name for logging

    Returns:
        dict: Help content result
    """
    # Extract args from command_data
    args: list = command_data.get("args", [])

    logger.debug("Processing help command", player_name=player_name, args=args)

    if len(args) > 1:
        logger.warning("Help command with too many arguments", player_name=player_name, args=args)
        return {"result": "Usage: help [command]"}

    command_name = args[0] if args else None
    help_content = get_help_content(command_name)

    logger.debug("Help content generated", player_name=player_name, command=command_name)
    return {"result": help_content}
