"""Base NPC class with stats, inventory, communication, and behavior framework."""

# pylint: disable=too-many-lines,too-many-public-methods  # Reason: NPC base requires extensive base functionality; many public methods for comprehensive NPC operations

import json
import time
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Any, cast

from ..models.npc import NPCDefinition
from ..structured_logging.enhanced_logging_config import get_logger
from .behavior_engine import BehaviorEngine

if TYPE_CHECKING:
    from ..events import EventBus
    from .event_reaction_system import NPCEventReactionSystem

logger = get_logger(__name__)


class NPCBase(ABC):  # pylint: disable=too-many-instance-attributes  # Reason: NPC base requires many fields for complete state
    """Base class for all NPCs with stats, inventory, communication, and behavior."""

    def __init__(
        self,
        definition: Any,
        npc_id: str,
        event_bus: "EventBus | None" = None,
        event_reaction_system: "NPCEventReactionSystem | None" = None,
    ) -> None:
        """Initialize the NPC base class."""
        self.npc_id = npc_id
        self.definition = definition
        self.current_room: str | None = None  # Set by _apply_definition_attributes
        self._apply_definition_attributes(definition)
        self._alive = True
        self.is_active = True

        self._stats = self._parse_stats(self._safe_get(definition, "base_stats", "{}"))
        self._behavior_config = self._parse_behavior_config(self._safe_get(definition, "behavior_config", "{}"))
        self._ai_config = self._parse_ai_config(self._safe_get(definition, "ai_integration_stub", "{}"))

        self._normalize_determination_points()

        self._inventory: list[dict[str, Any]] = []
        self._behavior_engine = BehaviorEngine()
        self._setup_base_behavior_rules()
        self._last_action_time = time.time()
        self._last_idle_movement_time: float | None = None
        self.event_bus = event_bus
        self.event_reaction_system = event_reaction_system
        self.movement_integration: Any | None = None
        self.combat_integration: Any | None = None
        self.communication_integration: Any | None = None

        # Register default event reactions if reaction system is available
        if self.event_reaction_system:
            self._register_default_reactions()

    @staticmethod
    def _safe_get(obj: Any, attr: str, default: Any) -> Any:
        """Get attribute from obj with default to avoid lazy-loading issues."""
        return getattr(obj, attr, default)

    def _apply_definition_attributes(self, definition: Any) -> None:
        """Set npc_type, name, current_room, spawn_room_id from definition."""
        self.npc_type = self._safe_get(definition, "npc_type", "unknown")
        self.name = self._safe_get(definition, "name", "Unknown NPC")
        self.current_room = self._safe_get(definition, "room_id", None)
        room_id = self._safe_get(definition, "room_id", None)
        self.spawn_room_id = room_id if room_id is not None else self.current_room

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

    def _apply_dp_from_source(self, source_key: str, max_dp_from: str | None = None) -> bool:
        """Set determination_points from source_key; optionally set max_dp. Returns True if applied."""
        if source_key not in self._stats:
            return False
        self._stats["determination_points"] = self._stats[source_key]
        if "max_dp" not in self._stats and max_dp_from:
            if max_dp_from == "max_hp" and "max_hp" in self._stats:
                self._stats["max_dp"] = self._stats["max_hp"]
            elif max_dp_from == "health" and "max_hp" not in self._stats:
                self._stats["max_dp"] = self._stats[source_key]
        return True

    def _normalize_determination_points(self) -> None:
        """Ensure _stats has determination_points; support hp/dp backward compat."""
        if "determination_points" in self._stats:
            return
        if (
            self._apply_dp_from_source("dp")
            or self._apply_dp_from_source("hp", "max_hp")
            or self._apply_dp_from_source("health", "health")
        ):
            return
        self._stats["determination_points"] = 20  # Default DP

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
        """Apply default idle movement config based on NPC type."""
        if "idle_movement_enabled" not in config:
            config["idle_movement_enabled"] = self.npc_type in ["passive_mob", "aggressive_mob"]
        if "idle_movement_interval" not in config:
            config["idle_movement_interval"] = 100
        if "idle_movement_probability" not in config:
            config["idle_movement_probability"] = 0.25
        if "idle_movement_weighted_home" not in config:
            config["idle_movement_weighted_home"] = True

    def _parse_ai_config(self, ai_json: str) -> dict[str, Any]:
        """Parse AI integration configuration from JSON string."""
        try:
            return json.loads(ai_json) if ai_json else {}
        except json.JSONDecodeError:
            logger.warning("Invalid AI config JSON, using defaults", npc_id=self.npc_id)
            return {"ai_enabled": False, "ai_model": None}

    def _setup_base_behavior_rules(self) -> None:
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
        self._behavior_engine.register_action_handler("die", self._handle_die)
        self._behavior_engine.register_action_handler("idle", self._handle_idle)

    def get_stats(self) -> dict[str, Any]:
        """Get current NPC stats."""
        return self._stats.copy()

    @property
    def is_alive(self) -> bool:
        """Return True if NPC is alive (determination_points > 0)."""
        return bool(self._alive)

    @is_alive.setter
    def is_alive(self, value: bool) -> None:
        """Allow backward-compatible assignment (npc.is_alive = False)."""
        self._alive = value

    def _safe_stat_int(self, key: str, default: int = 50) -> int:
        """Return stats[key] as int, or default if missing/None."""
        val = self._stats.get(key)
        return default if val is None else int(val)

    def _compute_max_dp(self) -> int:
        """Compute max_dp from stats when max_dp/max_hp not explicitly set."""
        max_dp_raw = self._stats.get("max_dp")
        max_hp_raw = self._stats.get("max_hp")
        if max_dp_raw is not None or max_hp_raw is not None:
            raw = max_dp_raw if max_dp_raw is not None else max_hp_raw
            return int(raw) if raw is not None else 100
        if "constitution" in self._stats and "size" in self._stats:
            return (self._safe_stat_int("constitution") + self._safe_stat_int("size")) // 5
        return 100

    def get_combat_stats(self) -> dict[str, int]:
        """Return current_dp, max_dp, dexterity for CombatParticipantData."""
        current_dp = self._stats.get("determination_points", self._stats.get("dp", self._stats.get("hp", 100)))
        max_dp = self._compute_max_dp()
        dexterity = self._stats.get("dexterity", 10)
        return {
            "current_dp": int(current_dp),
            "max_dp": max_dp,
            "dexterity": int(dexterity),
        }

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
        """Update determination points after taking damage; return new DP."""
        current_dp = self._stats.get(
            "determination_points", self._stats.get("dp", self._stats.get("determination_points", 0))
        )
        new_dp = max(0, current_dp - damage)
        self._stats["determination_points"] = new_dp
        if "dp" in self._stats:
            self._stats["dp"] = new_dp
        if "determination_points" in self._stats:
            self._stats["determination_points"] = new_dp
        return cast(int, new_dp)

    def _publish_damage_event(self, damage: int, damage_type: str, source_id: str | None) -> None:
        """Publish damage event to event bus."""
        if not self.event_bus:
            return

        from ..events.event_types import NPCTookDamage

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
        """Handle NPC death after taking fatal damage."""
        self._alive = False
        logger.info("NPC died", npc_id=self.npc_id, damage=damage)

        # Use combat integration for death handling
        if hasattr(self, "combat_integration") and self.combat_integration:
            self.combat_integration.handle_npc_death(self.npc_id, self.current_room, "damage", source_id)
        else:
            if self.event_bus:
                from ..events.event_types import NPCDied

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
        """Return (event_bus, persistence) for movement integration, or (None, None)."""
        event_bus = getattr(self, "_event_bus", None)
        persistence = None

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

    def _is_npc_in_combat(self) -> bool:
        """Return True if NPC is in combat (blocks movement); False on lookup failure."""
        try:
            from ..services.combat_service import get_combat_service

            combat_service = get_combat_service()
            if combat_service:
                return combat_service.is_npc_in_combat_sync(self.npc_id)
        except (ImportError, AttributeError, RuntimeError):
            pass
        return False

    def _move_with_integration(self, room_id: str) -> bool:
        """Move NPC using movement integration; return True if successful."""
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
        """Move NPC without integration (simple room update)."""
        self.current_room = room_id
        logger.debug("NPC moved to room (simple)", npc_id=self.npc_id, room_id=room_id)
        return True

    def move_to_room(self, room_id: str, use_integration: bool = True) -> bool:
        """Move NPC to a room; blocked in combat. Return True if successful."""
        try:
            if self._is_npc_in_combat():
                logger.debug(
                    "NPC movement blocked - NPC in combat",
                    npc_id=self.npc_id,
                    room_id=room_id,
                )
                return False
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
                    result: bool = cast(
                        bool,
                        self.communication_integration.send_whisper_to_player(
                            self.npc_id, target_id, message, self.current_room
                        ),
                    )
                    return result
                # Send message to room
                result2: bool = cast(
                    bool,
                    self.communication_integration.send_message_to_room(
                        self.npc_id, self.current_room, message, channel
                    ),
                )
                return result2
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
                result: bool = cast(
                    bool,
                    self.communication_integration.handle_player_message(
                        self.npc_id, speaker_id, message, self.current_room, channel
                    ),
                )
                return result

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

            # No event bus available
            return False

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

            if self.npc_type in ["shopkeeper", "passive_mob"]:
                farewell = self._behavior_config.get("farewell_message", "Goodbye!")
                reactions.append(NPCEventReactionTemplates.player_left_room_farewell(self.npc_id, farewell))

            if self.npc_type == "aggressive_mob":
                reactions.append(NPCEventReactionTemplates.npc_attacked_retaliation(self.npc_id))

            if self.npc_type in ["shopkeeper", "passive_mob"]:
                response = self._behavior_config.get("response_message", "I heard you!")
                reactions.append(NPCEventReactionTemplates.player_spoke_response(self.npc_id, response))

            if reactions:
                self.event_reaction_system.register_npc_reactions(self.npc_id, reactions)
                logger.debug("Registered default reactions", npc_id=self.npc_id, reaction_count=len(reactions))

        except (ImportError, AttributeError, TypeError) as e:
            logger.error(
                "Error registering default reactions", npc_id=self.npc_id, error=str(e), error_type=type(e).__name__
            )

    def get_npc_context(self) -> dict[str, Any]:
        """Return context for event reactions."""
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
        """Schedule idle movement; default False. Override in subclasses (e.g. PassiveMobNPC)."""
        return False

    def _enrich_behavior_context(self, _context: dict[str, Any]) -> None:
        """
        Hook for subclasses to add context before behavior rules run.
        Override in AggressiveMobNPC to set player_in_range, enemy_nearby, target_id.
        """
        # Default: no-op. AggressiveMobNPC overrides to populate player detection.
        return None

    async def execute_behavior(self, context: dict[str, Any]) -> bool:
        """Execute NPC behavior based on context."""
        try:
            if not self.is_active or not self.is_alive:
                return False

            current_time = time.time()
            context["time_since_last_action"] = current_time - self._last_action_time
            context["current_time"] = current_time

            dp_value = self._stats.get(
                "determination_points", self._stats.get("dp", self._stats.get("determination_points", 0))
            )
            context["dp"] = dp_value
            context["determination_points"] = dp_value
            context["current_room"] = self.current_room
            context["is_alive"] = self.is_alive
            context["is_active"] = self.is_active

            context["idle_movement_enabled"] = self._behavior_config.get("idle_movement_enabled", False)
            context["idle_movement_interval"] = self._behavior_config.get("idle_movement_interval", 10)
            context["idle_movement_probability"] = self._behavior_config.get("idle_movement_probability", 0.25)
            context["in_combat"] = False  # Will be checked by schedule_idle_movement if needed
            context["flee_threshold"] = self._behavior_config.get("flee_threshold", 20)
            if self.npc_type in ["passive_mob", "aggressive_mob"]:
                self.schedule_idle_movement()
            self._enrich_behavior_context(context)
            result = self._behavior_engine.execute_applicable_rules(context)
            self._last_action_time = current_time

            return result

        except (TypeError, KeyError, AttributeError) as e:
            logger.error("Error executing behavior", npc_id=self.npc_id, error=str(e), error_type=type(e).__name__)
            return False

    def to_dict(self) -> dict[str, Any]:
        """Convert NPC to dictionary for serialization."""
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
        npc.current_room = data.get("current_room", getattr(definition, "room_id", None))
        npc._stats = data.get("stats", {})
        npc._inventory = data.get("inventory", [])
        npc._alive = data.get("is_alive", True)
        npc.is_active = data.get("is_active", True)
        npc._last_action_time = data.get("last_action_time", time.time())
        return npc

    # Base action handlers
    def _handle_die(self, _context: dict[str, Any]) -> bool:
        """Handle death action."""
        self._alive = False
        self.is_active = False
        logger.info("NPC died", npc_id=self.npc_id)
        return True

    def _handle_idle(self, _context: dict[str, Any]) -> bool:
        """Handle idle action."""
        logger.debug("NPC is idle", npc_id=self.npc_id)
        return True

    def generate_ai_response(self, input_text: str) -> str:
        """Generate AI response (placeholder for future implementation)."""
        if self._ai_config.get("ai_enabled", False):
            # Placeholder for AI integration
            return f"[AI Response to: {input_text}]"
        return "I don't understand."

    def make_ai_decision(self, _context: dict[str, Any]) -> dict[str, Any]:
        """Make AI decision (placeholder for future implementation)."""
        if self._ai_config.get("ai_enabled", False):
            # Placeholder for AI decision making
            return {"action": "idle", "confidence": 0.5}
        return {"action": "idle", "confidence": 1.0}

    def learn_from_interaction(self, player_id: str, feedback: str) -> bool:
        """Learn from interaction (placeholder for future implementation)."""
        if self._ai_config.get("ai_enabled", False):
            # Placeholder for AI learning
            logger.debug("AI learning from interaction", npc_id=self.npc_id, player_id=player_id, feedback=feedback)
            return True
        return False
