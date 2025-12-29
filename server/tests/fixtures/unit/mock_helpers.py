"""
Strict mocking helpers for unit tests.

Provides fixtures and helpers that default to autospec=True to reduce
mock drift and catch interface mismatches.
"""

from collections.abc import Callable
from typing import Any

import pytest
from pytest_mock import MockerFixture  # type: ignore[import-not-found]  # pytest-mock doesn't have type stubs


@pytest.fixture
def strict_mocker(mocker: MockerFixture) -> Callable[..., Any]:
    """
    Return a patch helper that enables autospec by default.

    Usage:
        patched_fn = strict_mocker("server.module.fn")
    """

    def _patch(target: str, **kwargs: Any):
        kwargs.setdefault("autospec", True)
        return mocker.patch(target, **kwargs)

    return _patch


def strict_patch(mocker: MockerFixture, target: str, **kwargs: Any):
    """
    Convenience helper for direct calls with autospec=True by default.
    """
    kwargs.setdefault("autospec", True)
    return mocker.patch(target, **kwargs)
