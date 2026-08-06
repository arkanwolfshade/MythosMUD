"""
Container inventory transfer and loot operations.

Mixin host: ContainerService.
"""

from __future__ import annotations

from typing import cast
from uuid import UUID

from ..async_persistence import AsyncPersistenceLayer
from ..exceptions import ValidationError
from ..models.container import ContainerComponent
from ..models.player import Player
from ..structured_logging.enhanced_logging_config import get_logger
from ..utils.audit_logger import audit_logger
from ..utils.error_logging import log_and_raise
from .container_service_access import ContainerAccessMixin
from .container_service_helpers import (
    ContainerCapacityError,
    ContainerNotFoundError,
    ContainerServiceError,
    as_object_dict,
    filter_container_data,
    items_json_for_persist,
    player_inventory_for_response,
)
from .inventory_mutation_guard import InventoryMutationGuard
from .inventory_service import InventoryCapacityError, InventoryService, InventoryStack

logger = get_logger(__name__)


class ContainerTransferToMixin(ContainerAccessMixin):  # pylint: disable=too-few-public-methods  # Reason: mixin host for ContainerService transfer-in API
    """Transfer items into containers."""

    # Host ContainerService rebinds these fields on instances.
    # cast(object, None) only satisfies basedpyright reportUninitializedInstanceVariable.
    inventory_service: InventoryService = cast(InventoryService, cast(object, None))
    persistence: AsyncPersistenceLayer = cast(AsyncPersistenceLayer, cast(object, None))
    mutation_guard: InventoryMutationGuard = cast(InventoryMutationGuard, cast(object, None))

    def _log_container_data_before_validation(
        self, container_data: dict[str, object], container_id: UUID, player_id: UUID
    ) -> None:
        """Debug shape of container_data from persistence before Pydantic validate."""
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

    def _require_container_has_capacity(
        self,
        container: ContainerComponent,
        container_id: UUID,
        player_id: UUID,
        item: InventoryStack,
    ) -> None:
        """Raise ContainerCapacityError when the container has no free slots."""
        if container.has_capacity():
            return
        log_and_raise(
            ContainerCapacityError,
            f"Container capacity exceeded: {container_id}",
            operation="transfer_to_container",
            container_id=str(container_id),
            player_id=str(player_id),
            item_id=item.get("item_id", "unknown"),
            capacity_slots=container.capacity_slots,
            used_slots=container.get_used_slots(),
            details={
                "container_id": str(container_id),
                "capacity_slots": container.capacity_slots,
                "used_slots": container.get_used_slots(),
            },
            user_friendly="Container is full",
        )

    def _audit_transfer_to_container(
        self,
        container: ContainerComponent,
        player: Player,
        container_id: UUID,
        player_id: UUID,
        item: InventoryStack,
    ) -> None:
        """Best-effort audit log for transfer-to-container (must not fail the transfer)."""
        try:
            source_type_value = (
                container.source_type.value if hasattr(container.source_type, "value") else str(container.source_type)
            )
            audit_logger.log_container_interaction(
                player_id=str(player_id),
                player_name=str(player.name),
                container_id=str(container_id),
                event_type="container_transfer",
                source_type=source_type_value,
                room_id=container.room_id,
                direction="to_container",
                item_id=item.get("item_id"),
                item_name=item.get("item_name"),
                success=True,
            )
        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Audit logging errors unpredictable, must not fail container operation
            logger.warning("Failed to log container transfer to audit log", error=str(e))

    def _add_stack_to_container_or_raise(
        self,
        container: ContainerComponent,
        transfer_item: InventoryStack,
        container_id: UUID,
        player_id: UUID,
        item: InventoryStack,
    ) -> list[InventoryStack]:
        """Add a stack via InventoryService; map capacity failures to ContainerCapacityError."""
        try:
            return self.inventory_service.add_stack(container.items, transfer_item)
        except InventoryCapacityError as e:
            log_and_raise(
                ContainerCapacityError,
                f"Container capacity exceeded: {e}",
                operation="transfer_to_container",
                container_id=str(container_id),
                player_id=str(player_id),
                item_id=item.get("item_id", "unknown"),
                details={"container_id": str(container_id), "error": str(e)},
                user_friendly="Container is full",
            )

    async def _require_player_for_transfer(
        self, player_id: UUID, container_id: UUID, item: InventoryStack, operation: str
    ) -> Player:
        """Load player or raise ValidationError for transfer ops."""
        player = await self.persistence.get_player_by_id(player_id)
        if not player:
            log_and_raise(
                ValidationError,
                f"Player not found: {player_id}",
                operation=operation,
                container_id=str(container_id),
                player_id=str(player_id),
                item_id=item.get("item_id", "unknown"),
                details={"player_id": str(player_id)},
                user_friendly="Player not found",
            )
        return player

    async def _require_container_component(
        self, container_id: UUID, player_id: UUID, item: InventoryStack, operation: str
    ) -> ContainerComponent:
        """Load and validate container component for transfer-to."""
        raw_container = await self.persistence.get_container(container_id)
        if not raw_container:
            log_and_raise(
                ContainerNotFoundError,
                f"Container not found: {container_id}",
                operation=operation,
                container_id=str(container_id),
                player_id=str(player_id),
                item_id=item.get("item_id", "unknown"),
                details={"container_id": str(container_id)},
                user_friendly="Container not found",
            )
        if not isinstance(raw_container, dict):
            log_and_raise(
                ContainerServiceError,
                f"Invalid container payload: {container_id}",
                operation=operation,
                container_id=str(container_id),
                player_id=str(player_id),
                item_id=item.get("item_id", "unknown"),
                details={"container_id": str(container_id)},
                user_friendly="Container data is invalid",
            )
        # get_container returns dict[str, Any] | None; after the guards it is always a dict.
        container_data = as_object_dict(raw_container)
        self._log_container_data_before_validation(container_data, container_id, player_id)
        return ContainerComponent.model_validate(filter_container_data(container_data))

    async def _execute_transfer_to_container(
        self,
        container: ContainerComponent,
        player: Player,
        container_id: UUID,
        player_id: UUID,
        mutation_token: str,
        item: InventoryStack,
        quantity: int | None,
    ) -> dict[str, object]:
        """Mutation-guarded body: add stack, persist, audit, return response."""
        async with self.mutation_guard.acquire_async(str(player_id), mutation_token) as decision:
            if not decision.should_apply:
                logger.warning(
                    "Transfer suppressed by mutation guard",
                    container_id=str(container_id),
                    player_id=str(player_id),
                    duplicate=decision.duplicate,
                )
                raise ContainerServiceError("Transfer suppressed by mutation guard")
            transfer_item = item.copy()
            if quantity is not None:
                transfer_item["quantity"] = quantity
            new_container_items = self._add_stack_to_container_or_raise(
                container, transfer_item, container_id, player_id, item
            )
            container.items = new_container_items
            _ = await self.persistence.update_container(
                container_id,
                items_json=items_json_for_persist(new_container_items),
            )
            logger.info(
                "Item transferred to container",
                container_id=str(container_id),
                player_id=str(player_id),
                item_id=item.get("item_id"),
                quantity=transfer_item.get("quantity"),
            )
            self._audit_transfer_to_container(container, player, container_id, player_id, item)
            return {
                "container": container.model_dump(),
                "player_inventory": player_inventory_for_response(player),
            }

    async def transfer_to_container(  # pylint: disable=too-many-arguments,too-many-positional-arguments  # Reason: Public API needs all transfer parameters
        self,
        container_id: UUID,
        player_id: UUID,
        mutation_token: str,
        item: InventoryStack,
        quantity: int | None = None,
    ) -> dict[str, object]:
        """Transfer items from player inventory to container."""
        logger.info(
            "Transferring item to container",
            container_id=str(container_id),
            player_id=str(player_id),
            item_id=item.get("item_id"),
            quantity=quantity,
        )
        self._verify_container_open(container_id, player_id, mutation_token)
        container = await self._require_container_component(container_id, player_id, item, "transfer_to_container")
        self._require_container_has_capacity(container, container_id, player_id, item)
        if container.weight_limit is not None:
            pass  # prototype weights not yet available
        player = await self._require_player_for_transfer(player_id, container_id, item, "transfer_to_container")
        return await self._execute_transfer_to_container(
            container, player, container_id, player_id, mutation_token, item, quantity
        )
