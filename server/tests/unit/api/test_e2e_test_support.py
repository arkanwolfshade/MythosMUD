"""Unit tests for the e2e test-support endpoints: where they are mounted, who may call them, and what they return."""

from __future__ import annotations

from types import SimpleNamespace
from typing import cast

import pytest
from fastapi import HTTPException
from fastapi.routing import APIRoute

from server.api.admin import e2e_test_support
from server.api.admin.e2e_test_support import (
    PlaceRequest,
    e2e_test_support_enabled,
    e2e_test_support_router,
    place_player,
    player_state,
    require_e2e_admin,
    reset_shared_players,
    reset_tutorial_character,
)
from server.models.user import User
from server.services.e2e_player_support import E2ePlayerState, E2ePlayerSupport, UnknownPlayerError, UnknownRoomError

STATE = E2ePlayerState(
    current_room_id="room_a",
    respawn_room_id=None,
    tutorial_instance_id=None,
    bank_items=["Ring"],
    current_dp=50,
    corruption=0,
    magic_points=None,
    max_magic_points=None,
    intelligence=None,
    current_lcd=100,
    inventory_items=["Sling"],
    quests={"q": "active"},
    debrief_pending=False,
)


def _user(*, admin: bool = False, superuser: bool = False) -> User:
    return cast(User, cast(object, SimpleNamespace(is_admin=admin, is_superuser=superuser)))


class _FakeSupport:  # stands in for E2ePlayerSupport
    def __init__(self) -> None:
        self.calls: list[tuple[str, ...]] = []

    async def reset_shared_players(self) -> None:
        self.calls.append(("reset",))

    async def reset_tutorial_character(self, name: str) -> None:
        if name == "Nobody":
            raise UnknownPlayerError(name)
        self.calls.append(("reset-tutorial", name))

    async def place(self, name: str, room_id: str) -> None:
        if name == "Nobody":
            raise UnknownPlayerError(name)
        if room_id == "no_such_room":
            raise UnknownRoomError(room_id)
        self.calls.append(("place", name, room_id))

    async def state(self, name: str) -> E2ePlayerState:
        if name == "Nobody":
            raise UnknownPlayerError(name)
        return STATE


def _support() -> tuple[_FakeSupport, E2ePlayerSupport]:
    fake = _FakeSupport()
    return fake, cast(E2ePlayerSupport, cast(object, fake))


@pytest.mark.parametrize(
    ("environment", "database_url", "expected"),
    [
        ("e2e_test", "postgresql+asyncpg://u:p@localhost:5432/mythos_e2e", True),
        ("e2e_test", "postgresql://u:p@localhost:5432/mythos_e2e?sslmode=disable", True),
        ("e2e_test", "postgresql+asyncpg://u:p@localhost:5432/mythos_dev", False),
        ("e2e_test", None, False),
        ("local", "postgresql+asyncpg://u:p@localhost:5432/mythos_e2e", False),
        ("unit_test", "postgresql+asyncpg://u:p@localhost:5432/mythos_unit", False),
    ],
)
def test_the_routes_are_mounted_only_for_the_e2e_environment_on_the_e2e_database(
    monkeypatch: pytest.MonkeyPatch, environment: str, database_url: str | None, expected: bool
) -> None:
    config = SimpleNamespace(
        logging=SimpleNamespace(environment=environment), database=SimpleNamespace(url=database_url or "")
    )
    monkeypatch.setattr(e2e_test_support, "get_config", lambda: config)

    assert e2e_test_support_enabled() is expected


def test_the_database_is_not_even_consulted_outside_the_e2e_environment(monkeypatch: pytest.MonkeyPatch) -> None:
    config = SimpleNamespace(logging=SimpleNamespace(environment="unit_test"))  # no `database`: reading it would fail
    monkeypatch.setattr(e2e_test_support, "get_config", lambda: config)

    assert e2e_test_support_enabled() is False


@pytest.mark.parametrize("user", [_user(admin=True), _user(superuser=True)])
def test_an_admin_or_superuser_passes_the_admin_check(user: User) -> None:
    assert require_e2e_admin(user) is user


def test_a_plain_player_is_refused_and_no_user_is_unauthorized() -> None:
    with pytest.raises(HTTPException) as plain:
        _ = require_e2e_admin(_user())
    with pytest.raises(HTTPException) as nobody:
        _ = require_e2e_admin(None)

    assert plain.value.status_code == 403
    assert nobody.value.status_code == 401


def test_the_admin_check_is_not_rate_limited() -> None:
    user = _user(admin=True)

    for _ in range(150):  # AdminAuthService allows 100 per five minutes; specs poll the state endpoint far more
        assert require_e2e_admin(user) is user


def test_every_route_requires_the_admin_check() -> None:
    routes = [route for route in e2e_test_support_router.routes if isinstance(route, APIRoute)]

    assert len(routes) == 4
    for route in routes:
        assert require_e2e_admin in [dependency.call for dependency in route.dependant.dependencies], route.path


async def test_reset_endpoints_call_the_support_and_answer_no_content() -> None:
    fake, support = _support()
    admin = _user(admin=True)

    shared = await reset_shared_players(admin, support)
    tutorial = await reset_tutorial_character("E2ETutorial", admin, support)

    assert shared.status_code == 204 and tutorial.status_code == 204
    assert fake.calls == [("reset",), ("reset-tutorial", "E2ETutorial")]


async def test_place_moves_the_character() -> None:
    fake, support = _support()

    response = await place_player("E2ETutorial", PlaceRequest(room_id="room_b"), _user(admin=True), support)

    assert response.status_code == 204
    assert fake.calls == [("place", "E2ETutorial", "room_b")]


@pytest.mark.parametrize(("name", "room_id"), [("Nobody", "room_b"), ("E2ETutorial", "no_such_room")])
async def test_placing_an_unknown_character_or_room_is_a_404(name: str, room_id: str) -> None:
    _fake, support = _support()

    with pytest.raises(HTTPException) as refused:
        _ = await place_player(name, PlaceRequest(room_id=room_id), _user(admin=True), support)

    assert refused.value.status_code == 404


async def test_resetting_an_unknown_character_is_a_404() -> None:
    _fake, support = _support()

    with pytest.raises(HTTPException) as refused:
        _ = await reset_tutorial_character("Nobody", _user(admin=True), support)

    assert refused.value.status_code == 404


async def test_state_returns_the_state_and_an_unknown_name_is_a_404() -> None:
    _fake, support = _support()
    admin = _user(admin=True)

    assert await player_state("E2ETutorial", admin, support) == STATE
    with pytest.raises(HTTPException) as refused:
        _ = await player_state("Nobody", admin, support)

    assert refused.value.status_code == 404
