"""
NPC Idle Movement Handler for MythosMUD.

This module provides idle movement functionality for NPCs, allowing them to
wander within their subzone boundaries when not engaged in combat or other
activities.

As documented in the Pnakotic Manuscripts, proper idle movement patterns
are essential for maintaining the illusion of a living, breathing world
while respecting the territorial boundaries that keep entities in their
designated domains.
"""

import random
import time
from typing import Any

from ..logging.enhanced_logging_config import get_logger
from ..persistence import get_persistence
from .movement_integration import NPCMovementIntegration

logger = get_logger(__name__)


class IdleMovementHandler:
    """
    Handler for NPC idle movement logic.

    This class manages the decision-making and execution of idle movement
    for NPCs, including probability checks, exit selection, and subzone
    boundary validation.
    """

    def __init__(self, event_bus=None, persistence=None):
        """
        Initialize the idle movement handler.

        Args:
            event_bus: Optional EventBus instance for movement events
            persistence: Optional persistence layer instance
        """
        self.persistence = persistence or get_persistence(event_bus)
        self.movement_integration = NPCMovementIntegration(event_bus, self.persistence)
        logger.debug("Idle movement handler initialized")

    def should_idle_move(
        self,
        npc_instance: Any,
        npc_definition: Any,
        behavior_config: dict[str, Any],
        current_time: float | None = None,
    ) -> bool:
        """
        Determine if an NPC should attempt idle movement.

        Checks multiple conditions:
        - Idle movement must be enabled in behavior_config
        - NPC must not be in combat
        - Movement probability check must pass
        - Minimum interval since last movement must have elapsed

        Args:
            npc_instance: The NPC instance to check
            npc_definition: The NPC definition containing subzone info
            behavior_config: Behavior configuration dictionary
            current_time: Current timestamp (defaults to time.time())

        Returns:
            bool: True if NPC should attempt movement, False otherwise
        """
        try:
            if current_time is None:
                current_time = time.time()

            # Check if idle movement is enabled
            idle_enabled = behavior_config.get("idle_movement_enabled", False)
            if not idle_enabled:
                logger.debug("Idle movement disabled for NPC", npc_id=getattr(npc_instance, "npc_id", "unknown"))
                return False

            # Check if NPC is in combat (NPCs in combat should not idle move)
            if self._is_npc_in_combat(npc_instance):
                logger.debug("NPC in combat, skipping idle movement", npc_id=getattr(npc_instance, "npc_id", "unknown"))
                return False

            # Check if NPC is alive and active
            if not getattr(npc_instance, "is_alive", True) or not getattr(npc_instance, "is_active", True):
                logger.debug("NPC not alive or active", npc_id=getattr(npc_instance, "npc_id", "unknown"))
                return False

            # Check movement probability
            movement_probability = behavior_config.get("idle_movement_probability", 0.25)
            if random.random() > movement_probability:
                logger.debug(
                    "Movement probability check failed",
                    npc_id=getattr(npc_instance, "npc_id", "unknown"),
                    probability=movement_probability,
                )
                return False

            # Check minimum interval (if tracking last movement time)
            # For now, we'll rely on the scheduling system to handle intervals
            # This method is called when it's time to check, so interval is already handled

            return True

        except Exception as e:
            npc_id = getattr(npc_instance, "npc_id", "unknown")
            logger.error("Error checking if NPC should idle move", npc_id=npc_id, error=str(e))
            return False

    def _is_npc_in_combat(self, npc_instance: Any) -> bool:
        """
        Check if an NPC is currently in combat.

        Args:
            npc_instance: The NPC instance to check

        Returns:
            bool: True if NPC is in combat, False otherwise
        """
        try:
            # Try to get combat integration from NPC instance
            if hasattr(npc_instance, "combat_integration") and npc_instance.combat_integration:
                # Check if there's a way to query combat state
                # For now, we'll check if the NPC has combat-related attributes
                # that indicate active combat
                pass

            # Try to query combat service directly
            try:
                from ..services.combat_service import get_combat_service

                combat_service = get_combat_service()
                if combat_service:
                    # Check if NPC is in the combat service's tracking
                    npc_id = getattr(npc_instance, "npc_id", None)
                    if npc_id:
                        # Convert string ID to UUID if needed
                        import uuid

                        try:
                            npc_uuid = uuid.UUID(npc_id) if isinstance(npc_id, str) else npc_id
                            if npc_uuid in combat_service._npc_combats:
                                return True
                        except (ValueError, AttributeError):
                            # NPC ID might not be a valid UUID, check string mapping
                            # Check if there's a UUID mapping in combat integration service
                            if hasattr(combat_service, "_npc_combat_integration_service"):
                                npc_combat_service = combat_service._npc_combat_integration_service
                                if npc_combat_service and hasattr(npc_combat_service, "_uuid_to_string_id_mapping"):
                                    # Check reverse mapping
                                    for uuid_key, string_id in npc_combat_service._uuid_to_string_id_mapping.items():
                                        if string_id == npc_id:
                                            if uuid_key in combat_service._npc_combats:
                                                return True
            except (ImportError, AttributeError, RuntimeError):
                # Combat service not available or not initialized
                logger.debug("Combat service not available for combat check")
                pass

            return False

        except Exception as e:
            logger.debug("Error checking NPC combat state", error=str(e))
            return False

    def get_valid_exits(
        self, current_room_id: str, npc_definition: Any, behavior_config: dict[str, Any]
    ) -> dict[str, str]:
        """
        Get exits from current room that stay within subzone boundaries.

        Args:
            current_room_id: ID of the current room
            npc_definition: NPC definition containing subzone information
            behavior_config: Behavior configuration dictionary

        Returns:
            dict[str, str]: Dictionary of direction -> room_id mappings for valid exits
        """
        try:
            # Get all exits from current room
            all_exits = self.movement_integration.get_available_exits(current_room_id)
            if not all_exits:
                logger.debug("No exits available from room", room_id=current_room_id)
                return {}

            # Get NPC's subzone ID
            npc_sub_zone_id = getattr(npc_definition, "sub_zone_id", None)
            if not npc_sub_zone_id:
                logger.warning("NPC definition missing sub_zone_id", npc_id=getattr(npc_definition, "id", "unknown"))
                return {}

            # Filter exits to only those within subzone
            valid_exits = {}
            for direction, target_room_id in all_exits.items():
                if self.movement_integration.validate_subzone_boundary(npc_sub_zone_id, target_room_id):
                    valid_exits[direction] = target_room_id
                else:
                    logger.debug(
                        "Exit filtered out due to subzone boundary",
                        direction=direction,
                        target_room_id=target_room_id,
                        npc_sub_zone_id=npc_sub_zone_id,
                    )

            return valid_exits

        except Exception as e:
            logger.error("Error getting valid exits", room_id=current_room_id, error=str(e))
            return {}

    def select_exit(
        self,
        valid_exits: dict[str, str],
        spawn_room_id: str,
        current_room_id: str,
        behavior_config: dict[str, Any],
    ) -> tuple[str, str] | None:
        """
        Select an exit using weighted random selection favoring exits closer to spawn room.

        Args:
            valid_exits: Dictionary of direction -> room_id mappings
            spawn_room_id: ID of the NPC's spawn room
            current_room_id: ID of the current room
            behavior_config: Behavior configuration dictionary

        Returns:
            tuple[str, str] | None: (direction, room_id) tuple if exit selected, None otherwise
        """
        try:
            if not valid_exits:
                return None

            # If only one exit, return it
            if len(valid_exits) == 1:
                direction, room_id = next(iter(valid_exits.items()))
                return (direction, room_id)

            # Check if weighted selection is enabled
            weighted_home = behavior_config.get("idle_movement_weighted_home", True)

            if not weighted_home:
                # Random selection without weighting
                direction = random.choice(list(valid_exits.keys()))
                return (direction, valid_exits[direction])

            # Weighted selection: prefer exits that keep NPC closer to spawn room
            # Calculate distances and assign weights
            exit_weights: list[tuple[str, str, float]] = []
            spawn_distance = self._calculate_distance_to_room(current_room_id, spawn_room_id)

            for direction, target_room_id in valid_exits.items():
                target_distance = self._calculate_distance_to_room(target_room_id, spawn_room_id)
                # Weight inversely proportional to distance from spawn
                # Exits that move closer to spawn get higher weight
                # Exits that move further get lower weight
                distance_diff = target_distance - spawn_distance
                # Weight: 1.0 for moving closer, 0.5 for moving further, 0.25 for moving much further
                if distance_diff < 0:
                    weight = 1.0  # Moving closer to spawn
                elif distance_diff == 0:
                    weight = 0.75  # Same distance
                elif distance_diff == 1:
                    weight = 0.5  # One room further
                else:
                    weight = 0.25  # Much further

                exit_weights.append((direction, target_room_id, weight))

            # Select exit based on weights
            if not exit_weights:
                return None

            # Normalize weights to probabilities
            total_weight = sum(weight for _, _, weight in exit_weights)
            if total_weight == 0:
                # Fallback to random selection
                direction = random.choice(list(valid_exits.keys()))
                return (direction, valid_exits[direction])

            # Select based on weighted probabilities
            rand = random.random() * total_weight
            cumulative = 0.0
            for direction, room_id, weight in exit_weights:
                cumulative += weight
                if rand <= cumulative:
                    return (direction, room_id)

            # Fallback to last exit
            direction, room_id, _ = exit_weights[-1]
            return (direction, room_id)

        except Exception as e:
            logger.error("Error selecting exit", error=str(e))
            return None

    def _calculate_distance_to_room(self, from_room_id: str, to_room_id: str) -> int:
        """
        Calculate approximate distance between two rooms.

        This is a simplified distance calculation that counts the minimum
        number of room hops needed. For now, it uses a simple heuristic
        based on room ID similarity or performs a basic path search.

        Args:
            from_room_id: Starting room ID
            to_room_id: Target room ID

        Returns:
            int: Approximate distance in room hops (0 if same room, higher for further rooms)
        """
        try:
            if from_room_id == to_room_id:
                return 0

            # Simple heuristic: if rooms are in same subzone, use room ID similarity
            # For more accurate distance, we'd need to do BFS pathfinding
            # For now, we'll use a simple approach: check if rooms share common prefixes
            from_parts = from_room_id.split("_")
            to_parts = to_room_id.split("_")

            # If rooms share the same subzone (first 3 parts: plane_zone_subzone)
            if len(from_parts) >= 3 and len(to_parts) >= 3:
                if from_parts[:3] == to_parts[:3]:
                    # Same subzone - estimate distance based on room name differences
                    # This is a heuristic; for accurate distance, use BFS
                    return abs(len(from_parts) - len(to_parts)) + 1

            # Different subzones or invalid format - return high distance
            return 999

        except Exception as e:
            logger.debug("Error calculating room distance", error=str(e))
            return 999

    def execute_idle_movement(
        self,
        npc_instance: Any,
        npc_definition: Any,
        behavior_config: dict[str, Any],
    ) -> bool:
        """
        Execute idle movement for an NPC.

        This method orchestrates the full idle movement process:
        1. Check if movement should occur
        2. Get valid exits within subzone
        3. Select an exit using weighted selection
        4. Execute the movement

        Args:
            npc_instance: The NPC instance to move
            npc_definition: The NPC definition
            behavior_config: Behavior configuration dictionary

        Returns:
            bool: True if movement was executed successfully, False otherwise
        """
        try:
            # Check if NPC should move
            if not self.should_idle_move(npc_instance, npc_definition, behavior_config):
                return False

            # Get current room
            current_room_id = getattr(npc_instance, "current_room", None)
            if not current_room_id:
                logger.warning("NPC has no current room", npc_id=getattr(npc_instance, "npc_id", "unknown"))
                return False

            # Get spawn room (default to current room if not tracked)
            spawn_room_id = getattr(npc_instance, "spawn_room_id", None) or getattr(
                npc_definition, "room_id", current_room_id
            )

            # Get valid exits within subzone
            valid_exits = self.get_valid_exits(current_room_id, npc_definition, behavior_config)
            if not valid_exits:
                logger.debug("No valid exits for idle movement", npc_id=getattr(npc_instance, "npc_id", "unknown"))
                return False

            # Select exit
            exit_selection = self.select_exit(valid_exits, spawn_room_id, current_room_id, behavior_config)
            if not exit_selection:
                logger.debug("No exit selected for idle movement", npc_id=getattr(npc_instance, "npc_id", "unknown"))
                return False

            direction, target_room_id = exit_selection

            # Execute movement
            success = self.movement_integration.move_npc_to_room(
                getattr(npc_instance, "npc_id", "unknown"), current_room_id, target_room_id
            )

            if success:
                logger.info(
                    "NPC idle movement executed",
                    npc_id=getattr(npc_instance, "npc_id", "unknown"),
                    from_room=current_room_id,
                    to_room=target_room_id,
                    direction=direction,
                )
            else:
                logger.warning(
                    "NPC idle movement failed",
                    npc_id=getattr(npc_instance, "npc_id", "unknown"),
                    from_room=current_room_id,
                    to_room=target_room_id,
                )

            return success

        except Exception as e:
            npc_id = getattr(npc_instance, "npc_id", "unknown")
            logger.error("Error executing idle movement", npc_id=npc_id, error=str(e))
            return False
