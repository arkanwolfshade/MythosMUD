"""Unit tests for CorruptionRepository (#804)."""

import uuid
from datetime import UTC, datetime, timedelta
from unittest.mock import AsyncMock, MagicMock

import pytest

from server.models.corruption import CorruptionCooldown
from server.services.corruption_repository import CorruptionRepository


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
def repo(mock_session: _MockAsyncSession) -> CorruptionRepository:
    """CorruptionRepository backed by mock session."""
    return CorruptionRepository(mock_session.session)


@pytest.mark.asyncio
async def test_add_adjustment_log(repo: CorruptionRepository, mock_session: _MockAsyncSession) -> None:
    """add_adjustment_log persists a ledger entry with the given fields."""
    player_id = uuid.uuid4()
    entry = await repo.add_adjustment_log(player_id, 5, "spell_cast", "{}", "room_1")
    assert entry.player_id == player_id
    assert entry.delta == 5
    assert entry.reason_code == "spell_cast"
    assert entry.location_id == "room_1"
    mock_session.add.assert_called_once()
    mock_session.flush.assert_awaited()


@pytest.mark.asyncio
async def test_get_cooldown_returns_record(repo: CorruptionRepository, mock_session: _MockAsyncSession) -> None:
    """get_cooldown returns the scalar result."""
    player_id = uuid.uuid4()
    cooldown = MagicMock(spec=CorruptionCooldown)
    mock_session.execute.return_value = _scalar_result(cooldown)
    got = await repo.get_cooldown(player_id, "cleanse")
    assert got is cooldown
    mock_session.execute.assert_awaited_once()


@pytest.mark.asyncio
async def test_get_cooldown_returns_none_when_absent(
    repo: CorruptionRepository, mock_session: _MockAsyncSession
) -> None:
    """get_cooldown returns None when no cooldown row exists."""
    mock_session.execute.return_value = _scalar_result(None)
    got = await repo.get_cooldown(uuid.uuid4(), "cleanse")
    assert got is None


@pytest.mark.asyncio
async def test_set_cooldown_creates_when_absent(repo: CorruptionRepository, mock_session: _MockAsyncSession) -> None:
    """set_cooldown inserts a new row when none exists yet."""
    player_id = uuid.uuid4()
    expires = datetime.now(UTC).replace(tzinfo=None)
    mock_session.execute.return_value = _scalar_result(None)
    cooldown = await repo.set_cooldown(player_id, "cleanse", expires)
    assert cooldown.player_id == player_id
    assert cooldown.action_code == "cleanse"
    assert cooldown.cooldown_expires_at == expires
    mock_session.add.assert_called_once()
    mock_session.flush.assert_awaited()


@pytest.mark.asyncio
async def test_set_cooldown_updates_existing(repo: CorruptionRepository, mock_session: _MockAsyncSession) -> None:
    """set_cooldown updates the expiry on an existing row rather than inserting a second one."""
    player_id = uuid.uuid4()
    expires = datetime.now(UTC).replace(tzinfo=None)
    existing = CorruptionCooldown(player_id=player_id, action_code="cleanse", cooldown_expires_at=expires)
    mock_session.execute.return_value = _scalar_result(existing)
    new_expires = expires + timedelta(hours=6)
    cooldown = await repo.set_cooldown(player_id, "cleanse", new_expires)
    assert cooldown is existing
    assert cooldown.cooldown_expires_at == new_expires
    mock_session.add.assert_not_called()
    mock_session.flush.assert_awaited()
