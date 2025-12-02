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

import random
import time
from typing import Any

from server.events.event_bus import EventBus
from server.events.event_types import (
    NPCEnteredRoom,
    NPCLeftRoom,
    PlayerEnteredRoom,
    PlayerLeftRoom,
)
from server.models.npc import NPCDefinition, NPCSpawnRule

from ..logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)


class ZoneConfiguration:
    """Represents the configuration for a zone or sub-zone."""

    def __init__(self, config_data: dict[str, Any]):
        """
        Initialize zone configuration.

        Args:
            config_data: Dictionary containing zone configuration data
        """
        self.zone_type = config_data.get("zone_type")  # Only populated for zone-level configs
        self.environment = config_data.get("environment", "outdoors")
        self.description = config_data.get("description", "")
        self.weather_patterns = config_data.get("weather_patterns", [])
        self.special_rules = config_data.get("special_rules", {})

        # Extract NPC-related modifiers
        self.npc_spawn_modifier = self.special_rules.get("npc_spawn_modifier", 1.0)
        self.sanity_drain_rate = self.special_rules.get("sanity_drain_rate", 0.0)
        self.combat_modifier = self.special_rules.get("combat_modifier", 1.0)
        self.exploration_bonus = self.special_rules.get("exploration_bonus", 0.0)
        self.access_requirements = self.special_rules.get("access_requirements", [])

    def get_effective_spawn_probability(self, base_probability: float) -> float:
        """
        Calculate effective spawn probability based on zone modifiers.

        Args:
            base_probability: Base spawn probability from NPC definition

        Returns:
            Effective spawn probability adjusted for zone modifiers
        """
        return min(1.0, base_probability * self.npc_spawn_modifier)

    def can_access(self, player_requirements: list[str]) -> bool:
        """
        Check if a player can access this zone based on requirements.

        Args:
            player_requirements: List of player capabilities/items

        Returns:
            True if player can access the zone, False otherwise
        """
        if not self.access_requirements:
            return True

        return any(req in player_requirements for req in self.access_requirements)


class PopulationStats:
    """Statistics for NPC population in a zone or sub-zone."""

    def __init__(self, zone_id: str, sub_zone_id: str):
        """
        Initialize population statistics.

        Args:
            zone_id: The zone identifier
            sub_zone_id: The sub-zone identifier
        """
        self.zone_id = zone_id
        self.sub_zone_id = sub_zone_id
        self.total_npcs = 0
        self.npcs_by_type: dict[str, int] = {}
        self.npcs_by_definition: dict[int, int] = {}  # Track by individual NPC definition ID
        self.npcs_by_room: dict[str, int] = {}
        self.required_npcs = 0
        self.optional_npcs = 0
        self.last_updated = time.time()

    def add_npc(self, npc_type: str, room_id: str, is_required: bool, npc_definition_id: int | None = None) -> None:
        """
        Add an NPC to the population statistics.

        Args:
            npc_type: Type of the NPC
            room_id: Room where the NPC is located
            is_required: Whether the NPC is required
            npc_definition_id: The NPC definition ID for individual tracking
        """
        self.total_npcs += 1
        self.npcs_by_type[npc_type] = self.npcs_by_type.get(npc_type, 0) + 1
        self.npcs_by_room[room_id] = self.npcs_by_room.get(room_id, 0) + 1

        # Track by individual NPC definition ID
        if npc_definition_id is not None:
            self.npcs_by_definition[npc_definition_id] = self.npcs_by_definition.get(npc_definition_id, 0) + 1

        if is_required:
            self.required_npcs += 1
        else:
            self.optional_npcs += 1

        self.last_updated = time.time()

    def remove_npc(self, npc_type: str, room_id: str, is_required: bool, npc_definition_id: int | None = None) -> None:
        """
        Remove an NPC from the population statistics.

        Args:
            npc_type: Type of the NPC
            room_id: Room where the NPC was located
            is_required: Whether the NPC was required
            npc_definition_id: The NPC definition ID for individual tracking
        """
        self.total_npcs = max(0, self.total_npcs - 1)
        self.npcs_by_type[npc_type] = max(0, self.npcs_by_type.get(npc_type, 0) - 1)
        self.npcs_by_room[room_id] = max(0, self.npcs_by_room.get(room_id, 0) - 1)

        # Remove from individual NPC definition tracking
        if npc_definition_id is not None:
            self.npcs_by_definition[npc_definition_id] = max(0, self.npcs_by_definition.get(npc_definition_id, 0) - 1)

        if is_required:
            self.required_npcs = max(0, self.required_npcs - 1)
        else:
            self.optional_npcs = max(0, self.optional_npcs - 1)

        self.last_updated = time.time()

    def to_dict(self) -> dict[str, Any]:
        """Convert population statistics to dictionary."""
        return {
            "zone_id": self.zone_id,
            "sub_zone_id": self.sub_zone_id,
            "total_npcs": self.total_npcs,
            "npcs_by_type": self.npcs_by_type.copy(),
            "npcs_by_definition": self.npcs_by_definition.copy(),
            "npcs_by_room": self.npcs_by_room.copy(),
            "required_npcs": self.required_npcs,
            "optional_npcs": self.optional_npcs,
            "last_updated": self.last_updated,
        }


class NPCPopulationController:
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
        spawning_service=None,
        lifecycle_manager=None,
        async_persistence=None,
    ):
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
        import asyncio
        import threading

        result_container: dict[str, Any] = {"configs": {"zone": {}, "subzone": {}}, "error": None}

        def run_async():
            new_loop = asyncio.new_event_loop()
            asyncio.set_event_loop(new_loop)
            try:
                new_loop.run_until_complete(self._async_load_zone_configurations(result_container))
            finally:
                new_loop.close()

        thread = threading.Thread(target=run_async)
        thread.start()
        thread.join()

        error = result_container.get("error")
        if error is not None:
            logger.error(
                "Failed to load zone configs from database",
                error=str(error),
                error_type=type(error).__name__,
            )
            if isinstance(error, BaseException):
                raise RuntimeError("Failed to load zone configurations from database") from error
            raise RuntimeError(f"Failed to load zone configurations from database: {error}")

        # Note: The old code stored both zone and subzone configs in a single dict
        # For now, we'll merge them into zone_configurations for backward compatibility
        # TODO: Consider separating zone and subzone configs into separate attributes
        configs = result_container.get("configs")
        if configs is None or not isinstance(configs, dict):
            logger.error("Invalid configs in result_container", configs_type=type(configs).__name__)
            raise RuntimeError("Failed to load zone configurations: invalid configs structure")
        zone_configs = configs.get("zone", {})
        subzone_configs = configs.get("subzone", {})
        self.zone_configurations = {**zone_configs, **subzone_configs}
        logger.info(
            "Loaded zone configurations from PostgreSQL database",
            zone_count=len(zone_configs),
            subzone_count=len(subzone_configs),
            total_count=len(self.zone_configurations),
        )

    async def _async_load_zone_configurations(self, result_container: dict[str, Any]) -> None:
        """Async helper to load zone configurations from PostgreSQL database."""
        import os

        import asyncpg

        try:
            # Get database URL from environment
            database_url = os.getenv("DATABASE_URL")
            if not database_url:
                raise ValueError("DATABASE_URL environment variable not set")

            # Convert SQLAlchemy-style URL to asyncpg-compatible format
            if database_url.startswith("postgresql+asyncpg://"):
                database_url = database_url.replace("postgresql+asyncpg://", "postgresql://", 1)

            # Use asyncpg directly to avoid event loop conflicts
            conn = await asyncpg.connect(database_url)
            try:
                # Query zones (authoritative zone data)
                zone_query = """
                    SELECT
                        z.id,
                        z.stable_id as zone_stable_id,
                        z.zone_type,
                        z.environment,
                        z.description,
                        z.weather_patterns,
                        z.special_rules
                    FROM zones z
                    ORDER BY z.stable_id
                """
                zone_rows = await conn.fetch(zone_query)

                for row in zone_rows:
                    zone_stable_id = row["zone_stable_id"]
                    zone_type = row["zone_type"]
                    environment = row["environment"]
                    description = row["description"]
                    # asyncpg returns JSONB as dict/list, but ensure proper types
                    weather_patterns = row["weather_patterns"] if row["weather_patterns"] else []
                    if isinstance(weather_patterns, str):
                        import json

                        weather_patterns = json.loads(weather_patterns)

                    special_rules = row["special_rules"] if row["special_rules"] else {}
                    if isinstance(special_rules, str):
                        import json

                        special_rules = json.loads(special_rules)

                    # Extract zone name from stable_id (format: 'plane/zone')
                    zone_parts = zone_stable_id.split("/")
                    zone_name = zone_parts[1] if len(zone_parts) > 1 else zone_stable_id

                    # Build config data dictionary for zone
                    config_data = {
                        "zone_type": zone_type,
                        "environment": environment,
                        "description": description,
                        "weather_patterns": weather_patterns,
                        "special_rules": special_rules,
                    }

                    zone_config = ZoneConfiguration(config_data)
                    result_container["configs"]["zone"][zone_name] = zone_config

                # Query subzones (authoritative subzone data) with zone info via zone_configurations
                subzone_query = """
                    SELECT
                        sz.id,
                        z.stable_id as zone_stable_id,
                        sz.stable_id as subzone_stable_id,
                        sz.environment,
                        sz.description,
                        sz.special_rules,
                        z.zone_type,
                        z.weather_patterns
                    FROM subzones sz
                    JOIN zones z ON sz.zone_id = z.id
                    ORDER BY z.stable_id, sz.stable_id
                """
                subzone_rows = await conn.fetch(subzone_query)

                for row in subzone_rows:
                    zone_stable_id = row["zone_stable_id"]
                    subzone_stable_id = row["subzone_stable_id"]
                    environment = row["environment"]
                    description = row["description"]
                    # asyncpg returns JSONB as dict/list, but ensure proper types
                    special_rules = row["special_rules"] if row["special_rules"] else {}
                    if isinstance(special_rules, str):
                        import json

                        special_rules = json.loads(special_rules)

                    # Subzones inherit zone_type and weather_patterns from parent zone
                    zone_type = row["zone_type"]
                    weather_patterns = row["weather_patterns"] if row["weather_patterns"] else []
                    if isinstance(weather_patterns, str):
                        import json

                        weather_patterns = json.loads(weather_patterns)

                    # Extract zone name from stable_id (format: 'plane/zone')
                    zone_parts = zone_stable_id.split("/")
                    zone_name = zone_parts[1] if len(zone_parts) > 1 else zone_stable_id

                    # Build config data dictionary for subzone
                    config_data = {
                        "zone_type": zone_type,  # Inherited from zone
                        "environment": environment,
                        "description": description,
                        "weather_patterns": weather_patterns,  # Inherited from zone
                        "special_rules": special_rules,
                    }

                    zone_config = ZoneConfiguration(config_data)
                    subzone_key = f"{zone_name}/{subzone_stable_id}"
                    result_container["configs"]["subzone"][subzone_key] = zone_config
                    logger.debug(
                        "Loaded subzone configuration",
                        subzone_key=subzone_key,
                        zone_stable_id=zone_stable_id,
                        subzone_stable_id=subzone_stable_id,
                        zone_name=zone_name,
                    )
            finally:
                await conn.close()
        except Exception as e:
            result_container["error"] = e
            raise

    def _subscribe_to_events(self) -> None:
        """Subscribe to relevant game events."""
        logger.info("NPC Population Controller subscribing to game events")
        self.event_bus.subscribe(PlayerEnteredRoom, self._handle_player_entered_room)
        self.event_bus.subscribe(PlayerLeftRoom, self._handle_player_left_room)
        self.event_bus.subscribe(NPCEnteredRoom, self._handle_npc_entered_room)
        self.event_bus.subscribe(NPCLeftRoom, self._handle_npc_left_room)
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

    def _handle_player_left_room(self, event: PlayerLeftRoom) -> None:
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

    def _get_zone_key_from_room_id(self, room_id: str) -> str:
        """
        Extract zone key from room ID.

        Args:
            room_id: The room identifier

        Returns:
            Zone key in format "zone/sub_zone"
        """
        # Room IDs are in format: "plane_zone_sub_zone_[room_description]_number" or "plane_zone_sub_zone_[room_description]"
        # Examples: "earth_arkhamcity_downtown_001" -> "arkhamcity/downtown"
        #           "earth_arkhamcity_sanitarium_room_foyer_entrance_001" -> "arkhamcity/sanitarium"
        #           "earth_arkhamcity_downtown_intersection_derby_garrison" -> "arkhamcity/downtown"
        #           "earth_innsmouth_waterfront_dock_002" -> "innsmouth/waterfront"
        parts = room_id.split("_")
        if len(parts) >= 4:
            # We need exactly the zone (parts[1]) and sub_zone (parts[2])
            # Everything after parts[2] is room description (with or without numeric suffix)
            zone = parts[1]  # arkhamcity, innsmouth, katmandu
            sub_zone = parts[2]  # sanitarium, downtown, waterfront, etc.
            return f"{zone}/{sub_zone}"

        return "unknown/unknown"

    def _get_active_npcs_from_lifecycle_manager(self) -> dict[str, Any]:
        """
        Get active NPCs from the lifecycle manager (single source of truth).

        Returns:
            Dictionary mapping npc_id to NPC instance data, or empty dict if lifecycle_manager unavailable
        """
        if not self.lifecycle_manager or not hasattr(self.lifecycle_manager, "active_npcs"):
            return {}
        return self.lifecycle_manager.active_npcs

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

    def _check_spawn_requirements_for_room(self, room_id: str) -> None:
        """
        Check if NPCs need to be spawned for a specific room.

        Args:
            room_id: The room identifier
        """
        logger.info("Checking spawn requirements for room", room_id=room_id)
        zone_key = self._get_zone_key_from_room_id(room_id)
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
        logger.info("Evaluating spawn conditions for NPC", npc_id=definition.id, npc_name=definition.name)

        # Check population limits
        zone_key = self._get_zone_key_from_room_id(room_id)
        stats = self.get_population_stats(zone_key)
        if stats:
            # Check by individual NPC definition ID, not by type
            current_count = stats.npcs_by_definition.get(int(definition.id), 0)
            logger.info(
                "Current count for NPC in zone",
                npc_id=definition.id,
                npc_name=definition.name,
                current_count=current_count,
            )
            if not definition.can_spawn(current_count):
                logger.info(
                    "NPC cannot spawn due to population limits",
                    npc_id=definition.id,
                    current_count=current_count,
                    max_population=definition.max_population,
                )
                return False
        else:
            logger.info("No population stats found for zone", zone_key=zone_key)

        # Check spawn rules
        if int(definition.id) in self.spawn_rules:
            logger.info(
                "Found spawn rules for NPC", rule_count=len(self.spawn_rules[int(definition.id)]), npc_id=definition.id
            )
            # Get current NPC count for population checks
            current_npc_count = stats.npcs_by_definition.get(int(definition.id), 0) if stats else 0

            for i, rule in enumerate(self.spawn_rules[int(definition.id)]):
                logger.info("Checking spawn rule", rule_number=i + 1, npc_id=definition.id)

                # Check if current NPC population is below the rule's max_population limit
                if not rule.can_spawn_with_population(current_npc_count):
                    logger.info(
                        "Spawn rule failed population check",
                        rule_index=i + 1,
                        current_npc_count=current_npc_count,
                        max_population=rule.max_population,
                    )
                    continue

                logger.info("Spawn rule spawn conditions", rule_number=i + 1, spawn_conditions=rule.spawn_conditions)
                logger.info("Current game state", game_state=self.current_game_state)
                if not rule.check_spawn_conditions(self.current_game_state):
                    logger.info("Spawn rule failed spawn conditions check", rule_number=i + 1)
                    continue

                # Check spawn probability with zone modifier
                effective_probability = zone_config.get_effective_spawn_probability(float(definition.spawn_probability))
                random_roll = random.random()
                logger.info(
                    "Spawn rule probability check",
                    rule_index=i + 1,
                    roll=random_roll,
                    threshold=effective_probability,
                )
                if random_roll <= effective_probability:
                    logger.info("NPC should spawn based on spawn rule", npc_id=definition.id, rule_number=i + 1)
                    return True
                else:
                    logger.info("NPC failed probability roll for spawn rule", npc_id=definition.id, rule_number=i + 1)
        else:
            logger.info("No spawn rules found for NPC", npc_id=definition.id)

        # Required NPCs always spawn if conditions are met
        if definition.is_required():
            logger.info("NPC is required and conditions are met, spawning", npc_id=definition.id)
            return True

        logger.info("NPC should not spawn", npc_id=definition.id)
        return False

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
                zone_key = self._get_zone_key_from_room_id(room_id)
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
                return npc_id
            else:
                # Use getattr to avoid potential lazy loading issues
                definition_name = getattr(definition, "name", "Unknown NPC")
                logger.error("Failed to spawn NPC", npc_name=definition_name, room_id=room_id)
                return None

        except Exception as e:
            # Use getattr to avoid potential lazy loading issues
            definition_name = getattr(definition, "name", "Unknown NPC")
            logger.error("Error spawning NPC", npc_name=definition_name, error=str(e))
            return None

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
        # Query active NPCs from lifecycle manager (single source of truth)
        active_npcs = self._get_active_npcs_from_lifecycle_manager()
        if npc_id not in active_npcs:
            logger.warning("Attempted to despawn non-existent NPC", npc_id=npc_id)
            return False

        npc_instance = active_npcs[npc_id]
        # Get room_id from NPC instance
        # Handle Mock objects by ensuring we get a string value, not a Mock
        room_id_value = getattr(npc_instance, "current_room", None)
        if room_id_value is None:
            room_id_value = getattr(npc_instance, "current_room_id", None)
        if room_id_value is None:
            room_id_value = getattr(npc_instance, "room_id", None)

        # Ensure room_id is a string (handle Mock objects)
        if isinstance(room_id_value, str):
            room_id = room_id_value
        else:
            room_id = "unknown"

        # Get NPC metadata for population stats update
        npc_type_value = getattr(npc_instance, "npc_type", None)
        npc_type = npc_type_value if isinstance(npc_type_value, str) else "unknown"

        is_required_value = getattr(npc_instance, "is_required", None)
        is_required = bool(is_required_value) if is_required_value is not None else False

        # Try to get definition_id from NPC instance or lifecycle record
        definition_id: int | None = None
        if hasattr(npc_instance, "definition_id"):
            definition_id_value = npc_instance.definition_id
            if isinstance(definition_id_value, int):
                definition_id = definition_id_value
        elif self.lifecycle_manager and npc_id in getattr(self.lifecycle_manager, "lifecycle_records", {}):
            record = self.lifecycle_manager.lifecycle_records[npc_id]
            if hasattr(record, "definition") and hasattr(record.definition, "id"):
                definition_id = int(record.definition.id)

        # Update population statistics
        if room_id and room_id != "unknown":
            zone_key = self._get_zone_key_from_room_id(room_id)
            if zone_key in self.population_stats:
                stats = self.population_stats[zone_key]
                stats.remove_npc(npc_type, room_id, is_required, definition_id)

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
            if not spawned_at_value or not isinstance(spawned_at_value, (int, float)):
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
