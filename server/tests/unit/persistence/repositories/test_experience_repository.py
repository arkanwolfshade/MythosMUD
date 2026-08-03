"""Unit tests for ExperienceRepository."""

import uuid
from unittest.mock import AsyncMock, MagicMock, patch

import pytest
from sqlalchemy.exc import SQLAlchemyError

from server.exceptions import DatabaseError
from server.persistence.repositories.experience_repository import ExperienceRepository


@pytest.fixture
def repo() -> ExperienceRepository:
    return ExperienceRepository(event_bus=None)


@pytest.mark.asyncio
async def test_gain_experience_negative_amount(repo: ExperienceRepository) -> None:
    player = MagicMock()
    with pytest.raises(ValueError, match="non-negative"):
        await repo.gain_experience(player, -1)


@pytest.mark.asyncio
async def test_gain_experience_success(repo: ExperienceRepository) -> None:
    player = MagicMock()
    player.player_id = uuid.uuid4()
    player.name = "Tester"
    player.experience_points = 10
    player.level = 1

    with patch.object(repo, "update_player_xp", new_callable=AsyncMock) as mock_update:
        await repo.gain_experience(player, 5, source="combat")

    assert player.experience_points == 15
    mock_update.assert_awaited_once()


@pytest.mark.asyncio
async def test_gain_experience_publishes_event() -> None:
    event_bus = MagicMock()
    repo = ExperienceRepository(event_bus=event_bus)
    player = MagicMock()
    player.player_id = uuid.uuid4()
    player.name = "Tester"
    player.experience_points = 0
    player.level = 1

    with patch.object(repo, "update_player_xp", new_callable=AsyncMock):
        await repo.gain_experience(player, 10, source="quest")

    event_bus.publish.assert_called_once()


@pytest.mark.asyncio
async def test_update_player_xp_negative_delta(repo: ExperienceRepository) -> None:
    with pytest.raises(ValueError, match="non-negative"):
        await repo.update_player_xp(uuid.uuid4(), -5)


@pytest.mark.asyncio
async def test_update_player_xp_success(repo: ExperienceRepository) -> None:
    player_id = uuid.uuid4()
    mock_session = AsyncMock()
    mock_result = MagicMock()
    mock_result.scalar.return_value = 1
    mock_session.execute = AsyncMock(return_value=mock_result)
    mock_session.__aenter__ = AsyncMock(return_value=mock_session)
    mock_session.__aexit__ = AsyncMock(return_value=None)
    mock_maker = MagicMock(return_value=mock_session)

    with patch("server.persistence.repositories.experience_repository.get_session_maker", return_value=mock_maker):
        await repo.update_player_xp(player_id, 10, reason="test")

    mock_session.commit.assert_awaited_once()


@pytest.mark.asyncio
async def test_update_player_xp_player_not_found(repo: ExperienceRepository) -> None:
    player_id = uuid.uuid4()
    mock_session = AsyncMock()
    mock_result = MagicMock()
    mock_result.scalar.return_value = 0
    mock_session.execute = AsyncMock(return_value=mock_result)
    mock_session.__aenter__ = AsyncMock(return_value=mock_session)
    mock_session.__aexit__ = AsyncMock(return_value=None)

    with patch(
        "server.persistence.repositories.experience_repository.get_session_maker",
        return_value=MagicMock(return_value=mock_session),
    ):
        with pytest.raises(DatabaseError):
            await repo.update_player_xp(player_id, 5)


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
            await repo.update_player_stat_field(player_id, "lucidity", -1)
