"""
NPC Combat Integration for MythosMUD.

This module provides integration between NPCs and the existing combat system,
including damage calculation, combat events, and interaction with the game
mechanics service.

As documented in the Cultes des Goules, proper combat integration is essential
for maintaining the balance between mortal investigators and the eldritch
entities they encounter.
"""

from typing import Any

from ..events import EventBus
from ..events.event_types import NPCAttacked
from ..game.mechanics import GameMechanicsService
from ..logging.enhanced_logging_config import get_logger
from ..persistence import get_persistence

logger = get_logger(__name__)


class NPCCombatIntegration:
    """
    Integrates NPCs with the existing combat and game mechanics systems.

    This class provides methods for NPCs to interact with the combat system,
    including damage calculation, combat events, and integration with the
    game mechanics service for sanity, fear, and corruption effects.
    """

    def __init__(self, event_bus: EventBus | None = None):
        """
        Initialize the NPC combat integration.

        Args:
            event_bus: Optional EventBus instance. If None, will get the global
                instance.
        """
        self.event_bus = event_bus or EventBus()
        self._persistence = get_persistence(event_bus)
        self._game_mechanics = GameMechanicsService(self._persistence)
        logger.debug("NPC combat integration initialized")

    def calculate_damage(
        self,
        attacker_stats: dict[str, Any],
        target_stats: dict[str, Any],
        weapon_damage: int = 0,
        damage_type: str = "physical",
    ) -> int:
        """
        Calculate damage based on attacker and target stats.

        Args:
            attacker_stats: Stats of the attacking entity (NPC or player)
            target_stats: Stats of the target entity
            weapon_damage: Base damage from weapon or attack
            damage_type: Type of damage being dealt

        Returns:
            int: Calculated damage amount
        """
        try:
            # Base damage calculation
            base_damage = weapon_damage

            # Add strength modifier for physical attacks
            if damage_type == "physical":
                strength_mod = attacker_stats.get("strength", 10)
                strength_bonus = max(0, (strength_mod - 10) // 2)
                base_damage += strength_bonus

            # Apply target's constitution for damage reduction
            target_con = target_stats.get("constitution", 10)
            damage_reduction = max(0, (target_con - 10) // 4)
            final_damage = max(1, base_damage - damage_reduction)

            logger.debug(
                "Damage calculated", base_damage=base_damage, final_damage=final_damage, damage_type=damage_type
            )

            return final_damage

        except Exception as e:
            logger.error("Error calculating damage", error=str(e))
            return 1  # Minimum damage

    def apply_combat_effects(self, target_id: str, damage: int, damage_type: str, source_id: str | None = None) -> bool:
        """
        Apply combat effects to a target (player or NPC).

        Args:
            target_id: ID of the target entity
            damage: Amount of damage to apply
            damage_type: Type of damage
            source_id: ID of the source entity

        Returns:
            bool: True if effects were applied successfully
        """
        try:
            # Check if target is a player (has player data)
            player = self._persistence.get_player(target_id)
            if player:
                # Apply damage to player using game mechanics service
                success, message = self._game_mechanics.damage_player(target_id, damage, damage_type)

                # Apply sanity loss for certain damage types
                if damage_type in ["mental", "occult"]:
                    sanity_loss = min(damage // 2, 10)  # Cap sanity loss
                    self._game_mechanics.apply_sanity_loss(target_id, sanity_loss, f"combat_{damage_type}")

                # Apply fear for certain damage types
                if damage_type in ["occult", "eldritch"]:
                    fear_gain = min(damage // 3, 5)  # Cap fear gain
                    self._game_mechanics.apply_fear(target_id, fear_gain, f"combat_{damage_type}")

                logger.info(
                    "Combat effects applied to player", target_id=target_id, damage=damage, damage_type=damage_type
                )
                return success

            # If not a player, assume it's an NPC
            # NPCs handle their own damage through their take_damage method
            logger.debug("Target is not a player, assuming NPC", target_id=target_id)
            return True

        except Exception as e:
            logger.error("Error applying combat effects", target_id=target_id, error=str(e))
            return False

    def handle_npc_attack(
        self,
        npc_id: str,
        target_id: str,
        room_id: str,
        attack_damage: int,
        attack_type: str = "physical",
        npc_stats: dict[str, Any] | None = None,
    ) -> bool:
        """
        Handle an NPC attack on a target.

        Args:
            npc_id: ID of the attacking NPC
            target_id: ID of the target
            room_id: ID of the room where attack occurs
            attack_damage: Base damage of the attack
            attack_type: Type of attack
            npc_stats: Optional NPC stats (if not provided, will try to get from target)

        Returns:
            bool: True if attack was handled successfully
        """
        try:
            # Get target stats
            target_stats = {}
            player = self._persistence.get_player(target_id)
            if player:
                target_stats = player.stats.model_dump()
            else:
                # For NPC vs NPC combat, we'd need the target NPC stats
                # This is a limitation of the current design
                target_stats = {"constitution": 10}  # Default stats

            # Use provided NPC stats or default
            if not npc_stats:
                npc_stats = {"strength": 10, "constitution": 10}  # Default stats

            # Calculate actual damage
            actual_damage = self.calculate_damage(npc_stats, target_stats, attack_damage, attack_type)

            # Apply combat effects
            self.apply_combat_effects(target_id, actual_damage, attack_type, npc_id)

            # Publish attack event
            if self.event_bus:
                self.event_bus.publish(
                    NPCAttacked(
                        npc_id=npc_id,
                        target_id=target_id,
                        room_id=room_id,
                        damage=actual_damage,
                        attack_type=attack_type,
                    )
                )

            logger.info(
                "NPC attack handled", npc_id=npc_id, target_id=target_id, damage=actual_damage, attack_type=attack_type
            )
            return True

        except Exception as e:
            logger.error("Error handling NPC attack", npc_id=npc_id, target_id=target_id, error=str(e))
            return False

    def handle_npc_death(self, npc_id: str, room_id: str, cause: str = "unknown", killer_id: str | None = None) -> bool:
        """
        Handle NPC death and related effects.

        Args:
            npc_id: ID of the dead NPC
            room_id: ID of the room where death occurred
            cause: Cause of death
            killer_id: ID of the entity that killed the NPC

        Returns:
            bool: True if death was handled successfully
        """
        try:
            # Calculate XP reward for the killer
            xp_reward = 0

            if killer_id:
                # For now, use a default XP reward since NPC retrieval is complex
                # TODO: Implement proper NPC retrieval from NPC database
                xp_reward = 10  # Default XP reward for aggressive mobs

                # Apply effects to killer if it's a player
                player = self._persistence.get_player(killer_id)
                if player:
                    # Gain occult knowledge for killing NPCs
                    occult_gain = 5  # Small amount of occult knowledge
                    self._game_mechanics.gain_occult_knowledge(killer_id, occult_gain, f"killed_{npc_id}")

                    # Apply sanity loss for killing (even aggressive NPCs)
                    sanity_loss = 2  # Small sanity loss for taking a life
                    self._game_mechanics.apply_sanity_loss(killer_id, sanity_loss, f"killed_{npc_id}")

            # Note: NPCDied event is now published by CombatService via NATS
            # This prevents duplicate event publishing and ensures consistent event handling

            logger.info(
                "NPC death handled",
                npc_id=npc_id,
                cause=cause,
                killer_id=killer_id,
                xp_reward=xp_reward,
            )
            return True

        except Exception as e:
            logger.error("Error handling NPC death", npc_id=npc_id, error=str(e))
            return False

    def get_combat_stats(self, entity_id: str, npc_stats: dict[str, Any] | None = None) -> dict[str, Any]:
        """
        Get combat-relevant stats for an entity.

        Args:
            entity_id: ID of the entity
            npc_stats: Optional NPC stats (for NPC entities)

        Returns:
            dict: Combat stats
        """
        try:
            # Check if it's a player
            player = self._persistence.get_player(entity_id)
            if player:
                stats = player.stats.model_dump()
                return {
                    "hp": stats.get("current_health", 100),
                    "max_hp": stats.get("max_health", 100),
                    "strength": stats.get("strength", 10),
                    "constitution": stats.get("constitution", 10),
                    "sanity": stats.get("sanity", 100),
                    "fear": stats.get("fear", 0),
                    "corruption": stats.get("corruption", 0),
                }

            # For NPCs, use provided stats or return empty dict
            if npc_stats:
                return npc_stats

            logger.warning("Entity not found for combat stats", entity_id=entity_id)
            return {}

        except Exception as e:
            # If there's a database error (e.g., in test environment),
            # try to return NPC stats if provided
            if npc_stats:
                logger.debug("Database error, returning provided NPC stats", entity_id=entity_id, error=str(e))
                return npc_stats
            logger.error("Error getting combat stats", entity_id=entity_id, error=str(e))
            return {}
