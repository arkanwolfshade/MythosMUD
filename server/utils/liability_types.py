"""The liability stack shape, stored as JSON in ``player_lucidity.liabilities``."""

from typing import TypedDict

# Normalized liability row (code + stack count). Functional form avoids Pyright/Pylance
# complaining that class-based TypedDict.__doc__ is incompatible with object.__doc__.
LiabilityStackEntry = TypedDict(  # noqa: UP013 -- keep functional syntax; class form triggers __doc__ override
    "LiabilityStackEntry",
    {
        "code": str,
        "stacks": int,
    },
)


__all__ = ["LiabilityStackEntry"]
