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


def _parse_quest_abandon_args(command_data: dict[str, Any]) -> tuple[str | None, str | None]:
    """
    Parse 'quest abandon <name>' from command_data.
    Returns (quest_name, error_message). If error_message is not None, quest_name is None.
    """
    args: list[Any] = command_data.get("args", []) or []
    first = (args[0] if isinstance(args[0], str) else "") if args else ""
    if not args or first.lower() != "abandon":
        return None, "Usage: quest abandon <quest name>. Use 'journal' or 'quests' to see your quest log."
    quest_name = " ".join(str(p) for p in args[1:]).strip()
    if not quest_name:
        return None, "Usage: quest abandon <quest name>."
    return quest_name, None


async def _resolve_quest_command_context(
    request: Any, current_user: dict[str, Any]
) -> tuple[uuid.UUID | None, QuestService | None, str | None]:
    """
    Resolve player_id and QuestService from request and current_user.
    Returns (player_id, quest_service, error_message). If error_message is not None, use it.
    """
    services = _get_container_and_persistence(request)
    if not services:
        return None, None, "Quest system is not available."
    _container, persistence = services
    quest_service = _get_quest_service(request)
    if not quest_service:
        return None, None, "Quest system is not available."
    try:
        player = await persistence.get_player_by_name(get_username_from_user(current_user))
    except Exception:  # pylint: disable=broad-exception-caught  # Reason: Resolver must return message, not crash; caller returns "Failed to load character"
        return None, None, "Failed to load character."
    if not player:
        return None, None, "Character not found."
    player_id = _resolve_player_id(player)
    if not player_id:
        return None, None, "Character id is invalid."
    return player_id, quest_service, None


def _format_goal_line(goal: dict[str, Any]) -> str:
    """Return a single goal progress line for the quest log."""
    target = goal.get("target") or "?"
    if goal.get("done", False):
        return f"      - {target}: done"
    return f"      - {target}: {goal.get('current', 0)}/{goal.get('required', 1)}"


def _format_one_quest_entry(e: dict[str, Any]) -> list[str]:
    """Return lines for a single quest log entry."""
    state = e.get("state", "?")
    title = e.get("title") or e.get("name") or "Unknown"
    lines = [f"  [{state.upper()}] {title}"]
    desc = (e.get("description") or "").strip()
    if desc:
        lines.append(f"      {desc}")
    for g in e.get("goals_with_progress") or []:
        lines.append(_format_goal_line(g))
    return lines


def _format_quest_log(entries: list[dict[str, Any]]) -> str:
    """Format quest log entries as text for the player."""
    if not entries:
        return "You have no active or completed quests."
    lines = ["Quest log", "---"]
    for e in entries:
        lines.extend(_format_one_quest_entry(e))
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
    _player_name: str,
) -> dict[str, str]:
    """
    Handle quest command: subcommand "abandon <quest_name>" abandons an active quest by name.

    Usage: quest abandon <quest common name>
    """
    quest_name, parse_error = _parse_quest_abandon_args(command_data)
    if parse_error:
        return {"result": parse_error}
    player_id, quest_service, ctx_error = await _resolve_quest_command_context(request, current_user)
    if ctx_error:
        return {"result": ctx_error}
    # Explicit checks: when ctx_error is None the resolver should return non-None ids/service;
    # avoid assert so validation is not stripped under python -O (Codacy B101).
    if not quest_service or not player_id or quest_name is None:
        return {"result": "Quest system error. Please try again."}
    try:
        result = await quest_service.abandon(player_id, quest_name)
        if result.get("success"):
            return {"result": result.get("message", "Quest abandoned.")}
        return {"result": result.get("message", "Could not abandon quest.")}
    except Exception as e:  # pylint: disable=broad-exception-caught  # Reason: Command must return user message, not crash; log and return generic message
        logger.exception("Quest abandon command failed", player_id=str(player_id), quest_name=quest_name, error=str(e))
        return {"result": "Failed to abandon quest."}
