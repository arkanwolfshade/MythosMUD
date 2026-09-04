"""Item instance model for runtime item representation.

This module defines the ItemInstance dataclass which represents a runtime
item created from an item prototype, with instance-specific state and properties.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import UTC, datetime
from typing import Any


@dataclass(frozen=True, slots=True)
class ItemInstance:  # pylint: disable=too-many-instance-attributes  # Reason: Item instance requires many fields to capture complete item state
    """Runtime representation of an item created from a prototype."""

    item_instance_id: str
    prototype_id: str
    name: str
    quantity: int = 1
    slot_type: str = "backpack"
    flags: list[str] = field(default_factory=list)
    metadata: dict[str, Any] = field(default_factory=dict)
    origin: dict[str, Any] = field(default_factory=dict)
    created_at: datetime = field(default_factory=lambda: datetime.now(UTC))

    def to_inventory_stack(self) -> dict[str, Any]:
        """
        Convert the instance into an inventory stack payload understood by legacy services.

        The stack retains compatibility with pre-item-system payloads by exposing `item_id`
        while preferring `item_instance_id` and `prototype_id`.
        """

        stack: dict[str, Any] = {
            "item_instance_id": self.item_instance_id,
            "prototype_id": self.prototype_id,
            "item_id": self.prototype_id,
            "item_name": self.name,
            "slot_type": self.slot_type,
            "quantity": self.quantity,
        }

        if self.flags:
            stack["flags"] = list(self.flags)
        if self.metadata:
            stack["metadata"] = dict(self.metadata)
        if self.origin:
            stack["origin"] = dict(self.origin)
        stack["created_at"] = self.created_at.isoformat()
        return stack
