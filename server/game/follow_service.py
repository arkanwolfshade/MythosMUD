"""
Follow service for MythosMUD.

In-memory follow state: who is following whom (player or NPC).
When the followed entity moves, followers attempt the same move; on failure they are auto-unfollowed.
Player-to-player follow requires target acceptance (pending request + follow_request event).
"""

# pylint: disable=too-many-lines  # FollowService keeps tightly coupled follow logic together; splitting would harm cohesion.

from __future__ import annotations

import uuid
from datetime import UTC, datetime
from typing import TYPE_CHECKING, Any, Literal, TypeGuard

from server.events.event_types import NPCEnteredRoom, PlayerEnteredRoom
from server.structured_logging.enhanced_logging_config import get_logger

if TYPE_CHECKING:
    from server.events.event_bus import EventBus
    from server.game.movement_service import MovementService
    from server.realtime.connection_manager import ConnectionManager
    from server.services.player_position_service import PlayerPositionService
    from server.services.user_manager import UserManager

logger = get_logger(__name__)

FOLLOW_REQUEST_TTL_SECONDS = 60
TargetType = Literal["player", "npc"]
# Stored value: (target_id, target_type) for player; (target_id, target_type, display_name) for NPC.
_FollowTargetValue = tuple[str, TargetType] | tuple[str, TargetType, str]


def _is_npc_follow_value(v: _FollowTargetValue) -> TypeGuard[tuple[str, TargetType, str]]:
    """True when v is the 3-tuple (target_id, 'npc', display_name)."""
    return len(v) == 3


def _str_id(value: uuid.UUID | str) -> str:
    """Normalize ID to string for dict keys."""
    return str(value) if isinstance(value, uuid.UUID) else value


class FollowService:
    """
    In-memory follow state and movement propagation.

    Subscribes to PlayerEnteredRoom and NPCEnteredRoom to move followers.
    Pending player-to-player follow requests expire after 60s; requestor is notified.
    """

    def __init__(
        self,
        event_bus: EventBus | None = None,
        movement_service: MovementService | None = None,
        user_manager: UserManager | None = None,
        connection_manager: ConnectionManager | None = None,
        async_persistence: Any | None = None,
        player_position_service: PlayerPositionService | None = None,
    ) -> None:
        self._event_bus = event_bus
        self._movement_service = movement_service
        self._user_manager = user_manager
        self._connection_manager = connection_manager
        self._async_persistence = async_persistence
        self._player_position_service = player_position_service
        self._logger = get_logger(__name__)
        # follower_id -> (target_id, target_type) or (target_id, target_type, display_name)
        self._follow_target: dict[str, _FollowTargetValue] = {}
        # request_id -> { requestor_id, requestor_name, target_id, created_at }
        self._pending_requests: dict[str, dict[str, Any]] = {}
        self._service_id = "follow_service"
        if event_bus:
            event_bus.subscribe(
                PlayerEnteredRoom,
                self._on_player_entered_room,
                service_id=self._service_id,
            )
            event_bus.subscribe(
                NPCEnteredRoom,
                self._on_npc_entered_room,
                service_id=self._service_id,
            )
        self._logger.info(
            "FollowService initialized",
            has_event_bus=bool(event_bus),
            has_movement_service=bool(movement_service),
        )

    def _expire_pending_requests(self) -> None:
        """Remove expired pending requests and notify requestors."""
        now = datetime.now(UTC)
        to_remove: list[str] = []
        for req_id, data in self._pending_requests.items():
            created = data.get("created_at")
            if isinstance(created, datetime):
                elapsed = (now - created).total_seconds()
                if elapsed >= FOLLOW_REQUEST_TTL_SECONDS:
                    to_remove.append(req_id)
        for req_id in to_remove:
            data = self._pending_requests.pop(req_id, {})
            if data and self._connection_manager:
                requestor_id = data.get("requestor_id")
                if requestor_id:
                    self._send_result_to_player(
                        _str_id(requestor_id),
                        "Your follow request has expired.",
                    )
                    self._logger.debug(
                        "Follow request expired",
                        request_id=req_id,
                        requestor_id=requestor_id,
                    )

    def _send_result_to_player(self, player_id: str, result: str) -> None:
        """Send a command_response-style message to a single player."""
        if not self._connection_manager:
            return
        try:
            import asyncio

            from server.realtime.connection_manager_api import send_game_event

            asyncio.create_task(
                send_game_event(
                    player_id,
                    "command_response",
                    {"result": result},
                )
            )
        except (ImportError, ValueError, TypeError, RuntimeError) as e:
            self._logger.warning(
                "Failed to send follow message to player",
                player_id=player_id,
                error=str(e),
            )

    def _send_result_and_player_update(self, player_id: str, result: str, position: str | None = None) -> None:
        """Send command_response with result message and optional player_update (e.g. position) for client UI."""
        if not self._connection_manager:
            return
        try:
            import asyncio

            from server.realtime.connection_manager_api import send_game_event

            data: dict[str, Any] = {"result": result}
            if position is not None:
                data["player_update"] = {"position": position}
            asyncio.create_task(
                send_game_event(
                    player_id,
                    "command_response",
                    data,
                )
            )
        except (ImportError, ValueError, TypeError, RuntimeError) as e:
            self._logger.warning(
                "Failed to send result and player update to player",
                player_id=player_id,
                error=str(e),
            )

    def _send_follow_state_to_player(self, player_id: str, following: dict[str, Any] | None) -> None:
        """Send follow_state event so client can update title panel (who I am following)."""
        if not self._connection_manager:
            return
        try:
            import asyncio

            from server.realtime.connection_manager_api import send_game_event

            asyncio.create_task(
                send_game_event(
                    player_id,
                    "follow_state",
                    {"following": following},
                )
            )
        except (ImportError, ValueError, TypeError, RuntimeError) as e:
            self._logger.warning(
                "Failed to send follow_state to player",
                player_id=player_id,
                error=str(e),
            )

    async def request_follow(
        self,
        requestor_id: uuid.UUID | str,
        target_id: str,
        target_type: TargetType,
        requestor_name: str,
        target_display_name: str | None = None,
    ) -> dict[str, Any]:
        """
        Request to follow a player (pending acceptance) or start following an NPC immediately.

        Returns dict with keys: success (bool), result (str), and optionally target_message (str).
        target_display_name: Optional display name for messages (e.g. NPC "Sanitarium patient").
        """
        self._expire_pending_requests()
        rid = _str_id(requestor_id)
        if rid == target_id:
            return {"success": False, "result": "You cannot follow yourself."}
        current = self._follow_target.get(rid)
        if current:
            return {"success": False, "result": "You are already following someone. Use /unfollow first."}

        if target_type == "npc":
            display_name = (target_display_name or target_id).strip() or target_id
            self._follow_target[rid] = (target_id, "npc", display_name)
            self._logger.info(
                "Player now following NPC",
                requestor_id=rid,
                target_id=target_id,
            )
            self._send_follow_state_to_player(rid, {"target_name": display_name, "target_type": "npc"})
            return {"success": True, "result": f"You are now following {display_name}."}

        # Player target: check mute then create pending request
        if self._user_manager:
            try:
                target_uuid = uuid.UUID(target_id) if isinstance(target_id, str) else target_id
                req_uuid = uuid.UUID(rid) if isinstance(rid, str) else requestor_id
                muted = await self._user_manager.is_player_muted_async(target_uuid, req_uuid)
                if muted:
                    return {
                        "success": False,
                        "result": "They are not accepting follow requests.",
                    }
            except (ValueError, TypeError, AttributeError) as e:
                self._logger.warning(
                    "Mute check failed for follow request",
                    requestor_id=rid,
                    target_id=target_id,
                    error=str(e),
                )
                return {"success": False, "result": "Unable to complete follow request."}

        request_id = str(uuid.uuid4())
        self._pending_requests[request_id] = {
            "requestor_id": rid,
            "requestor_name": requestor_name,
            "target_id": target_id,
            "created_at": datetime.now(UTC),
        }
        import asyncio

        asyncio.create_task(self._send_follow_request_to_target(target_id, request_id, requestor_name, rid))
        self._logger.info(
            "Follow request created",
            request_id=request_id,
            requestor_id=rid,
            target_id=target_id,
        )
        return {
            "success": True,
            "result": "Follow request sent. Waiting for them to accept.",
            "request_id": request_id,
        }

    async def _send_follow_request_to_target(
        self,
        target_id: str,
        request_id: str,
        requestor_name: str,
        requestor_id: str,
    ) -> None:
        """Send follow_request event to the target player only."""
        if not self._connection_manager:
            self._logger.warning("No connection manager; cannot send follow_request to target")
            return
        try:
            from server.realtime.envelope import build_event

            event = build_event(
                "follow_request",
                {
                    "request_id": request_id,
                    "requestor_name": requestor_name,
                    "requestor_id": requestor_id,
                },
            )
            target_uuid = uuid.UUID(target_id) if isinstance(target_id, str) else target_id
            await self._connection_manager.send_personal_message(target_uuid, event)
        except (ValueError, TypeError, AttributeError, RuntimeError) as e:
            self._logger.warning(
                "Failed to send follow_request to target",
                target_id=target_id,
                error=str(e),
            )

    async def accept_follow(self, target_id: uuid.UUID | str, request_id: str) -> dict[str, Any]:
        """Accept a follow request. Target is the player who accepted (the followee)."""
        self._expire_pending_requests()
        tid = _str_id(target_id)
        data = self._pending_requests.pop(request_id, None)
        if not data or data.get("target_id") != tid:
            return {"success": False, "result": "Invalid or expired follow request."}
        requestor_id = data.get("requestor_id", "")
        requestor_name = data.get("requestor_name", "Someone")
        self._follow_target[requestor_id] = (tid, "player")
        self._logger.info(
            "Follow request accepted",
            requestor_id=requestor_id,
            target_id=tid,
        )
        target_display_name = tid
        if self._async_persistence:
            try:
                target_uuid = uuid.UUID(tid) if isinstance(tid, str) else target_id
                followee = await self._async_persistence.get_player_by_id(target_uuid)
                if followee and getattr(followee, "name", None):
                    target_display_name = followee.name
            except (ValueError, TypeError, AttributeError):
                pass
        self._send_result_to_player(requestor_id, f"You are now following {target_display_name}.")
        self._send_result_to_player(tid, f"{requestor_name} is now following you.")
        return {
            "success": True,
            "result": f"You are now being followed by {requestor_name}.",
            "requestor_id": requestor_id,
        }

    async def decline_follow(self, target_id: uuid.UUID | str, request_id: str) -> dict[str, Any]:
        """Decline a follow request."""
        self._expire_pending_requests()
        tid = _str_id(target_id)
        data = self._pending_requests.pop(request_id, None)
        if not data or data.get("target_id") != tid:
            return {"success": False, "result": "Invalid or expired follow request."}
        requestor_id = data.get("requestor_id", "")
        self._send_result_to_player(requestor_id, "Your follow request was declined.")
        return {
            "success": True,
            "result": "You declined the follow request.",
            "requestor_id": requestor_id,
        }

    def unfollow(self, follower_id: uuid.UUID | str) -> dict[str, Any]:
        """Stop following. Returns result message."""
        fid = _str_id(follower_id)
        removed = self._follow_target.pop(fid, None)
        if removed:
            self._logger.info("Player unfollowed", follower_id=fid, target_id=removed[0])
            self._send_follow_state_to_player(fid, None)
            return {"success": True, "result": "You are no longer following anyone."}
        return {"success": True, "result": "You weren't following anyone."}

    def get_followers(self, target_id: str) -> list[str]:
        """Return list of follower player IDs (for movement propagation)."""
        target_id_str = _str_id(target_id)
        return [f for f, v in self._follow_target.items() if v[0] == target_id_str]

    def get_following(self, follower_id: uuid.UUID | str) -> tuple[str, TargetType] | None:
        """Return (target_id, target_type) if following someone, else None."""
        fid = _str_id(follower_id)
        v = self._follow_target.get(fid)
        if v is None:
            return None
        return (v[0], v[1])

    def get_following_display_name(self, follower_id: uuid.UUID | str) -> str | None:
        """Return stored display name when following an NPC, else None. For players, resolve via persistence."""
        fid = _str_id(follower_id)
        v = self._follow_target.get(fid)
        if not v or v[1] != "npc":
            return None
        if _is_npc_follow_value(v):
            return v[2]
        return None

    async def get_following_display(
        self,
        follower_id: uuid.UUID | str,
        async_persistence: Any | None = None,
    ) -> str:
        """Format who you follow and who follows you for /following output."""
        fid = _str_id(follower_id)
        lines: list[str] = []
        following = self._follow_target.get(fid)
        if following:
            target_id, ttype = following[0], following[1]
            target_display = target_id
            if ttype == "player" and async_persistence:
                try:
                    target_player = await async_persistence.get_player_by_id(uuid.UUID(target_id))
                    if target_player and getattr(target_player, "name", None):
                        target_display = target_player.name
                except (ValueError, TypeError, AttributeError):
                    pass
            elif ttype == "npc" and len(following) >= 3:
                target_display = following[2]
            lines.append(f"You are following: {target_display} ({ttype})")
        else:
            lines.append("You are not following anyone.")
        followers = self.get_followers(fid)
        if followers:
            if async_persistence:
                names: list[str] = []
                for pid in followers:
                    try:
                        p = await async_persistence.get_player_by_id(uuid.UUID(pid))
                        names.append(getattr(p, "name", pid) if p else pid)
                    except (ValueError, TypeError, AttributeError):
                        names.append(pid)
                lines.append("Following you: " + ", ".join(names))
            else:
                lines.append("Following you: " + ", ".join(followers))
        else:
            lines.append("No one is following you.")
        return "\n".join(lines)

    async def _ensure_follower_standing(self, follower_id: str) -> bool:
        """
        If follower is sitting or prone, try to stand them so they can move.
        Returns True if follower is or can be standing, False if unable to stand.
        """
        if not self._async_persistence or not self._player_position_service:
            return True
        try:
            player = await self._async_persistence.get_player_by_id(uuid.UUID(follower_id))
            if not player or not hasattr(player, "get_stats"):
                return True
            stats = player.get_stats() or {}
            if not isinstance(stats, dict):
                return True
            position = (stats.get("position") or "standing").lower()
            if position == "standing":
                return True
            if position not in ("sitting", "lying"):
                return True
            name = getattr(player, "name", None) or str(follower_id)
            result = await self._player_position_service.change_position(name, "standing")
            if result.get("success"):
                self._logger.debug(
                    "Follower stood automatically to follow",
                    follower_id=follower_id,
                )
                # Notify follower so Game Info shows stand message and Character panel updates posture.
                self._send_result_and_player_update(
                    follower_id,
                    result.get("message", "You rise to your feet."),
                    position="standing",
                )
                return True
            self._logger.info(
                "Follower could not stand to follow",
                follower_id=follower_id,
            )
            return False
        except (ValueError, TypeError, AttributeError) as e:
            self._logger.warning(
                "Could not check/stand follower for follow move",
                follower_id=follower_id,
                error=str(e),
            )
            return True

    async def _on_player_entered_room(self, event: PlayerEnteredRoom) -> None:
        """Move followers when the followed player moves."""
        if not event.from_room_id or not self._movement_service:
            return
        followers = self.get_followers(event.player_id)
        for follower_id in followers:
            await self._handle_player_follower_move(follower_id, event)

    async def _on_npc_entered_room(self, event: NPCEnteredRoom) -> None:
        """Move followers when the followed NPC moves."""
        if not event.from_room_id or not self._movement_service:
            return
        followers = self.get_followers(event.npc_id)
        for follower_id in followers:
            await self._handle_npc_follower_move(follower_id, event)

    async def _handle_player_follower_move(self, follower_id: str, event: PlayerEnteredRoom) -> None:
        """
        Handle movement propagation for a single follower of a player.

        This helper keeps _on_player_entered_room shallow for readability and Pylint nesting rules.
        """
        if not self._movement_service or event.from_room_id is None:
            # Guard for mypy and runtime: caller should already check these, but we assert locally for safety.
            return
        movement_service = self._movement_service
        try:
            if not await self._ensure_follower_standing(follower_id):
                self.unfollow(follower_id)
                self._send_result_to_player(
                    follower_id,
                    "You could not stand to follow and are no longer following.",
                )
                self._logger.info(
                    "Follower lost target (could not stand)",
                    follower_id=follower_id,
                    target_id=event.player_id,
                )
                return
            # Idempotency: if follower is already in target room (e.g. duplicate
            # PlayerEnteredRoom event), skip move and do not unfollow.
            if self._async_persistence:
                try:
                    follower = await self._async_persistence.get_player_by_id(uuid.UUID(follower_id))
                    if follower and getattr(follower, "current_room_id", None):
                        if str(follower.current_room_id) == event.room_id:
                            self._logger.debug(
                                "Follower already in target room, skipping move",
                                follower_id=follower_id,
                                room_id=event.room_id,
                            )
                            return
                except (ValueError, TypeError, AttributeError):
                    pass
            success = await movement_service.move_player(
                follower_id,
                event.from_room_id,
                event.room_id,
            )
            if not success:
                self.unfollow(follower_id)
                self._send_result_to_player(
                    follower_id,
                    "You lost your target and are no longer following.",
                )
                self._send_follow_state_to_player(follower_id, None)
                self._logger.info(
                    "Follower lost target (move failed)",
                    follower_id=follower_id,
                    target_id=event.player_id,
                )
            else:
                # Notify follower so Game Info shows they moved (room_state updates Location panel).
                self._send_result_to_player(
                    follower_id,
                    "You follow your target into the room.",
                )
        except Exception as e:  # pylint: disable=broad-exception-caught
            self._logger.warning(
                "Error moving follower",
                follower_id=follower_id,
                error=str(e),
            )
            self.unfollow(follower_id)
            self._send_result_to_player(
                follower_id,
                "You lost your target and are no longer following.",
            )

    async def _handle_npc_follower_move(self, follower_id: str, event: NPCEnteredRoom) -> None:
        """
        Handle movement propagation for a single follower of an NPC.

        Extracted helper to keep _on_npc_entered_room shallow and maintain Pylint nesting limits.
        """
        if not self._movement_service or event.from_room_id is None:
            # Guard for mypy and runtime: caller should already check these, but we assert locally for safety.
            return
        movement_service = self._movement_service
        try:
            if not await self._ensure_follower_standing(follower_id):
                self.unfollow(follower_id)
                self._send_result_to_player(
                    follower_id,
                    "You could not stand to follow and are no longer following.",
                )
                self._logger.info(
                    "Follower lost target (could not stand)",
                    follower_id=follower_id,
                    npc_id=event.npc_id,
                )
                return
            # Idempotency: skip move if follower already in target room.
            if self._async_persistence:
                try:
                    follower = await self._async_persistence.get_player_by_id(uuid.UUID(follower_id))
                    if follower and getattr(follower, "current_room_id", None):
                        if str(follower.current_room_id) == event.room_id:
                            self._logger.debug(
                                "Follower already in target room, skipping move (NPC)",
                                follower_id=follower_id,
                                room_id=event.room_id,
                            )
                            return
                except (ValueError, TypeError, AttributeError):
                    pass
            success = await movement_service.move_player(
                follower_id,
                event.from_room_id,
                event.room_id,
            )
            if not success:
                self.unfollow(follower_id)
                self._send_result_to_player(
                    follower_id,
                    "You lost your target and are no longer following.",
                )
                self._send_follow_state_to_player(follower_id, None)
                self._logger.info(
                    "Follower lost target (NPC move failed)",
                    follower_id=follower_id,
                    npc_id=event.npc_id,
                )
            else:
                self._send_result_to_player(
                    follower_id,
                    "You follow your target into the room.",
                )
        except Exception as e:  # pylint: disable=broad-exception-caught
            self._logger.warning(
                "Error moving follower of NPC",
                follower_id=follower_id,
                error=str(e),
            )
            self.unfollow(follower_id)
            self._send_result_to_player(
                follower_id,
                "You lost your target and are no longer following.",
            )

    def on_player_disconnect(self, player_id: uuid.UUID | str) -> None:
        """Remove player from follow state and cancel any pending requests involving them."""
        pid = _str_id(player_id)
        self._follow_target.pop(pid, None)
        to_remove = [
            req_id
            for req_id, data in self._pending_requests.items()
            if data.get("requestor_id") == pid or data.get("target_id") == pid
        ]
        for req_id in to_remove:
            self._pending_requests.pop(req_id, None)
        for fid, v in list(self._follow_target.items()):
            target_id = v[0]
            if target_id == pid:
                self._follow_target.pop(fid, None)
        self._logger.debug("Cleaned up follow state for disconnected player", player_id=pid)
