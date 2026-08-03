"""Unit tests for PlayerSkillRepository."""

import uuid
from types import SimpleNamespace
from unittest.mock import AsyncMock, MagicMock, patch

import pytest
from sqlalchemy.exc import SQLAlchemyError

from server.exceptions import DatabaseError
from server.persistence.repositories.player_skill_repository import PlayerSkillRepository


@pytest.fixture
def repo() -> PlayerSkillRepository:
    return PlayerSkillRepository()


@pytest.mark.asyncio
async def test_delete_for_player_success(repo: PlayerSkillRepository) -> None:
    player_id = uuid.uuid4()
    mock_session = AsyncMock()
    mock_session.__aenter__ = AsyncMock(return_value=mock_session)
    mock_session.__aexit__ = AsyncMock(return_value=None)

    with patch(
        "server.persistence.repositories.player_skill_repository.get_session_maker",
        return_value=MagicMock(return_value=mock_session),
    ):
        await repo.delete_for_player(player_id)

    mock_session.commit.assert_awaited_once()


@pytest.mark.asyncio
async def test_delete_for_player_db_error(repo: PlayerSkillRepository) -> None:
    player_id = uuid.uuid4()
    mock_session = AsyncMock()
    mock_session.execute = AsyncMock(side_effect=SQLAlchemyError("fail"))
    mock_session.__aenter__ = AsyncMock(return_value=mock_session)
    mock_session.__aexit__ = AsyncMock(return_value=None)

    with patch(
        "server.persistence.repositories.player_skill_repository.get_session_maker",
        return_value=MagicMock(return_value=mock_session),
    ):
        with pytest.raises(DatabaseError):
            await repo.delete_for_player(player_id)


@pytest.mark.asyncio
async def test_insert_many_empty(repo: PlayerSkillRepository) -> None:
    await repo.insert_many(uuid.uuid4(), [])


@pytest.mark.asyncio
async def test_insert_many_success(repo: PlayerSkillRepository) -> None:
    player_id = uuid.uuid4()
    mock_session = AsyncMock()
    mock_session.__aenter__ = AsyncMock(return_value=mock_session)
    mock_session.__aexit__ = AsyncMock(return_value=None)

    with patch(
        "server.persistence.repositories.player_skill_repository.get_session_maker",
        return_value=MagicMock(return_value=mock_session),
    ):
        await repo.insert_many(player_id, [(1, 50), (2, 30)])

    mock_session.commit.assert_awaited_once()


@pytest.mark.asyncio
async def test_get_by_player_id_success(repo: PlayerSkillRepository) -> None:
    player_id = uuid.uuid4()
    mock_session = AsyncMock()
    mock_result = MagicMock()
    mock_result.mappings.return_value.all.return_value = [
        SimpleNamespace(
            player_id=str(player_id),
            skill_id=1,
            value=50,
            skill_key="spot",
            skill_name="Spot Hidden",
            skill_description="desc",
            skill_base_value=25,
            skill_allow_at_creation=True,
            skill_category="perception",
        )
    ]
    mock_session.execute = AsyncMock(return_value=mock_result)
    mock_session.__aenter__ = AsyncMock(return_value=mock_session)
    mock_session.__aexit__ = AsyncMock(return_value=None)

    with patch(
        "server.persistence.repositories.player_skill_repository.get_session_maker",
        return_value=MagicMock(return_value=mock_session),
    ):
        skills = await repo.get_by_player_id(player_id)

    assert len(skills) == 1
    assert skills[0].value == 50


@pytest.mark.asyncio
async def test_update_value_success(repo: PlayerSkillRepository) -> None:
    player_id = uuid.uuid4()
    mock_session = AsyncMock()
    mock_session.__aenter__ = AsyncMock(return_value=mock_session)
    mock_session.__aexit__ = AsyncMock(return_value=None)

    with patch(
        "server.persistence.repositories.player_skill_repository.get_session_maker",
        return_value=MagicMock(return_value=mock_session),
    ):
        await repo.update_value(player_id, 3, 75)

    mock_session.commit.assert_awaited_once()
