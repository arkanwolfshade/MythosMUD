"""talk / talk <n> command for NPC dialogue trees (#583)."""

from __future__ import annotations

import uuid
from collections.abc import Mapping
from typing import cast

from ..alias_storage import AliasStorage
from ..exceptions import DatabaseError
from ..game.chat_npc_system import (
    deliver_npc_room_speech,
    deliver_personal_system,
    schedule_coro,
    schedule_personal_system,
)
from ..game.dialogue import (
    DialoguePrompt,
    format_dialogue_options,
    format_dialogue_prompt,
    get_dialogue_service,
)
from ..game.scripted_actions import ScriptedActionContext, run_scripted_actions
from ..structured_logging.enhanced_logging_config import get_logger
from ..utils.command_parser import get_username_from_user
from .command_results import command_error
from .communication_commands_support import app_from_request, get_pose_persistence, primary_id
from .quest_commands import npc_definition_id, resolve_npc_in_player_room
from .scripted_action_support import action_context

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
    except ValueError, TypeError:
        return None


def _remainder_from_command_data(command_data: Mapping[str, object]) -> str:
    """Join talk args into a single remainder string."""
    args = command_data.get("args", [])
    if isinstance(args, list):
        return " ".join(str(a) for a in cast(list[object], args)).strip()
    if isinstance(args, str):
        return args.strip()
    return ""


def _room_of(player: object | None) -> str | None:
    """The room the player stands in, if the model says."""
    room = cast(object | None, getattr(player, "current_room_id", None))
    return room if isinstance(room, str) and room else None


async def _send_prompt(player_id: uuid.UUID, npc_id: str, npc_name: str, room_id: str, prompt: DialoguePrompt) -> None:
    """The NPC's line as speech only this player hears, then the numbered options as a system prompt (#1107)."""
    spoke = await deliver_npc_room_speech(
        npc_id=npc_id, room_id=room_id, message=prompt.text, npc_name=npc_name, target_player_id=player_id
    )
    if spoke.get("success") is not True:
        # Without the speech channel the line would be lost; fall back to the plain system prompt.
        _ = await deliver_personal_system(player_id, format_dialogue_prompt(npc_name, prompt.text, prompt.options))
        return
    if prompt.options:
        _ = await deliver_personal_system(player_id, format_dialogue_options(prompt.options))


def _emit_prompt(
    player_id: uuid.UUID,
    npc_name: str,
    prompt: DialoguePrompt,
    *,
    npc_id: str | None = None,
    room_id: str | None = None,
) -> str:
    """Send a node to the player; return the short command result.

    The NPC's line is that NPC speaking, private to this player; the options stay a system prompt. Without the NPC and
    the room to speak in, the whole node is a system prompt.
    """
    if prompt.ended:
        schedule_personal_system(player_id, prompt.text)
        return prompt.text
    body = format_dialogue_prompt(npc_name, prompt.text, prompt.options)
    if npc_id and room_id:
        schedule_coro(_send_prompt(player_id, npc_id, npc_name, room_id, prompt))
    else:
        schedule_personal_system(player_id, body)
    return body


async def _run_prompt_actions(prompt: DialoguePrompt, ctx: ScriptedActionContext | None) -> None:
    """Run the presented node's scripted actions (after its line has been sent)."""
    if prompt.actions and ctx is not None:
        await run_scripted_actions(prompt.actions, ctx)


async def open_dialogue(
    player_id: uuid.UUID,
    *,
    npc_id: str,
    npc_name: str,
    definition_id: int,
    room_id: str | None,
    ctx: ScriptedActionContext | None,
) -> str:
    """
    Start the NPC's dialogue for a player: send its first line and run that node's actions.

    Shared by `talk <npc>` (the player speaks first) and NPCs that open the conversation themselves.
    Returns the text shown, or the reason there was nothing to say.
    """
    result = await get_dialogue_service().start_with_npc(
        player_id, npc_id=npc_id, npc_name=npc_name, npc_definition_id=definition_id
    )
    if isinstance(result, str):
        return result
    text = _emit_prompt(player_id, npc_name, result, npc_id=npc_id, room_id=room_id)
    await _run_prompt_actions(result, ctx)
    return text


async def _talk_by_option_index(
    player_id: uuid.UUID, option_index: int, *, player: object | None = None, app: object | None = None
) -> dict[str, str]:
    """Advance an active dialogue by numbered option."""
    service = get_dialogue_service()
    result = await service.choose_option(player_id, option_index)
    if isinstance(result, str):
        return {"result": result}
    cursor = service.get_cursor(player_id)
    npc_name = cursor.npc_name if cursor else "Someone"
    if result.ended:
        service.clear_cursor(player_id)
    text = _emit_prompt(player_id, npc_name, result, npc_id=cursor.npc_id if cursor else None, room_id=_room_of(player))
    ctx = action_context(app, player, get_pose_persistence(app)) if player is not None else None
    await _run_prompt_actions(result, ctx)
    return {"result": text}


async def reply_to_dialogue(
    command_data: Mapping[str, object], request: object | None, player_name: str
) -> dict[str, str] | None:
    """`reply <n>` during a conversation picks answer n, exactly like `talk <n>` (#1105).

    None when it is not that (no number, or the player is not in a conversation), so the caller falls through to
    the ordinary whisper reply.
    """
    message = command_data.get("message")
    if not isinstance(message, str) or not message.strip().isdigit():
        return None
    app = app_from_request(request)
    persistence = get_pose_persistence(app)
    if not persistence:
        return None
    try:
        player = await persistence.get_player_by_name(player_name)
    except DatabaseError as e:
        logger.debug("Reply could not load the player to check for a conversation", player=player_name, error=str(e))
        return None
    player_id = _resolve_player_id(player) if player else None
    if player_id is None or get_dialogue_service().get_cursor(player_id) is None:
        return None
    return await _talk_by_option_index(player_id, int(message.strip()), player=player, app=app)


async def _talk_with_npc(
    player: object, player_id: uuid.UUID, npc_name_arg: str, *, app: object | None = None
) -> dict[str, str]:
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
    except TypeError, ValueError:
        return {"result": "That person has nothing to say."}

    npc_id_raw = cast(object | None, getattr(npc, "npc_id", None))
    npc_name_raw = cast(object | None, getattr(npc, "name", None))
    npc_id = str(npc_id_raw or definition_id)
    npc_name = str(npc_name_raw or "Someone")
    ctx = action_context(app, player, get_pose_persistence(app))
    text = await open_dialogue(
        player_id,
        npc_id=npc_id,
        npc_name=npc_name,
        definition_id=definition_id,
        room_id=_room_of(player),
        ctx=ctx,
    )
    return {"result": text}


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
        return command_error(_TALK_USAGE)

    try:
        player = await persistence.get_player_by_name(get_username_from_user(current_user))
    except Exception as e:  # pylint: disable=broad-exception-caught  # Reason: command must return user message
        logger.exception("Talk command failed loading player", player=player_name, error=str(e))
        return {"result": "You cannot talk right now."}
    if not player:
        return command_error("Character not found.")
    player_id = _resolve_player_id(player)
    if not player_id:
        return command_error("Character id is invalid.")

    if remainder.isdigit():
        return await _talk_by_option_index(player_id, int(remainder), player=player, app=app)
    return await _talk_with_npc(player, player_id, remainder, app=app)
