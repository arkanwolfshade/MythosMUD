"""
NPC Event Subscription and Reaction System.

This module provides a system for NPCs to subscribe to game events and
react to them automatically based on their behavior configuration.

As documented in the Pnakotic Manuscripts, the ability of entities to
perceive and respond to dimensional disturbances is crucial for maintaining
the delicate balance of our reality.
"""

import time
from collections.abc import Callable
from typing import Any, TypeVar

from ..events import EventBus
from ..events.event_types import (
    BaseEvent,
    NPCAttacked,
    NPCDied,
    NPCEnteredRoom,
    NPCLeftRoom,
    NPCListened,
    NPCSpoke,
    NPCTookDamage,
    ObjectAddedToRoom,
    ObjectRemovedFromRoom,
    PlayerEnteredRoom,
    PlayerLeftRoom,
)
from ..structured_logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)

# Type variable for generic event types
EventT = TypeVar("EventT", bound=BaseEvent)


class NPCEventReaction:
    """
    Represents a reaction that an NPC can have to a specific event type.

    This class defines the conditions under which an NPC should react
    and the action to take when those conditions are met.
    """

    def __init__(
        self,
        event_type: type[BaseEvent],
        condition: Callable[[Any, dict[str, Any]], bool] | None = None,
        action: Callable[[Any, dict[str, Any]], bool] | None = None,
        priority: int = 0,
    ):
        """
        Initialize an NPC event reaction.

        Args:
            event_type: The type of event this reaction responds to
            condition: Optional function to check if reaction should trigger
            action: Function to execute when reaction triggers
            priority: Priority level (higher = more important)
        """
        self.event_type = event_type
        self.condition = condition
        self.action = action
        self.priority = priority
        self.last_triggered = 0.0
        self.trigger_count = 0

    def should_trigger(self, event: BaseEvent, npc_context: dict[str, Any]) -> bool:
        """
        Check if this reaction should trigger for the given event.

        Args:
            event: The event that occurred
            npc_context: Context about the NPC (stats, location, etc.)

        Returns:
            bool: True if reaction should trigger
        """
        if not isinstance(event, self.event_type):
            return False

        if self.condition is None:
            return True

        try:
            return self.condition(event, npc_context)
        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Reaction condition errors unpredictable, must return False
            logger.error("Error checking reaction condition", event_type=event.event_type, error=str(e))
            return False

    def execute(self, event: BaseEvent, npc_context: dict[str, Any]) -> bool:
        """
        Execute the reaction action.

        Args:
            event: The event that triggered the reaction
            npc_context: Context about the NPC

        Returns:
            bool: True if action executed successfully
        """
        if self.action is None:
            return True

        try:
            self.last_triggered = time.time()
            self.trigger_count += 1
            return self.action(event, npc_context)
        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Reaction action errors unpredictable, must return False
            logger.error("Error executing reaction action", event_type=event.event_type, error=str(e))
            return False


class NPCEventReactionSystem:
    """
    System for managing NPC event subscriptions and reactions.

    This class handles the subscription of NPCs to various game events
    and coordinates their reactions based on behavior configuration.
    """

    def __init__(self, event_bus: EventBus):
        """
        Initialize the NPC event reaction system.

        Args:
            event_bus: The event bus to subscribe to
        """
        self.event_bus = event_bus
        self._npc_reactions: dict[str, list[NPCEventReaction]] = {}
        self._event_subscriptions: dict[type[BaseEvent], set[str]] = {}
        self._reaction_cooldowns: dict[str, float] = {}

        # Subscribe to all relevant event types
        self._subscribe_to_events()

        logger.debug("NPC event reaction system initialized")

    def _subscribe_to_events(self) -> None:
        """Subscribe to all event types that NPCs might react to."""
        event_types = [
            PlayerEnteredRoom,
            PlayerLeftRoom,
            NPCEnteredRoom,
            NPCLeftRoom,
            NPCAttacked,
            NPCTookDamage,
            NPCDied,
            NPCSpoke,
            NPCListened,
            ObjectAddedToRoom,
            ObjectRemovedFromRoom,
        ]

        for event_type in event_types:
            # Use service_id for tracking and cleanup (Task 2: Event Subscriber Cleanup)
            self.event_bus.subscribe(event_type, self._handle_event, service_id="npc_event_reaction_system")
            self._event_subscriptions[event_type] = set()
            logger.debug("Subscribed to event type", event_type=event_type.__name__)

    def register_npc_reactions(self, npc_id: str, reactions: list[NPCEventReaction]) -> None:
        """
        Register reactions for a specific NPC.

        Args:
            npc_id: The ID of the NPC
            reactions: List of reactions this NPC can have
        """
        if npc_id not in self._npc_reactions:
            self._npc_reactions[npc_id] = []

        # Add new reactions
        self._npc_reactions[npc_id].extend(reactions)

        # Sort by priority (highest first)
        self._npc_reactions[npc_id].sort(key=lambda r: r.priority, reverse=True)

        # Update event subscriptions
        for reaction in reactions:
            event_type = reaction.event_type
            if event_type in self._event_subscriptions:
                self._event_subscriptions[event_type].add(npc_id)

        logger.debug("Registered NPC reactions", npc_id=npc_id, reaction_count=len(reactions))

    def unregister_npc_reactions(self, npc_id: str) -> None:
        """
        Unregister all reactions for a specific NPC.

        Args:
            npc_id: The ID of the NPC
        """
        if npc_id in self._npc_reactions:
            # Remove from event subscriptions
            for _event_type, npc_set in self._event_subscriptions.items():
                npc_set.discard(npc_id)

            # Remove reactions
            del self._npc_reactions[npc_id]

            logger.debug("Unregistered NPC reactions", npc_id=npc_id)

    def _handle_event(self, event: BaseEvent) -> None:
        """
        Handle an incoming event and trigger appropriate NPC reactions.

        Args:
            event: The event that occurred
        """
        event_type = type(event)

        if event_type not in self._event_subscriptions:
            return

        # Get NPCs that are subscribed to this event type
        subscribed_npcs = self._event_subscriptions[event_type]

        for npc_id in subscribed_npcs:
            if npc_id not in self._npc_reactions:
                continue

            # Check cooldown
            cooldown_key = f"{npc_id}_{event_type.__name__}"
            current_time = time.time()
            if cooldown_key in self._reaction_cooldowns:
                if current_time - self._reaction_cooldowns[cooldown_key] < 1.0:  # 1 second cooldown
                    continue

            # Get NPC context (this would need to be provided by the NPC system)
            npc_context = self._get_npc_context(npc_id)
            if not npc_context:
                continue

            # Check and execute reactions
            reactions = self._npc_reactions[npc_id]
            for reaction in reactions:
                if reaction.should_trigger(event, npc_context):
                    if reaction.execute(event, npc_context):
                        # Set cooldown
                        self._reaction_cooldowns[cooldown_key] = current_time
                        logger.debug("NPC reaction executed", npc_id=npc_id, event_type=event_type.__name__)
                        break  # Only execute highest priority reaction

    def _get_npc_context(self, npc_id: str) -> dict[str, Any] | None:
        """
        Get context information for an NPC.

        This method attempts to get actual NPC context from the NPC system.

        Args:
            npc_id: The ID of the NPC

        Returns:
            dict: NPC context information
        """
        # Try to get NPC context from the NPC system
        # This would need to be connected to the actual NPC management system
        try:
            # For now, return a basic context
            # In a real implementation, this would query the NPC system
            return {"npc_id": npc_id, "current_room": "unknown", "is_alive": True, "stats": {}, "behavior_config": {}}
        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: NPC context retrieval errors unpredictable, must return None
            logger.error("Error getting NPC context", npc_id=npc_id, error=str(e))
            return None

    def get_npc_reaction_stats(self, npc_id: str) -> dict[str, Any]:
        """
        Get statistics about an NPC's reactions.

        Args:
            npc_id: The ID of the NPC

        Returns:
            dict: Reaction statistics
        """
        if npc_id not in self._npc_reactions:
            return {}

        reactions = self._npc_reactions[npc_id]
        total_triggers = sum(r.trigger_count for r in reactions)

        return {
            "reaction_count": len(reactions),
            "total_triggers": total_triggers,
            "reactions": [
                {
                    "event_type": r.event_type.__name__,
                    "priority": r.priority,
                    "trigger_count": r.trigger_count,
                    "last_triggered": r.last_triggered,
                }
                for r in reactions
            ],
        }


# Predefined reaction templates for common NPC behaviors
class NPCEventReactionTemplates:
    """Templates for common NPC event reactions."""

    @staticmethod
    def player_entered_room_greeting(npc_id: str, greeting_message: str = "Hello there!") -> NPCEventReaction:
        """Create a reaction that greets players when they enter the room."""

        def condition(event: PlayerEnteredRoom, npc_context: dict[str, Any]) -> bool:
            return event.room_id == npc_context.get("current_room")

        def action(event: PlayerEnteredRoom, _npc_context: dict[str, Any]) -> bool:  # pylint: disable=unused-argument  # Reason: Parameter required for action signature, context not used in this action
            # This would need to be connected to the NPC's speak method
            logger.info("NPC would greet player", npc_id=npc_id, player_id=event.player_id, message=greeting_message)
            return True

        return NPCEventReaction(event_type=PlayerEnteredRoom, condition=condition, action=action, priority=1)

    @staticmethod
    def player_left_room_farewell(npc_id: str, farewell_message: str = "Goodbye!") -> NPCEventReaction:
        """Create a reaction that says farewell when players leave the room."""

        def condition(event: PlayerLeftRoom, npc_context: dict[str, Any]) -> bool:
            return event.room_id == npc_context.get("current_room")

        def action(event: PlayerLeftRoom, _npc_context: dict[str, Any]) -> bool:  # pylint: disable=unused-argument  # Reason: Parameter required for action signature, context not used in this action
            logger.info("NPC would say farewell", npc_id=npc_id, player_id=event.player_id, message=farewell_message)
            return True

        return NPCEventReaction(event_type=PlayerLeftRoom, condition=condition, action=action, priority=1)

    @staticmethod
    def npc_attacked_retaliation(npc_id: str) -> NPCEventReaction:
        """Create a reaction that makes an NPC retaliate when attacked."""

        def condition(event: NPCAttacked, npc_context: dict[str, Any]) -> bool:
            return event.target_id == npc_id and npc_context.get("is_alive", True)

        def action(event: NPCAttacked, _npc_context: dict[str, Any]) -> bool:  # pylint: disable=unused-argument  # Reason: Parameter required for action signature, context not used in this action
            logger.info("NPC would retaliate", npc_id=npc_id, attacker_id=event.npc_id)
            return True

        return NPCEventReaction(
            event_type=NPCAttacked,
            condition=condition,
            action=action,
            priority=10,  # High priority for combat reactions
        )

    @staticmethod
    def player_spoke_response(npc_id: str, response_message: str = "I heard you!") -> NPCEventReaction:
        """Create a reaction that responds when players speak in the room."""

        def condition(event: NPCListened, npc_context: dict[str, Any]) -> bool:
            return event.npc_id == npc_id and event.room_id == npc_context.get("current_room")

        def action(event: NPCListened, _npc_context: dict[str, Any]) -> bool:  # pylint: disable=unused-argument  # Reason: Parameter required for action signature, context not used in this action
            logger.info(
                "NPC would respond to player", npc_id=npc_id, speaker_id=event.speaker_id, message=response_message
            )
            return True

        return NPCEventReaction(event_type=NPCListened, condition=condition, action=action, priority=2)
