"""Unit tests for ProfessionRepository."""

from __future__ import annotations

from unittest.mock import AsyncMock, MagicMock, patch

import pytest
from sqlalchemy.exc import SQLAlchemyError

from server.exceptions import DatabaseError
from server.persistence.repositories.profession_repository import (
    ProfessionRepository,
    _bool_or_default,
    _row_to_profession,
    _str_or_default,
    _text_or_default,
)


def test_helpers_defaults():
    assert _str_or_default(None) == ""
    assert _text_or_default(None, "x") == "x"
    assert _bool_or_default(None) is True
    assert _bool_or_default(False) is False


def test_row_to_profession():
    row = MagicMock()
    row.id = 1
    row.name = "Detective"
    row.description = "Investigator"
    row.flavor_text = ""
    row.stat_requirements = "{}"
    row.mechanical_effects = "{}"
    row.is_available = True
    row.stat_modifiers = "[]"
    row.skill_modifiers = "[]"
    prof = _row_to_profession(row)
    assert prof.name == "Detective"


@pytest.fixture
def repo():
    return ProfessionRepository()


def _profession_row():
    row = MagicMock()
    row.id = 2
    row.name = "Occultist"
    row.description = "Scholar"
    row.flavor_text = "Lore"
    row.stat_requirements = "{}"
    row.mechanical_effects = "{}"
    row.is_available = True
    row.stat_modifiers = "[]"
    row.skill_modifiers = "[]"
    return row


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


@pytest.mark.asyncio
async def test_get_all_professions(repo):
    mock_session = _mock_session([_profession_row()])
    with patch(
        "server.persistence.repositories.profession_repository.get_session_maker",
        return_value=MagicMock(return_value=mock_session),
    ):
        professions = await repo.get_all_professions()
    assert len(professions) == 1
    assert professions[0].name == "Occultist"


@pytest.mark.asyncio
async def test_get_profession_by_id(repo):
    mock_session = _mock_session(_profession_row(), first_only=True)
    with patch(
        "server.persistence.repositories.profession_repository.get_session_maker",
        return_value=MagicMock(return_value=mock_session),
    ):
        prof = await repo.get_profession_by_id(2)
    assert prof is not None
    assert prof.id == 2


@pytest.mark.asyncio
async def test_get_profession_by_id_not_found(repo):
    mock_session = _mock_session(None, first_only=True)
    with patch(
        "server.persistence.repositories.profession_repository.get_session_maker",
        return_value=MagicMock(return_value=mock_session),
    ):
        prof = await repo.get_profession_by_id(99)
    assert prof is None


@pytest.mark.asyncio
async def test_get_all_professions_db_error(repo):
    mock_session = AsyncMock()
    mock_session.execute = AsyncMock(side_effect=SQLAlchemyError("fail"))
    mock_session.__aenter__ = AsyncMock(return_value=mock_session)
    mock_session.__aexit__ = AsyncMock(return_value=None)
    with patch(
        "server.persistence.repositories.profession_repository.get_session_maker",
        return_value=MagicMock(return_value=mock_session),
    ):
        with pytest.raises(DatabaseError):
            await repo.get_all_professions()
