"""
INSTANCE_BOUND item stacks: items that belong only to the instance they were made for.

Pure functions over item-stack dicts (inventory, equipped, container and floor-drop stacks all share
that shape). Imports only constants, so the flush service, player state helpers and anything else
can use it without pulling in models or services.
"""

from __future__ import annotations

from collections.abc import Mapping
from typing import cast

from .constants import INSTANCE_BOUND_FLAG

Stack = dict[str, object]


def is_instance_bound_stack(stack: Mapping[str, object]) -> bool:
    """True if the stack's prototype is flagged INSTANCE_BOUND."""
    flags = stack.get("flags")
    return isinstance(flags, list) and INSTANCE_BOUND_FLAG in cast(list[object], flags)


def _inner_stacks(stack: Mapping[str, object]) -> list[Stack] | None:
    """Stacks held inside a carried container (inner_container.items), or None if it holds none."""
    inner = stack.get("inner_container")
    if not isinstance(inner, dict):
        return None
    items = cast(dict[str, object], inner).get("items")
    if not isinstance(items, list):
        return None
    return [cast(Stack, item) for item in cast(list[object], items) if isinstance(item, dict)]


def strip_instance_bound_stacks(stacks: list[Stack]) -> tuple[list[Stack], int]:
    """The stacks without INSTANCE_BOUND ones (also inside carried containers), and how many were removed.

    The input is not modified: a container that loses an item comes back as a copy.
    """
    kept: list[Stack] = []
    removed = 0
    for stack in stacks:
        if is_instance_bound_stack(stack):
            removed += 1
            continue
        inner = _inner_stacks(stack)
        if inner is not None:
            inner_kept, inner_removed = strip_instance_bound_stacks(inner)
            if inner_removed:
                removed += inner_removed
                stack = {**stack, "inner_container": {**cast(Stack, stack["inner_container"]), "items": inner_kept}}
        kept.append(stack)
    return kept, removed
