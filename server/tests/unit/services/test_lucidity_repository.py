"""Unit tests for LucidityRepository."""

import uuid
from datetime import UTC, datetime
from unittest.mock import AsyncMock, MagicMock

import pytest

from server.models.lucidity import LucidityCooldown, LucidityExposureState, PlayerLucidity
from server.services.lucidity_repository import LucidityRepository, _utc_now


@pytest.fixture
def mock_session() -> AsyncMock:
    """AsyncSession mock with execute/add/flush."""
    session = AsyncMock()
    session.add = MagicMock()
    return session


@pytest.fixture
def repo(mock_session: AsyncMock) -> LucidityRepository:
    """LucidityRepository backed by mock session."""
    return LucidityRepository(mock_session)


def test_utc_now_is_naive():
    """_utc_now returns naive UTC datetime."""
    ts = _utc_now()
    assert ts.tzinfo is None


@pytest.mark.asyncio
async def test_get_player_lucidity_returns_record(repo: LucidityRepository, mock_session: AsyncMock):
    """get_player_lucidity returns scalar result."""
    player_id = uuid.uuid4()
    record = MagicMock(spec=PlayerLucidity)
    result = MagicMock()
    result.scalar_one_or_none.return_value = record
    mock_session.execute.return_value = result
    got = await repo.get_player_lucidity(player_id)
    assert got is record
    mock_session.execute.assert_awaited_once()


@pytest.mark.asyncio
async def test_get_or_create_player_lucidity_existing(repo: LucidityRepository, mock_session: AsyncMock):
    """get_or_create returns existing record without add."""
    player_id = uuid.uuid4()
    existing = MagicMock(spec=PlayerLucidity)
    result = MagicMock()
    result.scalar_one_or_none.return_value = existing
    mock_session.execute.return_value = result
    got = await repo.get_or_create_player_lucidity(player_id)
    assert got is existing
    mock_session.add.assert_not_called()


@pytest.mark.asyncio
async def test_get_or_create_player_lucidity_creates(repo: LucidityRepository, mock_session: AsyncMock):
    """get_or_create inserts new PlayerLucidity when missing."""
    player_id = uuid.uuid4()
    result = MagicMock()
    result.scalar_one_or_none.return_value = None
    mock_session.execute.return_value = result
    got = await repo.get_or_create_player_lucidity(player_id)
    assert got.player_id == player_id
    mock_session.add.assert_called_once()
    mock_session.flush.assert_awaited()


@pytest.mark.asyncio
async def test_add_adjustment_log(repo: LucidityRepository, mock_session: AsyncMock):
    """add_adjustment_log persists log entry."""
    player_id = uuid.uuid4()
    entry = await repo.add_adjustment_log(player_id, -5, "combat", "{}", "room_1")
    assert entry.player_id == player_id
    assert entry.delta == -5
    mock_session.add.assert_called_once()
    mock_session.flush.assert_awaited()


@pytest.mark.asyncio
async def test_get_exposure_state(repo: LucidityRepository, mock_session: AsyncMock):
    """get_exposure_state returns exposure record."""
    player_id = uuid.uuid4()
    exposure = MagicMock(spec=LucidityExposureState)
    result = MagicMock()
    result.scalar_one_or_none.return_value = exposure
    mock_session.execute.return_value = result
    got = await repo.get_exposure_state(player_id, "deep_one")
    assert got is exposure


@pytest.mark.asyncio
async def test_increment_exposure_state_new(repo: LucidityRepository, mock_session: AsyncMock):
    """increment_exposure_state creates record when absent."""
    player_id = uuid.uuid4()
    result = MagicMock()
    result.scalar_one_or_none.return_value = None
    mock_session.execute.return_value = result
    exposure = await repo.increment_exposure_state(player_id, "shoggoth")
    assert exposure.player_id == player_id
    assert exposure.entity_archetype == "shoggoth"
    assert exposure.encounter_count == 1
    mock_session.add.assert_called_once()


@pytest.mark.asyncio
async def test_increment_exposure_state_existing(repo: LucidityRepository, mock_session: AsyncMock):
    """increment_exposure_state bumps count on existing record."""
    player_id = uuid.uuid4()
    existing = LucidityExposureState(
        player_id=player_id,
        entity_archetype="shoggoth",
        encounter_count=2,
        last_encounter_at=datetime.now(UTC).replace(tzinfo=None),
    )
    result = MagicMock()
    result.scalar_one_or_none.return_value = existing
    mock_session.execute.return_value = result
    exposure = await repo.increment_exposure_state(player_id, "shoggoth")
    assert exposure.encounter_count == 3
    mock_session.add.assert_not_called()


@pytest.mark.asyncio
async def test_get_cooldown(repo: LucidityRepository, mock_session: AsyncMock):
    """get_cooldown returns cooldown record."""
    player_id = uuid.uuid4()
    cooldown = MagicMock(spec=LucidityCooldown)
    result = MagicMock()
    result.scalar_one_or_none.return_value = cooldown
    mock_session.execute.return_value = result
    got = await repo.get_cooldown(player_id, "meditate")
    assert got is cooldown


@pytest.mark.asyncio
async def test_set_cooldown_new(repo: LucidityRepository, mock_session: AsyncMock):
    """set_cooldown creates record when absent."""
    player_id = uuid.uuid4()
    expires = datetime.now(UTC).replace(tzinfo=None)
    result = MagicMock()
    result.scalar_one_or_none.return_value = None
    mock_session.execute.return_value = result
    cooldown = await repo.set_cooldown(player_id, "meditate", expires)
    assert cooldown.action_code == "meditate"
    mock_session.add.assert_called_once()


@pytest.mark.asyncio
async def test_set_cooldown_update(repo: LucidityRepository, mock_session: AsyncMock):
    """set_cooldown updates existing record."""
    player_id = uuid.uuid4()
    expires = datetime.now(UTC).replace(tzinfo=None)
    existing = LucidityCooldown(player_id=player_id, action_code="meditate", cooldown_expires_at=expires)
    result = MagicMock()
    result.scalar_one_or_none.return_value = existing
    mock_session.execute.return_value = result
    new_expires = expires.replace(hour=expires.hour + 1)
    cooldown = await repo.set_cooldown(player_id, "meditate", new_expires)
    assert cooldown.cooldown_expires_at == new_expires
    mock_session.add.assert_not_called()


@pytest.mark.asyncio
async def test_delete_cooldowns_by_action_code_pattern(repo: LucidityRepository, mock_session: AsyncMock):
    """delete_cooldowns_by_action_code_pattern returns rowcount."""
    player_id = uuid.uuid4()
    result = MagicMock()
    result.rowcount = 3
    mock_session.execute.return_value = result
    deleted = await repo.delete_cooldowns_by_action_code_pattern(player_id, "spell_%")
    assert deleted == 3
    mock_session.flush.assert_awaited()
