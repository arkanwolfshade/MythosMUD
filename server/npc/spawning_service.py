"""
NPC Spawning Service for MythosMUD.

This module implements the core NPC spawning logic that integrates with the
population control system to spawn NPCs based on required/optional population
rules and game state conditions.

As documented in the Cultes des Goules, proper spawning rituals are essential
for maintaining the delicate balance between the mundane and the eldritch forces
that lurk in the shadows of our world. The spawning service ensures that NPCs
appear at the right time, in the right place, and under the right conditions.
"""

import logging
import random
import time
from typing import Any

from server.events.event_bus import EventBus
from server.events.event_types import NPCEnteredRoom, NPCLeftRoom, PlayerEnteredRoom, PlayerLeftRoom
from server.models.npc import NPCDefinition, NPCSpawnRule
from server.npc.behaviors import AggressiveMobNPC, PassiveMobNPC, ShopkeeperNPC
from server.npc.population_control import NPCPopulationController, ZoneConfiguration

logger = logging.getLogger(__name__)


class NPCSpawnRequest:
    """Represents a request to spawn an NPC."""

    def __init__(
        self,
        definition: NPCDefinition,
        room_id: str,
        spawn_rule: NPCSpawnRule,
        priority: int = 0,
        reason: str = "automatic",
    ):
        """
        Initialize spawn request.

        Args:
            definition: NPC definition to spawn
            room_id: Room where NPC should be spawned
            spawn_rule: Spawn rule that triggered this request
            priority: Spawn priority (higher = more important)
            reason: Reason for spawning (automatic, manual, required, etc.)
        """
        self.definition = definition
        self.room_id = room_id
        self.spawn_rule = spawn_rule
        self.priority = priority
        self.reason = reason
        self.created_at = time.time()

    def __repr__(self) -> str:
        """String representation of spawn request."""
        return f"<NPCSpawnRequest(definition={self.definition.name}, room={self.room_id}, priority={self.priority}, reason={self.reason})>"


class NPCSpawnResult:
    """Represents the result of an NPC spawn attempt."""

    def __init__(
        self,
        success: bool,
        npc_id: str | None = None,
        npc_instance: Any | None = None,
        error_message: str | None = None,
        spawn_request: NPCSpawnRequest | None = None,
    ):
        """
        Initialize spawn result.

        Args:
            success: Whether the spawn was successful
            npc_id: ID of the spawned NPC (if successful)
            npc_instance: NPC instance object (if successful)
            error_message: Error message (if failed)
            spawn_request: Original spawn request
        """
        self.success = success
        self.npc_id = npc_id
        self.npc_instance = npc_instance
        self.error_message = error_message
        self.spawn_request = spawn_request
        self.spawned_at = time.time() if success else None

    def __repr__(self) -> str:
        """String representation of spawn result."""
        if self.success:
            return f"<NPCSpawnResult(success=True, npc_id={self.npc_id})>"
        else:
            return f"<NPCSpawnResult(success=False, error={self.error_message})>"


class NPCSpawningService:
    """
    Main service for NPC spawning logic.

    This service handles the spawning of NPCs based on population rules,
    game state conditions, and spawn requests. It integrates with the
    population control system to ensure proper population management.
    """

    def __init__(self, event_bus: EventBus, population_controller: NPCPopulationController):
        """
        Initialize the NPC spawning service.

        Args:
            event_bus: Event bus for publishing and subscribing to events
            population_controller: Population controller for managing NPC populations
        """
        self.event_bus = event_bus
        self.population_controller = population_controller

        # Spawn queue and tracking
        self.spawn_queue: list[NPCSpawnRequest] = []
        self.spawn_history: list[NPCSpawnResult] = []
        self.active_npc_instances: dict[str, Any] = {}  # npc_id -> npc_instance

        # Spawn configuration
        self.max_spawn_queue_size = 100
        self.spawn_retry_attempts = 3
        self.spawn_retry_delay = 5.0  # seconds

        # Subscribe to relevant events
        self._subscribe_to_events()

        logger.info("NPC Spawning Service initialized")

    def _subscribe_to_events(self) -> None:
        """Subscribe to relevant game events."""
        self.event_bus.subscribe(PlayerEnteredRoom, self._handle_player_entered_room)
        self.event_bus.subscribe(PlayerLeftRoom, self._handle_player_left_room)
        self.event_bus.subscribe(NPCEnteredRoom, self._handle_npc_entered_room)
        self.event_bus.subscribe(NPCLeftRoom, self._handle_npc_left_room)

    def _handle_player_entered_room(self, event: PlayerEnteredRoom) -> None:
        """Handle player entering a room - trigger spawn checks."""
        self._check_spawn_requirements_for_room(event.room_id)

    def _handle_player_left_room(self, event: PlayerLeftRoom) -> None:
        """Handle player leaving a room - may trigger despawn checks."""
        # For now, we don't automatically despawn NPCs when players leave
        # This could be implemented based on specific requirements
        pass

    def _handle_npc_entered_room(self, event: NPCEnteredRoom) -> None:
        """Handle NPC entering a room."""
        # Update our tracking if this is one of our spawned NPCs
        if event.npc_id in self.active_npc_instances:
            logger.debug(f"Tracked NPC {event.npc_id} entered room {event.room_id}")

    def _handle_npc_left_room(self, event: NPCLeftRoom) -> None:
        """Handle NPC leaving a room."""
        # Update our tracking if this is one of our spawned NPCs
        if event.npc_id in self.active_npc_instances:
            logger.debug(f"Tracked NPC {event.npc_id} left room {event.room_id}")

    def _check_spawn_requirements_for_room(self, room_id: str) -> None:
        """
        Check if NPCs need to be spawned for a specific room.

        Args:
            room_id: The room identifier
        """
        zone_key = self.population_controller._get_zone_key_from_room_id(room_id)
        zone_config = self.population_controller.get_zone_configuration(zone_key)

        if not zone_config:
            logger.warning(f"No zone configuration found for {zone_key} (room: {room_id})")
            return

        # Check each NPC definition for spawn requirements
        for npc_def_id, definition in self.population_controller.npc_definitions.items():
            if definition.sub_zone_id not in zone_key:
                continue

            # Check if this NPC should spawn
            spawn_requests = self._evaluate_spawn_requirements(definition, zone_config, room_id)
            for request in spawn_requests:
                self._queue_spawn_request(request)

    def _evaluate_spawn_requirements(
        self, definition: NPCDefinition, zone_config: ZoneConfiguration, room_id: str
    ) -> list[NPCSpawnRequest]:
        """
        Evaluate spawn requirements for an NPC definition.

        Args:
            definition: NPC definition to evaluate
            zone_config: Zone configuration
            room_id: Target room ID

        Returns:
            List of spawn requests that should be queued
        """
        spawn_requests = []

        # Check population limits
        zone_key = self.population_controller._get_zone_key_from_room_id(room_id)
        stats = self.population_controller.get_population_stats(zone_key)
        if stats:
            current_count = stats.npcs_by_type.get(definition.npc_type, 0)
            if not definition.can_spawn(current_count):
                logger.debug(f"Population limit reached for {definition.name} in {zone_key}")
                return spawn_requests

        # Check spawn rules
        if definition.id in self.population_controller.spawn_rules:
            for rule in self.population_controller.spawn_rules[definition.id]:
                if not rule.can_spawn_for_player_count(self.population_controller.current_game_state["player_count"]):
                    continue

                if not rule.check_spawn_conditions(self.population_controller.current_game_state):
                    continue

                # Determine spawn priority
                priority = self._calculate_spawn_priority(definition, rule, zone_config)

                # Check spawn probability with zone modifier
                effective_probability = zone_config.get_effective_spawn_probability(definition.spawn_probability)
                if random.random() <= effective_probability:
                    request = NPCSpawnRequest(
                        definition=definition,
                        room_id=room_id,
                        spawn_rule=rule,
                        priority=priority,
                        reason="automatic",
                    )
                    spawn_requests.append(request)

        # Required NPCs always spawn if conditions are met
        if definition.is_required() and not spawn_requests:
            # Check if we already have a required NPC of this type
            if stats and stats.npcs_by_type.get(definition.npc_type, 0) == 0:
                request = NPCSpawnRequest(
                    definition=definition,
                    room_id=room_id,
                    spawn_rule=None,  # Required NPCs don't need spawn rules
                    priority=100,  # High priority for required NPCs
                    reason="required",
                )
                spawn_requests.append(request)

        return spawn_requests

    def _calculate_spawn_priority(
        self, definition: NPCDefinition, rule: NPCSpawnRule, zone_config: ZoneConfiguration
    ) -> int:
        """
        Calculate spawn priority for an NPC.

        Args:
            definition: NPC definition
            rule: Spawn rule
            zone_config: Zone configuration

        Returns:
            Priority value (higher = more important)
        """
        priority = 0

        # Base priority by NPC type
        type_priorities = {
            "shopkeeper": 80,
            "quest_giver": 70,
            "passive_mob": 30,
            "aggressive_mob": 20,
        }
        priority += type_priorities.get(definition.npc_type, 50)

        # Required NPCs get higher priority
        if definition.is_required():
            priority += 50

        # Zone spawn modifier affects priority
        priority = int(priority * zone_config.npc_spawn_modifier)

        # Player count affects priority (more players = higher priority for some NPCs)
        player_count = self.population_controller.current_game_state["player_count"]
        if player_count > 0:
            priority += min(player_count * 5, 25)

        return priority

    def _queue_spawn_request(self, request: NPCSpawnRequest) -> None:
        """
        Queue a spawn request for processing.

        Args:
            request: Spawn request to queue
        """
        if len(self.spawn_queue) >= self.max_spawn_queue_size:
            logger.warning("Spawn queue is full, dropping oldest request")
            self.spawn_queue.pop(0)

        # Insert request in priority order
        inserted = False
        for i, existing_request in enumerate(self.spawn_queue):
            if request.priority > existing_request.priority:
                self.spawn_queue.insert(i, request)
                inserted = True
                break

        if not inserted:
            self.spawn_queue.append(request)

        logger.debug(f"Queued spawn request: {request}")

    def process_spawn_queue(self) -> list[NPCSpawnResult]:
        """
        Process all queued spawn requests.

        Returns:
            List of spawn results
        """
        results = []
        requests_to_process = self.spawn_queue.copy()
        self.spawn_queue.clear()

        for request in requests_to_process:
            result = self._spawn_npc_from_request(request)
            results.append(result)
            self.spawn_history.append(result)

            # Keep only recent history
            if len(self.spawn_history) > 1000:
                self.spawn_history = self.spawn_history[-500:]

        return results

    def _spawn_npc_from_request(self, request: NPCSpawnRequest) -> NPCSpawnResult:
        """
        Spawn an NPC from a spawn request.

        Args:
            request: Spawn request to process

        Returns:
            Spawn result
        """
        try:
            # Create NPC instance
            npc_instance = self._create_npc_instance(request.definition, request.room_id)
            if not npc_instance:
                return NPCSpawnResult(
                    success=False,
                    error_message="Failed to create NPC instance",
                    spawn_request=request,
                )

            # Generate unique NPC ID
            npc_id = self._generate_npc_id(request.definition, request.room_id)

            # Store NPC instance
            self.active_npc_instances[npc_id] = npc_instance

            # Update population controller
            self.population_controller._spawn_npc(request.definition, request.room_id)

            # Publish NPC entered room event
            event = NPCEnteredRoom(
                timestamp=None,
                event_type="",
                npc_id=npc_id,
                room_id=request.room_id,
            )
            self.event_bus.publish(event)

            logger.info(f"Successfully spawned NPC: {npc_id} ({request.definition.name}) in {request.room_id}")

            return NPCSpawnResult(
                success=True,
                npc_id=npc_id,
                npc_instance=npc_instance,
                spawn_request=request,
            )

        except Exception as e:
            logger.error(f"Failed to spawn NPC from request {request}: {str(e)}")
            return NPCSpawnResult(
                success=False,
                error_message=str(e),
                spawn_request=request,
            )

    def _create_npc_instance(self, definition: NPCDefinition, room_id: str) -> Any | None:
        """
        Create an NPC instance from a definition.

        Args:
            definition: NPC definition
            room_id: Room where NPC will be spawned

        Returns:
            NPC instance or None if creation failed
        """
        try:
            # Create appropriate NPC type based on definition
            if definition.npc_type == "shopkeeper":
                return ShopkeeperNPC(
                    definition=definition,
                    room_id=room_id,
                    event_bus=self.event_bus,
                    event_reaction_system=None,  # Will be set up later
                )
            elif definition.npc_type == "passive_mob":
                return PassiveMobNPC(
                    definition=definition,
                    room_id=room_id,
                    event_bus=self.event_bus,
                    event_reaction_system=None,  # Will be set up later
                )
            elif definition.npc_type == "aggressive_mob":
                return AggressiveMobNPC(
                    definition=definition,
                    room_id=room_id,
                    event_bus=self.event_bus,
                    event_reaction_system=None,  # Will be set up later
                )
            else:
                logger.warning(f"Unknown NPC type: {definition.npc_type}")
                return None

        except Exception as e:
            logger.error(f"Failed to create NPC instance for {definition.name}: {str(e)}")
            return None

    def _generate_npc_id(self, definition: NPCDefinition, room_id: str) -> str:
        """
        Generate a unique NPC ID.

        Args:
            definition: NPC definition
            room_id: Room where NPC is spawned

        Returns:
            Unique NPC ID
        """
        timestamp = int(time.time())
        random_suffix = random.randint(1000, 9999)
        return f"{definition.name.lower().replace(' ', '_')}_{room_id}_{timestamp}_{random_suffix}"

    def despawn_npc(self, npc_id: str, reason: str = "manual") -> bool:
        """
        Despawn an NPC instance.

        Args:
            npc_id: ID of the NPC to despawn
            reason: Reason for despawning

        Returns:
            True if NPC was despawned successfully
        """
        if npc_id not in self.active_npc_instances:
            logger.warning(f"Attempted to despawn non-existent NPC: {npc_id}")
            return False

        try:
            # Get NPC instance
            npc_instance = self.active_npc_instances[npc_id]

            # Publish NPC left room event
            event = NPCLeftRoom(
                timestamp=None,
                event_type="",
                npc_id=npc_id,
                room_id=npc_instance.room_id,
            )
            self.event_bus.publish(event)

            # Remove from active instances
            del self.active_npc_instances[npc_id]

            # Update population controller
            self.population_controller.despawn_npc(npc_id)

            logger.info(f"Successfully despawned NPC: {npc_id} (reason: {reason})")
            return True

        except Exception as e:
            logger.error(f"Failed to despawn NPC {npc_id}: {str(e)}")
            return False

    def get_spawn_statistics(self) -> dict[str, Any]:
        """
        Get spawning statistics.

        Returns:
            Dictionary containing spawn statistics
        """
        total_requests = len(self.spawn_history)
        successful_spawns = sum(1 for result in self.spawn_history if result.success)
        failed_spawns = total_requests - successful_spawns

        # Count by reason
        reason_counts = {}
        for result in self.spawn_history:
            if result.spawn_request:
                reason = result.spawn_request.reason
                reason_counts[reason] = reason_counts.get(reason, 0) + 1

        # Count by NPC type
        type_counts = {}
        for result in self.spawn_history:
            if result.success and result.spawn_request:
                npc_type = result.spawn_request.definition.npc_type
                type_counts[npc_type] = type_counts.get(npc_type, 0) + 1

        return {
            "total_requests": total_requests,
            "successful_spawns": successful_spawns,
            "failed_spawns": failed_spawns,
            "success_rate": successful_spawns / total_requests if total_requests > 0 else 0.0,
            "active_npcs": len(self.active_npc_instances),
            "queued_requests": len(self.spawn_queue),
            "reason_counts": reason_counts,
            "type_counts": type_counts,
        }

    def cleanup_inactive_npcs(self, max_age_seconds: int = 3600) -> int:
        """
        Clean up inactive NPCs.

        Args:
            max_age_seconds: Maximum age in seconds before cleanup

        Returns:
            Number of NPCs cleaned up
        """
        current_time = time.time()
        npcs_to_remove = []

        for npc_id, npc_instance in self.active_npc_instances.items():
            # Check if NPC has been inactive for too long
            # This is a simplified check - in a real implementation,
            # you might want to track last activity time
            if hasattr(npc_instance, "spawned_at"):
                age = current_time - npc_instance.spawned_at
                if age > max_age_seconds:
                    npcs_to_remove.append(npc_id)

        for npc_id in npcs_to_remove:
            self.despawn_npc(npc_id, reason="cleanup")

        if npcs_to_remove:
            logger.info(f"Cleaned up {len(npcs_to_remove)} inactive NPCs")

        return len(npcs_to_remove)
