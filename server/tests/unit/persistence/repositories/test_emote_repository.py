"""Unit tests for EmoteRepository (#624)."""

from __future__ import annotations

from unittest.mock import AsyncMock, MagicMock, patch

import pytest
from sqlalchemy.exc import SQLAlchemyError

from server.exceptions import DatabaseError
from server.persistence.repositories.emote_repository import EmoteRepository


@pytest.fixture
def repo():
    return EmoteRepository()


def _mock_session(rows):
    mock_session = AsyncMock()
    mock_session.execute = AsyncMock(return_value=iter(rows))
    mock_session.__aenter__ = AsyncMock(return_value=mock_session)
    mock_session.__aexit__ = AsyncMock(return_value=None)
    return mock_session


def _emote_row(stable_id: str, self_message: str, other_message: str):
    row = MagicMock()
    row.stable_id = stable_id
    row.self_message = self_message
    row.other_message = other_message
    return row


def _alias_row(stable_id: str, alias: str):
    row = MagicMock()
    row.stable_id = stable_id
    row.alias = alias
    return row


@pytest.mark.asyncio
async def test_get_emotes(repo):
    mock_session = _mock_session([_emote_row("twibble", "You twibble.", "{player_name} twibbles.")])
    with patch(
        "server.persistence.repositories.emote_repository.get_session_maker",
        return_value=MagicMock(return_value=mock_session),
    ):
        emotes = await repo.get_emotes()
    assert len(emotes) == 1
    assert emotes[0] == {
        "stable_id": "twibble",
        "self_message": "You twibble.",
        "other_message": "{player_name} twibbles.",
    }


@pytest.mark.asyncio
async def test_get_emotes_empty(repo):
    mock_session = _mock_session([])
    with patch(
        "server.persistence.repositories.emote_repository.get_session_maker",
        return_value=MagicMock(return_value=mock_session),
    ):
        emotes = await repo.get_emotes()
    assert emotes == []


@pytest.mark.asyncio
async def test_get_emotes_db_error(repo):
    mock_session = AsyncMock()
    mock_session.execute = AsyncMock(side_effect=SQLAlchemyError("fail"))
    mock_session.__aenter__ = AsyncMock(return_value=mock_session)
    mock_session.__aexit__ = AsyncMock(return_value=None)
    with patch(
        "server.persistence.repositories.emote_repository.get_session_maker",
        return_value=MagicMock(return_value=mock_session),
    ):
        with pytest.raises(DatabaseError):
            await repo.get_emotes()


@pytest.mark.asyncio
async def test_get_emote_aliases(repo):
    mock_session = _mock_session([_alias_row("twibble", "tw")])
    with patch(
        "server.persistence.repositories.emote_repository.get_session_maker",
        return_value=MagicMock(return_value=mock_session),
    ):
        aliases = await repo.get_emote_aliases()
    assert aliases == [{"stable_id": "twibble", "alias": "tw"}]


@pytest.mark.asyncio
async def test_get_emote_aliases_db_error(repo):
    mock_session = AsyncMock()
    mock_session.execute = AsyncMock(side_effect=SQLAlchemyError("fail"))
    mock_session.__aenter__ = AsyncMock(return_value=mock_session)
    mock_session.__aexit__ = AsyncMock(return_value=None)
    with patch(
        "server.persistence.repositories.emote_repository.get_session_maker",
        return_value=MagicMock(return_value=mock_session),
    ):
        with pytest.raises(DatabaseError):
            await repo.get_emote_aliases()
