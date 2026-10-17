"""Unit tests for talk command helpers."""

# pyright: reportPrivateUsage=false

import uuid
from collections.abc import Sequence
from dataclasses import dataclass, field
from typing import cast
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.commands import talk_command as cmd
from server.game.dialogue.dialogue_service import DialoguePrompt
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


def test_emit_prompt_ended() -> None:
    player_id = uuid.uuid4()
    prompt = DialoguePrompt(text="Goodbye.", options=[], ended=True)
    with patch("server.commands.talk_command.schedule_personal_system") as sched:
        result = cmd._emit_prompt(player_id, "NPC", prompt)
    assert result == "Goodbye."
    sched.assert_called_once()


def test_emit_prompt_with_options() -> None:
    player_id = uuid.uuid4()
    prompt = DialoguePrompt(text="Hello?", options=["Yes", "No"], ended=False)
    with patch("server.commands.talk_command.schedule_personal_system") as sched:
        with patch("server.commands.talk_command.format_dialogue_prompt", return_value="formatted"):
            result = cmd._emit_prompt(player_id, "NPC", prompt)
    assert result == "formatted"
    sched.assert_called_once()


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

    def __init__(self, prompt: DialoguePrompt) -> None:
        self.prompt = prompt

    async def start_with_npc(
        self, player_id: uuid.UUID, *, npc_id: str, npc_name: str, npc_definition_id: int
    ) -> DialoguePrompt:
        _ = player_id, npc_id, npc_name, npc_definition_id
        return self.prompt

    async def choose_option(self, player_id: uuid.UUID, option_index: int) -> DialoguePrompt:
        _ = player_id, option_index
        return self.prompt

    def get_cursor(self, player_id: uuid.UUID) -> None:
        _ = player_id

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

    def fake_emit(player_id: uuid.UUID, npc_name: str, prompt: DialoguePrompt) -> str:
        _ = player_id, npc_name, prompt
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
