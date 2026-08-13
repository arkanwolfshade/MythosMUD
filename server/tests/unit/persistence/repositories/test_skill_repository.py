"""Unit tests for SkillRepository."""

from __future__ import annotations

from types import SimpleNamespace
from unittest.mock import AsyncMock, MagicMock, patch

import pytest
from sqlalchemy.exc import SQLAlchemyError

from server.exceptions import DatabaseError
from server.persistence.repositories.skill_repository import SkillRepository, _row_to_skill


@pytest.fixture
def repo() -> SkillRepository:
    return SkillRepository()


def test_row_to_skill_defaults() -> None:
    row = SimpleNamespace(
        id=1,
        key=None,
        name=None,
        description="desc",
        base_value=None,
        allow_at_creation=None,
        category="knowledge",
    )
    skill = _row_to_skill(row)
    assert skill.key == ""
    assert skill.name == ""
    assert skill.base_value == 0
    assert skill.allow_at_creation is True


@pytest.mark.asyncio
async def test_get_all_skills_success(repo: SkillRepository) -> None:
    mock_session = AsyncMock()
    mock_result = MagicMock()
    mock_result.mappings.return_value.all.return_value = [
        SimpleNamespace(
            id=1,
            key="spot",
            name="Spot Hidden",
            description="desc",
            base_value=25,
            allow_at_creation=True,
            category="perception",
        )
    ]
    mock_session.execute = AsyncMock(return_value=mock_result)
    mock_session.__aenter__ = AsyncMock(return_value=mock_session)
    mock_session.__aexit__ = AsyncMock(return_value=None)

    with patch(
        "server.persistence.repositories.skill_repository.get_session_maker",
        return_value=MagicMock(return_value=mock_session),
    ):
        skills = await repo.get_all_skills()

    assert len(skills) == 1
    assert skills[0].key == "spot"


@pytest.mark.asyncio
async def test_get_all_skills_db_error(repo: SkillRepository) -> None:
    mock_session = AsyncMock()
    mock_session.execute = AsyncMock(side_effect=SQLAlchemyError("fail"))
    mock_session.__aenter__ = AsyncMock(return_value=mock_session)
    mock_session.__aexit__ = AsyncMock(return_value=None)

    with patch(
        "server.persistence.repositories.skill_repository.get_session_maker",
        return_value=MagicMock(return_value=mock_session),
    ):
        with pytest.raises(DatabaseError):
            await repo.get_all_skills()


@pytest.mark.asyncio
async def test_get_skill_by_id_found(repo: SkillRepository) -> None:
    mock_session = AsyncMock()
    mock_result = MagicMock()
    mock_result.mappings.return_value.first.return_value = SimpleNamespace(
        id=2,
        key="library_use",
        name="Library Use",
        description=None,
        base_value=5,
        allow_at_creation=False,
        category="knowledge",
    )
    mock_session.execute = AsyncMock(return_value=mock_result)
    mock_session.__aenter__ = AsyncMock(return_value=mock_session)
    mock_session.__aexit__ = AsyncMock(return_value=None)

    with patch(
        "server.persistence.repositories.skill_repository.get_session_maker",
        return_value=MagicMock(return_value=mock_session),
    ):
        skill = await repo.get_skill_by_id(2)

    assert skill is not None
    assert skill.key == "library_use"


@pytest.mark.asyncio
async def test_get_skill_by_id_not_found(repo: SkillRepository) -> None:
    mock_session = AsyncMock()
    mock_result = MagicMock()
    mock_result.mappings.return_value.first.return_value = None
    mock_session.execute = AsyncMock(return_value=mock_result)
    mock_session.__aenter__ = AsyncMock(return_value=mock_session)
    mock_session.__aexit__ = AsyncMock(return_value=None)

    with patch(
        "server.persistence.repositories.skill_repository.get_session_maker",
        return_value=MagicMock(return_value=mock_session),
    ):
        assert await repo.get_skill_by_id(999) is None


@pytest.mark.asyncio
async def test_get_skill_by_id_db_error(repo: SkillRepository) -> None:
    mock_session = AsyncMock()
    mock_session.execute = AsyncMock(side_effect=SQLAlchemyError("fail"))
    mock_session.__aenter__ = AsyncMock(return_value=mock_session)
    mock_session.__aexit__ = AsyncMock(return_value=None)

    with patch(
        "server.persistence.repositories.skill_repository.get_session_maker",
        return_value=MagicMock(return_value=mock_session),
    ):
        with pytest.raises(DatabaseError):
            await repo.get_skill_by_id(1)


@pytest.mark.asyncio
async def test_get_skill_by_key_found(repo: SkillRepository) -> None:
    mock_session = AsyncMock()
    mock_result = MagicMock()
    mock_result.mappings.return_value.first.return_value = SimpleNamespace(
        id=3,
        key="accounting",
        name="Accounting",
        description="ledgers",
        base_value=5,
        allow_at_creation=True,
        category="knowledge",
    )
    mock_session.execute = AsyncMock(return_value=mock_result)
    mock_session.__aenter__ = AsyncMock(return_value=mock_session)
    mock_session.__aexit__ = AsyncMock(return_value=None)

    with patch(
        "server.persistence.repositories.skill_repository.get_session_maker",
        return_value=MagicMock(return_value=mock_session),
    ):
        skill = await repo.get_skill_by_key("accounting")

    assert skill is not None
    assert skill.name == "Accounting"


@pytest.mark.asyncio
async def test_get_skill_by_key_not_found(repo: SkillRepository) -> None:
    mock_session = AsyncMock()
    mock_result = MagicMock()
    mock_result.mappings.return_value.first.return_value = None
    mock_result = MagicMock()
    mock_result.mappings.return_value.first.return_value = None
    mock_session.execute = AsyncMock(return_value=mock_result)
    mock_session.__aenter__ = AsyncMock(return_value=mock_session)
    mock_session.__aexit__ = AsyncMock(return_value=None)

    with patch(
        "server.persistence.repositories.skill_repository.get_session_maker",
        return_value=MagicMock(return_value=mock_session),
    ):
        assert await repo.get_skill_by_key("missing") is None


@pytest.mark.asyncio
async def test_get_skill_by_key_db_error(repo: SkillRepository) -> None:
    mock_session = AsyncMock()
    mock_session.execute = AsyncMock(side_effect=SQLAlchemyError("fail"))
    mock_session.__aenter__ = AsyncMock(return_value=mock_session)
    mock_session.__aexit__ = AsyncMock(return_value=None)

    with patch(
        "server.persistence.repositories.skill_repository.get_session_maker",
        return_value=MagicMock(return_value=mock_session),
    ):
        with pytest.raises(DatabaseError):
            await repo.get_skill_by_key("spot")
