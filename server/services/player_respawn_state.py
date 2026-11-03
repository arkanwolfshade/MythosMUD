"""
Player-state and logging helpers for PlayerRespawnService.

Split out of player_respawn_service.py (file size): changes to the player aggregate the respawn holds in its registry
unit (ADR-029 step 6a) -- death-room bookkeeping and the respawn state changes, all sync -- and respawn logging.
"""

from __future__ import annotations

import uuid
from typing import TYPE_CHECKING

from ..constants.spawn_defaults import LIMBO_ROOM_ID
from ..models.game import PositionState
from ..models.player_dp import DpChange, restored
from ..structured_logging.enhanced_logging_config import get_logger
from .player_health_service import PlayerHealthService

if TYPE_CHECKING:
    from ..game.player_registry import PlayerAggregate

logger = get_logger(__name__)

# Stats key for room id where the player last died (survives limbo move for login UI).
DEATH_ROOM_ID_STAT = "death_room_id"
DEATH_LOCATION_STAT = "death_location"


def record_death_room(player: PlayerAggregate, death_location: str) -> None:
    """Keep the pre-limbo death room on the player's stats, for the death interstitial and login."""
    if not death_location or death_location in (LIMBO_ROOM_ID, "catatonia_failover"):
        return
    # Display name is filled by the death service; never store the raw id there (#910).
    # Login re-resolves the name from death_room_id when it is missing.
    player.row.set_stat(DEATH_ROOM_ID_STAT, death_location, sync=True)


def clear_death_room(player: PlayerAggregate) -> None:
    """Forget the death room once the player has respawned."""
    player.row.remove_stat(DEATH_ROOM_ID_STAT, sync=True)
    player.row.remove_stat(DEATH_LOCATION_STAT, sync=True)


def apply_standard_respawn_state(player: PlayerAggregate, respawn_room: str) -> tuple[DpChange, str]:
    """Restore full health and move the player to ``respawn_room``; return the DP change and the room they left."""
    change = PlayerHealthService.apply_in(player, restored(player.row.stats))
    old_room = player.row.current_room_id
    player.row.set_current_room_id(respawn_room, sync=True)
    clear_death_room(player)
    return change, old_room


def apply_sanitarium_player_state(player: PlayerAggregate, respawn_room: str) -> str:
    """Stand the player up in ``respawn_room``; return the room they left."""
    player.row.set_stat("position", PositionState.STANDING, sync=True)
    old_room = player.row.current_room_id
    player.row.set_current_room_id(respawn_room, sync=True)
    clear_death_room(player)
    return old_room


def log_standard_respawn(
    player_name: str, player_id: uuid.UUID, respawn_room: str, change: DpChange, old_room: str
) -> None:
    """Log standard respawn details."""
    logger.info(
        "Player respawned",
        player_id=player_id,
        player_name=player_name,
        respawn_room=respawn_room,
        old_dp=change.old_dp,
        new_dp=change.new_dp,
        max_dp=change.max_dp,
        from_limbo=old_room == LIMBO_ROOM_ID,
    )


def log_lucidity_respawn(  # pylint: disable=too-many-arguments  # Reason: one log line's fields
    kind: str,
    player_name: str,
    player_id: uuid.UUID,
    respawn_room: str,
    lucidity: tuple[int, int],
    old_room: str,
) -> None:
    """Log a delirium or sanitarium respawn (``kind``); ``lucidity`` is (old, new)."""
    logger.info(
        "Player respawned from delirium" if kind == "delirium" else "Player respawned from sanitarium",
        player_id=player_id,
        player_name=player_name,
        respawn_room=respawn_room,
        old_lucidity=lucidity[0],
        new_lucidity=lucidity[1],
        from_room=old_room,
    )
