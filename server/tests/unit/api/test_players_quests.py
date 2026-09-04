"""
Unit tests for GET /api/players/{player_id}/quests (quest log).

Tests get_player_quests with mocked PlayerService and QuestService.
"""

import uuid
from unittest.mock import AsyncMock, MagicMock

import pytest

from server.api.players import get_player_quests

# pylint: disable=redefined-outer-name  # Reason: Pytest fixtures are injected as function parameters, which triggers this warning but is the standard pytest pattern
# pylint: disable=protected-access  # Reason: Tests need to access protected members to verify internal state and behavior


@pytest.fixture
def mock_request():
    """Minimal request for endpoint (not used for quest logic)."""
    return MagicMock()


@pytest.fixture
def mock_user():
    """Authenticated user."""
    from server.models.user import User

    return User(
        id=uuid.uuid4(),
        username="testuser",
        email="test@example.com",
        hashed_password="hashed",
        is_active=True,
        is_superuser=False,
        is_verified=True,
    )


@pytest.fixture
def player_id():
    """Character (player) UUID."""
    return uuid.uuid4()


@pytest.fixture
def mock_player_service():
    """PlayerService that validates character access."""
    svc = MagicMock()
    svc.validate_character_access = AsyncMock(return_value=(True, MagicMock(), None))
    return svc


@pytest.fixture
def mock_quest_service():
    """QuestService that returns quest log entries."""
    svc = MagicMock()
    svc.get_quest_log = AsyncMock(return_value=[])
    return svc


@pytest.mark.asyncio
async def test_get_player_quests_returns_quest_log(
    request, mock_user, player_id, mock_player_service, mock_quest_service
):
    """GET quests returns QuestLogResponse with entries when access allowed."""
    req = request.getfixturevalue("mock_request")
    mock_quest_service.get_quest_log = AsyncMock(
        return_value=[
            {
                "quest_id": "leave_the_tutorial",
                "name": "leave_the_tutorial",
                "title": "Leave the Tutorial",
                "description": "Find your way out.",
                "goals_with_progress": [{"goal_type": "complete_activity", "current": 0, "required": 1, "done": False}],
                "state": "active",
            }
        ]
    )

    response = await get_player_quests(
        player_id=player_id,
        _request=req,
        current_user=mock_user,
        player_service=mock_player_service,
        quest_service=mock_quest_service,
        include_completed=True,
    )

    assert response.quests is not None
    assert len(response.quests) == 1
    assert response.quests[0].quest_id == "leave_the_tutorial"
    assert response.quests[0].name == "leave_the_tutorial"
    assert response.quests[0].state == "active"
    mock_player_service.validate_character_access.assert_awaited_once_with(player_id, mock_user.id)
    mock_quest_service.get_quest_log.assert_awaited_once_with(player_id, include_completed=True)


@pytest.mark.asyncio
async def test_get_player_quests_include_completed_false(
    request, mock_user, player_id, mock_player_service, mock_quest_service
):
    """GET quests with include_completed=False passes to get_quest_log."""
    req = request.getfixturevalue("mock_request")
    await get_player_quests(
        player_id=player_id,
        _request=req,
        current_user=mock_user,
        player_service=mock_player_service,
        quest_service=mock_quest_service,
        include_completed=False,
    )

    mock_quest_service.get_quest_log.assert_awaited_once_with(player_id, include_completed=False)


@pytest.mark.asyncio
async def test_get_player_quests_403_when_not_owner(
    request, mock_user, player_id, mock_player_service, mock_quest_service
):
    """GET quests raises 403 when validate_character_access returns not ok."""
    from server.exceptions import LoggedHTTPException

    req = request.getfixturevalue("mock_request")
    mock_player_service.validate_character_access = AsyncMock(
        return_value=(False, None, "Not authorized to view this character's quests")
    )

    with pytest.raises(LoggedHTTPException) as exc_info:
        await get_player_quests(
            player_id=player_id,
            _request=req,
            current_user=mock_user,
            player_service=mock_player_service,
            quest_service=mock_quest_service,
        )

    assert exc_info.value.status_code == 403
    mock_player_service.validate_character_access.assert_awaited_once_with(player_id, mock_user.id)
    mock_quest_service.get_quest_log.assert_not_awaited()
