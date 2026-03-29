"""Prototype registry access and equip-slot inference for inventory items."""

from __future__ import annotations

from collections.abc import Sequence
from typing import cast

from ..game.items.prototype_registry import PrototypeRegistryError
from .inventory_item_matching import normalize_slot_name


def prototype_registry_from_request(request: object) -> object | None:
    """Resolve prototype registry from FastAPI-style request (agent-readable indirection)."""
    app: object = cast(object, getattr(request, "app", None))
    if app is None:
        return None
    state: object = cast(object, getattr(app, "state", None))
    return cast(object, getattr(state, "prototype_registry", None)) if state is not None else None


def prototype_from_registry(registry: object, prototype_id: str) -> object | None:
    get_proto = getattr(registry, "get", None)
    if not callable(get_proto):
        return None
    try:
        return cast(object | None, get_proto(prototype_id))
    except PrototypeRegistryError:
        return None


def _inventory_prototype_id(selected_stack: dict[str, object]) -> str | None:
    if selected_stack.get("slot_type") != "inventory":
        return None
    prototype_raw = selected_stack.get("prototype_id") or selected_stack.get("item_id")
    return prototype_raw if isinstance(prototype_raw, str) else None


def _wear_slots_from_prototype(prototype: object) -> list[object]:
    wear_slots_raw: object = getattr(prototype, "wear_slots", [])
    if isinstance(wear_slots_raw, (list, tuple)):
        return list(cast(Sequence[object], wear_slots_raw))
    return []


def _first_normalized_wear_slot(wear_slots: list[object]) -> str | None:
    if not wear_slots:
        return None
    first: object = wear_slots[0]
    return normalize_slot_name(first) if isinstance(first, str) else normalize_slot_name(str(first))


def infer_equip_slot_from_prototype(request: object, selected_stack: dict[str, object]) -> str | None:
    """Infer equip slot from prototype wear_slots for inventory items."""
    prototype_id = _inventory_prototype_id(selected_stack)
    if not prototype_id:
        return None
    registry = prototype_registry_from_request(request)
    if registry is None:
        return None
    prototype = prototype_from_registry(registry, prototype_id)
    if prototype is None:
        return None
    return _first_normalized_wear_slot(_wear_slots_from_prototype(prototype))
