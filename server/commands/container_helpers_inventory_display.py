"""Container display helpers for inventory UI (wearable contents, slot matching)."""

from __future__ import annotations

from collections.abc import Mapping
from typing import cast
from uuid import UUID

from ..models.player import Player
from ..services.inventory_service import InventoryStack
from .container_helpers_inventory_logging import logger
from .inventory_service_helpers import get_shared_services


def _inventory_stack_to_display_dict(stack: InventoryStack) -> dict[str, object]:
    """Shallow-copy a wearable stack into a plain dict for equipped-view metadata."""
    return dict(stack)


def _component_metadata(component: object) -> dict[str, object]:
    meta = getattr(component, "metadata", None)
    return cast(dict[str, object], meta) if isinstance(meta, dict) else {}


def _equipped_matches_container_metadata(
    equipped_item: Mapping[str, object],
    container_item_name: object | None,
    container_item_id: object | None,
) -> bool:
    equipped_item_name = equipped_item.get("item_name")
    equipped_item_id = equipped_item.get("item_id")
    name_ok = bool(container_item_name) and bool(equipped_item_name) and container_item_name == equipped_item_name
    id_ok = bool(container_item_id) and bool(equipped_item_id) and container_item_id == equipped_item_id
    return name_ok or id_ok


def match_container_to_slot(
    container_component: object,
    equipped_view: dict[str, dict[str, object]],
) -> str | None:
    """Match a container component to an equipped slot. Returns slot name or None."""
    container_metadata = _component_metadata(container_component)
    container_item_name = container_metadata.get("item_name")
    container_item_id = container_metadata.get("item_id")

    for slot_name, equipped_item in equipped_view.items():
        if _equipped_matches_container_metadata(equipped_item, container_item_name, container_item_id):
            logger.debug(
                "Found matching slot",
                matching_slot=slot_name,
                container_item_name=container_item_name,
                equipped_item_name=equipped_item.get("item_name"),
            )
            return slot_name

    logger.debug(
        "No matching slot found for container",
        container_item_name=container_item_name,
        container_item_id=container_item_id,
        equipped_slots=list(equipped_view.keys()),
    )
    return None


def _lock_state_as_str(lock_state: object) -> str:
    value = getattr(lock_state, "value", None)
    if isinstance(value, str):
        return value
    return str(lock_state)


async def _apply_container_component_to_slot(
    container_component: object,
    equipped_view: dict[str, dict[str, object]],
    container_contents: dict[str, list[dict[str, object]]],
    container_capacities: dict[str, int],
    container_lock_states: dict[str, str],
) -> None:
    container_metadata = _component_metadata(container_component)
    raw_items_obj = getattr(container_component, "items", None)
    raw_items_list: list[object]
    if isinstance(raw_items_obj, list):
        raw_items_list = list(cast(list[object], raw_items_obj))
    else:
        raw_items_list = []
    items_count = len(raw_items_list)
    logger.debug(
        "Processing container component",
        container_item_name=container_metadata.get("item_name"),
        container_item_id=container_metadata.get("item_id"),
        container_items_count=items_count,
    )

    matching_slot = match_container_to_slot(container_component, equipped_view)
    if not matching_slot:
        return

    capacity_slots = getattr(container_component, "capacity_slots", 0)
    container_capacities[matching_slot] = int(capacity_slots)
    lock_state = getattr(container_component, "lock_state", "unlocked")
    container_lock_states[matching_slot] = _lock_state_as_str(lock_state)

    if raw_items_list:
        container_contents[matching_slot] = [
            _inventory_stack_to_display_dict(cast(InventoryStack, item)) for item in raw_items_list
        ]
    else:
        container_contents[matching_slot] = []
    logger.debug(
        "Container contents set",
        matching_slot=matching_slot,
        items_count=len(container_contents[matching_slot]),
    )


async def get_container_data_for_inventory(
    request: object,
    player: Player,
    equipped_view: dict[str, dict[str, object]],
) -> tuple[dict[str, list[dict[str, object]]], dict[str, int], dict[str, str]]:
    """Get container contents, capacities, and lock states for equipped containers."""
    container_contents: dict[str, list[dict[str, object]]] = {}
    container_capacities: dict[str, int] = {}
    container_lock_states: dict[str, str] = {}

    try:
        _, wearable_container_service, _ = get_shared_services(request)
        player_id_uuid = UUID(str(player.player_id))
        wearable_containers = await wearable_container_service.get_wearable_containers_for_player(player_id_uuid)
        logger.debug(
            "Getting container contents",
            player_id=str(player_id_uuid),
            wearable_containers_count=len(wearable_containers),
            equipped_slots=list(equipped_view.keys()),
        )

        for container_component in wearable_containers:
            await _apply_container_component_to_slot(
                container_component,
                equipped_view,
                container_contents,
                container_capacities,
                container_lock_states,
            )
    except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Container access errors unpredictable, optional display
        logger.debug(
            "Error getting container contents for inventory display",
            error=str(e),
            player=player.name,
        )

    return container_contents, container_capacities, container_lock_states


def update_equipped_with_container_info(
    equipped_view: dict[str, dict[str, object]],
    container_contents: dict[str, list[dict[str, object]]],
    container_capacities: dict[str, int],
    container_lock_states: dict[str, str],
) -> None:
    """Update equipped items' metadata to include container information."""
    for slot_name, equipped_item in equipped_view.items():
        if slot_name not in container_contents:
            continue

        container_items = container_contents[slot_name]
        container_slots_used = len(container_items)

        if "metadata" not in equipped_item:
            equipped_item["metadata"] = {}
        meta = equipped_item["metadata"]
        if not isinstance(meta, dict):
            equipped_item["metadata"] = {}
            meta = equipped_item["metadata"]
        meta_obj = cast(dict[str, object], meta)
        if "container" not in meta_obj:
            meta_obj["container"] = {}

        container_raw = meta_obj["container"]
        if isinstance(container_raw, dict):
            container_dict: dict[str, object] = dict(cast(dict[str, object], container_raw))
        else:
            container_dict = {}
        container_dict.update(
            {
                "lock_state": container_lock_states.get(slot_name, "unlocked"),
                "capacity_slots": container_capacities.get(slot_name, 20),
                "slots_in_use": container_slots_used,
            }
        )
        meta_obj["container"] = container_dict
