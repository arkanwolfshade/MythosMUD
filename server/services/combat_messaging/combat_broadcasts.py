"""Combat event broadcasts (start, attack, death, end, error, target switch)."""

from typing import Any, cast

from server.realtime.envelope import build_event
from server.services.combat_messaging.base import HasConnectionManager, log_room_broadcast_result
from server.structured_logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)


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
        exclude_player: str | None = None,
    ) -> dict[str, object]:
        """Build one combat event and send it to the room, optionally skipping one player."""
        event = build_event(event_type, data, room_id=room_id)
        broadcast_stats = await self.connection_manager.broadcast_to_room(room_id, event, exclude_player=exclude_player)
        stats = cast(dict[str, object], broadcast_stats)
        log_room_broadcast_result(label, room_id, stats)
        return stats

    async def broadcast_combat_target_switch(
        self, room_id: str, combat_id: str, npc_name: str, new_target_name: str
    ) -> dict[str, object]:
        """Broadcast one short room message when an NPC switches aggro target (ADR-016)."""
        room_message = f"{npc_name} turns its gaze to {new_target_name}."
        return await self._broadcast_combat_event(
            "combat_target_switch",
            room_id,
            {"combat_id": combat_id, "npc_name": npc_name, "new_target_name": new_target_name, "message": room_message},
            "Combat target switch broadcast",
        )

    async def broadcast_player_joined_combat(
        self, room_id: str, combat_id: str, player_name: str, npc_name: str, player_id: str
    ) -> dict[str, object]:
        """Broadcast one room line when a player joins a fight already under way (#833). The joiner is excluded."""
        return await self._broadcast_combat_event(
            "combat_participant_joined",
            room_id,
            {
                "combat_id": combat_id,
                "player_name": player_name,
                "npc_name": npc_name,
                "message": f"{player_name} joins the fight against {npc_name}!",
            },
            "Combat join broadcast",
            exclude_player=player_id,
        )

    async def broadcast_taunt_result(self, room_id: str, combat_id: str, message: str) -> dict[str, object]:
        """Broadcast the one room line for a resolved taunt: success, failure or fumble (#833)."""
        return await self._broadcast_combat_event(
            "combat_taunt",
            room_id,
            {"combat_id": combat_id, "message": message},
            "Combat taunt broadcast",
        )

    async def broadcast_protect_result(self, room_id: str, combat_id: str, message: str) -> dict[str, object]:
        """Broadcast one room line for a protect: its cast result, or one hit the cover redirected (#991)."""
        return await self._broadcast_combat_event(
            "combat_protect",
            room_id,
            {"combat_id": combat_id, "message": message},
            "Combat protect broadcast",
        )
