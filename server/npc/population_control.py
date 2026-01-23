"""
NPC Population Control System.

This module implements sub-zone-based NPC population management, including
spawning, despawning, and population monitoring across different zones and
sub-zones of the game world.

As documented in the Cultes des Goules, proper population management is essential
for maintaining the delicate balance between the mundane and the eldritch forces
that lurk in the shadows of our world. The spawn modifiers found in zone
configurations reflect the inherent mystical properties of different locations.
"""

# pylint: disable=too-many-lines  # Reason: Population control requires extensive population management logic for comprehensive NPC population tracking and control

import time
from typing import Any, cast

from server.events.event_bus import EventBus
from server.events.event_types import (
    NPCEnteredRoom,
    NPCLeftRoom,
    PlayerEnteredRoom,
    PlayerLeftRoom,
)
from server.models.npc import NPCDefinition, NPCSpawnRule

from ..structured_logging.enhanced_logging_config import get_logger
from .npc_utils import (
    extract_definition_id_from_npc,
    extract_npc_metadata,
    extract_room_id_from_npc,
    get_zone_key_from_room_id,
)
from .population_stats import PopulationStats
from .spawn_validator import should_spawn_npc
from .zone_config_loader import load_zone_configurations
from .zone_configuration import ZoneConfiguration

logger = get_logger(__name__)


class NPCPopulationController:  # pylint: disable=too-many-instance-attributes  # Reason: Population controller requires many state tracking and configuration attributes
    """
    Controller for NPC population management across zones and sub-zones.

    This class manages population limits, zone rules, and spawn validation.
    It queries NPCLifecycleManager for active NPC instances and maintains
    population_stats for zone-level aggregates.

    SERVICE HIERARCHY:
    - Level 2: Population limits and zone rules
    - Uses: NPCLifecycleManager (queries active_npcs, calls spawn_npc)
    - Used by: NPCInstanceService

    ARCHITECTURE NOTES:
    - NO longer maintains duplicate active_npcs tracking (removed in unification)
    - Queries lifecycle_manager.active_npcs via helper methods when needed
    - Maintains population_stats for zone-level population aggregates only
    - Validates population limits BEFORE calling lifecycle_manager.spawn_npc()
    - NPCLifecycleManager.active_npcs is the single source of truth for active NPC instances
    """

    def __init__(
        self,
        event_bus: EventBus,
        spawning_service: Any = None,
        lifecycle_manager: Any = None,
        async_persistence: Any = None,
    ) -> None:
        """
        Initialize the NPC population controller.

        Args:
            event_bus: Event bus for publishing and subscribing to events
            spawning_service: Optional NPC spawning service for proper NPC creation
            lifecycle_manager: Optional NPC lifecycle manager for consistent ID generation
            async_persistence: Async persistence layer for loading zone configs from database (required)
        """
        self.event_bus = event_bus
        self.spawning_service = spawning_service
        self.lifecycle_manager = lifecycle_manager
        self.async_persistence = async_persistence

        if self.async_persistence is None:
            raise ValueError("async_persistence is required for NPCPopulationController")

        # Population tracking
        self.population_stats: dict[str, PopulationStats] = {}
        # REMOVED: self.active_npcs - NPCLifecycleManager.active_npcs is now the single source of truth
        # Use _get_active_npcs_from_lifecycle_manager() helper method to query NPC instances
        self.zone_configurations: dict[str, ZoneConfiguration] = {}

        # Clear population stats on initialization to ensure clean state
        self.clear_population_stats()
        logger.info("Clearing population stats on initialization")

        # NPC definitions and spawn rules (loaded from database)
        self.npc_definitions: dict[int, NPCDefinition] = {}
        self.spawn_rules: dict[int, list[NPCSpawnRule]] = {}

        # Game state tracking
        self.current_game_state: dict[str, Any] = {
            "time_of_day": "day",
            "weather": "clear",
            "player_count": 0,
            "player_level_min": 1,
        }

        # Load zone configurations
        self._load_zone_configurations()

        # Subscribe to relevant events
        self._subscribe_to_events()

        logger.info("NPC Population Controller initialized", zones_loaded=len(self.zone_configurations))

    def _load_zone_configurations(self) -> None:
        """Load zone and sub-zone configurations from PostgreSQL database."""
        self.zone_configurations = load_zone_configurations()

    def _subscribe_to_events(self) -> None:
        """Subscribe to relevant game events."""
        logger.info("NPC Population Controller subscribing to game events")
        # Use service_id for tracking and cleanup (Task 2: Event Subscriber Cleanup)
        self.event_bus.subscribe(
            PlayerEnteredRoom, self._handle_player_entered_room, service_id="npc_population_control"
        )
        self.event_bus.subscribe(PlayerLeftRoom, self._handle_player_left_room, service_id="npc_population_control")
        self.event_bus.subscribe(NPCEnteredRoom, self._handle_npc_entered_room, service_id="npc_population_control")
        self.event_bus.subscribe(NPCLeftRoom, self._handle_npc_left_room, service_id="npc_population_control")
        logger.info("NPC Population Controller event subscriptions completed")

    def _handle_player_entered_room(self, event: PlayerEnteredRoom) -> None:
        """Handle player entering a room."""
        logger.info(
            "NPC Population Controller received PlayerEnteredRoom event",
            player_id=event.player_id,
            room_id=event.room_id,
        )

        # Update player count for the zone
        self._update_player_count()

        # Check if we need to spawn NPCs based on new player presence
        self._check_spawn_requirements_for_room(event.room_id)

    def _handle_player_left_room(self, _event: PlayerLeftRoom) -> None:
        """Handle player leaving a room."""
        # Update player count for the zone
        self._update_player_count()

    def _handle_npc_entered_room(self, event: NPCEnteredRoom) -> None:
        """Handle NPC entering a room."""
        # Note: Population statistics are tracked in _spawn_npc_instance, not here
        # This method is kept for potential future room-specific tracking needs
        logger.debug("NPC entered room", npc_id=event.npc_id, room_id=event.room_id)

    def _handle_npc_left_room(self, event: NPCLeftRoom) -> None:
        """Handle NPC leaving a room."""
        # Note: Population statistics are tracked in _despawn_npc_instance, not here
        # This method is kept for potential future room-specific tracking needs
        logger.debug("NPC left room", npc_id=event.npc_id, room_id=event.room_id)

    def _get_active_npcs_from_lifecycle_manager(self) -> dict[str, Any]:
        """
        Get active NPCs from the lifecycle manager (single source of truth).

        Returns:
            Dictionary mapping npc_id to NPC instance data, or empty dict if lifecycle_manager unavailable
        """
        if not self.lifecycle_manager or not hasattr(self.lifecycle_manager, "active_npcs"):
            return {}
        result: dict[str, Any] = cast(dict[str, Any], self.lifecycle_manager.active_npcs)
        return result

    def _update_player_count(self) -> None:
        """Update the current player count in game state."""
        # This would typically query the player service
        # For now, we'll use a placeholder
        self.current_game_state["player_count"] = 1  # Placeholder

    def load_npc_definitions(self, definitions: list[NPCDefinition]) -> None:
        """
        Load NPC definitions from the database.

        Args:
            definitions: List of NPC definitions to load
        """
        self.npc_definitions.clear()
        for definition in definitions:
            self.npc_definitions[int(definition.id)] = definition
            logger.debug(
                "Loaded NPC definition", npc_id=definition.id, npc_name=definition.name, npc_type=definition.npc_type
            )

    def load_spawn_rules(self, rules: list[NPCSpawnRule]) -> None:
        """
        Load spawn rules from the database.

        Args:
            rules: List of spawn rules to load
        """
        self.spawn_rules.clear()
        for rule in rules:
            if int(rule.npc_definition_id) not in self.spawn_rules:
                self.spawn_rules[int(rule.npc_definition_id)] = []
            self.spawn_rules[int(rule.npc_definition_id)].append(rule)
            logger.debug(
                "Loaded spawn rule",
                rule_id=rule.id,
                npc_definition_id=rule.npc_definition_id,
                sub_zone_id=rule.sub_zone_id,
            )

    def update_game_state(self, new_state: dict[str, Any]) -> None:
        """
        Update the current game state.

        Args:
            new_state: Dictionary containing new game state values
        """
        self.current_game_state.update(new_state)
        logger.debug("Updated game state", new_state=new_state)

    def get_zone_configuration(self, zone_key: str) -> ZoneConfiguration | None:
        """
        Get zone configuration for a given zone key.

        Args:
            zone_key: Zone key in format "zone/sub_zone" or "zone"

        Returns:
            Zone configuration or None if not found
        """
        # First, try exact match
        config = self.zone_configurations.get(zone_key)
        if config:
            return config

        # If zone_key is "zone/subzone" format and not found, try zone-level config as fallback
        if "/" in zone_key:
            zone_name = zone_key.split("/")[0]
            config = self.zone_configurations.get(zone_name)
            if config:
                logger.debug(
                    "Subzone config not found, using zone-level config as fallback",
                    requested_zone_key=zone_key,
                    fallback_zone_key=zone_name,
                )
                return config

        return None

    def get_population_stats(self, zone_key: str) -> PopulationStats | None:
        """
        Get population statistics for a given zone.

        Args:
            zone_key: Zone key in format "zone/sub_zone"

        Returns:
            Population statistics or None if not found
        """
        return self.population_stats.get(zone_key)

    def _get_zone_key_from_room_id(self, room_id: str) -> str:
        """
        Extract zone key from room ID.

        Args:
            room_id: The room identifier

        Returns:
            Zone key in format "zone/sub_zone"
        """
        return get_zone_key_from_room_id(room_id)

    def _check_spawn_requirements_for_room(self, room_id: str) -> None:
        """
        Check if NPCs need to be spawned for a specific room.

        Args:
            room_id: The room identifier
        """
        logger.info("Checking spawn requirements for room", room_id=room_id)
        zone_key = get_zone_key_from_room_id(room_id)
        logger.info("Generated zone key", zone_key=zone_key)
        zone_config = self.get_zone_configuration(zone_key)

        if not zone_config:
            # Check if we have any zone configurations loaded at all
            available_keys = list(self.zone_configurations.keys())
            logger.warning(
                "No zone configuration found",
                zone_key=zone_key,
                room_id=room_id,
                total_configs_loaded=len(self.zone_configurations),
                available_keys=available_keys[:10] if len(available_keys) > 10 else available_keys,
                message="This may indicate a missing zone configuration in the database or a key mismatch",
            )
            # Don't return early - some rooms may not need NPC spawning
            # Instead, we'll just skip NPC spawning for this room
            return

        logger.info("Zone configuration found", zone_key=zone_key)

        # Check each NPC definition for spawn requirements
        logger.info("Checking NPC definitions for spawn requirements", npc_count=len(self.npc_definitions))
        for _npc_def_id, definition in self.npc_definitions.items():
            logger.info(
                "Checking NPC", npc_id=definition.id, npc_name=definition.name, sub_zone_id=definition.sub_zone_id
            )
            if str(definition.sub_zone_id) not in zone_key:
                logger.info(
                    "NPC sub_zone not in zone_key, skipping",
                    npc_id=definition.id,
                    sub_zone_id=definition.sub_zone_id,
                    zone_key=zone_key,
                )
                continue

            logger.info("NPC sub_zone matches, checking spawn conditions", npc_id=definition.id)
            # Check if this NPC should spawn
            if self._should_spawn_npc(definition, zone_config, room_id):
                logger.info("NPC should spawn, attempting spawn", npc_id=definition.id, npc_name=definition.name)
                self._spawn_npc(definition, room_id)
            else:
                logger.info("NPC should not spawn", npc_id=definition.id, npc_name=definition.name)

    def _should_spawn_npc(self, definition: NPCDefinition, zone_config: ZoneConfiguration, room_id: str) -> bool:
        """
        Determine if an NPC should spawn based on conditions.

        Args:
            definition: NPC definition
            zone_config: Zone configuration
            room_id: Target room ID

        Returns:
            True if NPC should spawn, False otherwise
        """
        zone_key = self._get_zone_key_from_room_id(room_id)
        stats = self.get_population_stats(zone_key)
        return should_spawn_npc(definition, zone_config, room_id, stats, self.spawn_rules, self.current_game_state)

    def _spawn_npc(self, definition: NPCDefinition, room_id: str) -> str | None:
        """
        Spawn an NPC instance using the lifecycle manager.

        Args:
            definition: NPC definition
            room_id: Room where to spawn the NPC

        Returns:
            Generated NPC instance ID, or None if spawn failed
        """
        if not self.lifecycle_manager:
            logger.error("No lifecycle manager available - cannot spawn NPC")
            return None

        try:
            # Use the lifecycle manager to spawn the NPC (this ensures consistent ID generation)
            npc_id = self.lifecycle_manager.spawn_npc(definition, room_id, "population_control")

            if npc_id:
                # Update population statistics
                zone_key = get_zone_key_from_room_id(room_id)
                if zone_key not in self.population_stats:
                    zone_parts = zone_key.split("/")
                    self.population_stats[zone_key] = PopulationStats(zone_parts[0], zone_parts[1])

                stats = self.population_stats[zone_key]

                # Log population stats before adding NPC
                logger.debug(
                    "Population stats before adding NPC",
                    npc_id=npc_id,
                    npc_name=definition.name,
                    definition_id=definition.id,
                    zone_key=zone_key,
                    current_count_by_definition=stats.npcs_by_definition.get(int(definition.id), 0),
                    max_population=definition.max_population,
                )

                stats.add_npc(str(definition.npc_type), room_id, definition.is_required(), int(definition.id))

                # Log population stats after adding NPC
                logger.debug(
                    "Population stats after adding NPC",
                    npc_id=npc_id,
                    npc_name=definition.name,
                    definition_id=definition.id,
                    zone_key=zone_key,
                    new_count_by_definition=stats.npcs_by_definition.get(int(definition.id), 0),
                    max_population=definition.max_population,
                )

                # REMOVED: No longer storing duplicate NPC data here
                # NPCLifecycleManager.active_npcs is the single source of truth for NPC instances
                # Population statistics are maintained in population_stats for zone-level aggregates

                # Use getattr to avoid potential lazy loading issues
                definition_name = getattr(definition, "name", "Unknown NPC")
                logger.info(
                    "Spawned NPC",
                    npc_id=npc_id,
                    npc_name=definition_name,
                    npc_type=definition.npc_type,
                    room_id=room_id,
                    zone_key=zone_key,
                )
                result: str = cast(str, npc_id)
                return result

            # NPC spawn failed or returned None
            # Use getattr to avoid potential lazy loading issues
            definition_name = getattr(definition, "name", "Unknown NPC")
            logger.error("Failed to spawn NPC", npc_name=definition_name, room_id=room_id)
            return None

        except (ValueError, KeyError, AttributeError, TypeError, IndexError, RuntimeError) as e:
            # Use getattr to avoid potential lazy loading issues
            definition_name = getattr(definition, "name", "Unknown NPC")
            logger.error("Error spawning NPC", npc_name=definition_name, error=str(e))
            return None

    def spawn_npc(self, definition: NPCDefinition, room_id: str) -> str | None:
        """
        Spawn an NPC instance using the population controller.

        This is the public API for spawning NPCs through the population controller.
        It ensures proper population validation and tracking.

        Args:
            definition: NPC definition
            room_id: Room where to spawn the NPC

        Returns:
            Generated NPC instance ID, or None if spawn failed
        """
        return self._spawn_npc(definition, room_id)

    def _update_population_stats_for_despawn(
        self, room_id: str, npc_type: str, is_required: bool, definition_id: int | None
    ) -> None:
        """
        Update population statistics when an NPC is despawned.

        Args:
            room_id: Room ID where the NPC was located
            npc_type: Type of the NPC
            is_required: Whether the NPC was required
            definition_id: Definition ID of the NPC
        """
        if not room_id or room_id == "unknown":
            return

        zone_key = get_zone_key_from_room_id(room_id)
        if zone_key not in self.population_stats:
            return

        stats = self.population_stats[zone_key]
        stats.remove_npc(npc_type, room_id, is_required, definition_id)

    def despawn_npc(self, npc_id: str) -> bool:
        """
        Despawn an NPC instance.

        This method updates population statistics when an NPC is despawned.
        Actual despawning is handled by NPCLifecycleManager.

        Args:
            npc_id: ID of the NPC to despawn

        Returns:
            True if NPC was despawned, False if not found
        """
        active_npcs = self._get_active_npcs_from_lifecycle_manager()
        if npc_id not in active_npcs:
            logger.warning("Attempted to despawn non-existent NPC", npc_id=npc_id)
            return False

        npc_instance = active_npcs[npc_id]
        room_id = extract_room_id_from_npc(npc_instance)
        npc_type, is_required = extract_npc_metadata(npc_instance)
        definition_id = extract_definition_id_from_npc(npc_instance, npc_id, self.lifecycle_manager)

        self._update_population_stats_for_despawn(room_id, npc_type, is_required, definition_id)

        npc_name = getattr(npc_instance, "name", "Unknown")
        logger.info("Despawned NPC", npc_id=npc_id, npc_name=npc_name)
        return True

    def get_zone_population_summary(self) -> dict[str, Any]:
        """
        Get a summary of NPC populations across all zones.

        Returns:
            Dictionary containing population summaries
        """
        # Query active NPCs from lifecycle manager (single source of truth)
        active_npcs = self._get_active_npcs_from_lifecycle_manager()

        summary: dict[str, Any] = {
            "total_zones": len(self.population_stats),
            "total_active_npcs": len(active_npcs),
            "zones": {},
        }

        for zone_key, stats in self.population_stats.items():
            summary["zones"][zone_key] = stats.to_dict()

        return summary

    def clear_population_stats(self) -> None:
        """
        Clear all population statistics.

        This ensures a clean state when the server starts, as NPCs are ephemeral
        and should not persist across server restarts.
        Note: Active NPC instances are managed by NPCLifecycleManager, not this controller.
        """
        self.population_stats.clear()
        logger.info("Population stats cleared")

    def cleanup_inactive_npcs(self, max_age_seconds: int = 3600) -> int:
        """
        Clean up NPCs that have been inactive for too long.

        Args:
            max_age_seconds: Maximum age in seconds before cleanup

        Returns:
            Number of NPCs cleaned up
        """
        # Query active NPCs from lifecycle manager (single source of truth)
        active_npcs = self._get_active_npcs_from_lifecycle_manager()
        if not active_npcs:
            return 0

        current_time = time.time()
        npcs_to_remove = []

        for npc_id, npc_instance in active_npcs.items():
            # Get spawn time from NPC instance
            spawned_at_value = getattr(npc_instance, "spawned_at", None)
            # Ensure spawned_at is a number (handle Mock objects)
            if not spawned_at_value or not isinstance(spawned_at_value, int | float):
                continue

            age = current_time - spawned_at_value
            is_required_value = getattr(npc_instance, "is_required", None)
            is_required = bool(is_required_value) if is_required_value is not None else False
            if age > max_age_seconds and not is_required:
                npcs_to_remove.append(npc_id)

        for npc_id in npcs_to_remove:
            self.despawn_npc(npc_id)

        if npcs_to_remove:
            logger.info("Cleaned up inactive NPCs", count=len(npcs_to_remove))

        return len(npcs_to_remove)


__all__ = ["NPCPopulationController", "PopulationStats", "ZoneConfiguration"]
