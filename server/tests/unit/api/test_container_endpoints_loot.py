"""
Unit tests for the loot-all endpoint.

The endpoint hands the whole loot to ContainerService.loot_all, one player-registry unit of work (ADR-029 step 4b;
the loot itself is tested in tests/unit/services/test_container_transfers.py), then reports the result.
"""

from __future__ import annotations

import uuid
from collections.abc import Awaitable, Callable
from dataclasses import dataclass, field
from types import SimpleNamespace
from typing import cast

import pytest
from fastapi import APIRouter, FastAPI, Request
from fastapi.routing import APIRoute

from server.api.container_endpoints_loot import loot_all_items, register_loot_endpoints
from server.api.container_models import LootAllRequest
from server.exceptions import LoggedHTTPException
from server.game.player_registry import PlayerRegistry
from server.models.container import ContainerComponent, ContainerSourceType
from server.services.container_service import (
    ContainerCapacityError,
    ContainerLockedError,
    ContainerNotFoundError,
    LootAllResult,
)
from server.tests.fixtures.shared.player_registry import FakeDatabase

CID = uuid.uuid4()
PID = uuid.uuid4()
TORCH: dict[str, object] = {
    "item_instance_id": "torch-1",
    "prototype_id": "torch",
    "item_id": "torch",
    "item_name": "Torch",
    "slot_type": "backpack",
    "quantity": 1,
}


@dataclass
class _User:
    id: uuid.UUID = field(default_factory=uuid.uuid4)


@dataclass
class _Service:
    """ContainerService's loot_all, recording what it was asked."""

    outcome: LootAllResult | Exception
    calls: list[tuple[uuid.UUID, uuid.UUID, str, PlayerRegistry]] = field(default_factory=list)

    async def loot_all(
        self, container_id: uuid.UUID, player_id: uuid.UUID, mutation_token: str, *, registry: PlayerRegistry
    ) -> LootAllResult:
        self.calls.append((container_id, player_id, mutation_token, registry))
        if isinstance(self.outcome, Exception):
            raise self.outcome
        return self.outcome


def _request(app: FastAPI | None = None) -> Request:
    scope: dict[str, object] = {"type": "http", "method": "POST", "path": "/loot-all", "headers": []}
    if app is not None:
        scope["app"] = app
    return Request(scope)


def _empty_container() -> ContainerComponent:
    return ContainerComponent.model_validate(
        {
            "container_id": str(CID),
            "room_id": "earth_arkhamcity_sanitarium_room_foyer_001",
            "source_type": ContainerSourceType.ENVIRONMENT.value,
            "capacity_slots": 10,
            "items": [],
        }
    )


def _install(monkeypatch: pytest.MonkeyPatch, service: _Service) -> list[object]:
    """Route the endpoint's lookups to ``service``; returns what it emits, in order."""
    emitted: list[object] = []

    async def player_id(_user: object, _persistence: object) -> uuid.UUID:
        return PID

    async def emit(
        _cm: object, _request_data: object, container: ContainerComponent, _pid: object, items_removed: int
    ) -> None:
        emitted.append((container, items_removed))

    monkeypatch.setattr("server.api.container_endpoints_loot.get_player_id_from_user", player_id)

    def container_service(_persistence: object) -> _Service:
        return service

    monkeypatch.setattr("server.api.container_endpoints_loot.get_container_service", container_service)

    async def snapshot(
        _cm: object, _pid: object, inventory: list[dict[str, object]], equipped: dict[str, object]
    ) -> None:
        emitted.append(("inventory", inventory, equipped))

    monkeypatch.setattr("server.api.container_endpoints_loot.emit_loot_all_event", emit)
    monkeypatch.setattr("server.api.container_endpoints_loot.emit_inventory_snapshot", snapshot)
    return emitted


async def test_loot_all_hands_the_whole_loot_to_the_service(monkeypatch: pytest.MonkeyPatch) -> None:
    container = _empty_container()
    service = _Service(LootAllResult(container=container, player_inventory=[TORCH], player_equipped={}, items_looted=2))
    emitted = _install(monkeypatch, service)
    registry = PlayerRegistry(FakeDatabase().session)

    response = await loot_all_items(
        LootAllRequest(container_id=CID, mutation_token="token"), _request(), _User(), None, None, registry
    )

    assert service.calls == [(CID, PID, "token", registry)]
    # The inventory first: the client's transfer pane must never offer a stack the player no longer holds.
    assert emitted == [("inventory", [TORCH], {}), (container, 2)]
    assert response.items_looted == 2
    assert [stack.item_id for stack in response.player_inventory] == ["torch"]


async def test_an_unauthenticated_loot_is_refused(monkeypatch: pytest.MonkeyPatch) -> None:
    service = _Service(RuntimeError("never called"))
    _ = _install(monkeypatch, service)

    with pytest.raises(LoggedHTTPException) as refused:
        _ = await loot_all_items(
            LootAllRequest(container_id=CID, mutation_token="token"),
            _request(),
            None,
            None,
            None,
            PlayerRegistry(FakeDatabase().session),
        )

    assert refused.value.status_code == 401
    assert service.calls == []


@pytest.mark.parametrize(
    ("error", "status_code"),
    [
        (ContainerNotFoundError("gone"), 404),
        (ContainerLockedError("locked"), 423),
        (ContainerCapacityError("full"), 409),
        (RuntimeError("boom"), 500),
    ],
)
async def test_a_failed_loot_maps_to_its_status(
    monkeypatch: pytest.MonkeyPatch, error: Exception, status_code: int
) -> None:
    _ = _install(monkeypatch, _Service(error))

    with pytest.raises(LoggedHTTPException) as failed:
        _ = await loot_all_items(
            LootAllRequest(container_id=CID, mutation_token="token"),
            _request(),
            _User(),
            None,
            None,
            PlayerRegistry(FakeDatabase().session),
        )

    assert failed.value.status_code == status_code


async def test_the_route_is_post_loot_all_and_passes_the_apps_registry(monkeypatch: pytest.MonkeyPatch) -> None:
    router = APIRouter()
    register_loot_endpoints(router)
    [route] = router.routes
    assert isinstance(route, APIRoute)
    assert route.path == "/loot-all" and route.methods == {"POST"}

    registry = PlayerRegistry(FakeDatabase().session)
    app = FastAPI()
    app.state.container = SimpleNamespace(player_registry=registry)
    seen: list[PlayerRegistry] = []

    async def loot(*args: object) -> None:
        seen.append(cast(PlayerRegistry, args[-1]))

    monkeypatch.setattr("server.api.container_endpoints_loot.loot_all_items", loot)
    endpoint = cast(Callable[..., Awaitable[object]], route.endpoint)
    _ = await endpoint(
        LootAllRequest(container_id=CID, mutation_token="token"),
        _request(app),
        current_user=_User(),
        persistence=None,
        connection_manager=None,
    )

    assert seen == [registry]
