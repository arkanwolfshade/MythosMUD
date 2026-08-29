# pyright: reportPrivateUsage=false
# Tests import players.py helpers that are module-private by convention.
"""Unit tests for server.api.players helpers and core list/create paths."""

import uuid
from typing import cast
from unittest.mock import AsyncMock, MagicMock

import pytest
from fastapi import Request

from server.api.players import (
    _disconnect_other_characters,
    _get_connection_manager,
    _validate_character_access,
    _validate_character_id,
    _validate_player_for_grace_period,
    create_player,
    get_class_description,
    list_players,
)
from server.exceptions import LoggedHTTPException, ValidationError
from server.schemas.players.player_requests import SelectCharacterRequest


def _user(*, is_superuser: bool = True) -> MagicMock:
    u = MagicMock()
    u.id = uuid.uuid4()
    u.username = "test-admin"
    u.is_superuser = is_superuser
    return u


def test_get_class_description_known_and_fallback() -> None:
    assert "researcher" in get_class_description("investigator").lower()
    assert "unknown" in get_class_description("custom_unknown").lower()


def test_validate_character_id_accepts_uuid_string() -> None:
    u = _user()
    cid = str(uuid.uuid4())
    assert _validate_character_id(cid, MagicMock(spec=Request), u) == uuid.UUID(cid)


def test_validate_character_id_rejects_bad_format() -> None:
    u = _user()
    with pytest.raises(LoggedHTTPException) as ei:
        _ = _validate_character_id("not-a-uuid", MagicMock(spec=Request), u)
    assert ei.value.status_code == 400


def test_get_connection_manager_from_app_state() -> None:
    cm: MagicMock = MagicMock()
    container: MagicMock = MagicMock()
    container.connection_manager = cm
    state: MagicMock = MagicMock()
    state.container = container
    app: MagicMock = MagicMock()
    app.state = state
    req: MagicMock = MagicMock(spec=Request)
    req.app = app
    assert _get_connection_manager(req) is cm


def test_get_connection_manager_none_without_container() -> None:
    state: MagicMock = MagicMock()
    state.container = None
    app: MagicMock = MagicMock()
    app.state = state
    req: MagicMock = MagicMock(spec=Request)
    req.app = app
    assert _get_connection_manager(req) is None


@pytest.mark.asyncio
async def test_validate_character_access_success() -> None:
    char: MagicMock = MagicMock()
    svc: MagicMock = MagicMock()
    validate_m: AsyncMock = AsyncMock(return_value=(True, char, ""))
    svc.validate_character_access = validate_m
    result: MagicMock = cast(
        MagicMock,
        await _validate_character_access(uuid.uuid4(), _user(), MagicMock(spec=Request), svc),
    )
    assert result is char


@pytest.mark.asyncio
async def test_validate_character_access_not_found() -> None:
    svc = MagicMock()
    svc.validate_character_access = AsyncMock(return_value=(False, None, "Player not found here"))
    with pytest.raises(LoggedHTTPException) as ei:
        await _validate_character_access(uuid.uuid4(), _user(), MagicMock(spec=Request), svc)
    assert ei.value.status_code == 404


@pytest.mark.asyncio
async def test_validate_character_access_wrong_owner() -> None:
    svc = MagicMock()
    svc.validate_character_access = AsyncMock(return_value=(False, None, "Character does not belong to user"))
    with pytest.raises(LoggedHTTPException) as ei:
        await _validate_character_access(uuid.uuid4(), _user(), MagicMock(spec=Request), svc)
    assert ei.value.status_code == 403


@pytest.mark.asyncio
async def test_validate_player_for_grace_period_deleted() -> None:
    svc = MagicMock()
    svc.validate_character_access = AsyncMock(return_value=(False, None, "Character deleted"))
    with pytest.raises(LoggedHTTPException) as ei:
        await _validate_player_for_grace_period(uuid.uuid4(), _user(), MagicMock(spec=Request), svc)
    assert ei.value.status_code == 404


@pytest.mark.asyncio
async def test_disconnect_other_characters_no_manager() -> None:
    await _disconnect_other_characters(uuid.uuid4(), _user(), None, MagicMock())
    # no exception


@pytest.mark.asyncio
async def test_disconnect_other_characters_disconnects_peer() -> None:
    selected = uuid.uuid4()
    other = uuid.uuid4()
    other_char = MagicMock()
    other_char.id = other
    cm: MagicMock = MagicMock()
    cm.player_websockets = {other: MagicMock()}
    disconnect_ws: AsyncMock = AsyncMock()
    cm.disconnect_websocket = disconnect_ws
    svc: MagicMock = MagicMock()
    get_chars: AsyncMock = AsyncMock(return_value=[other_char])
    svc.get_user_characters = get_chars
    await _disconnect_other_characters(selected, _user(), cm, svc)
    disconnect_ws.assert_awaited_once()


@pytest.mark.asyncio
async def test_create_player_success() -> None:
    svc = MagicMock()
    created = MagicMock()
    svc.create_player = AsyncMock(return_value=created)
    out = await create_player("Hero", MagicMock(spec=Request), "room_1", _user(), svc)
    assert out is created


@pytest.mark.asyncio
async def test_create_player_validation_error_to_400() -> None:
    svc = MagicMock()
    svc.create_player = AsyncMock(side_effect=ValidationError("bad name"))
    with pytest.raises(LoggedHTTPException) as ei:
        _ = await create_player("x", MagicMock(spec=Request), "room_1", _user(), svc)
    assert ei.value.status_code == 400


@pytest.mark.asyncio
async def test_create_player_rejects_non_superuser() -> None:
    """#734: no client caller uses this endpoint; it's admin-only, not self-service."""
    from fastapi import HTTPException

    svc = MagicMock()
    with pytest.raises(HTTPException) as ei:
        _ = await create_player("Hero", MagicMock(spec=Request), "room_1", _user(is_superuser=False), svc)
    assert ei.value.status_code == 403
    assert svc.mock_calls == []


@pytest.mark.asyncio
async def test_list_players_requires_auth() -> None:
    svc = MagicMock()
    with pytest.raises(LoggedHTTPException) as ei:
        _ = await list_players(MagicMock(spec=Request), None, svc)
    assert ei.value.status_code == 401


@pytest.mark.asyncio
async def test_list_players_returns_list() -> None:
    svc = MagicMock()
    svc.list_players = AsyncMock(return_value=[MagicMock()])
    out = await list_players(MagicMock(spec=Request), _user(), svc)
    assert len(out) == 1


@pytest.mark.asyncio
async def test_get_available_classes() -> None:
    from server.api.players import get_available_classes

    gen = MagicMock()
    gen.CLASS_PREREQUISITES = {"investigator": {}}
    gen.MIN_STAT = 1
    gen.MAX_STAT = 99
    out = await get_available_classes(_user(), gen)
    assert "investigator" in out.classes


@pytest.mark.asyncio
async def test_get_player_not_found() -> None:
    from server.api.players import get_player

    svc = MagicMock()
    svc.get_player_by_id = AsyncMock(return_value=None)
    with pytest.raises(LoggedHTTPException) as ei:
        await get_player(uuid.uuid4(), MagicMock(spec=Request), _user(), svc)
    assert ei.value.status_code == 404


@pytest.mark.asyncio
async def test_get_player_success() -> None:
    from server.api.players import get_player

    player = MagicMock()
    svc = MagicMock()
    svc.get_player_by_id = AsyncMock(return_value=player)
    out = await get_player(uuid.uuid4(), MagicMock(spec=Request), _user(), svc)
    assert out is player


@pytest.mark.asyncio
async def test_get_player_by_name_success() -> None:
    from server.api.players import get_player_by_name

    player = MagicMock()
    svc = MagicMock()
    svc.get_player_by_name = AsyncMock(return_value=player)
    out = await get_player_by_name("Hero", MagicMock(spec=Request), _user(), svc)
    assert out is player


@pytest.mark.asyncio
async def test_get_player_rejects_non_owner_non_admin() -> None:
    """#734: PlayerRead carries user_id/stats/inventory/is_admin -- not public game data."""
    from server.api.players import get_player

    owner = _user(is_superuser=False)
    owner.is_admin = False
    other_caller = _user(is_superuser=False)
    other_caller.is_admin = False

    player = MagicMock()
    player.user_id = owner.id
    svc = MagicMock()
    svc.get_player_by_id = AsyncMock(return_value=player)

    with pytest.raises(LoggedHTTPException) as ei:
        await get_player(uuid.uuid4(), MagicMock(spec=Request), other_caller, svc)
    assert ei.value.status_code == 403


@pytest.mark.asyncio
async def test_get_player_allows_owner() -> None:
    from server.api.players import get_player

    owner = _user(is_superuser=False)
    owner.is_admin = False

    player = MagicMock()
    player.user_id = owner.id
    svc = MagicMock()
    svc.get_player_by_id = AsyncMock(return_value=player)

    out = await get_player(uuid.uuid4(), MagicMock(spec=Request), owner, svc)
    assert out is player


@pytest.mark.asyncio
async def test_get_user_characters_success() -> None:
    from server.api.players import get_user_characters

    svc = MagicMock()
    svc.get_user_characters = AsyncMock(return_value=[MagicMock()])
    out = await get_user_characters(MagicMock(spec=Request), _user(), svc)
    assert len(out) == 1


@pytest.mark.asyncio
async def test_get_player_skills_success() -> None:
    from server.api.players import get_player_skills

    svc = MagicMock()
    svc.get_player_skills = AsyncMock(return_value=[{"skill_id": 1, "skill_key": "k", "skill_name": "N", "value": 1}])
    out = await get_player_skills(uuid.uuid4(), MagicMock(spec=Request), _user(), svc)
    assert len(out.skills) == 1


@pytest.mark.asyncio
async def test_get_player_skills_forbidden() -> None:
    from server.api.players import get_player_skills

    svc = MagicMock()
    svc.get_player_skills = AsyncMock(return_value=None)
    with pytest.raises(LoggedHTTPException) as ei:
        await get_player_skills(uuid.uuid4(), MagicMock(spec=Request), _user(), svc)
    assert ei.value.status_code == 403


@pytest.mark.asyncio
async def test_get_player_quests_success() -> None:
    from server.api.players import get_player_quests

    player_svc = MagicMock()
    player_svc.validate_character_access = AsyncMock(return_value=(True, MagicMock(), ""))
    quest_svc = MagicMock()
    quest_svc.get_quest_log = AsyncMock(
        return_value=[
            {
                "quest_id": "quest-1",
                "name": "q",
                "title": "T",
                "description": "d",
                "goals_with_progress": [],
                "state": "active",
            }
        ]
    )
    out = await get_player_quests(uuid.uuid4(), MagicMock(spec=Request), _user(), player_svc, quest_svc)
    assert len(out.quests) == 1


@pytest.mark.asyncio
async def test_get_player_quests_forbidden() -> None:
    from server.api.players import get_player_quests

    player_svc = MagicMock()
    player_svc.validate_character_access = AsyncMock(return_value=(False, None, "does not belong"))
    quest_svc = MagicMock()
    with pytest.raises(LoggedHTTPException) as ei:
        await get_player_quests(uuid.uuid4(), MagicMock(spec=Request), _user(), player_svc, quest_svc)
    assert ei.value.status_code == 403


@pytest.mark.asyncio
async def test_delete_player_success() -> None:
    from server.api.players import delete_player

    svc = MagicMock()
    svc.delete_player = AsyncMock(return_value=(True, "deleted"))
    out = await delete_player(uuid.uuid4(), MagicMock(spec=Request), _user(), svc)
    assert out.message == "deleted"


@pytest.mark.asyncio
async def test_delete_player_not_found() -> None:
    from server.api.players import delete_player

    svc = MagicMock()
    svc.delete_player = AsyncMock(return_value=(False, "missing"))
    with pytest.raises(LoggedHTTPException) as ei:
        await delete_player(uuid.uuid4(), MagicMock(spec=Request), _user(), svc)
    assert ei.value.status_code == 404


@pytest.mark.asyncio
async def test_delete_player_validation_error() -> None:
    from server.api.players import delete_player

    svc = MagicMock()
    svc.delete_player = AsyncMock(side_effect=ValidationError("bad"))
    with pytest.raises(LoggedHTTPException) as ei:
        await delete_player(uuid.uuid4(), MagicMock(spec=Request), _user(), svc)
    assert ei.value.status_code == 404


@pytest.mark.asyncio
async def test_delete_player_rejects_non_superuser() -> None:
    """#734: raw-by-UUID deletion, no ownership check; must be admin-gated."""
    from fastapi import HTTPException

    from server.api.players import delete_player

    svc = MagicMock()
    with pytest.raises(HTTPException) as ei:
        await delete_player(uuid.uuid4(), MagicMock(spec=Request), _user(is_superuser=False), svc)
    assert ei.value.status_code == 403
    assert svc.mock_calls == []


@pytest.mark.asyncio
async def test_delete_character_success() -> None:
    from server.api.players import delete_character

    svc = MagicMock()
    svc.soft_delete_character = AsyncMock(return_value=(True, "gone"))
    out = await delete_character(str(uuid.uuid4()), MagicMock(spec=Request), _user(), svc)
    assert out.success is True


@pytest.mark.asyncio
async def test_delete_character_invalid_id() -> None:
    from server.api.players import delete_character

    svc = MagicMock()
    with pytest.raises(LoggedHTTPException) as ei:
        await delete_character("not-uuid", MagicMock(spec=Request), _user(), svc)
    assert ei.value.status_code == 400


@pytest.mark.asyncio
async def test_select_character_success() -> None:
    from server.api.players import select_character

    char_id = uuid.uuid4()
    character = MagicMock()
    svc = MagicMock()
    svc.validate_character_access = AsyncMock(return_value=(True, character, ""))
    req = MagicMock(spec=Request)
    req.app.state.container = None
    out = await select_character(
        SelectCharacterRequest(character_id=str(char_id)),
        req,
        _user(),
        svc,
    )
    assert out is character
