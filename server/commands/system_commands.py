"""
System commands for MythosMUD.

This module contains handlers for system-level commands like help.
"""

from typing import Any, cast

from ..alias_storage import AliasStorage
from ..help.help_content import get_help_content
from ..structured_logging.enhanced_logging_config import get_logger
from .catalog_commands import resolve_is_admin

logger = get_logger(__name__)


async def handle_system_command(
    command_data: dict[str, Any],
    _current_user: dict[str, Any],
    request: Any,
    _alias_storage: AliasStorage | None,
    _player_name: str,
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


def _help_topic(command_data: dict[str, object]) -> str | None:
    """Topic from the validated command's ``topic`` field, falling back to the first positional arg."""
    topic: object = command_data.get("topic")
    if isinstance(topic, str) and topic.strip():
        return topic
    args: object = command_data.get("args")
    if isinstance(args, list) and args:
        return str(cast(list[object], args)[0])
    return None


async def handle_help_command(
    command_data: dict[str, object],
    current_user: object,
    request: object,
    _alias_storage: AliasStorage | None,
    player_name: str,
) -> dict[str, object]:
    """
    Handle the help command: ``help`` lists topics, ``help <command|alias|guide>`` shows one entry.

    Admin-only commands are documented only for admins. The result is HTML restricted to the tags the
    client sanitizer keeps, so it is flagged ``is_html``.
    """
    args: object = command_data.get("args")
    if isinstance(args, list) and len(cast(list[object], args)) > 1:
        logger.warning("Help command with too many arguments", player_name=player_name, args=args)
        return {"result": "Usage: help [command]"}

    topic = _help_topic(command_data)
    is_admin = await resolve_is_admin(current_user, request, player_name)
    logger.debug("Processing help command", player_name=player_name, topic=topic, is_admin=is_admin)
    return {"result": get_help_content(topic, is_admin=is_admin), "is_html": True}
