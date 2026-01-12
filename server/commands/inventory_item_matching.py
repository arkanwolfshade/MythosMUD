"""Item matching utilities for inventory commands."""

from collections.abc import Mapping
from typing import Any


def extract_item_identifier(stack: dict[str, Any], key: str) -> str | None:
    """Extract and normalize item identifier from stack."""
    value = stack.get(key)
    if isinstance(value, str):
        stripped = value.strip()
        return stripped if stripped else None
    return None


def build_drop_candidates(drop_list: list[dict[str, Any]]) -> list[tuple[int, str | None, str | None, str | None]]:
    """Build list of candidate tuples (index, item_name, item_id, prototype_id)."""
    candidates: list[tuple[int, str | None, str | None, str | None]] = []
    for idx, stack in enumerate(drop_list):
        item_name = extract_item_identifier(stack, "item_name")
        item_id = extract_item_identifier(stack, "item_id")
        prototype_id = extract_item_identifier(stack, "prototype_id")
        candidates.append((idx, item_name, item_id, prototype_id))
    return candidates


def match_exact_drop(candidates: list[tuple[int, str | None, str | None, str | None]], normalized: str) -> int | None:
    """Match by exact identifier (item_name, item_id, or prototype_id)."""
    for idx, item_name, item_id, prototype_id in candidates:
        for candidate in (item_name, item_id, prototype_id):
            if candidate and candidate.lower() == normalized:
                return idx
    return None


def match_prefix_drop(candidates: list[tuple[int, str | None, str | None, str | None]], normalized: str) -> int | None:
    """Match by prefix: first item_name, then item_id/prototype_id."""
    for idx, item_name, _item_id, _prototype_id in candidates:
        if item_name and item_name.lower().startswith(normalized):
            return idx

    for idx, _item_name, item_id, prototype_id in candidates:
        for candidate in (item_id, prototype_id):
            if candidate and candidate.lower().startswith(normalized):
                return idx
    return None


def match_substring_drop(
    candidates: list[tuple[int, str | None, str | None, str | None]], normalized: str
) -> int | None:
    """Match by substring containment in any identifier."""
    for idx, item_name, item_id, prototype_id in candidates:
        for candidate in (item_name, item_id, prototype_id):
            if candidate and normalized in candidate.lower():
                return idx
    return None


def match_room_drop_by_name(drop_list: list[dict[str, Any]], search_term: str) -> int | None:
    """
    Resolve a room drop index using Lovecraftian-grade fuzzy matching heuristics.

    Human collaborators: we prefer exact identifiers, then courteous prefix matches, before falling back
    to substring containment—echoing the cataloguing rites described in Dr. Wilmarth's Restricted Archives.
    Agentic aides: return a zero-based index for the best candidate or None if no alignment is found.
    """
    normalized = search_term.strip().lower()
    if not normalized:
        return None

    candidates = build_drop_candidates(drop_list)

    # Try exact match first
    match = match_exact_drop(candidates, normalized)
    if match is not None:
        return match

    # Try prefix match
    match = match_prefix_drop(candidates, normalized)
    if match is not None:
        return match

    # Fall back to substring match
    return match_substring_drop(candidates, normalized)


def build_inventory_candidates(
    inventory: list[dict[str, Any]],
) -> list[tuple[int, str | None, str | None, str | None]]:
    """Build list of candidate tuples (index, item_name, item_id, prototype_id) from inventory."""
    candidates: list[tuple[int, str | None, str | None, str | None]] = []
    for idx, stack in enumerate(inventory):
        item_name = extract_item_identifier(stack, "item_name")
        item_id = extract_item_identifier(stack, "item_id")
        prototype_id = extract_item_identifier(stack, "prototype_id")
        candidates.append((idx, item_name, item_id, prototype_id))
    return candidates


def match_inventory_item_by_name(inventory: list[dict[str, Any]], search_term: str) -> int | None:
    """
    Resolve an inventory index from a fuzzy name search.

    Human scholars: this mirrors the ritual we employ for room drops, prioritising exact designations
    before leaning on sympathetic naming. Agentic aides: return a zero-based index when the augury aligns,
    otherwise yield None.
    """
    normalized = search_term.strip().lower()
    if not normalized:
        return None

    candidates = build_inventory_candidates(inventory)

    # Try exact match first
    match = match_exact_drop(candidates, normalized)
    if match is not None:
        return match

    # Try prefix match
    match = match_prefix_drop(candidates, normalized)
    if match is not None:
        return match

    # Fall back to substring match
    return match_substring_drop(candidates, normalized)


def normalize_slot_name(slot: str | None) -> str | None:
    """Normalize equipment slot identifiers to lowercase snake_case."""

    if slot is None:
        return None
    normalized = slot.strip().lower()
    return normalized or None


def clean_item_value(value: str | None) -> str | None:
    """Clean item value for matching. Returns cleaned string or None."""
    if isinstance(value, str):
        stripped = value.strip()
        return stripped if stripped else None
    return None


def build_equipped_candidates(
    equipped: Mapping[str, Mapping[str, Any]],
) -> list[tuple[str, str | None, str | None, str | None]]:
    """Build list of candidates from equipped items. Returns list of (slot_key, item_name, item_id, prototype_id)."""
    candidates: list[tuple[str, str | None, str | None, str | None]] = []
    for slot_name, stack in equipped.items():
        item_name = stack.get("item_name")
        item_id = stack.get("item_id")
        prototype_id = stack.get("prototype_id")

        candidates.append(
            (
                normalize_slot_name(slot_name) or slot_name,
                clean_item_value(item_name),
                clean_item_value(item_id),
                clean_item_value(prototype_id),
            )
        )
    return candidates


def search_exact_match(
    candidates: list[tuple[str, str | None, str | None, str | None]], normalized_term: str
) -> str | None:
    """Search for exact match. Returns slot_key if found, None otherwise."""
    for slot_key, item_name, item_id, prototype_id in candidates:
        for candidate in (item_name, item_id, prototype_id):
            if candidate and candidate.lower() == normalized_term:
                return slot_key
    return None


def search_prefix_match(
    candidates: list[tuple[str, str | None, str | None, str | None]], normalized_term: str
) -> str | None:
    """Search for prefix match. Returns slot_key if found, None otherwise."""
    for slot_key, item_name, item_id, prototype_id in candidates:
        for candidate in (item_name, item_id, prototype_id):
            if candidate and candidate.lower().startswith(normalized_term):
                return slot_key
    return None


def search_substring_match(
    candidates: list[tuple[str, str | None, str | None, str | None]], normalized_term: str
) -> str | None:
    """Search for substring match. Returns slot_key if found, None otherwise."""
    for slot_key, item_name, item_id, prototype_id in candidates:
        for candidate in (item_name, item_id, prototype_id):
            if candidate and normalized_term in candidate.lower():
                return slot_key
    return None


def match_equipped_item_by_name(equipped: Mapping[str, Mapping[str, Any]], search_term: str) -> str | None:
    """
    Resolve an equipped slot identifier via fuzzy item name search.

    Scholars: we invoke the same sympathetic naming rites used for inventory and room drops.
    Agents: return the normalized slot key when a match is found; otherwise None.
    """
    normalized_term = search_term.strip().lower()
    if not normalized_term:
        return None

    candidates = build_equipped_candidates(equipped)

    result = search_exact_match(candidates, normalized_term)
    if result:
        return result

    result = search_prefix_match(candidates, normalized_term)
    if result:
        return result

    result = search_substring_match(candidates, normalized_term)
    if result:
        return result

    return None
