"""Unit tests for SkillUseLogRepository."""

from __future__ import annotations

import uuid
from unittest.mock import AsyncMock, MagicMock, patch

import pytest
from sqlalchemy.exc import SQLAlchemyError

from server.exceptions import DatabaseError
from server.persistence.repositories.skill_use_log_repository import SkillUseLogRepository


@pytest.fixture
def repo():
    return SkillUseLogRepository()


def _mock_session(rows=None):
    mock_session = AsyncMock()
    mock_session.commit = AsyncMock()
    if rows is not None:
        mock_result = MagicMock()
        mock_result.mappings.return_value.all.return_value = rows
        mock_session.execute = AsyncMock(return_value=mock_result)
    else:
        mock_session.execute = AsyncMock()
    mock_session.__aenter__ = AsyncMock(return_value=mock_session)
    mock_session.__aexit__ = AsyncMock(return_value=None)
    return mock_session


@pytest.mark.asyncio
async def test_record_use(repo):
    mock_session = _mock_session()
    player_id = uuid.uuid4()
    with patch(
        "server.persistence.repositories.skill_use_log_repository.get_session_maker",
        return_value=MagicMock(return_value=mock_session),
    ):
        await repo.record_use(player_id, skill_id=3, character_level_at_use=2)
    mock_session.commit.assert_awaited_once()


@pytest.mark.asyncio
async def test_get_skill_ids_used_at_level(repo):
    row = MagicMock()
    row.skill_id = 5
    mock_session = _mock_session([row])
    player_id = uuid.uuid4()
    with patch(
        "server.persistence.repositories.skill_use_log_repository.get_session_maker",
        return_value=MagicMock(return_value=mock_session),
    ):
        ids = await repo.get_skill_ids_used_at_level(player_id, 3)
    assert ids == [5]


@pytest.mark.asyncio
async def test_record_use_db_error(repo):
    mock_session = AsyncMock()
    mock_session.execute = AsyncMock(side_effect=SQLAlchemyError("fail"))
    mock_session.__aenter__ = AsyncMock(return_value=mock_session)
    mock_session.__aexit__ = AsyncMock(return_value=None)
    with patch(
        "server.persistence.repositories.skill_use_log_repository.get_session_maker",
        return_value=MagicMock(return_value=mock_session),
    ):
        with pytest.raises(DatabaseError):
            await repo.record_use(uuid.uuid4(), skill_id=1, character_level_at_use=1)
