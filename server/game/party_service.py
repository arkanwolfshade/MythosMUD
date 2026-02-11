"""
Party service for MythosMUD.

In-memory ephemeral party state: parties exist only for the session. No persistence.
Leader can invite, kick, and disband; members can leave. Cleanup on disconnect.
Party invites use the same confirmation pattern as /follow: target must accept or decline.
"""

from __future__ import annotations

import asyncio
import uuid
from collections.abc import Callable, Coroutine
from dataclasses import dataclass, field
from datetime import UTC, datetime
from typing import TYPE_CHECKING, Any, cast

from server.structured_logging.enhanced_logging_config import get_logger

if TYPE_CHECKING:
    from server.events.event_bus import EventBus
    from server.realtime.connection_manager import ConnectionManager

logger = get_logger(__name__)

PARTY_INVITE_TTL_SECONDS = 60


def _str_id(value: uuid.UUID | str) -> str:
    """Normalize ID to string for dict keys and membership sets."""
    return str(value) if isinstance(value, uuid.UUID) else value


@dataclass
class Party:
    """
    In-memory party model.

    Ephemeral: not persisted. party_id and member_ids are string IDs for consistency
    with container/connection_manager usage (player_id as UUID is passed in/out as str
    in many code paths).
    """

    party_id: str
    leader_id: str
    member_ids: set[str] = field(default_factory=set)
    created_at: datetime = field(default_factory=lambda: datetime.now(UTC))

    def __post_init__(self) -> None:
        """Ensure leader is in member set."""
        if self.leader_id not in self.member_ids:
            self.member_ids = set(self.member_ids) | {self.leader_id}


class PartyService:
    """
    In-memory party management: create, disband, add/remove/kick members, leader checks.

    No persistence. Party invites require target acceptance (pending invite + party_invite event).
    Call on_player_disconnect(player_id) on session end to remove player from any party
    and disband if they were leader; pending invites involving that player are cancelled.
    Emits PartyUpdated events when event_bus is set.
    """

    def __init__(
        self,
        event_bus: EventBus | None = None,
        connection_manager: ConnectionManager | None = None,
        async_persistence: Any | None = None,
    ) -> None:
        """Initialize empty party store. Optionally provide event_bus, connection_manager, and async_persistence."""
        self._parties: dict[str, Party] = {}
        self._player_to_party: dict[str, str] = {}
        self._event_bus = event_bus
        self._connection_manager = connection_manager
        self._async_persistence = async_persistence
        self._pending_invites: dict[str, dict[str, Any]] = {}
        self._logger = get_logger(__name__)
        self._logger.info(
            "PartyService initialized",
            has_event_bus=bool(event_bus),
            has_connection_manager=bool(connection_manager),
            has_async_persistence=bool(async_persistence),
        )

    def _emit_party_updated(
        self,
        party_id: str,
        leader_id: str,
        member_ids: list[str],
        change_type: str = "updated",
    ) -> None:
        """Emit PartyUpdated event if event_bus is set."""
        if not self._event_bus:
            return
        try:
            from server.events.event_types import PartyUpdated

            self._event_bus.publish(
                PartyUpdated(
                    party_id=party_id,
                    leader_id=leader_id,
                    member_ids=member_ids,
                    change_type=change_type,
                )
            )
        except (ImportError, TypeError, AttributeError) as e:
            self._logger.warning(
                "Failed to emit PartyUpdated",
                party_id=party_id,
                error=str(e),
            )

    def create_party(self, leader_id: uuid.UUID | str) -> dict[str, Any]:
        """
        Create a new party with the given player as leader.

        Returns dict with success (bool), result (str), and optionally party_id.
        Fails if leader is already in a party.
        """
        lid = _str_id(leader_id)
        if lid in self._player_to_party:
            return {"success": False, "result": "You are already in a party. Leave it first."}
        party_id = str(uuid.uuid4())
        party = Party(party_id=party_id, leader_id=lid, member_ids={lid})
        self._parties[party_id] = party
        self._player_to_party[lid] = party_id
        self._emit_party_updated(party_id, lid, list(party.member_ids), "created")
        self._logger.info("Party created", party_id=party_id, leader_id=lid)
        return {"success": True, "result": "You have formed a new party.", "party_id": party_id}

    def disband_party(self, party_id: str | None, by_player_id: uuid.UUID | str | None = None) -> dict[str, Any]:
        """
        Disband a party. If by_player_id is given, only the leader may disband.

        If party_id is None and by_player_id is set, disband the party that player is in (if leader).
        Returns success and result message.
        """
        pid = _str_id(by_player_id) if by_player_id else None
        if party_id is None and pid:
            party_id = self._player_to_party.get(pid)
        if not party_id or party_id not in self._parties:
            return {"success": False, "result": "No such party."}
        party = self._parties[party_id]
        if by_player_id is not None and party.leader_id != pid:
            return {"success": False, "result": "Only the party leader can disband the party."}
        member_ids_snapshot = list(party.member_ids)
        leader_id = party.leader_id
        # Notify all members except the one who disbanded (if any)
        for mid in member_ids_snapshot:
            if mid != pid:  # Don't notify the person who disbanded
                self._schedule_notification(
                    cast(
                        Callable[[], Coroutine[Any, Any, None]],
                        lambda m=mid, lid=leader_id: self._notify_player_removed_from_party(m, lid),
                    )
                )
        for mid in party.member_ids:
            self._player_to_party.pop(mid, None)
        del self._parties[party_id]
        self._emit_party_updated(party_id, leader_id, member_ids_snapshot, "disbanded")
        self._logger.info("Party disbanded", party_id=party_id, by_player_id=pid)
        return {"success": True, "result": "The party has been disbanded."}

    def add_member(self, party_id: str, member_id: uuid.UUID | str) -> dict[str, Any]:
        """
        Add a player to a party. Fails if party does not exist or player is already in a party.
        """
        mid = _str_id(member_id)
        if mid in self._player_to_party:
            return {"success": False, "result": "That player is already in a party."}
        if party_id not in self._parties:
            return {"success": False, "result": "No such party."}
        party = self._parties[party_id]
        party.member_ids.add(mid)
        self._player_to_party[mid] = party_id
        self._emit_party_updated(party_id, party.leader_id, list(party.member_ids), "member_joined")
        self._logger.info("Member added to party", party_id=party_id, member_id=mid)
        return {"success": True, "result": "Player has been added to the party."}

    def _expire_pending_invites(self) -> None:
        """Remove expired pending invites and notify inviters."""
        now = datetime.now(UTC)
        to_remove: list[str] = []
        for invite_id, data in self._pending_invites.items():
            created = data.get("created_at")
            if isinstance(created, datetime):
                elapsed = (now - created).total_seconds()
                if elapsed >= PARTY_INVITE_TTL_SECONDS:
                    to_remove.append(invite_id)
        for invite_id in to_remove:
            data = self._pending_invites.pop(invite_id, {})
            if data:
                inviter_id = data.get("inviter_id")
                if inviter_id:
                    self._send_result_to_player(
                        _str_id(inviter_id),
                        "Your party invite has expired.",
                    )
                    self._logger.debug(
                        "Party invite expired",
                        invite_id=invite_id,
                        inviter_id=inviter_id,
                    )

    def _send_result_to_player(self, player_id: str, result: str) -> None:
        """Send a command_response-style message to a single player."""
        if not self._connection_manager:
            return
        try:
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
                "Failed to send party message to player",
                player_id=player_id,
                error=str(e),
            )

    def _schedule_notification(self, coro_factory: Callable[[], Coroutine[Any, Any, None]]) -> None:
        """
        Safely schedule an async notification, handling cases where no event loop is running.

        Args:
            coro_factory: A callable that returns a coroutine (to avoid creating coro when no loop exists)
        """
        try:
            # Try to get the running event loop (raises RuntimeError if none)
            asyncio.get_running_loop()
            # Only create the coroutine if we have a running loop
            coro = coro_factory()
            asyncio.create_task(coro)
        except RuntimeError:
            # No running event loop (e.g., in unit tests) - skip notification
            self._logger.debug(
                "Skipping async notification - no running event loop",
                notification_type="party_removal",
            )

    async def _notify_player_removed_from_party(self, removed_player_id: str, leader_id: str) -> None:
        """Notify a player they have been removed from a party. Resolves leader name."""
        leader_display_name = leader_id
        if self._async_persistence:
            try:
                leader_uuid = uuid.UUID(leader_id) if isinstance(leader_id, str) else leader_id
                leader_player = await self._async_persistence.get_player_by_id(leader_uuid)
                if leader_player and getattr(leader_player, "name", None):
                    leader_display_name = leader_player.name
            except (ValueError, TypeError, AttributeError) as e:
                self._logger.warning(
                    "Failed to resolve leader name for party removal notification",
                    leader_id=leader_id,
                    error=str(e),
                )
        message = f"You have been removed from {leader_display_name}'s party."
        self._send_result_to_player(removed_player_id, message)

    async def _send_party_invite_to_target(
        self,
        target_id: str,
        invite_id: str,
        inviter_name: str,
        inviter_id: str,
    ) -> None:
        """Send party_invite event to the target player only."""
        if not self._connection_manager:
            self._logger.warning("No connection manager; cannot send party_invite to target")
            return
        try:
            from server.realtime.envelope import build_event

            event = build_event(
                "party_invite",
                {
                    "invite_id": invite_id,
                    "inviter_name": inviter_name,
                    "inviter_id": inviter_id,
                },
            )
            target_uuid = uuid.UUID(target_id) if isinstance(target_id, str) else target_id
            await self._connection_manager.send_personal_message(target_uuid, event)
        except (ValueError, TypeError, AttributeError, RuntimeError) as e:
            self._logger.warning(
                "Failed to send party_invite to target",
                target_id=target_id,
                error=str(e),
            )

    async def request_party_invite(
        self,
        inviter_id: uuid.UUID | str,
        inviter_name: str,
        party_id: str,
        target_id: uuid.UUID | str,
    ) -> dict[str, Any]:
        """
        Create a pending party invite and send party_invite event to target.
        Target must accept or decline via accept_party_invite / decline_party_invite.
        Returns success and message for inviter.
        """
        self._expire_pending_invites()
        iid = _str_id(inviter_id)
        tid = _str_id(target_id)
        if tid in self._player_to_party:
            return {"success": False, "result": "That player is already in a party."}
        if party_id not in self._parties:
            return {"success": False, "result": "No such party."}
        party = self._parties[party_id]
        if party.leader_id != iid:
            return {"success": False, "result": "Only the party leader can invite members."}
        if tid in party.member_ids:
            return {"success": False, "result": "That player is already in your party."}
        invite_id = str(uuid.uuid4())
        self._pending_invites[invite_id] = {
            "inviter_id": iid,
            "inviter_name": inviter_name,
            "party_id": party_id,
            "target_id": tid,
            "created_at": datetime.now(UTC),
        }
        asyncio.create_task(self._send_party_invite_to_target(tid, invite_id, inviter_name, iid))
        self._logger.info(
            "Party invite created",
            invite_id=invite_id,
            inviter_id=iid,
            target_id=tid,
            party_id=party_id,
        )
        return {
            "success": True,
            "result": "Party invite sent. Waiting for them to accept.",
            "invite_id": invite_id,
        }

    async def accept_party_invite(self, target_id: uuid.UUID | str, invite_id: str) -> dict[str, Any]:
        """Accept a party invite. Target is the player who accepted (the invitee)."""
        self._expire_pending_invites()
        tid = _str_id(target_id)
        data = self._pending_invites.pop(invite_id, None)
        if not data or data.get("target_id") != tid:
            return {"success": False, "result": "Invalid or expired party invite."}
        inviter_id = data.get("inviter_id", "")
        inviter_name = data.get("inviter_name", "Someone")
        party_id = data.get("party_id", "")
        result = self.add_member(party_id, tid)
        if result.get("success"):
            # Resolve target player's display name (same pattern as FollowService.accept_follow)
            target_display_name = tid
            if self._async_persistence:
                try:
                    target_uuid = uuid.UUID(tid) if isinstance(tid, str) else target_id
                    player = await self._async_persistence.get_player_by_id(target_uuid)
                    if player and getattr(player, "name", None):
                        target_display_name = player.name
                except (ValueError, TypeError, AttributeError) as e:
                    self._logger.warning(
                        "Failed to resolve player name for party invite notification",
                        target_id=tid,
                        error=str(e),
                    )
            message = f"{target_display_name} has joined your party."
            self._send_result_to_player(inviter_id, message)
            self._logger.info(
                "Party invite accepted",
                invite_id=invite_id,
                inviter_id=inviter_id,
                target_id=tid,
                target_name=target_display_name,
            )
        # Construct personalized message for the accepting player (same pattern as FollowService.accept_follow)
        accepting_player_message = f"You have joined {inviter_name}'s party."
        return {
            "success": result.get("success", False),
            "result": accepting_player_message
            if result.get("success")
            else result.get("result", "Invalid or expired party invite."),
            "inviter_id": inviter_id,
        }

    async def decline_party_invite(self, target_id: uuid.UUID | str, invite_id: str) -> dict[str, Any]:
        """Decline a party invite."""
        self._expire_pending_invites()
        tid = _str_id(target_id)
        data = self._pending_invites.pop(invite_id, None)
        if not data or data.get("target_id") != tid:
            return {"success": False, "result": "Invalid or expired party invite."}
        inviter_id = data.get("inviter_id", "")
        self._send_result_to_player(inviter_id, "Your party invite was declined.")
        self._logger.info(
            "Party invite declined",
            invite_id=invite_id,
            inviter_id=inviter_id,
            target_id=tid,
        )
        return {
            "success": True,
            "result": "You declined the party invite.",
            "inviter_id": inviter_id,
        }

    def remove_member(self, party_id: str, player_id: uuid.UUID | str) -> dict[str, Any]:
        """
        Remove a player from a party (leave or internal remove). If leader leaves,
        party is disbanded.
        """
        pid = _str_id(player_id)
        if party_id not in self._parties:
            return {"success": False, "result": "No such party."}
        party = self._parties[party_id]
        if pid not in party.member_ids:
            return {"success": False, "result": "That player is not in this party."}
        party.member_ids.discard(pid)
        self._player_to_party.pop(pid, None)
        if party.leader_id == pid:
            # Leader left: disband. Emit disbanded before clearing.
            member_ids_snapshot = list(party.member_ids)
            leader_id = pid
            # Notify remaining members that party was disbanded
            for mid in member_ids_snapshot:
                if mid != pid:  # Don't notify the leader who left
                    self._schedule_notification(
                        cast(
                            Callable[[], Coroutine[Any, Any, None]],
                            lambda m=mid, lid=leader_id: self._notify_player_removed_from_party(m, lid),
                        )
                    )
            for mid in list(party.member_ids):
                self._player_to_party.pop(mid, None)
            del self._parties[party_id]
            self._emit_party_updated(party_id, pid, member_ids_snapshot, "disbanded")
            self._logger.info("Party disbanded (leader left)", party_id=party_id, leader_id=pid)
            return {"success": True, "result": "You left the party. The party has been disbanded."}
        self._emit_party_updated(party_id, party.leader_id, list(party.member_ids), "member_left")
        self._logger.info("Member left party", party_id=party_id, player_id=pid)
        return {"success": True, "result": "You have left the party."}

    def kick_member(
        self,
        party_id: str,
        target_id: uuid.UUID | str,
        by_player_id: uuid.UUID | str,
    ) -> dict[str, Any]:
        """Remove a member from the party. Only the leader may kick."""
        by_id = _str_id(by_player_id)
        tid = _str_id(target_id)
        if party_id not in self._parties:
            return {"success": False, "result": "No such party."}
        party = self._parties[party_id]
        if party.leader_id != by_id:
            return {"success": False, "result": "Only the party leader can kick members."}
        if tid == by_id:
            return {"success": False, "result": "You cannot kick yourself. Use leave instead."}
        if tid not in party.member_ids:
            return {"success": False, "result": "That player is not in your party."}
        leader_id = party.leader_id
        party.member_ids.discard(tid)
        self._player_to_party.pop(tid, None)
        # Notify the kicked player
        self._schedule_notification(lambda: self._notify_player_removed_from_party(tid, leader_id))
        self._emit_party_updated(party_id, leader_id, list(party.member_ids), "member_left")
        self._logger.info("Member kicked from party", party_id=party_id, target_id=tid, by_id=by_id)
        return {"success": True, "result": "Player has been removed from the party."}

    def get_party_for_player(self, player_id: uuid.UUID | str) -> Party | None:
        """Return the party the player is in, or None."""
        pid = _str_id(player_id)
        party_id = self._player_to_party.get(pid)
        if party_id is None:
            return None
        return self._parties.get(party_id)

    def get_party(self, party_id: str) -> Party | None:
        """Return the party by id, or None."""
        return self._parties.get(party_id)

    def is_leader(self, player_id: uuid.UUID | str) -> bool:
        """Return True if the player is the leader of their current party."""
        party = self.get_party_for_player(player_id)
        if party is None:
            return False
        return party.leader_id == _str_id(player_id)

    def get_party_members(self, player_id: uuid.UUID | str) -> list[str]:
        """
        Return list of party member IDs for the given player (including themselves).
        Empty list if not in a party. For use by combat/quest/lucidity hooks.
        """
        party = self.get_party_for_player(player_id)
        if party is None:
            return []
        return list(party.member_ids)

    def is_in_same_party(self, player_id_a: uuid.UUID | str, player_id_b: uuid.UUID | str) -> bool:
        """
        Return True if both players are in the same party. For combat/validator hook:
        e.g. block attacking a party member when party-friendly rules are enabled.
        """
        party_a = self.get_party_for_player(player_id_a)
        if party_a is None:
            return False
        pid_b = _str_id(player_id_b)
        return pid_b in party_a.member_ids

    def on_player_disconnect(self, player_id: uuid.UUID | str) -> None:
        """
        Remove player from any party and disband if they were leader.
        Cancel any pending invites where this player is inviter or target.
        Call on session disconnect.
        """
        pid = _str_id(player_id)
        for invite_id, data in list(self._pending_invites.items()):
            if data.get("inviter_id") == pid or data.get("target_id") == pid:
                self._pending_invites.pop(invite_id, None)
                other_id = data.get("target_id") if data.get("inviter_id") == pid else data.get("inviter_id")
                if other_id:
                    self._send_result_to_player(
                        other_id,
                        "Party invite was cancelled (player disconnected).",
                    )
                self._logger.debug(
                    "Party invite cancelled on disconnect",
                    invite_id=invite_id,
                    disconnected_id=pid,
                )
        party_id = self._player_to_party.pop(pid, None)
        if party_id is None:
            return
        party = self._parties.get(party_id)
        if not party:
            return
        party.member_ids.discard(pid)
        if party.leader_id == pid:
            member_ids_snapshot = list(party.member_ids)
            for mid in list(party.member_ids):
                self._player_to_party.pop(mid, None)
            del self._parties[party_id]
            self._emit_party_updated(party_id, pid, member_ids_snapshot, "disbanded")
            self._logger.info("Party disbanded on leader disconnect", party_id=party_id, leader_id=pid)
        elif not party.member_ids:
            del self._parties[party_id]
            self._logger.debug("Party removed (empty after disconnect)", party_id=party_id)
        else:
            self._emit_party_updated(party_id, party.leader_id, list(party.member_ids), "member_left")
        self._logger.debug("Cleaned up party state for disconnected player", player_id=pid)
