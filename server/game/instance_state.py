"""
What a player carries that belongs only to an instance, and how to clear it.

Two kinds of player state are tied to one instance and must not outlive it:

* items flagged INSTANCE_BOUND (see game.items.instance_bound), in the inventory, equipped, or inside a
  carried container;
* status effects marked ``"instance_scoped": true`` (player_effects rows, cleared by
  ``effect_store.clear_instance_scoped_effects``).

When a player's instance has been lost (logout, restart) and they are given a fresh one, whatever
the old one handed them is cleared so the new run starts clean.
"""

from __future__ import annotations

import uuid
from collections.abc import Iterable, Mapping
from typing import TYPE_CHECKING, NamedTuple, Protocol, cast

from ..constants.lucidity import STARTING_LCD
from ..structured_logging.enhanced_logging_config import get_logger
from .items.instance_bound import strip_instance_bound_stacks

if TYPE_CHECKING:
    from ..models.player import Player
    from .player_registry import PlayerRegistry

logger = get_logger(__name__)


class StrippedInventory(NamedTuple):
    """How many instance-bound items a strip removed, and the inventory it committed."""

    removed: int
    carried: list[dict[str, object]]
    equipped: dict[str, object]


async def strip_instance_bound_items(registry: PlayerRegistry, player_id: uuid.UUID) -> StrippedInventory:
    """Remove INSTANCE_BOUND items from the player's live inventory and equipment, as one registry unit (ADR-029
    step 4c-i); returns how many were removed and the inventory now committed.

    Instance-scoped effects are separate (``clear_instance_scoped_effects``).
    """
    async with registry.mutate(player_id) as player:
        carried, removed = strip_instance_bound_stacks([dict(stack) for stack in player.inventory.carried])
        equipped: dict[str, object] = {}
        for slot, stack in player.inventory.equipped.items():
            if not isinstance(stack, Mapping):
                equipped[slot] = stack
                continue
            kept, slot_removed = strip_instance_bound_stacks([dict(cast(Mapping[str, object], stack))])
            removed += slot_removed
            if kept:
                equipped[slot] = kept[0]
        if removed:
            player.inventory.replace(carried, equipped)
    return StrippedInventory(removed, carried, equipped)


async def clear_lost_instance_items(registry: PlayerRegistry | None, player: Player) -> None:
    """A restarted run does not keep what the lost instance handed the player: strip it (after the caller's save),
    then mirror the committed inventory onto ``player``, the connection's own copy. Logged, never raised."""
    if registry is None:
        logger.warning("Run restart: no player registry, instance-bound items kept", player_id=player.player_id)
        return
    try:
        stripped = await strip_instance_bound_items(registry, uuid.UUID(str(player.player_id)))
    except Exception as e:  # pylint: disable=broad-exception-caught  # Reason: as restart_instance_run, a failed reset must not block the reconnect
        logger.error("Run restart: instance-bound item strip failed", player_id=player.player_id, error=str(e))
        return
    if stripped.removed:
        player.set_inventory(stripped.carried)
        player.set_equipped_items(
            {
                slot: cast(dict[str, object], stack)
                for slot, stack in stripped.equipped.items()
                if isinstance(stack, dict)
            }
        )
    logger.info("Run restart: instance-bound items removed", player_id=player.player_id, removed=stripped.removed)


class QuestResetter(Protocol):  # pylint: disable=too-few-public-methods  # Reason: Protocol stub
    """The slice of QuestService a run restart drives."""

    async def reset_offered_quests(self, player_id: uuid.UUID, room_ids: Iterable[str]) -> list[str]:
        """Put the quests these rooms offer (and what they unlock) back to not started."""
        ...  # pylint: disable=unnecessary-ellipsis  # Reason: basedpyright requires an explicit stub body for a non-None Protocol return type


async def _reset_lucidity(player_id: uuid.UUID) -> None:
    """Set the player's lucidity back to what a new character starts with."""
    # Imported here: the database module pulls in the app's engine setup, which this module must not need to import.
    from ..database import get_async_session
    from ..services.lucidity_repository import LucidityRepository
    from ..services.lucidity_service import resolve_tier

    async for session in get_async_session():
        lucidity = await LucidityRepository(session).get_or_create_player_lucidity(player_id)
        lucidity.current_lcd = STARTING_LCD
        lucidity.current_tier = resolve_tier(STARTING_LCD)
        await session.commit()


async def restart_instance_run(player: Player, stable_room_ids: Iterable[str], quests: QuestResetter | None) -> None:
    """Start the player's run over: full DP, starting lucidity, and the instance's quests back to not started.

    The instance-bound items (``strip_instance_bound_items``) and effects are separate. Corruption is a floor that survives a
    restart, so it is untouched. Each step is isolated: a failure is logged and never blocks the reconnect.
    """
    _ = player.restore_to_full_health()
    player_id = uuid.UUID(str(player.player_id))
    try:
        await _reset_lucidity(player_id)
    except Exception as e:  # pylint: disable=broad-exception-caught  # Reason: a failed reset must not block the reconnect
        logger.error("Run restart: lucidity reset failed", player_id=str(player_id), error=str(e))
    if quests is None:
        return
    try:
        _ = await quests.reset_offered_quests(player_id, stable_room_ids)
    except Exception as e:  # pylint: disable=broad-exception-caught  # Reason: as above
        logger.error("Run restart: quest reset failed", player_id=str(player_id), error=str(e))
