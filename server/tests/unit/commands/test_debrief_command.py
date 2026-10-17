"""Unit tests for the (parked) debrief command: context validation, args handling, and delegation to the service."""

from __future__ import annotations

import uuid
from dataclasses import dataclass, field
from types import SimpleNamespace
from typing import cast

import pytest

from server.commands import debrief_command as command
from server.models.player import Player
from server.services.debrief_service import DebriefOutcome


@dataclass
class FakePersistence:
    player: Player | None
    lookups: list[str] = field(default_factory=lambda: cast(list[str], []))

    async def get_player_by_name(self, name: str) -> Player | None:
        self.lookups.append(name)
        return self.player

    async def save_player(self, player: object) -> object:  # pragma: no cover - never reached
        return player


def _player() -> Player:
    return Player(player_id=str(uuid.uuid4()), name="Tester")


def _request(persistence: FakePersistence | None, registry: object | None = None) -> object:
    container = SimpleNamespace(async_persistence=persistence, catatonia_registry=registry)
    return SimpleNamespace(app=SimpleNamespace(state=SimpleNamespace(container=container)))


@dataclass
class ServiceCalls:
    calls: list[tuple[Player, bool, object | None]] = field(
        default_factory=lambda: cast(list[tuple[Player, bool, object | None]], [])
    )


@pytest.fixture(name="service")
def _service(monkeypatch: pytest.MonkeyPatch) -> ServiceCalls:
    recorded = ServiceCalls()

    async def fake_perform(
        player: Player, *, wants_therapy: bool = False, catatonia_observer: object | None = None
    ) -> DebriefOutcome:
        recorded.calls.append((player, wants_therapy, catatonia_observer))
        return DebriefOutcome("Staff recap.", completed=True)

    monkeypatch.setattr(command, "perform_debrief", fake_perform)
    return recorded


@pytest.mark.asyncio
async def test_validate_context_fails_without_persistence() -> None:
    player, error = await command._validate_debrief_context(None, "alice", "alice")  # pyright: ignore[reportPrivateUsage]

    assert player is None
    assert error is not None
    assert "inaccessible" in error["result"]


@pytest.mark.asyncio
async def test_validate_context_fails_for_an_unknown_player() -> None:
    player, error = await command._validate_debrief_context(  # pyright: ignore[reportPrivateUsage]
        FakePersistence(None), "ghost", "ghost"
    )

    assert player is None
    assert error is not None
    assert "identity wavers" in error["result"]


@pytest.mark.asyncio
async def test_the_command_reports_missing_persistence(service: ServiceCalls) -> None:
    result = await command.handle_debrief_command({}, {"username": "alice"}, _request(None), None, "alice")

    assert "inaccessible" in result["result"]
    assert service.calls == []


@pytest.mark.asyncio
async def test_the_command_delegates_to_the_debrief_service(service: ServiceCalls) -> None:
    player, registry = _player(), object()

    result = await command.handle_debrief_command(
        {}, {"username": "alice"}, _request(FakePersistence(player), registry), None, "alice"
    )

    assert result == {"result": "Staff recap."}
    assert service.calls == [(player, False, registry)]


@pytest.mark.asyncio
@pytest.mark.parametrize(
    ("args", "expected"),
    [
        (["therapy"], True),  # the shape the real pipeline produces: a list
        (["Y"], True),
        (["t", "extra"], True),
        ("yes", True),  # a bare string is still accepted
        ([], False),
        (["no"], False),
        ("", False),
        ([None], False),
    ],
)
async def test_args_may_be_a_list_or_a_string(service: ServiceCalls, args: object, expected: bool) -> None:
    """Regression for #872: ``args`` is a list in the real pipeline; ``.lower()`` on it raised AttributeError."""
    _ = await command.handle_debrief_command(
        {"args": args}, {"username": "alice"}, _request(FakePersistence(_player())), None, "alice"
    )

    assert service.calls[0][1] is expected


def test_the_catatonia_registry_falls_back_to_app_state() -> None:
    registry = object()
    app = SimpleNamespace(state=SimpleNamespace(container=None, catatonia_registry=registry))

    assert command._get_catatonia_registry_from_app(app) is registry  # pyright: ignore[reportPrivateUsage]
    assert command._get_catatonia_registry_from_app(None) is None  # pyright: ignore[reportPrivateUsage]
