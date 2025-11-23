"""
Wearable container service for unified container system.

As documented in the restricted archives of Miskatonic University, wearable
container integration requires careful orchestration to ensure proper handling
of equip/unequip transitions, nested container capacity, and inventory spill.
"""

from __future__ import annotations

from typing import Any
from uuid import UUID

from ..exceptions import MythosMUDError
from ..logging.enhanced_logging_config import get_logger
from ..models.container import ContainerComponent, ContainerSourceType
from ..persistence import get_persistence
from ..utils.error_logging import create_error_context, log_and_raise

logger = get_logger(__name__)


class WearableContainerServiceError(MythosMUDError):
    """Base exception for wearable container service operations."""


class WearableContainerService:
    """
    Service for managing wearable container operations.

    Handles container creation on equip, preservation on unequip,
    nested capacity enforcement, and inventory spill rules.
    """

    def __init__(self, persistence: Any | None = None):
        """
        Initialize the wearable container service.

        Args:
            persistence: Persistence layer instance (optional, will get if not provided)
        """
        self.persistence = persistence or get_persistence()

    def handle_equip_wearable_container(self, player_id: UUID, item_stack: dict[str, Any]) -> dict[str, Any] | None:
        """
        Handle equipping a wearable container item.

        Creates a container in PostgreSQL if the item has an inner_container.

        Args:
            player_id: UUID of the player equipping the item
            item_stack: Item stack being equipped (may contain inner_container)

        Returns:
            dict with container_id if container was created, None otherwise

        Raises:
            WearableContainerServiceError: If container creation fails or capacity exceeded
        """
        inner_container = item_stack.get("inner_container")
        if not inner_container:
            # Not a container item, nothing to do
            return None

        context = create_error_context()
        context.metadata["operation"] = "handle_equip_wearable_container"
        context.metadata["player_id"] = str(player_id)
        context.metadata["item_id"] = item_stack.get("item_id", "unknown")

        logger.info(
            "Handling equip of wearable container",
            player_id=str(player_id),
            item_id=item_stack.get("item_id"),
        )

        # Validate inner container capacity
        capacity_slots = inner_container.get("capacity_slots", 20)
        items = inner_container.get("items", [])

        if len(items) > capacity_slots:
            log_and_raise(
                WearableContainerServiceError,
                f"Container capacity exceeded: {len(items)} items > {capacity_slots} capacity",
                context=context,
                details={
                    "capacity_slots": capacity_slots,
                    "items_count": len(items),
                },
                user_friendly="Container capacity exceeded",
            )

        # Check if container already exists for this item
        existing_containers = self.persistence.get_containers_by_entity_id(player_id)
        item_instance_id = item_stack.get("item_instance_id")

        for existing in existing_containers:
            if existing.get("source_type") == "equipment":
                # Check if this is the same item instance
                existing_metadata = existing.get("metadata", {})
                if existing_metadata.get("item_instance_id") == item_instance_id:
                    # Container already exists, return its ID
                    existing_id = existing.get("container_id")
                    logger.debug(
                        "Container already exists for item",
                        player_id=str(player_id),
                        item_instance_id=item_instance_id,
                        container_id=existing_id,
                    )
                    return {"container_id": UUID(existing_id) if isinstance(existing_id, str) else existing_id}

        # Create new container in PostgreSQL
        try:
            container_data = self.persistence.create_container(
                source_type="equipment",
                entity_id=player_id,
                capacity_slots=capacity_slots,
                lock_state=inner_container.get("lock_state", "unlocked"),
                allowed_roles=inner_container.get("allowed_roles", []),
                items_json=items,
                metadata_json={
                    "item_instance_id": item_instance_id,
                    "item_id": item_stack.get("item_id"),
                    "item_name": item_stack.get("item_name"),
                },
            )

            container_id = UUID(container_data["container_id"])

            logger.info(
                "Wearable container created on equip",
                player_id=str(player_id),
                container_id=str(container_id),
                item_instance_id=item_instance_id,
            )

            return {"container_id": container_id}

        except Exception as e:
            log_and_raise(
                WearableContainerServiceError,
                f"Failed to create wearable container: {str(e)}",
                context=context,
                details={"player_id": str(player_id), "error": str(e)},
                user_friendly="Failed to create container",
            )

    def handle_unequip_wearable_container(self, player_id: UUID, item_stack: dict[str, Any]) -> dict[str, Any] | None:
        """
        Handle unequipping a wearable container item.

        Preserves the container and its items by updating the inner_container
        in the item stack with current container state.

        Args:
            player_id: UUID of the player unequipping the item
            item_stack: Item stack being unequipped

        Returns:
            dict with updated inner_container if container exists, None otherwise
        """
        item_instance_id = item_stack.get("item_instance_id")
        if not item_instance_id:
            return None

        logger.info(
            "Handling unequip of wearable container",
            player_id=str(player_id),
            item_instance_id=item_instance_id,
        )

        # Find container for this item
        existing_containers = self.persistence.get_containers_by_entity_id(player_id)
        for existing in existing_containers:
            if existing.get("source_type") == "equipment":
                existing_metadata = existing.get("metadata", {})
                if existing_metadata.get("item_instance_id") == item_instance_id:
                    # Found the container, update inner_container in item stack
                    container = ContainerComponent.model_validate(existing)
                    inner_container = {
                        "capacity_slots": container.capacity_slots,
                        "items": container.items,
                        "lock_state": container.lock_state.value,
                    }
                    if container.allowed_roles:
                        inner_container["allowed_roles"] = container.allowed_roles

                    logger.info(
                        "Wearable container preserved on unequip",
                        player_id=str(player_id),
                        container_id=str(container.container_id),
                        items_count=len(container.items),
                    )

                    return {"inner_container": inner_container}

        # No container found, return None (item doesn't have a container)
        return None

    def get_wearable_containers_for_player(self, player_id: UUID) -> list[ContainerComponent]:
        """
        Get all wearable containers for a player.

        Args:
            player_id: UUID of the player

        Returns:
            list[ContainerComponent]: List of wearable containers
        """
        containers_data = self.persistence.get_containers_by_entity_id(player_id)
        if not containers_data:
            return []

        containers = []
        for container_data in containers_data:
            try:
                if container_data.get("source_type") == "equipment":
                    container = ContainerComponent.model_validate(container_data)
                    containers.append(container)
            except Exception as e:
                logger.warning(
                    "Error loading wearable container",
                    error=str(e),
                    player_id=str(player_id),
                    container_data=container_data,
                )
                continue

        return containers

    def add_items_to_wearable_container(
        self, player_id: UUID, container_id: UUID, items: list[dict[str, Any]]
    ) -> dict[str, Any]:
        """
        Add items to a wearable container.

        Args:
            player_id: UUID of the player
            container_id: UUID of the container
            items: List of items to add

        Returns:
            dict with updated container state

        Raises:
            WearableContainerServiceError: If capacity would be exceeded
        """
        context = create_error_context()
        context.metadata["operation"] = "add_items_to_wearable_container"
        context.metadata["player_id"] = str(player_id)
        context.metadata["container_id"] = str(container_id)

        # Get current container
        container_data = self.persistence.get_container(container_id)
        if not container_data:
            log_and_raise(
                WearableContainerServiceError,
                f"Container not found: {container_id}",
                context=context,
                details={"container_id": str(container_id)},
                user_friendly="Container not found",
            )

        container = ContainerComponent.model_validate(container_data)

        # Verify it's a wearable container for this player
        if container.source_type != ContainerSourceType.EQUIPMENT or container.entity_id != player_id:
            log_and_raise(
                WearableContainerServiceError,
                "Container is not a wearable container for this player",
                context=context,
                details={
                    "container_id": str(container_id),
                    "source_type": container.source_type.value,
                    "entity_id": str(container.entity_id),
                },
                user_friendly="Invalid container",
            )

        # Check capacity
        current_items = container.items
        if len(current_items) + len(items) > container.capacity_slots:
            log_and_raise(
                WearableContainerServiceError,
                f"Container capacity exceeded: {len(current_items) + len(items)} > {container.capacity_slots}",
                context=context,
                details={
                    "current_items": len(current_items),
                    "new_items": len(items),
                    "capacity_slots": container.capacity_slots,
                },
                user_friendly="Container capacity exceeded",
            )

        # Add items
        new_items = current_items + items

        # Update container
        updated_data = self.persistence.update_container(
            container_id=container_id,
            items_json=new_items,
        )

        logger.info(
            "Items added to wearable container",
            player_id=str(player_id),
            container_id=str(container_id),
            items_added=len(items),
            total_items=len(new_items),
        )

        return updated_data

    def update_wearable_container_items(
        self, player_id: UUID, container_id: UUID, items: list[dict[str, Any]]
    ) -> dict[str, Any]:
        """
        Update items in a wearable container.

        Args:
            player_id: UUID of the player
            container_id: UUID of the container
            items: New list of items

        Returns:
            dict with updated container state

        Raises:
            WearableContainerServiceError: If capacity would be exceeded
        """
        context = create_error_context()
        context.metadata["operation"] = "update_wearable_container_items"
        context.metadata["player_id"] = str(player_id)
        context.metadata["container_id"] = str(container_id)

        # Get current container
        container_data = self.persistence.get_container(container_id)
        if not container_data:
            log_and_raise(
                WearableContainerServiceError,
                f"Container not found: {container_id}",
                context=context,
                details={"container_id": str(container_id)},
                user_friendly="Container not found",
            )

        container = ContainerComponent.model_validate(container_data)

        # Verify it's a wearable container for this player
        if container.source_type != ContainerSourceType.EQUIPMENT or container.entity_id != player_id:
            log_and_raise(
                WearableContainerServiceError,
                "Container is not a wearable container for this player",
                context=context,
                details={
                    "container_id": str(container_id),
                    "source_type": container.source_type.value,
                    "entity_id": str(container.entity_id),
                },
                user_friendly="Invalid container",
            )

        # Check capacity
        if len(items) > container.capacity_slots:
            log_and_raise(
                WearableContainerServiceError,
                f"Container capacity exceeded: {len(items)} > {container.capacity_slots}",
                context=context,
                details={
                    "items_count": len(items),
                    "capacity_slots": container.capacity_slots,
                },
                user_friendly="Container capacity exceeded",
            )

        # Update container
        updated_data = self.persistence.update_container(
            container_id=container_id,
            items_json=items,
        )

        logger.info(
            "Wearable container items updated",
            player_id=str(player_id),
            container_id=str(container_id),
            items_count=len(items),
        )

        return updated_data

    def handle_container_overflow(
        self, player_id: UUID, container_id: UUID, overflow_items: list[dict[str, Any]]
    ) -> dict[str, Any]:
        """
        Handle container overflow by spilling items to inventory or ground.

        Args:
            player_id: UUID of the player
            container_id: UUID of the container
            overflow_items: Items that don't fit in container

        Returns:
            dict with spilled_items and ground_items
        """
        context = create_error_context()
        context.metadata["operation"] = "handle_container_overflow"
        context.metadata["player_id"] = str(player_id)
        context.metadata["container_id"] = str(container_id)

        logger.info(
            "Handling container overflow",
            player_id=str(player_id),
            container_id=str(container_id),
            overflow_count=len(overflow_items),
        )

        # Get player
        player = self.persistence.get_player(player_id)
        if not player:
            log_and_raise(
                WearableContainerServiceError,
                f"Player not found: {player_id}",
                context=context,
                details={"player_id": str(player_id)},
                user_friendly="Player not found",
            )

        # Try to add items to player inventory
        spilled_items = []
        ground_items = []

        player_inventory = getattr(player, "inventory", [])
        max_inventory_slots = 20  # Standard inventory capacity

        for item in overflow_items:
            if len(player_inventory) < max_inventory_slots:
                # Add to inventory
                player_inventory.append(item)
                spilled_items.append(item)
            else:
                # Inventory full, drop to ground
                ground_items.append(item)

        # Update player inventory if items were added
        if spilled_items:
            player.set_inventory(player_inventory)
            self.persistence.save_player(player)

        # Create ground container for dropped items if any
        if ground_items:
            room_id = getattr(player, "current_room_id", None)
            if room_id:
                try:
                    self.persistence.create_container(
                        source_type="environment",
                        room_id=room_id,
                        capacity_slots=20,
                        items_json=ground_items,
                        metadata_json={
                            "overflow_source": str(container_id),
                            "player_id": str(player_id),
                        },
                    )
                    logger.info(
                        "Overflow items dropped to ground",
                        player_id=str(player_id),
                        room_id=room_id,
                        items_count=len(ground_items),
                    )
                except Exception as e:
                    logger.error(
                        "Failed to create ground container for overflow items",
                        error=str(e),
                        player_id=str(player_id),
                        room_id=room_id,
                    )

        logger.info(
            "Container overflow handled",
            player_id=str(player_id),
            container_id=str(container_id),
            spilled_count=len(spilled_items),
            ground_count=len(ground_items),
        )

        return {
            "spilled_items": spilled_items,
            "ground_items": ground_items,
        }
