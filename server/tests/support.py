"""Typed mock helpers shared across the server test suite (#784).

``MagicMock(spec=X)`` is *statically* typed as ``MagicMock``, so every attribute read off it is
``Any``. The ``spec=`` argument buys runtime safety (unknown attributes raise) and exactly zero
static safety. That is why ``server/tests`` carries thousands of ``reportAny`` findings against
only a handful of shared fixtures: the type is lost at each of ~16k inline mock constructions.

``mock_of`` fixes that at one shared definition. The object really is a ``MagicMock`` at runtime,
and really does answer the ``T`` interface (``spec_set`` enforces it), but Python has no
intersection type to say "both" -- so each helper commits to one half and the cast names which.

Preference order for test doubles stays unchanged, per the project's standing rule:
real domain objects > small hand-written typed fakes > ``Protocol`` > ``TypedDict`` > ``mock_of``.
Reach for these helpers when a real object is genuinely impractical -- never to manufacture a
one-off ``Protocol`` or stack casts just to quiet a report.
"""

from __future__ import annotations

from typing import TypeVar, cast
from unittest.mock import AsyncMock, MagicMock, NonCallableMock

# PEP 695 (`def mock_of[T](...)`) is the modern spelling and ruff's UP047 prefers it, but Codacy's
# containerised PyLintPython3 runs an older parser that fails with
# "Parsing failed: expected '('" on the type-parameter list. The repo's 12 other generics all use
# TypeVar, so match them; UP047 is disabled for this file in [tool.ruff.lint.per-file-ignores].
T = TypeVar("T")


def mock_of(cls: type[T]) -> T:
    """A ``MagicMock`` restricted to ``cls``'s interface, typed as ``cls``.

    ``spec_set`` (not ``spec``) is deliberate: it rejects *writes* to attributes the real class
    does not define, so a renamed attribute fails the test instead of silently recording a call
    on a mock nobody reads. The cast is honest -- the object answers exactly ``cls``'s surface.

    Use ``calls_of()`` on the result when you need the assertion API back::

        service = mock_of(CombatService)
        service.resolve_attack(attacker, target)
        calls_of(service).resolve_attack.assert_called_once()
    """
    return cast(T, MagicMock(spec_set=cls))


def async_mock_of(cls: type[T]) -> T:
    """``mock_of`` for classes whose methods are coroutines.

    ``AsyncMock(spec_set=...)`` makes every awaitable member return a coroutine, so awaiting a
    method on the double works without per-method ``AsyncMock()`` assignment.
    """
    return cast(T, AsyncMock(spec_set=cls))


def calls_of(obj: object) -> MagicMock:
    """Recover the ``MagicMock`` assertion API from a double typed as its subject.

    The inverse of ``mock_of``: that cast hid the mock behind ``T`` so production-shaped calls
    type-check, and this one hands back ``assert_called_once_with`` and friends. Only ever pass an
    object that really is a mock -- there is no runtime check beyond the assertion below.
    """
    assert isinstance(obj, NonCallableMock), (  # noqa: S101
        f"calls_of() expects a mock created by mock_of()/async_mock_of(); got {type(obj).__name__}"
    )
    return cast(MagicMock, obj)
