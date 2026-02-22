"""
Unit tests for quest commands: journal/quests (quest log) and quest abandon.

Tests handle_journal_command and handle_quest_command with mocked container and services.
"""

import uuid
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.commands.quest_commands import handle_journal_command, handle_quest_command

# pylint: disable=redefined-outer-name  # Reason: Pytest fixtures are injected as function parameters, which triggers this warning but is the standard pytest pattern
# pylint: disable=protected-access  # Reason: Tests need to access protected members to verify internal state and behavior


@pytest.fixture
def current_user():
    """Minimal current_user dict for command handlers."""
    return {"id": str(uuid.uuid4()), "username": "testuser"}


@pytest.fixture
def mock_request():
    """Request with app.state.container (set per test)."""
    return MagicMock()


# ---- handle_journal_command ----
@pytest.mark.asyncio
async def test_journal_returns_unavailable_when_no_container(current_user, mock_request):
    """Journal returns message when container/persistence not available."""
    mock_request.app = None

    result = await handle_journal_command(
        _command_data={},
        current_user=current_user,
        request=mock_request,
        _alias_storage=None,
        player_name="testuser",
    )

    assert "result" in result
    assert "not available" in result["result"].lower()


@pytest.mark.asyncio
async def test_journal_returns_log_when_available(current_user, mock_request):
    """Journal returns formatted quest log when services available."""
    player_id = uuid.uuid4()
    mock_player = MagicMock()
    mock_player.player_id = player_id
    mock_persistence = AsyncMock()
    mock_persistence.get_player_by_name = AsyncMock(return_value=mock_player)
    mock_quest_service = MagicMock()
    mock_quest_service.get_quest_log = AsyncMock(
        return_value=[
            {
                "quest_id": "q1",
                "name": "leave_the_tutorial",
                "title": "Leave the Tutorial",
                "description": "Find your way out.",
                "goals_with_progress": [{"target": "exit", "current": 0, "required": 1, "done": False}],
                "state": "active",
            }
        ]
    )
    mock_container = MagicMock()
    mock_container.async_persistence = mock_persistence
    mock_container.quest_service = mock_quest_service
    mock_request.app = MagicMock()
    mock_request.app.state = MagicMock()
    mock_request.app.state.container = mock_container

    with (
        patch("server.commands.quest_commands.get_username_from_user", return_value="testuser"),
        patch(
            "server.commands.quest_commands._get_container_and_persistence",
            return_value=(mock_container, mock_persistence),
        ),
        patch("server.commands.quest_commands._get_quest_service", return_value=mock_quest_service),
    ):
        result = await handle_journal_command(
            _command_data={},
            current_user=current_user,
            request=mock_request,
            _alias_storage=None,
            player_name="testuser",
        )

    assert "result" in result
    assert "Quest log" in result["result"] or "leave_the_tutorial" in result["result"]
    assert "ACTIVE" in result["result"] or "active" in result["result"]


@pytest.mark.asyncio
async def test_journal_character_not_found(current_user, mock_request):
    """Journal returns error when character not found."""
    mock_persistence = AsyncMock()
    mock_persistence.get_player_by_name = AsyncMock(return_value=None)
    mock_container = MagicMock()
    mock_quest_service = MagicMock()
    with (
        patch("server.commands.quest_commands.get_username_from_user", return_value="testuser"),
        patch(
            "server.commands.quest_commands._get_container_and_persistence",
            return_value=(mock_container, mock_persistence),
        ),
        patch("server.commands.quest_commands._get_quest_service", return_value=mock_quest_service),
    ):
        result = await handle_journal_command(
            _command_data={},
            current_user=current_user,
            request=mock_request,
            _alias_storage=None,
            player_name="testuser",
        )

    assert "result" in result
    assert "Character not found" in result["result"] or "not found" in result["result"].lower()


# ---- handle_quest_command (abandon) ----
@pytest.mark.asyncio
async def test_quest_abandon_usage_when_no_subcommand(current_user, mock_request):
    """Quest command returns usage when args empty or not 'abandon'."""
    result = await handle_quest_command(
        command_data={"args": []},
        current_user=current_user,
        request=mock_request,
        _alias_storage=None,
        _player_name="testuser",
    )

    assert "result" in result
    assert "Usage" in result["result"] or "quest abandon" in result["result"].lower()


@pytest.mark.asyncio
async def test_quest_abandon_usage_when_wrong_subcommand(current_user, mock_request):
    """Quest command returns usage when first arg is not abandon."""
    result = await handle_quest_command(
        command_data={"args": ["list"]},
        current_user=current_user,
        request=mock_request,
        _alias_storage=None,
        _player_name="testuser",
    )

    assert "Usage" in result["result"] or "abandon" in result["result"].lower()


@pytest.mark.asyncio
async def test_quest_abandon_usage_when_no_quest_name(current_user, mock_request):
    """Quest abandon returns usage when quest name missing."""
    result = await handle_quest_command(
        command_data={"args": ["abandon"]},
        current_user=current_user,
        request=mock_request,
        _alias_storage=None,
        _player_name="testuser",
    )

    assert "Usage" in result["result"] or "quest name" in result["result"].lower()


@pytest.mark.asyncio
async def test_quest_abandon_success(current_user, mock_request):
    """Quest abandon returns success when abandon succeeds."""
    player_id = uuid.uuid4()
    mock_player = MagicMock()
    mock_player.player_id = player_id
    mock_persistence = AsyncMock()
    mock_persistence.get_player_by_name = AsyncMock(return_value=mock_player)
    mock_quest_service = MagicMock()
    mock_quest_service.abandon = AsyncMock(return_value={"success": True, "message": "Quest abandoned."})
    mock_container = MagicMock()

    with (
        patch("server.commands.quest_commands.get_username_from_user", return_value="testuser"),
        patch(
            "server.commands.quest_commands._get_container_and_persistence",
            return_value=(mock_container, mock_persistence),
        ),
        patch("server.commands.quest_commands._get_quest_service", return_value=mock_quest_service),
    ):
        result = await handle_quest_command(
            command_data={"args": ["abandon", "leave_the_tutorial"]},
            current_user=current_user,
            request=mock_request,
            _alias_storage=None,
            _player_name="testuser",
        )

    assert "result" in result
    assert "abandoned" in result["result"].lower()
    mock_quest_service.abandon.assert_awaited_once_with(player_id, "leave_the_tutorial")


@pytest.mark.asyncio
async def test_quest_abandon_failure_message(current_user, mock_request):
    """Quest abandon returns service message when abandon fails."""
    player_id = uuid.uuid4()
    mock_player = MagicMock()
    mock_player.player_id = player_id
    mock_persistence = AsyncMock()
    mock_persistence.get_player_by_name = AsyncMock(return_value=mock_player)
    mock_quest_service = MagicMock()
    mock_quest_service.abandon = AsyncMock(return_value={"success": False, "message": "You do not have this quest."})
    mock_container = MagicMock()

    with (
        patch("server.commands.quest_commands.get_username_from_user", return_value="testuser"),
        patch(
            "server.commands.quest_commands._get_container_and_persistence",
            return_value=(mock_container, mock_persistence),
        ),
        patch("server.commands.quest_commands._get_quest_service", return_value=mock_quest_service),
    ):
        result = await handle_quest_command(
            command_data={"args": ["abandon", "unknown_quest"]},
            current_user=current_user,
            request=mock_request,
            _alias_storage=None,
            _player_name="testuser",
        )

    assert "result" in result
    assert "do not have" in result["result"].lower() or "unknown" in result["result"].lower()
