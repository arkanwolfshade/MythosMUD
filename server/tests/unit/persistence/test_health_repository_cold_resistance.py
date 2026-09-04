"""Tests for cold damage resistance in HealthRepository."""

import uuid
from unittest.mock import AsyncMock, MagicMock

import pytest

from server.models.player import Player
from server.persistence.repositories.health_repository import HealthRepository


@pytest.mark.asyncio
async def test_cold_damage_resistance_reduces_damage() -> None:
    """Cold resistance should reduce incoming cold-type damage before persistence."""
    repo = HealthRepository()
    repo.update_player_health = AsyncMock()

    mock_player = MagicMock(spec=Player)
    mock_player.player_id = uuid.uuid4()
    mock_player.name = "TestPlayer"

    stats: dict[str, int] = {
        "current_dp": 100,
        "cold_resistance": 50,
    }
    mock_player.get_stats.return_value = stats

    await repo.damage_player(mock_player, 40, "cold")

    # With 50% resistance, effective damage should be half (rounded), minimum 1
    expected_damage = 20
    assert stats["current_dp"] == 100 - expected_damage
    repo.update_player_health.assert_awaited_once_with(
        mock_player.player_id,
        -expected_damage,
        "damage:cold",
    )


@pytest.mark.asyncio
async def test_damage_defaults_current_dp_to_20_when_missing() -> None:
    """Missing current_dp should use base investigator fallback to avoid inflated health."""
    repo = HealthRepository()
    repo.update_player_health = AsyncMock()

    mock_player = MagicMock(spec=Player)
    mock_player.player_id = uuid.uuid4()
    mock_player.name = "FallbackPlayer"

    stats: dict[str, int] = {}
    mock_player.get_stats.return_value = stats

    await repo.damage_player(mock_player, 5, "physical")

    assert stats["current_dp"] == 15
    repo.update_player_health.assert_awaited_once_with(
        mock_player.player_id,
        -5,
        "damage:physical",
    )
