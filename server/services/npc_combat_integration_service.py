"""
NPC Combat Integration Service for MythosMUD.

This service provides integration between NPCs and the combat system,
including combat memory management and basic combat interactions.

As documented in the Cultes des Goules, proper combat integration is essential
for maintaining the balance between mortal investigators and the eldritch
entities they encounter in our world.
"""

import time
from typing import Any
from uuid import UUID, uuid4

from ..events.combat_events import (
    NPCDiedEvent,
    NPCTookDamageEvent,
    PlayerAttackedEvent,
)
from ..events.event_bus import EventBus
from ..logging_config import get_logger
from ..persistence import get_persistence
from .combat_event_publisher import CombatEventPublisher
from .combat_messaging_integration import CombatMessagingIntegration
from .combat_service import CombatService

logger = get_logger(__name__)


class NPCCombatIntegrationService:
    """
    Service for integrating NPCs with the combat system.

    This service handles:
    - NPC combat memory management
    - Basic combat interactions
    - Event publishing and messaging
    """

    def __init__(self, event_bus: EventBus | None = None):
        """
        Initialize the NPC combat integration service.

        Args:
            event_bus: Optional EventBus instance. If None, will get the
                global instance.
        """
        self.event_bus = event_bus or EventBus()
        self._persistence = get_persistence(event_bus)
        self._combat_service = CombatService()
        self._messaging_integration = CombatMessagingIntegration()
        self._event_publisher = CombatEventPublisher(event_bus)

        # NPC combat memory - tracks last attacker for each NPC instance
        self._npc_combat_memory: dict[str, str] = {}

        logger.info("NPC Combat Integration Service initialized")

    def handle_player_attack_on_npc(
        self,
        player_id: str,
        npc_id: str,
        room_id: str,
        action_type: str = "punch",
        damage: int = 1,
    ) -> bool:
        """
        Handle a player attacking an NPC.

        Args:
            player_id: ID of the attacking player
            npc_id: ID of the target NPC
            room_id: ID of the room where combat occurs
            action_type: Type of attack action
            damage: Damage amount

        Returns:
            bool: True if attack was handled successfully
        """
        try:
            # Check if NPC is alive
            npc_instance = self._get_npc_instance(npc_id)
            if not npc_instance or not npc_instance.is_alive:
                logger.warning(
                    "Player attacked dead or non-existent NPC",
                    player_id=player_id,
                    npc_id=npc_id,
                )
                return False

            # Store combat memory - NPC remembers who attacked it
            self._npc_combat_memory[npc_id] = player_id

            # Apply damage to NPC
            damage_applied = npc_instance.take_damage(damage, "physical", player_id)
            if not damage_applied:
                logger.error(
                    "Failed to apply damage to NPC",
                    npc_id=npc_id,
                    damage=damage,
                )
                return False

            # Create a simple combat ID for tracking
            combat_id = str(uuid4())

            # Publish combat events
            self._event_publisher.publish_player_attacked(
                PlayerAttackedEvent(
                    event_type="player_attacked",
                    timestamp=time.time(),
                    combat_id=UUID(combat_id),
                    room_id=room_id,
                    attacker_id=UUID(player_id),
                    attacker_name=self._get_player_name(player_id),
                    target_id=UUID(npc_id),
                    target_name=npc_instance.name,
                    damage=damage,
                    action_type=action_type,
                )
            )

            self._event_publisher.publish_npc_took_damage(
                NPCTookDamageEvent(
                    event_type="npc_took_damage",
                    timestamp=time.time(),
                    combat_id=UUID(combat_id),
                    room_id=room_id,
                    npc_id=UUID(npc_id),
                    npc_name=npc_instance.name,
                    damage=damage,
                    current_hp=getattr(npc_instance, "_stats", {}).get("hp", 0),
                    max_hp=getattr(npc_instance, "_stats", {}).get("max_hp", 100),
                )
            )

            # Broadcast attack message
            self._messaging_integration.broadcast_combat_attack(
                room_id=room_id,
                attacker_name=self._get_player_name(player_id),
                target_name=npc_instance.name,
                damage=damage,
                action_type=action_type,
                combat_id=combat_id,
                attacker_id=player_id,
            )

            # Check if NPC died
            if not npc_instance.is_alive:
                self.handle_npc_death(npc_id, room_id, player_id, combat_id)

            logger.info(
                "Player attack on NPC handled",
                player_id=player_id,
                npc_id=npc_id,
                damage=damage,
                npc_alive=npc_instance.is_alive,
            )

            return True

        except Exception as e:
            logger.error(
                "Error handling player attack on NPC",
                player_id=player_id,
                npc_id=npc_id,
                error=str(e),
            )
            return False

    def handle_npc_death(
        self,
        npc_id: str,
        room_id: str,
        killer_id: str | None = None,
        combat_id: str | None = None,
    ) -> bool:
        """
        Handle NPC death and related effects.

        Args:
            npc_id: ID of the dead NPC
            room_id: ID of the room where death occurred
            killer_id: ID of the entity that killed the NPC
            combat_id: ID of the combat if applicable

        Returns:
            bool: True if death was handled successfully
        """
        try:
            # Get NPC instance
            npc_instance = self._get_npc_instance(npc_id)
            if not npc_instance:
                logger.warning(
                    "Attempted to handle death for non-existent NPC",
                    npc_id=npc_id,
                )
                return False

            # Get NPC definition for XP reward
            npc_definition = self._get_npc_definition(npc_id)
            xp_reward = 0
            if npc_definition:
                base_stats = npc_definition.base_stats
                if isinstance(base_stats, dict):
                    xp_reward = base_stats.get("xp_reward", 0)
                else:
                    xp_reward = 0

            # Award XP to killer if it's a player
            if killer_id and xp_reward > 0:
                player = self._persistence.get_player(killer_id)
                if player:
                    # Award XP using game mechanics service
                    try:
                        # Try to get game mechanics service from persistence
                        if hasattr(self._persistence, "get_game_mechanics_service"):
                            game_mechanics = self._persistence.get_game_mechanics_service()
                            if game_mechanics:
                                success, _ = game_mechanics.gain_experience(killer_id, xp_reward, f"killed_{npc_id}")
                                if success:
                                    logger.info(
                                        "Awarded XP to player",
                                        player_id=killer_id,
                                        xp_reward=xp_reward,
                                        npc_id=npc_id,
                                    )
                                else:
                                    logger.warning(
                                        "Failed to award XP to player",
                                        player_id=killer_id,
                                        xp_reward=xp_reward,
                                    )
                        else:
                            # Fallback: directly update player experience
                            player.stats.experience_points += xp_reward
                            self._persistence.save_player(player)
                            logger.info(
                                "Awarded XP to player (fallback)",
                                player_id=killer_id,
                                xp_reward=xp_reward,
                                npc_id=npc_id,
                            )
                    except Exception as e:
                        logger.error(
                            "Error awarding XP to player",
                            player_id=killer_id,
                            error=str(e),
                        )

            # Publish death event
            self._event_publisher.publish_npc_died(
                NPCDiedEvent(
                    event_type="npc_died",
                    timestamp=time.time(),
                    combat_id=UUID(combat_id) if combat_id else UUID(uuid4()),
                    room_id=room_id,
                    npc_id=UUID(npc_id),
                    npc_name=npc_instance.name,
                    xp_reward=xp_reward,
                )
            )

            # Broadcast death message
            self._messaging_integration.broadcast_combat_death(
                room_id=room_id,
                npc_name=npc_instance.name,
                xp_reward=xp_reward,
                combat_id=combat_id or "",
            )

            # Clear combat memory for this NPC
            if str(npc_id) in self._npc_combat_memory:
                del self._npc_combat_memory[str(npc_id)]

            # Despawn NPC
            self._despawn_npc(str(npc_id), room_id)

            logger.info(
                "NPC death handled",
                npc_id=npc_id,
                killer_id=killer_id,
                xp_reward=xp_reward,
                combat_id=combat_id,
            )

            return True

        except Exception as e:
            logger.error("Error handling NPC death", npc_id=npc_id, error=str(e))
            return False

    def get_npc_combat_memory(self, npc_id: str) -> str | None:
        """
        Get the last attacker for an NPC.

        Args:
            npc_id: ID of the NPC

        Returns:
            str: ID of the last attacker, or None if no memory
        """
        return self._npc_combat_memory.get(npc_id)

    def clear_npc_combat_memory(self, npc_id: str) -> bool:
        """
        Clear combat memory for an NPC.

        Args:
            npc_id: ID of the NPC

        Returns:
            bool: True if memory was cleared
        """
        if npc_id in self._npc_combat_memory:
            del self._npc_combat_memory[npc_id]
            logger.debug("Cleared combat memory for NPC", npc_id=npc_id)
            return True
        return False

    def _get_npc_instance(self, npc_id: str) -> Any | None:
        """Get NPC instance from the spawning service."""
        try:
            # Try to get from spawning service if available
            if hasattr(self._persistence, "get_npc_spawning_service"):
                spawning_service = self._persistence.get_npc_spawning_service()
                if spawning_service and npc_id in spawning_service.active_npc_instances:
                    return spawning_service.active_npc_instances[npc_id]

            return None

        except Exception as e:
            logger.error("Error getting NPC instance", npc_id=npc_id, error=str(e))
            return None

    def _get_npc_definition(self, npc_id: str) -> Any | None:
        """Get NPC definition for an NPC instance."""
        try:
            # Try to get from lifecycle manager if available
            if hasattr(self._persistence, "get_npc_lifecycle_manager"):
                lifecycle_manager = self._persistence.get_npc_lifecycle_manager()
                if lifecycle_manager and npc_id in lifecycle_manager.lifecycle_records:
                    return lifecycle_manager.lifecycle_records[npc_id].definition

            return None

        except Exception as e:
            logger.error("Error getting NPC definition", npc_id=npc_id, error=str(e))
            return None

    def _get_player_name(self, player_id: str) -> str:
        """Get player name for messaging."""
        try:
            player = self._persistence.get_player(player_id)
            return player.username if player else "Unknown Player"
        except Exception:
            return "Unknown Player"

    def _despawn_npc(self, npc_id: str, _room_id: str) -> None:
        """Despawn an NPC."""
        try:
            # Try lifecycle manager if available
            if hasattr(self._persistence, "get_npc_lifecycle_manager"):
                lifecycle_manager = self._persistence.get_npc_lifecycle_manager()
                if lifecycle_manager:
                    lifecycle_manager.despawn_npc(npc_id, "combat_death")
                    return

            # Fallback: try spawning service if available
            if hasattr(self._persistence, "get_npc_spawning_service"):
                spawning_service = self._persistence.get_npc_spawning_service()
                if spawning_service and npc_id in spawning_service.active_npc_instances:
                    del spawning_service.active_npc_instances[npc_id]

        except Exception as e:
            logger.error("Error despawning NPC", npc_id=npc_id, error=str(e))
