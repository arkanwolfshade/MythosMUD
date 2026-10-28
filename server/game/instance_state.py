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
from collections.abc import Iterable
from typing import TYPE_CHECKING, Protocol, cast

from ..constants.lucidity import STARTING_LCD
from ..structured_logging.enhanced_logging_config import get_logger
from .items.instance_bound import strip_instance_bound_stacks

if TYPE_CHECKING:
    from ..models.player import Player

logger = get_logger(__name__)


def strip_instance_bound_items(player: Player) -> int:
    """Remove INSTANCE_BOUND items from the player's inventory and equipment; returns how many were removed."""
    inventory, inventory_removed = strip_instance_bound_stacks(player.get_inventory())
    equipped = player.get_equipped_items()
    slots = [(slot, cast(dict[str, object], stack)) for slot, stack in equipped.items() if isinstance(stack, dict)]
    kept_equipped: dict[str, dict[str, object]] = {}
    equipped_removed = 0
    for slot, stack in slots:
        kept, removed = strip_instance_bound_stacks([stack])
        equipped_removed += removed
        if kept:
            kept_equipped[slot] = kept[0]
    if inventory_removed:
        player.set_inventory(inventory)
    if equipped_removed:
        player.set_equipped_items(kept_equipped)
    return inventory_removed + equipped_removed


def reset_instance_scoped_state(player: Player) -> int:
    """Clear the instance-bound items the player's old instance handed them; returns how many were removed.

    Instance-scoped effects are player_effects rows, cleared by ``effect_store.clear_instance_scoped_effects``
    (async), which every caller of this also awaits.
    """
    return strip_instance_bound_items(player)


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

    The rest of ``reset_instance_scoped_state`` (items, effects) is separate. Corruption is a floor that survives a
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
