"""talk / talk <n> command for NPC dialogue trees (#583)."""

from __future__ import annotations

import uuid
from collections.abc import Mapping
from typing import cast

from ..alias_storage import AliasStorage
from ..game.chat_npc_system import schedule_personal_system
from ..game.dialogue import DialoguePrompt, format_dialogue_prompt, get_dialogue_service
from ..structured_logging.enhanced_logging_config import get_logger
from ..utils.command_parser import get_username_from_user
from .communication_commands_support import app_from_request, get_pose_persistence, primary_id
from .quest_commands import npc_definition_id, resolve_npc_in_player_room

logger = get_logger(__name__)

_TALK_USAGE = "Usage: talk <npc> | talk <number>"


def _resolve_player_id(player: object) -> uuid.UUID | None:
    """Extract player UUID from player model."""
    raw = primary_id(player)
    if raw is None:
        return None
    if isinstance(raw, uuid.UUID):
        return raw
    try:
        return uuid.UUID(str(raw))
    except (ValueError, TypeError):
        return None


def _remainder_from_command_data(command_data: Mapping[str, object]) -> str:
    """Join talk args into a single remainder string."""
    args = command_data.get("args", [])
    if isinstance(args, list):
        return " ".join(str(a) for a in cast(list[object], args)).strip()
    if isinstance(args, str):
        return args.strip()
    return ""


def _emit_prompt(player_id: uuid.UUID, npc_name: str, prompt: DialoguePrompt) -> str:
    """Send personal system message for a node; return short command result."""
    if prompt.ended:
        schedule_personal_system(player_id, prompt.text)
        return prompt.text
    body = format_dialogue_prompt(npc_name, prompt.text, prompt.options)
    schedule_personal_system(player_id, body)
    return body


async def _talk_by_option_index(player_id: uuid.UUID, option_index: int) -> dict[str, str]:
    """Advance an active dialogue by numbered option."""
    service = get_dialogue_service()
    result = await service.choose_option(player_id, option_index)
    if isinstance(result, str):
        return {"result": result}
    cursor = service.get_cursor(player_id)
    npc_name = cursor.npc_name if cursor else "Someone"
    if result.ended:
        service.clear_cursor(player_id)
    return {"result": _emit_prompt(player_id, npc_name, result)}


async def _talk_with_npc(player: object, player_id: uuid.UUID, npc_name_arg: str) -> dict[str, str]:
    """Start dialogue with a same-room NPC."""
    npc_raw, npc_error = resolve_npc_in_player_room(player, npc_name_arg)
    if npc_error:
        return {"result": npc_error}
    if npc_raw is None:
        return {"result": "That person has nothing to say."}
    npc: object = cast(object, npc_raw)
    definition_id_str = npc_definition_id(npc)
    if not definition_id_str:
        return {"result": "That person has nothing to say."}
    try:
        definition_id = int(definition_id_str)
    except (TypeError, ValueError):
        return {"result": "That person has nothing to say."}

    npc_id_raw = cast(object | None, getattr(npc, "npc_id", None))
    npc_name_raw = cast(object | None, getattr(npc, "name", None))
    npc_id = str(npc_id_raw or definition_id)
    npc_name = str(npc_name_raw or "Someone")
    result = await get_dialogue_service().start_with_npc(
        player_id,
        npc_id=npc_id,
        npc_name=npc_name,
        npc_definition_id=definition_id,
    )
    if isinstance(result, str):
        return {"result": result}
    return {"result": _emit_prompt(player_id, npc_name, result)}


async def handle_talk_command(
    command_data: Mapping[str, object],
    current_user: Mapping[str, object],
    request: object | None,
    _alias_storage: AliasStorage | None,
    player_name: str,
) -> dict[str, str]:
    """Handle talk <npc> or talk <n> against same-room NPCs."""
    logger.debug("Processing talk command", player=player_name, command_data=command_data)
    app = app_from_request(request)
    persistence = get_pose_persistence(app)
    if not persistence:
        return {"result": "You cannot talk right now."}

    remainder = _remainder_from_command_data(command_data)
    if not remainder:
        return {"result": _TALK_USAGE}

    try:
        player = await persistence.get_player_by_name(get_username_from_user(current_user))
    except Exception as e:  # pylint: disable=broad-exception-caught  # Reason: command must return user message
        logger.exception("Talk command failed loading player", player=player_name, error=str(e))
        return {"result": "You cannot talk right now."}
    if not player:
        return {"result": "Character not found."}
    player_id = _resolve_player_id(player)
    if not player_id:
        return {"result": "Character id is invalid."}

    if remainder.isdigit():
        return await _talk_by_option_index(player_id, int(remainder))
    return await _talk_with_npc(player, player_id, remainder)
