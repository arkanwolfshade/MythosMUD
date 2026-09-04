"""Unit tests for LucidityRepository."""

import uuid
from datetime import UTC, datetime, timedelta
from unittest.mock import AsyncMock, MagicMock

import pytest

from server.models.lucidity import LucidityCooldown, LucidityExposureState, PlayerLucidity
from server.services.lucidity_repository import LucidityRepository, _utc_now


class _MockAsyncSession:
    """Session mock with typed attrs (AsyncMock children are otherwise Any)."""

    def __init__(self) -> None:
        self.execute: AsyncMock = AsyncMock()
        self.add: MagicMock = MagicMock()
        self.flush: AsyncMock = AsyncMock()
        self.session: AsyncMock = AsyncMock()
        self.session.execute = self.execute
        self.session.add = self.add
        self.session.flush = self.flush


def _scalar_result(value: object) -> MagicMock:
    """Execute result mock with typed scalar_one_or_none."""
    result: MagicMock = MagicMock()
    scalar_one_or_none: MagicMock = MagicMock(return_value=value)
    result.scalar_one_or_none = scalar_one_or_none
    return result


@pytest.fixture
def mock_session() -> _MockAsyncSession:
    """AsyncSession mock with execute/add/flush."""
    return _MockAsyncSession()


@pytest.fixture
def repo(mock_session: _MockAsyncSession) -> LucidityRepository:
    """LucidityRepository backed by mock session."""
    return LucidityRepository(mock_session.session)


def test_utc_now_is_naive():
    """_utc_now returns naive UTC datetime."""
    ts = _utc_now()
    assert ts.tzinfo is None


@pytest.mark.asyncio
async def test_get_player_lucidity_returns_record(repo: LucidityRepository, mock_session: _MockAsyncSession):
    """get_player_lucidity returns scalar result."""
    player_id = uuid.uuid4()
    record = MagicMock(spec=PlayerLucidity)
    mock_session.execute.return_value = _scalar_result(record)
    got = await repo.get_player_lucidity(player_id)
    assert got is record
    mock_session.execute.assert_awaited_once()


@pytest.mark.asyncio
async def test_get_or_create_player_lucidity_existing(repo: LucidityRepository, mock_session: _MockAsyncSession):
    """get_or_create returns existing record without add."""
    player_id = uuid.uuid4()
    existing = MagicMock(spec=PlayerLucidity)
    mock_session.execute.return_value = _scalar_result(existing)
    got = await repo.get_or_create_player_lucidity(player_id)
    assert got is existing
    mock_session.add.assert_not_called()


@pytest.mark.asyncio
async def test_get_or_create_player_lucidity_creates(repo: LucidityRepository, mock_session: _MockAsyncSession):
    """get_or_create inserts new PlayerLucidity when missing."""
    player_id = uuid.uuid4()
    mock_session.execute.return_value = _scalar_result(None)
    got = await repo.get_or_create_player_lucidity(player_id)
    assert got.player_id == player_id
    mock_session.add.assert_called_once()
    mock_session.flush.assert_awaited()


@pytest.mark.asyncio
async def test_add_adjustment_log(repo: LucidityRepository, mock_session: _MockAsyncSession):
    """add_adjustment_log persists log entry."""
    player_id = uuid.uuid4()
    entry = await repo.add_adjustment_log(player_id, -5, "combat", "{}", "room_1")
    assert entry.player_id == player_id
    assert entry.delta == -5
    mock_session.add.assert_called_once()
    mock_session.flush.assert_awaited()


@pytest.mark.asyncio
async def test_get_exposure_state(repo: LucidityRepository, mock_session: _MockAsyncSession):
    """get_exposure_state returns exposure record."""
    player_id = uuid.uuid4()
    exposure = MagicMock(spec=LucidityExposureState)
    mock_session.execute.return_value = _scalar_result(exposure)
    got = await repo.get_exposure_state(player_id, "deep_one")
    assert got is exposure


@pytest.mark.asyncio
async def test_increment_exposure_state_new(repo: LucidityRepository, mock_session: _MockAsyncSession):
    """increment_exposure_state creates record when absent."""
    player_id = uuid.uuid4()
    mock_session.execute.return_value = _scalar_result(None)
    exposure = await repo.increment_exposure_state(player_id, "shoggoth")
    assert exposure.player_id == player_id
    assert exposure.entity_archetype == "shoggoth"
    assert exposure.encounter_count == 1
    mock_session.add.assert_called_once()


@pytest.mark.asyncio
async def test_increment_exposure_state_existing(repo: LucidityRepository, mock_session: _MockAsyncSession):
    """increment_exposure_state bumps count on existing record."""
    player_id = uuid.uuid4()
    existing = LucidityExposureState(
        player_id=player_id,
        entity_archetype="shoggoth",
        encounter_count=2,
        last_encounter_at=datetime.now(UTC).replace(tzinfo=None),
    )
    mock_session.execute.return_value = _scalar_result(existing)
    exposure = await repo.increment_exposure_state(player_id, "shoggoth")
    assert exposure.encounter_count == 3
    mock_session.add.assert_not_called()


@pytest.mark.asyncio
async def test_get_cooldown(repo: LucidityRepository, mock_session: _MockAsyncSession):
    """get_cooldown returns cooldown record."""
    player_id = uuid.uuid4()
    cooldown = MagicMock(spec=LucidityCooldown)
    mock_session.execute.return_value = _scalar_result(cooldown)
    got = await repo.get_cooldown(player_id, "meditate")
    assert got is cooldown


@pytest.mark.asyncio
async def test_set_cooldown_new(repo: LucidityRepository, mock_session: _MockAsyncSession):
    """set_cooldown creates record when absent."""
    player_id = uuid.uuid4()
    expires = datetime.now(UTC).replace(tzinfo=None)
    mock_session.execute.return_value = _scalar_result(None)
    cooldown = await repo.set_cooldown(player_id, "meditate", expires)
    assert cooldown.action_code == "meditate"
    mock_session.add.assert_called_once()


@pytest.mark.asyncio
async def test_set_cooldown_update(repo: LucidityRepository, mock_session: _MockAsyncSession):
    """set_cooldown updates existing record."""
    player_id = uuid.uuid4()
    expires = datetime.now(UTC).replace(tzinfo=None)
    existing = LucidityCooldown(player_id=player_id, action_code="meditate", cooldown_expires_at=expires)
    mock_session.execute.return_value = _scalar_result(existing)
    new_expires = expires + timedelta(hours=1)
    cooldown = await repo.set_cooldown(player_id, "meditate", new_expires)
    assert cooldown.cooldown_expires_at == new_expires
    mock_session.add.assert_not_called()


@pytest.mark.asyncio
async def test_delete_cooldowns_by_action_code_pattern(repo: LucidityRepository, mock_session: _MockAsyncSession):
    """delete_cooldowns_by_action_code_pattern returns rowcount."""
    player_id = uuid.uuid4()
    result: MagicMock = MagicMock()
    result.rowcount = 3
    mock_session.execute.return_value = result
    deleted = await repo.delete_cooldowns_by_action_code_pattern(player_id, "spell_%")
    assert deleted == 3
    mock_session.flush.assert_awaited()
