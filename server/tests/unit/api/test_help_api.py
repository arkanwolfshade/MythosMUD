"""Unit tests for the help API (GET /v1/api/help)."""

# pyright: reportPrivateUsage=false
# Reason: _register_v1_routers is the registration point under test.

import uuid
from typing import cast

import pytest
from fastapi import FastAPI
from fastapi.routing import APIRoute
from pydantic import TypeAdapter

from server.api.help import get_help_docs, help_router
from server.api.item_catalog import user_is_admin
from server.app.factory import _register_v1_routers
from server.auth.users import get_current_user
from server.help.help_content import HelpDocs, get_manual
from server.models.user import User


def _user(*, is_superuser: bool) -> User:
    return User(
        id=uuid.uuid4(),
        username="testuser",
        email="test@example.com",
        hashed_password="hashed",
        is_active=True,
        is_superuser=is_superuser,
        is_verified=True,
    )


@pytest.mark.asyncio
async def test_a_player_gets_the_documentation_without_admin_commands() -> None:
    docs = await get_help_docs(_user(is_superuser=False))

    names = {cmd["name"] for cmd in docs["commands"]}
    assert "look" in names
    assert "npc" not in names
    assert "shutdown" not in names


@pytest.mark.asyncio
async def test_an_admin_also_gets_the_admin_commands() -> None:
    docs = await get_help_docs(_user(is_superuser=True))

    names = {cmd["name"] for cmd in docs["commands"]}
    assert {"look", "npc", "shutdown"} <= names


def test_the_response_model_round_trips_the_documentation_as_json() -> None:
    """FastAPI validates and serialises the return value through the response model; do the same here."""
    adapter = TypeAdapter(HelpDocs)

    body = cast(
        dict[str, list[dict[str, object]]], adapter.dump_python(adapter.validate_python(get_manual()), mode="json")
    )

    by_name = {cmd["name"]: cmd for cmd in body["commands"]}
    assert by_name["look"]["category"] == "Exploration"
    assert by_name["local"]["aliases"] == ["l"]
    assert "aliases" not in by_name["time"]  # NotRequired keys stay absent, not null


def test_the_router_produces_a_valid_openapi_schema() -> None:
    app = FastAPI()
    app.include_router(help_router)

    assert "/api/help" in cast(dict[str, object], app.openapi()["paths"])


def test_user_is_admin_accepts_superusers_and_rejects_everyone_else() -> None:
    assert user_is_admin(_user(is_superuser=True)) is True
    assert user_is_admin(_user(is_superuser=False)) is False


def test_the_v1_router_registers_the_help_route() -> None:
    app = FastAPI()

    _register_v1_routers(app)

    # The OpenAPI schema is the public surface; FastAPI wraps included routers, so app.routes is opaque.
    assert "/v1/api/help" in cast(dict[str, object], app.openapi()["paths"])


def test_the_route_is_mounted_and_requires_authentication() -> None:
    route = next(r for r in help_router.routes if isinstance(r, APIRoute) and r.path == "/api/help")

    assert route.methods == {"GET"}
    assert get_current_user in {dependency.call for dependency in route.dependant.dependencies}
