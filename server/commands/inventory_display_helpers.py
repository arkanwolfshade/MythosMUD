"""Display and rendering helpers for inventory commands."""

from collections.abc import Mapping
from typing import Any

DEFAULT_SLOT_CAPACITY = 20


def format_metadata(metadata: Mapping[str, Any] | None) -> str:
    """Format metadata for display."""
    if not metadata:
        return ""
    try:
        components = []
        for key, value in sorted(metadata.items()):
            # Handle nested dicts (like container dict) by using repr() explicitly
            if isinstance(value, dict):
                components.append(f"{key}={value!r}")
            else:
                components.append(f"{key}={value}")
        if components:
            return f" [{', '.join(components)}]"
    except Exception as exc:  # noqa: B904  # pragma: no cover - metadata formatting should rarely fail  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Metadata formatting errors unpredictable, optional display
        from ..structured_logging.enhanced_logging_config import get_logger

        logger = get_logger(__name__)
        logger.error("Failed to format metadata", error=str(exc), metadata=metadata, exc_info=True)
    return ""


def get_equipped_item_identifiers(equipped: dict[str, Any]) -> tuple[set[str], set[str]]:
    """Get sets of equipped item IDs and instance IDs for efficient lookup."""
    equipped_item_ids: set[str] = set()
    equipped_item_instance_ids: set[str] = set()
    for equipped_item in equipped.values():
        item_id = equipped_item.get("item_id")
        item_instance_id = equipped_item.get("item_instance_id")
        if item_id:
            equipped_item_ids.add(str(item_id))
        if item_instance_id:
            equipped_item_instance_ids.add(str(item_instance_id))
    return equipped_item_ids, equipped_item_instance_ids


def filter_non_equipped_inventory(
    inventory: list[dict[str, Any]], equipped_item_ids: set[str], equipped_item_instance_ids: set[str]
) -> list[dict[str, Any]]:
    """Filter out equipped items and container items from inventory."""
    non_equipped_inventory = []
    for stack in inventory:
        stack_item_id = stack.get("item_id")
        stack_item_instance_id = stack.get("item_instance_id")
        slot_type = stack.get("slot_type", "unknown")

        is_equipped = False
        if stack_item_instance_id and str(stack_item_instance_id) in equipped_item_instance_ids:
            is_equipped = True
        elif stack_item_id and str(stack_item_id) in equipped_item_ids:
            is_equipped = True

        is_in_container = slot_type not in ("unknown", "inventory")
        if not is_equipped and not is_in_container:
            non_equipped_inventory.append(stack)

    return non_equipped_inventory


def build_inventory_lines(inventory: list[dict[str, Any]]) -> list[str]:
    """Build inventory display lines."""
    lines = []
    if inventory:
        for index, stack in enumerate(inventory, start=1):
            item_name = stack.get("item_name") or stack.get("item_id", "Unknown Item")
            slot_type = stack.get("slot_type", "unknown")
            quantity = stack.get("quantity", 0)
            metadata_suffix = format_metadata(stack.get("metadata"))
            lines.append(f"{index}. {item_name} ({slot_type}) x{quantity}{metadata_suffix}")
    else:
        lines.append("No items in your pockets or on your person.")
    return lines


def build_container_metadata(
    slot_name: str,
    item_metadata: dict[str, Any],
    container_contents: dict[str, list[dict[str, Any]]] | None,
    container_capacities: dict[str, int] | None,
    container_lock_states: dict[str, str] | None,
) -> str:
    """Build and format metadata for equipped item with container."""
    if container_contents is not None and slot_name in container_contents:
        container_items = container_contents[slot_name]
        container_capacity = container_capacities.get(slot_name, 20) if container_capacities else 20
        container_lock_state = container_lock_states.get(slot_name, "unlocked") if container_lock_states else "unlocked"
        container_slots_used = len(container_items)

        container_dict = {
            "lock_state": container_lock_state,
            "capacity_slots": container_capacity,
            "slots_in_use": container_slots_used,
        }

        updated_metadata = {}
        for key, value in item_metadata.items():
            if key != "container":
                updated_metadata[key] = value
        updated_metadata["container"] = container_dict

        return format_metadata(updated_metadata)

    return format_metadata(item_metadata)


def build_equipped_lines(
    equipped: dict[str, Any],
    container_contents: dict[str, list[dict[str, Any]]] | None,
    container_capacities: dict[str, int] | None,
    container_lock_states: dict[str, str] | None,
) -> list[str]:
    """Build equipped items display lines."""
    lines = []
    if equipped:  # pylint: disable=too-many-nested-blocks  # Reason: Inventory display requires complex nested logic for item formatting, metadata handling, and display generation
        for slot_name in sorted(equipped.keys()):
            item = equipped[slot_name]
            item_name = item.get("item_name") or item.get("item_id", "Unknown Item")
            quantity = item.get("quantity", 0)
            item_metadata = item.get("metadata") or {}

            metadata_suffix = build_container_metadata(
                slot_name, item_metadata, container_contents, container_capacities, container_lock_states
            )

            lines.append(f"- {slot_name}: {item_name} x{quantity}{metadata_suffix}")

            if container_contents is not None and slot_name in container_contents:
                container_items = container_contents[slot_name]
                if container_items:
                    for container_item in container_items:
                        container_item_name = container_item.get("item_name") or container_item.get(
                            "name", "Unknown Item"
                        )
                        container_item_quantity = container_item.get("quantity", 1)
                        if container_item_quantity > 1:
                            lines.append(f"    - {container_item_name} x{container_item_quantity}")
                        else:
                            lines.append(f"    - {container_item_name}")
    else:
        lines.append("- Nothing equipped.")

    return lines


def render_inventory(
    inventory: list[dict[str, Any]],
    equipped: dict[str, Any],
    container_contents: dict[str, list[dict[str, Any]]] | None = None,
    container_capacities: dict[str, int] | None = None,
    container_lock_states: dict[str, str] | None = None,
) -> str:
    """Render inventory display with equipped items and container contents."""
    equipped_item_ids, equipped_item_instance_ids = get_equipped_item_identifiers(equipped)
    non_equipped_inventory = filter_non_equipped_inventory(inventory, equipped_item_ids, equipped_item_instance_ids)

    slots_used = len(non_equipped_inventory)
    remaining = max(DEFAULT_SLOT_CAPACITY - slots_used, 0)

    lines = [f"You are carrying {slots_used} / {DEFAULT_SLOT_CAPACITY} slots. Remaining capacity: {remaining}."]

    lines.extend(build_inventory_lines(inventory))
    lines.append("")
    lines.append("Equipped:")
    lines.extend(build_equipped_lines(equipped, container_contents, container_capacities, container_lock_states))

    return "\n".join(lines)
