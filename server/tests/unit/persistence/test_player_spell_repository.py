"""Unit tests for PlayerSpellRepository."""

import uuid
from datetime import UTC, datetime
from unittest.mock import AsyncMock, MagicMock, patch

import pytest
from sqlalchemy.exc import SQLAlchemyError

from server.exceptions import DatabaseError
from server.persistence.repositories.player_spell_repository import (
    PlayerSpellRepository,
    _row_to_player_spell,
)


def test_row_to_player_spell_maps_fields():
    row = MagicMock()
    row.id = 1
    row.player_id = uuid.uuid4()
    row.spell_id = "fireball"
    row.mastery = 5
    row.learned_at = datetime.now(UTC)
    row.last_cast_at = None
    row.times_cast = 2
    spell = _row_to_player_spell(row)
    assert spell.spell_id == "fireball"
    assert spell.mastery == 5
    assert spell.times_cast == 2


@pytest.fixture
def repo():
    return PlayerSpellRepository()


def _mock_session_with_rows(rows):
    mock_session = AsyncMock()
    mock_session.commit = AsyncMock()
    mock_result = MagicMock()
    if isinstance(rows, list):
        mock_result.mappings.return_value.all.return_value = rows
    else:
        mock_result.mappings.return_value.first.return_value = rows
    mock_session.execute = AsyncMock(return_value=mock_result)
    mock_session.__aenter__ = AsyncMock(return_value=mock_session)
    mock_session.__aexit__ = AsyncMock(return_value=None)
    return mock_session


def _spell_row(player_id=None):
    row = MagicMock()
    row.id = 1
    row.player_id = player_id or uuid.uuid4()
    row.spell_id = "light"
    row.mastery = 0
    row.learned_at = datetime.now(UTC)
    row.last_cast_at = None
    row.times_cast = 0
    return row


@pytest.mark.asyncio
async def test_get_player_spells(repo):
    player_id = uuid.uuid4()
    mock_session = _mock_session_with_rows([_spell_row(player_id)])
    with patch(
        "server.persistence.repositories.player_spell_repository.get_session_maker",
        return_value=MagicMock(return_value=mock_session),
    ):
        spells = await repo.get_player_spells(player_id)
    assert len(spells) == 1
    assert spells[0].spell_id == "light"


@pytest.mark.asyncio
async def test_get_player_spells_db_error(repo):
    mock_session = AsyncMock()
    mock_session.execute = AsyncMock(side_effect=SQLAlchemyError("fail"))
    mock_session.__aenter__ = AsyncMock(return_value=mock_session)
    mock_session.__aexit__ = AsyncMock(return_value=None)
    with patch(
        "server.persistence.repositories.player_spell_repository.get_session_maker",
        return_value=MagicMock(return_value=mock_session),
    ):
        with pytest.raises(DatabaseError):
            await repo.get_player_spells(uuid.uuid4())


@pytest.mark.asyncio
async def test_get_player_spell_found(repo):
    player_id = uuid.uuid4()
    mock_session = _mock_session_with_rows(_spell_row(player_id))
    with patch(
        "server.persistence.repositories.player_spell_repository.get_session_maker",
        return_value=MagicMock(return_value=mock_session),
    ):
        spell = await repo.get_player_spell(player_id, "light")
    assert spell is not None
    assert spell.spell_id == "light"


@pytest.mark.asyncio
async def test_get_player_spell_missing(repo):
    mock_session = _mock_session_with_rows(None)
    with patch(
        "server.persistence.repositories.player_spell_repository.get_session_maker",
        return_value=MagicMock(return_value=mock_session),
    ):
        spell = await repo.get_player_spell(uuid.uuid4(), "missing")
    assert spell is None


@pytest.mark.asyncio
async def test_learn_spell(repo):
    player_id = uuid.uuid4()
    mock_session = _mock_session_with_rows(_spell_row(player_id))
    with patch(
        "server.persistence.repositories.player_spell_repository.get_session_maker",
        return_value=MagicMock(return_value=mock_session),
    ):
        spell = await repo.learn_spell(player_id, "light", initial_mastery=10)
    assert spell.mastery == 0
    mock_session.commit.assert_awaited_once()


@pytest.mark.asyncio
async def test_learn_spell_no_row_raises(repo):
    mock_session = _mock_session_with_rows(None)
    with patch(
        "server.persistence.repositories.player_spell_repository.get_session_maker",
        return_value=MagicMock(return_value=mock_session),
    ):
        with pytest.raises(DatabaseError):
            await repo.learn_spell(uuid.uuid4(), "light")


@pytest.mark.asyncio
async def test_update_mastery(repo):
    row = _spell_row()
    row.mastery = 50
    mock_session = _mock_session_with_rows(row)
    with patch(
        "server.persistence.repositories.player_spell_repository.get_session_maker",
        return_value=MagicMock(return_value=mock_session),
    ):
        updated = await repo.update_mastery(uuid.uuid4(), "light", 50)
    assert updated is not None
    assert updated.mastery == 50


@pytest.mark.asyncio
async def test_update_mastery_not_found(repo):
    mock_session = _mock_session_with_rows(None)
    with patch(
        "server.persistence.repositories.player_spell_repository.get_session_maker",
        return_value=MagicMock(return_value=mock_session),
    ):
        assert await repo.update_mastery(uuid.uuid4(), "light", 50) is None


@pytest.mark.asyncio
async def test_record_spell_cast(repo):
    row = _spell_row()
    row.times_cast = 3
    mock_session = _mock_session_with_rows(row)
    with patch(
        "server.persistence.repositories.player_spell_repository.get_session_maker",
        return_value=MagicMock(return_value=mock_session),
    ):
        recorded = await repo.record_spell_cast(uuid.uuid4(), "light")
    assert recorded is not None
    assert recorded.times_cast == 3
