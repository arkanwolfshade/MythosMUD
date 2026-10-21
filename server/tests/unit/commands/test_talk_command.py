"""Unit tests for talk command helpers."""

# pyright: reportPrivateUsage=false

import uuid
from collections.abc import Sequence
from dataclasses import dataclass, field
from typing import cast
from unittest.mock import ANY, AsyncMock, MagicMock, patch

import pytest

from server.commands import talk_command as cmd
from server.exceptions import DatabaseError
from server.game.dialogue.dialogue_service import (
    DialogueCursor,
    DialoguePrompt,
    format_dialogue_options,
    format_dialogue_prompt,
)
from server.game.scripted_actions import ScriptedActionContext
from server.models.player import Player
from server.schemas.scripted_actions import NarrateAction, ScriptedAction
from server.services.corruption_service import CorruptionPersistenceProtocol


def test_resolve_player_id_uuid() -> None:
    pid = uuid.uuid4()
    player = MagicMock(player_id=pid)
    with patch("server.commands.talk_command.primary_id", return_value=pid):
        assert cmd._resolve_player_id(player) == pid


def test_resolve_player_id_invalid() -> None:
    with patch("server.commands.talk_command.primary_id", return_value="not-a-uuid"):
        assert cmd._resolve_player_id(MagicMock()) is None


def test_remainder_from_command_data_list() -> None:
    assert cmd._remainder_from_command_data({"args": ["npc", "name"]}) == "npc name"


def test_remainder_from_command_data_string() -> None:
    assert cmd._remainder_from_command_data({"args": "  hello  "}) == "hello"


@pytest.mark.asyncio
async def test_emit_prompt_ended() -> None:
    player_id = uuid.uuid4()
    prompt = DialoguePrompt(text="Goodbye.", options=[], ended=True)
    with patch("server.commands.talk_command.deliver_personal_system", new_callable=AsyncMock) as sent:
        result = await cmd._emit_prompt(player_id, "NPC", prompt)
    assert result == "Goodbye."
    sent.assert_awaited_once_with(player_id, "Goodbye.")


@pytest.mark.asyncio
async def test_emit_prompt_with_options() -> None:
    player_id = uuid.uuid4()
    prompt = DialoguePrompt(text="Hello?", options=["Yes", "No"], ended=False)
    with patch("server.commands.talk_command.deliver_personal_system", new_callable=AsyncMock) as sent:
        with patch("server.commands.talk_command.format_dialogue_prompt", return_value="formatted"):
            result = await cmd._emit_prompt(player_id, "NPC", prompt)
    assert result == "formatted"
    sent.assert_awaited_once_with(player_id, "formatted")


@pytest.mark.asyncio
async def test_talk_by_option_index_error_string() -> None:
    player_id = uuid.uuid4()
    service = MagicMock()
    service.choose_option = AsyncMock(return_value="Invalid option.")
    service.get_cursor.return_value = None
    with patch("server.commands.talk_command.get_dialogue_service", return_value=service):
        result = await cmd._talk_by_option_index(player_id, 1)
    assert result["result"] == "Invalid option."


@pytest.mark.asyncio
async def test_handle_talk_command_no_persistence() -> None:
    request = MagicMock()
    with patch("server.commands.talk_command.app_from_request", return_value=MagicMock()):
        with patch("server.commands.talk_command.get_pose_persistence", return_value=None):
            result = await cmd.handle_talk_command({"args": ["npc"]}, {}, request, None, "Player")
    assert "cannot talk" in result["result"]


@pytest.mark.asyncio
async def test_handle_talk_command_usage() -> None:
    request = MagicMock()
    with patch("server.commands.talk_command.app_from_request", return_value=MagicMock()):
        with patch("server.commands.talk_command.get_pose_persistence", return_value=MagicMock()):
            with patch("server.commands.talk_command.get_username_from_user", return_value="Alice"):
                persistence = MagicMock()
                persistence.get_player_by_name = AsyncMock(return_value=MagicMock(player_id=uuid.uuid4()))
                with patch("server.commands.talk_command.get_pose_persistence", return_value=persistence):
                    result = await cmd.handle_talk_command({"args": []}, {}, request, None, "Alice")
    assert "Usage" in result["result"]


# --- scripted actions ---------------------------------------------------------------------------------------------


class FakeDialogue:
    """Stands in for DialogueService: always presents the same prompt."""

    prompt: DialoguePrompt
    cursor: DialogueCursor | None

    def __init__(self, prompt: DialoguePrompt, cursor: DialogueCursor | None = None) -> None:
        self.prompt = prompt
        self.cursor = cursor

    async def start_with_npc(
        self, player_id: uuid.UUID, *, npc_id: str, npc_name: str, npc_definition_id: int
    ) -> DialoguePrompt:
        _ = player_id, npc_id, npc_name, npc_definition_id
        return self.prompt

    async def choose_option(self, player_id: uuid.UUID, option_index: int) -> DialoguePrompt:
        _ = player_id, option_index
        return self.prompt

    def get_cursor(self, player_id: uuid.UUID) -> DialogueCursor | None:
        _ = player_id
        return self.cursor

    def clear_cursor(self, player_id: uuid.UUID) -> None:
        _ = player_id


@dataclass
class ActionRig:
    """Records the order of the line and the actions, and what the runner was handed."""

    order: list[str] = field(default_factory=lambda: cast(list[str], []))
    ran: list[list[ScriptedAction]] = field(default_factory=lambda: cast(list[list[ScriptedAction]], []))
    ctx: ScriptedActionContext = field(
        default_factory=lambda: ScriptedActionContext(
            player=Player(player_id=str(uuid.uuid4()), name="Ctx"),
            persistence=cast(CorruptionPersistenceProtocol, object()),
        )
    )


@pytest.fixture(name="rig")
def _rig(monkeypatch: pytest.MonkeyPatch) -> ActionRig:
    rig = ActionRig()

    async def fake_emit(player_id: uuid.UUID, npc_name: str, prompt: DialoguePrompt, **where: object) -> str:
        _ = player_id, npc_name, prompt, where
        rig.order.append("line")
        return "text"

    async def fake_run(actions: Sequence[ScriptedAction], ctx: ScriptedActionContext) -> None:
        assert ctx is rig.ctx
        rig.order.append("actions")
        rig.ran.append(list(actions))

    def fake_context(app: object | None, player: object, persistence: object | None) -> ScriptedActionContext:
        _ = app, player, persistence
        return rig.ctx

    monkeypatch.setattr(cmd, "_emit_prompt", fake_emit)
    monkeypatch.setattr(cmd, "run_scripted_actions", fake_run)
    monkeypatch.setattr(cmd, "action_context", fake_context)

    def fake_persistence(app: object | None) -> object:
        _ = app
        return object()

    monkeypatch.setattr(cmd, "get_pose_persistence", fake_persistence)
    return rig


def _action_prompt() -> DialoguePrompt:
    return DialoguePrompt(
        text="Hold still.", options=["Thanks"], ended=False, actions=[NarrateAction(text="Warmth spreads.")]
    )


@pytest.mark.asyncio
async def test_talk_with_npc_runs_the_start_node_actions_after_the_line(rig: ActionRig) -> None:
    player_id = uuid.uuid4()
    player = Player(player_id=str(player_id), name="Tester")
    prompt = _action_prompt()
    with (
        patch("server.commands.talk_command.resolve_npc_in_player_room", return_value=(MagicMock(npc_id="n"), None)),
        patch("server.commands.talk_command.npc_definition_id", return_value="42"),
        patch("server.commands.talk_command.get_dialogue_service", return_value=FakeDialogue(prompt)),
    ):
        _ = await cmd._talk_with_npc(player, player_id, "Ghoul", app=object())

    assert rig.ran == [prompt.actions]
    assert rig.order == ["line", "actions"]


@pytest.mark.asyncio
async def test_talk_by_option_index_runs_the_chosen_node_actions(rig: ActionRig) -> None:
    player_id = uuid.uuid4()
    player = Player(player_id=str(player_id), name="Tester")
    prompt = _action_prompt()
    with patch("server.commands.talk_command.get_dialogue_service", return_value=FakeDialogue(prompt)):
        _ = await cmd._talk_by_option_index(player_id, 1, player=player, app=object())

    assert rig.ran == [prompt.actions]
    assert rig.order == ["line", "actions"]


@pytest.mark.asyncio
async def test_talk_does_not_run_actions_when_there_are_none(rig: ActionRig) -> None:
    prompt = DialoguePrompt(text="Hello.", options=[], ended=False)
    with patch("server.commands.talk_command.get_dialogue_service", return_value=FakeDialogue(prompt)):
        _ = await cmd._talk_by_option_index(
            uuid.uuid4(), 1, player=Player(player_id=str(uuid.uuid4()), name="T"), app=object()
        )

    assert rig.ran == []


@pytest.mark.asyncio
async def test_talk_with_npc_success() -> None:
    player_id = uuid.uuid4()
    player = MagicMock()
    npc = MagicMock(npc_id="npc-1", name="Librarian")
    prompt = DialoguePrompt(text="Welcome.", options=["Ask"], ended=False)
    service = MagicMock()
    service.start_with_npc = AsyncMock(return_value=prompt)
    with patch("server.commands.talk_command.resolve_npc_in_player_room", return_value=(npc, None)):
        with patch("server.commands.talk_command.npc_definition_id", return_value="42"):
            with patch("server.commands.talk_command.get_dialogue_service", return_value=service):
                with patch("server.commands.talk_command._emit_prompt", return_value="formatted"):
                    result = await cmd._talk_with_npc(player, player_id, "Librarian")
    assert result["result"] == "formatted"


# --- reply <n> answers a conversation (#1105) -------------------------------------------------------------------


def _conversation(*, active: bool) -> MagicMock:
    """A dialogue service that does (or does not) have a conversation open for the player."""
    service: MagicMock = MagicMock()
    service.get_cursor = MagicMock(return_value=object() if active else None)
    return service


async def _reply(
    message: object, *, active: bool = True, lookup: AsyncMock | None = None
) -> tuple[dict[str, str] | None, AsyncMock, AsyncMock]:
    """Run reply_to_dialogue; returns (result, the talk-option stand-in, the player lookup)."""
    player_id = uuid.uuid4()
    find_player: AsyncMock = lookup if lookup is not None else AsyncMock(return_value=MagicMock(player_id=player_id))
    persistence: MagicMock = MagicMock()
    persistence.get_player_by_name = find_player
    option: AsyncMock = AsyncMock(return_value={"result": "Strays, the constable says."})
    with (
        patch("server.commands.talk_command.app_from_request", return_value=MagicMock()),
        patch("server.commands.talk_command.get_pose_persistence", return_value=persistence),
        patch("server.commands.talk_command.primary_id", return_value=player_id),
        patch("server.commands.talk_command.get_dialogue_service", return_value=_conversation(active=active)),
        patch("server.commands.talk_command._talk_by_option_index", option),
    ):
        result = await cmd.reply_to_dialogue({"message": message}, MagicMock(), "Alice")
    return result, option, find_player


@pytest.mark.asyncio
async def test_reply_with_a_number_in_a_conversation_picks_that_answer() -> None:
    result, option, _ = await _reply("2")

    assert result == {"result": "Strays, the constable says."}
    option.assert_awaited_once()
    assert option.await_args is not None
    assert option.await_args.args[1] == 2


@pytest.mark.asyncio
async def test_reply_ignores_the_spaces_around_the_number() -> None:
    _, option, _ = await _reply("  3 ")

    assert option.await_args is not None
    assert option.await_args.args[1] == 3


@pytest.mark.asyncio
async def test_reply_with_a_number_outside_a_conversation_is_left_for_the_whisper_reply() -> None:
    result, option, _ = await _reply("2", active=False)

    assert result is None
    option.assert_not_awaited()


@pytest.mark.asyncio
@pytest.mark.parametrize("message", ["The seal is cracked.", "2 or 3", "", "   ", None, 2])
async def test_reply_that_is_not_a_bare_number_is_left_for_the_whisper_reply(message: object) -> None:
    result, option, find_player = await _reply(message)

    assert result is None
    option.assert_not_awaited()
    find_player.assert_not_awaited()  # no database work for ordinary whispers


@pytest.mark.asyncio
async def test_reply_without_persistence_or_when_it_fails_is_left_for_the_whisper_reply() -> None:
    request = MagicMock()
    with (
        patch("server.commands.talk_command.app_from_request", return_value=MagicMock()),
        patch("server.commands.talk_command.get_pose_persistence", return_value=None),
    ):
        assert await cmd.reply_to_dialogue({"message": "1"}, request, "Alice") is None

    failing: AsyncMock = AsyncMock(side_effect=DatabaseError("db down"))
    result, option, _ = await _reply("1", lookup=failing)

    assert result is None
    option.assert_not_awaited()


# --- the NPC's line is NPC speech, private to the player (#1107) -----------------------------------------------


def test_room_of_reads_the_players_room_and_ignores_a_missing_one() -> None:
    assert cmd._room_of(MagicMock(current_room_id="room-1")) == "room-1"
    assert cmd._room_of(MagicMock(current_room_id=None)) is None
    assert cmd._room_of(None) is None


@pytest.mark.asyncio
async def test_emit_prompt_speaks_the_line_as_the_npc_when_it_knows_who_and_where() -> None:
    player_id = uuid.uuid4()
    prompt = DialoguePrompt(text="Sit.", options=["Yes"], ended=False)
    with (
        patch.object(cmd, "_send_prompt", new_callable=AsyncMock) as send,
        patch.object(cmd, "deliver_personal_system", new_callable=AsyncMock) as system,
    ):
        result = await cmd._emit_prompt(player_id, "Ghoul", prompt, npc_id="npc-1", room_id="room-1")

    send.assert_awaited_once_with(player_id, "npc-1", "Ghoul", "room-1", prompt)
    system.assert_not_awaited()
    assert "Sit." in result


@pytest.mark.asyncio
async def test_emit_prompt_falls_back_to_a_system_prompt_without_an_npc_or_room() -> None:
    player_id = uuid.uuid4()
    prompt = DialoguePrompt(text="Sit.", options=["Yes"], ended=False)
    with (
        patch.object(cmd, "_send_prompt", new_callable=AsyncMock) as send,
        patch.object(cmd, "deliver_personal_system", new_callable=AsyncMock) as system,
    ):
        _ = await cmd._emit_prompt(player_id, "Ghoul", prompt, npc_id="npc-1", room_id=None)

    send.assert_not_awaited()
    system.assert_awaited_once_with(player_id, format_dialogue_prompt("Ghoul", "Sit.", ["Yes"]))


@pytest.mark.asyncio
async def test_send_prompt_speaks_privately_then_sends_the_options() -> None:
    player_id = uuid.uuid4()
    prompt = DialoguePrompt(text="Sit.", options=["Yes", "No"], ended=False)
    with (
        patch.object(cmd, "deliver_npc_room_speech", new_callable=AsyncMock, return_value={"success": True}) as speech,
        patch.object(cmd, "deliver_personal_system", new_callable=AsyncMock) as system,
    ):
        await cmd._send_prompt(player_id, "npc-1", "Ghoul", "room-1", prompt)

    speech.assert_awaited_once_with(
        npc_id="npc-1", room_id="room-1", message="Sit.", npc_name="Ghoul", target_player_id=player_id
    )
    system.assert_awaited_once_with(player_id, format_dialogue_options(["Yes", "No"]))


@pytest.mark.asyncio
async def test_send_prompt_sends_no_options_block_for_a_node_without_options() -> None:
    prompt = DialoguePrompt(text="Hm.", options=[], ended=False)
    with (
        patch.object(cmd, "deliver_npc_room_speech", new_callable=AsyncMock, return_value={"success": True}),
        patch.object(cmd, "deliver_personal_system", new_callable=AsyncMock) as system,
    ):
        await cmd._send_prompt(uuid.uuid4(), "npc-1", "Ghoul", "room-1", prompt)

    system.assert_not_awaited()


@pytest.mark.asyncio
async def test_send_prompt_falls_back_to_the_whole_node_as_a_system_prompt_when_speech_fails() -> None:
    """A line that cannot be spoken must not vanish and strand the player mid-conversation."""
    player_id = uuid.uuid4()
    prompt = DialoguePrompt(text="Sit.", options=["Yes"], ended=False)
    with (
        patch.object(cmd, "deliver_npc_room_speech", new_callable=AsyncMock, return_value={"success": False}),
        patch.object(cmd, "deliver_personal_system", new_callable=AsyncMock) as system,
    ):
        await cmd._send_prompt(player_id, "npc-1", "Ghoul", "room-1", prompt)

    system.assert_awaited_once_with(player_id, format_dialogue_prompt("Ghoul", "Sit.", ["Yes"]))


# --- the callers hand _emit_prompt the NPC and the room (without them the line silently reverts to a system prompt) ---


def _cursor() -> DialogueCursor:
    return DialogueCursor(npc_id="npc-1", npc_name="Ghoul", npc_definition_id=7, node_id="n", dialogue_id="d")


@pytest.mark.asyncio
async def test_talk_by_option_index_speaks_as_the_cursors_npc_in_the_players_room(rig: ActionRig) -> None:
    _ = rig
    player_id = uuid.uuid4()
    player = Player(player_id=str(player_id), name="Tester", current_room_id="room-1")
    prompt = DialoguePrompt(text="Hm.", options=[], ended=False)
    with (
        patch("server.commands.talk_command.get_dialogue_service", return_value=FakeDialogue(prompt, _cursor())),
        patch.object(cmd, "_emit_prompt", new_callable=AsyncMock, return_value="text") as emit,
    ):
        _ = await cmd._talk_by_option_index(player_id, 1, player=player, app=object())

    emit.assert_awaited_once_with(player_id, "Ghoul", prompt, npc_id="npc-1", room_id="room-1")


@pytest.mark.asyncio
async def test_open_dialogue_speaks_as_the_npc_in_the_given_room() -> None:
    player_id = uuid.uuid4()
    prompt = DialoguePrompt(text="Hi.", options=[], ended=False)
    with (
        patch("server.commands.talk_command.get_dialogue_service", return_value=FakeDialogue(prompt)),
        patch.object(cmd, "_emit_prompt", new_callable=AsyncMock, return_value="text") as emit,
    ):
        _ = await cmd.open_dialogue(
            player_id, npc_id="npc-1", npc_name="Ghoul", definition_id=7, room_id="room-1", ctx=None
        )

    emit.assert_awaited_once_with(player_id, "Ghoul", prompt, npc_id="npc-1", room_id="room-1")


@pytest.mark.asyncio
async def test_talk_with_npc_opens_the_dialogue_in_the_players_room(rig: ActionRig) -> None:
    player_id = uuid.uuid4()
    player = Player(player_id=str(player_id), name="Tester", current_room_id="room-1")
    with (
        patch("server.commands.talk_command.resolve_npc_in_player_room", return_value=(MagicMock(npc_id="n"), None)),
        patch("server.commands.talk_command.npc_definition_id", return_value="42"),
        patch.object(cmd, "open_dialogue", new_callable=AsyncMock, return_value="text") as opened,
    ):
        _ = await cmd._talk_with_npc(player, player_id, "Ghoul", app=object())

    opened.assert_awaited_once_with(
        player_id, npc_id="n", npc_name=ANY, definition_id=42, room_id="room-1", ctx=rig.ctx
    )
