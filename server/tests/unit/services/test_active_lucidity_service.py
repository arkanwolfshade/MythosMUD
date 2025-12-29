"""
Unit tests for active lucidity service.

Tests the ActiveLucidityService class for encounter lucidity loss and recovery actions.
"""

import uuid
from datetime import UTC, datetime, timedelta
from unittest.mock import AsyncMock, MagicMock

import pytest

from server.services.active_lucidity_service import (
    ActiveLucidityService,
    LucidityActionOnCooldownError,
    UnknownEncounterCategoryError,
    UnknownLucidityActionError,
)


@pytest.fixture
def mock_session():
    """Create a mock async session."""
    return AsyncMock()


@pytest.fixture
def active_lucidity_service(mock_session):
    """Create an ActiveLucidityService instance."""
    return ActiveLucidityService(mock_session)


@pytest.fixture
def sample_player_id():
    """Create a sample player ID."""
    return uuid.uuid4()


@pytest.mark.asyncio
async def test_active_lucidity_service_init(mock_session):
    """Test ActiveLucidityService initialization."""
    service = ActiveLucidityService(mock_session)
    assert service._session == mock_session
    assert service._lucidity_service is not None
    assert service._now_provider is not None


@pytest.mark.asyncio
async def test_active_lucidity_service_init_with_now_provider(mock_session):
    """Test ActiveLucidityService initialization with custom now_provider."""
    custom_now = datetime(2024, 1, 1, tzinfo=UTC)

    def now_provider():
        return custom_now

    service = ActiveLucidityService(mock_session, now_provider=now_provider)
    assert service._now_provider() == custom_now


@pytest.mark.asyncio
async def test_apply_encounter_lucidity_loss_first_encounter(active_lucidity_service, sample_player_id):
    """Test apply_encounter_lucidity_loss() for first encounter."""
    mock_result = MagicMock()
    mock_result.new_lcd = 94
    active_lucidity_service._lucidity_service.increment_exposure_state = AsyncMock()
    mock_exposure = MagicMock()
    mock_exposure.encounter_count = 1
    active_lucidity_service._lucidity_service.increment_exposure_state.return_value = mock_exposure
    active_lucidity_service._lucidity_service.apply_lucidity_adjustment = AsyncMock(return_value=mock_result)

    result = await active_lucidity_service.apply_encounter_lucidity_loss(
        sample_player_id, "eldritch_horror", category="disturbing"
    )

    assert result == mock_result
    # First encounter should use first_time delta (-6 for disturbing)
    call_args = active_lucidity_service._lucidity_service.apply_lucidity_adjustment.call_args
    assert call_args[0][1] == -6  # first_time delta


@pytest.mark.asyncio
async def test_apply_encounter_lucidity_loss_repeat_encounter(active_lucidity_service, sample_player_id):
    """Test apply_encounter_lucidity_loss() for repeat encounter."""
    mock_result = MagicMock()
    mock_result.new_lcd = 92
    mock_exposure = MagicMock()
    mock_exposure.encounter_count = 2  # Repeat encounter
    active_lucidity_service._lucidity_service.increment_exposure_state = AsyncMock(return_value=mock_exposure)
    active_lucidity_service._lucidity_service.apply_lucidity_adjustment = AsyncMock(return_value=mock_result)

    result = await active_lucidity_service.apply_encounter_lucidity_loss(
        sample_player_id, "eldritch_horror", category="disturbing"
    )

    assert result == mock_result
    # Repeat encounter should use repeat delta (-2 for disturbing)
    call_args = active_lucidity_service._lucidity_service.apply_lucidity_adjustment.call_args
    assert call_args[0][1] == -2  # repeat delta


@pytest.mark.asyncio
async def test_apply_encounter_lucidity_loss_acclimated(active_lucidity_service, sample_player_id):
    """Test apply_encounter_lucidity_loss() for acclimated encounter."""
    mock_result = MagicMock()
    mock_result.new_lcd = 95
    mock_exposure = MagicMock()
    mock_exposure.encounter_count = 6  # At threshold
    active_lucidity_service._lucidity_service.increment_exposure_state = AsyncMock(return_value=mock_exposure)
    active_lucidity_service._lucidity_service.apply_lucidity_adjustment = AsyncMock(return_value=mock_result)

    result = await active_lucidity_service.apply_encounter_lucidity_loss(
        sample_player_id, "eldritch_horror", category="disturbing"
    )

    assert result == mock_result
    # Acclimated encounter should use half of repeat delta (-2/2 = -1 for disturbing)
    call_args = active_lucidity_service._lucidity_service.apply_lucidity_adjustment.call_args
    assert call_args[0][1] == -1  # half of repeat delta


@pytest.mark.asyncio
async def test_apply_encounter_lucidity_loss_unknown_category(active_lucidity_service, sample_player_id):
    """Test apply_encounter_lucidity_loss() raises error for unknown category."""
    with pytest.raises(UnknownEncounterCategoryError):
        await active_lucidity_service.apply_encounter_lucidity_loss(
            sample_player_id, "eldritch_horror", category="unknown_category"
        )


@pytest.mark.asyncio
async def test_apply_encounter_lucidity_loss_string_player_id(active_lucidity_service):
    """Test apply_encounter_lucidity_loss() handles string player_id."""
    player_id_str = str(uuid.uuid4())
    mock_result = MagicMock()
    mock_exposure = MagicMock()
    mock_exposure.encounter_count = 1
    active_lucidity_service._lucidity_service.increment_exposure_state = AsyncMock(return_value=mock_exposure)
    active_lucidity_service._lucidity_service.apply_lucidity_adjustment = AsyncMock(return_value=mock_result)

    result = await active_lucidity_service.apply_encounter_lucidity_loss(
        player_id_str, "eldritch_horror", category="disturbing"
    )

    assert result == mock_result
    # Should convert string to UUID
    call_args = active_lucidity_service._lucidity_service.apply_lucidity_adjustment.call_args
    assert isinstance(call_args[0][0], uuid.UUID)


@pytest.mark.asyncio
async def test_apply_encounter_lucidity_loss_invalid_string_player_id(active_lucidity_service):
    """Test apply_encounter_lucidity_loss() raises error for invalid string player_id."""
    with pytest.raises(ValueError, match="Invalid player_id format"):
        await active_lucidity_service.apply_encounter_lucidity_loss(
            "invalid-uuid", "eldritch_horror", category="disturbing"
        )


@pytest.mark.asyncio
async def test_apply_encounter_lucidity_loss_horrific_category(active_lucidity_service, sample_player_id):
    """Test apply_encounter_lucidity_loss() with horrific category."""
    mock_result = MagicMock()
    mock_exposure = MagicMock()
    mock_exposure.encounter_count = 1
    active_lucidity_service._lucidity_service.increment_exposure_state = AsyncMock(return_value=mock_exposure)
    active_lucidity_service._lucidity_service.apply_lucidity_adjustment = AsyncMock(return_value=mock_result)

    result = await active_lucidity_service.apply_encounter_lucidity_loss(
        sample_player_id, "eldritch_horror", category="horrific"
    )

    assert result == mock_result
    # Horrific first_time is -12
    call_args = active_lucidity_service._lucidity_service.apply_lucidity_adjustment.call_args
    assert call_args[0][1] == -12


@pytest.mark.asyncio
async def test_apply_encounter_lucidity_loss_cosmic_category(active_lucidity_service, sample_player_id):
    """Test apply_encounter_lucidity_loss() with cosmic category."""
    mock_result = MagicMock()
    mock_exposure = MagicMock()
    mock_exposure.encounter_count = 1
    active_lucidity_service._lucidity_service.increment_exposure_state = AsyncMock(return_value=mock_exposure)
    active_lucidity_service._lucidity_service.apply_lucidity_adjustment = AsyncMock(return_value=mock_result)

    result = await active_lucidity_service.apply_encounter_lucidity_loss(
        sample_player_id, "eldritch_horror", category="cosmic"
    )

    assert result == mock_result
    # Cosmic first_time is -20
    call_args = active_lucidity_service._lucidity_service.apply_lucidity_adjustment.call_args
    assert call_args[0][1] == -20


@pytest.mark.asyncio
async def test_apply_encounter_lucidity_loss_with_location(active_lucidity_service, sample_player_id):
    """Test apply_encounter_lucidity_loss() includes location_id in metadata."""
    mock_result = MagicMock()
    mock_exposure = MagicMock()
    mock_exposure.encounter_count = 1
    active_lucidity_service._lucidity_service.increment_exposure_state = AsyncMock(return_value=mock_exposure)
    active_lucidity_service._lucidity_service.apply_lucidity_adjustment = AsyncMock(return_value=mock_result)

    await active_lucidity_service.apply_encounter_lucidity_loss(
        sample_player_id, "eldritch_horror", category="disturbing", location_id="room_001"
    )

    call_args = active_lucidity_service._lucidity_service.apply_lucidity_adjustment.call_args
    assert call_args[1]["location_id"] == "room_001"


@pytest.mark.asyncio
async def test_perform_recovery_action_success(active_lucidity_service, sample_player_id):
    """Test perform_recovery_action() successfully performs recovery."""
    mock_result = MagicMock()
    mock_result.new_lcd = 55
    active_lucidity_service._lucidity_service.get_cooldown = AsyncMock(return_value=None)
    active_lucidity_service._lucidity_service.apply_lucidity_adjustment = AsyncMock(return_value=mock_result)
    active_lucidity_service._lucidity_service.set_cooldown = AsyncMock()

    result = await active_lucidity_service.perform_recovery_action(sample_player_id, action_code="pray")

    assert result == mock_result
    # Pray action should give +8 LCD
    call_args = active_lucidity_service._lucidity_service.apply_lucidity_adjustment.call_args
    assert call_args[0][1] == 8
    active_lucidity_service._lucidity_service.set_cooldown.assert_awaited_once()


@pytest.mark.asyncio
async def test_perform_recovery_action_on_cooldown(active_lucidity_service, sample_player_id):
    """Test perform_recovery_action() raises error when on cooldown."""
    mock_cooldown = MagicMock()
    mock_cooldown.cooldown_expires_at = datetime.now(UTC) + timedelta(minutes=5)
    active_lucidity_service._lucidity_service.get_cooldown = AsyncMock(return_value=mock_cooldown)

    with pytest.raises(LucidityActionOnCooldownError):
        await active_lucidity_service.perform_recovery_action(sample_player_id, action_code="pray")


@pytest.mark.asyncio
async def test_perform_recovery_action_cooldown_expired(active_lucidity_service, sample_player_id):
    """Test perform_recovery_action() succeeds when cooldown has expired."""
    mock_result = MagicMock()
    mock_cooldown = MagicMock()
    mock_cooldown.cooldown_expires_at = datetime.now(UTC) - timedelta(minutes=1)  # Expired
    active_lucidity_service._lucidity_service.get_cooldown = AsyncMock(return_value=mock_cooldown)
    active_lucidity_service._lucidity_service.apply_lucidity_adjustment = AsyncMock(return_value=mock_result)
    active_lucidity_service._lucidity_service.set_cooldown = AsyncMock()

    result = await active_lucidity_service.perform_recovery_action(sample_player_id, action_code="pray")

    assert result == mock_result
    active_lucidity_service._lucidity_service.set_cooldown.assert_awaited_once()


@pytest.mark.asyncio
async def test_perform_recovery_action_naive_datetime_cooldown(active_lucidity_service, sample_player_id):
    """Test perform_recovery_action() handles naive datetime in cooldown."""
    mock_result = MagicMock()
    mock_cooldown = MagicMock()
    # Naive datetime (no timezone)
    mock_cooldown.cooldown_expires_at = datetime.now() + timedelta(minutes=5)
    active_lucidity_service._lucidity_service.get_cooldown = AsyncMock(return_value=mock_cooldown)
    active_lucidity_service._lucidity_service.apply_lucidity_adjustment = AsyncMock(return_value=mock_result)
    active_lucidity_service._lucidity_service.set_cooldown = AsyncMock()

    # Should convert naive datetime to UTC-aware
    result = await active_lucidity_service.perform_recovery_action(sample_player_id, action_code="pray")
    assert result == mock_result


@pytest.mark.asyncio
async def test_perform_recovery_action_unknown_action(active_lucidity_service, sample_player_id):
    """Test perform_recovery_action() raises error for unknown action."""
    with pytest.raises(UnknownLucidityActionError):
        await active_lucidity_service.perform_recovery_action(sample_player_id, action_code="unknown_action")


@pytest.mark.asyncio
async def test_perform_recovery_action_string_player_id(active_lucidity_service):
    """Test perform_recovery_action() handles string player_id."""
    player_id_str = str(uuid.uuid4())
    mock_result = MagicMock()
    active_lucidity_service._lucidity_service.get_cooldown = AsyncMock(return_value=None)
    active_lucidity_service._lucidity_service.apply_lucidity_adjustment = AsyncMock(return_value=mock_result)
    active_lucidity_service._lucidity_service.set_cooldown = AsyncMock()

    result = await active_lucidity_service.perform_recovery_action(player_id_str, action_code="pray")

    assert result == mock_result
    # Should convert string to UUID
    call_args = active_lucidity_service._lucidity_service.apply_lucidity_adjustment.call_args
    assert isinstance(call_args[0][0], uuid.UUID)


@pytest.mark.asyncio
async def test_perform_recovery_action_invalid_string_player_id(active_lucidity_service):
    """Test perform_recovery_action() raises error for invalid string player_id."""
    with pytest.raises(ValueError, match="Invalid player_id format"):
        await active_lucidity_service.perform_recovery_action("invalid-uuid", action_code="pray")


@pytest.mark.asyncio
async def test_perform_recovery_action_all_actions(active_lucidity_service, sample_player_id):
    """Test perform_recovery_action() works for all recovery actions."""
    actions = ["pray", "meditate", "group_solace", "therapy", "folk_tonic"]
    expected_deltas = [8, 6, 4, 15, 3]

    for action, expected_delta in zip(actions, expected_deltas, strict=True):
        mock_result = MagicMock()
        active_lucidity_service._lucidity_service.get_cooldown = AsyncMock(return_value=None)
        active_lucidity_service._lucidity_service.apply_lucidity_adjustment = AsyncMock(return_value=mock_result)
        active_lucidity_service._lucidity_service.set_cooldown = AsyncMock()

        result = await active_lucidity_service.perform_recovery_action(sample_player_id, action_code=action)

        assert result == mock_result
        call_args = active_lucidity_service._lucidity_service.apply_lucidity_adjustment.call_args
        assert call_args[0][1] == expected_delta


@pytest.mark.asyncio
async def test_perform_recovery_action_sets_cooldown(active_lucidity_service, sample_player_id):
    """Test perform_recovery_action() sets cooldown after action."""
    mock_result = MagicMock()
    active_lucidity_service._lucidity_service.get_cooldown = AsyncMock(return_value=None)
    active_lucidity_service._lucidity_service.apply_lucidity_adjustment = AsyncMock(return_value=mock_result)
    active_lucidity_service._lucidity_service.set_cooldown = AsyncMock()

    await active_lucidity_service.perform_recovery_action(sample_player_id, action_code="pray")

    # Should set cooldown
    active_lucidity_service._lucidity_service.set_cooldown.assert_awaited_once()
    call_args = active_lucidity_service._lucidity_service.set_cooldown.call_args
    assert call_args[0][1] == "pray"  # action_code
    assert isinstance(call_args[0][2], datetime)  # expires_at


@pytest.mark.asyncio
async def test_perform_recovery_action_with_location(active_lucidity_service, sample_player_id):
    """Test perform_recovery_action() includes location_id."""
    mock_result = MagicMock()
    active_lucidity_service._lucidity_service.get_cooldown = AsyncMock(return_value=None)
    active_lucidity_service._lucidity_service.apply_lucidity_adjustment = AsyncMock(return_value=mock_result)
    active_lucidity_service._lucidity_service.set_cooldown = AsyncMock()

    await active_lucidity_service.perform_recovery_action(sample_player_id, action_code="pray", location_id="room_001")

    call_args = active_lucidity_service._lucidity_service.apply_lucidity_adjustment.call_args
    assert call_args[1]["location_id"] == "room_001"


@pytest.mark.asyncio
async def test_get_action_cooldown_success(active_lucidity_service, sample_player_id):
    """Test get_action_cooldown() retrieves cooldown."""
    mock_cooldown = MagicMock()
    active_lucidity_service._lucidity_service.get_cooldown = AsyncMock(return_value=mock_cooldown)

    result = await active_lucidity_service.get_action_cooldown(sample_player_id, "pray")

    assert result == mock_cooldown
    active_lucidity_service._lucidity_service.get_cooldown.assert_awaited_once_with(sample_player_id, "pray")


@pytest.mark.asyncio
async def test_get_action_cooldown_string_player_id(active_lucidity_service):
    """Test get_action_cooldown() handles string player_id."""
    player_id_str = str(uuid.uuid4())
    mock_cooldown = MagicMock()
    active_lucidity_service._lucidity_service.get_cooldown = AsyncMock(return_value=mock_cooldown)

    result = await active_lucidity_service.get_action_cooldown(player_id_str, "pray")

    assert result == mock_cooldown
    # Should convert string to UUID
    call_args = active_lucidity_service._lucidity_service.get_cooldown.call_args
    assert isinstance(call_args[0][0], uuid.UUID)


@pytest.mark.asyncio
async def test_get_action_cooldown_invalid_string_player_id(active_lucidity_service):
    """Test get_action_cooldown() raises error for invalid string player_id."""
    with pytest.raises(ValueError, match="Invalid player_id format"):
        await active_lucidity_service.get_action_cooldown("invalid-uuid", "pray")


@pytest.mark.asyncio
async def test_get_action_cooldown_lowercases_action_code(active_lucidity_service, sample_player_id):
    """Test get_action_cooldown() lowercases action_code."""
    mock_cooldown = MagicMock()
    active_lucidity_service._lucidity_service.get_cooldown = AsyncMock(return_value=mock_cooldown)

    await active_lucidity_service.get_action_cooldown(sample_player_id, "PRAY")

    # Should lowercase action_code
    call_args = active_lucidity_service._lucidity_service.get_cooldown.call_args
    assert call_args[0][1] == "pray"
