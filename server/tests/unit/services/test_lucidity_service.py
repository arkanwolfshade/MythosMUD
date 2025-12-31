"""
Unit tests for lucidity service.
"""

import uuid
from unittest.mock import AsyncMock, MagicMock

import pytest

from server.models.lucidity import PlayerLucidity
from server.services.lucidity_service import LucidityService


@pytest.fixture
def mock_session():
    """Create a mock async session."""
    session = MagicMock()
    session.flush = AsyncMock()
    return session


@pytest.fixture
def mock_lucidity_record():
    """Create a mock lucidity record."""
    record = PlayerLucidity(
        player_id=uuid.uuid4(),
        current_lcd=50,
        current_tier="uneasy",
    )
    return record


@pytest.mark.asyncio
async def test_apply_lucidity_adjustment_positive_delta(mock_session, mock_lucidity_record):
    """Test applying positive lucidity adjustment."""
    service = LucidityService(mock_session)

    # Mock repository
    service._repo.get_or_create_player_lucidity = AsyncMock(return_value=mock_lucidity_record)
    service._repo.add_adjustment_log = AsyncMock()

    player_id = uuid.uuid4()
    result = await service.apply_lucidity_adjustment(
        player_id=player_id,
        delta=10,
        reason_code="test_positive",
    )

    assert result.previous_lcd == 50
    assert result.new_lcd == 60
    assert result.previous_tier == "uneasy"


@pytest.mark.asyncio
async def test_apply_lucidity_adjustment_negative_delta(mock_session, mock_lucidity_record):
    """Test applying negative lucidity adjustment."""
    service = LucidityService(mock_session)

    # Mock repository
    service._repo.get_or_create_player_lucidity = AsyncMock(return_value=mock_lucidity_record)
    service._repo.add_adjustment_log = AsyncMock()

    player_id = uuid.uuid4()
    result = await service.apply_lucidity_adjustment(
        player_id=player_id,
        delta=-20,
        reason_code="test_negative",
    )

    assert result.previous_lcd == 50
    assert result.new_lcd == 30
    assert result.previous_tier == "uneasy"


@pytest.mark.asyncio
async def test_apply_lucidity_adjustment_clamps_to_max(mock_session, mock_lucidity_record):
    """Test that lucidity adjustment clamps to maximum value."""
    # Set record to near max
    mock_lucidity_record.current_lcd = 95

    service = LucidityService(mock_session)
    service._repo.get_or_create_player_lucidity = AsyncMock(return_value=mock_lucidity_record)
    service._repo.add_adjustment_log = AsyncMock()

    player_id = uuid.uuid4()
    result = await service.apply_lucidity_adjustment(
        player_id=player_id,
        delta=20,  # Would exceed max
        reason_code="test_clamp",
    )

    # Should be clamped to 100
    assert result.new_lcd == 100


@pytest.mark.asyncio
async def test_apply_lucidity_adjustment_clamps_to_min(mock_session, mock_lucidity_record):
    """Test that lucidity adjustment clamps to minimum value."""
    # Set record to near min
    mock_lucidity_record.current_lcd = -95

    service = LucidityService(mock_session)
    service._repo.get_or_create_player_lucidity = AsyncMock(return_value=mock_lucidity_record)
    service._repo.add_adjustment_log = AsyncMock()

    player_id = uuid.uuid4()
    result = await service.apply_lucidity_adjustment(
        player_id=player_id,
        delta=-20,  # Would exceed min
        reason_code="test_clamp",
    )

    # Should be clamped to -100
    assert result.new_lcd == -100
