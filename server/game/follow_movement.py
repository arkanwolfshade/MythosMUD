"""Follower auto-stand and movement propagation for FollowService."""

# pyright: reportPrivateUsage=false
# Reason: Module helpers are co-owned with FollowService and intentionally use its private fields.
# pylint: disable=protected-access  # Reason: Same co-owned helper surface as pyright private-usage exemption.
# pylint: disable=missing-function-docstring  # Reason: Protocol method stubs; contracts live in class docstrings

from __future__ import annotations

import uuid
from typing import TYPE_CHECKING, Protocol

from server.events.event_types import NPCEnteredRoom, PlayerEnteredRoom
from server.realtime.posture_notify import emit_posture_change

if TYPE_CHECKING:
    from structlog.stdlib import BoundLogger

    from server.game.follow_types import FollowActionResult, FollowPersistence, FollowPlayerView, FollowStatePayload
    from server.game.movement_service import MovementService
    from server.realtime.connection_manager import ConnectionManager
    from server.services.player_position_service import PlayerPositionService


class _FollowMovementHost(Protocol):
    """FollowService surface required by movement helpers."""

    _async_persistence: FollowPersistence | None
    _player_position_service: PlayerPositionService | None
    _connection_manager: ConnectionManager | None
    _movement_service: MovementService | None
    _logger: BoundLogger

    def get_followers(self, target_id: str) -> list[str]: ...

    def unfollow(self, follower_id: uuid.UUID | str) -> FollowActionResult: ...

    def _send_result_to_player(self, player_id: str, result: str) -> None: ...

    def _send_follow_state_to_player(self, player_id: str, following: FollowStatePayload | None) -> None: ...


def follower_needs_stand(player: FollowPlayerView) -> bool:
    """True when follower posture is sitting or lying (must stand to move)."""
    stats = player.get_stats() or {}
    position = stats.get("position", "standing")
    if not isinstance(position, str):
        return False
    return position.lower() in ("sitting", "lying")


async def stand_follower_for_move(host: _FollowMovementHost, follower_id: str, player: FollowPlayerView) -> bool:
    """Stand a sitting/lying follower; emit posture on success. False if stand fails."""
    position_service = host._player_position_service
    if position_service is None:
        return True
    name = player.name or str(follower_id)
    result = await position_service.change_position(name, "standing")
    if not result.get("success"):
        host._logger.info(
            "Follower could not stand to follow",
            follower_id=follower_id,
        )
        return False
    host._logger.debug(
        "Follower stood automatically to follow",
        follower_id=follower_id,
    )
    room_id = result.get("room_id")
    _ = await emit_posture_change(
        host._connection_manager,
        player_id=uuid.UUID(follower_id),
        display_name=result.get("player_display_name", name),
        room_id=str(room_id) if room_id else None,
        previous_position=result.get("previous_position"),
        new_position=result.get("position", "standing"),
        include_self_message=True,
        send_personal_update=True,
    )
    return True


async def ensure_follower_standing(host: _FollowMovementHost, follower_id: str) -> bool:
    """
    If follower is sitting or prone, try to stand them so they can move.
    Returns True if follower is or can be standing, False if unable to stand.
    """
    if not host._async_persistence or not host._player_position_service:
        return True
    try:
        player = await host._async_persistence.get_player_by_id(uuid.UUID(follower_id))
        if not player or not follower_needs_stand(player):
            return True
        return await stand_follower_for_move(host, follower_id, player)
    except (ValueError, TypeError, AttributeError) as e:
        host._logger.warning(
            "Could not check/stand follower for follow move",
            follower_id=follower_id,
            error=str(e),
        )
        return True


async def follower_already_in_room(host: _FollowMovementHost, follower_id: str, room_id: str) -> bool:
    """True when follower is already at room_id (duplicate enter events)."""
    if not host._async_persistence:
        return False
    try:
        follower = await host._async_persistence.get_player_by_id(uuid.UUID(follower_id))
        if follower is None:
            return False
        current = follower.current_room_id
        return bool(current) and str(current) == room_id
    except (ValueError, TypeError, AttributeError):
        return False


def drop_follower(host: _FollowMovementHost, follower_id: str, *, clear_follow_state: bool = False) -> None:
    """Unfollow and notify the follower they lost their target."""
    _ = host.unfollow(follower_id)
    host._send_result_to_player(
        follower_id,
        "You lost your target and are no longer following.",
    )
    if clear_follow_state:
        host._send_follow_state_to_player(follower_id, None)


async def propagate_follower_move(
    host: _FollowMovementHost,
    follower_id: str,
    from_room_id: str | None,
    to_room_id: str,
    *,
    log_extra: dict[str, object],
    already_in_room_msg: str,
    move_failed_msg: str,
    error_msg: str,
) -> None:
    """Stand, move, and notify one follower into the target's new room."""
    if not host._movement_service or from_room_id is None:
        return
    movement_service = host._movement_service
    try:
        if not await ensure_follower_standing(host, follower_id):
            _ = host.unfollow(follower_id)
            host._send_result_to_player(
                follower_id,
                "You could not stand to follow and are no longer following.",
            )
            host._logger.info(
                "Follower lost target (could not stand)",
                follower_id=follower_id,
                **log_extra,
            )
            return
        if await follower_already_in_room(host, follower_id, to_room_id):
            host._logger.debug(
                already_in_room_msg,
                follower_id=follower_id,
                room_id=to_room_id,
            )
            return
        success = await movement_service.move_player(follower_id, from_room_id, to_room_id)
        if not success:
            drop_follower(host, follower_id, clear_follow_state=True)
            host._logger.info(move_failed_msg, follower_id=follower_id, **log_extra)
            return
        host._send_result_to_player(follower_id, "You follow your target into the room.")
    except Exception as e:  # pylint: disable=broad-exception-caught
        host._logger.warning(error_msg, follower_id=follower_id, error=str(e))
        drop_follower(host, follower_id)


async def on_player_entered_room(host: _FollowMovementHost, event: PlayerEnteredRoom) -> None:
    """Move followers when the followed player moves."""
    if not event.from_room_id or not host._movement_service:
        return
    for follower_id in host.get_followers(event.player_id):
        await propagate_follower_move(
            host,
            follower_id,
            event.from_room_id,
            event.room_id,
            log_extra={"target_id": event.player_id},
            already_in_room_msg="Follower already in target room, skipping move",
            move_failed_msg="Follower lost target (move failed)",
            error_msg="Error moving follower",
        )


async def on_npc_entered_room(host: _FollowMovementHost, event: NPCEnteredRoom) -> None:
    """Move followers when the followed NPC moves."""
    if not event.from_room_id or not host._movement_service:
        return
    for follower_id in host.get_followers(event.npc_id):
        await propagate_follower_move(
            host,
            follower_id,
            event.from_room_id,
            event.room_id,
            log_extra={"npc_id": event.npc_id},
            already_in_room_msg="Follower already in target room, skipping move (NPC)",
            move_failed_msg="Follower lost target (NPC move failed)",
            error_msg="Error moving follower of NPC",
        )
