"""
NPC Interaction and Relationship System for MythosMUD.

This module implements NPC-to-NPC interactions and relationship management,
allowing NPCs to form complex social dynamics, alliances, rivalries, and
behavioral modifications based on their relationships with other NPCs.

As documented in the Cultes des Goules, proper relationship management is essential
for maintaining the delicate balance between the mundane and the eldritch forces
that lurk in the shadows of our world. The interaction system ensures that NPCs
can form meaningful connections and react appropriately to each other's presence.
"""

import logging
import random
import time
from enum import Enum
from typing import Any

from server.events.event_bus import EventBus
from server.events.event_types import NPCEnteredRoom, NPCLeftRoom, NPCSpoke
from server.models.npc import NPCRelationship, NPCRelationshipType
from server.npc.behaviors import NPCBase

logger = logging.getLogger(__name__)


class NPCInteractionType(str, Enum):
    """Enumeration of NPC interaction types."""

    GREETING = "greeting"
    FAREWELL = "farewell"
    CONVERSATION = "conversation"
    COOPERATION = "cooperation"
    CONFLICT = "conflict"
    ASSISTANCE = "assistance"
    IGNORE = "ignore"
    OBSERVE = "observe"


class NPCInteractionResult(str, Enum):
    """Enumeration of NPC interaction results."""

    SUCCESS = "success"
    FAILURE = "failure"
    NEUTRAL = "neutral"
    POSITIVE = "positive"
    NEGATIVE = "negative"
    IGNORED = "ignored"


class NPCInteraction:
    """Represents an interaction between two NPCs."""

    def __init__(
        self,
        initiator_id: str,
        target_id: str,
        interaction_type: NPCInteractionType,
        context: dict[str, Any] | None = None,
    ):
        """
        Initialize NPC interaction.

        Args:
            initiator_id: ID of the NPC initiating the interaction
            target_id: ID of the NPC being interacted with
            interaction_type: Type of interaction
            context: Additional context for the interaction
        """
        self.initiator_id = initiator_id
        self.target_id = target_id
        self.interaction_type = interaction_type
        self.context = context or {}
        self.timestamp = time.time()
        self.result = NPCInteractionResult.NEUTRAL
        self.effects: dict[str, Any] = {}

    def __repr__(self) -> str:
        """String representation of the interaction."""
        return f"<NPCInteraction({self.initiator_id} -> {self.target_id}, {self.interaction_type}, {self.result})>"


class NPCRelationshipManager:
    """Manages NPC relationships and their effects on behavior."""

    def __init__(self, event_bus: EventBus):
        """
        Initialize the NPC relationship manager.

        Args:
            event_bus: Event bus for publishing and subscribing to events
        """
        self.event_bus = event_bus
        self.relationships: dict[tuple[int, int], NPCRelationship] = {}
        self.relationship_cache: dict[str, dict[str, float]] = {}  # npc_id -> {other_npc_id: modifier}
        self.interaction_history: list[NPCInteraction] = []

        # Subscribe to relevant events
        self._subscribe_to_events()

        logger.info("NPC Relationship Manager initialized")

    def _subscribe_to_events(self) -> None:
        """Subscribe to relevant game events."""
        self.event_bus.subscribe(NPCEnteredRoom, self._handle_npc_entered_room)
        self.event_bus.subscribe(NPCLeftRoom, self._handle_npc_left_room)
        self.event_bus.subscribe(NPCSpoke, self._handle_npc_spoke)

    def _handle_npc_entered_room(self, event: NPCEnteredRoom) -> None:
        """Handle NPC entering a room - check for interactions."""
        # This would trigger interaction checks with other NPCs in the room
        # For now, we'll just log the event
        logger.debug(f"NPC {event.npc_id} entered room {event.room_id}")

    def _handle_npc_left_room(self, event: NPCLeftRoom) -> None:
        """Handle NPC leaving a room."""
        logger.debug(f"NPC {event.npc_id} left room {event.room_id}")

    def _handle_npc_spoke(self, event: NPCSpoke) -> None:
        """Handle NPC speaking - may trigger interactions with other NPCs."""
        logger.debug(f"NPC {event.npc_id} spoke: {event.message}")

    def load_relationships(self, relationships: list[NPCRelationship]) -> None:
        """
        Load NPC relationships from the database.

        Args:
            relationships: List of NPC relationships to load
        """
        self.relationships.clear()
        self.relationship_cache.clear()

        for relationship in relationships:
            # Store relationship in both directions
            key1 = (relationship.npc_id_1, relationship.npc_id_2)
            key2 = (relationship.npc_id_2, relationship.npc_id_1)
            self.relationships[key1] = relationship
            self.relationships[key2] = relationship

            # Update cache
            self._update_relationship_cache(relationship)

        logger.info(f"Loaded {len(relationships)} NPC relationships")

    def _update_relationship_cache(self, relationship: NPCRelationship) -> None:
        """
        Update the relationship cache for a relationship.

        Args:
            relationship: Relationship to cache
        """
        npc1_id = str(relationship.npc_id_1)
        npc2_id = str(relationship.npc_id_2)

        if npc1_id not in self.relationship_cache:
            self.relationship_cache[npc1_id] = {}
        if npc2_id not in self.relationship_cache:
            self.relationship_cache[npc2_id] = {}

        modifier = relationship.get_relationship_modifier()
        self.relationship_cache[npc1_id][npc2_id] = modifier
        self.relationship_cache[npc2_id][npc1_id] = modifier

    def get_relationship_modifier(self, npc1_id: str, npc2_id: str) -> float:
        """
        Get relationship modifier between two NPCs.

        Args:
            npc1_id: ID of the first NPC
            npc2_id: ID of the second NPC

        Returns:
            Relationship modifier (-1.0 to 1.0)
        """
        if npc1_id in self.relationship_cache and npc2_id in self.relationship_cache[npc1_id]:
            return self.relationship_cache[npc1_id][npc2_id]
        return 0.0  # Neutral if no relationship found

    def get_relationship_type(self, npc1_id: str, npc2_id: str) -> NPCRelationshipType | None:
        """
        Get relationship type between two NPCs.

        Args:
            npc1_id: ID of the first NPC
            npc2_id: ID of the second NPC

        Returns:
            Relationship type or None if no relationship found
        """
        # Convert string IDs to integers for lookup
        try:
            npc1_int = int(npc1_id.split("_")[-1]) if "_" in npc1_id else int(npc1_id)
            npc2_int = int(npc2_id.split("_")[-1]) if "_" in npc2_id else int(npc2_id)
        except (ValueError, IndexError):
            return None

        key = (npc1_int, npc2_int)
        if key in self.relationships:
            return NPCRelationshipType(self.relationships[key].relationship_type)
        return None

    def add_relationship(
        self, npc1_id: int, npc2_id: int, relationship_type: NPCRelationshipType, strength: float = 0.5
    ) -> None:
        """
        Add a new relationship between two NPCs.

        Args:
            npc1_id: ID of the first NPC definition
            npc2_id: ID of the second NPC definition
            relationship_type: Type of relationship
            strength: Strength of the relationship (0.0 to 1.0)
        """
        relationship = NPCRelationship(
            npc_id_1=npc1_id,
            npc_id_2=npc2_id,
            relationship_type=relationship_type.value,
            relationship_strength=strength,
        )

        # Store relationship in both directions
        key1 = (npc1_id, npc2_id)
        key2 = (npc2_id, npc1_id)
        self.relationships[key1] = relationship
        self.relationships[key2] = relationship

        # Update cache
        self._update_relationship_cache(relationship)

        logger.info(f"Added relationship: {npc1_id} {relationship_type.value} {npc2_id} (strength: {strength})")

    def remove_relationship(self, npc1_id: int, npc2_id: int) -> bool:
        """
        Remove a relationship between two NPCs.

        Args:
            npc1_id: ID of the first NPC definition
            npc2_id: ID of the second NPC definition

        Returns:
            True if relationship was removed, False if not found
        """
        key1 = (npc1_id, npc2_id)
        key2 = (npc2_id, npc1_id)

        if key1 in self.relationships:
            del self.relationships[key1]
            del self.relationships[key2]

            # Update cache
            npc1_str = str(npc1_id)
            npc2_str = str(npc2_id)
            if npc1_str in self.relationship_cache and npc2_str in self.relationship_cache[npc1_str]:
                del self.relationship_cache[npc1_str][npc2_str]
            if npc2_str in self.relationship_cache and npc1_str in self.relationship_cache[npc2_str]:
                del self.relationship_cache[npc2_str][npc1_str]

            logger.info(f"Removed relationship between {npc1_id} and {npc2_id}")
            return True

        return False

    def get_relationship_statistics(self) -> dict[str, Any]:
        """
        Get relationship statistics.

        Returns:
            Dictionary containing relationship statistics
        """
        total_relationships = len(self.relationships) // 2  # Divide by 2 since we store both directions
        relationship_types = {}
        strength_ranges = {"weak": 0, "medium": 0, "strong": 0}

        # Use a set to track processed relationships to avoid double counting
        processed_relationships = set()

        for _key, relationship in self.relationships.items():
            # Create a unique identifier for the relationship (smaller ID first)
            rel_id = tuple(sorted([relationship.npc_id_1, relationship.npc_id_2]))

            if rel_id not in processed_relationships:
                processed_relationships.add(rel_id)

                rel_type = relationship.relationship_type
                relationship_types[rel_type] = relationship_types.get(rel_type, 0) + 1

                # Count by strength
                if relationship.relationship_strength < 0.33:
                    strength_ranges["weak"] += 1
                elif relationship.relationship_strength < 0.67:
                    strength_ranges["medium"] += 1
                else:
                    strength_ranges["strong"] += 1

        return {
            "total_relationships": total_relationships,
            "relationship_types": relationship_types,
            "strength_ranges": strength_ranges,
            "cached_npcs": len(self.relationship_cache),
            "interaction_history_size": len(self.interaction_history),
        }


class NPCInteractionEngine:
    """Engine for processing NPC-to-NPC interactions."""

    def __init__(self, event_bus: EventBus, relationship_manager: NPCRelationshipManager):
        """
        Initialize the NPC interaction engine.

        Args:
            event_bus: Event bus for publishing and subscribing to events
            relationship_manager: Relationship manager for NPC relationships
        """
        self.event_bus = event_bus
        self.relationship_manager = relationship_manager
        self.active_npcs: dict[str, NPCBase] = {}
        self.interaction_rules: dict[NPCInteractionType, dict[str, Any]] = {}

        # Initialize interaction rules
        self._initialize_interaction_rules()

        logger.info("NPC Interaction Engine initialized")

    def _initialize_interaction_rules(self) -> None:
        """Initialize interaction rules for different interaction types."""
        self.interaction_rules = {
            NPCInteractionType.GREETING: {
                "base_probability": 0.8,
                "relationship_modifier": 0.2,
                "success_threshold": 0.5,
            },
            NPCInteractionType.CONVERSATION: {
                "base_probability": 0.6,
                "relationship_modifier": 0.3,
                "success_threshold": 0.4,
            },
            NPCInteractionType.COOPERATION: {
                "base_probability": 0.4,
                "relationship_modifier": 0.4,
                "success_threshold": 0.6,
            },
            NPCInteractionType.CONFLICT: {
                "base_probability": 0.2,
                "relationship_modifier": -0.3,
                "success_threshold": 0.3,
            },
            NPCInteractionType.ASSISTANCE: {
                "base_probability": 0.3,
                "relationship_modifier": 0.5,
                "success_threshold": 0.7,
            },
        }

    def register_npc(self, npc_id: str, npc_instance: NPCBase) -> None:
        """
        Register an NPC instance for interaction processing.

        Args:
            npc_id: ID of the NPC
            npc_instance: NPC instance
        """
        self.active_npcs[npc_id] = npc_instance
        logger.debug(f"Registered NPC for interactions: {npc_id}")

    def unregister_npc(self, npc_id: str) -> None:
        """
        Unregister an NPC instance.

        Args:
            npc_id: ID of the NPC
        """
        if npc_id in self.active_npcs:
            del self.active_npcs[npc_id]
            logger.debug(f"Unregistered NPC from interactions: {npc_id}")

    def process_interaction(
        self,
        initiator_id: str,
        target_id: str,
        interaction_type: NPCInteractionType,
        context: dict[str, Any] | None = None,
    ) -> NPCInteraction:
        """
        Process an interaction between two NPCs.

        Args:
            initiator_id: ID of the NPC initiating the interaction
            target_id: ID of the NPC being interacted with
            interaction_type: Type of interaction
            context: Additional context for the interaction

        Returns:
            NPCInteraction object with results
        """
        interaction = NPCInteraction(initiator_id, target_id, interaction_type, context)

        # Check if both NPCs are active
        if initiator_id not in self.active_npcs or target_id not in self.active_npcs:
            interaction.result = NPCInteractionResult.IGNORED
            interaction.effects["reason"] = "One or both NPCs not active"
            return interaction

        # Get relationship modifier
        relationship_modifier = self.relationship_manager.get_relationship_modifier(initiator_id, target_id)
        relationship_type = self.relationship_manager.get_relationship_type(initiator_id, target_id)

        # Calculate interaction success
        success = self._calculate_interaction_success(interaction_type, relationship_modifier, context)

        # Determine result based on success and relationship
        interaction.result = self._determine_interaction_result(success, relationship_type, interaction_type)

        # Apply interaction effects
        interaction.effects = self._apply_interaction_effects(interaction, relationship_modifier)

        # Record interaction
        self.relationship_manager.interaction_history.append(interaction)

        # Keep only recent history
        if len(self.relationship_manager.interaction_history) > 1000:
            self.relationship_manager.interaction_history = self.relationship_manager.interaction_history[-500:]

        logger.debug(f"Processed interaction: {interaction}")
        return interaction

    def _calculate_interaction_success(
        self, interaction_type: NPCInteractionType, relationship_modifier: float, context: dict[str, Any] | None
    ) -> bool:
        """
        Calculate whether an interaction will be successful.

        Args:
            interaction_type: Type of interaction
            relationship_modifier: Relationship modifier
            context: Additional context

        Returns:
            True if interaction should succeed
        """
        if interaction_type not in self.interaction_rules:
            return False

        rules = self.interaction_rules[interaction_type]
        base_probability = rules["base_probability"]
        rel_modifier = rules["relationship_modifier"]

        # Calculate success probability
        success_probability = base_probability + (relationship_modifier * rel_modifier)
        success_probability = max(0.0, min(1.0, success_probability))  # Clamp to [0, 1]

        # Add context modifiers
        if context:
            if "room_mood" in context:
                success_probability += context["room_mood"] * 0.1
            if "time_of_day" in context:
                if context["time_of_day"] == "night":
                    success_probability *= 0.8  # Interactions less likely at night

        return random.random() < success_probability

    def _determine_interaction_result(
        self, success: bool, relationship_type: NPCRelationshipType | None, interaction_type: NPCInteractionType
    ) -> NPCInteractionResult:
        """
        Determine the result of an interaction.

        Args:
            success: Whether the interaction was successful
            relationship_type: Type of relationship between NPCs
            interaction_type: Type of interaction

        Returns:
            Interaction result
        """
        if not success:
            return NPCInteractionResult.FAILURE

        if relationship_type == NPCRelationshipType.ALLY:
            return NPCInteractionResult.POSITIVE
        elif relationship_type == NPCRelationshipType.ENEMY:
            return NPCInteractionResult.NEGATIVE
        elif relationship_type == NPCRelationshipType.FOLLOWER:
            return NPCInteractionResult.POSITIVE
        else:
            return NPCInteractionResult.NEUTRAL

    def _apply_interaction_effects(self, interaction: NPCInteraction, relationship_modifier: float) -> dict[str, Any]:
        """
        Apply effects of an interaction.

        Args:
            interaction: The interaction to apply effects for
            relationship_modifier: Relationship modifier

        Returns:
            Dictionary of effects applied
        """
        effects = {}

        # Apply relationship changes based on interaction result
        if interaction.result == NPCInteractionResult.POSITIVE:
            effects["relationship_change"] = 0.1
        elif interaction.result == NPCInteractionResult.NEGATIVE:
            effects["relationship_change"] = -0.1
        else:
            effects["relationship_change"] = 0.0

        # Apply behavior modifications
        if interaction.interaction_type == NPCInteractionType.COOPERATION:
            effects["cooperation_bonus"] = 0.2
        elif interaction.interaction_type == NPCInteractionType.CONFLICT:
            effects["aggression_increase"] = 0.1

        # Apply mood changes
        if interaction.result == NPCInteractionResult.POSITIVE:
            effects["mood_improvement"] = 0.15
        elif interaction.result == NPCInteractionResult.NEGATIVE:
            effects["mood_decline"] = 0.15

        return effects

    def get_interaction_statistics(self) -> dict[str, Any]:
        """
        Get interaction statistics.

        Returns:
            Dictionary containing interaction statistics
        """
        total_interactions = len(self.relationship_manager.interaction_history)
        if total_interactions == 0:
            return {"total_interactions": 0}

        # Count by result
        result_counts = {}
        type_counts = {}
        for interaction in self.relationship_manager.interaction_history:
            result = interaction.result
            interaction_type = interaction.interaction_type
            result_counts[result] = result_counts.get(result, 0) + 1
            type_counts[interaction_type] = type_counts.get(interaction_type, 0) + 1

        # Calculate success rate
        successful_interactions = sum(
            1
            for interaction in self.relationship_manager.interaction_history
            if interaction.result
            in [NPCInteractionResult.SUCCESS, NPCInteractionResult.POSITIVE, NPCInteractionResult.NEUTRAL]
        )
        success_rate = successful_interactions / total_interactions if total_interactions > 0 else 0.0

        return {
            "total_interactions": total_interactions,
            "success_rate": success_rate,
            "result_counts": result_counts,
            "type_counts": type_counts,
            "active_npcs": len(self.active_npcs),
        }

    def cleanup_old_interactions(self, max_age_seconds: int = 86400) -> int:
        """
        Clean up old interaction history.

        Args:
            max_age_seconds: Maximum age in seconds before cleanup

        Returns:
            Number of interactions cleaned up
        """
        current_time = time.time()
        interactions_to_keep = []

        for interaction in self.relationship_manager.interaction_history:
            age = current_time - interaction.timestamp
            if age <= max_age_seconds:
                interactions_to_keep.append(interaction)

        cleaned_count = len(self.relationship_manager.interaction_history) - len(interactions_to_keep)
        self.relationship_manager.interaction_history = interactions_to_keep

        if cleaned_count > 0:
            logger.info(f"Cleaned up {cleaned_count} old interactions")

        return cleaned_count
