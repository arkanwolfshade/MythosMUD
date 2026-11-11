"""Unit tests for ExperienceRepository."""

# pyright: reportAny=false, reportUnusedCallResult=false
# TEST_MOCK: mock_result.scalar()/session.commit() are untyped AsyncMock/MagicMock results.

import uuid
from unittest.mock import AsyncMock, MagicMock, patch

import pytest
from sqlalchemy.exc import SQLAlchemyError

from server.exceptions import DatabaseError
from server.persistence.repositories.experience_repository import ExperienceRepository


@pytest.fixture
def repo() -> ExperienceRepository:
    return ExperienceRepository()


@pytest.mark.asyncio
async def test_update_player_stat_field_invalid_name(repo: ExperienceRepository) -> None:
    with pytest.raises(ValueError, match="Invalid stat field"):
        await repo.update_player_stat_field(uuid.uuid4(), "not_a_stat", 1)


@pytest.mark.asyncio
async def test_update_player_stat_field_invalid_delta_type(repo: ExperienceRepository) -> None:
    with pytest.raises(TypeError, match="delta must be int or float"):
        await repo.update_player_stat_field(uuid.uuid4(), "strength", "bad")  # type: ignore[arg-type]


@pytest.mark.asyncio
async def test_update_player_stat_field_success(repo: ExperienceRepository) -> None:
    player_id = uuid.uuid4()
    mock_session = AsyncMock()
    mock_result = MagicMock()
    mock_result.scalar.return_value = 1
    mock_session.execute = AsyncMock(return_value=mock_result)
    mock_session.__aenter__ = AsyncMock(return_value=mock_session)
    mock_session.__aexit__ = AsyncMock(return_value=None)

    with patch(
        "server.persistence.repositories.experience_repository.get_session_maker",
        return_value=MagicMock(return_value=mock_session),
    ):
        await repo.update_player_stat_field(player_id, "strength", 2, reason="level up")

    mock_session.commit.assert_awaited_once()


@pytest.mark.asyncio
async def test_update_player_stat_field_db_error(repo: ExperienceRepository) -> None:
    player_id = uuid.uuid4()
    mock_session = AsyncMock()
    mock_session.execute = AsyncMock(side_effect=SQLAlchemyError("fail"))
    mock_session.__aenter__ = AsyncMock(return_value=mock_session)
    mock_session.__aexit__ = AsyncMock(return_value=None)

    with patch(
        "server.persistence.repositories.experience_repository.get_session_maker",
        return_value=MagicMock(return_value=mock_session),
    ):
        with pytest.raises(DatabaseError):
            await repo.update_player_stat_field(player_id, "fear", -1)


@pytest.mark.asyncio
async def test_update_player_stat_field_refuses_lucidity(repo: ExperienceRepository) -> None:
    """Lucidity is not a stats field (ADR-029 step 3a): writes go through LucidityService."""
    with pytest.raises(ValueError, match="Invalid stat field name: lucidity"):
        await repo.update_player_stat_field(uuid.uuid4(), "lucidity", -1)
