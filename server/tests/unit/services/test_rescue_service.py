"""
Unit tests for rescue service.

Tests the RescueService class for performing rescue operations.
"""

import uuid
from unittest.mock import AsyncMock, MagicMock

import pytest

from server.models.lucidity import PlayerLucidity
from server.services.rescue_service import RescueService


@pytest.fixture
def mock_persistence():
    """Create a mock persistence layer."""
    return MagicMock()


@pytest.fixture
def mock_session():
    """Create a mock async session."""
    session = MagicMock()
    session.get = AsyncMock()
    session.commit = AsyncMock()
    session.rollback = AsyncMock()
    return session


@pytest.fixture
def async_session_factory(mock_session):
    """Create an async session factory."""

    async def factory():
        yield mock_session

    return factory


@pytest.fixture
def mock_lucidity_service():
    """Create a mock lucidity service."""
    service = MagicMock()
    service.apply_lucidity_adjustment = AsyncMock()
    return service


@pytest.fixture
def lucidity_service_factory(mock_lucidity_service):
    """Create a lucidity service factory."""

    def factory(session):
        return mock_lucidity_service

    return factory


@pytest.fixture
def mock_event_dispatcher():
    """Create a mock event dispatcher."""
    return AsyncMock()


@pytest.fixture
def rescue_service(mock_persistence, async_session_factory, lucidity_service_factory, mock_event_dispatcher):
    """Create a RescueService instance."""
    return RescueService(
        persistence=mock_persistence,
        session_factory=async_session_factory,
        lucidity_service_factory=lucidity_service_factory,
        event_dispatcher=mock_event_dispatcher,
    )


@pytest.fixture
def sample_rescuer():
    """Create a sample rescuer player."""
    player = MagicMock()
    player.player_id = uuid.uuid4()
    player.current_room_id = uuid.uuid4()
    return player


@pytest.fixture
def sample_target():
    """Create a sample target player."""
    player = MagicMock()
    player.player_id = uuid.uuid4()
    player.current_room_id = uuid.uuid4()
    return player


@pytest.fixture
def sample_lucidity_record():
    """Create a sample lucidity record."""
    record = MagicMock(spec=PlayerLucidity)
    record.current_tier = "catatonic"
    record.current_lcd = 0.0
    return record


@pytest.mark.asyncio
async def test_rescue_no_persistence(async_session_factory, lucidity_service_factory, mock_event_dispatcher):
    """Test rescue() returns error when persistence is not available."""
    service = RescueService(
        persistence=None,
        session_factory=async_session_factory,
        lucidity_service_factory=lucidity_service_factory,
        event_dispatcher=mock_event_dispatcher,
    )
    result = await service.rescue("target", {"username": "rescuer"})
    assert "not available" in result["result"]


@pytest.mark.asyncio
async def test_rescue_rescuer_not_found(rescue_service, mock_persistence):
    """Test rescue() returns error when rescuer is not found."""
    mock_persistence.get_player_by_name = AsyncMock(return_value=None)
    result = await rescue_service.rescue("target", {"username": "rescuer"})
    assert "Unable to identify rescuer" in result["result"]


@pytest.mark.asyncio
async def test_rescue_target_not_found(rescue_service, mock_persistence, sample_rescuer):
    """Test rescue() returns error when target is not found."""
    mock_persistence.get_player_by_name = AsyncMock(side_effect=[sample_rescuer, None])
    result = await rescue_service.rescue("target", {"username": "rescuer"})
    assert "Could not find" in result["result"]


@pytest.mark.asyncio
async def test_rescue_different_rooms(rescue_service, mock_persistence, sample_rescuer, sample_target):
    """Test rescue() returns error when rescuer and target are in different rooms."""
    sample_rescuer.current_room_id = uuid.uuid4()
    sample_target.current_room_id = uuid.uuid4()  # Different room
    mock_persistence.get_player_by_name = AsyncMock(side_effect=[sample_rescuer, sample_target])
    result = await rescue_service.rescue("target", {"username": "rescuer"})
    assert "not within reach" in result["result"]


@pytest.mark.asyncio
async def test_rescue_lucidity_record_not_found(
    rescue_service, mock_persistence, mock_session, sample_rescuer, sample_target
):
    """Test rescue() returns error when lucidity record is not found."""
    sample_rescuer.current_room_id = uuid.uuid4()
    sample_target.current_room_id = sample_rescuer.current_room_id  # Same room
    mock_persistence.get_player_by_name = AsyncMock(side_effect=[sample_rescuer, sample_target])
    mock_session.get = AsyncMock(return_value=None)
    result = await rescue_service.rescue("target", {"username": "rescuer"})
    assert "lucidity record could not be found" in result["result"]


@pytest.mark.asyncio
async def test_rescue_not_catatonic(
    rescue_service, mock_persistence, mock_session, sample_rescuer, sample_target, sample_lucidity_record
):
    """Test rescue() returns error when target is not catatonic."""
    sample_rescuer.current_room_id = uuid.uuid4()
    sample_target.current_room_id = sample_rescuer.current_room_id  # Same room
    sample_lucidity_record.current_tier = "stable"  # Not catatonic
    mock_persistence.get_player_by_name = AsyncMock(side_effect=[sample_rescuer, sample_target])
    mock_session.get = AsyncMock(return_value=sample_lucidity_record)
    result = await rescue_service.rescue("target", {"username": "rescuer"})
    assert "isn't catatonic" in result["result"]


@pytest.mark.asyncio
async def test_rescue_success(
    rescue_service,
    mock_persistence,
    mock_session,
    mock_lucidity_service,
    mock_event_dispatcher,
    sample_rescuer,
    sample_target,
    sample_lucidity_record,
):
    """Test rescue() successfully rescues target."""
    sample_rescuer.current_room_id = uuid.uuid4()
    sample_target.current_room_id = sample_rescuer.current_room_id  # Same room
    sample_lucidity_record.current_tier = "catatonic"
    sample_lucidity_record.current_lcd = 0.0
    mock_persistence.get_player_by_name = AsyncMock(side_effect=[sample_rescuer, sample_target])
    mock_session.get = AsyncMock(return_value=sample_lucidity_record)
    mock_result = MagicMock()
    mock_result.new_lcd = 1.0
    mock_lucidity_service.apply_lucidity_adjustment = AsyncMock(return_value=mock_result)
    result = await rescue_service.rescue("target", {"username": "rescuer"})
    assert "rushes to rescue" in result["result"]
    assert result["new_lcd"] == 1.0
    mock_lucidity_service.apply_lucidity_adjustment.assert_awaited_once()
    mock_event_dispatcher.assert_awaited()


@pytest.mark.asyncio
async def test_rescue_with_player_name(
    rescue_service,
    mock_persistence,
    mock_session,
    mock_lucidity_service,
    sample_rescuer,
    sample_target,
    sample_lucidity_record,
):
    """Test rescue() uses provided player_name instead of current_user."""
    sample_rescuer.current_room_id = uuid.uuid4()
    sample_target.current_room_id = sample_rescuer.current_room_id
    sample_lucidity_record.current_tier = "catatonic"
    sample_lucidity_record.current_lcd = 0.0
    mock_persistence.get_player_by_name = AsyncMock(side_effect=[sample_rescuer, sample_target])
    mock_session.get = AsyncMock(return_value=sample_lucidity_record)
    mock_result = MagicMock()
    mock_result.new_lcd = 1.0
    mock_lucidity_service.apply_lucidity_adjustment = AsyncMock(return_value=mock_result)
    result = await rescue_service.rescue("target", {}, player_name="CustomRescuer")
    assert "CustomRescuer" in result["result"]
    mock_persistence.get_player_by_name.assert_any_call("CustomRescuer")


@pytest.mark.asyncio
async def test_rescue_delta_calculation(
    rescue_service,
    mock_persistence,
    mock_session,
    mock_lucidity_service,
    sample_rescuer,
    sample_target,
    sample_lucidity_record,
):
    """Test rescue() calculates delta correctly."""
    sample_rescuer.current_room_id = uuid.uuid4()
    sample_target.current_room_id = sample_rescuer.current_room_id
    sample_lucidity_record.current_tier = "catatonic"
    sample_lucidity_record.current_lcd = 0.5  # Half lucidity
    mock_persistence.get_player_by_name = AsyncMock(side_effect=[sample_rescuer, sample_target])
    mock_session.get = AsyncMock(return_value=sample_lucidity_record)
    mock_result = MagicMock()
    mock_result.new_lcd = 1.0
    mock_lucidity_service.apply_lucidity_adjustment = AsyncMock(return_value=mock_result)
    await rescue_service.rescue("target", {"username": "rescuer"})
    # Delta should be 1 - 0.5 = 0.5
    call_args = mock_lucidity_service.apply_lucidity_adjustment.call_args
    assert call_args[0][1] == 0.5  # delta argument


@pytest.mark.asyncio
async def test_rescue_delta_zero_or_negative(
    rescue_service,
    mock_persistence,
    mock_session,
    mock_lucidity_service,
    sample_rescuer,
    sample_target,
    sample_lucidity_record,
):
    """Test rescue() sets delta to 1 when delta is zero or negative."""
    sample_rescuer.current_room_id = uuid.uuid4()
    sample_target.current_room_id = sample_rescuer.current_room_id
    sample_lucidity_record.current_tier = "catatonic"
    sample_lucidity_record.current_lcd = 1.0  # Already at max
    mock_persistence.get_player_by_name = AsyncMock(side_effect=[sample_rescuer, sample_target])
    mock_session.get = AsyncMock(return_value=sample_lucidity_record)
    mock_result = MagicMock()
    mock_result.new_lcd = 1.0
    mock_lucidity_service.apply_lucidity_adjustment = AsyncMock(return_value=mock_result)
    await rescue_service.rescue("target", {"username": "rescuer"})
    # Delta should be set to 1 when calculated delta <= 0
    call_args = mock_lucidity_service.apply_lucidity_adjustment.call_args
    assert call_args[0][1] == 1  # delta should be 1


@pytest.mark.asyncio
async def test_rescue_apply_lucidity_error(
    rescue_service,
    mock_persistence,
    mock_session,
    mock_lucidity_service,
    sample_rescuer,
    sample_target,
    sample_lucidity_record,
):
    """Test rescue() handles errors during lucidity adjustment."""
    sample_rescuer.current_room_id = uuid.uuid4()
    sample_target.current_room_id = sample_rescuer.current_room_id
    sample_lucidity_record.current_tier = "catatonic"
    sample_lucidity_record.current_lcd = 0.0
    mock_persistence.get_player_by_name = AsyncMock(side_effect=[sample_rescuer, sample_target])
    mock_session.get = AsyncMock(return_value=sample_lucidity_record)
    mock_lucidity_service.apply_lucidity_adjustment = AsyncMock(side_effect=Exception("Database error"))
    result = await rescue_service.rescue("target", {"username": "rescuer"})
    assert "unexpected error" in result["result"]
    mock_session.rollback.assert_awaited_once()


@pytest.mark.asyncio
async def test_rescue_event_dispatcher_error(
    rescue_service,
    mock_persistence,
    mock_session,
    mock_lucidity_service,
    mock_event_dispatcher,
    sample_rescuer,
    sample_target,
    sample_lucidity_record,
):
    """Test rescue() handles event dispatcher errors gracefully."""
    sample_rescuer.current_room_id = uuid.uuid4()
    sample_target.current_room_id = sample_rescuer.current_room_id
    sample_lucidity_record.current_tier = "catatonic"
    sample_lucidity_record.current_lcd = 0.0
    mock_persistence.get_player_by_name = AsyncMock(side_effect=[sample_rescuer, sample_target])
    mock_session.get = AsyncMock(return_value=sample_lucidity_record)
    mock_result = MagicMock()
    mock_result.new_lcd = 1.0
    mock_lucidity_service.apply_lucidity_adjustment = AsyncMock(return_value=mock_result)
    mock_event_dispatcher.side_effect = Exception("Event error")
    # Should not raise, should handle gracefully
    result = await rescue_service.rescue("target", {"username": "rescuer"})
    assert "rushes to rescue" in result["result"]


@pytest.mark.asyncio
async def test_rescue_metadata_includes_rescuer(
    rescue_service,
    mock_persistence,
    mock_session,
    mock_lucidity_service,
    sample_rescuer,
    sample_target,
    sample_lucidity_record,
):
    """Test rescue() includes rescuer in metadata."""
    sample_rescuer.current_room_id = uuid.uuid4()
    sample_target.current_room_id = sample_rescuer.current_room_id
    sample_lucidity_record.current_tier = "catatonic"
    sample_lucidity_record.current_lcd = 0.0
    mock_persistence.get_player_by_name = AsyncMock(side_effect=[sample_rescuer, sample_target])
    mock_session.get = AsyncMock(return_value=sample_lucidity_record)
    mock_result = MagicMock()
    mock_result.new_lcd = 1.0
    mock_lucidity_service.apply_lucidity_adjustment = AsyncMock(return_value=mock_result)
    await rescue_service.rescue("target", {"username": "rescuer"})
    call_args = mock_lucidity_service.apply_lucidity_adjustment.call_args
    metadata = call_args[1]["metadata"]
    assert metadata["rescuer"] == "rescuer"
    assert metadata["source"] == "rescue_command"


@pytest.mark.asyncio
async def test_rescue_metadata_includes_location(
    rescue_service,
    mock_persistence,
    mock_session,
    mock_lucidity_service,
    sample_rescuer,
    sample_target,
    sample_lucidity_record,
):
    """Test rescue() includes location_id in lucidity adjustment."""
    room_id = uuid.uuid4()
    sample_rescuer.current_room_id = room_id
    sample_target.current_room_id = room_id
    sample_lucidity_record.current_tier = "catatonic"
    sample_lucidity_record.current_lcd = 0.0
    mock_persistence.get_player_by_name = AsyncMock(side_effect=[sample_rescuer, sample_target])
    mock_session.get = AsyncMock(return_value=sample_lucidity_record)
    mock_result = MagicMock()
    mock_result.new_lcd = 1.0
    mock_lucidity_service.apply_lucidity_adjustment = AsyncMock(return_value=mock_result)
    await rescue_service.rescue("target", {"username": "rescuer"})
    call_args = mock_lucidity_service.apply_lucidity_adjustment.call_args
    assert call_args[1]["location_id"] == str(room_id)


@pytest.mark.asyncio
async def test_rescue_dispatches_events_for_both_players(
    rescue_service,
    mock_persistence,
    mock_session,
    mock_lucidity_service,
    mock_event_dispatcher,
    sample_rescuer,
    sample_target,
    sample_lucidity_record,
):
    """Test rescue() dispatches events for both target and rescuer."""
    sample_rescuer.current_room_id = uuid.uuid4()
    sample_target.current_room_id = sample_rescuer.current_room_id
    sample_lucidity_record.current_tier = "catatonic"
    sample_lucidity_record.current_lcd = 0.0
    mock_persistence.get_player_by_name = AsyncMock(side_effect=[sample_rescuer, sample_target])
    mock_session.get = AsyncMock(return_value=sample_lucidity_record)
    mock_result = MagicMock()
    mock_result.new_lcd = 1.0
    mock_lucidity_service.apply_lucidity_adjustment = AsyncMock(return_value=mock_result)
    await rescue_service.rescue("target", {"username": "rescuer"})
    # Should dispatch events for both players
    assert mock_event_dispatcher.await_count >= 2


@pytest.mark.asyncio
async def test_rescue_handles_uuid_strings(
    rescue_service,
    mock_persistence,
    mock_session,
    mock_lucidity_service,
    sample_rescuer,
    sample_target,
    sample_lucidity_record,
):
    """Test rescue() handles player_id as UUID strings."""
    sample_rescuer.player_id = str(uuid.uuid4())  # String UUID
    sample_target.player_id = str(uuid.uuid4())  # String UUID
    sample_rescuer.current_room_id = uuid.uuid4()
    sample_target.current_room_id = sample_rescuer.current_room_id
    sample_lucidity_record.current_tier = "catatonic"
    sample_lucidity_record.current_lcd = 0.0
    mock_persistence.get_player_by_name = AsyncMock(side_effect=[sample_rescuer, sample_target])
    mock_session.get = AsyncMock(return_value=sample_lucidity_record)
    mock_result = MagicMock()
    mock_result.new_lcd = 1.0
    mock_lucidity_service.apply_lucidity_adjustment = AsyncMock(return_value=mock_result)
    result = await rescue_service.rescue("target", {"username": "rescuer"})
    assert "rushes to rescue" in result["result"]


@pytest.mark.asyncio
async def test_rescue_handles_uuid_objects(
    rescue_service,
    mock_persistence,
    mock_session,
    mock_lucidity_service,
    sample_rescuer,
    sample_target,
    sample_lucidity_record,
):
    """Test rescue() handles player_id as UUID objects."""
    sample_rescuer.player_id = uuid.uuid4()  # UUID object
    sample_target.player_id = uuid.uuid4()  # UUID object
    sample_rescuer.current_room_id = uuid.uuid4()
    sample_target.current_room_id = sample_rescuer.current_room_id
    sample_lucidity_record.current_tier = "catatonic"
    sample_lucidity_record.current_lcd = 0.0
    mock_persistence.get_player_by_name = AsyncMock(side_effect=[sample_rescuer, sample_target])
    mock_session.get = AsyncMock(return_value=sample_lucidity_record)
    mock_result = MagicMock()
    mock_result.new_lcd = 1.0
    mock_lucidity_service.apply_lucidity_adjustment = AsyncMock(return_value=mock_result)
    result = await rescue_service.rescue("target", {"username": "rescuer"})
    assert "rushes to rescue" in result["result"]
