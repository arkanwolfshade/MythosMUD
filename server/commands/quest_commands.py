"""
Quest commands: journal / quests (quest log), quest abandon/ask/turnin.

Returns formatted quest log for journal/quests; abandons by name; asks NPC for
offered quests; turns in at NPC when goals are met.
"""

from __future__ import annotations

import uuid
from typing import Any

from ..alias_storage import AliasStorage
from ..game.quest import QuestService
from ..structured_logging.enhanced_logging_config import get_logger
from ..utils.command_parser import get_username_from_user
from .look_npc import _find_matching_npcs, _get_lifecycle_manager, _get_npc_room_id, _should_include_npc

logger = get_logger(__name__)

_QUEST_USAGE = (
    "Usage: quest abandon <quest name> | quest ask <npc> | quest turnin <npc>. "
    "Use 'journal' or 'quests' to see your quest log."
)


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


def _parse_quest_subcommand(command_data: dict[str, Any]) -> tuple[str | None, str | None, str | None]:
    """
    Parse quest subcommand args.

    Returns (subcommand, remainder, error_message).
    """
    args: list[Any] = command_data.get("args", []) or []
    if not args:
        return None, None, _QUEST_USAGE
    sub = str(args[0]).lower().strip()
    remainder = " ".join(str(p) for p in args[1:]).strip()
    if sub not in ("abandon", "ask", "turnin"):
        return None, None, _QUEST_USAGE
    if not remainder:
        if sub == "abandon":
            return None, None, "Usage: quest abandon <quest name>."
        return None, None, f"Usage: quest {sub} <npc>."
    return sub, remainder, None


async def _resolve_quest_command_context(
    request: Any, current_user: dict[str, Any]
) -> tuple[Any | None, uuid.UUID | None, QuestService | None, str | None]:
    """
    Resolve player, player_id and QuestService from request and current_user.
    Returns (player, player_id, quest_service, error_message).
    """
    services = _get_container_and_persistence(request)
    if not services:
        return None, None, None, "Quest system is not available."
    _container, persistence = services
    quest_service = _get_quest_service(request)
    if not quest_service:
        return None, None, None, "Quest system is not available."
    try:
        player = await persistence.get_player_by_name(get_username_from_user(current_user))
    except Exception:  # pylint: disable=broad-exception-caught  # Reason: Resolver must return message, not crash
        return None, None, None, "Failed to load character."
    if not player:
        return None, None, None, "Character not found."
    player_id = _resolve_player_id(player)
    if not player_id:
        return None, None, None, "Character id is invalid."
    return player, player_id, quest_service, None


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


def _npc_definition_id(npc: Any) -> str | None:
    """Return NPC definition id as string for quest offers/triggers."""
    definition = getattr(npc, "definition", None)
    if definition is None:
        return None
    raw = getattr(definition, "id", None)
    if raw is None:
        return None
    return str(raw)


def _active_npc_ids_in_room(lifecycle: Any, room_id: Any) -> list[Any]:
    """Return active, includable NPC ids currently in room_id."""
    return [
        npc_id
        for npc_id, npc_instance in (lifecycle.active_npcs or {}).items()
        if _get_npc_room_id(npc_instance) == room_id and _should_include_npc(npc_instance)
    ]


def _resolve_npc_in_player_room(player: Any, npc_name: str) -> tuple[Any | None, str | None]:
    """
    Find a single matching NPC in the player's current room.

    Returns (npc_instance, error_message).
    """
    room_id = getattr(player, "current_room_id", None)
    if not room_id:
        return None, "You are not in a room."
    lifecycle = _get_lifecycle_manager()
    if not lifecycle:
        return None, "No one here answers."
    matches = _find_matching_npcs(npc_name.lower().strip(), _active_npc_ids_in_room(lifecycle, room_id))
    if not matches:
        return None, f"You do not see '{npc_name}' here."
    if len(matches) > 1:
        names = ", ".join(getattr(n, "name", "?") for n in matches)
        return None, f"Which one? Matches: {names}"
    return matches[0], None


def _format_quest_action_results(results: list[dict[str, Any]], empty_message: str) -> str:
    """Format start/turn-in result dicts into player text."""
    if not results:
        return empty_message
    lines: list[str] = []
    for result in results:
        lines.append(str(result.get("message") or ("Done." if result.get("success") else "Failed.")))
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
    except Exception as e:  # pylint: disable=broad-exception-caught  # Reason: Command must return user message, not crash
        logger.exception("Journal/quests command failed", player=player_name, error=str(e))
        return {"result": "Failed to load quest log."}


async def _handle_quest_abandon(quest_service: Any, player_id: uuid.UUID, remainder: str) -> dict[str, str]:
    """Run quest abandon subcommand."""
    result = await quest_service.abandon(player_id, remainder)
    if result.get("success"):
        return {"result": result.get("message", "Quest abandoned.")}
    return {"result": result.get("message", "Could not abandon quest.")}


async def _handle_quest_npc_sub(
    quest_service: Any,
    player: Any,
    player_id: uuid.UUID,
    sub: str,
    remainder: str,
) -> dict[str, str]:
    """Run quest ask or turnin against an NPC in the player's room."""
    npc, npc_error = _resolve_npc_in_player_room(player, remainder)
    if npc_error:
        return {"result": npc_error}
    definition_id = _npc_definition_id(npc)
    if not definition_id:
        return {"result": "That person has nothing to discuss."}

    if sub == "ask":
        results = await quest_service.start_quest_by_trigger(player_id, "npc", definition_id)
        empty = f"{getattr(npc, 'name', 'They')} have no quests for you."
        return {"result": _format_quest_action_results(results, empty)}

    results = await quest_service.turn_in_at_entity(player_id, "npc", definition_id)
    empty = f"You have nothing to turn in to {getattr(npc, 'name', 'them')}."
    return {"result": _format_quest_action_results(results, empty)}


async def _quest_command_ready(
    request: Any, current_user: dict[str, Any]
) -> tuple[Any, uuid.UUID, Any] | dict[str, str]:
    """Resolve quest command context or return an error response dict."""
    player, player_id, quest_service, ctx_error = await _resolve_quest_command_context(request, current_user)
    if ctx_error:
        return {"result": ctx_error}
    if not quest_service or not player_id or player is None:
        return {"result": "Quest system error. Please try again."}
    return player, player_id, quest_service


async def handle_quest_command(
    command_data: dict[str, Any],
    current_user: dict[str, Any],
    request: Any,
    _alias_storage: AliasStorage | None,
    _player_name: str,
) -> dict[str, str]:
    """
    Handle quest command subcommands: abandon, ask, turnin.

    Usage:
      quest abandon <quest common name>
      quest ask <npc>
      quest turnin <npc>
    """
    sub, remainder, parse_error = _parse_quest_subcommand(command_data)
    if parse_error or not sub or remainder is None:
        return {"result": parse_error or _QUEST_USAGE}

    ready = await _quest_command_ready(request, current_user)
    if isinstance(ready, dict):
        return ready
    player, player_id, quest_service = ready

    try:
        if sub == "abandon":
            return await _handle_quest_abandon(quest_service, player_id, remainder)
        return await _handle_quest_npc_sub(quest_service, player, player_id, sub, remainder)
    except Exception as e:  # pylint: disable=broad-exception-caught  # Reason: Command must return user message, not crash
        logger.exception("Quest command failed", player_id=str(player_id), subcommand=sub, error=str(e))
        return {"result": "Failed to process quest command."}
