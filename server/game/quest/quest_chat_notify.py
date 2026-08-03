"""Quest lifecycle and NPC quest-line chat helpers (issue #146 MVP).

# group: quest chat notify helpers
# Milestone progress (#583): notify on first progress change or newly met goal;
# completing tick uses only notify_quest_completed (no duplicate progress line).
"""

from __future__ import annotations

import uuid
from typing import Any

from server.game.chat_npc_system import schedule_npc_room_speech, schedule_personal_system


def notify_quest_started(player_id: uuid.UUID | str, title: str) -> None:
    """Personal system chat when a quest becomes active."""
    schedule_personal_system(player_id, f"Quest started: {title}")


def notify_quest_progress(player_id: uuid.UUID | str, title: str) -> None:
    """Personal system chat for milestone progress (first tick or goal newly met)."""
    schedule_personal_system(player_id, f"Quest progress: {title}")


def notify_quest_completed(player_id: uuid.UUID | str, title: str) -> None:
    """Personal system chat when a quest completes."""
    schedule_personal_system(player_id, f"Quest completed: {title}")


def notify_quest_abandoned(player_id: uuid.UUID | str, title: str) -> None:
    """Personal system chat when a quest is abandoned."""
    schedule_personal_system(player_id, f"Quest abandoned: {title}")


def _as_int(value: object, default: int = 0) -> int:
    """Coerce progress/config scalars to int; non-numeric becomes default."""
    return int(value) if isinstance(value, int | float) else default


def _goal_is_met(progress: dict[str, Any], goal_index: int, goal: Any) -> bool:
    """Return True if one goal is satisfied given current progress."""
    current_val = _as_int(progress.get(str(goal_index), 0))
    goal_type = getattr(goal, "type", None) or (goal.get("type") if isinstance(goal, dict) else None)
    raw_config = getattr(goal, "config", None) or (goal.get("config") if isinstance(goal, dict) else None)
    config: dict[str, Any] = raw_config if isinstance(raw_config, dict) else {}
    if goal_type == "complete_activity":
        return current_val == 1
    if goal_type in ("kill_n", "collect_n"):
        return current_val >= _as_int(config.get("count", 1), 1)
    return False


def _progress_has_any_value(progress: dict[str, Any], goal_count: int) -> bool:
    """True if any goal slot has a non-zero / non-empty progress value."""
    for i in range(goal_count):
        value = progress.get(str(i), 0)
        if value:
            return True
    return False


def should_notify_quest_progress(
    old_progress: dict[str, Any],
    new_progress: dict[str, Any],
    definition: Any,
    *,
    will_complete: bool = False,
) -> bool:
    """
    Return True when a progress personal-system line should be sent.

    Notifies on first progress change on the instance, or when any goal newly
    becomes met. Suppresses when progress is unchanged or the tick completes
    the quest (caller should send notify_quest_completed only).
    """
    if will_complete:
        return False
    if old_progress == new_progress:
        return False
    goals = getattr(definition, "goals", None) or []
    goal_count = len(goals)
    if not _progress_has_any_value(old_progress, goal_count):
        return True
    for i, goal in enumerate(goals):
        if not _goal_is_met(old_progress, i, goal) and _goal_is_met(new_progress, i, goal):
            return True
    return False


def emit_quest_npc_say(
    *,
    npc_id: str,
    npc_name: str,
    room_id: str,
    line: str,
) -> None:
    """Room say-shaped NPC line for quest ask/turnin."""
    schedule_npc_room_speech(npc_id=npc_id, npc_name=npc_name, room_id=room_id, message=line)


def quest_ask_npc_line(title: str) -> str:
    """Template NPC speech when offering/starting a quest."""
    return f"I have a task for you: {title}."


def quest_turnin_npc_line(title: str) -> str:
    """Template NPC speech when accepting a turn-in."""
    return f"You have completed: {title}. Well done."


def title_from_quest_result(result: dict[str, Any], *, prefix: str) -> str | None:
    """Extract quest title from a QuestService result message, if successful."""
    if not result.get("success"):
        return None
    if isinstance(result.get("title"), str) and result["title"]:
        return str(result["title"])
    message = str(result.get("message") or "")
    if message.startswith(prefix):
        return message[len(prefix) :].strip() or None
    return None
