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

import random
import time
from dataclasses import dataclass
from typing import Any

from server.events.event_bus import EventBus
from server.events.event_types import NPCEnteredRoom, NPCLeftRoom, PlayerEnteredRoom, PlayerLeftRoom
from server.models.npc import NPCDefinition, NPCSpawnRule
from server.npc.behaviors import AggressiveMobNPC, NPCBase, PassiveMobNPC, ShopkeeperNPC
from server.npc.population_control import NPCPopulationController, ZoneConfiguration

from ..logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)


@dataclass
class SimpleNPCDefinition:
    """Simple data class to hold NPC definition data without SQLAlchemy relationships."""

    id: int
    name: str
    npc_type: str
    room_id: str | None
    base_stats: str
    behavior_config: str
    ai_integration_stub: str


class NPCSpawnRequest:
    """Represents a request to spawn an NPC."""

    def __init__(
        self,
        definition: NPCDefinition,
        room_id: str,
        spawn_rule: NPCSpawnRule | None = None,
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

    def __init__(self, event_bus: EventBus, population_controller: "NPCPopulationController | None"):
        """
        Initialize the NPC spawning service.

        Args:
            event_bus: Event bus for publishing and subscribing to events
            population_controller: Population controller for managing NPC populations (can be set later)
        """
        self.event_bus = event_bus
        self.population_controller = population_controller

        # Spawn queue and tracking
        self.spawn_queue: list[NPCSpawnRequest] = []
        self.spawn_history: list[NPCSpawnResult] = []

        # Spawn configuration
        self.max_spawn_queue_size = 100
        self.spawn_retry_attempts = 3
        self.spawn_retry_delay = 5.0  # seconds

        # Subscribe to relevant events
        self._subscribe_to_events()

        logger.info("NPC Spawning Service initialized")

    def _subscribe_to_events(self) -> None:
        """Subscribe to relevant game events."""
        # NOTE: Removed PlayerEnteredRoom subscription to prevent duplicate spawning
        # The population controller is the sole authority for spawn decisions
        # self.event_bus.subscribe(PlayerEnteredRoom, self._handle_player_entered_room)
        # self.event_bus.subscribe(PlayerLeftRoom, self._handle_player_left_room)
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
        # Note: NPC instances are now managed by lifecycle manager
        # This method is kept for compatibility but no longer tracks instances
        logger.debug("NPC entered room event received", npc_id=event.npc_id, room_id=event.room_id)

    def _handle_npc_left_room(self, event: NPCLeftRoom) -> None:
        """Handle NPC leaving a room."""
        # Note: NPC instances are now managed by lifecycle manager
        # This method is kept for compatibility but no longer tracks instances
        logger.debug("NPC left room event received", npc_id=event.npc_id, room_id=event.room_id)

    def _check_spawn_requirements_for_room(self, room_id: str) -> None:
        """
        Check if NPCs need to be spawned for a specific room.

        Args:
            room_id: The room identifier
        """
        if self.population_controller is None:
            return

        zone_key = self.population_controller._get_zone_key_from_room_id(room_id)
        zone_config = self.population_controller.get_zone_configuration(zone_key)

        if not zone_config:
            logger.warning("No zone configuration found", zone_key=zone_key, room_id=room_id)
            return

        # Check each NPC definition for spawn requirements
        for _npc_def_id, definition in self.population_controller.npc_definitions.items():
            if str(definition.sub_zone_id) not in zone_key:
                continue

            # Check if this NPC should spawn
            spawn_requests = self._evaluate_spawn_requirements(definition, zone_config, room_id)
            for request in spawn_requests:
                self._queue_spawn_request(request)

    def _evaluate_spawn_requirements(
        self, definition: NPCDefinition, zone_config: "ZoneConfiguration", room_id: str
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
        if self.population_controller is None:
            return []

        spawn_requests: list[NPCSpawnRequest] = []

        # Check population limits
        zone_key = self.population_controller._get_zone_key_from_room_id(room_id)
        stats = self.population_controller.get_population_stats(zone_key)
        if stats:
            # Check by individual NPC definition ID, not by type
            current_count = stats.npcs_by_definition.get(int(definition.id), 0)
            if not definition.can_spawn(current_count):
                definition_name = getattr(definition, "name", "Unknown NPC")
                logger.debug(
                    "Population limit reached",
                    npc_name=definition_name,
                    zone_key=zone_key,
                    current_count=current_count,
                    max_population=definition.max_population,
                )
                return spawn_requests

        # Get current NPC count for this specific definition
        current_npc_count = stats.npcs_by_definition.get(int(definition.id), 0) if stats else 0

        # Check spawn rules
        if int(definition.id) in self.population_controller.spawn_rules:
            for rule in self.population_controller.spawn_rules[int(definition.id)]:
                # Check if current NPC population allows spawning more instances
                if not rule.can_spawn_with_population(current_npc_count):
                    logger.debug(
                        "Spawn rule population limit reached",
                        npc_name=definition.name,
                        current_npc_count=current_npc_count,
                        max_population=rule.max_population,
                    )
                    continue

                if not rule.check_spawn_conditions(self.population_controller.current_game_state):
                    continue

                # Determine spawn priority
                priority = self._calculate_spawn_priority(definition, rule, zone_config)

                # Check spawn probability with zone modifier
                effective_probability = zone_config.get_effective_spawn_probability(float(definition.spawn_probability))
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
            # Check if we already have a required NPC of this specific definition
            if stats and stats.npcs_by_definition.get(int(definition.id), 0) == 0:
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
        self, definition: NPCDefinition, rule: NPCSpawnRule, zone_config: "ZoneConfiguration"
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
        # AI Agent note: Use npc_type.value to get string value from enum
        # str(enum) returns "NPCDefinitionType.SHOPKEEPER", but we need "shopkeeper"
        type_priorities = {
            "shopkeeper": 80,
            "quest_giver": 70,
            "passive_mob": 30,
            "aggressive_mob": 20,
        }
        priority += type_priorities.get(str(definition.npc_type.value), 50)

        # Required NPCs get higher priority
        if definition.is_required():
            priority += 50

        # Zone spawn modifier affects priority
        priority = int(priority * zone_config.npc_spawn_modifier)

        # Player count affects priority (more players = higher priority for some NPCs)
        if self.population_controller is not None and self.population_controller.current_game_state:
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

        # Avoid logging the entire request object to prevent recursion issues
        definition_name = getattr(request.definition, "name", "Unknown NPC")
        logger.debug("Queued spawn request", npc_name=definition_name, room_id=request.room_id)

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

            # Don't call back into population controller to avoid circular dependency
            # The population controller will update its own statistics when needed

            # Mutate room state via Room API which will publish the event
            from ..persistence import get_persistence

            persistence = get_persistence()
            room = persistence.get_room(request.room_id)
            if not room:
                definition_name = getattr(request.definition, "name", "Unknown NPC")
                logger.warning("Room not found for NPC spawn", npc_name=definition_name, room_id=request.room_id)
                return NPCSpawnResult(
                    success=False,
                    error_message="Room not found",
                    spawn_request=request,
                )
            room.npc_entered(npc_id)

            # Use getattr to safely access definition.name to avoid recursion issues
            definition_name = getattr(request.definition, "name", "Unknown NPC")
            logger.info("Successfully spawned NPC", npc_id=npc_id, npc_name=definition_name, room_id=request.room_id)

            return NPCSpawnResult(
                success=True,
                npc_id=npc_id,
                npc_instance=npc_instance,
                spawn_request=request,
            )

        except Exception as e:
            logger.error("Failed to spawn NPC from request", request=request, error=str(e))
            return NPCSpawnResult(
                success=False,
                error_message=str(e),
                spawn_request=request,
            )

    def _create_npc_instance(self, definition: NPCDefinition, room_id: str, npc_id: str | None = None) -> Any | None:
        """
        Create an NPC instance from a definition.

        Args:
            definition: NPC definition
            room_id: Room where NPC will be spawned
            npc_id: Optional pre-generated NPC ID (if None, will generate one)

        Returns:
            NPC instance or None if creation failed
        """
        try:
            # Extract all attributes first to avoid any potential lazy loading issues
            definition_id = getattr(definition, "id", 0)
            definition_name = getattr(definition, "name", "Unknown NPC")
            definition_type = getattr(definition, "npc_type", "unknown")
            definition_room_id = getattr(definition, "room_id", None)
            definition_base_stats = getattr(definition, "base_stats", "{}")
            definition_behavior_config = getattr(definition, "behavior_config", "{}")
            definition_ai_integration_stub = getattr(definition, "ai_integration_stub", "{}")

            # Convert NPCDefinition to SimpleNPCDefinition to avoid SQLAlchemy relationship issues
            simple_definition = SimpleNPCDefinition(
                id=definition_id,
                name=definition_name,
                npc_type=definition_type,
                room_id=definition_room_id,
                base_stats=definition_base_stats,
                behavior_config=definition_behavior_config,
                ai_integration_stub=definition_ai_integration_stub,
            )

            # Generate a unique NPC ID if not provided
            if npc_id is None:
                npc_id = self._generate_npc_id(simple_definition, room_id)

            # Create appropriate NPC type based on definition
            # Type annotation for base class to allow different subclass assignments
            npc_instance: NPCBase
            if simple_definition.npc_type == "shopkeeper":
                npc_instance = ShopkeeperNPC(
                    definition=simple_definition,
                    npc_id=npc_id,
                    event_bus=self.event_bus,
                    event_reaction_system=None,  # Will be set up later
                )
            elif simple_definition.npc_type == "passive_mob":
                npc_instance = PassiveMobNPC(
                    definition=simple_definition,
                    npc_id=npc_id,
                    event_bus=self.event_bus,
                    event_reaction_system=None,  # Will be set up later
                )
            elif simple_definition.npc_type == "aggressive_mob":
                npc_instance = AggressiveMobNPC(
                    definition=simple_definition,
                    npc_id=npc_id,
                    event_bus=self.event_bus,
                    event_reaction_system=None,  # Will be set up later
                )
            elif simple_definition.npc_type == "quest_giver":
                # For now, treat quest_giver as a passive_mob until we implement specific quest behavior
                npc_instance = PassiveMobNPC(
                    definition=simple_definition,
                    npc_id=npc_id,
                    event_bus=self.event_bus,
                    event_reaction_system=None,  # Will be set up later
                )
            else:
                logger.warning("Unknown NPC type", npc_type=simple_definition.npc_type)
                return None

            # Set the current room for the NPC instance
            npc_instance.current_room = room_id

            return npc_instance

        except Exception as e:
            # Use extracted name to avoid potential lazy loading issues
            definition_name = getattr(definition, "name", "Unknown NPC")
            logger.error("Failed to create NPC instance", npc_name=definition_name, error=str(e))
            return None

    def _generate_npc_id(self, definition: NPCDefinition | SimpleNPCDefinition, room_id: str) -> str:
        """
        Generate a unique NPC ID.

        Args:
            definition: NPC definition (either NPCDefinition or SimpleNPCDefinition)
            room_id: Room where NPC is spawned

        Returns:
            Unique NPC ID
        """
        timestamp = int(time.time())
        random_suffix = random.randint(1000, 9999)
        # Use getattr to avoid potential lazy loading issues
        definition_name = getattr(definition, "name", "unknown_npc")
        return f"{definition_name.lower().replace(' ', '_')}_{room_id}_{timestamp}_{random_suffix}"

    def despawn_npc(self, npc_id: str, reason: str = "manual") -> bool:
        """
        Despawn an NPC instance.

        Args:
            npc_id: ID of the NPC to despawn
            reason: Reason for despawning

        Returns:
            True if NPC was despawned successfully
        """
        # Note: NPC instances are now managed by lifecycle manager
        # This method should delegate to the lifecycle manager
        logger.warning(
            "Despawn request for NPC", npc_id=npc_id, message="NPC instances now managed by lifecycle manager"
        )
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
        reason_counts: dict[str, int] = {}
        for result in self.spawn_history:
            if result.spawn_request:
                reason = result.spawn_request.reason
                reason_counts[reason] = reason_counts.get(reason, 0) + 1

        # Count by NPC type
        # AI Agent note: Use npc_type.value to get string value from enum
        # str(enum) returns "NPCDefinitionType.SHOPKEEPER", but we need "shopkeeper"
        # Handle both enum and string types (string for mocks in tests)
        type_counts: dict[str, int] = {}
        for result in self.spawn_history:
            if result.success and result.spawn_request:
                npc_type = result.spawn_request.definition.npc_type
                npc_type_str = str(npc_type.value if hasattr(npc_type, "value") else npc_type)
                type_counts[npc_type_str] = type_counts.get(npc_type_str, 0) + 1

        return {
            "total_requests": total_requests,
            "successful_spawns": successful_spawns,
            "failed_spawns": failed_spawns,
            "success_rate": successful_spawns / total_requests if total_requests > 0 else 0.0,
            "active_npcs": 0,  # NPC instances now managed by lifecycle manager
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
        # Note: NPC instances are now managed by lifecycle manager
        # This method should delegate to the lifecycle manager
        logger.info(
            "Cleanup request received",
            max_age_seconds=max_age_seconds,
            message="NPC instances now managed by lifecycle manager",
        )
        return 0

    def _get_zone_key_from_room_id(self, room_id: str) -> str:
        """
        Extract zone key from room ID by delegating to the population controller.

        Args:
            room_id: The room identifier

        Returns:
            Zone key in format "zone/sub_zone"
        """
        if self.population_controller is None:
            return "unknown/unknown"

        return self.population_controller._get_zone_key_from_room_id(room_id)

    def get_population_stats(self, zone_key: str) -> Any | None:
        """
        Get population statistics for a given zone by delegating to the population controller.

        Args:
            zone_key: Zone key in format "zone/sub_zone"

        Returns:
            Population statistics or None if not found
        """
        if self.population_controller is None:
            return None

        return self.population_controller.get_population_stats(zone_key)
