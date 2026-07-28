"""Quest lifecycle and NPC quest-line chat helpers (issue #146 MVP).

# group: quest chat notify helpers
# ponytail: every-tick progress for debug; milestones in follow-up #583
"""

from __future__ import annotations

import uuid
from typing import Any

from server.game.chat_npc_system import schedule_npc_room_speech, schedule_personal_system


def notify_quest_started(player_id: uuid.UUID | str, title: str) -> None:
    """Personal system chat when a quest becomes active."""
    schedule_personal_system(player_id, f"Quest started: {title}")


def notify_quest_progress(player_id: uuid.UUID | str, title: str) -> None:
    """Personal system chat on every progress tick (debug volume)."""
    schedule_personal_system(player_id, f"Quest progress: {title}")


def notify_quest_completed(player_id: uuid.UUID | str, title: str) -> None:
    """Personal system chat when a quest completes."""
    schedule_personal_system(player_id, f"Quest completed: {title}")


def notify_quest_abandoned(player_id: uuid.UUID | str, title: str) -> None:
    """Personal system chat when a quest is abandoned."""
    schedule_personal_system(player_id, f"Quest abandoned: {title}")


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
