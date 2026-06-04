"""Shared TypedDicts for liability JSON stored on PlayerLucidity.liabilities."""

from collections.abc import Sequence
from typing import Protocol, TypedDict

# Normalized liability row (code + stack count). Functional form avoids Pyright/Pylance
# complaining that class-based TypedDict.__doc__ is incompatible with object.__doc__.
LiabilityStackEntry = TypedDict(  # noqa: UP013 -- keep functional syntax; class form triggers __doc__ override
    "LiabilityStackEntry",
    {
        "code": str,
        "stacks": int,
    },
)


# Protocols for injectable decode/encode callables. Pyright keeps concrete
# return types here better than Callable[..., SomeAlias] in other modules.
# Sequence (not Iterable) avoids reportUnknown* on TypedDict elements in __call__ params.
# Protocol stub bodies use Ellipsis per PEP 544; Pylint W2301 conflicts with pyright if replaced with pass.
# pylint: disable=unnecessary-ellipsis
class DecodeLiabilitiesFn(Protocol):
    """Callable that parses liability JSON into normalized stack entries."""

    def __call__(self, payload: str | None) -> list[LiabilityStackEntry]:
        """Decode stored liability text (or empty state) into stack rows."""
        ...


class EncodeLiabilitiesFn(Protocol):
    """Callable that serializes liability stack rows for persistence."""

    def __call__(self, entries: Sequence[LiabilityStackEntry]) -> str:
        """Encode stack rows into JSON suitable for PlayerLucidity.liabilities."""
        ...


__all__ = ["DecodeLiabilitiesFn", "EncodeLiabilitiesFn", "LiabilityStackEntry"]
