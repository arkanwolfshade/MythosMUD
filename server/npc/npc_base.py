"""
Base NPC class for MythosMUD.

This module provides the base NPC class with common functionality including
stats management, inventory, communication, and basic behavior framework.
"""

import json
import time
from abc import ABC, abstractmethod
from typing import Any

from ..models.npc import NPCDefinition
from ..structured_logging.enhanced_logging_config import get_logger
from .behavior_engine import BehaviorEngine

logger = get_logger(__name__)


class NPCBase(ABC):
    """
    Base class for all NPCs.

    This class provides common functionality including stats management,
    inventory, communication, and basic behavior framework.
    """

    def __init__(self, definition: Any, npc_id: str, event_bus=None, event_reaction_system=None):
        """
        Initialize the NPC base class.

        Args:
            definition: NPC definition from database
            npc_id: Unique identifier for this NPC instance
            event_bus: Optional event bus for publishing events
            event_reaction_system: Optional event reaction system for automatic reactions
        """
        self.npc_id = npc_id
        self.definition = definition
        # Avoid direct access to prevent potential lazy loading issues
        self.npc_type = getattr(definition, "npc_type", "unknown")
        self.name = getattr(definition, "name", "Unknown NPC")
        # Avoid direct access to prevent potential lazy loading issues
        self.current_room = getattr(definition, "room_id", None)
        # Track spawn room for idle movement (defaults to definition room_id or current_room)
        self.spawn_room_id = getattr(definition, "room_id", None) or self.current_room
        self.is_alive = True
        self.is_active = True

        # Parse configuration from definition - use getattr to avoid lazy loading issues
        self._stats = self._parse_stats(getattr(definition, "base_stats", "{}"))
        self._behavior_config = self._parse_behavior_config(getattr(definition, "behavior_config", "{}"))
        self._ai_config = self._parse_ai_config(getattr(definition, "ai_integration_stub", "{}"))

        # CRITICAL FIX: NPC stats use "determination_points"
        # Support backward compatibility with "hp", "dp", and "determination_points" during migration
        if "determination_points" not in self._stats:
            if "dp" in self._stats:
                self._stats["determination_points"] = self._stats["dp"]
            elif "hp" in self._stats:
                # Convert legacy "hp" to "determination_points"
                self._stats["determination_points"] = self._stats["hp"]
                # Also set max_dp from max_hp if present
                if "max_hp" in self._stats and "max_dp" not in self._stats:
                    self._stats["max_dp"] = self._stats["max_hp"]
            elif "determination_points" in self._stats:
                self._stats["determination_points"] = self._stats["determination_points"]
            else:
                self._stats["determination_points"] = 20  # Default DP

        # Initialize inventory
        self._inventory: list[dict[str, Any]] = []

        # Initialize behavior engine
        self._behavior_engine = BehaviorEngine()
        self._setup_base_behavior_rules()

        # Track last action time for behavior timing
        self._last_action_time = time.time()
        # Track last idle movement time for interval checking
        self._last_idle_movement_time: float | None = None

        # Initialize event system integration
        self.event_bus = event_bus
        self.event_reaction_system = event_reaction_system

        # Initialize integration systems (will be set by external systems)
        self.movement_integration: Any | None = None
        self.combat_integration: Any | None = None
        self.communication_integration: Any | None = None

        # Avoid accessing definition.name in logger to prevent potential lazy loading issues
        # Temporarily disable logging to avoid potential recursion issues
        # npc_name = getattr(definition, "name", "Unknown")
        # logger.info("NPC base initialized", npc_id=npc_id, npc_name=npc_name)

        # Register default event reactions if reaction system is available
        if self.event_reaction_system:
            self._register_default_reactions()

    def _parse_stats(self, stats_json: str) -> dict[str, Any]:
        """Parse stats from JSON string."""
        try:
            return json.loads(stats_json) if stats_json else {}
        except json.JSONDecodeError:
            logger.warning("Invalid stats JSON, using defaults", npc_id=self.npc_id)
            return {
                "determination_points": 20,
                "max_dp": 20,
                "strength": 50,
                "intelligence": 40,
                "charisma": 30,
            }

    def _parse_behavior_config(self, config_json: str) -> dict[str, Any]:
        """Parse behavior configuration from JSON string."""
        try:
            config = json.loads(config_json) if config_json else {}
            # Apply defaults for idle movement based on NPC type
            self._apply_idle_movement_defaults(config)
            return config
        except json.JSONDecodeError:
            logger.warning("Invalid behavior config JSON, using defaults", npc_id=self.npc_id)
            config = {}
            self._apply_idle_movement_defaults(config)
            return config

    def _apply_idle_movement_defaults(self, config: dict[str, Any]) -> None:
        """
        Apply default idle movement configuration based on NPC type.

        As documented in the Pnakotic Manuscripts, mob entities require
        different movement patterns than stationary entities like shopkeepers.

        Args:
            config: Behavior configuration dictionary to modify in-place
        """
        # Default idle movement enabled based on NPC type
        if "idle_movement_enabled" not in config:
            # Enable for mob types, disable for shopkeepers and quest givers
            config["idle_movement_enabled"] = self.npc_type in ["passive_mob", "aggressive_mob"]

        # Default movement interval (100 seconds, scaled 10x for 100ms tick rate)
        if "idle_movement_interval" not in config:
            config["idle_movement_interval"] = 100

        # Default movement probability (25%)
        if "idle_movement_probability" not in config:
            config["idle_movement_probability"] = 0.25

        # Default weighted home selection (true)
        if "idle_movement_weighted_home" not in config:
            config["idle_movement_weighted_home"] = True

    def _parse_ai_config(self, ai_json: str) -> dict[str, Any]:
        """Parse AI integration configuration from JSON string."""
        try:
            return json.loads(ai_json) if ai_json else {}
        except json.JSONDecodeError:
            logger.warning("Invalid AI config JSON, using defaults", npc_id=self.npc_id)
            return {"ai_enabled": False, "ai_model": None}

    def _setup_base_behavior_rules(self):
        """Setup base behavior rules common to all NPCs."""
        base_rules = [
            {
                "name": "check_health",
                "condition": "determination_points <= 0",
                "action": "die",
                "priority": 10,
            },
            {
                "name": "idle_behavior",
                "condition": "time_since_last_action > 300",
                "action": "idle",
                "priority": 1,
            },
        ]

        for rule in base_rules:
            self._behavior_engine.add_rule(rule)

        # Register base action handlers
        self._behavior_engine.register_action_handler("die", self._handle_die)
        self._behavior_engine.register_action_handler("idle", self._handle_idle)

    def get_stats(self) -> dict[str, Any]:
        """Get current NPC stats."""
        return self._stats.copy()

    def get_behavior_config(self) -> dict[str, Any]:
        """Get behavior configuration."""
        return self._behavior_config.copy()

    def get_ai_config(self) -> dict[str, Any]:
        """Get AI integration configuration."""
        return self._ai_config.copy()

    def get_inventory(self) -> list[dict[str, Any]]:
        """Get NPC inventory."""
        return self._inventory.copy()

    def add_item_to_inventory(self, item: dict[str, Any]) -> bool:
        """Add item to NPC inventory."""
        try:
            self._inventory.append(item)
            logger.debug("Added item to inventory", npc_id=self.npc_id, item_id=item.get("id"))
            return True
        except (TypeError, AttributeError) as e:
            logger.error(
                "Error adding item to inventory", npc_id=self.npc_id, error=str(e), error_type=type(e).__name__
            )
            return False

    def remove_item_from_inventory(self, item_id: str) -> bool:
        """Remove item from NPC inventory."""
        try:
            original_count = len(self._inventory)
            self._inventory = [item for item in self._inventory if item.get("id") != item_id]

            if len(self._inventory) < original_count:
                logger.debug("Removed item from inventory", npc_id=self.npc_id, item_id=item_id)
                return True
            else:
                logger.warning("Item not found in inventory", npc_id=self.npc_id, item_id=item_id)
                return False
        except (TypeError, KeyError, AttributeError) as e:
            logger.error(
                "Error removing item from inventory", npc_id=self.npc_id, error=str(e), error_type=type(e).__name__
            )
            return False

    def get_item_from_inventory(self, item_id: str) -> dict[str, Any] | None:
        """Get specific item from inventory."""
        for item in self._inventory:
            if item.get("id") == item_id:
                return item
        return None

    def _update_determination_points(self, damage: int) -> int:
        """
        Update determination points after taking damage.

        Args:
            damage: Amount of damage taken

        Returns:
            int: New determination points value
        """
        # CRITICAL FIX: Support determination_points, with backward compatibility for "dp" and "determination_points"
        current_dp = self._stats.get(
            "determination_points", self._stats.get("dp", self._stats.get("determination_points", 0))
        )
        new_dp = max(0, current_dp - damage)
        self._stats["determination_points"] = new_dp
        # Also update "dp" and "determination_points" if they exist for backward compatibility
        if "dp" in self._stats:
            self._stats["dp"] = new_dp
        if "determination_points" in self._stats:
            self._stats["determination_points"] = new_dp
        return new_dp

    def _publish_damage_event(self, damage: int, damage_type: str, source_id: str | None) -> None:
        """
        Publish damage event to event bus.

        Args:
            damage: Amount of damage taken
            damage_type: Type of damage
            source_id: ID of damage source
        """
        if not self.event_bus:
            return

        from ..events.event_types import NPCTookDamage

        # AI Agent: timestamp and event_type are set automatically by BaseEvent (init=False)
        self.event_bus.publish(
            NPCTookDamage(
                npc_id=self.npc_id,
                room_id=self.current_room or "unknown",
                damage=damage,
                damage_type=damage_type,
                source_id=source_id,
            )
        )

    def _handle_npc_death(self, damage: int, source_id: str | None) -> None:
        """
        Handle NPC death after taking fatal damage.

        Args:
            damage: Amount of damage that caused death
            source_id: ID of damage source
        """
        self.is_alive = False
        logger.info("NPC died", npc_id=self.npc_id, damage=damage)

        # Use combat integration for death handling
        if hasattr(self, "combat_integration") and self.combat_integration:
            self.combat_integration.handle_npc_death(self.npc_id, self.current_room, "damage", source_id)
        else:
            # Fallback to direct event publishing
            if self.event_bus:
                from ..events.event_types import NPCDied

                # AI Agent: timestamp and event_type are set automatically by BaseEvent (init=False)
                self.event_bus.publish(
                    NPCDied(
                        npc_id=self.npc_id,
                        room_id=self.current_room or "unknown",
                        cause="damage",
                        killer_id=source_id,
                    )
                )

    def take_damage(self, damage: int, damage_type: str = "physical", source_id: str | None = None) -> bool:
        """Take damage and update determination points (DP)."""
        try:
            if not self.is_alive:
                return False

            new_dp = self._update_determination_points(damage)
            self._publish_damage_event(damage, damage_type, source_id)

            if new_dp <= 0:
                self._handle_npc_death(damage, source_id)
            else:
                logger.debug("NPC took damage", npc_id=self.npc_id, damage=damage, new_dp=new_dp)

            return True
        except (TypeError, KeyError, AttributeError) as e:
            logger.error("Error taking damage", npc_id=self.npc_id, error=str(e), error_type=type(e).__name__)
            return False

    def heal(self, amount: int) -> bool:
        """Heal and update determination points (DP)."""
        try:
            if not self.is_alive:
                return False

            # CRITICAL FIX: Support determination_points, with backward compatibility for "dp" and "determination_points"
            current_dp = self._stats.get(
                "determination_points", self._stats.get("dp", self._stats.get("determination_points", 0))
            )
            max_dp = self._stats.get("max_dp", self._stats.get("max_dp", self._stats.get("max_dp", 20)))
            new_dp = min(max_dp, current_dp + amount)
            self._stats["determination_points"] = new_dp
            # Also update "dp" and "determination_points" if they exist for backward compatibility
            if "dp" in self._stats:
                self._stats["dp"] = new_dp
            if "determination_points" in self._stats:
                self._stats["determination_points"] = new_dp

            logger.debug("NPC healed", npc_id=self.npc_id, amount=amount, new_dp=new_dp)
            return True
        except (TypeError, KeyError, AttributeError, ValueError) as e:
            logger.error("Error healing", npc_id=self.npc_id, error=str(e), error_type=type(e).__name__)
            return False

    def _get_integration_dependencies(self) -> tuple[Any | None, Any | None]:
        """
        Get event bus and persistence dependencies for movement integration.

        Returns:
            tuple: (event_bus, persistence) or (None, None) if unavailable
        """
        event_bus = getattr(self, "_event_bus", None)
        persistence = None

        # Note: persistence is initialized to None and will be retrieved from container if needed
        # Early return only if both are already available (event_bus from self, persistence would need container)
        # Since persistence starts as None, we always need to check the container

        try:
            from ..container import ApplicationContainer

            container = ApplicationContainer.get_instance()
            if not container:
                return event_bus, persistence

            if not event_bus:
                event_bus = getattr(container, "event_bus", None)
            if not persistence:
                persistence = getattr(container, "async_persistence", None)

            return event_bus, persistence

        except (ImportError, AttributeError, RuntimeError) as e:
            logger.error("Error getting persistence or event bus", error=str(e), error_type=type(e).__name__)
            return event_bus, persistence

    def _move_with_integration(self, room_id: str) -> bool:
        """
        Move NPC using the movement integration system.

        Args:
            room_id: ID of the destination room

        Returns:
            bool: True if movement was successful
        """
        from .movement_integration import NPCMovementIntegration

        event_bus, persistence = self._get_integration_dependencies()

        if not persistence:
            logger.error("persistence (async_persistence) is required for NPCMovementIntegration", npc_id=self.npc_id)
            return False

        movement_integration = NPCMovementIntegration(event_bus, persistence=persistence)
        success = movement_integration.move_npc_to_room(self.npc_id, self.current_room or "unknown", room_id)

        if success:
            self.current_room = room_id
            logger.debug("NPC moved to room with integration", npc_id=self.npc_id, room_id=room_id)
            return True

        logger.warning("NPC movement failed with integration", npc_id=self.npc_id, room_id=room_id)
        return False

    def _move_simple(self, room_id: str) -> bool:
        """
        Move NPC without integration (simple room update).

        Args:
            room_id: ID of the destination room

        Returns:
            bool: True if movement was successful
        """
        self.current_room = room_id
        logger.debug("NPC moved to room (simple)", npc_id=self.npc_id, room_id=room_id)
        return True

    def move_to_room(self, room_id: str, use_integration: bool = True) -> bool:
        """
        Move NPC to a different room.

        Args:
            room_id: ID of the destination room
            use_integration: Whether to use the movement integration system

        Returns:
            bool: True if movement was successful
        """
        try:
            if use_integration:
                return self._move_with_integration(room_id)
            return self._move_simple(room_id)

        except (ImportError, AttributeError, RuntimeError, TypeError) as e:
            logger.error("Error moving NPC", npc_id=self.npc_id, error=str(e), error_type=type(e).__name__)
            return False

    def speak(self, message: str, channel: str = "local", target_id: str | None = None) -> bool:
        """NPC speaks a message."""
        try:
            logger.info("NPC spoke", npc_id=self.npc_id, message=message, channel=channel)

            # Use communication integration if available
            if hasattr(self, "communication_integration") and self.communication_integration:
                if target_id and channel == "whisper":
                    # Send whisper to specific target
                    return self.communication_integration.send_whisper_to_player(
                        self.npc_id, target_id, message, self.current_room
                    )
                else:
                    # Send message to room
                    return self.communication_integration.send_message_to_room(
                        self.npc_id, self.current_room, message, channel
                    )
            else:
                # Fallback to direct event publishing
                if self.event_bus:
                    from ..events.event_types import NPCSpoke

                    self.event_bus.publish(
                        NPCSpoke(
                            npc_id=self.npc_id,
                            room_id=self.current_room or "unknown",
                            message=message,
                            channel=channel,
                            target_id=target_id,
                        )
                    )
                return True

        except (AttributeError, TypeError, RuntimeError) as e:
            logger.error("Error NPC speaking", npc_id=self.npc_id, error=str(e), error_type=type(e).__name__)
            return False

    def listen(self, message: str, speaker_id: str, channel: str = "local") -> bool:
        """NPC receives/listens to a message."""
        try:
            logger.debug("NPC listened", npc_id=self.npc_id, speaker_id=speaker_id, message=message, channel=channel)

            # Use communication integration if available
            if hasattr(self, "communication_integration") and self.communication_integration:
                return self.communication_integration.handle_player_message(
                    self.npc_id, speaker_id, message, self.current_room, channel
                )
            else:
                # Fallback to direct event publishing
                if self.event_bus:
                    from ..events.event_types import NPCListened

                    self.event_bus.publish(
                        NPCListened(
                            npc_id=self.npc_id,
                            room_id=self.current_room or "unknown",
                            message=message,
                            speaker_id=speaker_id,
                            channel=channel,
                        )
                    )
                return True

        except (AttributeError, TypeError, RuntimeError) as e:
            logger.error("Error NPC listening", npc_id=self.npc_id, error=str(e), error_type=type(e).__name__)
            return False

    def _register_default_reactions(self) -> None:
        """Register default event reactions for this NPC."""
        if not self.event_reaction_system:
            return

        try:
            from .event_reaction_system import NPCEventReactionTemplates

            reactions = []

            # Add greeting reaction for friendly NPCs
            if self.npc_type in ["shopkeeper", "passive_mob"]:
                greeting = self._behavior_config.get("greeting_message", "Hello there!")
                reactions.append(NPCEventReactionTemplates.player_entered_room_greeting(self.npc_id, greeting))

            # Add farewell reaction
            if self.npc_type in ["shopkeeper", "passive_mob"]:
                farewell = self._behavior_config.get("farewell_message", "Goodbye!")
                reactions.append(NPCEventReactionTemplates.player_left_room_farewell(self.npc_id, farewell))

            # Add combat reactions for aggressive NPCs
            if self.npc_type == "aggressive_mob":
                reactions.append(NPCEventReactionTemplates.npc_attacked_retaliation(self.npc_id))

            # Add response reactions for communicative NPCs
            if self.npc_type in ["shopkeeper", "passive_mob"]:
                response = self._behavior_config.get("response_message", "I heard you!")
                reactions.append(NPCEventReactionTemplates.player_spoke_response(self.npc_id, response))

            # Register reactions
            if reactions:
                self.event_reaction_system.register_npc_reactions(self.npc_id, reactions)
                logger.debug("Registered default reactions", npc_id=self.npc_id, reaction_count=len(reactions))

        except (ImportError, AttributeError, TypeError) as e:
            logger.error(
                "Error registering default reactions", npc_id=self.npc_id, error=str(e), error_type=type(e).__name__
            )

    def get_npc_context(self) -> dict[str, Any]:
        """
        Get context information for this NPC for event reactions.

        Returns:
            dict: NPC context information
        """
        return {
            "npc_id": self.npc_id,
            "current_room": self.current_room,
            "is_alive": self.is_alive,
            "is_active": self.is_active,
            "stats": self._stats,
            "behavior_config": self._behavior_config,
            "npc_type": self.npc_type,
            "name": self.name,
        }

    def get_behavior_engine(self) -> BehaviorEngine:
        """Get the behavior engine for this NPC."""
        return self._behavior_engine

    @abstractmethod
    def get_behavior_rules(self) -> list[dict[str, Any]]:
        """Get NPC-specific behavior rules. Must be implemented by subclasses."""

    def schedule_idle_movement(self) -> bool:
        """
        Schedule idle movement for NPCs that support it.

        Default implementation returns False for NPCs that don't support
        idle movement (e.g., shopkeepers). Subclasses like PassiveMobNPC
        should override this method to implement movement scheduling.

        Returns:
            bool: True if movement was scheduled, False otherwise
        """
        return False

    async def execute_behavior(self, context: dict[str, Any]) -> bool:
        """Execute NPC behavior based on context."""
        try:
            if not self.is_active or not self.is_alive:
                return False

            # Add timing context
            current_time = time.time()
            context["time_since_last_action"] = current_time - self._last_action_time
            context["current_time"] = current_time

            # Add NPC-specific context
            # CRITICAL FIX: NPC stats use "determination_points"
            # Support backward compatibility with "dp" and "determination_points" for behavior rule evaluation
            dp_value = self._stats.get(
                "determination_points", self._stats.get("dp", self._stats.get("determination_points", 0))
            )
            context["dp"] = dp_value  # Keep "dp" key for backward compatibility with behavior rules
            context["determination_points"] = dp_value  # Add new key
            context["current_room"] = self.current_room
            context["is_alive"] = self.is_alive
            context["is_active"] = self.is_active

            # Add behavior config values to context for behavior rule evaluation
            context["idle_movement_enabled"] = self._behavior_config.get("idle_movement_enabled", False)
            context["idle_movement_interval"] = self._behavior_config.get("idle_movement_interval", 10)
            context["idle_movement_probability"] = self._behavior_config.get("idle_movement_probability", 0.25)
            context["in_combat"] = False  # Will be checked by schedule_idle_movement if needed
            context["flee_threshold"] = self._behavior_config.get("flee_threshold", 20)  # For aggressive mobs

            # Check and schedule idle movement for mob types
            if self.npc_type in ["passive_mob", "aggressive_mob"]:
                self.schedule_idle_movement()

            # Execute behavior rules
            result = self._behavior_engine.execute_applicable_rules(context)

            # Update last action time
            self._last_action_time = current_time

            return result

        except (TypeError, KeyError, AttributeError) as e:
            logger.error("Error executing behavior", npc_id=self.npc_id, error=str(e), error_type=type(e).__name__)
            return False

    def to_dict(self) -> dict[str, Any]:
        """Convert NPC to dictionary for serialization."""
        # Use getattr to safely access definition.id to avoid recursion issues
        definition_id = getattr(self.definition, "id", 0)
        return {
            "npc_id": self.npc_id,
            "definition_id": definition_id,
            "current_room": self.current_room,
            "stats": self._stats,
            "inventory": self._inventory,
            "is_alive": self.is_alive,
            "is_active": self.is_active,
            "last_action_time": self._last_action_time,
        }

    @classmethod
    def from_dict(cls, data: dict[str, Any], definition: NPCDefinition) -> "NPCBase":
        """Create NPC from dictionary data."""
        npc = cls(definition, data["npc_id"])
        # Use getattr to safely access definition.room_id to avoid recursion issues
        npc.current_room = data.get("current_room", getattr(definition, "room_id", None))
        npc._stats = data.get("stats", {})
        npc._inventory = data.get("inventory", [])
        npc.is_alive = data.get("is_alive", True)
        npc.is_active = data.get("is_active", True)
        npc._last_action_time = data.get("last_action_time", time.time())
        return npc

    # Base action handlers
    def _handle_die(self, _context: dict[str, Any]) -> bool:
        """Handle death action."""
        self.is_alive = False
        self.is_active = False
        logger.info("NPC died", npc_id=self.npc_id)
        return True

    def _handle_idle(self, _context: dict[str, Any]) -> bool:
        """Handle idle action."""
        logger.debug("NPC is idle", npc_id=self.npc_id)
        return True

    # AI integration stubs
    def generate_ai_response(self, input_text: str) -> str:
        """Generate AI response (placeholder for future implementation)."""
        if self._ai_config.get("ai_enabled", False):
            # Placeholder for AI integration
            return f"[AI Response to: {input_text}]"
        else:
            return "I don't understand."

    def make_ai_decision(self, _context: dict[str, Any]) -> dict[str, Any]:
        """Make AI decision (placeholder for future implementation)."""
        if self._ai_config.get("ai_enabled", False):
            # Placeholder for AI decision making
            return {"action": "idle", "confidence": 0.5}
        else:
            return {"action": "idle", "confidence": 1.0}

    def learn_from_interaction(self, player_id: str, feedback: str) -> bool:
        """Learn from interaction (placeholder for future implementation)."""
        if self._ai_config.get("ai_enabled", False):
            # Placeholder for AI learning
            logger.debug("AI learning from interaction", npc_id=self.npc_id, player_id=player_id, feedback=feedback)
            return True
        else:
            return False
