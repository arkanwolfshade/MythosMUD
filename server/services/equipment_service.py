"""Equipment service providing equip/unequip helpers built atop inventory logic."""

from __future__ import annotations

import copy
from collections.abc import Mapping, Sequence
from dataclasses import dataclass, field
from typing import Any, cast

from ..logging.enhanced_logging_config import get_logger
from .inventory_service import (
    InventoryCapacityError,
    InventoryService,
    InventoryStack,
)
from .wearable_container_service import WearableContainerService

logger = get_logger(__name__)


class EquipmentServiceError(Exception):
    """Base error for equipment service operations."""


class SlotValidationError(EquipmentServiceError):
    """Raised when requested slots or inventory positions are invalid."""


class EquipmentCapacityError(EquipmentServiceError):
    """Raised when an equip/unequip operation would exceed inventory capacity."""


def _clone_inventory(inventory: Sequence[Mapping[str, Any]]) -> list[InventoryStack]:
    return [cast(InventoryStack, copy.deepcopy(stack)) for stack in inventory]


def _clone_equipped(equipped: Mapping[str, Mapping[str, Any]]) -> dict[str, InventoryStack]:
    return {slot: cast(InventoryStack, copy.deepcopy(stack)) for slot, stack in equipped.items()}


@dataclass(frozen=True)
class EquipmentService:
    """
    Service orchestrating equip/unequip flows with stacking semantics.

    Operations return new inventory/equipped structures without mutating inputs.
    """

    inventory_service: InventoryService = field(default_factory=InventoryService)
    wearable_container_service: WearableContainerService | None = field(default=None)

    def equip_from_inventory(
        self,
        inventory: Sequence[Mapping[str, Any]],
        equipped: Mapping[str, Mapping[str, Any]],
        *,
        slot_index: int,
        target_slot: str | None = None,
    ) -> tuple[list[InventoryStack], dict[str, InventoryStack]]:
        """Equip an item from inventory into its designated slot."""

        working_inventory = _clone_inventory(inventory)
        working_equipped = _clone_equipped(equipped)

        if not 0 <= slot_index < len(working_inventory):
            raise SlotValidationError(f"Inventory slot index {slot_index} is invalid.")

        source_stack = copy.deepcopy(working_inventory[slot_index])
        slot_type = source_stack.get("slot_type")

        if not isinstance(slot_type, str) or not slot_type:
            raise SlotValidationError("Inventory item lacks a valid slot_type.")

        if target_slot is not None and slot_type != target_slot:
            raise SlotValidationError(f"Item slot '{slot_type}' does not match requested slot '{target_slot}'.")

        quantity = source_stack.get("quantity", 0)
        if not isinstance(quantity, int) or quantity <= 0:
            raise SlotValidationError("Inventory item must have a positive quantity.")

        if quantity == 1:
            del working_inventory[slot_index]
        else:
            updated_stack = copy.deepcopy(source_stack)
            updated_stack["quantity"] = quantity - 1
            working_inventory[slot_index] = updated_stack

        equipped_item = copy.deepcopy(source_stack)
        equipped_item["quantity"] = 1

        previously_equipped = working_equipped.get(slot_type)
        if previously_equipped is not None:
            try:
                working_inventory = self.inventory_service.add_stack(working_inventory, previously_equipped)
            except InventoryCapacityError as exc:
                raise EquipmentCapacityError(
                    f"Cannot swap '{previously_equipped['item_name']}' into inventory; capacity reached."
                ) from exc

        working_equipped[slot_type] = equipped_item

        # Handle wearable container creation if this is a container item
        if self.wearable_container_service and equipped_item.get("inner_container"):
            try:
                # Import here to avoid circular dependency

                # Get player_id from context if available
                # For now, we'll need to pass player_id separately or get it from context
                # This is a limitation - we may need to refactor EquipmentService to accept player_id
                # For now, we'll skip container creation here and handle it at the API/command layer
                pass
            except Exception as e:
                # Log but don't fail - container creation is not critical for equip operation
                logger.warning(
                    "Failed to create wearable container on equip",
                    error=str(e),
                    item_id=equipped_item.get("item_id"),
                )

        return working_inventory, working_equipped

    def unequip_to_inventory(
        self,
        inventory: Sequence[Mapping[str, Any]],
        equipped: Mapping[str, Mapping[str, Any]],
        *,
        slot_type: str,
    ) -> tuple[list[InventoryStack], dict[str, InventoryStack]]:
        """Return an equipped item back to inventory."""

        if not slot_type:
            raise SlotValidationError("Slot type must be provided for unequip operations.")

        working_inventory = _clone_inventory(inventory)
        working_equipped = _clone_equipped(equipped)

        equipped_item = working_equipped.pop(slot_type, None)
        if equipped_item is None:
            raise SlotValidationError(f"No equipped item found for slot '{slot_type}'.")

        try:
            working_inventory = self.inventory_service.add_stack(working_inventory, equipped_item)
        except InventoryCapacityError as exc:
            raise EquipmentCapacityError(
                f"Cannot move '{equipped_item['item_name']}' into inventory; capacity reached."
            ) from exc

        # Handle wearable container preservation if this is a container item
        if self.wearable_container_service and equipped_item.get("inner_container"):
            try:
                # Import here to avoid circular dependency

                # Get player_id from context if available
                # For now, we'll need to pass player_id separately or get it from context
                # This is a limitation - we may need to refactor EquipmentService to accept player_id
                # For now, we'll skip container preservation here and handle it at the API/command layer
                pass
            except Exception as e:
                # Log but don't fail - container preservation is not critical for unequip operation
                logger.warning(
                    "Failed to preserve wearable container on unequip",
                    error=str(e),
                    item_id=equipped_item.get("item_id"),
                )

        return working_inventory, working_equipped


__all__ = [
    "EquipmentService",
    "EquipmentServiceError",
    "SlotValidationError",
    "EquipmentCapacityError",
]
