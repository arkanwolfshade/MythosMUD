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
from typing import Any
from uuid import UUID

from ..exceptions import MythosMUDError, ValidationError
from ..logging.enhanced_logging_config import get_logger
from ..models.container import ContainerComponent, ContainerLockState, ContainerSourceType
from ..utils.audit_logger import audit_logger
from ..utils.error_logging import create_error_context, log_and_raise
from .inventory_mutation_guard import InventoryMutationGuard
from .inventory_service import InventoryCapacityError, InventoryService, InventoryStack

logger = get_logger(__name__)


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
        container = ContainerComponent.model_validate(container_data)

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

        # Check if container is locked (after access validation)
        if container.is_locked():
            # Check if player has key or is admin
            if not self._can_unlock_container(container, player):
                log_and_raise(
                    ContainerLockedError,
                    f"Container is locked: {container_id}",
                    context=context,
                    details={"container_id": str(container_id), "lock_state": container.lock_state.value},
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
                container = ContainerComponent.model_validate(container_data)
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

        container = ContainerComponent.model_validate(container_data)

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

        # Use mutation guard
        with self.mutation_guard.acquire(str(player_id), mutation_token) as decision:
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
            if quantity and quantity < transfer_item.get("quantity", 1):
                transfer_item["quantity"] = quantity

            # Add item to container using InventoryService
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

        container = ContainerComponent.model_validate(container_data)

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

        # Use mutation guard
        with self.mutation_guard.acquire(str(player_id), mutation_token) as decision:
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
            if quantity and quantity < transfer_item.get("quantity", 1):
                transfer_item["quantity"] = quantity

            # Remove item from container
            # Find and remove item from container.items
            new_container_items = []
            item_found = False
            for stack in container.items:
                if stack.get("item_id") == transfer_item.get("item_id") and stack.get(
                    "item_instance_id"
                ) == transfer_item.get("item_instance_id"):
                    item_found = True
                    remaining_quantity = stack.get("quantity", 1) - transfer_item.get("quantity", 1)
                    if remaining_quantity > 0:
                        new_stack = stack.copy()
                        new_stack["quantity"] = remaining_quantity
                        new_container_items.append(new_stack)
                else:
                    new_container_items.append(stack)

            if not item_found:
                log_and_raise(
                    ContainerServiceError,
                    f"Item not found in container: {transfer_item.get('item_id')}",
                    context=context,
                    details={"item_id": transfer_item.get("item_id"), "container_id": str(container_id)},
                    user_friendly="Item not found in container",
                )

            # Add item to player inventory using InventoryService
            player_inventory = getattr(player, "inventory", [])
            try:
                new_player_inventory = self.inventory_service.add_stack(player_inventory, transfer_item)
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
                quantity=transfer_item.get("quantity"),
            )

            # Audit log container transfer
            try:
                audit_logger.log_container_interaction(
                    player_id=str(player_id),
                    player_name=player.name,
                    container_id=str(container_id),
                    event_type="container_transfer",
                    source_type=container.source_type.value,
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
            if container.entity_id != player_id:
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

        container = ContainerComponent.model_validate(container_data)

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

        container = ContainerComponent.model_validate(container_data)

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
