"""Unit tests for server.api.professions."""

import uuid
from typing import cast
from unittest.mock import AsyncMock, MagicMock

import pytest
from fastapi import Request

from server.api.professions import get_all_professions, get_profession_by_id
from server.exceptions import LoggedHTTPException
from server.models.user import User


def _user() -> MagicMock:
    u = MagicMock()
    u.id = uuid.uuid4()
    return u


_PROF_DICT: dict[str, object] = {
    "id": 1,
    "name": "Investigator",
    "description": "Desc",
    "flavor_text": None,
    "stat_requirements": cast(list[object], []),
    "mechanical_effects": cast(list[object], []),
    "is_available": True,
}


@pytest.mark.asyncio
async def test_get_all_professions_requires_auth() -> None:
    svc = MagicMock()
    with pytest.raises(LoggedHTTPException) as ei:
        # Endpoint checks `if not current_user`; Depends types it as User only.
        _ = await get_all_professions(
            MagicMock(spec=Request),
            cast(User, cast(object, None)),
            svc,
        )
    assert ei.value.status_code == 401


@pytest.mark.asyncio
async def test_get_all_professions_success() -> None:
    svc = MagicMock()
    svc.get_all_professions_dict = AsyncMock(return_value=[_PROF_DICT])
    out = await get_all_professions(MagicMock(spec=Request), _user(), svc)
    assert len(out.professions) == 1
    assert out.professions[0].name == "Investigator"


@pytest.mark.asyncio
async def test_get_profession_by_id_not_found() -> None:
    svc = MagicMock()
    svc.get_profession_by_id_dict = AsyncMock(return_value=None)
    with pytest.raises(LoggedHTTPException) as ei:
        _ = await get_profession_by_id(99, MagicMock(spec=Request), _user(), svc)
    assert ei.value.status_code == 404


@pytest.mark.asyncio
async def test_get_profession_by_id_success() -> None:
    svc = MagicMock()
    svc.get_profession_by_id_dict = AsyncMock(return_value=_PROF_DICT)
    out = await get_profession_by_id(1, MagicMock(spec=Request), _user(), svc)
    assert out.id == 1
