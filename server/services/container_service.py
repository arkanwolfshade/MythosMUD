"""
Container service for unified container system operations.

As documented in the restricted archives of Miskatonic University, container
service operations require careful orchestration to ensure proper handling
of investigator artifacts, secure storage, and auditable interactions.
"""

from __future__ import annotations

import uuid
from dataclasses import dataclass, field
from datetime import UTC, datetime, timedelta
from typing import Any, cast
from uuid import UUID

from ..exceptions import MythosMUDError, ValidationError
from ..logging.enhanced_logging_config import get_logger
from ..models.container import ContainerComponent, ContainerLockState, ContainerSourceType
from ..utils.audit_logger import audit_logger
from ..utils.error_logging import create_error_context, log_and_raise
from .inventory_mutation_guard import InventoryMutationGuard
from .inventory_service import InventoryCapacityError, InventoryService, InventoryStack

logger = get_logger(__name__)


def _get_enum_value(enum_or_str: Any) -> str:
    """
    Safely get enum value, handling both enum instances and string values.

    When containers are deserialized from the database, enum fields may be strings
    instead of enum instances. This helper handles both cases.

    Args:
        enum_or_str: Either an enum instance or a string value

    Returns:
        String value of the enum
    """
    if hasattr(enum_or_str, "value"):
        return enum_or_str.value
    return str(enum_or_str)


def _filter_container_data(container_data: dict[str, Any]) -> dict[str, Any]:
    """
    Filter out database-specific fields that are not part of the ContainerComponent model.

    The database returns created_at and updated_at fields, but the ContainerComponent
    model has extra="forbid", so these fields must be removed before validation.

    Args:
        container_data: Raw container data from database

    Returns:
        Filtered container data without database-specific fields
    """
    filtered = {k: v for k, v in container_data.items() if k not in ("created_at", "updated_at")}
    return filtered


class ContainerServiceError(MythosMUDError):
    """Base exception for container service operations."""


class ContainerNotFoundError(ContainerServiceError):
    """Raised when a container is not found."""


class ContainerLockedError(ContainerServiceError):
    """Raised when attempting to access a locked container."""


class ContainerCapacityError(ContainerServiceError):
    """Raised when container capacity is exceeded."""


class ContainerAccessDeniedError(ContainerServiceError):
    """Raised when access to container is denied."""


@dataclass
class ContainerService:
    """
    Service for managing container operations.

    Orchestrates open/close, transfer operations, and mutation guards
    for the unified container system.
    """

    persistence: Any
    inventory_service: InventoryService = field(default_factory=lambda: InventoryService(max_slots=20))
    mutation_guard: InventoryMutationGuard = field(default_factory=InventoryMutationGuard)

    # Track open containers: {container_id: {player_id: mutation_token}}
    _open_containers: dict[UUID, dict[UUID, str]] = field(default_factory=dict, init=False)

    def open_container(self, container_id: UUID, player_id: UUID) -> dict[str, Any]:
        """
        Open a container for interaction.

        Args:
            container_id: Container UUID to open
            player_id: Player UUID opening the container

        Returns:
            dict containing container data and mutation_token

        Raises:
            ContainerNotFoundError: If container doesn't exist
            ContainerLockedError: If container is locked
            ContainerServiceError: If container is already open
        """
        context = create_error_context()
        context.metadata["operation"] = "open_container"
        context.metadata["container_id"] = str(container_id)
        context.metadata["player_id"] = str(player_id)

        logger.info("Opening container", container_id=str(container_id), player_id=str(player_id))

        # Check if container exists
        container_data = self.persistence.get_container(container_id)
        if not container_data:
            log_and_raise(
                ContainerNotFoundError,
                f"Container not found: {container_id}",
                context=context,
                details={"container_id": str(container_id)},
                user_friendly="Container not found",
            )

        # Convert to ContainerComponent
        container = ContainerComponent.model_validate(_filter_container_data(container_data))

        # Get player for access control checks
        player = self.persistence.get_player(player_id)
        if not player:
            log_and_raise(
                ValidationError,
                f"Player not found: {player_id}",
                context=context,
                details={"player_id": str(player_id)},
                user_friendly="Player not found",
            )

        # Validate access control (proximity, roles, ownership)
        self._validate_container_access(container, player, context)

        # Check if container is sealed (raises access denied, not locked error)
        if container.lock_state == ContainerLockState.SEALED:
            if not getattr(player, "is_admin", False):
                log_and_raise(
                    ContainerAccessDeniedError,
                    f"Container is sealed: {container_id}",
                    context=context,
                    details={
                        "container_id": str(container_id),
                        "lock_state": _get_enum_value(container.lock_state),
                    },
                    user_friendly="Container is sealed",
                )

        # Check if container is locked (after access validation)
        if container.is_locked():
            # Check if player has key or is admin
            if not self._can_unlock_container(container, player):
                log_and_raise(
                    ContainerLockedError,
                    f"Container is locked: {container_id}",
                    context=context,
                    details={"container_id": str(container_id), "lock_state": _get_enum_value(container.lock_state)},
                    user_friendly="Container is locked",
                )

        # Check if container is already open by this player
        if container_id in self._open_containers and player_id in self._open_containers[container_id]:
            log_and_raise(
                ContainerServiceError,
                f"Container already open: {container_id}",
                context=context,
                details={"container_id": str(container_id), "player_id": str(player_id)},
                user_friendly="Container is already open",
            )

        # Generate mutation token
        mutation_token = str(uuid.uuid4())

        # Track open container
        if container_id not in self._open_containers:
            self._open_containers[container_id] = {}
        self._open_containers[container_id][player_id] = mutation_token

        logger.info(
            "Container opened",
            container_id=str(container_id),
            player_id=str(player_id),
            mutation_token=mutation_token,
        )

        # Audit log container open
        try:
            # Handle source_type - it may be an enum or a string
            source_type_value = (
                container.source_type.value if hasattr(container.source_type, "value") else str(container.source_type)
            )
            audit_logger.log_container_interaction(
                player_id=str(player_id),
                player_name=player.name,
                container_id=str(container_id),
                event_type="container_open",
                source_type=source_type_value,
                room_id=container.room_id,
                success=True,
            )
        except Exception as e:
            logger.warning("Failed to log container open to audit log", error=str(e))

        return {
            "container": container.model_dump(),
            "mutation_token": mutation_token,
        }

    def close_container(self, container_id: UUID, player_id: UUID, mutation_token: str) -> None:
        """
        Close a container and release mutation guard.

        Args:
            container_id: Container UUID to close
            player_id: Player UUID closing the container
            mutation_token: Mutation token from open operation

        Raises:
            ContainerServiceError: If container is not open or token is invalid
        """
        context = create_error_context()
        context.metadata["operation"] = "close_container"
        context.metadata["container_id"] = str(container_id)
        context.metadata["player_id"] = str(player_id)

        logger.info("Closing container", container_id=str(container_id), player_id=str(player_id))

        # Check if container is open
        if container_id not in self._open_containers:
            log_and_raise(
                ContainerServiceError,
                f"Container not open: {container_id}",
                context=context,
                details={"container_id": str(container_id)},
                user_friendly="Container is not open",
            )

        if player_id not in self._open_containers[container_id]:
            log_and_raise(
                ContainerServiceError,
                f"Container not open by player: {container_id}",
                context=context,
                details={"container_id": str(container_id), "player_id": str(player_id)},
                user_friendly="Container is not open",
            )

        # Verify mutation token
        stored_token = self._open_containers[container_id][player_id]
        if stored_token != mutation_token:
            log_and_raise(
                ContainerServiceError,
                f"Invalid mutation token: {container_id}",
                context=context,
                details={"container_id": str(container_id), "player_id": str(player_id)},
                user_friendly="Invalid mutation token",
            )

        # Remove from open containers
        del self._open_containers[container_id][player_id]
        if not self._open_containers[container_id]:
            del self._open_containers[container_id]

        logger.info("Container closed", container_id=str(container_id), player_id=str(player_id))

        # Audit log container close
        try:
            # Get container and player for audit log
            container_data = self.persistence.get_container(container_id)
            player = self.persistence.get_player(player_id)
            if container_data and player:
                container = ContainerComponent.model_validate(_filter_container_data(container_data))
                # Handle source_type - it may be an enum or a string
                source_type_value = (
                    container.source_type.value
                    if hasattr(container.source_type, "value")
                    else str(container.source_type)
                )
                audit_logger.log_container_interaction(
                    player_id=str(player_id),
                    player_name=player.name,
                    container_id=str(container_id),
                    event_type="container_close",
                    source_type=source_type_value,
                    room_id=container.room_id,
                    success=True,
                )
        except Exception as e:
            logger.warning("Failed to log container close to audit log", error=str(e))

    def get_container_token(self, container_id: UUID, player_id: UUID) -> str | None:
        """
        Get existing mutation token if container is already open by this player.

        Args:
            container_id: Container UUID
            player_id: Player UUID

        Returns:
            Mutation token string if container is open, None otherwise
        """
        if container_id in self._open_containers:
            return self._open_containers[container_id].get(player_id)
        return None

    def transfer_to_container(
        self,
        container_id: UUID,
        player_id: UUID,
        mutation_token: str,
        item: InventoryStack,
        quantity: int | None = None,
    ) -> dict[str, Any]:
        """
        Transfer items from player inventory to container.

        Args:
            container_id: Container UUID
            player_id: Player UUID
            mutation_token: Mutation token from open operation
            item: Item stack to transfer
            quantity: Optional quantity to transfer (default: all)

        Returns:
            dict containing updated container and player inventory

        Raises:
            ContainerServiceError: If container is not open or token is invalid
            ContainerCapacityError: If container capacity is exceeded
        """
        context = create_error_context()
        context.metadata["operation"] = "transfer_to_container"
        context.metadata["container_id"] = str(container_id)
        context.metadata["player_id"] = str(player_id)
        context.metadata["item_id"] = item.get("item_id", "unknown")

        logger.info(
            "Transferring item to container",
            container_id=str(container_id),
            player_id=str(player_id),
            item_id=item.get("item_id"),
            quantity=quantity,
        )

        # Verify container is open (using the open token)
        self._verify_container_open(container_id, player_id, mutation_token)

        # Use the original mutation token for the mutation guard
        # This ensures that duplicate operations with the same token are prevented
        # The mutation guard will detect if the same token is used multiple times
        transfer_mutation_token = mutation_token

        # Get container
        container_data = self.persistence.get_container(container_id)
        if not container_data:
            log_and_raise(
                ContainerNotFoundError,
                f"Container not found: {container_id}",
                context=context,
                details={"container_id": str(container_id)},
                user_friendly="Container not found",
            )

        # Instrumentation: validate and log container_data structure before Pydantic validation
        if isinstance(container_data, dict):
            items_field = container_data.get("items")
            logger.debug(
                "Container data before validation",
                container_id=str(container_id),
                player_id=str(player_id),
                container_keys=list(container_data.keys()),
                items_type=type(items_field).__name__ if items_field is not None else None,
                items_sample=str(items_field)[:200] if items_field is not None else None,
            )
            if items_field is not None and not isinstance(items_field, list):
                logger.error(
                    "Container items field is not a list before validation",
                    container_id=str(container_id),
                    player_id=str(player_id),
                    items_type=type(items_field).__name__,
                    items_value=str(items_field)[:200],
                )
        else:
            logger.debug(
                "Non-dict container_data returned from persistence",
                container_id=str(container_id),
                player_id=str(player_id),
                container_data_type=type(container_data).__name__,
                container_data_repr=str(container_data)[:200],
            )

        container = ContainerComponent.model_validate(_filter_container_data(container_data))

        # Check capacity
        if not container.has_capacity():
            log_and_raise(
                ContainerCapacityError,
                f"Container capacity exceeded: {container_id}",
                context=context,
                details={
                    "container_id": str(container_id),
                    "capacity_slots": container.capacity_slots,
                    "used_slots": container.get_used_slots(),
                },
                user_friendly="Container is full",
            )

        # Check weight limit if specified
        if container.weight_limit is not None:
            # Calculate current weight (simplified - would need item weight data)
            # For now, we'll skip weight validation as it requires item prototype data
            # This can be enhanced later with proper weight calculation
            pass

        # Get player inventory
        player = self.persistence.get_player(player_id)
        if not player:
            log_and_raise(
                ValidationError,
                f"Player not found: {player_id}",
                context=context,
                details={"player_id": str(player_id)},
                user_friendly="Player not found",
            )

        # Use mutation guard with the new transfer-specific token
        with self.mutation_guard.acquire(str(player_id), transfer_mutation_token) as decision:
            if not decision.should_apply:
                logger.warning(
                    "Transfer suppressed by mutation guard",
                    container_id=str(container_id),
                    player_id=str(player_id),
                    duplicate=decision.duplicate,
                )
                raise ContainerServiceError("Transfer suppressed by mutation guard")

            # Prepare item for transfer
            transfer_item = item.copy()
            if quantity is not None:
                # Use the provided quantity (may be less than or equal to item quantity)
                transfer_item["quantity"] = quantity

            # Add item to container using InventoryService
            # Note: slot_type is always present in items from containers and player inventory
            # If missing, add_stack will raise InventoryValidationError
            try:
                new_container_items = self.inventory_service.add_stack(container.items, transfer_item)
            except InventoryCapacityError as e:
                log_and_raise(
                    ContainerCapacityError,
                    f"Container capacity exceeded: {e}",
                    context=context,
                    details={"container_id": str(container_id), "error": str(e)},
                    user_friendly="Container is full",
                )

            # Remove item from player inventory
            # This would use InventoryService.remove_stack or similar
            # For now, we'll update the container and return
            container.items = new_container_items

            # Persist container
            self.persistence.update_container(
                container_id,
                items_json=new_container_items,
            )

            logger.info(
                "Item transferred to container",
                container_id=str(container_id),
                player_id=str(player_id),
                item_id=item.get("item_id"),
                quantity=transfer_item.get("quantity"),
            )

            # Audit log container transfer
            try:
                # Handle source_type - it may be an enum or a string
                source_type_value = (
                    container.source_type.value
                    if hasattr(container.source_type, "value")
                    else str(container.source_type)
                )
                audit_logger.log_container_interaction(
                    player_id=str(player_id),
                    player_name=player.name,
                    container_id=str(container_id),
                    event_type="container_transfer",
                    source_type=source_type_value,
                    room_id=container.room_id,
                    direction="to_container",
                    item_id=item.get("item_id"),
                    item_name=item.get("item_name"),
                    success=True,
                )
            except Exception as e:
                logger.warning("Failed to log container transfer to audit log", error=str(e))

            return {
                "container": container.model_dump(),
                "player_inventory": player.inventory if hasattr(player, "inventory") else [],
            }

    def transfer_from_container(
        self,
        container_id: UUID,
        player_id: UUID,
        mutation_token: str,
        item: InventoryStack,
        quantity: int | None = None,
    ) -> dict[str, Any]:
        """
        Transfer items from container to player inventory.

        Args:
            container_id: Container UUID
            player_id: Player UUID
            mutation_token: Mutation token from open operation
            item: Item stack to transfer
            quantity: Optional quantity to transfer (default: all)

        Returns:
            dict containing updated container and player inventory

        Raises:
            ContainerServiceError: If container is not open or token is invalid
            ValidationError: If player not found
        """
        # Ensure item is a dictionary before using it
        if not isinstance(item, dict):
            log_and_raise(
                ContainerServiceError,
                f"Item must be a dictionary, got {type(item).__name__}",
                context=create_error_context(),
                details={"item_type": type(item).__name__, "item": str(item)},
                user_friendly="Invalid item data format",
            )

        context = create_error_context()
        context.metadata["operation"] = "transfer_from_container"
        context.metadata["container_id"] = str(container_id)
        context.metadata["player_id"] = str(player_id)
        context.metadata["item_id"] = item.get("item_id", "unknown")

        logger.info(
            "Transferring item from container",
            container_id=str(container_id),
            player_id=str(player_id),
            item_id=item.get("item_id"),
            quantity=quantity,
        )

        # Verify container is open (using the open token)
        self._verify_container_open(container_id, player_id, mutation_token)

        # Use the original mutation token for the mutation guard
        # This ensures that duplicate operations with the same token are prevented
        # The mutation guard will detect if the same token is used multiple times
        transfer_mutation_token = mutation_token

        # Get container
        container_data = self.persistence.get_container(container_id)
        if not container_data:
            log_and_raise(
                ContainerNotFoundError,
                f"Container not found: {container_id}",
                context=context,
                details={"container_id": str(container_id)},
                user_friendly="Container not found",
            )

        container = ContainerComponent.model_validate(_filter_container_data(container_data))

        # Get player inventory
        player = self.persistence.get_player(player_id)
        if not player:
            log_and_raise(
                ValidationError,
                f"Player not found: {player_id}",
                context=context,
                details={"player_id": str(player_id)},
                user_friendly="Player not found",
            )

        # Use mutation guard with the new transfer-specific token
        with self.mutation_guard.acquire(str(player_id), transfer_mutation_token) as decision:
            if not decision.should_apply:
                logger.warning(
                    "Transfer suppressed by mutation guard",
                    container_id=str(container_id),
                    player_id=str(player_id),
                    duplicate=decision.duplicate,
                )
                raise ContainerServiceError("Transfer suppressed by mutation guard")

            try:
                # Prepare item for transfer
                transfer_item = item.copy()
                # Ensure transfer_item is still a dictionary after copy
                if not isinstance(transfer_item, dict):
                    log_and_raise(
                        ContainerServiceError,
                        f"Item copy is not a dictionary, got {type(transfer_item).__name__}",
                        context=context,
                        details={
                            "item_type": type(item).__name__,
                            "transfer_item_type": type(transfer_item).__name__,
                            "item": str(item),
                        },
                        user_friendly="Invalid item data format",
                    )
                # After the check above, transfer_item is guaranteed to be a dict
                # Mypy needs explicit type narrowing via cast
                transfer_item_dict = cast(dict[str, Any], transfer_item)
                if quantity and quantity < transfer_item_dict.get("quantity", 1):
                    transfer_item_dict["quantity"] = quantity
                # Preserve original slot_type if present (for equippable items)
                # If the item was equipped before being put in the container, restore that slot_type
                # Check both direct slot_type field and metadata for backward compatibility
                if "slot_type" not in transfer_item_dict:
                    item_metadata = transfer_item_dict.get("metadata", {})
                    if isinstance(item_metadata, dict) and "slot_type" in item_metadata:
                        transfer_item_dict["slot_type"] = item_metadata["slot_type"]
                    else:
                        # Default to "backpack" for general inventory if no slot_type found
                        transfer_item_dict["slot_type"] = "backpack"

                # Remove item from container
                # Find and remove item from container.items
                new_container_items = []
                item_found = False

                # Instrumentation: log container.items structure before mutation
                logger.debug(
                    "Container items before transfer_from_container",
                    container_id=str(container_id),
                    player_id=str(player_id),
                    items_length=len(container.items),
                    items_types=[type(stack).__name__ for stack in container.items[:5]],
                    items_sample=[str(stack)[:100] for stack in container.items[:3]],
                )

                for stack in container.items:
                    # Note: InventoryStack is a TypedDict (dict-like), so stack is always a dict
                    # No need for isinstance check - mypy knows the type

                    # Note: transfer_item_dict is already guaranteed to be a dict from the check above
                    # This defensive check is kept for runtime safety but is unreachable according to mypy

                    if stack.get("item_id") == transfer_item_dict.get("item_id") and stack.get(
                        "item_instance_id"
                    ) == transfer_item_dict.get("item_instance_id"):
                        item_found = True
                        remaining_quantity = stack.get("quantity", 1) - transfer_item_dict.get("quantity", 1)
                        if remaining_quantity > 0:
                            new_stack = stack.copy()
                            new_stack["quantity"] = remaining_quantity
                            new_container_items.append(new_stack)
                    else:
                        new_container_items.append(stack)

                if not item_found:
                    log_and_raise(
                        ContainerServiceError,
                        f"Item not found in container: {transfer_item_dict.get('item_id')}",
                        context=context,
                        details={"item_id": transfer_item_dict.get("item_id"), "container_id": str(container_id)},
                        user_friendly="Item not found in container",
                    )

                # Add item to player inventory using InventoryService
                player_inventory = getattr(player, "inventory", [])

                # Instrumentation: log player inventory structure before mutation
                try:
                    inventory_length = len(player_inventory)
                except TypeError:
                    inventory_length = None

                logger.debug(
                    "Player inventory before add_stack",
                    container_id=str(container_id),
                    player_id=str(player_id),
                    inventory_length=inventory_length,
                    inventory_types=[type(stack).__name__ for stack in list(player_inventory)[:5]]
                    if isinstance(player_inventory, (list, tuple))
                    else type(player_inventory).__name__,
                )

                try:
                    new_player_inventory = self.inventory_service.add_stack(player_inventory, transfer_item_dict)
                except InventoryCapacityError as e:
                    log_and_raise(
                        ContainerCapacityError,
                        f"Player inventory capacity exceeded: {e}",
                        context=context,
                        details={"player_id": str(player_id), "error": str(e)},
                        user_friendly="Your inventory is full",
                    )

                # Update container
                container.items = new_container_items

                # Persist container
                self.persistence.update_container(
                    container_id,
                    items_json=new_container_items,
                )

                logger.info(
                    "Item transferred from container",
                    container_id=str(container_id),
                    player_id=str(player_id),
                    item_id=item.get("item_id"),
                    quantity=transfer_item_dict.get("quantity"),
                )

                # Audit log container transfer
                try:
                    audit_logger.log_container_interaction(
                        player_id=str(player_id),
                        player_name=player.name,
                        container_id=str(container_id),
                        event_type="container_transfer",
                        source_type=_get_enum_value(container.source_type),
                        room_id=container.room_id,
                        direction="from_container",
                        item_id=item.get("item_id"),
                        item_name=item.get("item_name"),
                        success=True,
                    )
                except Exception as e:
                    logger.warning("Failed to log container transfer to audit log", error=str(e))

                return {
                    "container": container.model_dump(),
                    "player_inventory": new_player_inventory,
                }
            except Exception as e:
                # Instrumentation: capture unexpected errors, including type issues like 'str'.get
                logger.error(
                    "Unexpected error during transfer_from_container",
                    container_id=str(container_id),
                    player_id=str(player_id),
                    item_type=type(item).__name__,
                    item_value=str(item),
                    container_items_length=len(getattr(container, "items", [])),
                    container_items_types=[type(stack).__name__ for stack in getattr(container, "items", [])[:5]],
                    error=str(e),
                    error_type=type(e).__name__,
                )
                raise

    def loot_all(
        self,
        container_id: UUID,
        player_id: UUID,
        mutation_token: str,
    ) -> dict[str, Any]:
        """
        Loot all eligible items from a container.

        Convenience method to transfer all items from container to player inventory,
        subject to capacity constraints. Requires a valid mutation token from open_container.

        Args:
            container_id: Container UUID
            player_id: Player UUID
            mutation_token: Mutation token from open operation

        Returns:
            dict containing updated container and player_inventory

        Raises:
            ContainerServiceError: If container is not open or token is invalid
            ContainerCapacityError: If player inventory capacity is exceeded (stops at that point)
        """
        context = create_error_context()
        context.metadata["operation"] = "loot_all"
        context.metadata["container_id"] = str(container_id)
        context.metadata["player_id"] = str(player_id)

        logger.info(
            "Looting all items from container",
            container_id=str(container_id),
            player_id=str(player_id),
        )

        # Verify container is open
        self._verify_container_open(container_id, player_id, mutation_token)

        # Get container
        container_data = self.persistence.get_container(container_id)
        if not container_data:
            log_and_raise(
                ContainerNotFoundError,
                f"Container not found: {container_id}",
                context=context,
                details={"container_id": str(container_id)},
                user_friendly="Container not found",
            )

        container = ContainerComponent.model_validate(_filter_container_data(container_data))

        # Store initial item count for audit logging
        initial_items_count = len(container.items)

        # Get player
        player = self.persistence.get_player(player_id)
        if not player:
            log_and_raise(
                ContainerServiceError,
                f"Player not found: {player_id}",
                context=context,
                details={"player_id": str(player_id)},
                user_friendly="Player not found",
            )

        player_inventory = getattr(player, "inventory", [])

        # Try to transfer each item
        for item in container.items:
            try:
                result = self.transfer_from_container(
                    container_id,
                    player_id,
                    mutation_token,
                    item,
                    item.get("quantity", 1),
                )
                # Update container and player inventory from result
                container_data = result.get("container", {})
                container = ContainerComponent.model_validate(_filter_container_data(container_data))
                player_inventory = result.get("player_inventory", player_inventory)
            except ContainerCapacityError:
                # Stop if capacity exceeded
                logger.warning(
                    "Loot-all stopped due to capacity",
                    container_id=str(container_id),
                    player_id=str(player_id),
                )
                break
            except Exception as e:
                # Log but continue with other items
                logger.warning(
                    "Error transferring item during loot-all",
                    error=str(e),
                    container_id=str(container_id),
                    player_id=str(player_id),
                )
                continue

        # Get final container state
        final_container_data = self.persistence.get_container(container_id)
        if final_container_data:
            final_container = ContainerComponent.model_validate(final_container_data)
        else:
            final_container = container

        # Log audit event
        audit_logger.log_container_interaction(
            player_id=str(player_id),
            player_name=getattr(player, "name", "Unknown"),
            container_id=str(container_id),
            event_type="container_loot_all",
            source_type=_get_enum_value(final_container.source_type),
            room_id=final_container.room_id,
            items_count=initial_items_count,
        )

        return {
            "container": final_container.to_dict(),
            "player_inventory": player_inventory,
            "mutation_token": mutation_token,
        }

    def _verify_container_open(self, container_id: UUID, player_id: UUID, mutation_token: str) -> None:
        """
        Verify that a container is open by the specified player with the given token.

        Args:
            container_id: Container UUID
            player_id: Player UUID
            mutation_token: Mutation token

        Raises:
            ContainerServiceError: If container is not open or token is invalid
        """
        if container_id not in self._open_containers:
            raise ContainerServiceError(f"Container not open: {container_id}")

        if player_id not in self._open_containers[container_id]:
            raise ContainerServiceError(f"Container not open by player: {container_id}")

        stored_token = self._open_containers[container_id][player_id]
        if stored_token != mutation_token:
            raise ContainerServiceError(f"Invalid mutation token: {container_id}")

    def _validate_container_access(self, container: ContainerComponent, player: Any, context: Any) -> None:
        """
        Validate that player has access to the container.

        Checks proximity, ownership, roles, and grace periods.

        Args:
            container: Container to check access for
            player: Player object
            context: Error context for logging

        Raises:
            ContainerAccessDeniedError: If access is denied
        """
        player_id = getattr(player, "player_id", None) or getattr(player, "id", None)
        is_admin = getattr(player, "is_admin", False)

        # Check proximity for environment and corpse containers
        if container.source_type in (ContainerSourceType.ENVIRONMENT, ContainerSourceType.CORPSE):
            player_room_id = getattr(player, "current_room_id", None)
            if player_room_id != container.room_id:
                log_and_raise(
                    ContainerAccessDeniedError,
                    f"Player not in same room as container: {container.container_id}",
                    context=context,
                    details={
                        "container_id": str(container.container_id),
                        "player_id": str(player_id),
                        "container_room_id": container.room_id,
                        "player_room_id": player_room_id,
                    },
                    user_friendly="You must be in the same room as the container",
                )

        # Check ownership for equipment containers
        if container.source_type == ContainerSourceType.EQUIPMENT:
            # Normalize both IDs to UUID for comparison
            # This handles cases where one is a UUID object and the other is a string
            player_id_uuid = UUID(str(player_id)) if player_id else None
            container_entity_id_uuid = UUID(str(container.entity_id)) if container.entity_id else None
            if container_entity_id_uuid != player_id_uuid:
                log_and_raise(
                    ContainerAccessDeniedError,
                    f"Player does not own equipment container: {container.container_id}",
                    context=context,
                    details={
                        "container_id": str(container.container_id),
                        "player_id": str(player_id),
                        "owner_id": str(container.entity_id),
                    },
                    user_friendly="You do not own this container",
                )

        # Check role-based access control
        if container.allowed_roles and not is_admin:
            # Get player role (simplified - would need proper role system)
            player_role = "admin" if is_admin else "player"
            if player_role not in container.allowed_roles:
                log_and_raise(
                    ContainerAccessDeniedError,
                    f"Player role not allowed: {container.container_id}",
                    context=context,
                    details={
                        "container_id": str(container.container_id),
                        "player_id": str(player_id),
                        "player_role": player_role,
                        "allowed_roles": container.allowed_roles,
                    },
                    user_friendly="You do not have permission to access this container",
                )

        # Check corpse grace period
        if container.source_type == ContainerSourceType.CORPSE and container.owner_id:
            grace_period_seconds = container.metadata.get("grace_period_seconds", 300)  # Default 5 minutes
            grace_period_start_str = container.metadata.get("grace_period_start")

            if grace_period_start_str:
                grace_period_start = datetime.fromisoformat(grace_period_start_str.replace("Z", "+00:00"))
                grace_period_end = grace_period_start + timedelta(seconds=grace_period_seconds)
                current_time = datetime.now(UTC)

                # If still in grace period, only owner can access
                if current_time < grace_period_end and container.owner_id != player_id and not is_admin:
                    log_and_raise(
                        ContainerAccessDeniedError,
                        f"Corpse grace period active: {container.container_id}",
                        context=context,
                        details={
                            "container_id": str(container.container_id),
                            "player_id": str(player_id),
                            "owner_id": str(container.owner_id),
                            "grace_period_end": grace_period_end.isoformat(),
                        },
                        user_friendly="The corpse's owner has exclusive access during the grace period",
                    )
            else:
                # No grace_period_start means grace period is still active (just created)
                # Only owner can access during grace period
                if container.owner_id != player_id and not is_admin:
                    log_and_raise(
                        ContainerAccessDeniedError,
                        f"Corpse grace period active: {container.container_id}",
                        context=context,
                        details={
                            "container_id": str(container.container_id),
                            "player_id": str(player_id),
                            "owner_id": str(container.owner_id),
                        },
                        user_friendly="The corpse's owner has exclusive access during the grace period",
                    )

    def _can_unlock_container(self, container: ContainerComponent, player: Any) -> bool:
        """
        Check if player can unlock the container.

        Args:
            container: Container to check
            player: Player object

        Returns:
            bool: True if player can unlock, False otherwise
        """
        # Admins can always unlock
        if getattr(player, "is_admin", False):
            return True

        # Sealed containers cannot be unlocked by non-admins
        if container.lock_state == ContainerLockState.SEALED:
            return False

        # Check if container requires a key
        key_item_id = container.metadata.get("key_item_id")
        if key_item_id:
            # Check if player has the key in inventory
            player_inventory = getattr(player, "inventory", [])
            for item in player_inventory:
                if item.get("item_id") == key_item_id:
                    return True
            # Player doesn't have the key
            return False

        # Locked containers without a key requirement still require admin to unlock
        # If no key is specified, only admins can unlock locked containers
        if container.lock_state == ContainerLockState.LOCKED:
            return False

        # Unlocked containers can be opened
        return container.lock_state == ContainerLockState.UNLOCKED

    def lock_container(self, container_id: UUID, player_id: UUID, lock_state: ContainerLockState) -> dict[str, Any]:
        """
        Lock a container.

        Args:
            container_id: Container UUID
            player_id: Player UUID performing the lock
            lock_state: Lock state to set (LOCKED or SEALED)

        Returns:
            dict containing updated container data

        Raises:
            ContainerNotFoundError: If container doesn't exist
            ContainerServiceError: If lock operation fails
        """
        context = create_error_context()
        context.metadata["operation"] = "lock_container"
        context.metadata["container_id"] = str(container_id)
        context.metadata["player_id"] = str(player_id)

        logger.info(
            "Locking container", container_id=str(container_id), player_id=str(player_id), lock_state=lock_state.value
        )

        # Get container
        container_data = self.persistence.get_container(container_id)
        if not container_data:
            log_and_raise(
                ContainerNotFoundError,
                f"Container not found: {container_id}",
                context=context,
                details={"container_id": str(container_id)},
                user_friendly="Container not found",
            )

        container = ContainerComponent.model_validate(_filter_container_data(container_data))

        # Get player for access control
        player = self.persistence.get_player(player_id)
        if not player:
            log_and_raise(
                ValidationError,
                f"Player not found: {player_id}",
                context=context,
                details={"player_id": str(player_id)},
                user_friendly="Player not found",
            )

        # Validate access (must own or be admin)
        is_admin = getattr(player, "is_admin", False)
        player_id_uuid = getattr(player, "player_id", None) or getattr(player, "id", None)

        if not is_admin:
            if container.source_type == ContainerSourceType.EQUIPMENT:
                if container.entity_id != player_id_uuid:
                    log_and_raise(
                        ContainerAccessDeniedError,
                        f"Player does not own container: {container_id}",
                        context=context,
                        details={"container_id": str(container_id), "player_id": str(player_id)},
                        user_friendly="You do not own this container",
                    )
            elif container.owner_id and container.owner_id != player_id_uuid:
                log_and_raise(
                    ContainerAccessDeniedError,
                    f"Player does not own container: {container_id}",
                    context=context,
                    details={"container_id": str(container_id), "player_id": str(player_id)},
                    user_friendly="You do not own this container",
                )

        # Update lock state
        updated = self.persistence.update_container(container_id, lock_state=lock_state.value)
        if not updated:
            log_and_raise(
                ContainerServiceError,
                f"Failed to lock container: {container_id}",
                context=context,
                details={"container_id": str(container_id)},
                user_friendly="Failed to lock container",
            )

        logger.info(
            "Container locked", container_id=str(container_id), player_id=str(player_id), lock_state=lock_state.value
        )

        return updated

    def unlock_container(self, container_id: UUID, player_id: UUID) -> dict[str, Any]:
        """
        Unlock a container.

        Args:
            container_id: Container UUID
            player_id: Player UUID performing the unlock

        Returns:
            dict containing updated container data

        Raises:
            ContainerNotFoundError: If container doesn't exist
            ContainerServiceError: If unlock operation fails
        """
        context = create_error_context()
        context.metadata["operation"] = "unlock_container"
        context.metadata["container_id"] = str(container_id)
        context.metadata["player_id"] = str(player_id)

        logger.info("Unlocking container", container_id=str(container_id), player_id=str(player_id))

        # Get container
        container_data = self.persistence.get_container(container_id)
        if not container_data:
            log_and_raise(
                ContainerNotFoundError,
                f"Container not found: {container_id}",
                context=context,
                details={"container_id": str(container_id)},
                user_friendly="Container not found",
            )

        container = ContainerComponent.model_validate(_filter_container_data(container_data))

        # Get player for access control
        player = self.persistence.get_player(player_id)
        if not player:
            log_and_raise(
                ValidationError,
                f"Player not found: {player_id}",
                context=context,
                details={"player_id": str(player_id)},
                user_friendly="Player not found",
            )

        # Validate access control (proximity, roles, ownership)
        self._validate_container_access(container, player, context)

        # Check if player can unlock
        if not self._can_unlock_container(container, player):
            log_and_raise(
                ContainerAccessDeniedError,
                f"Player cannot unlock container: {container_id}",
                context=context,
                details={"container_id": str(container_id), "player_id": str(player_id)},
                user_friendly="You cannot unlock this container",
            )

        # Update lock state to unlocked
        updated = self.persistence.update_container(container_id, lock_state=ContainerLockState.UNLOCKED.value)
        if not updated:
            log_and_raise(
                ContainerServiceError,
                f"Failed to unlock container: {container_id}",
                context=context,
                details={"container_id": str(container_id)},
                user_friendly="Failed to unlock container",
            )

        logger.info("Container unlocked", container_id=str(container_id), player_id=str(player_id))

        return updated
