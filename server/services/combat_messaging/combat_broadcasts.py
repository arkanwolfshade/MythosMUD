"""Combat event broadcasts (start, attack, death, end, error, target switch)."""

from typing import Any, cast

from server.realtime.envelope import build_event
from server.services.combat_messaging.base import HasConnectionManager
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

    async def broadcast_combat_start(
        self, room_id: str, attacker_name: str, target_name: str, combat_id: str
    ) -> dict[str, Any]:
        """Broadcast combat start message to all players in the room."""
        logger.info(
            "Broadcasting combat start",
            room_id=room_id,
            attacker_name=attacker_name,
            target_name=target_name,
            combat_id=combat_id,
        )
        messages = {
            "attack_attacker": f"You attack {target_name}!",
            "attack_defender": f"{attacker_name} attacks you!",
            "attack_other": f"{attacker_name} attacks {target_name}!",
        }
        combat_start_event = build_event(
            "combat_started",
            {"combat_id": combat_id, "attacker_name": attacker_name, "target_name": target_name, "messages": messages},
            room_id=room_id,
        )
        broadcast_stats = await self.connection_manager.broadcast_to_room(room_id, combat_start_event)
        logger.debug(
            "Combat start broadcast completed", room_id=room_id, combat_id=combat_id, broadcast_stats=broadcast_stats
        )
        return cast(dict[str, Any], broadcast_stats)

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
        logger.debug(
            "Combat attack broadcast completed",
            room_id=room_id,
            combat_id=combat_id,
            broadcast_stats=broadcast_stats,
        )
        return cast(dict[str, Any], broadcast_stats)

    async def broadcast_combat_death(
        self, room_id: str, npc_name: str, xp_reward: int, combat_id: str
    ) -> dict[str, Any]:
        """Broadcast NPC death message to all players in the room."""
        logger.info(
            "Broadcasting combat death",
            room_id=room_id,
            npc_name=npc_name,
            xp_reward=xp_reward,
            combat_id=combat_id,
        )
        messages = {
            "death_message": f"{npc_name} dies.",
            "xp_reward": f"You gain {xp_reward} experience points.",
        }
        death_event = build_event(
            "combat_death",
            {"combat_id": combat_id, "npc_name": npc_name, "xp_reward": xp_reward, "messages": messages},
            room_id=room_id,
        )
        broadcast_stats = await self.connection_manager.broadcast_to_room(room_id, death_event)
        logger.debug(
            "Combat death broadcast completed", room_id=room_id, combat_id=combat_id, broadcast_stats=broadcast_stats
        )
        return cast(dict[str, Any], broadcast_stats)

    async def broadcast_combat_end(self, room_id: str, combat_id: str, reason: str = "combat_ended") -> dict[str, Any]:
        """Broadcast combat end message to all players in the room."""
        logger.info("Broadcasting combat end", room_id=room_id, combat_id=combat_id, reason=reason)
        messages = {"combat_end": f"Combat ends. ({reason})"}
        combat_end_event = build_event(
            "combat_ended",
            {"combat_id": combat_id, "reason": reason, "messages": messages},
            room_id=room_id,
        )
        broadcast_stats = await self.connection_manager.broadcast_to_room(room_id, combat_end_event)
        logger.debug(
            "Combat end broadcast completed", room_id=room_id, combat_id=combat_id, broadcast_stats=broadcast_stats
        )
        return cast(dict[str, Any], broadcast_stats)

    async def broadcast_combat_error(self, room_id: str, error_message: str, player_id: str) -> dict[str, Any]:
        """Broadcast combat error message to a specific player."""
        logger.info("Broadcasting combat error", room_id=room_id, player_id=player_id, error_message=error_message)
        error_event = build_event(
            "combat_error",
            {"error_message": error_message},
            room_id=room_id,
            player_id=player_id,
        )
        try:
            delivery_status = await self.connection_manager.send_personal_message(player_id, error_event)
        except (ConnectionError, OSError, RuntimeError, ValueError) as e:
            logger.warning("Failed to send combat error message to player", player_id=player_id, error=str(e))
            delivery_status = {"success": False, "error": str(e)}
        logger.debug(
            "Combat error broadcast completed", room_id=room_id, player_id=player_id, delivery_status=delivery_status
        )
        return cast(dict[str, Any], delivery_status)

    async def broadcast_combat_target_switch(
        self, room_id: str, combat_id: str, npc_name: str, new_target_name: str
    ) -> dict[str, Any]:
        """Broadcast one short room message when an NPC switches aggro target (ADR-016)."""
        room_message = f"{npc_name} turns its gaze to {new_target_name}."
        event = build_event(
            "combat_target_switch",
            {"combat_id": combat_id, "npc_name": npc_name, "new_target_name": new_target_name, "message": room_message},
            room_id=room_id,
        )
        broadcast_stats = await self.connection_manager.broadcast_to_room(room_id, event)
        logger.debug(
            "Combat target switch broadcast",
            room_id=room_id,
            combat_id=combat_id,
            npc_name=npc_name,
            new_target_name=new_target_name,
        )
        return cast(dict[str, Any], broadcast_stats)
