"""Unit tests for SpellRepository."""

from __future__ import annotations

from unittest.mock import AsyncMock, MagicMock, patch

import pytest
from sqlalchemy.exc import SQLAlchemyError

from server.exceptions import DatabaseError
from server.persistence.repositories.spell_repository import SpellRepository, _row_to_spell_dict


def test_row_to_spell_dict_maps_fields():
    row = MagicMock()
    row.spell_id = "heal"
    row.name = "Heal"
    row.description = "Restore HP"
    row.school = "clerical"
    row.mp_cost = 5
    row.lucidity_cost = 0
    row.corruption_on_learn = 0
    row.corruption_on_cast = 0
    row.casting_time_seconds = 1
    row.target_type = "self"
    row.range_type = "touch"
    row.effect_type = "heal"
    row.effect_data = {"amount": 10}
    row.materials = ["herb"]
    result = _row_to_spell_dict(row)
    assert result["spell_id"] == "heal"
    assert result["materials"] == ["herb"]


@pytest.fixture
def repo():
    return SpellRepository()


def _mock_session(rows, first_only=False):
    mock_session = AsyncMock()
    mock_result = MagicMock()
    if first_only:
        mock_result.mappings.return_value.first.return_value = rows
    else:
        mock_result.mappings.return_value.all.return_value = rows
    mock_session.execute = AsyncMock(return_value=mock_result)
    mock_session.__aenter__ = AsyncMock(return_value=mock_session)
    mock_session.__aexit__ = AsyncMock(return_value=None)
    return mock_session


def _spell_row():
    row = MagicMock()
    row.spell_id = "light"
    row.name = "Light"
    row.description = "Glow"
    row.school = "mystic"
    row.mp_cost = 1
    row.lucidity_cost = 0
    row.corruption_on_learn = 0
    row.corruption_on_cast = 0
    row.casting_time_seconds = 0
    row.target_type = "self"
    row.range_type = "touch"
    row.effect_type = "utility"
    row.effect_data = {}
    row.materials = []
    return row


@pytest.mark.asyncio
async def test_get_all_spells(repo):
    mock_session = _mock_session([_spell_row()])
    with patch(
        "server.persistence.repositories.spell_repository.get_session_maker",
        return_value=MagicMock(return_value=mock_session),
    ):
        spells = await repo.get_all_spells()
    assert len(spells) == 1
    assert spells[0]["spell_id"] == "light"


@pytest.mark.asyncio
async def test_get_spell_by_id_found(repo):
    mock_session = _mock_session(_spell_row(), first_only=True)
    with patch(
        "server.persistence.repositories.spell_repository.get_session_maker",
        return_value=MagicMock(return_value=mock_session),
    ):
        spell = await repo.get_spell_by_id("light")
    assert spell is not None
    assert spell["name"] == "Light"


@pytest.mark.asyncio
async def test_get_spell_by_id_not_found(repo):
    mock_session = _mock_session(None, first_only=True)
    with patch(
        "server.persistence.repositories.spell_repository.get_session_maker",
        return_value=MagicMock(return_value=mock_session),
    ):
        spell = await repo.get_spell_by_id("missing")
    assert spell is None


@pytest.mark.asyncio
async def test_get_all_spells_db_error(repo):
    mock_session = AsyncMock()
    mock_session.execute = AsyncMock(side_effect=SQLAlchemyError("fail"))
    mock_session.__aenter__ = AsyncMock(return_value=mock_session)
    mock_session.__aexit__ = AsyncMock(return_value=None)
    with patch(
        "server.persistence.repositories.spell_repository.get_session_maker",
        return_value=MagicMock(return_value=mock_session),
    ):
        with pytest.raises(DatabaseError):
            await repo.get_all_spells()
