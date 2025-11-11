"""Inventory service providing stacking and slot management helpers."""

from __future__ import annotations

import copy
from collections.abc import Mapping, Sequence
from dataclasses import dataclass, field
from typing import Any, TypedDict, cast

from .inventory_mutation_guard import InventoryMutationGuard


class InventoryServiceError(Exception):
    """Base exception for inventory service operations."""


class InventoryValidationError(InventoryServiceError):
    """Raised when item payloads are malformed or incomplete."""


class InventoryCapacityError(InventoryServiceError):
    """Raised when an operation would exceed the configured slot capacity."""


class InventorySplitError(InventoryServiceError):
    """Raised when stack splitting arguments are invalid."""


class InventoryStackRequired(TypedDict):
    item_id: str
    item_name: str
    slot_type: str
    quantity: int


class InventoryStack(InventoryStackRequired, total=False):
    metadata: dict[str, Any]


@dataclass(frozen=True)
class InventoryService:
    """
    Pure inventory mutation helpers for stacking, splitting, and slot limits.

    The service never mutates the provided inventory argument and instead
    returns a new list, preserving thread-safety expectations for callers that
    may perform optimistic concurrency checks on payloads.
    """

    max_slots: int = 20
    mutation_guard: InventoryMutationGuard = field(default_factory=InventoryMutationGuard)

    def add_stack(
        self,
        inventory: Sequence[Mapping[str, Any]],
        incoming: Mapping[str, Any],
    ) -> list[InventoryStack]:
        """
        Add or merge an item stack into the inventory.

        Args:
            inventory: Current ordered inventory slots.
            incoming: Payload describing the stack to add.

        Returns:
            New inventory list with the stack merged or appended.

        Raises:
            InventoryValidationError: If payloads are missing required fields.
            InventoryCapacityError: If the inventory is already at capacity.
        """

        normalized_inventory = [self._clone_stack(stack) for stack in inventory]
        new_stack = self._clone_stack(incoming)

        for index, stack in enumerate(normalized_inventory):
            if self._can_merge(stack, new_stack):
                merged_quantity = stack["quantity"] + new_stack["quantity"]
                normalized_inventory[index] = self._clone_with_quantity(stack, merged_quantity)
                return normalized_inventory

        if len(normalized_inventory) >= self.max_slots:
            raise InventoryCapacityError(
                f"Inventory cannot exceed {self.max_slots} slots; unable to add '{new_stack['item_name']}'."
            )

        normalized_inventory.append(new_stack)
        return normalized_inventory

    def split_stack(
        self,
        inventory: Sequence[Mapping[str, Any]],
        *,
        slot_index: int,
        split_quantity: int,
    ) -> list[InventoryStack]:
        """
        Split a stack into two, inserting the new stack immediately after the source slot.

        Args:
            inventory: Current ordered inventory slots.
            slot_index: Index of the stack to split.
            split_quantity: Quantity to move into the new stack.

        Returns:
            New inventory list with the split applied.

        Raises:
            InventorySplitError: For invalid indices or quantities.
            InventoryCapacityError: When the split would exceed slot capacity.
        """

        if not 0 <= slot_index < len(inventory):
            raise InventorySplitError(f"Slot index {slot_index} is outside current inventory bounds.")

        if split_quantity <= 0:
            raise InventorySplitError("Split quantity must be a positive integer.")

        if len(inventory) >= self.max_slots:
            raise InventoryCapacityError(
                f"Inventory already occupies all {self.max_slots} slots; unable to split stack."
            )

        normalized_inventory = [self._clone_stack(stack) for stack in inventory]
        source_stack = normalized_inventory[slot_index]

        if split_quantity >= source_stack["quantity"]:
            raise InventorySplitError("Split quantity must be less than the existing stack size.")

        remaining_quantity = source_stack["quantity"] - split_quantity
        normalized_inventory[slot_index] = self._clone_with_quantity(source_stack, remaining_quantity)
        split_stack = self._clone_with_quantity(source_stack, split_quantity)
        normalized_inventory.insert(slot_index + 1, split_stack)
        return normalized_inventory

    def begin_mutation(self, player_id: str, token: str | None):
        """
        Acquire a guarded mutation context for the given player.

        Returns a context manager decision that should be used via:

            with service.begin_mutation(player_id, token) as decision:
                if decision.should_apply:
                    ...

        This pattern ensures per-player serialization and idempotent behaviour.
        """

        return self.mutation_guard.acquire(player_id, token)

    def _clone_stack(self, stack: Mapping[str, Any]) -> InventoryStack:
        try:
            item_id = cast(str, stack["item_id"])
            item_name = cast(str, stack["item_name"])
            slot_type = cast(str, stack["slot_type"])
            quantity = int(stack["quantity"])
        except KeyError as exc:
            raise InventoryValidationError(f"Missing required inventory field: {exc.args[0]}") from None
        except (TypeError, ValueError) as exc:
            raise InventoryValidationError("Quantity must be coercible to an integer.") from exc

        if quantity <= 0:
            raise InventoryValidationError("Quantity must be a positive integer.")

        clone: InventoryStack = {
            "item_id": item_id,
            "item_name": item_name,
            "slot_type": slot_type,
            "quantity": quantity,
        }

        metadata = stack.get("metadata")
        if metadata is not None:
            if not isinstance(metadata, dict):
                raise InventoryValidationError("Metadata must be a mapping when provided.")
            clone["metadata"] = copy.deepcopy(metadata)

        return clone

    def _clone_with_quantity(self, stack: Mapping[str, Any], quantity: int) -> InventoryStack:
        if quantity <= 0:
            raise InventorySplitError("Resulting stack quantity must remain positive after the split.")
        clone = self._clone_stack(stack)
        clone["quantity"] = quantity
        return clone

    @staticmethod
    def _can_merge(existing: InventoryStack, incoming: InventoryStack) -> bool:
        if existing["item_id"] != incoming["item_id"]:
            return False
        if existing["slot_type"] != incoming["slot_type"]:
            return False
        if existing["item_name"] != incoming["item_name"]:
            return False

        return InventoryService._normalize_metadata(existing) == InventoryService._normalize_metadata(incoming)

    @staticmethod
    def _normalize_metadata(stack: InventoryStack) -> dict[str, Any]:
        metadata = stack.get("metadata")
        if metadata is None:
            return {}
        return metadata


__all__ = [
    "InventoryService",
    "InventoryServiceError",
    "InventoryValidationError",
    "InventoryCapacityError",
    "InventorySplitError",
    "InventoryStack",
]
