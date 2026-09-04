"""
Strict mocking helpers for unit tests.

Provides fixtures and helpers that default to autospec=True to reduce
mock drift and catch interface mismatches.
"""

from collections.abc import Callable
from typing import Any
from unittest.mock import MagicMock

import pytest
from pytest_mock import MockerFixture


@pytest.fixture
def strict_mocker(mocker: MockerFixture) -> Callable[..., Any]:
    """
    Return a patch helper that enables autospec by default.

    Usage:
        patched_fn = strict_mocker("server.module.fn")
    """

    def _patch(target: str, **kwargs: Any) -> MagicMock:
        kwargs.setdefault("autospec", True)
        return mocker.patch(target, **kwargs)  # type: ignore[no-any-return]  # Reason: mocker.patch returns Any, but we declare MagicMock for type safety

    return _patch


def strict_patch(mocker: MockerFixture, target: str, **kwargs: Any) -> MagicMock:
    """
    Convenience helper for direct calls with autospec=True by default.
    """
    kwargs.setdefault("autospec", True)
    return mocker.patch(target, **kwargs)  # type: ignore[no-any-return]  # Reason: mocker.patch returns Any, but we declare MagicMock for type safety
