"""
Unit tests for active lucidity service.

Tests the ActiveLucidityService class for encounter lucidity loss and recovery actions.
"""

import uuid
from dataclasses import dataclass, field
from datetime import UTC, datetime, timedelta
from types import SimpleNamespace
from typing import cast
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


@dataclass
class FakeRepo:
    """Stands in for LucidityRepository (exposure and cooldowns): serves configured values, records writes."""

    encounter_count: int = 1
    cooldown: object | None = None
    cooldown_queries: list[tuple[uuid.UUID, str]] = field(default_factory=lambda: cast(list[tuple[uuid.UUID, str]], []))
    cooldowns_set: list[tuple[uuid.UUID, str, datetime]] = field(
        default_factory=lambda: cast(list[tuple[uuid.UUID, str, datetime]], [])
    )

    async def increment_exposure_state(self, player_id: uuid.UUID, entity_archetype: str) -> SimpleNamespace:
        _ = player_id, entity_archetype
        return SimpleNamespace(encounter_count=self.encounter_count)

    async def get_cooldown(self, player_id: uuid.UUID, action_code: str) -> object | None:
        self.cooldown_queries.append((player_id, action_code))
        return self.cooldown

    async def set_cooldown(self, player_id: uuid.UUID, action_code: str, expires_at: datetime) -> None:
        self.cooldowns_set.append((player_id, action_code, expires_at))


@pytest.fixture
def repo(monkeypatch: pytest.MonkeyPatch) -> FakeRepo:
    """The cooldown repository every ActiveLucidityService built in a test gets."""
    fake = FakeRepo()

    def build(_session: object) -> FakeRepo:
        return fake

    monkeypatch.setattr("server.services.active_lucidity_service.LucidityRepository", build)
    return fake


@pytest.fixture
def active_lucidity_service(mock_session, repo: FakeRepo):
    """Create an ActiveLucidityService instance."""
    _ = repo
    return ActiveLucidityService(mock_session, MagicMock())


@pytest.fixture
def sample_player_id():
    """Create a sample player ID."""
    return uuid.uuid4()


@pytest.mark.asyncio
async def test_active_lucidity_service_init(mock_session):
    """Test ActiveLucidityService initialization."""
    service = ActiveLucidityService(mock_session, MagicMock())
    assert service._session == mock_session
    assert service._lucidity_service is not None
    assert service._now_provider is not None


@pytest.mark.asyncio
async def test_active_lucidity_service_init_with_now_provider(mock_session):
    """Test ActiveLucidityService initialization with custom now_provider."""
    custom_now = datetime(2024, 1, 1, tzinfo=UTC)

    def now_provider():
        return custom_now

    service = ActiveLucidityService(mock_session, MagicMock(), now_provider=now_provider)
    assert service._now_provider() == custom_now


@pytest.mark.asyncio
async def test_apply_encounter_lucidity_loss_first_encounter(active_lucidity_service, sample_player_id, repo: FakeRepo):
    """Test apply_encounter_lucidity_loss() for first encounter."""
    mock_result = MagicMock()
    mock_result.new_lcd = 94
    repo.encounter_count = 1
    active_lucidity_service._lucidity_service.apply_lucidity_adjustment = AsyncMock(return_value=mock_result)

    result = await active_lucidity_service.apply_encounter_lucidity_loss(
        sample_player_id, "eldritch_horror", category="disturbing"
    )

    assert result == mock_result
    # First encounter should use first_time delta (-6 for disturbing)
    call_args = active_lucidity_service._lucidity_service.apply_lucidity_adjustment.call_args
    assert call_args[0][1] == -6  # first_time delta


@pytest.mark.asyncio
async def test_apply_encounter_lucidity_loss_repeat_encounter(
    # Reason: UNTYPED_FIXTURE - active_lucidity_service is this file's untyped fixture; tests swap its methods for mocks.
    # Appropriate because: a typed ActiveLucidityService would forbid the method mocks every test in this file relies on.
    active_lucidity_service,  # pyright: ignore[reportMissingParameterType, reportUnknownParameterType]
    sample_player_id: uuid.UUID,
    repo: FakeRepo,
):
    """Test apply_encounter_lucidity_loss() for repeat encounter."""
    mock_result = MagicMock()
    mock_result.new_lcd = 92
    repo.encounter_count = 2  # Repeat encounter
    active_lucidity_service._lucidity_service.apply_lucidity_adjustment = AsyncMock(return_value=mock_result)

    result = await active_lucidity_service.apply_encounter_lucidity_loss(
        sample_player_id, "eldritch_horror", category="disturbing"
    )

    assert result == mock_result
    # Repeat encounter should use repeat delta (-2 for disturbing)
    call_args = active_lucidity_service._lucidity_service.apply_lucidity_adjustment.call_args
    assert call_args[0][1] == -2  # repeat delta


@pytest.mark.asyncio
async def test_apply_encounter_lucidity_loss_acclimated(active_lucidity_service, sample_player_id, repo: FakeRepo):
    """Test apply_encounter_lucidity_loss() for acclimated encounter."""
    mock_result = MagicMock()
    mock_result.new_lcd = 95
    repo.encounter_count = 6  # At threshold
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
async def test_apply_encounter_lucidity_loss_string_player_id(active_lucidity_service, repo: FakeRepo):
    """Test apply_encounter_lucidity_loss() handles string player_id."""
    player_id_str = str(uuid.uuid4())
    mock_result = MagicMock()
    repo.encounter_count = 1
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
async def test_apply_encounter_lucidity_loss_horrific_category(
    # Reason: UNTYPED_FIXTURE - active_lucidity_service is this file's untyped fixture; tests swap its methods for mocks.
    # Appropriate because: a typed ActiveLucidityService would forbid the method mocks every test in this file relies on.
    active_lucidity_service,  # pyright: ignore[reportMissingParameterType, reportUnknownParameterType]
    sample_player_id: uuid.UUID,
    repo: FakeRepo,
):
    """Test apply_encounter_lucidity_loss() with horrific category."""
    mock_result = MagicMock()
    repo.encounter_count = 1
    active_lucidity_service._lucidity_service.apply_lucidity_adjustment = AsyncMock(return_value=mock_result)

    result = await active_lucidity_service.apply_encounter_lucidity_loss(
        sample_player_id, "eldritch_horror", category="horrific"
    )

    assert result == mock_result
    # Horrific first_time is -12
    call_args = active_lucidity_service._lucidity_service.apply_lucidity_adjustment.call_args
    assert call_args[0][1] == -12


@pytest.mark.asyncio
async def test_apply_encounter_lucidity_loss_cosmic_category(active_lucidity_service, sample_player_id, repo: FakeRepo):
    """Test apply_encounter_lucidity_loss() with cosmic category."""
    mock_result = MagicMock()
    repo.encounter_count = 1
    active_lucidity_service._lucidity_service.apply_lucidity_adjustment = AsyncMock(return_value=mock_result)

    result = await active_lucidity_service.apply_encounter_lucidity_loss(
        sample_player_id, "eldritch_horror", category="cosmic"
    )

    assert result == mock_result
    # Cosmic first_time is -20
    call_args = active_lucidity_service._lucidity_service.apply_lucidity_adjustment.call_args
    assert call_args[0][1] == -20


@pytest.mark.asyncio
async def test_apply_encounter_lucidity_loss_with_location(active_lucidity_service, sample_player_id, repo: FakeRepo):
    """Test apply_encounter_lucidity_loss() includes location_id in metadata."""
    mock_result = MagicMock()
    repo.encounter_count = 1
    active_lucidity_service._lucidity_service.apply_lucidity_adjustment = AsyncMock(return_value=mock_result)

    await active_lucidity_service.apply_encounter_lucidity_loss(
        sample_player_id, "eldritch_horror", category="disturbing", location_id="room_001"
    )

    call_args = active_lucidity_service._lucidity_service.apply_lucidity_adjustment.call_args
    assert call_args[1]["location_id"] == "room_001"


@pytest.mark.asyncio
async def test_perform_recovery_action_success(active_lucidity_service, sample_player_id, repo: FakeRepo):
    """Test perform_recovery_action() successfully performs recovery."""
    mock_result = MagicMock()
    mock_result.new_lcd = 55
    active_lucidity_service._lucidity_service.apply_lucidity_adjustment = AsyncMock(return_value=mock_result)

    result = await active_lucidity_service.perform_recovery_action(sample_player_id, action_code="pray")

    assert result == mock_result
    # Pray action should give +8 LCD
    call_args = active_lucidity_service._lucidity_service.apply_lucidity_adjustment.call_args
    assert call_args[0][1] == 8
    assert len(repo.cooldowns_set) == 1


@pytest.mark.asyncio
async def test_perform_recovery_action_on_cooldown(active_lucidity_service, sample_player_id, repo: FakeRepo):
    """Test perform_recovery_action() raises error when on cooldown."""
    mock_cooldown = MagicMock()
    mock_cooldown.cooldown_expires_at = datetime.now(UTC) + timedelta(minutes=5)
    repo.cooldown = mock_cooldown

    with pytest.raises(LucidityActionOnCooldownError):
        await active_lucidity_service.perform_recovery_action(sample_player_id, action_code="pray")


@pytest.mark.asyncio
async def test_perform_recovery_action_cooldown_expired(active_lucidity_service, sample_player_id, repo: FakeRepo):
    """Test perform_recovery_action() succeeds when cooldown has expired."""
    mock_result = MagicMock()
    mock_cooldown = MagicMock()
    mock_cooldown.cooldown_expires_at = datetime.now(UTC) - timedelta(minutes=1)  # Expired
    repo.cooldown = mock_cooldown
    active_lucidity_service._lucidity_service.apply_lucidity_adjustment = AsyncMock(return_value=mock_result)

    result = await active_lucidity_service.perform_recovery_action(sample_player_id, action_code="pray")

    assert result == mock_result
    assert len(repo.cooldowns_set) == 1


@pytest.mark.asyncio
async def test_perform_recovery_action_naive_datetime_cooldown(mock_session, sample_player_id, repo: FakeRepo):
    """Test perform_recovery_action() handles naive datetime in cooldown."""
    # Use a fixed time to avoid timezone and timing issues
    fixed_now = datetime(2024, 1, 15, 12, 0, 0, tzinfo=UTC)

    def now_provider():
        return fixed_now

    service = ActiveLucidityService(mock_session, MagicMock(), now_provider=now_provider)

    mock_result = MagicMock()
    mock_cooldown = MagicMock()
    # Naive datetime (no timezone) - set to expired cooldown (1 minute ago in naive time)
    # The code converts naive datetime to UTC-aware using .replace(tzinfo=UTC)
    # which treats the naive time as if it were already UTC
    mock_cooldown.cooldown_expires_at = datetime(2024, 1, 15, 11, 59, 0)  # 1 minute before fixed_now
    repo.cooldown = mock_cooldown
    service._lucidity_service.apply_lucidity_adjustment = AsyncMock(return_value=mock_result)  # type: ignore[method-assign]

    # Should convert naive datetime to UTC-aware and allow action since cooldown is expired
    result = await service.perform_recovery_action(sample_player_id, action_code="pray")
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
    active_lucidity_service._lucidity_service.apply_lucidity_adjustment = AsyncMock(return_value=mock_result)

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
    actions = ["pray", "meditate", "group_solace", "therapy"]
    expected_deltas = [8, 6, 4, 15]

    for action, expected_delta in zip(actions, expected_deltas, strict=True):
        mock_result = MagicMock()
        active_lucidity_service._lucidity_service.apply_lucidity_adjustment = AsyncMock(return_value=mock_result)

        result = await active_lucidity_service.perform_recovery_action(sample_player_id, action_code=action)

        assert result == mock_result
        call_args = active_lucidity_service._lucidity_service.apply_lucidity_adjustment.call_args
        assert call_args[0][1] == expected_delta


@pytest.mark.asyncio
async def test_perform_recovery_action_sets_cooldown(active_lucidity_service, sample_player_id, repo: FakeRepo):
    """Test perform_recovery_action() sets cooldown after action."""
    mock_result = MagicMock()
    active_lucidity_service._lucidity_service.apply_lucidity_adjustment = AsyncMock(return_value=mock_result)

    await active_lucidity_service.perform_recovery_action(sample_player_id, action_code="pray")

    # Should set cooldown
    [(_player_id, action_code, expires_at)] = repo.cooldowns_set
    assert action_code == "pray"
    assert isinstance(expires_at, datetime)


@pytest.mark.asyncio
async def test_perform_recovery_action_with_location(active_lucidity_service, sample_player_id):
    """Test perform_recovery_action() includes location_id."""
    mock_result = MagicMock()
    active_lucidity_service._lucidity_service.apply_lucidity_adjustment = AsyncMock(return_value=mock_result)

    await active_lucidity_service.perform_recovery_action(sample_player_id, action_code="pray", location_id="room_001")

    call_args = active_lucidity_service._lucidity_service.apply_lucidity_adjustment.call_args
    assert call_args[1]["location_id"] == "room_001"


@pytest.mark.asyncio
async def test_get_action_cooldown_success(active_lucidity_service, sample_player_id, repo: FakeRepo):
    """Test get_action_cooldown() retrieves cooldown."""
    mock_cooldown = MagicMock()
    repo.cooldown = mock_cooldown

    result = await active_lucidity_service.get_action_cooldown(sample_player_id, "pray")

    assert result == mock_cooldown
    assert repo.cooldown_queries == [(sample_player_id, "pray")]


@pytest.mark.asyncio
async def test_get_action_cooldown_string_player_id(active_lucidity_service, repo: FakeRepo):
    """Test get_action_cooldown() handles string player_id."""
    player_id_str = str(uuid.uuid4())
    mock_cooldown = MagicMock()
    repo.cooldown = mock_cooldown

    result = await active_lucidity_service.get_action_cooldown(player_id_str, "pray")

    assert result == mock_cooldown
    # Should convert string to UUID
    [(queried_id, _code)] = repo.cooldown_queries
    assert isinstance(queried_id, uuid.UUID)


@pytest.mark.asyncio
async def test_get_action_cooldown_invalid_string_player_id(active_lucidity_service):
    """Test get_action_cooldown() raises error for invalid string player_id."""
    with pytest.raises(ValueError, match="Invalid player_id format"):
        await active_lucidity_service.get_action_cooldown("invalid-uuid", "pray")


@pytest.mark.asyncio
async def test_get_action_cooldown_lowercases_action_code(active_lucidity_service, sample_player_id, repo: FakeRepo):
    """Test get_action_cooldown() lowercases action_code."""
    mock_cooldown = MagicMock()
    repo.cooldown = mock_cooldown

    await active_lucidity_service.get_action_cooldown(sample_player_id, "PRAY")

    # Should lowercase action_code
    assert [code for _id, code in repo.cooldown_queries] == ["pray"]
