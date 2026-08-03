"""Unit tests for DialogueDefinitionRepository."""

from __future__ import annotations

from datetime import UTC, datetime
from types import SimpleNamespace
from unittest.mock import AsyncMock, MagicMock, patch

import pytest
from sqlalchemy.exc import SQLAlchemyError

from server.exceptions import DatabaseError
from server.persistence.repositories.dialogue_definition_repository import (
    DialogueDefinitionRepository,
    _definition_dict,
    _row_to_dialogue,
)


def test_definition_dict_non_dict() -> None:
    assert _definition_dict("not a dict") == {}


def test_definition_dict_coerces_keys() -> None:
    assert _definition_dict({1: "a", "b": 2}) == {"1": "a", "b": 2}


def test_row_to_dialogue() -> None:
    now = datetime.now(UTC)
    row = SimpleNamespace(
        id="dlg_1",
        definition={"start": "greeting", "nodes": {}},
        npc_definition_id=7,
        created_at=now,
        updated_at=now,
    )
    dialogue = _row_to_dialogue(row)
    assert dialogue.id == "dlg_1"
    assert dialogue.npc_definition_id == 7


@pytest.fixture
def repo() -> DialogueDefinitionRepository:
    return DialogueDefinitionRepository()


def _mock_session_with_rows(rows: list[object]) -> AsyncMock:
    mock_session = AsyncMock()
    mock_result = MagicMock()
    mock_result.mappings.return_value.all.return_value = rows
    mock_result.mappings.return_value.first.return_value = rows[0] if rows else None
    mock_session.execute = AsyncMock(return_value=mock_result)
    mock_session.commit = AsyncMock()
    mock_session.__aenter__ = AsyncMock(return_value=mock_session)
    mock_session.__aexit__ = AsyncMock(return_value=None)
    return mock_session


@pytest.mark.asyncio
async def test_list_all_success(repo: DialogueDefinitionRepository) -> None:
    now = datetime.now(UTC)
    row = SimpleNamespace(
        id="t1",
        definition={"start": "greeting", "nodes": {}},
        npc_definition_id=1,
        created_at=now,
        updated_at=now,
    )
    mock_session = _mock_session_with_rows([row])

    with patch(
        "server.persistence.repositories.dialogue_definition_repository.get_session_maker",
        return_value=MagicMock(return_value=mock_session),
    ):
        dialogues = await repo.list_all()

    assert len(dialogues) == 1
    assert dialogues[0].id == "t1"


@pytest.mark.asyncio
async def test_list_all_db_error(repo: DialogueDefinitionRepository) -> None:
    mock_session = AsyncMock()
    mock_session.execute = AsyncMock(side_effect=SQLAlchemyError("fail"))
    mock_session.__aenter__ = AsyncMock(return_value=mock_session)
    mock_session.__aexit__ = AsyncMock(return_value=None)

    with patch(
        "server.persistence.repositories.dialogue_definition_repository.get_session_maker",
        return_value=MagicMock(return_value=mock_session),
    ):
        with pytest.raises(DatabaseError):
            await repo.list_all()


@pytest.mark.asyncio
async def test_get_by_id_found(repo: DialogueDefinitionRepository) -> None:
    now = datetime.now(UTC)
    row = SimpleNamespace(
        id="t1",
        definition={},
        npc_definition_id=None,
        created_at=now,
        updated_at=now,
    )
    mock_session = _mock_session_with_rows([row])

    with patch(
        "server.persistence.repositories.dialogue_definition_repository.get_session_maker",
        return_value=MagicMock(return_value=mock_session),
    ):
        dialogue = await repo.get_by_id("t1")

    assert dialogue is not None
    assert dialogue.id == "t1"


@pytest.mark.asyncio
async def test_get_by_id_not_found(repo: DialogueDefinitionRepository) -> None:
    mock_session = _mock_session_with_rows([])

    with patch(
        "server.persistence.repositories.dialogue_definition_repository.get_session_maker",
        return_value=MagicMock(return_value=mock_session),
    ):
        assert await repo.get_by_id("missing") is None


@pytest.mark.asyncio
async def test_get_by_npc_definition_id_found(repo: DialogueDefinitionRepository) -> None:
    now = datetime.now(UTC)
    row = SimpleNamespace(
        id="t2",
        definition={},
        npc_definition_id=99,
        created_at=now,
        updated_at=now,
    )
    mock_session = _mock_session_with_rows([row])

    with patch(
        "server.persistence.repositories.dialogue_definition_repository.get_session_maker",
        return_value=MagicMock(return_value=mock_session),
    ):
        dialogue = await repo.get_by_npc_definition_id(99)

    assert dialogue is not None
    assert dialogue.npc_definition_id == 99


@pytest.mark.asyncio
async def test_upsert_success(repo: DialogueDefinitionRepository) -> None:
    now = datetime.now(UTC)
    row = SimpleNamespace(
        id="t3",
        definition={"start": "greeting", "nodes": {}},
        npc_definition_id=5,
        created_at=now,
        updated_at=now,
    )
    mock_session = _mock_session_with_rows([row])

    with patch(
        "server.persistence.repositories.dialogue_definition_repository.get_session_maker",
        return_value=MagicMock(return_value=mock_session),
    ):
        dialogue = await repo.upsert("t3", {"start": "greeting", "nodes": {}}, npc_definition_id=5)

    assert dialogue.id == "t3"
    mock_session.commit.assert_awaited_once()


@pytest.mark.asyncio
async def test_delete_true(repo: DialogueDefinitionRepository) -> None:
    mock_session = AsyncMock()
    mock_result = MagicMock()
    mock_result.mappings.return_value.first.return_value = {"deleted": True}
    mock_session.execute = AsyncMock(return_value=mock_result)
    mock_session.commit = AsyncMock()
    mock_session.__aenter__ = AsyncMock(return_value=mock_session)
    mock_session.__aexit__ = AsyncMock(return_value=None)

    with patch(
        "server.persistence.repositories.dialogue_definition_repository.get_session_maker",
        return_value=MagicMock(return_value=mock_session),
    ):
        deleted = await repo.delete("t1")

    assert deleted is True


@pytest.mark.asyncio
async def test_delete_not_found(repo: DialogueDefinitionRepository) -> None:
    mock_session = AsyncMock()
    mock_result = MagicMock()
    mock_result.mappings.return_value.first.return_value = None
    mock_session.execute = AsyncMock(return_value=mock_result)
    mock_session.commit = AsyncMock()
    mock_session.__aenter__ = AsyncMock(return_value=mock_session)
    mock_session.__aexit__ = AsyncMock(return_value=None)

    with patch(
        "server.persistence.repositories.dialogue_definition_repository.get_session_maker",
        return_value=MagicMock(return_value=mock_session),
    ):
        assert await repo.delete("missing") is False
