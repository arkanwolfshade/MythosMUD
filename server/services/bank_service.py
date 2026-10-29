"""
Player bank deposit boxes (#977).

Each player has at most one box: a "bank" container owned by them (owner_id = player id, no room),
created the first time it is needed. A box holds BANK_BOX_CAPACITY slots. The bank commands refuse a
deposit into a full box, but items forwarded from a flushed instance are always accepted, so the box
can end up over capacity until the player withdraws something: a loss is never made worse by a full box.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Protocol, cast
from uuid import UUID

from ..constants.containers import BANK_SOURCE_TYPE
from ..exceptions import DatabaseError
from ..models.room import Room
from ..persistence.container_create_params import ContainerCreateParams
from ..persistence.container_persistence_async import write_container_items_async
from ..structured_logging.enhanced_logging_config import get_logger

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession

    from ..game.player_registry import DbSession, PlayerRegistry

logger = get_logger(__name__)

BANK_BOX_CAPACITY = 100


class BankBoxPersistence(Protocol):
    """The slice of AsyncPersistenceLayer the deposit boxes need."""

    async def get_bank_container(self, owner_id: UUID) -> dict[str, object] | None:
        """The owner's bank box, or None if they have never opened one."""
        ...  # pylint: disable=unnecessary-ellipsis  # Reason: basedpyright needs a stub body for a non-None return

    async def create_container(
        self, source_type: str, params: ContainerCreateParams | None = None
    ) -> dict[str, object]:
        """Create a container row."""
        ...  # pylint: disable=unnecessary-ellipsis  # Reason: basedpyright needs a stub body for a non-None return


def is_bank_room(room: Room | None) -> bool:
    """True if room is a bank. attributes is untyped JSONB: only a literal true counts."""
    return room is not None and cast(object, room.attributes.get("bank")) is True


async def get_or_create_bank_box(persistence: BankBoxPersistence, owner_id: UUID) -> dict[str, object]:
    """Return the player's deposit box, creating it on first use."""
    box = await persistence.get_bank_container(owner_id)
    if box is not None:
        return box
    try:
        return await persistence.create_container(
            BANK_SOURCE_TYPE,
            ContainerCreateParams(
                owner_id=owner_id,
                capacity_slots=BANK_BOX_CAPACITY,
                metadata_json={"name": "deposit box"},
            ),
        )
    except DatabaseError:
        # Lost a create race (uq_containers_bank_owner): the winner's box is the one to use.
        box = await persistence.get_bank_container(owner_id)
        if box is None:
            raise
        return box


async def forward_to_bank_box(
    persistence: BankBoxPersistence, registry: PlayerRegistry, owner_id: UUID, stacks: list[dict[str, object]]
) -> None:
    """Append stacks to the owner's box (created if needed). Never evicts or refuses: may exceed capacity.

    Runs under the box's container lock, as deposits and withdrawals do (ADR-029), so neither can be overwritten.
    The box is read again under the lock: the copy read to find it may already be stale.
    """
    box_id = UUID(str((await get_or_create_bank_box(persistence, owner_id))["container_id"]))
    async with registry.mutate_many([], containers=[box_id]):  # pylint: disable=contextmanager-generator-missing-cleanup  # Reason: @asynccontextmanager always drives this generator to completion; pylint cannot see through the wrapper
        box = await persistence.get_bank_container(owner_id)
        held = box.get("items_json") if box is not None else None
        items = [*(cast(list[dict[str, object]], held) if isinstance(held, list) else []), *stacks]

        async def write(session: DbSession) -> None:
            # The registry's sessions come from server.database.get_session_maker(); DbSession is their typed slice.
            await write_container_items_async(cast("AsyncSession", cast(object, session)), box_id, items)

        registry.write_container(box_id, write)
