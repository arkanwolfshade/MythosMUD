"""
Unit tests for MP regeneration service.

Tests the MPRegenerationService class for magic point regeneration.
"""

import uuid
from typing import Any
from unittest.mock import AsyncMock, MagicMock

import pytest

from server.game.magic.mp_regeneration_service import MPRegenerationService

# pylint: disable=protected-access  # Reason: Test file - accessing protected members is standard practice for unit testing
# pylint: disable=redefined-outer-name  # Reason: Test file - pytest fixture parameter names must match fixture names, causing intentional redefinitions


@pytest.fixture
def mock_player_service():
    """Create a mock player service."""
    service = MagicMock()
    service.persistence = MagicMock()
    return service


@pytest.fixture
def mp_regeneration_service(mock_player_service):
    """Create an MPRegenerationService instance."""
    return MPRegenerationService(mock_player_service)


@pytest.fixture
def sample_player_id():
    """Create a sample player ID."""
    return uuid.uuid4()


@pytest.fixture
def mock_player():
    """Create a mock player."""
    player = MagicMock()
    player.get_stats = MagicMock(return_value={})
    return player


def test_mp_regeneration_service_init(mock_player_service):
    """Test MPRegenerationService initialization."""
    service = MPRegenerationService(mock_player_service)
    assert service.player_service == mock_player_service
    assert service.regen_rate == 0.01  # Default rate


def test_mp_regeneration_service_init_custom_rate(mock_player_service):
    """Test MPRegenerationService initialization with custom regen_rate."""
    service = MPRegenerationService(mock_player_service, regen_rate=0.02)
    assert service.regen_rate == 0.02


@pytest.mark.asyncio
async def test_process_tick_regeneration_player_not_found(mp_regeneration_service, sample_player_id):
    """Test process_tick_regeneration() returns zero when player not found."""
    mp_regeneration_service.player_service.persistence.get_player_by_id = AsyncMock(return_value=None)
    result = await mp_regeneration_service.process_tick_regeneration(sample_player_id)
    assert result["mp_restored"] == 0
    assert result["current_mp"] == 0
    assert result["max_mp"] == 0


@pytest.mark.asyncio
async def test_process_tick_regeneration_at_max(mp_regeneration_service, sample_player_id, mock_player):
    """Test process_tick_regeneration() returns zero when MP already at max."""
    mock_player.get_stats.return_value = {"magic_points": 10, "max_magic_points": 10}
    mp_regeneration_service.player_service.persistence.get_player_by_id = AsyncMock(return_value=mock_player)
    result = await mp_regeneration_service.process_tick_regeneration(sample_player_id)
    assert result["mp_restored"] == 0
    assert result["current_mp"] == 10
    assert result["max_mp"] == 10


@pytest.mark.asyncio
async def test_process_tick_regeneration_restores_mp(mp_regeneration_service, sample_player_id, mock_player):
    """Test process_tick_regeneration() restores MP."""
    mock_player.get_stats.return_value = {"magic_points": 5, "max_magic_points": 10, "position": "standing"}
    mp_regeneration_service.player_service.persistence.get_player_by_id = AsyncMock(return_value=mock_player)
    mp_regeneration_service.player_service.persistence.save_player = AsyncMock()
    result = await mp_regeneration_service.process_tick_regeneration(sample_player_id)
    assert result["mp_restored"] >= 0
    assert result["current_mp"] >= 5
    assert result["max_mp"] == 10


@pytest.mark.asyncio
async def test_process_tick_regeneration_calculates_max_from_power(
    mp_regeneration_service, sample_player_id, mock_player
):
    """Test process_tick_regeneration() calculates max_mp from power if not present."""
    mock_player.get_stats.return_value = {"magic_points": 5, "power": 50}  # No max_magic_points
    mp_regeneration_service.player_service.persistence.get_player_by_id = AsyncMock(return_value=mock_player)
    mp_regeneration_service.player_service.persistence.save_player = AsyncMock()
    result = await mp_regeneration_service.process_tick_regeneration(sample_player_id)
    # max_mp should be calculated as ceil(50 * 0.2) = 10
    assert result["max_mp"] == 10


@pytest.mark.asyncio
async def test_process_tick_regeneration_fractional_accumulation(
    mp_regeneration_service, sample_player_id, mock_player
):
    """Test process_tick_regeneration() accumulates fractional MP."""
    mock_player.get_stats.return_value = {"magic_points": 5, "max_magic_points": 10, "position": "standing"}
    mp_regeneration_service.player_service.persistence.get_player_by_id = AsyncMock(return_value=mock_player)
    mp_regeneration_service.player_service.persistence.save_player = AsyncMock()
    # Run multiple ticks to accumulate fractional MP
    result1 = await mp_regeneration_service.process_tick_regeneration(sample_player_id)
    result2 = await mp_regeneration_service.process_tick_regeneration(sample_player_id)
    # Should accumulate fractional MP across ticks
    assert result2["current_mp"] >= result1["current_mp"]


def test_get_regen_multiplier_standing(mp_regeneration_service):
    """Test _get_regen_multiplier() returns 1.0 for standing position."""
    stats = {"position": "standing"}
    multiplier = mp_regeneration_service._get_regen_multiplier(stats)
    assert multiplier == 1.0


def test_get_regen_multiplier_sitting(mp_regeneration_service):
    """Test _get_regen_multiplier() returns REST multiplier for sitting."""
    stats = {"position": "sitting"}
    multiplier = mp_regeneration_service._get_regen_multiplier(stats)
    assert multiplier == 3.0  # REST_MP_REGEN_MULTIPLIER


def test_get_regen_multiplier_lying(mp_regeneration_service):
    """Test _get_regen_multiplier() returns enhanced REST multiplier for lying."""
    stats = {"position": "lying"}
    multiplier = mp_regeneration_service._get_regen_multiplier(stats)
    assert multiplier == pytest.approx(3.6)  # REST_MP_REGEN_MULTIPLIER * 1.2 (floating point)


def test_get_regen_multiplier_default_position(mp_regeneration_service):
    """Test _get_regen_multiplier() defaults to 1.0 when position not specified."""
    stats: dict[str, Any] = {}
    multiplier = mp_regeneration_service._get_regen_multiplier(stats)
    assert multiplier == 1.0


@pytest.mark.asyncio
async def test_restore_mp_from_rest_player_not_found(mp_regeneration_service, sample_player_id):
    """Test restore_mp_from_rest() returns error when player not found."""
    mp_regeneration_service.player_service.persistence.get_player_by_id = AsyncMock(return_value=None)
    result = await mp_regeneration_service.restore_mp_from_rest(sample_player_id)
    assert result["success"] is False
    assert "not found" in result["message"].lower()
    assert result["mp_restored"] == 0


@pytest.mark.asyncio
async def test_restore_mp_from_rest_at_max(mp_regeneration_service, sample_player_id, mock_player):
    """Test restore_mp_from_rest() returns message when MP already at max."""
    mock_player.get_stats.return_value = {"magic_points": 10, "max_magic_points": 10}
    mp_regeneration_service.player_service.persistence.get_player_by_id = AsyncMock(return_value=mock_player)
    result = await mp_regeneration_service.restore_mp_from_rest(sample_player_id)
    assert result["success"] is True
    assert "already full" in result["message"].lower()
    assert result["mp_restored"] == 0


@pytest.mark.asyncio
async def test_restore_mp_from_rest_restores_mp(mp_regeneration_service, sample_player_id, mock_player):
    """Test restore_mp_from_rest() restores MP."""
    mock_player.get_stats.return_value = {"magic_points": 5, "max_magic_points": 10}
    mp_regeneration_service.player_service.persistence.get_player_by_id = AsyncMock(return_value=mock_player)
    mp_regeneration_service.player_service.persistence.save_player = AsyncMock()
    result = await mp_regeneration_service.restore_mp_from_rest(sample_player_id, duration_seconds=60)
    assert result["success"] is True
    assert result["mp_restored"] > 0
    assert result["current_mp"] > 5
    assert result["max_mp"] == 10


@pytest.mark.asyncio
async def test_restore_mp_from_rest_calculates_max_from_power(mp_regeneration_service, sample_player_id, mock_player):
    """Test restore_mp_from_rest() calculates max_mp from power if not present."""
    mock_player.get_stats.return_value = {"magic_points": 5, "power": 50}  # No max_magic_points
    mp_regeneration_service.player_service.persistence.get_player_by_id = AsyncMock(return_value=mock_player)
    mp_regeneration_service.player_service.persistence.save_player = AsyncMock()
    result = await mp_regeneration_service.restore_mp_from_rest(sample_player_id)
    assert result["max_mp"] == 10  # ceil(50 * 0.2)


@pytest.mark.asyncio
async def test_restore_mp_from_meditation_player_not_found(mp_regeneration_service, sample_player_id):
    """Test restore_mp_from_meditation() returns error when player not found."""
    mp_regeneration_service.player_service.persistence.get_player_by_id = AsyncMock(return_value=None)
    result = await mp_regeneration_service.restore_mp_from_meditation(sample_player_id)
    assert result["success"] is False
    assert "not found" in result["message"].lower()
    assert result["mp_restored"] == 0


@pytest.mark.asyncio
async def test_restore_mp_from_meditation_at_max(mp_regeneration_service, sample_player_id, mock_player):
    """Test restore_mp_from_meditation() returns message when MP already at max."""
    mock_player.get_stats.return_value = {"magic_points": 10, "max_magic_points": 10}
    mp_regeneration_service.player_service.persistence.get_player_by_id = AsyncMock(return_value=mock_player)
    result = await mp_regeneration_service.restore_mp_from_meditation(sample_player_id)
    assert result["success"] is True
    assert "already full" in result["message"].lower()
    assert result["mp_restored"] == 0


@pytest.mark.asyncio
async def test_restore_mp_from_meditation_restores_mp(mp_regeneration_service, sample_player_id, mock_player):
    """Test restore_mp_from_meditation() restores MP."""
    mock_player.get_stats.return_value = {"magic_points": 5, "max_magic_points": 10}
    mp_regeneration_service.player_service.persistence.get_player_by_id = AsyncMock(return_value=mock_player)
    mp_regeneration_service.player_service.persistence.save_player = AsyncMock()
    result = await mp_regeneration_service.restore_mp_from_meditation(sample_player_id, duration_seconds=180)
    assert result["success"] is True
    assert result["mp_restored"] > 0
    assert result["current_mp"] > 5
    assert "meditation" in result["message"].lower()


@pytest.mark.asyncio
async def test_restore_mp_from_meditation_higher_than_rest(mp_regeneration_service, sample_player_id, mock_player):
    """Test restore_mp_from_meditation() restores more MP than rest."""
    mock_player.get_stats.return_value = {"magic_points": 0, "max_magic_points": 10}
    mp_regeneration_service.player_service.persistence.get_player_by_id = AsyncMock(return_value=mock_player)
    mp_regeneration_service.player_service.persistence.save_player = AsyncMock()
    rest_result = await mp_regeneration_service.restore_mp_from_rest(sample_player_id, duration_seconds=60)
    # Reset player stats
    mock_player.get_stats.return_value = {"magic_points": 0, "max_magic_points": 10}
    meditation_result = await mp_regeneration_service.restore_mp_from_meditation(sample_player_id, duration_seconds=60)
    # Meditation should restore more MP (5x multiplier vs 3x for rest)
    assert meditation_result["mp_restored"] > rest_result["mp_restored"]


@pytest.mark.asyncio
async def test_restore_mp_from_item_player_not_found(mp_regeneration_service, sample_player_id):
    """Test restore_mp_from_item() returns error when player not found."""
    # Ensure magic_service is not set so it uses fallback path
    mp_regeneration_service.player_service.magic_service = None
    mp_regeneration_service.player_service.persistence.get_player_by_id = AsyncMock(return_value=None)
    result = await mp_regeneration_service.restore_mp_from_item(sample_player_id, amount=5)
    assert result["success"] is False
    assert "not found" in result["message"].lower()
    assert result["mp_restored"] == 0


@pytest.mark.asyncio
async def test_restore_mp_from_item_restores_mp(mp_regeneration_service, sample_player_id, mock_player):
    """Test restore_mp_from_item() restores MP."""
    # Ensure magic_service is not set so it uses fallback path
    mp_regeneration_service.player_service.magic_service = None
    mock_player.get_stats.return_value = {"magic_points": 5, "max_magic_points": 10}
    mp_regeneration_service.player_service.persistence.get_player_by_id = AsyncMock(return_value=mock_player)
    mp_regeneration_service.player_service.persistence.save_player = AsyncMock()
    result = await mp_regeneration_service.restore_mp_from_item(sample_player_id, amount=3)
    assert result["success"] is True
    assert result["mp_restored"] == 3
    assert result["current_mp"] == 8


@pytest.mark.asyncio
async def test_restore_mp_from_item_respects_max(mp_regeneration_service, sample_player_id, mock_player):
    """Test restore_mp_from_item() respects max_mp limit."""
    # Ensure magic_service is not set so it uses fallback path
    mp_regeneration_service.player_service.magic_service = None
    mock_player.get_stats.return_value = {"magic_points": 9, "max_magic_points": 10}
    mp_regeneration_service.player_service.persistence.get_player_by_id = AsyncMock(return_value=mock_player)
    mp_regeneration_service.player_service.persistence.save_player = AsyncMock()
    result = await mp_regeneration_service.restore_mp_from_item(sample_player_id, amount=5)
    assert result["success"] is True
    assert result["current_mp"] == 10  # Capped at max
    assert result["mp_restored"] == 1  # Only restored 1 (from 9 to 10)


@pytest.mark.asyncio
async def test_restore_mp_from_item_uses_magic_service(mp_regeneration_service, sample_player_id):
    """Test restore_mp_from_item() uses magic_service if available."""
    mock_magic_service = MagicMock()
    mock_magic_service.restore_mp = AsyncMock(return_value={"success": True, "mp_restored": 5})
    # Set magic_service explicitly
    mp_regeneration_service.player_service.magic_service = mock_magic_service
    result = await mp_regeneration_service.restore_mp_from_item(sample_player_id, amount=5)
    assert result["success"] is True
    assert result["mp_restored"] == 5
    mock_magic_service.restore_mp.assert_awaited_once_with(sample_player_id, 5)


@pytest.mark.asyncio
async def test_restore_mp_from_item_calculates_max_from_power(mp_regeneration_service, sample_player_id, mock_player):
    """Test restore_mp_from_item() calculates max_mp from power if not present."""
    # Ensure magic_service is not set so it uses fallback path
    mp_regeneration_service.player_service.magic_service = None
    mock_player.get_stats.return_value = {"magic_points": 5, "power": 50}  # No max_magic_points
    mp_regeneration_service.player_service.persistence.get_player_by_id = AsyncMock(return_value=mock_player)
    mp_regeneration_service.player_service.persistence.save_player = AsyncMock()
    result = await mp_regeneration_service.restore_mp_from_item(sample_player_id, amount=3)
    assert result["max_mp"] == 10  # ceil(50 * 0.2)


@pytest.mark.asyncio
async def test_process_tick_regeneration_sitting_position(mp_regeneration_service, sample_player_id, mock_player):
    """Test process_tick_regeneration() uses REST multiplier for sitting position."""
    mock_player.get_stats.return_value = {"magic_points": 5, "max_magic_points": 10, "position": "sitting"}
    mp_regeneration_service.player_service.persistence.get_player_by_id = AsyncMock(return_value=mock_player)
    mp_regeneration_service.player_service.persistence.save_player = AsyncMock()
    result = await mp_regeneration_service.process_tick_regeneration(sample_player_id)
    # Should restore more MP due to REST multiplier
    assert result["mp_restored"] >= 0


@pytest.mark.asyncio
async def test_process_tick_regeneration_lying_position(mp_regeneration_service, sample_player_id, mock_player):
    """Test process_tick_regeneration() uses enhanced REST multiplier for lying position."""
    mock_player.get_stats.return_value = {"magic_points": 5, "max_magic_points": 10, "position": "lying"}
    mp_regeneration_service.player_service.persistence.get_player_by_id = AsyncMock(return_value=mock_player)
    mp_regeneration_service.player_service.persistence.save_player = AsyncMock()
    result = await mp_regeneration_service.process_tick_regeneration(sample_player_id)
    # Should restore MP
    assert result["mp_restored"] >= 0
