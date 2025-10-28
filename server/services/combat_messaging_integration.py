"""
Combat messaging integration with real-time messaging system.

This service integrates combat messages with the existing real-time messaging
infrastructure to broadcast combat events to all players in a room.

As noted in the Pnakotic Manuscripts, the transmission of forbidden knowledge
must reach all who bear witness to the cosmic horror unfolding.
"""

from typing import Any

from server.logging.enhanced_logging_config import get_logger
from server.realtime.connection_manager import connection_manager
from server.realtime.envelope import build_event
from server.services.combat_messaging_service import CombatMessagingService

logger = get_logger(__name__)


class CombatMessagingIntegration:
    """
    Integrates combat messaging with the real-time messaging system.

    This service handles broadcasting combat messages to all players in a room
    using the existing real-time messaging infrastructure.
    """

    def __init__(self):
        """Initialize the combat messaging integration service."""
        self.messaging_service = CombatMessagingService()

    async def broadcast_combat_start(
        self,
        room_id: str,
        attacker_name: str,
        target_name: str,
        combat_id: str,
    ) -> dict[str, Any]:
        """
        Broadcast combat start message to all players in the room.

        Args:
            room_id: The room where combat is starting
            attacker_name: Name of the attacking player
            target_name: Name of the target NPC
            combat_id: Unique combat identifier

        Returns:
            dict: Broadcast delivery statistics
        """
        logger.info(
            "Broadcasting combat start",
            room_id=room_id,
            attacker_name=attacker_name,
            target_name=target_name,
            combat_id=combat_id,
        )

        # Generate combat start messages for different perspectives
        # For now, we'll create simple messages since we don't have room occupants
        messages = {
            "attack_attacker": f"You attack {target_name}!",
            "attack_defender": f"{attacker_name} attacks you!",
            "attack_other": f"{attacker_name} attacks {target_name}!",
        }

        # Create combat start event
        combat_start_event = build_event(
            "combat_started",
            {
                "combat_id": combat_id,
                "attacker_name": attacker_name,
                "target_name": target_name,
                "messages": messages,
            },
            room_id=room_id,
        )

        # Broadcast to all players in the room
        broadcast_stats = await connection_manager.broadcast_to_room(room_id, combat_start_event)

        logger.debug(
            "Combat start broadcast completed",
            room_id=room_id,
            combat_id=combat_id,
            broadcast_stats=broadcast_stats,
        )

        return broadcast_stats

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
        """
        Broadcast combat attack message to all players in the room.

        Args:
            room_id: The room where combat is happening
            attacker_name: Name of the attacking player
            target_name: Name of the target NPC
            damage: Damage dealt
            action_type: Type of attack (punch, kick, etc.)
            combat_id: Unique combat identifier
            attacker_id: ID of the attacking player (for exclusion)

        Returns:
            dict: Broadcast delivery statistics
        """
        logger.info(
            "Broadcasting combat attack",
            room_id=room_id,
            attacker_name=attacker_name,
            target_name=target_name,
            damage=damage,
            action_type=action_type,
            combat_id=combat_id,
        )

        # Generate attack messages for different perspectives
        messages = {
            "attack_attacker": (f"You {action_type} {target_name} for {damage} damage."),
            "attack_defender": (f"{attacker_name} {action_type}s you for {damage} damage."),
            "attack_other": (f"{attacker_name} {action_type}s {target_name} for {damage} damage."),
        }

        # Create attack event
        attack_event = build_event(
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

        # Broadcast to all players in the room (excluding attacker)
        broadcast_stats = await connection_manager.broadcast_to_room(room_id, attack_event, exclude_player=attacker_id)

        # Send personal message to the attacker
        personal_message = messages.get(
            "attack_attacker",
            f"You {action_type} {target_name} for {damage} damage.",
        )
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
            await connection_manager.send_personal_message(attacker_id, personal_event)
        except Exception as e:
            logger.warning(
                "Failed to send personal combat message to attacker",
                attacker_id=attacker_id,
                error=str(e),
            )

        logger.debug(
            "Combat attack broadcast completed",
            room_id=room_id,
            combat_id=combat_id,
            broadcast_stats=broadcast_stats,
        )

        return broadcast_stats

    async def broadcast_combat_death(
        self,
        room_id: str,
        npc_name: str,
        xp_reward: int,
        combat_id: str,
    ) -> dict[str, Any]:
        """
        Broadcast NPC death message to all players in the room.

        Args:
            room_id: The room where the NPC died
            npc_name: Name of the NPC that died
            xp_reward: XP reward for killing the NPC
            combat_id: Unique combat identifier

        Returns:
            dict: Broadcast delivery statistics
        """
        logger.info(
            "Broadcasting combat death",
            room_id=room_id,
            npc_name=npc_name,
            xp_reward=xp_reward,
            combat_id=combat_id,
        )

        # Generate death messages
        messages = {
            "death_message": f"{npc_name} dies.",
            "xp_reward": f"You gain {xp_reward} experience points.",
        }

        # Create death event
        death_event = build_event(
            "combat_death",
            {
                "combat_id": combat_id,
                "npc_name": npc_name,
                "xp_reward": xp_reward,
                "messages": messages,
            },
            room_id=room_id,
        )

        # Broadcast to all players in the room
        broadcast_stats = await connection_manager.broadcast_to_room(room_id, death_event)

        logger.debug(
            "Combat death broadcast completed",
            room_id=room_id,
            combat_id=combat_id,
            broadcast_stats=broadcast_stats,
        )

        return broadcast_stats

    async def broadcast_combat_end(
        self,
        room_id: str,
        combat_id: str,
        reason: str = "combat_ended",
    ) -> dict[str, Any]:
        """
        Broadcast combat end message to all players in the room.

        Args:
            room_id: The room where combat ended
            combat_id: Unique combat identifier
            reason: Reason for combat ending

        Returns:
            dict: Broadcast delivery statistics
        """
        logger.info(
            "Broadcasting combat end",
            room_id=room_id,
            combat_id=combat_id,
            reason=reason,
        )

        # Generate combat end messages
        messages = {
            "combat_end": f"Combat ends. ({reason})",
        }

        # Create combat end event
        combat_end_event = build_event(
            "combat_ended",
            {
                "combat_id": combat_id,
                "reason": reason,
                "messages": messages,
            },
            room_id=room_id,
        )

        # Broadcast to all players in the room
        broadcast_stats = await connection_manager.broadcast_to_room(room_id, combat_end_event)

        logger.debug(
            "Combat end broadcast completed",
            room_id=room_id,
            combat_id=combat_id,
            broadcast_stats=broadcast_stats,
        )

        return broadcast_stats

    async def broadcast_combat_error(
        self,
        room_id: str,
        error_message: str,
        player_id: str,
    ) -> dict[str, Any]:
        """
        Broadcast combat error message to a specific player.

        Args:
            room_id: The room where the error occurred
            error_message: Error message to display
            player_id: ID of the player to send the error to

        Returns:
            dict: Message delivery status
        """
        logger.info(
            "Broadcasting combat error",
            room_id=room_id,
            player_id=player_id,
            error_message=error_message,
        )

        # Create error event
        error_event = build_event(
            "combat_error",
            {
                "error_message": error_message,
            },
            room_id=room_id,
            player_id=player_id,
        )

        # Send personal message to the player
        delivery_status = await connection_manager.send_personal_message(player_id, error_event)

        logger.debug(
            "Combat error broadcast completed",
            room_id=room_id,
            player_id=player_id,
            delivery_status=delivery_status,
        )

        return delivery_status

    async def broadcast_player_mortally_wounded(
        self,
        player_id: str,
        player_name: str,
        attacker_name: str | None,
        room_id: str,
    ) -> dict[str, Any]:
        """
        Broadcast player mortally wounded message to all players in the room.

        Args:
            player_id: ID of the mortally wounded player
            player_name: Name of the mortally wounded player
            attacker_name: Name of the attacker (if applicable)
            room_id: Room where the player became mortally wounded

        Returns:
            dict: Broadcast delivery statistics
        """
        logger.info(
            "Broadcasting player mortally wounded",
            player_id=player_id,
            player_name=player_name,
            attacker_name=attacker_name,
            room_id=room_id,
        )

        # Generate messages
        if attacker_name:
            personal_message = (
                f"{attacker_name}'s attack causes you to collapse as darkness begins closing in on your vision"
            )
            room_message = f"{player_name} collapses from {attacker_name}'s attack and is on the verge of death!"
        else:
            personal_message = "You collapse as darkness begins closing in on your vision"
            room_message = f"{player_name} collapses and is on the verge of death!"

        # Create event for the mortally wounded player
        personal_event = build_event(
            "player_mortally_wounded",
            {
                "player_id": player_id,
                "player_name": player_name,
                "attacker_name": attacker_name,
                "message": personal_message,
            },
            room_id=room_id,
            player_id=player_id,
        )

        # Create event for other players in room
        room_event = build_event(
            "player_mortally_wounded_room",
            {
                "player_id": player_id,
                "player_name": player_name,
                "attacker_name": attacker_name,
                "message": room_message,
            },
            room_id=room_id,
        )

        # Send personal message to the player
        try:
            await connection_manager.send_personal_message(player_id, personal_event)
        except Exception as e:
            logger.warning("Failed to send mortally wounded message to player", player_id=player_id, error=str(e))

        # Broadcast to all other players in the room
        broadcast_stats = await connection_manager.broadcast_to_room(room_id, room_event, exclude_player=player_id)

        logger.debug("Player mortally wounded broadcast completed", room_id=room_id, broadcast_stats=broadcast_stats)

        return broadcast_stats

    async def broadcast_player_death(
        self,
        player_id: str,
        player_name: str,
        room_id: str,
        death_location: str,
    ) -> dict[str, Any]:
        """
        Broadcast player death message to all players in the room.

        Args:
            player_id: ID of the dead player
            player_name: Name of the dead player
            room_id: Room where the player died
            death_location: Detailed death location information

        Returns:
            dict: Broadcast delivery statistics
        """
        logger.info(
            "Broadcasting player death",
            player_id=player_id,
            player_name=player_name,
            room_id=room_id,
            death_location=death_location,
        )

        # Generate messages
        personal_message = "You exhale your last breath."
        room_message = f"{player_name} exhales their last breath."

        # Create event for the dead player
        personal_event = build_event(
            "player_died",
            {
                "player_id": player_id,
                "player_name": player_name,
                "death_location": death_location,
                "message": personal_message,
            },
            room_id=room_id,
            player_id=player_id,
        )

        # Create event for other players in room
        room_event = build_event(
            "player_died_room",
            {
                "player_id": player_id,
                "player_name": player_name,
                "message": room_message,
            },
            room_id=room_id,
        )

        # Send personal message to the player
        try:
            await connection_manager.send_personal_message(player_id, personal_event)
        except Exception as e:
            logger.warning("Failed to send death message to player", player_id=player_id, error=str(e))

        # Broadcast to all other players in the room
        broadcast_stats = await connection_manager.broadcast_to_room(room_id, room_event, exclude_player=player_id)

        logger.debug("Player death broadcast completed", room_id=room_id, broadcast_stats=broadcast_stats)

        return broadcast_stats

    async def broadcast_player_respawn(
        self,
        player_id: str,
        player_name: str,
        room_id: str,
    ) -> dict[str, Any]:
        """
        Broadcast player respawn message to all players in the room.

        Args:
            player_id: ID of the respawned player
            player_name: Name of the respawned player
            room_id: Room where the player respawned

        Returns:
            dict: Broadcast delivery statistics
        """
        logger.info("Broadcasting player respawn", player_id=player_id, player_name=player_name, room_id=room_id)

        # Generate messages
        personal_message = "You open your eyes and awaken from your coma."
        room_message = f"Patient {player_name} opens their eyes and awakens from their coma."

        # Create event for the respawned player
        personal_event = build_event(
            "player_respawned",
            {
                "player_id": player_id,
                "player_name": player_name,
                "message": personal_message,
            },
            room_id=room_id,
            player_id=player_id,
        )

        # Create event for other players in room
        room_event = build_event(
            "player_respawned_room",
            {
                "player_id": player_id,
                "player_name": player_name,
                "message": room_message,
            },
            room_id=room_id,
        )

        # Send personal message to the player
        try:
            await connection_manager.send_personal_message(player_id, personal_event)
        except Exception as e:
            logger.warning("Failed to send respawn message to player", player_id=player_id, error=str(e))

        # Broadcast to all other players in the room
        broadcast_stats = await connection_manager.broadcast_to_room(room_id, room_event, exclude_player=player_id)

        logger.debug("Player respawn broadcast completed", room_id=room_id, broadcast_stats=broadcast_stats)

        return broadcast_stats

    async def send_hp_decay_message(
        self,
        player_id: str,
        current_hp: int,
    ) -> dict[str, Any]:
        """
        Send HP decay message to a specific mortally wounded player.

        Args:
            player_id: ID of the player losing HP
            current_hp: Current HP after decay

        Returns:
            dict: Message delivery status
        """
        logger.debug("Sending HP decay message", player_id=player_id, current_hp=current_hp)

        # Generate message
        message = f"Your lifeforce ebbs away... (HP: {current_hp})"

        # Create event for the player
        decay_event = build_event(
            "player_hp_decay",
            {
                "player_id": player_id,
                "current_hp": current_hp,
                "message": message,
            },
            player_id=player_id,
        )

        # Send personal message to the player
        try:
            delivery_status = await connection_manager.send_personal_message(player_id, decay_event)
        except Exception as e:
            logger.warning("Failed to send HP decay message to player", player_id=player_id, error=str(e))
            delivery_status = {"success": False, "error": str(e)}

        logger.debug("HP decay message sent", player_id=player_id, delivery_status=delivery_status)

        return delivery_status


# Global combat messaging integration instance
combat_messaging_integration = CombatMessagingIntegration()
