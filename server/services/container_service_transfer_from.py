"""
Container inventory transfer and loot operations.

Mixin host: ContainerService.
"""

from __future__ import annotations

from typing import cast
from uuid import UUID

from ..models.container import ContainerComponent
from ..models.player import Player
from ..structured_logging.enhanced_logging_config import get_logger
from ..utils.audit_logger import audit_logger
from ..utils.error_logging import log_and_raise
from .container_service_helpers import (
    UNKNOWN_STACK,
    ContainerCapacityError,
    ContainerServiceError,
    as_object_dict,
    filter_container_data,
    get_enum_value,
    items_json_for_persist,
    player_inventory_for_response,
)
from .container_service_transfer_to import ContainerTransferToMixin
from .inventory_service import InventoryCapacityError, InventoryStack

logger = get_logger(__name__)


class ContainerTransferFromMixin(ContainerTransferToMixin):
    """Transfer items from containers and loot-all."""

    def _prepare_transfer_item(self, item: InventoryStack, quantity: int | None) -> InventoryStack:
        """Prepare item for transfer, handling quantity and slot_type."""
        transfer_item = item.copy()
        if quantity and quantity < transfer_item.get("quantity", 1):
            transfer_item["quantity"] = quantity

        # Defensive: stack may omit slot_type when data skipped TypedDict validation
        raw_stack = cast(dict[str, object], transfer_item)
        if "slot_type" not in raw_stack:
            metadata_raw = raw_stack.get("metadata")
            metadata = cast(dict[str, object], metadata_raw) if isinstance(metadata_raw, dict) else {}
            transfer_item["slot_type"] = str(metadata.get("slot_type", "backpack"))

        return transfer_item

    def _remove_item_from_container(
        self, container: ContainerComponent, transfer_item_dict: InventoryStack, container_id: UUID, player_id: UUID
    ) -> list[InventoryStack]:
        """Remove item from container items list."""
        logger.debug(
            "Container items before transfer_from_container",
            container_id=str(container_id),
            player_id=str(player_id),
            items_length=len(container.items),
            items_types=[type(stack).__name__ for stack in container.items[:5]],
            items_sample=[str(stack)[:100] for stack in container.items[:3]],
        )

        new_container_items: list[InventoryStack] = []
        item_found = False

        for stack in container.items:
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
                operation="remove_item_from_container",
                container_id=str(container_id),
                item_id=transfer_item_dict.get("item_id"),
                details={"item_id": transfer_item_dict.get("item_id"), "container_id": str(container_id)},
                user_friendly="Item not found in container",
            )

        return new_container_items

    def _add_item_to_player_inventory(  # pylint: disable=too-many-arguments,too-many-positional-arguments  # Reason: Inventory management requires many parameters for context and inventory operations
        self, player: Player, transfer_item_dict: InventoryStack, container_id: UUID, player_id: UUID
    ) -> list[InventoryStack]:
        """Add item to player inventory using InventoryService."""
        player_inventory = player_inventory_for_response(player)

        try:
            inventory_length = len(player_inventory)
        except TypeError:
            inventory_length = None

        logger.debug(
            "Player inventory before add_stack",
            container_id=str(container_id),
            player_id=str(player_id),
            inventory_length=inventory_length,
            inventory_types=[type(stack).__name__ for stack in player_inventory[:5]],
        )

        try:
            return self.inventory_service.add_stack(player_inventory, transfer_item_dict)
        except InventoryCapacityError as e:
            log_and_raise(
                ContainerCapacityError,
                f"Player inventory capacity exceeded: {e}",
                operation="add_item_to_player_inventory",
                container_id=str(container_id),
                player_id=str(player_id),
                item_id=transfer_item_dict.get("item_id", "unknown"),
                details={"player_id": str(player_id), "error": str(e)},
                user_friendly="Your inventory is full",
            )

    async def _persist_and_audit_transfer_from_container(
        self,
        container: ContainerComponent,
        container_id: UUID,
        player: Player,
        item: InventoryStack,
        transfer_item_dict: InventoryStack,
        new_container_items: list[InventoryStack],
        new_player_inventory: list[InventoryStack],
    ) -> dict[str, object]:
        """Persist container changes and log audit trail."""
        container.items = new_container_items

        _ = await self.persistence.update_container(
            container_id,
            items_json=items_json_for_persist(new_container_items),
        )

        logger.info(
            "Item transferred from container",
            container_id=str(container_id),
            player_id=str(player.player_id),
            item_id=item.get("item_id"),
            quantity=transfer_item_dict.get("quantity"),
        )

        try:
            audit_logger.log_container_interaction(
                player_id=str(player.player_id),
                player_name=str(player.name),
                container_id=str(container_id),
                event_type="container_transfer",
                source_type=get_enum_value(container.source_type),
                room_id=container.room_id,
                direction="from_container",
                item_id=item.get("item_id"),
                item_name=item.get("item_name"),
                success=True,
            )
        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Audit logging errors unpredictable, must not fail container operation
            logger.warning("Failed to log container transfer to audit log", error=str(e))

        return {
            "container": container.model_dump(),
            "player_inventory": new_player_inventory,
        }

    async def _execute_transfer_from_container(  # pylint: disable=too-many-arguments,too-many-positional-arguments  # Reason: Mutation-guarded transfer body needs full context
        self,
        container: ContainerComponent,
        player: Player,
        container_id: UUID,
        player_id: UUID,
        mutation_token: str,
        item: InventoryStack,
        quantity: int | None,
    ) -> dict[str, object]:
        """Mutation-guarded body: remove stack, add to player, persist, audit."""
        async with self.mutation_guard.acquire_async(str(player_id), mutation_token) as decision:
            if not decision.should_apply:
                logger.warning(
                    "Transfer suppressed by mutation guard",
                    container_id=str(container_id),
                    player_id=str(player_id),
                    duplicate=decision.duplicate,
                )
                raise ContainerServiceError("Transfer suppressed by mutation guard")
            try:
                transfer_item_dict = self._prepare_transfer_item(item, quantity)
                new_container_items = self._remove_item_from_container(
                    container, transfer_item_dict, container_id, player_id
                )
                new_player_inventory = self._add_item_to_player_inventory(
                    player, transfer_item_dict, container_id, player_id
                )
                return await self._persist_and_audit_transfer_from_container(
                    container, container_id, player, item, transfer_item_dict, new_container_items, new_player_inventory
                )
            except Exception as e:
                logger.error(
                    "Unexpected error during transfer_from_container",
                    container_id=str(container_id),
                    player_id=str(player_id),
                    item_type=type(item).__name__,
                    item_value=str(item),
                    container_items_length=len(container.items),
                    container_items_types=[type(stack).__name__ for stack in container.items[:5]],
                    error=str(e),
                    error_type=type(e).__name__,
                )
                raise

    async def transfer_from_container(  # pylint: disable=too-many-arguments,too-many-positional-arguments  # Reason: Container transfer requires many parameters for context and transfer operations
        self,
        container_id: UUID,
        player_id: UUID,
        mutation_token: str,
        item: InventoryStack,
        quantity: int | None = None,
    ) -> dict[str, object]:
        """Transfer items from container to player inventory."""
        logger.info(
            "Transferring item from container",
            container_id=str(container_id),
            player_id=str(player_id),
            item_id=item.get("item_id"),
            quantity=quantity,
        )
        self._verify_container_open(container_id, player_id, mutation_token)
        container = await self._require_container_component(container_id, player_id, item, "transfer_from_container")
        player = await self._require_player_for_transfer(player_id, container_id, item, "transfer_from_container")
        return await self._execute_transfer_from_container(
            container, player, container_id, player_id, mutation_token, item, quantity
        )

    async def _loot_items_until_full(
        self,
        container: ContainerComponent,
        container_id: UUID,
        player_id: UUID,
        mutation_token: str,
        player_inventory: list[InventoryStack],
    ) -> tuple[ContainerComponent, list[InventoryStack]]:
        """Transfer each container stack until capacity error; returns updated state."""
        for item in container.items:
            try:
                result = await self.transfer_from_container(
                    container_id,
                    player_id,
                    mutation_token,
                    item,
                    item.get("quantity", 1),
                )
                container_payload = result.get("container", {})
                if isinstance(container_payload, dict):
                    container = ContainerComponent.model_validate(
                        filter_container_data(cast(dict[str, object], container_payload))
                    )
                inv_payload = result.get("player_inventory", player_inventory)
                if isinstance(inv_payload, list):
                    player_inventory = cast(list[InventoryStack], inv_payload)
            except ContainerCapacityError:
                logger.warning(
                    "Loot-all stopped due to capacity",
                    container_id=str(container_id),
                    player_id=str(player_id),
                )
                break
            except Exception as e:  # pylint: disable=broad-exception-caught  # Continue processing other items on error  # noqa: B904
                logger.warning(
                    "Error transferring item during loot-all",
                    error=str(e),
                    container_id=str(container_id),
                    player_id=str(player_id),
                )
                continue
        return container, player_inventory

    async def _finalize_loot_all(
        self,
        container: ContainerComponent,
        container_id: UUID,
        player: Player,
        player_id: UUID,
        mutation_token: str,
        player_inventory: list[InventoryStack],
        initial_items_count: int,
    ) -> dict[str, object]:
        """Reload container, audit loot-all, and build response payload."""
        final_raw = await self.persistence.get_container(container_id)
        final_container = (
            ContainerComponent.model_validate(filter_container_data(as_object_dict(final_raw)))
            if final_raw
            else container
        )
        audit_logger.log_container_interaction(
            player_id=str(player_id),
            player_name=str(player.name),
            container_id=str(container_id),
            event_type="container_loot_all",
            source_type=get_enum_value(final_container.source_type),
            room_id=final_container.room_id,
            items_count=initial_items_count,
        )
        return {
            "container": final_container.to_dict(),
            "player_inventory": player_inventory,
            "mutation_token": mutation_token,
        }

    async def loot_all(
        self,
        container_id: UUID,
        player_id: UUID,
        mutation_token: str,
    ) -> dict[str, object]:
        """Loot all eligible items from a container (requires open mutation token)."""
        logger.info(
            "Looting all items from container",
            container_id=str(container_id),
            player_id=str(player_id),
        )
        self._verify_container_open(container_id, player_id, mutation_token)
        container = await self._require_container_component(container_id, player_id, UNKNOWN_STACK, "loot_all")
        initial_items_count = len(container.items)
        player = await self.persistence.get_player_by_id(player_id)
        if not player:
            log_and_raise(
                ContainerServiceError,
                f"Player not found: {player_id}",
                operation="loot_all",
                container_id=str(container_id),
                player_id=str(player_id),
                details={"player_id": str(player_id)},
                user_friendly="Player not found",
            )
        player_inventory = player_inventory_for_response(player)
        container, player_inventory = await self._loot_items_until_full(
            container, container_id, player_id, mutation_token, player_inventory
        )
        return await self._finalize_loot_all(
            container,
            container_id,
            player,
            player_id,
            mutation_token,
            player_inventory,
            initial_items_count,
        )
