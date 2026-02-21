"""
Unit tests for QuestDefinitionRepository.

Tests get_by_id, get_by_name, and list_quest_ids_offered_by with mocked session.
"""

from unittest.mock import AsyncMock, MagicMock, patch

import pytest
from sqlalchemy.exc import SQLAlchemyError

from server.exceptions import DatabaseError
from server.models.quest import QuestDefinition
from server.persistence.repositories.quest_definition_repository import QuestDefinitionRepository


@pytest.fixture
def quest_definition_repository():
    """Create a QuestDefinitionRepository instance."""
    return QuestDefinitionRepository()


@pytest.fixture
def mock_quest_definition():
    """Create a mock QuestDefinition with definition JSONB."""
    q = MagicMock(spec=QuestDefinition)
    q.id = "leave_the_tutorial"
    q.definition = {
        "name": "leave_the_tutorial",
        "title": "Leave the Tutorial",
        "description": "Find your way out.",
        "goals": [],
        "rewards": [],
        "triggers": [],
    }
    return q


def _make_session_context(mock_session):
    """Return context manager that yields mock_session for async with."""
    session_maker = MagicMock()
    session_maker.return_value.__aenter__ = AsyncMock(return_value=mock_session)
    session_maker.return_value.__aexit__ = AsyncMock(return_value=None)
    return session_maker


@pytest.mark.asyncio
async def test_get_by_id_success(request, mock_quest_definition):
    """Test get_by_id returns definition when found."""
    repo = request.getfixturevalue("quest_definition_repository")
    mock_session = AsyncMock()
    mock_result = MagicMock()
    mock_result.scalar_one_or_none.return_value = mock_quest_definition
    mock_session.execute.return_value = mock_result

    with patch("server.persistence.repositories.quest_definition_repository.get_session_maker") as mock_get_session:
        mock_get_session.return_value = _make_session_context(mock_session)

        result = await repo.get_by_id("leave_the_tutorial")

        assert result is mock_quest_definition
        assert result.id == "leave_the_tutorial"


@pytest.mark.asyncio
async def test_get_by_id_not_found(request):
    """Test get_by_id returns None when not found."""
    repo = request.getfixturevalue("quest_definition_repository")
    mock_session = AsyncMock()
    mock_result = MagicMock()
    mock_result.scalar_one_or_none.return_value = None
    mock_session.execute.return_value = mock_result

    with patch("server.persistence.repositories.quest_definition_repository.get_session_maker") as mock_get_session:
        mock_get_session.return_value = _make_session_context(mock_session)

        result = await repo.get_by_id("unknown_quest")

        assert result is None


@pytest.mark.asyncio
async def test_get_by_id_database_error(request):
    """Test get_by_id raises DatabaseError on DB failure."""
    repo = request.getfixturevalue("quest_definition_repository")
    mock_session = AsyncMock()
    mock_session.execute.side_effect = SQLAlchemyError("Connection failed")

    with patch("server.persistence.repositories.quest_definition_repository.get_session_maker") as mock_get_session:
        mock_get_session.return_value = _make_session_context(mock_session)

        with pytest.raises(DatabaseError):
            await repo.get_by_id("any_id")


@pytest.mark.asyncio
async def test_get_by_name_success(request, mock_quest_definition):
    """Test get_by_name returns definition when found by common name."""
    repo = request.getfixturevalue("quest_definition_repository")
    mock_session = AsyncMock()
    mock_result = MagicMock()
    mock_result.scalar_one_or_none.return_value = mock_quest_definition
    mock_session.execute.return_value = mock_result

    with patch("server.persistence.repositories.quest_definition_repository.get_session_maker") as mock_get_session:
        mock_get_session.return_value = _make_session_context(mock_session)

        result = await repo.get_by_name("leave_the_tutorial")

        assert result is mock_quest_definition
        assert result.definition["name"] == "leave_the_tutorial"


@pytest.mark.asyncio
async def test_get_by_name_not_found(request):
    """Test get_by_name returns None when not found."""
    repo = request.getfixturevalue("quest_definition_repository")
    mock_session = AsyncMock()
    mock_result = MagicMock()
    mock_result.scalar_one_or_none.return_value = None
    mock_session.execute.return_value = mock_result

    with patch("server.persistence.repositories.quest_definition_repository.get_session_maker") as mock_get_session:
        mock_get_session.return_value = _make_session_context(mock_session)

        result = await repo.get_by_name("unknown")

        assert result is None


@pytest.mark.asyncio
async def test_get_by_name_database_error(request):
    """Test get_by_name raises DatabaseError on DB failure."""
    repo = request.getfixturevalue("quest_definition_repository")
    mock_session = AsyncMock()
    mock_session.execute.side_effect = SQLAlchemyError("Connection failed")

    with patch("server.persistence.repositories.quest_definition_repository.get_session_maker") as mock_get_session:
        mock_get_session.return_value = _make_session_context(mock_session)

        with pytest.raises(DatabaseError):
            await repo.get_by_name("any_name")


@pytest.mark.asyncio
async def test_list_quest_ids_offered_by_success(request):
    """Test list_quest_ids_offered_by returns quest IDs for entity."""
    repo = request.getfixturevalue("quest_definition_repository")
    mock_session = AsyncMock()
    mock_result = MagicMock()
    mock_result.all.return_value = [("leave_the_tutorial",)]
    mock_session.execute.return_value = mock_result

    with patch("server.persistence.repositories.quest_definition_repository.get_session_maker") as mock_get_session:
        mock_get_session.return_value = _make_session_context(mock_session)

        result = await repo.list_quest_ids_offered_by("room", "earth_tutorial_exit_room")

        assert result == ["leave_the_tutorial"]


@pytest.mark.asyncio
async def test_list_quest_ids_offered_by_empty(request):
    """Test list_quest_ids_offered_by returns empty list when no offers."""
    repo = request.getfixturevalue("quest_definition_repository")
    mock_session = AsyncMock()
    mock_result = MagicMock()
    mock_result.all.return_value = []
    mock_session.execute.return_value = mock_result

    with patch("server.persistence.repositories.quest_definition_repository.get_session_maker") as mock_get_session:
        mock_get_session.return_value = _make_session_context(mock_session)

        result = await repo.list_quest_ids_offered_by("npc", "some_npc_id")

        assert result == []


@pytest.mark.asyncio
async def test_list_quest_ids_offered_by_database_error(request):
    """Test list_quest_ids_offered_by raises DatabaseError on DB failure."""
    repo = request.getfixturevalue("quest_definition_repository")
    mock_session = AsyncMock()
    mock_session.execute.side_effect = SQLAlchemyError("Connection failed")

    with patch("server.persistence.repositories.quest_definition_repository.get_session_maker") as mock_get_session:
        mock_get_session.return_value = _make_session_context(mock_session)

        with pytest.raises(DatabaseError):
            await repo.list_quest_ids_offered_by("room", "room_id")
