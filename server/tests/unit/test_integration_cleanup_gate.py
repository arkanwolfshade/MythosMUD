"""
Unit tests for the integration-cleanup gate (#949).

The integration fixture plugin is loaded for every test, and its autouse db_cleanup deletes every
mutable table. Once #949 made that cleanup work again, running it after each unit test made the
server suite ~9x slower; the gate limits it to tests that actually touch the database.
"""

# pyright: reportPrivateUsage=false
# Reason: this module tests the integration fixtures' private gate helper directly.

from collections.abc import Callable
from typing import cast

import pytest

from server.tests.fixtures.integration import _test_touches_database


class _Node:
    def __init__(self, markers: set[str]) -> None:
        self._markers: set[str] = markers

    def get_closest_marker(self, name: str) -> object | None:
        return name if name in self._markers else None


class _Request:
    def __init__(self, markers: set[str], function: Callable[..., object] | None) -> None:
        self.node: _Node = _Node(markers)
        self.function: Callable[..., object] | None = function


def _request(markers: set[str], function: Callable[..., object] | None) -> pytest.FixtureRequest:
    return cast(pytest.FixtureRequest, cast(object, _Request(markers, function)))


def _plain_unit_test() -> None:
    return None


def _unit_test_using_db(session_factory: object) -> None:
    _ = session_factory


def test_integration_marked_test_is_cleaned_up() -> None:
    assert _test_touches_database(_request({"integration"}, _plain_unit_test)) is True


def test_unit_test_that_asks_for_session_factory_is_cleaned_up() -> None:
    assert _test_touches_database(_request({"unit"}, _unit_test_using_db)) is True


def test_plain_unit_test_skips_cleanup() -> None:
    assert _test_touches_database(_request({"unit"}, _plain_unit_test)) is False


def test_request_without_a_test_function_skips_cleanup() -> None:
    assert _test_touches_database(_request(set(), None)) is False
