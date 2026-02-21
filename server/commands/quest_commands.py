"""
Quest commands: journal / quests (quest log), quest abandon <name>.

Returns formatted quest log for journal/quests; abandons an active quest by common name.
"""

from __future__ import annotations

import uuid
from typing import Any

from ..alias_storage import AliasStorage
from ..game.quest import QuestService
from ..structured_logging.enhanced_logging_config import get_logger
from ..utils.command_parser import get_username_from_user

logger = get_logger(__name__)


def _get_quest_service(request: Any) -> QuestService | None:
    """Get QuestService from request app container, or None if unavailable."""
    app = request.app if request else None
    if not app or not getattr(app.state, "container", None):
        return None
    quest_service = getattr(app.state.container, "quest_service", None)
    if not isinstance(quest_service, QuestService):
        return None
    return quest_service


def _get_container_and_persistence(request: Any) -> tuple[Any, Any] | None:
    """Get container and async_persistence from request, or None."""
    app = request.app if request else None
    if not app or not getattr(app.state, "container", None):
        return None
    container = app.state.container
    persistence = getattr(container, "async_persistence", None)
    if not persistence:
        return None
    return container, persistence


def _resolve_player_id(player: Any) -> uuid.UUID | None:
    """Extract player_id from player object as UUID, or None."""
    raw = getattr(player, "player_id", None) or getattr(player, "id", None)
    if not raw:
        return None
    try:
        return uuid.UUID(str(raw)) if not isinstance(raw, uuid.UUID) else raw
    except (TypeError, ValueError):
        return None


def _format_quest_log(entries: list[dict[str, Any]]) -> str:
    """Format quest log entries as text for the player."""
    if not entries:
        return "You have no active or completed quests."
    lines = ["Quest log", "---"]
    for e in entries:
        state = e.get("state", "?")
        title = e.get("title") or e.get("name") or "Unknown"
        lines.append(f"  [{state.upper()}] {title}")
        desc = (e.get("description") or "").strip()
        if desc:
            lines.append(f"      {desc}")
        goals = e.get("goals_with_progress") or []
        for g in goals:
            current = g.get("current", 0)
            required = g.get("required", 1)
            done = g.get("done", False)
            target = g.get("target") or "?"
            if done:
                lines.append(f"      - {target}: done")
            else:
                lines.append(f"      - {target}: {current}/{required}")
    lines.append("---")
    return "\n".join(lines)


async def handle_journal_command(
    _command_data: dict[str, Any],
    current_user: dict[str, Any],
    request: Any,
    _alias_storage: AliasStorage | None,
    player_name: str,
) -> dict[str, str]:
    """
    Handle journal and quests commands: return formatted quest log for the active character.

    Resolves player by name from command context, fetches quest log from QuestService,
    and returns formatted text.
    """
    logger.debug("Processing journal/quests command", player=player_name)

    services = _get_container_and_persistence(request)
    if not services:
        return {"result": "Quest log is not available."}
    _container, persistence = services
    quest_service = _get_quest_service(request)
    if not quest_service:
        return {"result": "Quest log is not available."}

    try:
        player = await persistence.get_player_by_name(get_username_from_user(current_user))
        if not player:
            return {"result": "Character not found."}
        player_id = _resolve_player_id(player)
        if not player_id:
            return {"result": "Character id is invalid."}

        entries = await quest_service.get_quest_log(player_id, include_completed=True)
        return {"result": _format_quest_log(entries)}
    except Exception as e:  # pylint: disable=broad-exception-caught  # Reason: Command must return user message, not crash; log and return generic message
        logger.exception("Journal/quests command failed", player=player_name, error=str(e))
        return {"result": "Failed to load quest log."}


async def handle_quest_command(
    command_data: dict[str, Any],
    current_user: dict[str, Any],
    request: Any,
    _alias_storage: AliasStorage | None,
    player_name: str,
) -> dict[str, str]:
    """
    Handle quest command: subcommand "abandon <quest_name>" abandons an active quest by name.

    Usage: quest abandon <quest common name>
    """
    args: list[Any] = command_data.get("args", []) or []
    if not args or (args[0] if isinstance(args[0], str) else "").lower() != "abandon":
        return {"result": "Usage: quest abandon <quest name>. Use 'journal' or 'quests' to see your quest log."}

    quest_name_parts = args[1:] if len(args) > 1 else []
    quest_name = " ".join(str(p) for p in quest_name_parts).strip()
    if not quest_name:
        return {"result": "Usage: quest abandon <quest name>."}

    services = _get_container_and_persistence(request)
    if not services:
        return {"result": "Quest system is not available."}
    _container, persistence = services
    quest_service = _get_quest_service(request)
    if not quest_service:
        return {"result": "Quest system is not available."}

    try:
        player = await persistence.get_player_by_name(get_username_from_user(current_user))
        if not player:
            return {"result": "Character not found."}
        player_id = _resolve_player_id(player)
        if not player_id:
            return {"result": "Character id is invalid."}

        result = await quest_service.abandon(player_id, quest_name)
        if result.get("success"):
            return {"result": result.get("message", "Quest abandoned.")}
        return {"result": result.get("message", "Could not abandon quest.")}
    except Exception as e:  # pylint: disable=broad-exception-caught  # Reason: Command must return user message, not crash; log and return generic message
        logger.exception("Quest abandon command failed", player=player_name, error=str(e))
        return {"result": "Failed to abandon quest."}
