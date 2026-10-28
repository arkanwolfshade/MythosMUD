"""
Player-state and logging helpers for PlayerRespawnService.

Split out of player_respawn_service.py (file size): pure functions of the Player they are given --
death-room bookkeeping, DP normalisation, the respawn state changes, and respawn logging.
"""

from __future__ import annotations

import uuid

from ..constants.spawn_defaults import LIMBO_ROOM_ID
from ..models.game import PositionState
from ..models.player import Player
from ..structured_logging.enhanced_logging_config import get_logger
from ..utils.int_coercion import coerce_int

logger = get_logger(__name__)

# Stats key for room id where the player last died (survives limbo move for login UI).
DEATH_ROOM_ID_STAT = "death_room_id"
DEATH_LOCATION_STAT = "death_location"


def normalize_current_dp(stats: dict[str, object]) -> int:
    """Return current_dp as an int, defaulting to 0 for non-numeric values."""
    current_dp = stats.get("current_dp", 0)
    if isinstance(current_dp, int | float):
        return int(current_dp)
    return 0


def record_death_room_on_player(player: Player, death_location: str) -> None:
    """Persist pre-limbo death room on player stats for death interstitial / login."""
    if not death_location or death_location in (LIMBO_ROOM_ID, "catatonia_failover"):
        return
    stats = player.get_stats()
    # Display name is filled by the death service; never store the raw id there (#910).
    # Login re-resolves the name from death_room_id when it is missing.
    stats[DEATH_ROOM_ID_STAT] = death_location
    player.set_stats(stats)


def clear_death_room_on_player(player: Player) -> None:
    """Clear persisted death room after successful respawn."""
    stats = player.get_stats()
    _ = stats.pop(DEATH_ROOM_ID_STAT, None)
    _ = stats.pop(DEATH_LOCATION_STAT, None)
    player.set_stats(stats)


def apply_standard_respawn_state(player: Player, respawn_room: str) -> tuple[int, int, str]:
    """Restore full health and move player to respawn_room; return (old_dp, max_dp, old_room)."""
    old_dp = player.restore_to_full_health()
    stats = player.get_stats()
    max_dp = coerce_int(stats.get("max_dp", 100), default=100)
    old_room = player.current_room_id
    player.current_room_id = respawn_room
    clear_death_room_on_player(player)
    return old_dp, max_dp, old_room


def log_standard_respawn(
    player: Player, player_id: uuid.UUID, respawn_room: str, old_dp: int, max_dp: int, old_room: str
) -> None:
    """Log standard respawn details."""
    logger.info(
        "Player respawned",
        player_id=player_id,
        player_name=player.name,
        respawn_room=respawn_room,
        old_dp=old_dp,
        new_dp=max_dp,
        max_dp=max_dp,
        from_limbo=old_room == LIMBO_ROOM_ID,
    )


def apply_sanitarium_player_state(player: Player, respawn_room: str) -> tuple[dict[str, object], str]:
    """Set posture to standing and move player to respawn room; return (stats, old_room)."""
    stats = player.get_stats()
    stats["position"] = PositionState.STANDING
    player.set_stats(stats)
    old_room = player.current_room_id
    player.current_room_id = respawn_room
    clear_death_room_on_player(player)
    return player.get_stats(), old_room


def log_sanitarium_respawn(
    player: Player, player_id: uuid.UUID, respawn_room: str, old_lucidity: int, new_lucidity: int, old_room: str
) -> None:
    """Log sanitarium respawn details."""
    logger.info(
        "Player respawned from sanitarium",
        player_id=player_id,
        player_name=player.name,
        respawn_room=respawn_room,
        old_lucidity=old_lucidity,
        new_lucidity=new_lucidity,
        from_room=old_room,
    )


def log_delirium_respawn(
    player: Player, player_id: uuid.UUID, respawn_room: str, old_lucidity: int, new_lucidity: int, old_room: str
) -> None:
    """Log delirium respawn details."""
    logger.info(
        "Player respawned from delirium",
        player_id=player_id,
        player_name=player.name,
        respawn_room=respawn_room,
        old_lucidity=old_lucidity,
        new_lucidity=new_lucidity,
        from_room=old_room,
    )
