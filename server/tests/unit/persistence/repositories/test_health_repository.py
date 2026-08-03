"""Unit tests for HealthRepository."""

from __future__ import annotations

import uuid
from unittest.mock import AsyncMock, MagicMock, patch

import pytest
from sqlalchemy.exc import SQLAlchemyError

from server.exceptions import DatabaseError
from server.models.player import Player
from server.persistence.repositories.health_repository import HealthRepository, _stats_int


def test_stats_int_defaults_and_coercion() -> None:
    assert _stats_int({}, "current_dp", 20) == 20
    assert _stats_int({"current_dp": "15"}, "current_dp", 20) == 15
    assert _stats_int({"current_dp": object()}, "current_dp", 20) == 20
    assert _stats_int({"current_dp": "nope"}, "current_dp", 20) == 20


def test_calculate_effective_damage_zero_and_resistance_edge_cases() -> None:
    repo = HealthRepository()
    assert repo._calculate_effective_damage({}, 0, "cold") == 0
    assert repo._calculate_effective_damage({"cold_resistance": object()}, 10, "cold") == 10
    assert repo._calculate_effective_damage({"cold_resistance": "bad"}, 10, "water") == 10
    # Full resist still leaves at least 1 damage
    assert repo._calculate_effective_damage({"cold_resistance": 100}, 10, "cold") == 1


@pytest.mark.asyncio
async def test_damage_player_rejects_negative() -> None:
    repo = HealthRepository()
    with pytest.raises(ValueError, match="positive"):
        await repo.damage_player(MagicMock(spec=Player), -1)


@pytest.mark.asyncio
async def test_damage_player_logs_and_reraises_on_unexpected_error() -> None:
    repo = HealthRepository()
    player = MagicMock(spec=Player)
    player.player_id = uuid.uuid4()
    player.name = "Hurt"
    with patch.object(repo, "_damage_player_inner", new_callable=AsyncMock, side_effect=RuntimeError("db")):
        with pytest.raises(RuntimeError):
            await repo.damage_player(player, 5)


@pytest.mark.asyncio
async def test_heal_player_rejects_negative() -> None:
    repo = HealthRepository()
    with pytest.raises(ValueError, match="positive"):
        await repo.heal_player(MagicMock(spec=Player), -1)


@pytest.mark.asyncio
async def test_heal_player_success_and_capped() -> None:
    repo = HealthRepository()
    repo.update_player_health = AsyncMock()
    player = MagicMock(spec=Player)
    player.player_id = uuid.uuid4()
    player.name = "Healed"
    stats: dict[str, object] = {"current_dp": 10, "max_dp": 20, "constitution": 50, "size": 50}
    player.get_stats.return_value = stats

    await repo.heal_player(player, 100)

    assert stats["current_dp"] == 20
    player.set_stats.assert_called()
    repo.update_player_health.assert_awaited_once_with(player.player_id, 10, "healing")


@pytest.mark.asyncio
async def test_heal_player_no_op_when_already_full() -> None:
    repo = HealthRepository()
    repo.update_player_health = AsyncMock()
    player = MagicMock(spec=Player)
    player.player_id = uuid.uuid4()
    player.name = "Full"
    stats: dict[str, object] = {"current_dp": 20, "max_dp": 20}
    player.get_stats.return_value = stats

    await repo.heal_player(player, 5)

    repo.update_player_health.assert_not_awaited()


@pytest.mark.asyncio
async def test_heal_player_max_dp_fallback_when_zero() -> None:
    repo = HealthRepository()
    repo.update_player_health = AsyncMock()
    player = MagicMock(spec=Player)
    player.player_id = uuid.uuid4()
    player.name = "Fallback"
    stats: dict[str, object] = {"current_dp": 5, "max_dp": 0, "constitution": 0, "size": 0}
    player.get_stats.return_value = stats

    await repo.heal_player(player, 3)

    assert stats["current_dp"] == 8
    repo.update_player_health.assert_awaited_once()


@pytest.mark.asyncio
async def test_heal_player_logs_and_reraises_on_unexpected_error() -> None:
    repo = HealthRepository()
    player = MagicMock(spec=Player)
    player.player_id = uuid.uuid4()
    player.name = "FailHeal"
    with patch.object(repo, "_heal_player_inner", new_callable=AsyncMock, side_effect=OSError("disk")):
        with pytest.raises(OSError):
            await repo.heal_player(player, 5)


@pytest.mark.asyncio
async def test_update_player_health_success() -> None:
    repo = HealthRepository()
    player_id = uuid.uuid4()
    mock_session = AsyncMock()
    mock_session.execute = AsyncMock()
    mock_session.__aenter__ = AsyncMock(return_value=mock_session)
    mock_session.__aexit__ = AsyncMock(return_value=None)

    with patch(
        "server.persistence.repositories.health_repository.get_session_maker",
        return_value=MagicMock(return_value=mock_session),
    ):
        await repo.update_player_health(player_id, -3, reason="damage:physical")

    mock_session.commit.assert_awaited_once()


@pytest.mark.asyncio
async def test_update_player_health_raises_database_error() -> None:
    repo = HealthRepository()
    mock_session = AsyncMock()
    mock_session.execute = AsyncMock(side_effect=SQLAlchemyError("boom"))
    mock_session.__aenter__ = AsyncMock(return_value=mock_session)
    mock_session.__aexit__ = AsyncMock(return_value=None)

    with patch(
        "server.persistence.repositories.health_repository.get_session_maker",
        return_value=MagicMock(return_value=mock_session),
    ):
        with pytest.raises(DatabaseError):
            await repo.update_player_health(uuid.uuid4(), 1, reason="heal")
