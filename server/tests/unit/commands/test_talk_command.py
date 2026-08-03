"""Unit tests for talk command helpers."""

import uuid
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.commands import talk_command as cmd
from server.game.dialogue.dialogue_service import DialoguePrompt


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
