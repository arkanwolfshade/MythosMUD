"""
Unit tests for lucidity service.
"""

import uuid
from datetime import UTC, datetime
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.models.lucidity import PlayerLucidity
from server.services.lucidity_helpers import LIABILITY_CATALOG, encode_liabilities
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
    # Reason: Standard test mocking practice - replacing method with AsyncMock for testing
    service._repo.get_or_create_player_lucidity = AsyncMock(return_value=mock_lucidity_record)  # type: ignore[method-assign]
    service._repo.add_adjustment_log = AsyncMock()  # type: ignore[method-assign]

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
    service._repo.get_or_create_player_lucidity = AsyncMock(return_value=mock_lucidity_record)  # type: ignore[method-assign]
    service._repo.add_adjustment_log = AsyncMock()  # type: ignore[method-assign]

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
    service._repo.get_or_create_player_lucidity = AsyncMock(return_value=mock_lucidity_record)  # type: ignore[method-assign]
    service._repo.add_adjustment_log = AsyncMock()  # type: ignore[method-assign]

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
    service._repo.get_or_create_player_lucidity = AsyncMock(return_value=mock_lucidity_record)  # type: ignore[method-assign]
    service._repo.add_adjustment_log = AsyncMock()  # type: ignore[method-assign]

    player_id = uuid.uuid4()
    result = await service.apply_lucidity_adjustment(
        player_id=player_id,
        delta=-20,  # Would exceed min
        reason_code="test_clamp",
    )

    # Should be clamped to -100
    assert result.new_lcd == -100


@pytest.mark.asyncio
async def test_add_liability_new_entry(mock_session, mock_lucidity_record):
    """Test adding a new liability code."""
    service = LucidityService(mock_session)
    service._repo.get_or_create_player_lucidity = AsyncMock(return_value=mock_lucidity_record)  # type: ignore[method-assign]
    player_id = mock_lucidity_record.player_id
    code = await service.add_liability(player_id, "night_frayed_reflexes")
    assert code == "night_frayed_reflexes"
    mock_session.flush.assert_awaited()


@pytest.mark.asyncio
async def test_add_liability_increments_stack(mock_session, mock_lucidity_record):
    """Test stacking an existing liability."""
    mock_lucidity_record.liabilities = encode_liabilities([{"code": "night_frayed_reflexes", "stacks": 1}])
    service = LucidityService(mock_session)
    service._repo.get_or_create_player_lucidity = AsyncMock(return_value=mock_lucidity_record)  # type: ignore[method-assign]
    code = await service.add_liability(mock_lucidity_record.player_id, "night_frayed_reflexes")
    assert code == "night_frayed_reflexes"


@pytest.mark.asyncio
async def test_clear_liability_remove_all(mock_session, mock_lucidity_record):
    """Test clearing all stacks of a liability."""
    mock_lucidity_record.liabilities = encode_liabilities([{"code": "ethereal_chill", "stacks": 2}])
    service = LucidityService(mock_session)
    service._repo.get_or_create_player_lucidity = AsyncMock(return_value=mock_lucidity_record)  # type: ignore[method-assign]
    changed = await service.clear_liability(mock_lucidity_record.player_id, "ethereal_chill", remove_all=True)
    assert changed is True


@pytest.mark.asyncio
async def test_clear_liability_decrements_stack(mock_session, mock_lucidity_record):
    """Test decrementing liability stacks."""
    mock_lucidity_record.liabilities = encode_liabilities([{"code": "ethereal_chill", "stacks": 2}])
    service = LucidityService(mock_session)
    service._repo.get_or_create_player_lucidity = AsyncMock(return_value=mock_lucidity_record)  # type: ignore[method-assign]
    changed = await service.clear_liability(mock_lucidity_record.player_id, "ethereal_chill")
    assert changed is True


@pytest.mark.asyncio
async def test_get_player_lucidity_delegates(mock_session, mock_lucidity_record):
    """Test get_player_lucidity delegates to repository."""
    service = LucidityService(mock_session)
    service._repo.get_or_create_player_lucidity = AsyncMock(return_value=mock_lucidity_record)  # type: ignore[method-assign]
    record = await service.get_player_lucidity(mock_lucidity_record.player_id)
    assert record is mock_lucidity_record


@pytest.mark.asyncio
async def test_increment_exposure_state_delegates(mock_session):
    """Test increment_exposure_state delegates to repository."""
    service = LucidityService(mock_session)
    expected = MagicMock()
    service._repo.increment_exposure_state = AsyncMock(return_value=expected)  # type: ignore[method-assign]
    player_id = uuid.uuid4()
    result = await service.increment_exposure_state(player_id, "deep_one")
    assert result is expected


@pytest.mark.asyncio
async def test_cooldown_get_and_set(mock_session):
    """Test cooldown get/set delegates to repository."""
    service = LucidityService(mock_session)
    player_id = uuid.uuid4()
    expires = datetime(1926, 1, 1, tzinfo=UTC)
    cooldown = MagicMock()
    service._repo.get_cooldown = AsyncMock(return_value=cooldown)  # type: ignore[method-assign]
    service._repo.set_cooldown = AsyncMock(return_value=cooldown)  # type: ignore[method-assign]
    assert await service.get_cooldown(player_id, "rest") is cooldown
    assert await service.set_cooldown(player_id, "rest", expires) is cooldown


@pytest.mark.asyncio
async def test_clear_hallucination_timers(mock_session):
    """Test clearing hallucination timer cooldowns."""
    service = LucidityService(mock_session)
    service._repo.delete_cooldowns_by_action_code_pattern = AsyncMock(return_value=2)  # type: ignore[method-assign]
    count = await service.clear_hallucination_timers(uuid.uuid4())
    assert count == 2


@pytest.mark.asyncio
async def test_apply_lucidity_adjustment_adds_liability_on_large_drop(mock_session, mock_lucidity_record):
    """Large negative delta triggers liability addition."""
    service = LucidityService(
        mock_session,
        liability_picker=lambda *_args: "night_frayed_reflexes",
    )
    service._repo.get_or_create_player_lucidity = AsyncMock(return_value=mock_lucidity_record)  # type: ignore[method-assign]
    service._repo.add_adjustment_log = AsyncMock()  # type: ignore[method-assign]
    with patch("server.services.lucidity_service.send_lucidity_change_event", new=AsyncMock()):
        result = await service.apply_lucidity_adjustment(
            player_id=mock_lucidity_record.player_id,
            delta=-20,
            reason_code="shock",
        )
    assert "night_frayed_reflexes" in result.liabilities_added


def test_max_lcd_from_stats():
    """Test max LCD calculation from stats dict."""
    assert LucidityService._max_lcd_from_stats({"education": 80}) == 80
    assert LucidityService._max_lcd_from_stats({"max_lucidity": 90}) == 90
    assert LucidityService._max_lcd_from_stats({}) == 100


def test_default_liability_picker(mock_session):
    """Default picker returns first catalog entry when none applied."""
    service = LucidityService(mock_session)
    code = service._default_liability_picker(str(uuid.uuid4()), 50, 30, "test")
    assert code in LIABILITY_CATALOG
