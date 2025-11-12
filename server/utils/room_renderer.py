"""
Room rendering utilities for MythosMUD.

Provides helpers for formatting room drop information so both command
handlers and realtime transports can present a consistent, lore-friendly
view of the detritus investigators leave behind.
"""

from __future__ import annotations

from collections.abc import Iterable, Mapping, Sequence
from copy import deepcopy
from typing import Any

DROP_INTRO_LINE = "Scattered upon the floor, you notice:"
DROP_EMPTY_LINE = "The floor bears no abandoned curios."


def _coerce_stack(stack: Mapping[str, Any]) -> tuple[str, str, int]:
    """Normalize stack fields for presentation."""
    item_name = str(stack.get("item_name") or stack.get("item_id") or "Uncatalogued Relic")
    slot_type = str(stack.get("slot_type") or "unknown")
    quantity_raw = stack.get("quantity", 0)
    try:
        quantity = int(quantity_raw)
    except (TypeError, ValueError):
        quantity = 0
    return item_name, slot_type, quantity


def format_room_drop_lines(drops: Sequence[Mapping[str, Any]] | None) -> list[str]:
    """
    Build human-readable lines describing room drops.

    Args:
        drops: An iterable of drop stack mappings.

    Returns:
        List[str]: Narrative lines suitable for terminal rendering.
    """
    safe_drops: Sequence[Mapping[str, Any]] = drops or ()
    if not safe_drops:
        return [DROP_EMPTY_LINE]

    lines = [DROP_INTRO_LINE]
    for index, stack in enumerate(safe_drops, start=1):
        item_name, slot_type, quantity = _coerce_stack(stack)
        lines.append(f"{index}. {item_name} x{quantity} ({slot_type})")
    return lines


def build_room_drop_summary(drops: Sequence[Mapping[str, Any]] | None) -> str:
    """Return a newline-separated textual summary of room drops."""
    return "\n".join(format_room_drop_lines(drops))


def clone_room_drops(drops: Iterable[Mapping[str, Any]] | None) -> list[dict[str, Any]]:
    """Deep copy room drop payloads to shield callers from mutation."""
    if not drops:
        return []
    return [deepcopy(dict(stack)) for stack in drops]
