"""
NPC behavior system for MythosMUD.

This module provides the core NPC behavior system including base classes,
behavior engines, and specific NPC type implementations.

As noted in the Pnakotic Manuscripts, proper behavioral programming is essential
for maintaining the delicate balance between order and chaos in our eldritch
entity management systems.
"""

import json
import time
from abc import ABC, abstractmethod
from collections.abc import Callable
from typing import Any

from ..logging.enhanced_logging_config import get_logger
from ..models.npc import NPCDefinition

logger = get_logger(__name__)


class BehaviorEngine:
    """
    Deterministic behavior engine for NPCs.

    This engine evaluates rules based on context and executes actions
    in a deterministic, priority-based manner.
    """

    def __init__(self):
        """Initialize the behavior engine."""
        self.rules: list[dict[str, Any]] = []
        self.action_handlers: dict[str, Callable] = {}
        self.state: dict[str, Any] = {}

        logger.debug("Behavior engine initialized", engine_id=id(self))

    def add_rule(self, rule: dict[str, Any]) -> bool:
        """
        Add a behavior rule to the engine.

        Args:
            rule: Rule dictionary with name, condition, action, and priority

        Returns:
            bool: True if rule was added successfully
        """
        try:
            required_fields = ["name", "condition", "action", "priority"]
            if not all(field in rule for field in required_fields):
                logger.error("Rule missing required fields", rule=rule)
                return False

            # Remove existing rule with same name
            self.rules = [r for r in self.rules if r["name"] != rule["name"]]

            # Add new rule
            self.rules.append(rule)
            logger.debug(
                "Added behavior rule",
                rule_name=rule["name"],
                priority=rule.get("priority", 0),
                total_rules=len(self.rules),
            )
            return True

        except Exception as e:
            logger.error("Error adding behavior rule", error=str(e))
            return False

    def remove_rule(self, rule_name: str) -> bool:
        """
        Remove a behavior rule from the engine.

        Args:
            rule_name: Name of the rule to remove

        Returns:
            bool: True if rule was removed successfully
        """
        try:
            original_count = len(self.rules)
            self.rules = [r for r in self.rules if r["name"] != rule_name]

            if len(self.rules) < original_count:
                logger.debug("Removed behavior rule", rule_name=rule_name)
                return True
            else:
                logger.warning("Rule not found for removal", rule_name=rule_name)
                return False

        except Exception as e:
            logger.error("Error removing behavior rule", error=str(e))
            return False

    def get_rules(self) -> list[dict[str, Any]]:
        """Get all behavior rules."""
        return self.rules.copy()

    def evaluate_condition(self, condition: str, context: dict[str, Any]) -> bool:
        """
        Evaluate a condition string against context.

        Args:
            condition: Condition string to evaluate
            context: Context dictionary with variables

        Returns:
            bool: True if condition is met
        """
        try:
            logger.debug("Evaluating behavior condition", condition=condition, context_keys=list(context.keys()))
            # Simple condition evaluation (can be enhanced with more complex logic)
            if "==" in condition:
                parts = condition.split("==")
                if len(parts) == 2:
                    var_name = parts[0].strip()
                    expected_value = parts[1].strip().strip("\"'")
                    context_value = context.get(var_name, "")
                    # Handle boolean values properly
                    if expected_value.lower() in ["true", "false"]:
                        return bool(context_value) == (expected_value.lower() == "true")
                    return str(context_value) == expected_value

            elif "!=" in condition:
                parts = condition.split("!=")
                if len(parts) == 2:
                    var_name = parts[0].strip()
                    expected_value = parts[1].strip().strip("\"'")
                    return str(context.get(var_name, "")) != expected_value

            elif ">" in condition:
                parts = condition.split(">")
                if len(parts) == 2:
                    var_name = parts[0].strip()
                    threshold = float(parts[1].strip())
                    return float(context.get(var_name, 0)) > threshold

            elif "<" in condition:
                parts = condition.split("<")
                if len(parts) == 2:
                    var_name = parts[0].strip()
                    threshold = float(parts[1].strip())
                    return float(context.get(var_name, 0)) < threshold

            elif ">=" in condition:
                parts = condition.split(">=")
                if len(parts) == 2:
                    var_name = parts[0].strip()
                    threshold = float(parts[1].strip())
                    return float(context.get(var_name, 0)) >= threshold

            elif "<=" in condition:
                parts = condition.split("<=")
                if len(parts) == 2:
                    var_name = parts[0].strip()
                    threshold = float(parts[1].strip())
                    return float(context.get(var_name, 0)) <= threshold

            # Boolean conditions
            elif condition == "true":
                return True
            elif condition == "false":
                return False
            else:
                # Treat as boolean variable
                return bool(context.get(condition, False))

            # Fallback for malformed conditions
            return False

        except Exception as e:
            logger.error(
                "Error evaluating condition", condition=condition, context_keys=list(context.keys()), error=str(e)
            )
            return False

    def get_applicable_rules(self, context: dict[str, Any]) -> list[dict[str, Any]]:
        """
        Get rules that are applicable given the current context.

        Args:
            context: Current context dictionary

        Returns:
            List of applicable rules sorted by priority (highest first)
        """
        applicable_rules = []

        for rule in self.rules:
            if self.evaluate_condition(rule["condition"], context):
                applicable_rules.append(rule)

        # Sort by priority (highest first)
        applicable_rules.sort(key=lambda r: r["priority"], reverse=True)
        return applicable_rules

    def register_action_handler(self, action_name: str, handler: Callable) -> bool:
        """
        Register an action handler for a specific action.

        Args:
            action_name: Name of the action
            handler: Function to handle the action

        Returns:
            bool: True if handler was registered successfully
        """
        try:
            self.action_handlers[action_name] = handler
            # Temporarily disable logging to avoid potential recursion issues
            # logger.debug("Registered action handler", action_name=action_name)
            return True
        except Exception as e:
            logger.error("Error registering action handler", action_name=action_name, error=str(e))
            return False

    def execute_action(self, action_name: str, context: dict[str, Any]) -> bool:
        """
        Execute a specific action.

        Args:
            action_name: Name of the action to execute
            context: Context for the action

        Returns:
            bool: True if action was executed successfully
        """
        try:
            if action_name not in self.action_handlers:
                logger.warning("No handler registered for action", action_name=action_name)
                return False

            handler = self.action_handlers[action_name]
            result = handler(context)
            logger.debug("Executed action", action_name=action_name, result=result)
            return result

        except Exception as e:
            logger.error("Error executing action", action_name=action_name, error=str(e))
            return False

    def execute_applicable_rules(self, context: dict[str, Any]) -> bool:
        """
        Execute all applicable rules based on context.

        Args:
            context: Current context dictionary

        Returns:
            bool: True if at least one rule was executed successfully
        """
        try:
            applicable_rules = self.get_applicable_rules(context)

            if not applicable_rules:
                logger.debug(
                    "No applicable rules found for context",
                    context_keys=list(context.keys()),
                    total_rules=len(self.rules),
                )
                return True  # No rules to execute is considered success

            # Execute highest priority rule only (deterministic behavior)
            highest_priority_rule = applicable_rules[0]
            logger.debug(
                "Executing highest priority rule",
                rule_name=highest_priority_rule["name"],
                priority=highest_priority_rule["priority"],
                action=highest_priority_rule["action"],
            )

            result = self.execute_action(highest_priority_rule["action"], context)
            logger.debug("Rule execution completed", rule_name=highest_priority_rule["name"], success=result)
            return result

        except Exception as e:
            logger.error(
                "Error executing applicable rules",
                context_keys=list(context.keys()),
                total_rules=len(self.rules),
                error=str(e),
            )
            return False


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
        self.is_alive = True
        self.is_active = True

        # Parse configuration from definition - use getattr to avoid lazy loading issues
        self._stats = self._parse_stats(getattr(definition, "base_stats", "{}"))
        self._behavior_config = self._parse_behavior_config(getattr(definition, "behavior_config", "{}"))
        self._ai_config = self._parse_ai_config(getattr(definition, "ai_integration_stub", "{}"))

        # Initialize inventory
        self._inventory: list[dict[str, Any]] = []

        # Initialize behavior engine
        self._behavior_engine = BehaviorEngine()
        self._setup_base_behavior_rules()

        # Track last action time for behavior timing
        self._last_action_time = time.time()

        # Initialize event system integration
        self.event_bus = event_bus
        self.event_reaction_system = event_reaction_system

        # Initialize integration systems (will be set by external systems)
        self.movement_integration = None
        self.combat_integration = None
        self.communication_integration = None

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
            return {"hp": 100, "strength": 10, "intelligence": 8, "charisma": 6}

    def _parse_behavior_config(self, config_json: str) -> dict[str, Any]:
        """Parse behavior configuration from JSON string."""
        try:
            return json.loads(config_json) if config_json else {}
        except json.JSONDecodeError:
            logger.warning("Invalid behavior config JSON, using defaults", npc_id=self.npc_id)
            return {}

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
                "condition": "hp <= 0",
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
        except Exception as e:
            logger.error("Error adding item to inventory", npc_id=self.npc_id, error=str(e))
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
        except Exception as e:
            logger.error("Error removing item from inventory", npc_id=self.npc_id, error=str(e))
            return False

    def get_item_from_inventory(self, item_id: str) -> dict[str, Any] | None:
        """Get specific item from inventory."""
        for item in self._inventory:
            if item.get("id") == item_id:
                return item
        return None

    def take_damage(self, damage: int, damage_type: str = "physical", source_id: str | None = None) -> bool:
        """Take damage and update health."""
        try:
            if not self.is_alive:
                return False

            current_hp = self._stats.get("hp", 0)
            new_hp = max(0, current_hp - damage)
            self._stats["hp"] = new_hp

            # Publish damage event
            if self.event_bus:
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

            if new_hp <= 0:
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
            else:
                logger.debug("NPC took damage", npc_id=self.npc_id, damage=damage, new_hp=new_hp)

            return True
        except Exception as e:
            logger.error("Error taking damage", npc_id=self.npc_id, error=str(e))
            return False

    def heal(self, amount: int) -> bool:
        """Heal and update health."""
        try:
            if not self.is_alive:
                return False

            current_hp = self._stats.get("hp", 0)
            max_hp = self._stats.get("max_hp", 100)
            new_hp = min(max_hp, current_hp + amount)
            self._stats["hp"] = new_hp

            logger.debug("NPC healed", npc_id=self.npc_id, amount=amount, new_hp=new_hp)
            return True
        except Exception as e:
            logger.error("Error healing", npc_id=self.npc_id, error=str(e))
            return False

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
                # Use the movement integration system for enhanced functionality
                from .movement_integration import NPCMovementIntegration

                # Get event bus from persistence if available
                event_bus = getattr(self, "_event_bus", None)
                if not event_bus and hasattr(self, "definition"):
                    # Try to get event bus from persistence
                    try:
                        from ..persistence import get_persistence

                        persistence = get_persistence()
                        event_bus = getattr(persistence, "_event_bus", None)
                    except (ImportError, AttributeError, RuntimeError) as e:
                        logger.error(
                            "Error getting persistence or event bus", error=str(e), error_type=type(e).__name__
                        )
                        pass

                movement_integration = NPCMovementIntegration(event_bus)
                success = movement_integration.move_npc_to_room(self.npc_id, self.current_room or "unknown", room_id)

                if success:
                    self.current_room = room_id
                    logger.debug("NPC moved to room with integration", npc_id=self.npc_id, room_id=room_id)
                    return True
                else:
                    logger.warning("NPC movement failed with integration", npc_id=self.npc_id, room_id=room_id)
                    return False
            else:
                # Simple movement without integration
                self.current_room = room_id
                logger.debug("NPC moved to room (simple)", npc_id=self.npc_id, room_id=room_id)
                return True

        except Exception as e:
            logger.error("Error moving NPC", npc_id=self.npc_id, error=str(e))
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

        except Exception as e:
            logger.error("Error NPC speaking", npc_id=self.npc_id, error=str(e))
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

        except Exception as e:
            logger.error("Error NPC listening", npc_id=self.npc_id, error=str(e))
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

        except Exception as e:
            logger.error("Error registering default reactions", npc_id=self.npc_id, error=str(e))

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
        pass

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
            context["hp"] = self._stats.get("hp", 0)
            context["current_room"] = self.current_room
            context["is_alive"] = self.is_alive
            context["is_active"] = self.is_active

            # Execute behavior rules
            result = self._behavior_engine.execute_applicable_rules(context)

            # Update last action time
            self._last_action_time = current_time

            return result

        except Exception as e:
            logger.error("Error executing behavior", npc_id=self.npc_id, error=str(e))
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
    def _handle_die(self, context: dict[str, Any]) -> bool:
        """Handle death action."""
        self.is_alive = False
        self.is_active = False
        logger.info("NPC died", npc_id=self.npc_id)
        return True

    def _handle_idle(self, context: dict[str, Any]) -> bool:
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

    def make_ai_decision(self, context: dict[str, Any]) -> dict[str, Any]:
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


class ShopkeeperNPC(NPCBase):
    """Shopkeeper NPC type with buy/sell functionality."""

    def __init__(self, definition: Any, npc_id: str, event_bus=None, event_reaction_system=None):
        """Initialize shopkeeper NPC."""
        super().__init__(definition, npc_id, event_bus, event_reaction_system)
        self._shop_inventory: list[dict[str, Any]] = []
        self._buyable_items: dict[str, int] = {}  # item_id -> base_price
        self._setup_shopkeeper_behavior_rules()

    def _setup_shopkeeper_behavior_rules(self):
        """Setup shopkeeper-specific behavior rules."""
        shopkeeper_rules = [
            {
                "name": "greet_customer",
                "condition": "player_nearby == true",
                "action": "greet_customer",
                "priority": 5,
            },
            {
                "name": "restock_inventory",
                "condition": "time_since_last_action > 3600",
                "action": "restock_inventory",
                "priority": 3,
            },
        ]

        for rule in shopkeeper_rules:
            self._behavior_engine.add_rule(rule)

        # Register shopkeeper action handlers
        self._behavior_engine.register_action_handler("greet_customer", self._handle_greet_customer)
        self._behavior_engine.register_action_handler("restock_inventory", self._handle_restock_inventory)

    def get_behavior_rules(self) -> list[dict[str, Any]]:
        """Get shopkeeper-specific behavior rules."""
        return self._behavior_engine.get_rules()

    def get_shop_inventory(self) -> list[dict[str, Any]]:
        """Get shop inventory."""
        return self._shop_inventory.copy()

    def add_shop_item(self, item: dict[str, Any]) -> bool:
        """Add item to shop inventory."""
        try:
            self._shop_inventory.append(item)
            logger.debug("Added item to shop inventory", npc_id=self.npc_id, item_id=item.get("id"))
            return True
        except Exception as e:
            logger.error("Error adding item to shop inventory", npc_id=self.npc_id, error=str(e))
            return False

    def add_buyable_item(self, item_id: str, base_price: int) -> bool:
        """Add item to buyable items list."""
        try:
            self._buyable_items[item_id] = base_price
            logger.debug("Added buyable item", npc_id=self.npc_id, item_id=item_id, base_price=base_price)
            return True
        except Exception as e:
            logger.error("Error adding buyable item", npc_id=self.npc_id, error=str(e))
            return False

    def buy_from_player(self, player_id: str, item: dict[str, Any]) -> bool:
        """Buy item from player."""
        try:
            item_id = item.get("id")
            if item_id not in self._buyable_items:
                logger.warning("Item not in buyable list", npc_id=self.npc_id, item_id=item_id)
                return False

            # Add to NPC inventory
            self.add_item_to_inventory(item)
            logger.info("Bought item from player", npc_id=self.npc_id, player_id=player_id, item_id=item_id)
            return True
        except Exception as e:
            logger.error("Error buying from player", npc_id=self.npc_id, error=str(e))
            return False

    def sell_to_player(self, player_id: str, item_id: str, quantity: int = 1) -> bool:
        """Sell item to player."""
        try:
            # Find item in shop inventory
            for item in self._shop_inventory:
                if item.get("id") == item_id and item.get("quantity", 0) >= quantity:
                    # Reduce quantity
                    item["quantity"] = item.get("quantity", 0) - quantity
                    if item["quantity"] <= 0:
                        self._shop_inventory.remove(item)

                    logger.info(
                        "Sold item to player",
                        npc_id=self.npc_id,
                        player_id=player_id,
                        item_id=item_id,
                        quantity=quantity,
                    )
                    return True

            logger.warning("Item not available for sale", npc_id=self.npc_id, item_id=item_id)
            return False
        except Exception as e:
            logger.error("Error selling to player", npc_id=self.npc_id, error=str(e))
            return False

    def calculate_price(self, base_price: int, markup: float = None) -> int:
        """Calculate final price with markup."""
        if markup is None:
            markup = self._behavior_config.get("markup", 1.0)
        return int(base_price * markup)

    def _handle_greet_customer(self, context: dict[str, Any]) -> bool:
        """Handle greeting customer action."""
        self.speak("Welcome to my shop! How may I help you today?")
        return True

    def _handle_restock_inventory(self, context: dict[str, Any]) -> bool:
        """Handle restocking inventory action."""
        # Placeholder for restocking logic
        logger.debug("Restocking shop inventory", npc_id=self.npc_id)
        return True


class PassiveMobNPC(NPCBase):
    """Passive mob NPC type with wandering and response behaviors."""

    def __init__(self, definition: Any, npc_id: str, event_bus=None, event_reaction_system=None):
        """Initialize passive mob NPC."""
        super().__init__(definition, npc_id, event_bus, event_reaction_system)
        self._setup_passive_mob_behavior_rules()

    def _setup_passive_mob_behavior_rules(self):
        """Setup passive mob-specific behavior rules."""
        passive_mob_rules = [
            {
                "name": "wander_periodically",
                "condition": "time_since_last_action > wander_interval",
                "action": "wander",
                "priority": 2,
            },
            {
                "name": "respond_to_greeting",
                "condition": "player_greeted == true",
                "action": "respond_to_greeting",
                "priority": 4,
            },
            {
                "name": "avoid_conflict",
                "condition": "threat_detected == true",
                "action": "flee",
                "priority": 6,
            },
        ]

        for rule in passive_mob_rules:
            self._behavior_engine.add_rule(rule)

        # Register passive mob action handlers
        self._behavior_engine.register_action_handler("wander", self._handle_wander)
        self._behavior_engine.register_action_handler("respond_to_greeting", self._handle_respond_to_greeting)
        self._behavior_engine.register_action_handler("flee", self._handle_flee)

    def get_behavior_rules(self) -> list[dict[str, Any]]:
        """Get passive mob-specific behavior rules."""
        return self._behavior_engine.get_rules()

    def wander(self) -> bool:
        """Perform wandering behavior."""
        try:
            # Placeholder for wandering logic
            logger.debug("NPC is wandering", npc_id=self.npc_id)
            return True
        except Exception as e:
            logger.error("Error wandering", npc_id=self.npc_id, error=str(e))
            return False

    def respond_to_player(self, player_id: str, interaction_type: str) -> bool:
        """Respond to player interaction."""
        try:
            response_chance = self._behavior_config.get("response_chance", 0.5)
            if response_chance > 0.5:  # Simple probability check
                self.speak(f"Hello there, {player_id}!")
                logger.debug("NPC responded to player", npc_id=self.npc_id, player_id=player_id)
                return True
            return False
        except Exception as e:
            logger.error("Error responding to player", npc_id=self.npc_id, error=str(e))
            return False

    def _handle_wander(self, context: dict[str, Any]) -> bool:
        """Handle wandering action."""
        return self.wander()

    def _handle_respond_to_greeting(self, context: dict[str, Any]) -> bool:
        """Handle responding to greeting action."""
        player_id = context.get("player_id", "stranger")
        return self.respond_to_player(player_id, "greet")

    def _handle_flee(self, context: dict[str, Any]) -> bool:
        """Handle fleeing action."""
        self.speak("I must get away from here!")
        logger.debug("NPC is fleeing", npc_id=self.npc_id)
        return True


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
                "name": "flee_when_low_hp",
                "condition": "hp < flee_threshold",
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
        except Exception as e:
            logger.error("Error hunting target", npc_id=self.npc_id, error=str(e))
            return False

    def attack_target(self, target_id: str) -> bool:
        """Attack a specific target."""
        try:
            attack_damage = self._behavior_config.get("attack_damage", 20)
            logger.info("NPC attacked target", npc_id=self.npc_id, target_id=target_id, damage=attack_damage)

            # Use combat integration for attack handling
            if hasattr(self, "combat_integration") and self.combat_integration:
                success = self.combat_integration.handle_npc_attack(
                    self.npc_id, target_id, self.current_room, attack_damage, "physical", self.get_stats()
                )
                return success
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

        except Exception as e:
            logger.error("Error attacking target", npc_id=self.npc_id, error=str(e))
            return False

    def flee(self) -> bool:
        """Flee from current situation."""
        try:
            self.speak("I must retreat!")
            logger.debug("NPC is fleeing", npc_id=self.npc_id)
            return True
        except Exception as e:
            logger.error("Error fleeing", npc_id=self.npc_id, error=str(e))
            return False

    def patrol_territory(self) -> bool:
        """Patrol the NPC's territory."""
        try:
            logger.debug("NPC is patrolling territory", npc_id=self.npc_id)
            return True
        except Exception as e:
            logger.error("Error patrolling territory", npc_id=self.npc_id, error=str(e))
            return False

    def _handle_hunt_target(self, context: dict[str, Any]) -> bool:
        """Handle hunting target action."""
        target_id = context.get("target_id", "unknown")
        return self.hunt_target(target_id)

    def _handle_attack_target(self, context: dict[str, Any]) -> bool:
        """Handle attacking target action."""
        target_id = context.get("target_id", "unknown")
        return self.attack_target(target_id)

    def _handle_flee(self, context: dict[str, Any]) -> bool:
        """Handle fleeing action."""
        return self.flee()

    def _handle_patrol_territory(self, context: dict[str, Any]) -> bool:
        """Handle patrolling territory action."""
        return self.patrol_territory()
