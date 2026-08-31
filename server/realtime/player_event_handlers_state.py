"""
Player state update event handlers.

This module handles player state updates (XP, DP, death, decay).
"""

from __future__ import annotations

import uuid
from collections.abc import Mapping
from typing import Protocol, runtime_checkable

from sqlalchemy.exc import SQLAlchemyError
from structlog.stdlib import BoundLogger

from ..events.event_types import PlayerDiedEvent, PlayerDPDecayEvent, PlayerDPUpdated
from ..models.player import Player
from ..services.player_combat_service import PlayerXPAwardEvent
from .connection_manager import ConnectionManager
from .envelope import build_event
from .player_event_handlers_utils import PlayerEventHandlerUtils
from .posture_notify import emit_posture_change, normalize_posture


@runtime_checkable
class _StatsPlayer(Protocol):  # pylint: disable=too-few-public-methods  # Reason: Protocol stub
    """Minimal player surface for reading posture from stats."""

    def get_stats(self) -> Mapping[str, object]: ...  # pylint: disable=missing-function-docstring  # Reason: Protocol stub


def _dp_posture_from_stats(stats: Mapping[str, object], new_dp: int) -> str:
    """Derive posture string for DP update payloads (standing / lying / from stats)."""
    if new_dp <= 0:
        return "lying"
    position = stats.get("position")
    if position is None:
        return "standing"
    if hasattr(position, "value"):
        return str(getattr(position, "value", str(position)))
    return str(position)


def _player_snapshot_for_dp(
    player: Player | None,
    event: PlayerDPUpdated,
    logger: BoundLogger,
) -> tuple[dict[str, object], str, str | None]:
    """Load stats and display fields for a DP update, or fall back when player is offline."""
    player_id_str = str(event.player_id)
    if player is None:
        logger.debug(
            "Player not in connection manager for DP update, using event data only",
            player_id=player_id_str,
        )
        return {}, "Unknown", None
    if not hasattr(player, "get_stats"):
        return {}, player.name, getattr(player, "current_room_id", None)
    stats_raw = player.get_stats()
    stats_dict = dict(stats_raw)
    return stats_dict, player.name, getattr(player, "current_room_id", None)


def _dp_player_update_payload(
    event: PlayerDPUpdated,
    player_id_str: str,
    stats: dict[str, object],
    player_name: str,
    current_room_id: str | None,
    posture: str,
) -> dict[str, object]:
    """Assemble the nested player object for a DP update WebSocket message."""
    merged_stats: dict[str, object] = {
        **stats,
        "current_dp": event.new_dp,
        "max_dp": event.max_dp,
        "position": posture,
    }
    return {
        "player_id": player_id_str,
        "name": player_name,
        "dp": event.new_dp,
        "max_dp": event.max_dp,
        "current_room_id": current_room_id,
        "stats": merged_stats,
    }


async def _attach_dp_updated_posture_fields(
    connection_manager: ConnectionManager,
    *,
    player_id: uuid.UUID | str,
    player_name: str,
    current_room_id: str | None,
    previous_position: str,
    posture: str,
    payload: dict[str, object],
) -> None:
    """Emit posture change and attach self-facing message fields when present."""
    posture_message = await emit_posture_change(
        connection_manager,
        player_id=player_id,
        display_name=player_name,
        room_id=current_room_id,
        previous_position=previous_position,
        new_position=posture,
        include_self_message=True,
        send_personal_update=False,
    )
    if posture_message:
        payload["posture_message"] = posture_message
        payload["previous_position"] = previous_position


async def _dispatch_player_dp_updated_payload(
    connection_manager: ConnectionManager,
    logger: BoundLogger,
    event: PlayerDPUpdated,
) -> None:
    """Build and send the player_dp_updated WebSocket payload."""
    player_id = event.player_id
    player_id_str = str(player_id)
    logger.info(
        "Received PlayerDPUpdated event",
        player_id=player_id_str,
        old_dp=event.old_dp,
        new_dp=event.new_dp,
        max_dp=event.max_dp,
        damage_taken=event.damage_taken,
    )
    player = await connection_manager.get_player(player_id)
    stats, player_name, current_room_id = _player_snapshot_for_dp(player, event, logger)
    previous_position = normalize_posture(stats.get("position"))
    posture = _dp_posture_from_stats(stats, event.new_dp)
    player_update_data = _dp_player_update_payload(event, player_id_str, stats, player_name, current_room_id, posture)
    payload: dict[str, object] = {
        "old_dp": event.old_dp,
        "new_dp": event.new_dp,
        "max_dp": event.max_dp,
        "damage_taken": event.damage_taken,
        "posture": posture,
        "player": player_update_data,
    }
    await _attach_dp_updated_posture_fields(
        connection_manager,
        player_id=player_id,
        player_name=player_name,
        current_room_id=current_room_id,
        previous_position=previous_position,
        posture=posture,
        payload=payload,
    )
    dp_update_event = build_event("player_dp_updated", payload, player_id=player_id_str)
    _ = await connection_manager.send_personal_message(player_id, dp_update_event)
    logger.info(
        "Sent DP update to player",
        player_id=player_id_str,
        old_dp=event.old_dp,
        new_dp=event.new_dp,
        damage_taken=event.damage_taken,
    )


async def _send_player_death_notification(
    connection_manager: ConnectionManager,
    logger: BoundLogger,
    event: PlayerDiedEvent,
) -> None:
    """Send player_died envelope to the deceased player's WebSocket session."""
    player_id_str = str(event.player_id)
    death_location_value = event.death_location or event.room_id
    death_event = build_event(
        "player_died",
        {
            "player_id": player_id_str,
            "player_name": event.player_name,
            "death_location": death_location_value,
            "current_dp": -10,
            "killer_id": event.killer_id,
            "killer_name": event.killer_name,
            "message": "You have died. The darkness claims you utterly.",
        },
        player_id=player_id_str,
    )
    delivery_status = await connection_manager.send_personal_message(event.player_id, death_event)
    logger.info(
        "Sent death notification to player",
        player_id=player_id_str,
        room_id=event.room_id,
        delivery_status=delivery_status,
    )


def _decay_previous_position_before_lying(player: object | None) -> str:
    """Prefer sitting when stats still show it; otherwise assume standing before collapse."""
    if not isinstance(player, _StatsPlayer):
        return "standing"
    stats_position = normalize_posture(player.get_stats().get("position"))
    return "sitting" if stats_position == "sitting" else "standing"


async def _maybe_attach_decay_posture_cross(
    connection_manager: ConnectionManager,
    event: PlayerDPDecayEvent,
    *,
    player: object | None,
    player_name: str,
    room_id: object | None,
    decay_payload: dict[str, object],
) -> None:
    """When DP crosses to <=0, emit lying posture and attach message fields."""
    if not event.new_dp <= 0 < event.old_dp:
        return
    previous_position = _decay_previous_position_before_lying(player)
    posture_message = await emit_posture_change(
        connection_manager,
        player_id=event.player_id,
        display_name=player_name,
        room_id=str(room_id) if room_id else None,
        previous_position=previous_position,
        new_position="lying",
        include_self_message=True,
        send_personal_update=False,
    )
    if posture_message:
        decay_payload["posture_message"] = posture_message
        decay_payload["previous_position"] = previous_position


async def _dispatch_player_dp_decay_payload(
    connection_manager: ConnectionManager,
    logger: BoundLogger,
    event: PlayerDPDecayEvent,
) -> None:
    """Build and send the player_dp_decay WebSocket payload."""
    player_id_str = str(event.player_id)
    player = await connection_manager.get_player(event.player_id)
    player_name = "Unknown"
    room_id = event.room_id
    if player is not None:
        player_name = player.name
        room_id = room_id or getattr(player, "current_room_id", None)

    decay_payload: dict[str, object] = {
        "player_id": player_id_str,
        "old_dp": event.old_dp,
        "new_dp": event.new_dp,
        "decay_amount": event.decay_amount,
        "room_id": event.room_id,
    }
    await _maybe_attach_decay_posture_cross(
        connection_manager,
        event,
        player=player,
        player_name=player_name,
        room_id=room_id,
        decay_payload=decay_payload,
    )
    decay_event = build_event(
        "player_dp_decay",
        decay_payload,
        player_id=player_id_str,
    )
    _ = await connection_manager.send_personal_message(event.player_id, decay_event)
    logger.debug("Sent DP decay notification to player", player_id=player_id_str, new_dp=event.new_dp)


class PlayerStateEventHandler:
    """Handles player state update events (XP, DP, death, decay)."""

    connection_manager: ConnectionManager | None
    utils: PlayerEventHandlerUtils
    _logger: BoundLogger

    def __init__(
        self,
        connection_manager: ConnectionManager | None,
        utils: PlayerEventHandlerUtils,
        logger: BoundLogger,
    ) -> None:
        """
        Initialize state event handler.

        Args:
            connection_manager: ConnectionManager instance
            utils: PlayerEventHandlerUtils instance
            logger: Logger instance
        """
        self.connection_manager = connection_manager
        self.utils = utils
        self._logger = logger

    async def handle_player_xp_awarded(self, event: PlayerXPAwardEvent) -> None:
        """
        Handle player XP award events by sending updates to the client.

        Args:
            event: The PlayerXPAwardEvent containing XP award information
        """
        if not self.connection_manager:
            self._logger.debug(
                "Connection manager not available, skipping player XP awarded event", player_id=event.player_id
            )
            return

        try:
            player_id = event.player_id
            player_id_str = str(player_id)

            player = await self.connection_manager.get_player(player_id)
            if not player:
                self._logger.warning("Player not found for XP award event", player_id=player_id_str)
                return

            player_update_data: dict[str, object] = {
                "player_id": player_id_str,
                "name": player.name,
                "level": player.level,
                "xp": player.experience_points,
                "current_room_id": getattr(player, "current_room_id", None),
            }

            xp_update_event = build_event(
                "player_xp_updated",
                {
                    "xp_amount": event.xp_amount,
                    "new_level": event.new_level,
                    "player": player_update_data,
                },
                player_id=player_id_str,
            )

            _ = await self.connection_manager.send_personal_message(player_id, xp_update_event)

            self._logger.info(
                "Sent XP award update to player",
                player_id=player_id_str,
                xp_amount=event.xp_amount,
                new_level=event.new_level,
            )

        except (ValueError, AttributeError, ImportError, SQLAlchemyError, TypeError) as e:
            self._logger.error("Error handling player XP award event", error_message=str(e), exc_info=True)

    async def handle_player_dp_updated(self, event: PlayerDPUpdated) -> None:
        """
        Handle player DP update events by sending updates to the client.

        Args:
            event: The PlayerDPUpdated event containing DP change information
        """
        if not self.connection_manager:
            self._logger.debug(
                "Connection manager not available, skipping player DP updated event", player_id=event.player_id
            )
            return

        try:
            await _dispatch_player_dp_updated_payload(self.connection_manager, self._logger, event)
        except (ValueError, AttributeError, ImportError, SQLAlchemyError, TypeError) as e:
            self._logger.error("Error handling player DP update event", error_message=str(e), exc_info=True)

    async def handle_player_died(self, event: PlayerDiedEvent) -> None:
        """
        Handle player death events by sending death notification to the client.

        Args:
            event: The PlayerDiedEvent containing death information
        """
        if not self.connection_manager:
            self._logger.debug(
                "Connection manager not available, skipping player died event",
                player_id=event.player_id,
            )
            return

        try:
            await _send_player_death_notification(self.connection_manager, self._logger, event)
        except (ValueError, AttributeError, ImportError, SQLAlchemyError, TypeError) as e:
            self._logger.error("Error handling player died event", error_message=str(e), exc_info=True)

    async def handle_player_dp_decay(self, event: PlayerDPDecayEvent) -> None:
        """
        Handle player DP decay events by sending decay notification to the client.

        Args:
            event: The PlayerDPDecayEvent containing DP decay information
        """
        if not self.connection_manager:
            self._logger.debug(
                "Connection manager not available, skipping player DP decay event",
                player_id=event.player_id,
            )
            return

        try:
            await _dispatch_player_dp_decay_payload(self.connection_manager, self._logger, event)
        except (ValueError, AttributeError, ImportError, SQLAlchemyError, TypeError) as e:
            self._logger.error("Error handling player DP decay event", error_message=str(e), exc_info=True)
