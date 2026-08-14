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

    def __init__(self, registry: PrototypeRegistry) -> None:
        """Initialize the item factory with a prototype registry.

        Args:
            registry: The prototype registry to use for item creation
        """
        self._registry = registry

    def _resolve_stack_slot(self, prototype: Any, overrides: dict[str, Any], slot_type: str | None) -> str:
        stack_slot = slot_type or overrides.get("slot_type")
        if stack_slot:
            return str(stack_slot)
        wear_slots = list(getattr(prototype, "wear_slots", []))
        return wear_slots[0] if wear_slots else "backpack"

    def _build_instance_metadata(self, prototype: Any, overrides: dict[str, Any]) -> dict[str, Any]:
        metadata = deepcopy(getattr(prototype, "metadata", {}))
        metadata.update(overrides.get("metadata", {}))
        component_metadata = initialize_components(prototype, overrides=overrides)
        if component_metadata:
            metadata.setdefault("components", component_metadata.get("components", []))
            if overrides_details := component_metadata.get("overrides"):
                metadata["component_overrides"] = overrides_details
        return metadata

    def create_instance(
        self,
        prototype_id: str,
        *,
        quantity: int = 1,
        overrides: dict[str, Any] | None = None,
        origin: dict[str, Any] | None = None,
        slot_type: str | None = None,
    ) -> ItemInstance:
        """Create an item instance from a prototype."""
        if quantity <= 0:
            raise ItemFactoryError("Quantity must be a positive integer.")
        try:
            prototype = self._registry.get(prototype_id)
        except PrototypeRegistryError as exc:
            logger.error("Item factory failed prototype lookup", prototype_id=prototype_id, error=str(exc))
            raise ItemFactoryError(f"Prototype '{prototype_id}' not found.") from exc
        overrides = deepcopy(overrides or {})
        origin = deepcopy(origin or {})
        item_name = str(overrides.get("name") or prototype.name)
        stack_slot = self._resolve_stack_slot(prototype, overrides, slot_type)
        metadata = self._build_instance_metadata(prototype, overrides)
        flags = list(overrides.get("flags") or getattr(prototype, "flags", []))
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
