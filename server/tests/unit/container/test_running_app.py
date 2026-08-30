"""Unit tests for server.container.running_app (#757: avoids npc/ -> services/ import cycle)."""

import sys
from collections.abc import Generator
from types import ModuleType
from unittest.mock import MagicMock

import pytest

from server.container.running_app import (
    combat_service_from_running_app,
    npc_instance_service_from_running_app,
)


@pytest.fixture(autouse=True)
def _restore_server_main() -> Generator[None, None, None]:  # pyright: ignore[reportUnusedFunction] - pytest autouse
    """Ensure a stubbed server.main module doesn't leak into other tests."""
    original = sys.modules.get("server.main")
    yield
    if original is not None:
        sys.modules["server.main"] = original
    else:
        _ = sys.modules.pop("server.main", None)


def _install_fake_main(app: object) -> None:
    fake_main = ModuleType("server.main")
    setattr(fake_main, "app", app)  # noqa: B010  # ModuleType has no static `app` attribute
    sys.modules["server.main"] = fake_main


def test_combat_service_from_running_app_returns_service_when_available() -> None:
    """Returns app.state.container.combat_service when the container has one wired up."""
    combat_service = MagicMock(name="combat_service")
    app = MagicMock()
    app.state.container.combat_service = combat_service
    _install_fake_main(app)

    assert combat_service_from_running_app() is combat_service


def test_combat_service_from_running_app_returns_none_without_container() -> None:
    """Returns None (not an AttributeError) when app.state.container is None."""
    app = MagicMock()
    app.state.container = None
    _install_fake_main(app)

    assert combat_service_from_running_app() is None


def test_combat_service_from_running_app_returns_none_without_app_state() -> None:
    """Returns None when the app object itself has no .state (pre-lifespan startup edge case)."""
    app = object()  # no .state attribute at all
    _install_fake_main(app)

    assert combat_service_from_running_app() is None


def test_npc_instance_service_from_running_app_returns_service(monkeypatch: pytest.MonkeyPatch) -> None:
    """Returns the process-wide singleton from get_npc_instance_service() when initialized."""
    npc_instance_service = MagicMock(name="npc_instance_service")
    fake_module = ModuleType("server.services.npc_instance_service")
    setattr(fake_module, "get_npc_instance_service", lambda: npc_instance_service)  # noqa: B010
    monkeypatch.setitem(sys.modules, "server.services.npc_instance_service", fake_module)

    assert npc_instance_service_from_running_app() is npc_instance_service


def test_npc_instance_service_from_running_app_returns_none_when_uninitialized(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """Startup-order case: get_npc_instance_service() raises before the bundle initializes it."""

    def _raise() -> object:
        raise RuntimeError("NPC instance service not initialized")

    fake_module = ModuleType("server.services.npc_instance_service")
    setattr(fake_module, "get_npc_instance_service", _raise)  # noqa: B010
    monkeypatch.setitem(sys.modules, "server.services.npc_instance_service", fake_module)

    assert npc_instance_service_from_running_app() is None
