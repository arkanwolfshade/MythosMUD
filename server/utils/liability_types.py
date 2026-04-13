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
class DecodeLiabilitiesFn(Protocol):
    def __call__(self, payload: str | None) -> list[LiabilityStackEntry]: ...


class EncodeLiabilitiesFn(Protocol):
    def __call__(self, entries: Sequence[LiabilityStackEntry]) -> str: ...


__all__ = ["DecodeLiabilitiesFn", "EncodeLiabilitiesFn", "LiabilityStackEntry"]
