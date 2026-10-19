"""Combat event broadcasts (start, attack, death, end, error, target switch, NPC disengage)."""

import uuid
from typing import Any, Protocol, cast

from server.constants.message_category import MessageCategory
from server.constants.message_segments import SegmentPart, message_with_segments, npc_name_segment
from server.constants.npc_disposition import NpcDisposition
from server.realtime.envelope import build_event
from server.services.combat_messaging.base import HasConnectionManager, log_room_broadcast_result
from server.structured_logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)


class _PersonalSender(Protocol):  # pylint: disable=too-few-public-methods  # Reason: Protocol stub
    """The one ConnectionManager method the target-switch line needs (connection_manager is untyped on the mixin)."""

    async def send_personal_message(self, player_id: uuid.UUID | str, event: dict[str, object]) -> object:
        """Send one event to one player."""
        ...  # pylint: disable=unnecessary-ellipsis  # Reason: basedpyright requires an explicit stub body for a non-None Protocol return type


def _npc_part(name: str, disposition: NpcDisposition | None) -> SegmentPart:
    """An NPC's name as a line part: styled when its disposition is known, plain text otherwise (#1036)."""
    return npc_name_segment(name, disposition) if disposition is not None else name


def _line_fields(parts: list[SegmentPart]) -> dict[str, object]:
    """``message`` for a line built from parts, plus ``segments`` only when something in it is styled."""
    built = message_with_segments(parts)
    styled = any("category" in segment for segment in built["segments"])
    return {"message": built["message"], **({"segments": built["segments"]} if styled else {})}


class CombatBroadcastMixin(HasConnectionManager):
    """Mixin for combat-related broadcast methods. Requires connection_manager on self."""

    def _build_combat_attack_messages(
        self, action_type: str, attacker_name: str, target_name: str, damage: int
    ) -> dict[str, str]:
        """Build perspective-specific attack messages."""
        return {
            "attack_attacker": f"You {action_type} {target_name} for {damage} damage.",
            "attack_defender": f"{attacker_name} {action_type}s you for {damage} damage.",
            "attack_other": f"{attacker_name} {action_type}s {target_name} for {damage} damage.",
        }

    def _build_combat_attack_categories(self) -> dict[str, str]:
        """
        Category of each perspective line in ``messages``, from that recipient's point of view.

        The room event reaches both the defender and bystanders, so it carries one category per
        ``messages`` key instead of a single ``category``: the defender is hurt, a bystander sees a hit.
        """
        return {
            "attack_attacker": MessageCategory.COMBAT_HIT.value,
            "attack_defender": MessageCategory.COMBAT_HURT.value,
            "attack_other": MessageCategory.COMBAT_HIT.value,
        }

    def _build_combat_attack_event(
        self,
        room_id: str,
        combat_id: str,
        attacker_name: str,
        target_name: str,
        damage: int,
        action_type: str,
        messages: dict[str, str],
    ) -> dict[str, Any]:
        """Build combat_attack event payload."""
        return build_event(
            "combat_attack",
            {
                "combat_id": combat_id,
                "attacker_name": attacker_name,
                "target_name": target_name,
                "damage": damage,
                "action_type": action_type,
                "messages": messages,
                "categories": self._build_combat_attack_categories(),
            },
            room_id=room_id,
        )

    async def _send_attacker_personal_combat_message(
        self,
        attacker_id: str,
        room_id: str,
        combat_id: str,
        target_name: str,
        damage: int,
        action_type: str,
        personal_message: str,
    ) -> None:
        """Send personal combat message to attacker. Logs warning on failure."""
        personal_event = build_event(
            "combat_attack_personal",
            {
                "combat_id": combat_id,
                "target_name": target_name,
                "damage": damage,
                "action_type": action_type,
                "message": personal_message,
                "category": MessageCategory.COMBAT_HIT.value,
            },
            room_id=room_id,
            player_id=attacker_id,
        )
        try:
            await self.connection_manager.send_personal_message(attacker_id, personal_event)
        except (ConnectionError, OSError, RuntimeError, ValueError) as e:
            logger.warning(
                "Failed to send personal combat message to attacker",
                attacker_id=attacker_id,
                error=str(e),
            )

    async def _send_attacker_personal_message_if_needed(
        self,
        attacker_id: str,
        messages: dict[str, str],
        room_id: str,
        combat_id: str,
        target_name: str,
        damage: int,
        action_type: str,
    ) -> None:
        """Send personal combat message to attacker when attacker_id is present."""
        if not attacker_id:
            return
        personal_message = messages.get("attack_attacker", f"You {action_type} {target_name} for {damage} damage.")
        await self._send_attacker_personal_combat_message(
            attacker_id, room_id, combat_id, target_name, damage, action_type, personal_message
        )

    async def broadcast_combat_attack(
        self,
        room_id: str,
        attacker_name: str,
        target_name: str,
        damage: int,
        action_type: str,
        combat_id: str,
        attacker_id: str,
    ) -> dict[str, Any]:
        """Broadcast combat attack to room. Excludes attacker from broadcast; sends them a personal message."""
        logger.info(
            "Broadcasting combat attack",
            room_id=room_id,
            attacker_name=attacker_name,
            target_name=target_name,
            damage=damage,
            action_type=action_type,
            combat_id=combat_id,
        )
        messages = self._build_combat_attack_messages(action_type, attacker_name, target_name, damage)
        attack_event = self._build_combat_attack_event(
            room_id, combat_id, attacker_name, target_name, damage, action_type, messages
        )
        broadcast_stats = await self.connection_manager.broadcast_to_room(
            room_id, attack_event, exclude_player=attacker_id
        )
        await self._send_attacker_personal_message_if_needed(
            attacker_id, messages, room_id, combat_id, target_name, damage, action_type
        )
        log_room_broadcast_result("Combat attack broadcast", room_id, cast(dict[str, Any], broadcast_stats))
        return cast(dict[str, Any], broadcast_stats)

    async def _broadcast_combat_event(
        self,
        event_type: str,
        room_id: str,
        data: dict[str, object],
        label: str,
        category: MessageCategory,
        exclude_player: str | None = None,
    ) -> dict[str, object]:
        """Build one combat event tagged with its message category and send it to the room, optionally skipping one player."""
        event = build_event(event_type, {**data, "category": category.value}, room_id=room_id)
        broadcast_stats = await self.connection_manager.broadcast_to_room(room_id, event, exclude_player=exclude_player)
        stats = cast(dict[str, object], broadcast_stats)
        log_room_broadcast_result(label, room_id, stats)
        return stats

    async def broadcast_combat_target_switch(
        self,
        room_id: str,
        combat_id: str,
        npc_name: str,
        new_target_name: str,
        npc_disposition: NpcDisposition | None = None,
        new_target_player_id: str | None = None,
    ) -> dict[str, object]:
        """
        Broadcast one short room message when an NPC switches aggro target (ADR-016).

        When the new target is a player, they are told "turns its gaze to you" and the rest of the room
        reads their name: each viewer sees the line from their own point of view.
        """
        npc_part = _npc_part(npc_name, npc_disposition)
        line = _line_fields([npc_part, f" turns its gaze to {new_target_name}."])
        stats = await self._broadcast_combat_event(
            "combat_target_switch",
            room_id,
            {"combat_id": combat_id, "npc_name": npc_name, "new_target_name": new_target_name, **line},
            "Combat target switch broadcast",
            MessageCategory.COMBAT_STATUS,
            exclude_player=new_target_player_id,
        )
        if new_target_player_id:
            personal = build_event(
                "combat_target_switch",
                {
                    "combat_id": combat_id,
                    "npc_name": npc_name,
                    "new_target_name": new_target_name,
                    **_line_fields([npc_part, " turns its gaze to you."]),
                    "category": MessageCategory.COMBAT_STATUS.value,
                },
                room_id=room_id,
                player_id=new_target_player_id,
            )
            try:
                sender = cast(_PersonalSender, self.connection_manager)
                _ = await sender.send_personal_message(new_target_player_id, personal)
            except (ConnectionError, OSError, RuntimeError, ValueError) as e:
                logger.warning(
                    "Failed to send personal target switch message", player_id=new_target_player_id, error=str(e)
                )
        return stats

    async def broadcast_npc_disengage(
        self,
        room_id: str,
        combat_id: str,
        npc_name: str,
        clause: str,
        npc_disposition: NpcDisposition | None = None,
    ) -> dict[str, object]:
        """Broadcast one room line when an NPC breaks off a fight: its name, then ``clause`` (e.g. "withdraws.")."""
        line = _line_fields([_npc_part(npc_name, npc_disposition), f" {clause}"])
        return await self._broadcast_combat_event(
            "combat_npc_disengage",
            room_id,
            {"combat_id": combat_id, "npc_name": npc_name, **line},
            "NPC disengage broadcast",
            MessageCategory.COMBAT_STATUS,
        )

    async def broadcast_player_joined_combat(
        self,
        room_id: str,
        combat_id: str,
        player_name: str,
        npc_name: str,
        player_id: str,
        npc_disposition: NpcDisposition | None = None,
    ) -> dict[str, object]:
        """Broadcast one room line when a player joins a fight already under way (#833). The joiner is excluded."""
        line = _line_fields([f"{player_name} joins the fight against ", _npc_part(npc_name, npc_disposition), "!"])
        return await self._broadcast_combat_event(
            "combat_participant_joined",
            room_id,
            {"combat_id": combat_id, "player_name": player_name, "npc_name": npc_name, **line},
            "Combat join broadcast",
            MessageCategory.COMBAT_STATUS,
            exclude_player=player_id,
        )

    async def broadcast_taunt_result(
        self, room_id: str, combat_id: str, line: str | list[SegmentPart]
    ) -> dict[str, object]:
        """Broadcast the one room line for a resolved taunt: success, failure or fumble (#833)."""
        parts: list[SegmentPart] = [line] if isinstance(line, str) else line
        return await self._broadcast_combat_event(
            "combat_taunt",
            room_id,
            {"combat_id": combat_id, **_line_fields(parts)},
            "Combat taunt broadcast",
            MessageCategory.COMBAT_STATUS,
        )

    async def broadcast_protect_result(self, room_id: str, combat_id: str, message: str) -> dict[str, object]:
        """Broadcast one room line for a protect: its cast result, or one hit the cover redirected (#991)."""
        return await self._broadcast_combat_event(
            "combat_protect",
            room_id,
            {"combat_id": combat_id, "message": message},
            "Combat protect broadcast",
            MessageCategory.COMBAT_STATUS,
        )
