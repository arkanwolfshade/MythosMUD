"""
NPC Combat Integration for MythosMUD.

This module provides integration between NPCs and the existing combat system,
including damage calculation, combat events, and interaction with the game
mechanics service.

As documented in the Cultes des Goules, proper combat integration is essential
for maintaining the balance between mortal investigators and the eldritch
entities they encounter.
"""

import uuid
from typing import Any

from ..events import EventBus
from ..events.event_types import NPCAttacked
from ..exceptions import DatabaseError, ValidationError
from ..game.mechanics import GameMechanicsService
from ..logging.enhanced_logging_config import get_logger

# Removed: from ..persistence import get_persistence - now using async_persistence

logger = get_logger(__name__)


class NPCCombatIntegration:
    """
    Integrates NPCs with the existing combat and game mechanics systems.

    This class provides methods for NPCs to interact with the combat system,
    including damage calculation, combat events, and integration with the
    game mechanics service for lucidity, fear, and corruption effects.
    """

    def __init__(self, event_bus: EventBus | None = None, async_persistence=None):
        """
        Initialize the NPC combat integration.

        Args:
            event_bus: Optional EventBus instance. If None, will get the global
                instance.
            async_persistence: Async persistence layer instance (required)
        """
        if async_persistence is None:
            raise ValueError("async_persistence is required for NPCCombatIntegration")
        self.event_bus = event_bus or EventBus()
        self._persistence = async_persistence
        self._game_mechanics = GameMechanicsService(async_persistence)
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
                strength_mod = attacker_stats.get("strength", 50)
                strength_bonus = max(0, (strength_mod - 50) // 2)
                base_damage += strength_bonus

            # Apply target's constitution for damage reduction
            target_con = target_stats.get("constitution", 50)
            damage_reduction = max(0, (target_con - 50) // 4)
            final_damage = max(1, base_damage - damage_reduction)

            logger.debug(
                "Damage calculated", base_damage=base_damage, final_damage=final_damage, damage_type=damage_type
            )

            return final_damage

        except (TypeError, ValueError, ArithmeticError) as e:
            logger.error("Error calculating damage", error=str(e))
            return 1  # Minimum damage

    async def apply_combat_effects(
        self, target_id: str, damage: int, damage_type: str, source_id: str | None = None
    ) -> bool:
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
            target_id_uuid = self._convert_target_id_to_uuid(target_id)
            player = await self._persistence.get_player_by_id(target_id_uuid)
            if player:
                return await self._apply_player_combat_effects(target_id, damage, damage_type)
            # If not a player, assume it's an NPC
            logger.debug("Target is not a player, assuming NPC", target_id=target_id)
            return True
        except AttributeError as e:
            self._handle_attribute_error(target_id, damage, damage_type, source_id, e)
            raise
        except ValidationError as e:
            return self._handle_validation_error(target_id, damage, damage_type, e)
        except Exception as e:
            self._handle_unexpected_error(target_id, damage, damage_type, e)
            raise

    def _convert_target_id_to_uuid(self, target_id: str) -> uuid.UUID:
        """Convert target_id to UUID if it's a string."""
        return uuid.UUID(target_id) if isinstance(target_id, str) else target_id

    async def _apply_player_combat_effects(self, target_id: str, damage: int, damage_type: str) -> bool:
        """Apply combat effects to a player."""
        # Apply damage to player using game mechanics service
        success, _ = await self._game_mechanics.damage_player(target_id, damage, damage_type)

        # Apply mental/occult effects
        await self._apply_mental_effects(target_id, damage, damage_type)

        logger.info("Combat effects applied to player", target_id=target_id, damage=damage, damage_type=damage_type)
        return success

    async def _apply_mental_effects(self, target_id: str, damage: int, damage_type: str) -> None:
        """Apply mental/occult effects (lucidity loss and fear) based on damage type."""
        # Apply lucidity loss for certain damage types
        if damage_type in ["mental", "occult"]:
            lucidity_loss = min(damage // 2, 10)  # Cap lucidity loss
            await self._game_mechanics.apply_lucidity_loss(target_id, lucidity_loss, f"combat_{damage_type}")

        # Apply fear for certain damage types
        if damage_type in ["occult", "eldritch"]:
            fear_gain = min(damage // 3, 5)  # Cap fear gain
            await self._game_mechanics.apply_fear(target_id, fear_gain, f"combat_{damage_type}")

    def _handle_attribute_error(
        self, target_id: str, damage: int, damage_type: str, source_id: str | None, error: AttributeError
    ) -> None:
        """Handle AttributeError (critical programming error)."""
        logger.critical(
            "CRITICAL: Missing persistence method called",
            target_id=target_id,
            error=str(error),
            error_type="AttributeError",
            damage=damage,
            damage_type=damage_type,
            source_id=source_id,
            exc_info=True,
        )

    def _handle_validation_error(self, target_id: str, damage: int, damage_type: str, error: ValidationError) -> bool:
        """Handle ValidationError (expected validation error)."""
        logger.warning(
            "Validation error in combat effects",
            target_id=target_id,
            error=str(error),
            damage=damage,
            damage_type=damage_type,
        )
        return False

    def _handle_unexpected_error(self, target_id: str, damage: int, damage_type: str, error: Exception) -> None:
        """Handle unexpected errors."""
        logger.error(
            "Unexpected error applying combat effects",
            target_id=target_id,
            error=str(error),
            error_type=type(error).__name__,
            damage=damage,
            damage_type=damage_type,
            exc_info=True,
        )

    async def handle_npc_attack(
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
            target_stats = self._get_target_stats(target_id)
            npc_stats = self._get_npc_stats(npc_stats)
            actual_damage = self.calculate_damage(npc_stats, target_stats, attack_damage, attack_type)
            await self.apply_combat_effects(target_id, actual_damage, attack_type, npc_id)
            self._publish_attack_event(npc_id, target_id, room_id, actual_damage, attack_type)
            logger.info(
                "NPC attack handled", npc_id=npc_id, target_id=target_id, damage=actual_damage, attack_type=attack_type
            )
            return True
        except (ValueError, TypeError, AttributeError, ArithmeticError) as e:
            logger.error("Error handling NPC attack", npc_id=npc_id, target_id=target_id, error=str(e))
            return False

    def _get_target_stats(self, target_id: str) -> dict[str, Any]:
        """Get target stats from player or use defaults."""
        target_id_uuid = uuid.UUID(target_id) if isinstance(target_id, str) else target_id
        player = self._persistence.get_player(target_id_uuid)
        if player:
            return player.stats.model_dump()
        # For NPC vs NPC combat, we'd need the target NPC stats
        # This is a limitation of the current design
        return {"constitution": 50}  # Default stats

    def _get_npc_stats(self, npc_stats: dict[str, Any] | None) -> dict[str, Any]:
        """Get NPC stats or use defaults."""
        if not npc_stats:
            return {"strength": 50, "constitution": 50}  # Default stats
        return npc_stats

    def _publish_attack_event(self, npc_id: str, target_id: str, room_id: str, damage: int, attack_type: str) -> None:
        """Publish NPC attack event to event bus."""
        if self.event_bus:
            self.event_bus.publish(
                NPCAttacked(
                    npc_id=npc_id,
                    target_id=target_id,
                    room_id=room_id,
                    damage=damage,
                    attack_type=attack_type,
                )
            )

    async def handle_npc_death(
        self, npc_id: str, room_id: str, cause: str = "unknown", killer_id: str | None = None
    ) -> bool:
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
                # Use default XP reward for NPC kills
                # Future enhancement: Calculate XP based on NPC definition data (level, type, etc.)
                # This would require access to NPC definition service or lifecycle manager
                xp_reward = 10  # Default XP reward for aggressive mobs

                # Apply effects to killer if it's a player
                # Convert killer_id to UUID if it's a string
                killer_id_uuid = uuid.UUID(killer_id) if isinstance(killer_id, str) else killer_id
                player = await self._persistence.get_player_by_id(killer_id_uuid)
                if player:
                    # Gain occult knowledge for killing NPCs
                    occult_gain = 5  # Small amount of occult knowledge
                    await self._game_mechanics.gain_occult_knowledge(killer_id, occult_gain, f"killed_{npc_id}")

                    # Apply lucidity loss for killing (even aggressive NPCs)
                    lucidity_loss = 2  # Small lucidity loss for taking a life
                    await self._game_mechanics.apply_lucidity_loss(killer_id, lucidity_loss, f"killed_{npc_id}")

            # Note: NPCDied event is now published by CombatService via NATS
            # This prevents duplicate event publishing and ensures consistent event handling

            logger.info(
                "NPC death handled",
                npc_id=npc_id,
                room_id=room_id,
                cause=cause,
                killer_id=killer_id,
                xp_reward=xp_reward,
            )
            return True

        except (ValueError, TypeError, AttributeError, ValidationError) as e:
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
            # Convert entity_id to UUID if it's a string
            entity_id_uuid = uuid.UUID(entity_id) if isinstance(entity_id, str) else entity_id
            player = self._persistence.get_player(entity_id_uuid)
            if player:
                stats = player.stats.model_dump()
                # Use current_dp for determination points
                current_dp = stats.get("current_dp", 100)
                # Handle both max_dp and max_health for backward compatibility
                # If neither exists, try to compute from constitution and size, or default to 100
                max_dp = stats.get("max_dp")
                if max_dp is None:
                    max_dp = stats.get("max_health")
                if max_dp is None:
                    # Try to compute from constitution and size if available
                    con = stats.get("constitution", 50)
                    siz = stats.get("size", 50)
                    max_dp = (con + siz) // 5 if con and siz else 100
                return {
                    "dp": current_dp,
                    "max_dp": max_dp,
                    "strength": stats.get("strength", 50),
                    "constitution": stats.get("constitution", 50),
                    "lucidity": stats.get("lucidity", 100),
                    "fear": stats.get("fear", 0),
                    "corruption": stats.get("corruption", 0),
                }

            # For NPCs, use provided stats or return empty dict
            if npc_stats:
                return npc_stats

            logger.warning("Entity not found for combat stats", entity_id=entity_id)
            return {}

        except (ValueError, TypeError, AttributeError, DatabaseError, ValidationError) as e:
            # If there's an error (e.g., invalid UUID, missing attributes, type mismatch, database errors),
            # try to return NPC stats if provided
            if npc_stats:
                logger.debug(
                    "Error getting combat stats, returning provided NPC stats", entity_id=entity_id, error=str(e)
                )
                return npc_stats
            logger.error("Error getting combat stats", entity_id=entity_id, error=str(e))
            return {}
