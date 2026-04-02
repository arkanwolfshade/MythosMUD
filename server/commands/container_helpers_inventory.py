"""Container-related helper functions for inventory commands (facade re-exports)."""

from __future__ import annotations

from .container_helpers_inventory_display import (
    get_container_data_for_inventory,
    match_container_to_slot,
    update_equipped_with_container_info,
)
from .container_helpers_inventory_find import (
    create_wearable_container,
    find_container_in_room,
    find_item_in_inventory,
    find_matching_equipped_containers,
    find_wearable_container,
    find_wearable_container_for_put,
    try_inner_container,
    try_inner_container_by_id,
    try_wearable_container_service,
    try_wearable_container_service_by_instance_id,
    try_wearable_container_service_by_name,
)
from .container_helpers_inventory_ops import (
    extract_items_from_container,
    filter_valid_items,
    find_item_in_container,
    parse_container_items,
    parse_json_string_items,
    resolve_container_id,
    transfer_item_from_container,
    transfer_item_to_container,
    validate_get_command_inputs,
    validate_put_command_inputs,
)

__all__ = [
    "create_wearable_container",
    "extract_items_from_container",
    "filter_valid_items",
    "find_container_in_room",
    "find_item_in_container",
    "find_item_in_inventory",
    "find_matching_equipped_containers",
    "find_wearable_container",
    "find_wearable_container_for_put",
    "get_container_data_for_inventory",
    "match_container_to_slot",
    "parse_container_items",
    "parse_json_string_items",
    "resolve_container_id",
    "transfer_item_from_container",
    "transfer_item_to_container",
    "try_inner_container",
    "try_inner_container_by_id",
    "try_wearable_container_service",
    "try_wearable_container_service_by_instance_id",
    "try_wearable_container_service_by_name",
    "update_equipped_with_container_info",
    "validate_get_command_inputs",
    "validate_put_command_inputs",
]
