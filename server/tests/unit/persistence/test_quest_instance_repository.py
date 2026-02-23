"""
Unit tests for QuestInstanceRepository.

Tests create, get_by_player_and_quest, update_state_and_progress,
list_active_by_player, list_completed_by_player with mocked session.
"""

import uuid
from unittest.mock import AsyncMock, MagicMock, patch

import pytest
from sqlalchemy.exc import SQLAlchemyError

from server.exceptions import DatabaseError
from server.models.quest import QuestInstance
from server.persistence.repositories.quest_instance_repository import (
    QuestInstanceRepository,
)

# pylint: disable=redefined-outer-name  # Reason: Pytest fixtures are injected as function parameters, which triggers this warning but is the standard pytest pattern
# pylint: disable=protected-access  # Reason: Tests need to access protected members to verify internal state and behavior


@pytest.fixture
def quest_instance_repository():
    """Create a QuestInstanceRepository instance."""
    return QuestInstanceRepository()


@pytest.fixture
def mock_quest_instance():
    """Create a mock QuestInstance."""
    inst = MagicMock(spec=QuestInstance)
    inst.id = uuid.uuid4()
    inst.player_id = str(uuid.uuid4())
    inst.quest_id = "leave_the_tutorial"
    inst.state = "active"
    inst.progress = {}
    return inst


def _make_session_context(mock_session):
    """Return context manager that yields mock_session for async with."""
    session_maker = MagicMock()
    session_maker.return_value.__aenter__ = AsyncMock(return_value=mock_session)
    session_maker.return_value.__aexit__ = AsyncMock(return_value=None)
    return session_maker


@pytest.mark.asyncio
async def test_create_success(quest_instance_repository):
    """Test create adds instance, commits, refreshes and returns it."""
    player_id = str(uuid.uuid4())
    mock_session = AsyncMock()
    mock_session.add = MagicMock()
    mock_session.commit = AsyncMock()
    mock_session.refresh = AsyncMock()

    with patch("server.persistence.repositories.quest_instance_repository.get_session_maker") as mock_get_session:
        mock_get_session.return_value = _make_session_context(mock_session)

        result = await quest_instance_repository.create(
            player_id=player_id,
            quest_id="leave_the_tutorial",
            state="active",
            progress={},
        )

        mock_session.add.assert_called_once()
        mock_session.commit.assert_awaited_once()
        mock_session.refresh.assert_awaited_once()
        assert result.player_id == player_id
        assert result.quest_id == "leave_the_tutorial"
        assert result.state == "active"
        assert result.progress == {}


@pytest.mark.asyncio
async def test_create_database_error(quest_instance_repository):
    """Test create raises DatabaseError on DB failure."""
    mock_session = AsyncMock()
    mock_session.add = MagicMock()
    mock_session.commit = AsyncMock(side_effect=SQLAlchemyError("Constraint failed"))

    with patch("server.persistence.repositories.quest_instance_repository.get_session_maker") as mock_get_session:
        mock_get_session.return_value = _make_session_context(mock_session)

        with pytest.raises(DatabaseError):
            await quest_instance_repository.create(
                player_id=str(uuid.uuid4()),
                quest_id="leave_the_tutorial",
            )


@pytest.mark.asyncio
async def test_get_by_player_and_quest_success(quest_instance_repository, mock_quest_instance):
    """Test get_by_player_and_quest returns instance when found."""
    mock_session = AsyncMock()
    mock_result = MagicMock()
    mock_result.unique.return_value.scalars.return_value.first.return_value = mock_quest_instance
    mock_session.execute.return_value = mock_result

    with patch("server.persistence.repositories.quest_instance_repository.get_session_maker") as mock_get_session:
        mock_get_session.return_value = _make_session_context(mock_session)

        result = await quest_instance_repository.get_by_player_and_quest(
            player_id=mock_quest_instance.player_id,
            quest_id=mock_quest_instance.quest_id,
        )

        assert result is mock_quest_instance


@pytest.mark.asyncio
async def test_get_by_player_and_quest_not_found(quest_instance_repository):
    """Test get_by_player_and_quest returns None when not found."""
    mock_session = AsyncMock()
    mock_result = MagicMock()
    mock_result.unique.return_value.scalars.return_value.first.return_value = None
    mock_session.execute.return_value = mock_result

    with patch("server.persistence.repositories.quest_instance_repository.get_session_maker") as mock_get_session:
        mock_get_session.return_value = _make_session_context(mock_session)

        result = await quest_instance_repository.get_by_player_and_quest(
            player_id=str(uuid.uuid4()),
            quest_id="leave_the_tutorial",
        )

        assert result is None


@pytest.mark.asyncio
async def test_get_by_player_and_quest_accepts_uuid(quest_instance_repository):
    """Test get_by_player_and_quest accepts UUID for player_id."""
    pid = uuid.uuid4()
    mock_session = AsyncMock()
    mock_result = MagicMock()
    mock_result.unique.return_value.scalars.return_value.first.return_value = None
    mock_session.execute.return_value = mock_result

    with patch("server.persistence.repositories.quest_instance_repository.get_session_maker") as mock_get_session:
        mock_get_session.return_value = _make_session_context(mock_session)

        result = await quest_instance_repository.get_by_player_and_quest(
            player_id=pid,
            quest_id="leave_the_tutorial",
        )

        assert result is None
        # Session execute should have been called with player_id as string in the query
        mock_session.execute.assert_awaited_once()


@pytest.mark.asyncio
async def test_update_state_and_progress_success(quest_instance_repository):
    """Test update_state_and_progress updates and commits."""
    instance_id = uuid.uuid4()
    mock_session = AsyncMock()
    mock_session.execute.return_value = MagicMock()
    mock_session.commit = AsyncMock()

    with patch("server.persistence.repositories.quest_instance_repository.get_session_maker") as mock_get_session:
        mock_get_session.return_value = _make_session_context(mock_session)

        await quest_instance_repository.update_state_and_progress(
            instance_id=instance_id,
            state="completed",
            progress={"0": 1},
        )

        mock_session.execute.assert_awaited_once()
        mock_session.commit.assert_awaited_once()


@pytest.mark.asyncio
async def test_update_state_and_progress_no_op(quest_instance_repository):
    """Test update_state_and_progress does nothing when no fields passed."""
    instance_id = uuid.uuid4()
    mock_session = AsyncMock()

    with patch("server.persistence.repositories.quest_instance_repository.get_session_maker") as mock_get_session:
        mock_get_session.return_value = _make_session_context(mock_session)

        await quest_instance_repository.update_state_and_progress(
            instance_id=instance_id,
        )

        mock_session.execute.assert_not_awaited()
        mock_session.commit.assert_not_awaited()


@pytest.mark.asyncio
async def test_list_active_by_player_success(quest_instance_repository, mock_quest_instance):
    """Test list_active_by_player returns list of active instances."""
    mock_session = AsyncMock()
    mock_result = MagicMock()
    mock_result.unique.return_value.scalars.return_value.all.return_value = [mock_quest_instance]
    mock_session.execute.return_value = mock_result

    with patch("server.persistence.repositories.quest_instance_repository.get_session_maker") as mock_get_session:
        mock_get_session.return_value = _make_session_context(mock_session)

        result = await quest_instance_repository.list_active_by_player(
            player_id=mock_quest_instance.player_id,
        )

        assert len(result) == 1
        assert result[0] is mock_quest_instance


@pytest.mark.asyncio
async def test_list_active_by_player_empty(quest_instance_repository):
    """Test list_active_by_player returns empty list when none."""
    mock_session = AsyncMock()
    mock_result = MagicMock()
    mock_result.unique.return_value.scalars.return_value.all.return_value = []
    mock_session.execute.return_value = mock_result

    with patch("server.persistence.repositories.quest_instance_repository.get_session_maker") as mock_get_session:
        mock_get_session.return_value = _make_session_context(mock_session)

        result = await quest_instance_repository.list_active_by_player(
            player_id=str(uuid.uuid4()),
        )

        assert result == []


@pytest.mark.asyncio
async def test_list_completed_by_player_success(quest_instance_repository, mock_quest_instance):
    """Test list_completed_by_player returns list of completed instances."""
    mock_quest_instance.state = "completed"
    mock_session = AsyncMock()
    mock_result = MagicMock()
    mock_result.unique.return_value.scalars.return_value.all.return_value = [mock_quest_instance]
    mock_session.execute.return_value = mock_result

    with patch("server.persistence.repositories.quest_instance_repository.get_session_maker") as mock_get_session:
        mock_get_session.return_value = _make_session_context(mock_session)

        result = await quest_instance_repository.list_completed_by_player(
            player_id=mock_quest_instance.player_id,
        )

        assert len(result) == 1
        assert result[0] is mock_quest_instance


@pytest.mark.asyncio
async def test_list_completed_by_player_database_error(quest_instance_repository):
    """Test list_completed_by_player raises DatabaseError on DB failure."""
    mock_session = AsyncMock()
    mock_session.execute.side_effect = SQLAlchemyError("Connection failed")

    with patch("server.persistence.repositories.quest_instance_repository.get_session_maker") as mock_get_session:
        mock_get_session.return_value = _make_session_context(mock_session)

        with pytest.raises(DatabaseError):
            await quest_instance_repository.list_completed_by_player(
                player_id=str(uuid.uuid4()),
            )
