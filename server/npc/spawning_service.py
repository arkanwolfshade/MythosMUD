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

# pylint: disable=wrong-import-position  # Reason: Imports after TYPE_CHECKING block avoid circular dependencies

from __future__ import annotations

import random
from typing import TYPE_CHECKING, TypedDict, cast

from structlog.stdlib import BoundLogger

from server.events.event_bus import EventBus

if TYPE_CHECKING:
    from server.npc.behaviors import NPCBase
    from server.npc.population_control import NPCPopulationController
    from server.services.npc_combat_integration_service import NPCCombatIntegrationService

from server.events.event_types import NPCEnteredRoom, NPCLeftRoom, PlayerEnteredRoom, PlayerLeftRoom
from server.models.npc import NPCDefinition, NPCSpawnRule
from server.npc.combat_integration import NPCCombatIntegration
from server.npc.population_control import ZoneConfiguration
from server.npc.population_stats import PopulationStats
from server.npc.spawning_instance_factory import create_npc_instance, generate_npc_id
from server.npc.spawning_models import NPCSpawnRequest, NPCSpawnResult, SimpleNPCDefinition
from server.npc.spawning_request_execution import spawn_npc_from_request

from ..structured_logging.enhanced_logging_config import get_logger

logger: BoundLogger = cast(BoundLogger, get_logger(__name__))


class NPCSpawnStatistics(TypedDict):
    """Schema for get_spawn_statistics() return value."""

    total_requests: int
    successful_spawns: int
    failed_spawns: int
    success_rate: float
    active_npcs: int
    queued_requests: int
    reason_counts: dict[str, int]
    type_counts: dict[str, int]


class NPCSpawningService:
    """
    Service for NPC instance creation and spawn request evaluation.

    This service provides low-level NPC instance creation via _create_npc_instance().
    Spawn request evaluation and queuing functionality may be deprecated/unused.

    SERVICE HIERARCHY:
    - Used by NPCLifecycleManager for actual NPC instance creation
    - Spawn decision logic is handled by NPCPopulationController

    ARCHITECTURE NOTE:
    - _create_npc_instance() is the authoritative method for creating NPC instances
    - Spawn request evaluation (queue, history) may be legacy code
    - Population validation should happen at NPCPopulationController level before calling this
    """

    event_bus: EventBus
    population_controller: NPCPopulationController | None
    combat_integration: NPCCombatIntegration | NPCCombatIntegrationService | None
    max_spawn_queue_size: int
    spawn_retry_attempts: int
    spawn_retry_delay: float

    def __init__(
        self,
        event_bus: EventBus,
        population_controller: NPCPopulationController | None,
        combat_integration: NPCCombatIntegration | NPCCombatIntegrationService | None = None,
    ) -> None:
        """
        Initialize the NPC spawning service.

        Args:
            event_bus: Event bus for publishing and subscribing to events
            population_controller: Population controller for managing NPC populations (can be set later)
            combat_integration: Optional combat integration for aggressive mob NPCs. Use
                NPCCombatIntegration when combat_service is not yet wired (e.g. container NPC bundle
                before NATS combat); use NPCCombatIntegrationService when the full combat stack is available.
        """
        self.event_bus = event_bus
        self.population_controller = population_controller
        self.combat_integration = combat_integration

        self.spawn_queue: list[NPCSpawnRequest] = []
        self.spawn_history: list[NPCSpawnResult] = []

        self.max_spawn_queue_size = 100
        self.spawn_retry_attempts = 3
        self.spawn_retry_delay = 5.0

        self._subscribe_to_events()

        logger.info("NPC Spawning Service initialized")

    def _subscribe_to_events(self) -> None:
        """Subscribe to relevant game events."""
        self.event_bus.subscribe(NPCEnteredRoom, self._handle_npc_entered_room, service_id="npc_spawning_service")
        self.event_bus.subscribe(NPCLeftRoom, self._handle_npc_left_room, service_id="npc_spawning_service")

    def _handle_player_entered_room(self, event: PlayerEnteredRoom) -> None:
        """Handle player entering a room - trigger spawn checks."""
        self._check_spawn_requirements_for_room(event.room_id)

    def _handle_player_left_room(self, _event: PlayerLeftRoom) -> None:
        """Handle player leaving a room - may trigger despawn checks."""

    def _handle_npc_entered_room(self, event: NPCEnteredRoom) -> None:
        """Handle NPC entering a room."""
        logger.debug("NPC entered room event received", npc_id=event.npc_id, room_id=event.room_id)

    def _handle_npc_left_room(self, event: NPCLeftRoom) -> None:
        """Handle NPC leaving a room."""
        logger.debug("NPC left room event received", npc_id=event.npc_id, room_id=event.room_id)

    def _check_spawn_requirements_for_room(self, room_id: str) -> None:
        """
        Check if NPCs need to be spawned for a specific room.

        Args:
            room_id: The room identifier
        """
        if self.population_controller is None:
            return

        zone_key = self.population_controller.get_zone_key_from_room_id(room_id)
        zone_config = self.population_controller.get_zone_configuration(zone_key)

        if not zone_config:
            logger.warning("No zone configuration found", zone_key=zone_key, room_id=room_id)
            return

        for _npc_def_id, definition in self.population_controller.npc_definitions.items():
            if str(definition.sub_zone_id) not in zone_key:
                continue

            spawn_requests = self._evaluate_spawn_requirements(definition, zone_config, room_id)
            for request in spawn_requests:
                self._queue_spawn_request(request)

    def _evaluate_spawn_rules(
        self,
        definition: NPCDefinition,
        zone_config: ZoneConfiguration,
        room_id: str,
        current_npc_count: int,
    ) -> list[NPCSpawnRequest]:
        """Evaluate spawn rules for a definition and return requests that pass conditions and probability."""
        if self.population_controller is None:
            return []
        requests: list[NPCSpawnRequest] = []
        def_id = int(definition.id)
        if def_id not in self.population_controller.spawn_rules:
            return requests
        for rule in self.population_controller.spawn_rules[def_id]:
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
            priority = self._calculate_spawn_priority(definition, rule, zone_config)
            effective_probability = zone_config.get_effective_spawn_probability(float(definition.spawn_probability))
            if random.random() <= effective_probability:  # nosec B311: spawn probability, not cryptographic
                requests.append(
                    NPCSpawnRequest(
                        definition=definition,
                        room_id=room_id,
                        spawn_rule=rule,
                        priority=priority,
                        reason="automatic",
                    )
                )
        return requests

    def _maybe_add_required_npc_request(
        self,
        definition: NPCDefinition,
        room_id: str,
        stats: PopulationStats | None,
        spawn_requests: list[NPCSpawnRequest],
    ) -> None:
        """If definition is required and not yet represented, append a required spawn request."""
        if not definition.is_required() or spawn_requests:
            return
        if not stats or stats.npcs_by_definition.get(int(definition.id), 0):
            return
        spawn_requests.append(
            NPCSpawnRequest(
                definition=definition,
                room_id=room_id,
                spawn_rule=None,
                priority=100,
                reason="required",
            )
        )

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
        if self.population_controller is None:
            return []

        zone_key = self.population_controller.get_zone_key_from_room_id(room_id)
        stats = self.population_controller.get_population_stats(zone_key)
        if stats:
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
                return []

        current_npc_count = stats.npcs_by_definition.get(int(definition.id), 0) if stats else 0
        spawn_requests = self._evaluate_spawn_rules(definition, zone_config, room_id, current_npc_count)
        self._maybe_add_required_npc_request(definition, room_id, stats, spawn_requests)
        return spawn_requests

    def _calculate_spawn_priority(
        self,
        definition: NPCDefinition,
        _rule: NPCSpawnRule,
        zone_config: ZoneConfiguration,  # pylint: disable=unused-argument  # Reason: reserved for future priority rules
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

        type_priorities = {
            "shopkeeper": 80,
            "quest_giver": 70,
            "passive_mob": 30,
            "aggressive_mob": 20,
        }
        priority += type_priorities.get(str(definition.npc_type), 50)

        if definition.is_required():
            priority += 50

        priority = int(priority * zone_config.npc_spawn_modifier)

        if self.population_controller is not None and self.population_controller.current_game_state:
            # current_game_state is dict[str, object]; .get is object until narrowed.
            pc_raw = self.population_controller.current_game_state.get("player_count", 0)
            if isinstance(pc_raw, int) and pc_raw > 0:
                priority += min(pc_raw * 5, 25)

        return priority

    def _queue_spawn_request(self, request: NPCSpawnRequest) -> None:
        """
        Queue a spawn request for processing.

        Args:
            request: Spawn request to queue
        """
        if len(self.spawn_queue) >= self.max_spawn_queue_size:
            logger.warning("Spawn queue is full, dropping oldest request")
            _ = self.spawn_queue.pop(0)

        inserted = False
        for i, existing_request in enumerate(self.spawn_queue):
            if request.priority > existing_request.priority:
                self.spawn_queue.insert(i, request)
                inserted = True
                break

        if not inserted:
            self.spawn_queue.append(request)

        definition_name = getattr(request.definition, "name", "Unknown NPC")
        logger.debug("Queued spawn request", npc_name=definition_name, room_id=request.room_id)

    def process_spawn_queue(self) -> list[NPCSpawnResult]:
        """
        Process all queued spawn requests.

        Returns:
            List of spawn results
        """
        results: list[NPCSpawnResult] = []
        requests_to_process = self.spawn_queue.copy()
        self.spawn_queue.clear()

        for request in requests_to_process:
            result = self._spawn_npc_from_request(request)
            results.append(result)
            self.spawn_history.append(result)

            if len(self.spawn_history) > 1000:
                self.spawn_history = self.spawn_history[-500:]

        return results

    def _spawn_npc_from_request(self, request: NPCSpawnRequest) -> NPCSpawnResult:
        """Spawn an NPC from a spawn request."""
        return spawn_npc_from_request(
            request,
            create_npc_instance=self._create_npc_instance,
            generate_npc_id=self._generate_npc_id,
        )

    def _create_npc_instance(
        self, definition: NPCDefinition, room_id: str, npc_id: str | None = None
    ) -> NPCBase | None:
        """Create an NPC instance from a definition."""
        return create_npc_instance(
            definition,
            room_id,
            self.event_bus,
            self.combat_integration,
            npc_id=npc_id,
        )

    def create_npc_instance(self, definition: NPCDefinition, room_id: str, npc_id: str | None = None) -> NPCBase | None:
        """
        Public wrapper for NPC instance creation used by lifecycle manager.

        This delegates to the internal _create_npc_instance helper while providing
        a non-protected API for other components.
        """
        return self._create_npc_instance(definition, room_id, npc_id)

    def _generate_npc_id(self, definition: NPCDefinition | SimpleNPCDefinition, room_id: str) -> str:
        """Generate a unique NPC ID."""
        return generate_npc_id(definition, room_id)

    def despawn_npc(self, npc_id: str, _reason: str = "manual") -> bool:  # pylint: disable=unused-argument  # Reason: future reason-based despawn
        """
        Despawn an NPC instance.

        Args:
            npc_id: ID of the NPC to despawn
            reason: Reason for despawning

        Returns:
            True if NPC was despawned successfully
        """
        logger.warning(
            "Despawn request for NPC", npc_id=npc_id, message="NPC instances now managed by lifecycle manager"
        )
        return False

    def _count_spawn_reasons(self, history: list[NPCSpawnResult]) -> dict[str, int]:
        """Count spawn results by request reason."""
        reason_counts: dict[str, int] = {}
        for result in history:
            if result.spawn_request:
                reason = result.spawn_request.reason
                reason_counts[reason] = reason_counts.get(reason, 0) + 1
        return reason_counts

    def _count_spawn_types(self, history: list[NPCSpawnResult]) -> dict[str, int]:
        """Count successful spawn results by NPC type (enum value or string for mocks)."""
        type_counts: dict[str, int] = {}
        for result in history:
            if result.success and result.spawn_request:
                npc_type = result.spawn_request.definition.npc_type
                npc_type_str = str(getattr(npc_type, "value", npc_type))
                type_counts[npc_type_str] = type_counts.get(npc_type_str, 0) + 1
        return type_counts

    def get_spawn_statistics(self) -> NPCSpawnStatistics:
        """
        Get spawning statistics.

        Returns:
            Dictionary containing spawn statistics
        """
        total_requests = len(self.spawn_history)
        successful_spawns = sum(1 for result in self.spawn_history if result.success)
        failed_spawns = total_requests - successful_spawns
        success_rate = successful_spawns / total_requests if total_requests > 0 else 0.0
        return {
            "total_requests": total_requests,
            "successful_spawns": successful_spawns,
            "failed_spawns": failed_spawns,
            "success_rate": success_rate,
            "active_npcs": 0,
            "queued_requests": len(self.spawn_queue),
            "reason_counts": self._count_spawn_reasons(self.spawn_history),
            "type_counts": self._count_spawn_types(self.spawn_history),
        }

    def cleanup_inactive_npcs(self, max_age_seconds: int = 3600) -> int:
        """
        Clean up inactive NPCs.

        Args:
            max_age_seconds: Maximum age in seconds before cleanup

        Returns:
            Number of NPCs cleaned up
        """
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

        return self.population_controller.get_zone_key_from_room_id(room_id)

    def get_population_stats(self, zone_key: str) -> PopulationStats | None:
        """
        Return zone-level NPC population aggregates for a zone key.

        Args:
            zone_key: Zone key in the form "zone/sub_zone".

        Returns:
            PopulationStats for the zone, or None if there is no controller or no stats yet.
        """
        if self.population_controller is None:
            return None

        return self.population_controller.get_population_stats(zone_key)
