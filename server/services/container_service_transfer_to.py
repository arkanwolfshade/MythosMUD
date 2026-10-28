"""
Container inventory transfer and loot operations.

Mixin host: ContainerService.

A transfer is one player-registry unit of work (ADR-029 step 4b): it holds the player's lock and then the container's,
reads the container fresh and the player's live inventory, changes both, and commits both in one transaction before it
returns. A failure anywhere leaves both as they were.
"""

from __future__ import annotations

from collections.abc import AsyncGenerator, Mapping, Sequence
from contextlib import asynccontextmanager
from typing import cast
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from ..async_persistence import AsyncPersistenceLayer
from ..exceptions import ActionRejectedError, ValidationError
from ..game.player_registry import DbSession, PartWrite, PlayerAggregate, PlayerNotFoundError, PlayerRegistry
from ..models.container import ContainerComponent
from ..persistence.container_persistence_async import write_container_items_async
from ..structured_logging.enhanced_logging_config import get_logger
from ..utils.audit_logger import ContainerInteractionEvent, audit_logger
from ..utils.error_logging import log_and_raise
from .container_service_access import ContainerAccessMixin
from .container_service_helpers import (
    ContainerCapacityError,
    ContainerNotFoundError,
    ContainerServiceError,
    as_object_dict,
    filter_container_data,
    get_enum_value,
    items_json_for_persist,
)
from .inventory_service import InventoryCapacityError, InventoryService, InventoryStack

logger = get_logger(__name__)


def container_items_write(container_id: UUID, items: Sequence[InventoryStack]) -> PartWrite:
    """The container's new contents, as a write the transfer's unit of work applies in its own transaction."""
    rows = [dict(row) for row in items_json_for_persist(list(items))]

    async def write(session: DbSession) -> None:
        # The registry's sessions come from server.database.get_session_maker(); DbSession is their typed slice.
        await write_container_items_async(cast(AsyncSession, cast(object, session)), container_id, rows)

    return write


def _stack_quantity(stack: Mapping[str, object]) -> int:
    raw = stack.get("quantity", 1)
    return raw if isinstance(raw, int) and not isinstance(raw, bool) else 1


def take_carried_stack(
    carried: Sequence[Mapping[str, object]], item: InventoryStack, quantity: int | None
) -> tuple[list[dict[str, object]], InventoryStack]:
    """Split ``quantity`` (default: all of it, never more than is held) off the player's own copy of ``item``.

    ``item`` only names the stack (its instance id, else its item id): what moves comes from what the player holds.
    Returns the carried stacks left and the stack to move. Raises ValidationError if the player does not carry it.
    """
    if quantity is not None and quantity <= 0:
        log_and_raise(ActionRejectedError, "Quantity must be a positive number.", operation="take_carried_stack")
    instance_id = item.get("item_instance_id")
    key, wanted = ("item_instance_id", instance_id) if instance_id else ("item_id", item.get("item_id"))
    for index, stack in enumerate(carried):
        if stack.get(key) != wanted:
            continue
        held = _stack_quantity(stack)
        moved = held if quantity is None else min(quantity, held)
        left = [dict(other) for other in carried]
        if moved == held:
            del left[index]
        else:
            left[index]["quantity"] = held - moved
        return left, cast(InventoryStack, cast(object, {**stack, "quantity": moved}))
    log_and_raise(
        ActionRejectedError,
        "You don't have that item.",
        operation="take_carried_stack",
        item_id=item.get("item_id", "unknown"),
        user_friendly="You don't have that item.",
    )


class ContainerTransferToMixin(ContainerAccessMixin):  # pylint: disable=too-few-public-methods  # Reason: mixin host for ContainerService transfer-in API
    """Transfer items into containers."""

    # Host ContainerService rebinds these fields on instances.
    # cast(object, None) only satisfies basedpyright reportUninitializedInstanceVariable.
    inventory_service: InventoryService = cast(InventoryService, cast(object, None))
    persistence: AsyncPersistenceLayer = cast(AsyncPersistenceLayer, cast(object, None))

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

    def _audit_transfer(  # pylint: disable=too-many-arguments,too-many-positional-arguments  # Reason: one audit row needs every one of these
        self,
        container: ContainerComponent,
        container_id: UUID,
        player_id: UUID,
        player_name: str,
        item: InventoryStack,
        direction: str,
    ) -> None:
        """Best-effort audit log for a committed transfer (must not fail it)."""
        try:
            audit_logger.log_container_interaction(
                ContainerInteractionEvent(
                    player_id=str(player_id),
                    player_name=player_name,
                    container_id=str(container_id),
                    event_type="container_transfer",
                    source_type=get_enum_value(container.source_type),
                    room_id=container.room_id,
                    direction=direction,
                    item_id=item.get("item_id"),
                    item_name=item.get("item_name"),
                    success=True,
                )
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

    @asynccontextmanager
    async def _transfer_unit(
        self, registry: PlayerRegistry, player_id: UUID, container_id: UUID, operation: str
    ) -> AsyncGenerator[PlayerAggregate]:
        """The player's unit of work, also holding the container (its lock, and the right to write it)."""
        try:
            async with registry.mutate(player_id, containers=[container_id]) as player:  # pylint: disable=contextmanager-generator-missing-cleanup  # Reason: @asynccontextmanager always drives this generator to completion; pylint cannot see through the wrapper
                yield player
        except PlayerNotFoundError:
            log_and_raise(
                ValidationError,
                f"Player not found: {player_id}",
                operation=operation,
                container_id=str(container_id),
                player_id=str(player_id),
                details={"player_id": str(player_id)},
                user_friendly="Player not found",
            )

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

    async def transfer_to_container(  # pylint: disable=too-many-arguments,too-many-positional-arguments  # Reason: Public API needs all transfer parameters
        self,
        container_id: UUID,
        player_id: UUID,
        mutation_token: str,
        item: InventoryStack,
        quantity: int | None = None,
        *,
        registry: PlayerRegistry,
    ) -> dict[str, object]:
        """Move a stack from the player's inventory into the container.

        ``item`` names the stack; ``quantity`` of the player's own copy moves (default: all, never more than held).
        Returns the container, the player's carried and equipped stacks and the quantity moved, as committed.
        """
        logger.info(
            "Transferring item to container",
            container_id=str(container_id),
            player_id=str(player_id),
            item_id=item.get("item_id"),
            quantity=quantity,
        )
        self._verify_container_open(container_id, player_id, mutation_token)
        async with self._transfer_unit(registry, player_id, container_id, "transfer_to_container") as player:
            container = await self._require_container_component(container_id, player_id, item, "transfer_to_container")
            self._require_container_has_capacity(container, container_id, player_id, item)
            carried, moved = take_carried_stack(player.inventory.carried, item, quantity)
            container.items = self._add_stack_to_container_or_raise(container, moved, container_id, player_id, item)
            player.inventory.set_carried(carried)
            registry.write_container(container_id, container_items_write(container_id, container.items))
            player_name = player.row.name
            equipped = dict(player.inventory.equipped)
        logger.info(
            "Item transferred to container",
            container_id=str(container_id),
            player_id=str(player_id),
            item_id=item.get("item_id"),
            quantity=moved["quantity"],
        )
        self._audit_transfer(container, container_id, player_id, player_name, moved, "to_container")
        return {
            "container": container.model_dump(),
            "player_inventory": carried,
            "player_equipped": equipped,
            "quantity": moved["quantity"],
        }
