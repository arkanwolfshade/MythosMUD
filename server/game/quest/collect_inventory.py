"""
Inventory helpers for collect_n quest goals.

Counts and consumes items by prototype id across top-level stacks and nested
embedded inner_container.items. UUID-backed wearable containers are out of
scope for v1 (ponytail: add container-service walk if holdings miss bag loot).
"""

from __future__ import annotations

from copy import deepcopy
from typing import Any


def _stack_prototype_id(stack: dict[str, Any]) -> str:
    """Return prototype id from a stack dict."""
    raw = stack.get("prototype_id") or stack.get("item_id") or ""
    return str(raw)


def _stack_quantity(stack: dict[str, Any]) -> int:
    """Return non-negative quantity for a stack."""
    try:
        qty = int(stack.get("quantity", 1) or 1)
    except (TypeError, ValueError):
        return 1
    return max(qty, 0)


def _nested_item_dicts(stack: dict[str, Any]) -> list[dict[str, Any]] | None:
    """Return inner_container.items as dicts, or None if absent."""
    inner = stack.get("inner_container")
    if not isinstance(inner, dict):
        return None
    nested = inner.get("items") or []
    if not isinstance(nested, list):
        return None
    return [item for item in nested if isinstance(item, dict)]


def count_prototype_in_stacks(stacks: list[dict[str, Any]], prototype_id: str) -> int:
    """
    Count holdings of prototype_id in stacks, including nested inner_container.items.

    Args:
        stacks: Inventory and/or equipped item stacks.
        prototype_id: Item prototype id to match.

    Returns:
        Total quantity held.
    """
    total = 0
    for stack in stacks:
        if _stack_prototype_id(stack) == prototype_id:
            total += _stack_quantity(stack)
        nested = _nested_item_dicts(stack)
        if nested is not None:
            total += count_prototype_in_stacks(nested, prototype_id)
    return total


def _dict_stacks_from_callable(getter: Any) -> list[dict[str, Any]]:
    """Call getter if present; return list of dict stacks."""
    if not callable(getter):
        return []
    value = getter() or []
    if not isinstance(value, list):
        return []
    return [item for item in value if isinstance(item, dict)]


def _dict_stacks_from_equipped(getter: Any) -> list[dict[str, Any]]:
    """Call equipped getter if present; return equipped stack dicts."""
    if not callable(getter):
        return []
    equipped = getter() or {}
    if not isinstance(equipped, dict):
        return []
    return [item for item in equipped.values() if isinstance(item, dict)]


def collect_player_stacks(player: Any) -> list[dict[str, Any]]:
    """Build a list of inventory + equipped stacks for counting."""
    stacks = _dict_stacks_from_callable(getattr(player, "get_inventory", None))
    stacks.extend(_dict_stacks_from_equipped(getattr(player, "get_equipped_items", None)))
    return stacks


def _consume_from_stack_list(stacks: list[dict[str, Any]], prototype_id: str, remaining: int) -> int:
    """Mutate stacks in place; return units still needed."""
    if remaining <= 0:
        return 0
    index = 0
    while index < len(stacks) and remaining > 0:
        stack = stacks[index]
        if _stack_prototype_id(stack) == prototype_id:
            qty = _stack_quantity(stack)
            if qty <= remaining:
                remaining -= qty
                stacks.pop(index)
                continue
            stack["quantity"] = qty - remaining
            return 0
        nested = _nested_item_dicts(stack)
        if nested is not None:
            remaining = _consume_from_stack_list(nested, prototype_id, remaining)
            inner = stack.get("inner_container")
            if isinstance(inner, dict):
                inner["items"] = nested
        index += 1
    return remaining


def _deepcopy_dict_stacks(items: list[Any]) -> list[dict[str, Any]]:
    """Deep-copy stack dicts from a raw inventory list."""
    return [deepcopy(item) for item in items if isinstance(item, dict)]


def _deepcopy_equipped_map(equipped: dict[Any, Any]) -> dict[str, dict[str, Any]]:
    """Deep-copy equipped slot map keeping only dict stacks."""
    return {str(slot): deepcopy(item) for slot, item in equipped.items() if isinstance(item, dict)}


def _snapshot_holdings(player: Any) -> tuple[list[dict[str, Any]], dict[str, dict[str, Any]]]:
    """Deep-copy inventory list and equipped map from player."""
    get_inventory = getattr(player, "get_inventory", None)
    get_equipped = getattr(player, "get_equipped_items", None)
    inventory_src = list(get_inventory() or []) if callable(get_inventory) else []
    equipped_src = dict(get_equipped() or {}) if callable(get_equipped) else {}
    return _deepcopy_dict_stacks(inventory_src), _deepcopy_equipped_map(equipped_src)


def _consume_from_equipped(equipped: dict[str, dict[str, Any]], prototype_id: str, remaining: int) -> int:
    """Consume from equipped slots; mutate equipped in place."""
    for slot in list(equipped.keys()):
        if remaining <= 0:
            break
        bucket = [equipped[slot]]
        remaining = _consume_from_stack_list(bucket, prototype_id, remaining)
        if not bucket:
            del equipped[slot]
        else:
            equipped[slot] = bucket[0]
    return remaining


def _apply_holdings(player: Any, inventory: list[dict[str, Any]], equipped: dict[str, dict[str, Any]]) -> None:
    """Write inventory and equipped back onto player."""
    set_inventory = getattr(player, "set_inventory", None)
    if callable(set_inventory):
        set_inventory(inventory)
    set_equipped = getattr(player, "set_equipped_items", None)
    if callable(set_equipped):
        set_equipped(equipped)


def consume_prototype_from_player(player: Any, prototype_id: str, count: int) -> bool:
    """
    Remove count units of prototype_id from player inventory, then equipped.

    Returns True if fully consumed. On failure, player state is left unchanged.
    """
    if count <= 0:
        return True

    inventory, equipped = _snapshot_holdings(player)
    held = count_prototype_in_stacks(inventory + list(equipped.values()), prototype_id)
    if held < count:
        return False

    remaining = _consume_from_stack_list(inventory, prototype_id, count)
    if remaining > 0:
        remaining = _consume_from_equipped(equipped, prototype_id, remaining)
    if remaining > 0:
        return False

    _apply_holdings(player, inventory, equipped)
    return True
