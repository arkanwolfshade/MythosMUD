"""Item factory for creating item instances from prototypes.

This module provides the ItemFactory class which creates runtime item instances
from item prototypes stored in the prototype registry.
"""

from __future__ import annotations

import uuid
from copy import deepcopy
from typing import Any

from server.game.items.component_hooks import initialize_components
from server.game.items.item_instance import ItemInstance
from server.game.items.prototype_registry import PrototypeRegistry, PrototypeRegistryError
from server.structured_logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)


class ItemFactoryError(Exception):
    """Raised when the factory cannot produce a valid instance."""


class ItemFactory:  # pylint: disable=too-few-public-methods  # Reason: Factory class with focused responsibility, minimal public interface
    """Factory responsible for instantiating runtime item instances."""

    def __init__(self, registry: PrototypeRegistry):
        """Initialize the item factory with a prototype registry.

        Args:
            registry: The prototype registry to use for item creation
        """
        self._registry = registry

    def create_instance(  # pylint: disable=too-many-arguments,too-many-positional-arguments,too-many-locals  # Reason: Item creation requires many parameters and intermediate variables for complex item instantiation logic
        self,
        prototype_id: str,
        *,
        quantity: int = 1,
        overrides: dict[str, Any] | None = None,
        origin: dict[str, Any] | None = None,
        slot_type: str | None = None,
    ) -> ItemInstance:
        """Create an item instance from a prototype.

        Args:
            prototype_id: The ID of the prototype to use
            quantity: Number of items to create (default: 1)
            overrides: Optional dictionary of property overrides
            origin: Optional dictionary describing item origin
            slot_type: Optional slot type for the item

        Returns:
            ItemInstance: The created item instance

        Raises:
            ItemFactoryError: If quantity is invalid or prototype not found
        """
        if quantity <= 0:
            raise ItemFactoryError("Quantity must be a positive integer.")

        try:
            prototype = self._registry.get(prototype_id)
        except PrototypeRegistryError as exc:
            logger.error("Item factory failed prototype lookup", prototype_id=prototype_id, error=str(exc))
            raise ItemFactoryError(f"Prototype '{prototype_id}' not found.") from exc

        overrides = deepcopy(overrides or {})
        origin = deepcopy(origin or {})

        name_override = overrides.get("name")
        item_name = str(name_override or prototype.name)

        stack_slot = slot_type or overrides.get("slot_type")
        if not stack_slot:
            wear_slots = list(getattr(prototype, "wear_slots", []))
            stack_slot = wear_slots[0] if wear_slots else "backpack"

        metadata = deepcopy(getattr(prototype, "metadata", {}))
        metadata.update(overrides.get("metadata", {}))
        component_metadata = initialize_components(prototype, overrides=overrides)
        if component_metadata:
            metadata.setdefault("components", component_metadata.get("components", []))
            if overrides_details := component_metadata.get("overrides"):
                metadata["component_overrides"] = overrides_details

        flags = list(getattr(prototype, "flags", []))
        if override_flags := overrides.get("flags"):
            flags = list(override_flags)

        instance = ItemInstance(
            item_instance_id=str(uuid.uuid4()),
            prototype_id=prototype.prototype_id,
            name=item_name,
            quantity=quantity,
            slot_type=stack_slot,
            flags=flags,
            metadata=metadata,
            origin=origin,
        )

        logger.info(
            "Item instance created",
            item_instance_id=instance.item_instance_id,
            prototype_id=instance.prototype_id,
            quantity=quantity,
            slot_type=stack_slot,
        )

        return instance
