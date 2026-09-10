"""Tests for the typed mock helpers in server/tests/support.py (#784)."""

from __future__ import annotations

import pytest

from server.tests.support import async_mock_of, calls_of, mock_of


class _Subject:
    """Stand-in for a service under test."""

    def resolve(self, value: int) -> str:
        return str(value)

    async def fetch(self, key: str) -> int:
        return len(key)


def test_mock_of_answers_the_subject_interface() -> None:
    double = mock_of(_Subject)
    double.resolve(3)
    calls_of(double).resolve.assert_called_once_with(3)


def test_mock_of_uses_spec_set_so_unknown_attributes_are_rejected() -> None:
    """spec_set (not spec) is the whole point: a renamed attribute must fail loudly."""
    double = mock_of(_Subject)
    with pytest.raises(AttributeError):
        double.no_such_method  # noqa: B018  # Reason: attribute read is the behaviour under test
    with pytest.raises(AttributeError):
        double.no_such_method = 1  # spec_set rejects writes too, unlike spec


@pytest.mark.asyncio
async def test_async_mock_of_returns_awaitable_members() -> None:
    double = async_mock_of(_Subject)
    calls_of(double).fetch.return_value = 7
    assert await double.fetch("abc") == 7
    calls_of(double).fetch.assert_awaited_once_with("abc")


def test_calls_of_rejects_a_non_mock() -> None:
    """Guards against calls_of() silently handing back a real object typed as a mock."""
    with pytest.raises(AssertionError, match="expects a mock"):
        calls_of(_Subject())
