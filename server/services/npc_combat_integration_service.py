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
)
from ..events.event_bus import EventBus
from ..logging_config import get_logger
from ..models.combat import CombatParticipantType
from ..persistence import get_persistence
from .combat_event_publisher import CombatEventPublisher
from .combat_messaging_integration import CombatMessagingIntegration
from .combat_service import CombatService
from .player_combat_service import PlayerCombatService

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
        self._player_combat_service = PlayerCombatService(self._persistence, self.event_bus)
        self._combat_service = CombatService(self._player_combat_service)

        # Enable auto-progression features
        self._combat_service.auto_progression_enabled = True
        self._combat_service.turn_interval_seconds = 6

        self._messaging_integration = CombatMessagingIntegration()
        self._event_publisher = CombatEventPublisher(event_bus)

        # NPC combat memory - tracks last attacker for each NPC instance
        self._npc_combat_memory: dict[str, str] = {}

        logger.info("NPC Combat Integration Service initialized with auto-progression enabled")

    async def handle_player_attack_on_npc(
        self,
        player_id: str,
        npc_id: str,
        room_id: str,
        action_type: str = "punch",
        damage: int = 1,
    ) -> bool:
        """
        Handle a player attacking an NPC using auto-progression combat system.

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

            # Convert string IDs to UUIDs for combat service
            try:
                attacker_uuid = UUID(player_id) if self._is_valid_uuid(player_id) else uuid4()
                target_uuid = UUID(npc_id) if self._is_valid_uuid(npc_id) else uuid4()
            except ValueError:
                attacker_uuid = uuid4()
                target_uuid = uuid4()

            # Check if combat already exists, if not start new combat
            existing_combat_id = self._combat_service._player_combats.get(attacker_uuid)
            if existing_combat_id:
                # Use existing combat
                combat_result = await self._combat_service.process_attack(
                    attacker_id=attacker_uuid, target_id=target_uuid, damage=damage
                )
            else:
                # Start new combat first
                player_name = self._get_player_name(player_id)

                # Use default player stats for now (TODO: get from player service)
                attacker_hp = 100
                attacker_max_hp = 100
                attacker_dex = 10

                # Get NPC stats properly from the NPC instance
                npc_stats = npc_instance.get_stats()
                npc_current_hp = npc_stats.get("hp", 100)
                npc_max_hp = npc_stats.get("max_hp", 100)
                npc_dexterity = npc_stats.get("dexterity", 10)

                # Start combat with auto-progression - fix parameter order
                await self._combat_service.start_combat(
                    room_id=room_id,
                    attacker_id=attacker_uuid,
                    target_id=target_uuid,
                    attacker_name=player_name,
                    target_name=npc_instance.name,
                    attacker_hp=attacker_hp,
                    attacker_max_hp=attacker_max_hp,
                    attacker_dex=attacker_dex,
                    target_hp=npc_current_hp,
                    target_max_hp=npc_max_hp,
                    target_dex=npc_dexterity,
                    attacker_type=CombatParticipantType.PLAYER,
                    target_type=CombatParticipantType.NPC,
                )

                # Now process the attack
                combat_result = await self._combat_service.process_attack(
                    attacker_id=attacker_uuid, target_id=target_uuid, damage=damage
                )

            if combat_result.success:
                # Broadcast attack message with health info
                self._messaging_integration.broadcast_combat_attack(
                    room_id=room_id,
                    attacker_name=self._get_player_name(player_id),
                    target_name=npc_instance.name,
                    damage=damage,
                    action_type=action_type,
                    combat_id=str(combat_result.combat_id) if combat_result.combat_id else str(uuid4()),
                    attacker_id=player_id,
                )

                # If combat ended, handle NPC death
                if combat_result.combat_ended:
                    self.handle_npc_death(npc_id, room_id, player_id, str(combat_result.combat_id))

                logger.info(
                    "Player attack on NPC handled with auto-progression",
                    player_id=player_id,
                    npc_id=npc_id,
                    damage=damage,
                    combat_ended=combat_result.combat_ended,
                )

                return True
            else:
                logger.warning(
                    "Combat attack failed",
                    player_id=player_id,
                    npc_id=npc_id,
                    message=combat_result.message,
                )
                return False

        except Exception as e:
            logger.error(
                f"Error handling player attack on NPC: {e}",
                player_id=player_id,
                npc_id=npc_id,
                error=str(e),
                exc_info=True,
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
            # Convert IDs to UUID if they are valid UUID strings, otherwise use string IDs
            try:
                npc_uuid = UUID(npc_id) if self._is_valid_uuid(npc_id) else None
                combat_uuid = UUID(combat_id) if combat_id and self._is_valid_uuid(combat_id) else uuid4()
            except ValueError:
                combat_uuid = uuid4()
                npc_uuid = None

            self._event_publisher.publish_npc_died(
                NPCDiedEvent(
                    event_type="npc_died",
                    timestamp=time.time(),
                    combat_id=combat_uuid,
                    room_id=room_id,
                    npc_id=npc_uuid,
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
            # Use the same approach as the combat handler
            from .npc_instance_service import get_npc_instance_service

            npc_instance_service = get_npc_instance_service()
            if hasattr(npc_instance_service, "spawning_service"):
                spawning_service = npc_instance_service.spawning_service
                if npc_id in spawning_service.active_npc_instances:
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

    def _is_valid_uuid(self, uuid_string: str) -> bool:
        """Check if a string is a valid UUID."""
        try:
            UUID(uuid_string)
            return True
        except ValueError:
            return False
