"""
Aggressive mob NPC type for MythosMUD.

This module provides the AggressiveMobNPC class with hunting and territorial behaviors.
"""

from typing import Any

from ..structured_logging.enhanced_logging_config import get_logger
from .npc_base import NPCBase

logger = get_logger(__name__)


class AggressiveMobNPC(NPCBase):
    """Aggressive mob NPC type with hunting and territorial behaviors."""

    def __init__(self, definition: Any, npc_id: str, event_bus=None, event_reaction_system=None):
        """Initialize aggressive mob NPC."""
        super().__init__(definition, npc_id, event_bus, event_reaction_system)
        self._targets: list[str] = []
        # Avoid direct access to prevent potential lazy loading issues
        self._territory_center = getattr(definition, "room_id", None)
        self._setup_aggressive_mob_behavior_rules()

    def _setup_aggressive_mob_behavior_rules(self):
        """Setup aggressive mob-specific behavior rules."""
        aggressive_mob_rules = [
            {
                "name": "hunt_players",
                "condition": "player_in_range == true",
                "action": "hunt_target",
                "priority": 7,
            },
            {
                "name": "attack_on_sight",
                "condition": "enemy_nearby == true",
                "action": "attack_target",
                "priority": 8,
            },
            {
                "name": "flee_when_low_dp",
                "condition": "dp < flee_threshold",
                "action": "flee",
                "priority": 9,
            },
            {
                "name": "patrol_territory",
                "condition": "time_since_last_action > 120",
                "action": "patrol_territory",
                "priority": 3,
            },
        ]

        for rule in aggressive_mob_rules:
            self._behavior_engine.add_rule(rule)

        # Register aggressive mob action handlers
        self._behavior_engine.register_action_handler("hunt_target", self._handle_hunt_target)
        self._behavior_engine.register_action_handler("attack_target", self._handle_attack_target)
        self._behavior_engine.register_action_handler("flee", self._handle_flee)
        self._behavior_engine.register_action_handler("patrol_territory", self._handle_patrol_territory)

    def get_behavior_rules(self) -> list[dict[str, Any]]:
        """Get aggressive mob-specific behavior rules."""
        return self._behavior_engine.get_rules()

    def hunt_target(self, target_id: str) -> bool:
        """Hunt a specific target."""
        try:
            if target_id not in self._targets:
                self._targets.append(target_id)

            logger.debug("NPC is hunting target", npc_id=self.npc_id, target_id=target_id)
            return True
        except (TypeError, AttributeError) as e:
            logger.error("Error hunting target", npc_id=self.npc_id, error=str(e), error_type=type(e).__name__)
            return False

    def attack_target(self, target_id: str) -> bool:
        """Attack a specific target."""
        try:
            attack_damage = self._behavior_config.get("attack_damage", 20)
            logger.info("NPC attacked target", npc_id=self.npc_id, target_id=target_id, damage=attack_damage)

            # Use combat integration for attack handling
            if hasattr(self, "combat_integration") and self.combat_integration:
                import asyncio

                try:
                    # Try to get running event loop
                    asyncio.get_running_loop()
                    # Fire-and-forget: create task for async call
                    asyncio.create_task(
                        self.combat_integration.handle_npc_attack(
                            self.npc_id, target_id, self.current_room, attack_damage, "physical", self.get_stats()
                        )
                    )
                    # Return True immediately (attack is queued)
                    return True
                except RuntimeError:
                    # No running loop - use asyncio.run() if possible
                    try:
                        success = asyncio.run(
                            self.combat_integration.handle_npc_attack(
                                self.npc_id, target_id, self.current_room, attack_damage, "physical", self.get_stats()
                            )
                        )
                        return success
                    except (RuntimeError, TypeError, AttributeError) as e:
                        logger.error(
                            "Failed to execute NPC attack",
                            npc_id=self.npc_id,
                            error=str(e),
                            error_type=type(e).__name__,
                        )
                        return False
            else:
                # Fallback to direct event publishing
                if self.event_bus:
                    from ..events.event_types import NPCAttacked

                    self.event_bus.publish(
                        NPCAttacked(
                            npc_id=self.npc_id,
                            target_id=target_id,
                            room_id=self.current_room or "unknown",
                            damage=attack_damage,
                            attack_type="physical",
                        )
                    )
                return True

        except (TypeError, KeyError, AttributeError, RuntimeError) as e:
            logger.error("Error attacking target", npc_id=self.npc_id, error=str(e), error_type=type(e).__name__)
            return False

    def flee(self) -> bool:
        """Flee from current situation."""
        try:
            self.speak("I must retreat!")
            logger.debug("NPC is fleeing", npc_id=self.npc_id)
            return True
        except (AttributeError, TypeError, RuntimeError) as e:
            logger.error("Error fleeing", npc_id=self.npc_id, error=str(e), error_type=type(e).__name__)
            return False

    def patrol_territory(self) -> bool:
        """Patrol the NPC's territory."""
        try:
            logger.debug("NPC is patrolling territory", npc_id=self.npc_id)
            return True
        except (TypeError, AttributeError) as e:
            logger.error("Error patrolling territory", npc_id=self.npc_id, error=str(e), error_type=type(e).__name__)
            return False

    def _handle_hunt_target(self, context: dict[str, Any]) -> bool:
        """Handle hunting target action."""
        target_id = context.get("target_id", "unknown")
        return self.hunt_target(target_id)

    def _handle_attack_target(self, context: dict[str, Any]) -> bool:
        """Handle attacking target action."""
        target_id = context.get("target_id", "unknown")
        return self.attack_target(target_id)

    def _handle_flee(self, _context: dict[str, Any]) -> bool:
        """Handle fleeing action."""
        return self.flee()

    def _handle_patrol_territory(self, _context: dict[str, Any]) -> bool:
        """Handle patrolling territory action."""
        return self.patrol_territory()
