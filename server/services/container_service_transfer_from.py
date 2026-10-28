"""
Container inventory transfer and loot operations.

Mixin host: ContainerService. Each operation is one player-registry unit of work; see container_service_transfer_to.
"""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from dataclasses import dataclass
from typing import cast
from uuid import UUID

from ..game.player_registry import PlayerRegistry
from ..models.container import ContainerComponent
from ..structured_logging.enhanced_logging_config import get_logger
from ..utils.audit_logger import ContainerInteractionEvent, audit_logger
from ..utils.error_logging import log_and_raise
from .container_service_helpers import (
    UNKNOWN_STACK,
    ContainerCapacityError,
    ContainerServiceError,
    get_enum_value,
    items_json_for_persist,
)
from .container_service_transfer_to import ContainerTransferToMixin, container_items_write
from .inventory_service import InventoryCapacityError, InventoryStack, InventoryValidationError

logger = get_logger(__name__)


@dataclass(frozen=True)
class LootAllResult:
    """What a loot-all committed: the container and the player's stacks after it, and how many stacks moved."""

    container: ContainerComponent
    player_inventory: list[dict[str, object]]
    player_equipped: dict[str, object]
    items_looted: int


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

    def _add_to_carried(
        self, carried: Sequence[Mapping[str, object]], stack: InventoryStack, container_id: UUID, player_id: UUID
    ) -> list[dict[str, object]]:
        """The player's carried stacks with ``stack`` merged in or appended; ContainerCapacityError when full."""
        try:
            return items_json_for_persist(self.inventory_service.add_stack(carried, stack))
        except InventoryCapacityError as e:
            log_and_raise(
                ContainerCapacityError,
                f"Player inventory capacity exceeded: {e}",
                operation="add_item_to_player_inventory",
                container_id=str(container_id),
                player_id=str(player_id),
                item_id=stack.get("item_id", "unknown"),
                details={"player_id": str(player_id), "error": str(e)},
                user_friendly="Your inventory is full",
            )

    @staticmethod
    def _resolve_container_stack(container: ContainerComponent, item: InventoryStack) -> InventoryStack:
        """
        Replace a caller-supplied stack with the container's own copy of it.

        The GUI identifies the stack by ``{item_id, item_instance_id}`` only, which is what
        .cursor/rules/server-authority.mdc asks for -- the client must not be the source of truth
        for item_name or quantity. Downstream inventory validation needs the full stack, though,
        and used to reject the partial one outright ("Missing required inventory field: item_name",
        surfacing as a 500 on every GUI loot). Resolving against the container we just loaded gives
        the authoritative stack without trusting the caller for anything but the identity.

        Args:
            container: Container component already loaded from persistence.
            item: Caller-supplied stack, possibly only an identifier.

        Returns:
            InventoryStack: The container's own stack when the instance id matches, else ``item``.
        """
        instance_id = item.get("item_instance_id")
        if not instance_id:
            return item
        for stored in container.items:
            if stored.get("item_instance_id") == instance_id:
                return stored
        return item

    async def transfer_from_container(  # pylint: disable=too-many-arguments,too-many-positional-arguments  # Reason: Container transfer requires many parameters for context and transfer operations
        self,
        container_id: UUID,
        player_id: UUID,
        mutation_token: str,
        item: InventoryStack,
        quantity: int | None = None,
        *,
        registry: PlayerRegistry,
    ) -> dict[str, object]:
        """Move a stack (``quantity`` of it, default all, never more than it holds) from the container to the player.

        Returns the container, the player's carried and equipped stacks and the quantity moved, as committed.
        """
        logger.info(
            "Transferring item from container",
            container_id=str(container_id),
            player_id=str(player_id),
            item_id=item.get("item_id"),
            quantity=quantity,
        )
        self._verify_container_open(container_id, player_id, mutation_token)
        async with self._transfer_unit(registry, player_id, container_id, "transfer_from_container") as player:
            container = await self._require_container_component(
                container_id, player_id, item, "transfer_from_container"
            )
            moved = self._prepare_transfer_item(self._resolve_container_stack(container, item), quantity)
            container.items = self._remove_item_from_container(container, moved, container_id, player_id)
            carried = self._add_to_carried(player.inventory.carried, moved, container_id, player_id)
            player.inventory.set_carried(carried)
            registry.write_container(container_id, container_items_write(container_id, container.items))
            player_name = player.row.name
            equipped = dict(player.inventory.equipped)
        logger.info(
            "Item transferred from container",
            container_id=str(container_id),
            player_id=str(player_id),
            item_id=moved.get("item_id"),
            quantity=moved.get("quantity", 1),
        )
        self._audit_transfer(container, container_id, player_id, player_name, moved, "from_container")
        return {
            "container": container.model_dump(),
            "player_inventory": carried,
            "player_equipped": equipped,
            "quantity": moved.get("quantity", 1),
        }

    def _loot_into(
        self, carried: list[dict[str, object]], container: ContainerComponent, container_id: UUID, player_id: UUID
    ) -> tuple[list[dict[str, object]], list[InventoryStack]]:
        """Move each container stack into ``carried`` until the player is full. Returns (carried, stacks left)."""
        left: list[InventoryStack] = []
        for position, stack in enumerate(container.items):
            try:
                carried = self._add_to_carried(carried, stack, container_id, player_id)
            except ContainerCapacityError:
                logger.warning("Loot-all stopped due to capacity", container_id=str(container_id))
                left.extend(container.items[position:])
                break
            except InventoryValidationError as e:
                # A malformed stack stays in the container; the rest still move.
                logger.warning("Loot-all skipped an invalid stack", container_id=str(container_id), error=str(e))
                left.append(stack)
        return carried, left

    async def loot_all(
        self, container_id: UUID, player_id: UUID, mutation_token: str, *, registry: PlayerRegistry
    ) -> LootAllResult:
        """Move every stack the player can carry out of the container, as one unit of work (stops when full)."""
        logger.info("Looting all items from container", container_id=str(container_id), player_id=str(player_id))
        self._verify_container_open(container_id, player_id, mutation_token)
        async with self._transfer_unit(registry, player_id, container_id, "loot_all") as player:
            container = await self._require_container_component(container_id, player_id, UNKNOWN_STACK, "loot_all")
            carried, left = self._loot_into(
                [dict(stack) for stack in player.inventory.carried], container, container_id, player_id
            )
            looted = len(container.items) - len(left)
            if looted:
                container.items = left
                player.inventory.set_carried(carried)
                registry.write_container(container_id, container_items_write(container_id, container.items))
            player_name = player.row.name
            equipped = dict(player.inventory.equipped)
        audit_logger.log_container_interaction(
            ContainerInteractionEvent(
                player_id=str(player_id),
                player_name=player_name,
                container_id=str(container_id),
                event_type="container_loot_all",
                source_type=get_enum_value(container.source_type),
                room_id=container.room_id,
                items_count=looted,
                success=True,
            )
        )
        return LootAllResult(
            container=container,
            player_inventory=[dict(stack) for stack in carried],
            player_equipped=equipped,
            items_looted=looted,
        )
