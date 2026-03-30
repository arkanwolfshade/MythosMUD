"""Unit tests for inventory_service_helpers.get_shared_services."""

from __future__ import annotations

from collections.abc import Generator
from unittest.mock import MagicMock

import pytest

import server.commands.inventory_service_helpers as ish


@pytest.fixture(autouse=True)
def reset_shared_inventory_services_autouse() -> Generator[None, None, None]:
    ish.reset_shared_inventory_services_for_tests()
    yield
    ish.reset_shared_inventory_services_for_tests()


def _request_with_persistence(persistence: object | None) -> MagicMock:
    container = MagicMock()
    container.async_persistence = persistence
    state = MagicMock()
    state.container = container
    app = MagicMock()
    app.state = state
    req = MagicMock()
    req.app = app
    return req


def test_get_shared_services_raises_without_async_persistence() -> None:
    req = _request_with_persistence(None)
    with pytest.raises(ValueError, match="async_persistence"):
        _ = ish.get_shared_services(req)


def test_get_shared_services_initializes_and_reuses_singletons() -> None:
    pers = MagicMock()
    req = _request_with_persistence(pers)
    inv1, wear1, eq1 = ish.get_shared_services(req)
    inv2, wear2, eq2 = ish.get_shared_services(req)
    assert inv1 is inv2
    assert wear1 is wear2
    assert eq1 is eq2
