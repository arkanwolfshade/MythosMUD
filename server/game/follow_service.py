"""
Follow service for MythosMUD.

In-memory follow state: who is following whom (player or NPC).
When the followed entity moves, followers attempt the same move; on failure they are auto-unfollowed.
Player-to-player follow requires target acceptance (pending request + follow_request event).
"""

from __future__ import annotations

import asyncio
import uuid
from collections.abc import Coroutine
from datetime import UTC, datetime
from typing import TYPE_CHECKING

from structlog.stdlib import BoundLogger

from server.events.event_types import NPCEnteredRoom, PlayerEnteredRoom
from server.game import follow_movement
from server.game.follow_types import (
    FOLLOW_REQUEST_TTL_SECONDS,
    FollowActionResult,
    FollowPersistence,
    FollowStatePayload,
    FollowTargetValue,
    PendingFollowRequest,
    TargetType,
    is_npc_follow_value,
    str_id,
)
from server.realtime.connection_manager_api import send_game_event
from server.structured_logging.enhanced_logging_config import get_logger

if TYPE_CHECKING:
    from server.events.event_bus import EventBus
    from server.game.movement_service import MovementService
    from server.realtime.connection_manager import ConnectionManager
    from server.services.player_position_service import PlayerPositionService
    from server.services.user_manager import UserManager

# Re-exports for callers/tests that import from this module.
_str_id = str_id
_is_npc_follow_value = is_npc_follow_value
_FollowTargetValue = FollowTargetValue

logger = get_logger(__name__)


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
        async_persistence: FollowPersistence | None = None,
        player_position_service: PlayerPositionService | None = None,
    ) -> None:
        self._event_bus: EventBus | None = event_bus
        self._movement_service: MovementService | None = movement_service
        self._user_manager: UserManager | None = user_manager
        self._connection_manager: ConnectionManager | None = connection_manager
        self._async_persistence: FollowPersistence | None = async_persistence
        self._player_position_service: PlayerPositionService | None = player_position_service
        self._logger: BoundLogger = get_logger(__name__)
        # follower_id -> (target_id, target_type) or (target_id, target_type, display_name)
        self._follow_target: dict[str, FollowTargetValue] = {}
        # request_id -> pending request record
        self._pending_requests: dict[str, PendingFollowRequest] = {}
        self._service_id: str = "follow_service"
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
            created = data["created_at"]
            elapsed = (now - created).total_seconds()
            if elapsed >= FOLLOW_REQUEST_TTL_SECONDS:
                to_remove.append(req_id)
        for req_id in to_remove:
            data = self._pending_requests.pop(req_id)
            if self._connection_manager:
                self._send_result_to_player(
                    data["requestor_id"],
                    "Your follow request has expired.",
                )
                self._logger.debug(
                    "Follow request expired",
                    request_id=req_id,
                    requestor_id=data["requestor_id"],
                )

    def _schedule_coro(self, coro: Coroutine[object, object, object]) -> None:
        """Fire-and-forget; close coro if no running event loop (e.g. sync unit tests)."""
        try:
            _ = asyncio.create_task(coro)
        except RuntimeError:
            coro.close()
            raise

    def _send_result_to_player(self, player_id: str, result: str) -> None:
        """Send a command_response-style message to a single player."""
        if not self._connection_manager:
            return
        try:
            self._schedule_coro(
                send_game_event(
                    player_id,
                    "command_response",
                    {"result": result},
                )
            )
        except (ValueError, TypeError, RuntimeError) as e:
            self._logger.warning(
                "Failed to send follow message to player",
                player_id=player_id,
                error=str(e),
            )

    def _send_follow_state_to_player(self, player_id: str, following: FollowStatePayload | None) -> None:
        """Send follow_state event so client can update title panel (who I am following)."""
        if not self._connection_manager:
            return
        try:
            self._schedule_coro(
                send_game_event(
                    player_id,
                    "follow_state",
                    {"following": following},
                )
            )
        except (ValueError, TypeError, RuntimeError) as e:
            self._logger.warning(
                "Failed to send follow_state to player",
                player_id=player_id,
                error=str(e),
            )

    def _start_following_npc(
        self,
        requestor_id: str,
        target_id: str,
        target_display_name: str | None,
    ) -> FollowActionResult:
        """Immediately attach follow state for an NPC target."""
        display_name = (target_display_name or target_id).strip() or target_id
        self._follow_target[requestor_id] = (target_id, "npc", display_name)
        self._logger.info(
            "Player now following NPC",
            requestor_id=requestor_id,
            target_id=target_id,
        )
        self._send_follow_state_to_player(requestor_id, {"target_name": display_name, "target_type": "npc"})
        return {"success": True, "result": f"You are now following {display_name}."}

    async def _follow_request_mute_failure(
        self,
        requestor_id: str,
        target_id: str,
    ) -> FollowActionResult | None:
        """Return a failure payload when mute blocks the request; None if allowed."""
        if not self._user_manager:
            return None
        try:
            if await self._user_manager.is_player_muted_async(uuid.UUID(target_id), uuid.UUID(requestor_id)):
                return {
                    "success": False,
                    "result": "They are not accepting follow requests.",
                }
        except (ValueError, TypeError, AttributeError) as e:
            self._logger.warning(
                "Mute check failed for follow request",
                requestor_id=requestor_id,
                target_id=target_id,
                error=str(e),
            )
            return {"success": False, "result": "Unable to complete follow request."}
        return None

    def _create_pending_follow_request(
        self,
        requestor_id: str,
        target_id: str,
        requestor_name: str,
    ) -> FollowActionResult:
        """Store a pending player follow request and notify the target when possible."""
        request_id = str(uuid.uuid4())
        self._pending_requests[request_id] = {
            "requestor_id": requestor_id,
            "requestor_name": requestor_name,
            "target_id": target_id,
            "created_at": datetime.now(UTC),
        }
        try:
            self._schedule_coro(
                self._send_follow_request_to_target(target_id, request_id, requestor_name, requestor_id)
            )
        except RuntimeError:
            # No running loop (e.g. sync unit tests); request remains pending in memory.
            pass
        self._logger.info(
            "Follow request created",
            request_id=request_id,
            requestor_id=requestor_id,
            target_id=target_id,
        )
        return {
            "success": True,
            "result": "Follow request sent. Waiting for them to accept.",
            "request_id": request_id,
        }

    async def request_follow(
        self,
        requestor_id: uuid.UUID | str,
        target_id: str,
        target_type: TargetType,
        requestor_name: str,
        target_display_name: str | None = None,
    ) -> FollowActionResult:
        """
        Request to follow a player (pending acceptance) or start following an NPC immediately.

        Returns dict with keys: success (bool), result (str), and optionally target_message (str).
        target_display_name: Optional display name for messages (e.g. NPC "Sanitarium patient").
        """
        self._expire_pending_requests()
        rid = str_id(requestor_id)
        if rid == target_id:
            return {"success": False, "result": "You cannot follow yourself."}
        if self._follow_target.get(rid):
            return {"success": False, "result": "You are already following someone. Use /unfollow first."}
        if target_type == "npc":
            return self._start_following_npc(rid, target_id, target_display_name)
        mute_failure = await self._follow_request_mute_failure(rid, target_id)
        if mute_failure is not None:
            return mute_failure
        return self._create_pending_follow_request(rid, target_id, requestor_name)

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
            _ = await self._connection_manager.send_personal_message(uuid.UUID(target_id), event)
        except (ValueError, TypeError, AttributeError, RuntimeError) as e:
            self._logger.warning(
                "Failed to send follow_request to target",
                target_id=target_id,
                error=str(e),
            )

    async def accept_follow(self, target_id: uuid.UUID | str, request_id: str) -> FollowActionResult:
        """Accept a follow request. Target is the player who accepted (the followee)."""
        self._expire_pending_requests()
        tid = str_id(target_id)
        data = self._pending_requests.pop(request_id, None)
        if not data or data["target_id"] != tid:
            return {"success": False, "result": "Invalid or expired follow request."}
        requestor_id = data["requestor_id"]
        requestor_name = data["requestor_name"]
        self._follow_target[requestor_id] = (tid, "player")
        self._logger.info(
            "Follow request accepted",
            requestor_id=requestor_id,
            target_id=tid,
        )
        target_display_name = tid
        if self._async_persistence:
            try:
                followee = await self._async_persistence.get_player_by_id(uuid.UUID(tid))
                if followee is not None and followee.name:
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

    async def decline_follow(self, target_id: uuid.UUID | str, request_id: str) -> FollowActionResult:
        """Decline a follow request."""
        self._expire_pending_requests()
        tid = str_id(target_id)
        data = self._pending_requests.pop(request_id, None)
        if not data or data["target_id"] != tid:
            return {"success": False, "result": "Invalid or expired follow request."}
        requestor_id = data["requestor_id"]
        self._send_result_to_player(requestor_id, "Your follow request was declined.")
        return {
            "success": True,
            "result": "You declined the follow request.",
            "requestor_id": requestor_id,
        }

    def unfollow(self, follower_id: uuid.UUID | str) -> FollowActionResult:
        """Stop following. Returns result message."""
        fid = str_id(follower_id)
        removed = self._follow_target.pop(fid, None)
        if removed:
            self._logger.info("Player unfollowed", follower_id=fid, target_id=removed[0])
            self._send_follow_state_to_player(fid, None)
            return {"success": True, "result": "You are no longer following anyone."}
        return {"success": True, "result": "You weren't following anyone."}

    def get_followers(self, target_id: str) -> list[str]:
        """Return list of follower player IDs (for movement propagation)."""
        target_id_str = str_id(target_id)
        return [f for f, v in self._follow_target.items() if v[0] == target_id_str]

    def get_following(self, follower_id: uuid.UUID | str) -> tuple[str, TargetType] | None:
        """Return (target_id, target_type) if following someone, else None."""
        fid = str_id(follower_id)
        v = self._follow_target.get(fid)
        if v is None:
            return None
        return (v[0], v[1])

    def get_following_display_name(self, follower_id: uuid.UUID | str) -> str | None:
        """Return stored display name when following an NPC, else None. For players, resolve via persistence."""
        fid = str_id(follower_id)
        v = self._follow_target.get(fid)
        if not v or v[1] != "npc":
            return None
        if is_npc_follow_value(v):
            return v[2]
        return None

    async def _resolve_follow_target_label(
        self,
        following: FollowTargetValue,
        async_persistence: FollowPersistence | None,
    ) -> str:
        """Human-readable label for the entity this player is following."""
        target_id, ttype = following[0], following[1]
        if ttype == "npc" and is_npc_follow_value(following):
            return following[2]
        if ttype != "player" or not async_persistence:
            return target_id
        try:
            target_player = await async_persistence.get_player_by_id(uuid.UUID(target_id))
            if target_player is not None and target_player.name:
                return target_player.name
            return target_id
        except (ValueError, TypeError, AttributeError):
            return target_id

    async def _followers_display_line(
        self,
        followers: list[str],
        async_persistence: FollowPersistence | None,
    ) -> str:
        """One line listing who follows the player (or none)."""
        if not followers:
            return "No one is following you."
        if not async_persistence:
            return "Following you: " + ", ".join(followers)
        names: list[str] = []
        for pid in followers:
            try:
                player = await async_persistence.get_player_by_id(uuid.UUID(pid))
                if player is not None and player.name:
                    names.append(player.name)
                else:
                    names.append(pid)
            except (ValueError, TypeError, AttributeError):
                names.append(pid)
        return "Following you: " + ", ".join(names)

    async def get_following_display(
        self,
        follower_id: uuid.UUID | str,
        async_persistence: FollowPersistence | None = None,
    ) -> str:
        """Format who you follow and who follows you for /following output."""
        fid = str_id(follower_id)
        following = self._follow_target.get(fid)
        if following:
            label = await self._resolve_follow_target_label(following, async_persistence)
            lines = [f"You are following: {label} ({following[1]})"]
        else:
            lines = ["You are not following anyone."]
        lines.append(await self._followers_display_line(self.get_followers(fid), async_persistence))
        return "\n".join(lines)

    async def _ensure_follower_standing(self, follower_id: str) -> bool:
        """If follower is sitting or prone, try to stand them so they can move."""
        return await follow_movement.ensure_follower_standing(self, follower_id)

    async def _on_player_entered_room(self, event: PlayerEnteredRoom) -> None:
        """Move followers when the followed player moves."""
        await follow_movement.on_player_entered_room(self, event)

    async def _on_npc_entered_room(self, event: NPCEnteredRoom) -> None:
        """Move followers when the followed NPC moves."""
        await follow_movement.on_npc_entered_room(self, event)

    def on_player_disconnect(self, player_id: uuid.UUID | str) -> None:
        """Remove player from follow state and cancel any pending requests involving them."""
        pid = str_id(player_id)
        _ = self._follow_target.pop(pid, None)
        to_remove = [
            req_id
            for req_id, data in self._pending_requests.items()
            if pid in (data["requestor_id"], data["target_id"])
        ]
        for req_id in to_remove:
            _ = self._pending_requests.pop(req_id, None)
        for fid, v in list(self._follow_target.items()):
            target_id = v[0]
            if target_id == pid:
                _ = self._follow_target.pop(fid, None)
        self._logger.debug("Cleaned up follow state for disconnected player", player_id=pid)
