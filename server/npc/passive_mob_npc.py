"""
Passive mob NPC type for MythosMUD.

This module provides the PassiveMobNPC class with wandering and response behaviors.
"""

import time
from typing import TYPE_CHECKING, Any

from ..structured_logging.enhanced_logging_config import get_logger
from .npc_base import NPCBase

if TYPE_CHECKING:
    from ..events import EventBus
    from .event_reaction_system import NPCEventReactionSystem

logger = get_logger(__name__)


class PassiveMobNPC(NPCBase):
    """Passive mob NPC type with wandering and response behaviors."""

    def __init__(
        self,
        definition: Any,
        npc_id: str,
        event_bus: "EventBus | None" = None,
        event_reaction_system: "NPCEventReactionSystem | None" = None,
    ) -> None:
        """Initialize passive mob NPC."""
        super().__init__(definition, npc_id, event_bus, event_reaction_system)
        self._setup_passive_mob_behavior_rules()

    def _setup_passive_mob_behavior_rules(self) -> None:
        """Setup passive mob-specific behavior rules."""
        # Note: Idle movement is handled by schedule_idle_movement() in execute_behavior(),
        # not through behavior rules, so we don't need a wander_periodically rule here.
        passive_mob_rules = [
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
        # Note: wander handler kept for backward compatibility, but idle movement uses schedule_idle_movement()
        self._behavior_engine.register_action_handler("wander", self._handle_wander)
        self._behavior_engine.register_action_handler("respond_to_greeting", self._handle_respond_to_greeting)
        self._behavior_engine.register_action_handler("flee", self._handle_flee)

    def get_behavior_rules(self) -> list[dict[str, Any]]:
        """Get passive mob-specific behavior rules."""
        return self._behavior_engine.get_rules()

    def wander(self) -> bool:
        """Perform wandering behavior using idle movement system."""
        try:
            # Use idle movement handler for wandering
            from ..container import ApplicationContainer
            from .idle_movement import IdleMovementHandler

            # Get async_persistence from container
            container = ApplicationContainer.get_instance()
            async_persistence = getattr(container, "async_persistence", None) if container else None

            if async_persistence is None:
                logger.error("async_persistence not available for idle movement", npc_id=self.npc_id)
                return False

            movement_handler = IdleMovementHandler(
                event_bus=self.event_bus,
                persistence=async_persistence,
            )

            # Get NPC definition
            definition = self.definition

            # Execute idle movement
            success = movement_handler.execute_idle_movement(self, definition, self._behavior_config)

            if success:
                self._last_idle_movement_time = time.time()
                logger.debug("NPC wandered successfully", npc_id=self.npc_id)
            else:
                logger.debug("NPC wander check did not result in movement", npc_id=self.npc_id)

            return success

        except (ImportError, AttributeError, RuntimeError, TypeError) as e:
            logger.error("Error wandering", npc_id=self.npc_id, error=str(e), error_type=type(e).__name__)
            return False

    def _should_schedule_movement(self, current_time: float) -> bool:
        """
        Check if idle movement should be scheduled based on configuration and timing.

        Args:
            current_time: Current timestamp

        Returns:
            bool: True if movement should be scheduled, False otherwise
        """
        if not self._behavior_config.get("idle_movement_enabled", False):
            return False

        movement_interval = self._behavior_config.get("idle_movement_interval", 10)

        # If this is the first time checking, allow scheduling
        if self._last_idle_movement_time is None:
            return True

        # Check if enough time has passed
        time_since_last = current_time - self._last_idle_movement_time
        if time_since_last < movement_interval:
            logger.debug(
                "Idle movement interval not elapsed",
                npc_id=self.npc_id,
                time_since_last=time_since_last,
                interval=movement_interval,
            )
            return False

        return True

    def _create_wander_action(self, current_time: float) -> Any:
        """
        Create a WANDER action message.

        Args:
            current_time: Current timestamp

        Returns:
            NPCActionMessage: The wander action message
        """
        from .threading import NPCActionMessage, NPCActionType

        return NPCActionMessage(
            action_type=NPCActionType.WANDER,
            npc_id=self.npc_id,
            timestamp=current_time,
        )

    def _queue_wander_action(self, wander_action: Any, current_time: float) -> bool:
        """
        Queue a WANDER action via the thread manager.

        Args:
            wander_action: The wander action message to queue
            current_time: Current timestamp

        Returns:
            bool: True if action was queued successfully, False otherwise
        """
        try:
            from ..services.npc_instance_service import get_npc_instance_service

            npc_instance_service = get_npc_instance_service()
            if not npc_instance_service or not hasattr(npc_instance_service, "lifecycle_manager"):
                return False

            lifecycle_manager = npc_instance_service.lifecycle_manager
            if not lifecycle_manager or not hasattr(lifecycle_manager, "thread_manager"):
                return False

            thread_manager = lifecycle_manager.thread_manager
            if not thread_manager:
                return False

            thread_manager.message_queue.add_message(self.npc_id, wander_action.to_dict())
            self._last_idle_movement_time = current_time
            logger.debug("Scheduled WANDER action for NPC", npc_id=self.npc_id)
            return True

        except (ImportError, AttributeError, RuntimeError) as e:
            logger.debug("Could not schedule WANDER action via thread manager", npc_id=self.npc_id, error=str(e))
            return False

    def schedule_idle_movement(self) -> bool:
        """
        Schedule a WANDER action for idle movement if interval has elapsed.

        This method checks if enough time has passed since the last movement
        and queues a WANDER action if conditions are met.

        Returns:
            bool: True if action was scheduled, False otherwise
        """
        try:
            current_time = time.time()

            if not self._should_schedule_movement(current_time):
                return False

            wander_action = self._create_wander_action(current_time)

            if self._queue_wander_action(wander_action, current_time):
                return True

            # Fallback: execute directly if thread manager unavailable
            return self.wander()

        except (TypeError, KeyError, AttributeError, RuntimeError) as e:
            logger.error(
                "Error scheduling idle movement", npc_id=self.npc_id, error=str(e), error_type=type(e).__name__
            )
            return False

    def respond_to_player(self, player_id: str, _interaction_type: str) -> bool:
        """Respond to player interaction."""
        try:
            response_chance = self._behavior_config.get("response_chance", 0.5)
            if response_chance > 0.5:  # Simple probability check
                self.speak(f"Hello there, {player_id}!")
                logger.debug("NPC responded to player", npc_id=self.npc_id, player_id=player_id)
                return True
            return False
        except (TypeError, KeyError, AttributeError) as e:
            logger.error("Error responding to player", npc_id=self.npc_id, error=str(e), error_type=type(e).__name__)
            return False

    def _handle_wander(self, _context: dict[str, Any]) -> bool:
        """Handle wandering action."""
        return self.wander()

    def _handle_respond_to_greeting(self, context: dict[str, Any]) -> bool:
        """Handle responding to greeting action."""
        player_id = context.get("player_id", "stranger")
        return self.respond_to_player(player_id, "greet")

    def _handle_flee(self, _context: dict[str, Any]) -> bool:
        """Handle fleeing action."""
        self.speak("I must get away from here!")
        logger.debug("NPC is fleeing", npc_id=self.npc_id)
        return True
