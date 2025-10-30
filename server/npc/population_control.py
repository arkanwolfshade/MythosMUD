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

import json
import random
import time
from pathlib import Path
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

    def add_npc(self, npc_type: str, room_id: str, is_required: bool, npc_definition_id: int = None) -> None:
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

    def remove_npc(self, npc_type: str, room_id: str, is_required: bool, npc_definition_id: int = None) -> None:
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
    Main controller for NPC population management across zones and sub-zones.

    This class manages NPC spawning, despawning, and population monitoring
    based on zone configurations, player counts, and game state conditions.
    """

    def __init__(
        self,
        event_bus: EventBus,
        spawning_service=None,
        lifecycle_manager=None,
        rooms_data_path: str = "data/local/rooms",
    ):
        """
        Initialize the NPC population controller.

        Args:
            event_bus: Event bus for publishing and subscribing to events
            spawning_service: Optional NPC spawning service for proper NPC creation
            lifecycle_manager: Optional NPC lifecycle manager for consistent ID generation
            rooms_data_path: Path to the rooms data directory
        """
        self.event_bus = event_bus
        self.spawning_service = spawning_service
        self.lifecycle_manager = lifecycle_manager
        self.rooms_data_path = Path(rooms_data_path)

        # Population tracking
        self.population_stats: dict[str, PopulationStats] = {}
        self.active_npcs: dict[str, dict[str, Any]] = {}  # npc_id -> npc_data
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
        """Load zone and sub-zone configurations from JSON files.

        The directory structure is: data/local/rooms/plane/zone/subzone/
        We need to traverse: plane -> zone -> subzone to find configurations.
        """
        try:
            # First level: plane directories (earth, yeng, etc.)
            for plane_dir in self.rooms_data_path.iterdir():
                if not plane_dir.is_dir():
                    continue

                logger.debug("Processing plane", plane_name=plane_dir.name)

                # Second level: zone directories (arkhamcity, innsmouth, katmandu, etc.)
                for zone_dir in plane_dir.iterdir():
                    if not zone_dir.is_dir():
                        continue

                    logger.debug("Processing zone", zone_name=zone_dir.name)

                    # Load zone configuration
                    zone_config_file = zone_dir / "zone_config.json"
                    if zone_config_file.exists():
                        with open(zone_config_file) as f:
                            zone_data = json.load(f)
                            zone_config = ZoneConfiguration(zone_data)
                            self.zone_configurations[zone_dir.name] = zone_config
                            logger.debug("Loaded zone config", zone_name=zone_dir.name)

                    # Third level: sub-zone directories (sanitarium, downtown, etc.)
                    for sub_zone_dir in zone_dir.iterdir():
                        if not sub_zone_dir.is_dir():
                            continue

                        sub_zone_config_file = sub_zone_dir / "subzone_config.json"
                        if sub_zone_config_file.exists():
                            with open(sub_zone_config_file) as f:
                                sub_zone_data = json.load(f)
                                sub_zone_config = ZoneConfiguration(sub_zone_data)
                                sub_zone_key = f"{zone_dir.name}/{sub_zone_dir.name}"
                                self.zone_configurations[sub_zone_key] = sub_zone_config
                                logger.debug("Loaded sub-zone config", sub_zone_key=sub_zone_key)

            logger.info(
                f"Loaded {len(self.zone_configurations)} zone configurations: {list(self.zone_configurations.keys())}"
            )

        except Exception as e:
            logger.error("Error loading zone configurations", error=str(e))

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
            f"NPC Population Controller received PlayerEnteredRoom event: player={event.player_id}, room={event.room_id}"
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
            self.npc_definitions[definition.id] = definition
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
            if rule.npc_definition_id not in self.spawn_rules:
                self.spawn_rules[rule.npc_definition_id] = []
            self.spawn_rules[rule.npc_definition_id].append(rule)
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
            zone_key: Zone key in format "zone/sub_zone"

        Returns:
            Zone configuration or None if not found
        """
        return self.zone_configurations.get(zone_key)

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
            logger.warning("No zone configuration found", zone_key=zone_key, room_id=room_id)
            return

        logger.info("Zone configuration found", zone_key=zone_key)

        # Check each NPC definition for spawn requirements
        logger.info("Checking NPC definitions for spawn requirements", npc_count=len(self.npc_definitions))
        for _npc_def_id, definition in self.npc_definitions.items():
            logger.info(
                "Checking NPC", npc_id=definition.id, npc_name=definition.name, sub_zone_id=definition.sub_zone_id
            )
            if definition.sub_zone_id not in zone_key:
                logger.info(
                    f"NPC {definition.id} sub_zone '{definition.sub_zone_id}' not in zone_key '{zone_key}', skipping"
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
            current_count = stats.npcs_by_definition.get(definition.id, 0)
            logger.info(
                "Current count for NPC in zone",
                npc_id=definition.id,
                npc_name=definition.name,
                current_count=current_count,
            )
            if not definition.can_spawn(current_count):
                logger.info(
                    f"NPC {definition.id} cannot spawn due to population limits (current: {current_count}, max: {definition.max_population})"
                )
                return False
        else:
            logger.info("No population stats found for zone", zone_key=zone_key)

        # Check spawn rules
        if definition.id in self.spawn_rules:
            logger.info(
                "Found spawn rules for NPC", rule_count=len(self.spawn_rules[definition.id]), npc_id=definition.id
            )
            # Get current NPC count for population checks
            current_npc_count = stats.npcs_by_definition.get(definition.id, 0) if stats else 0

            for i, rule in enumerate(self.spawn_rules[definition.id]):
                logger.info("Checking spawn rule", rule_number=i + 1, npc_id=definition.id)

                # Check if current NPC population is below the rule's max_population limit
                if not rule.can_spawn_with_population(current_npc_count):
                    logger.info(
                        f"Spawn rule {i + 1} failed population check (current NPCs: {current_npc_count}, max: {rule.max_population})"
                    )
                    continue

                logger.info("Spawn rule spawn conditions", rule_number=i + 1, spawn_conditions=rule.spawn_conditions)
                logger.info("Current game state", game_state=self.current_game_state)
                if not rule.check_spawn_conditions(self.current_game_state):
                    logger.info("Spawn rule failed spawn conditions check", rule_number=i + 1)
                    continue

                # Check spawn probability with zone modifier
                effective_probability = zone_config.get_effective_spawn_probability(definition.spawn_probability)
                random_roll = random.random()
                logger.info(
                    f"Spawn rule {i + 1} probability check: roll={random_roll:.3f}, threshold={effective_probability:.3f}"
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
                    current_count_by_definition=stats.npcs_by_definition.get(definition.id, 0),
                    max_population=definition.max_population,
                )

                stats.add_npc(definition.npc_type, room_id, definition.is_required(), definition.id)

                # Log population stats after adding NPC
                logger.debug(
                    "Population stats after adding NPC",
                    npc_id=npc_id,
                    npc_name=definition.name,
                    definition_id=definition.id,
                    zone_key=zone_key,
                    new_count_by_definition=stats.npcs_by_definition.get(definition.id, 0),
                    max_population=definition.max_population,
                )

                # Store NPC data for tracking
                self.active_npcs[npc_id] = {
                    "npc_type": definition.npc_type,
                    "room_id": room_id,
                    "is_required": definition.is_required(),
                    "spawned_at": time.time(),
                    "name": getattr(definition, "name", "Unknown NPC"),
                    "definition_id": definition.id,
                }

                # Use getattr to avoid potential lazy loading issues
                definition_name = getattr(definition, "name", "Unknown NPC")
                logger.info(
                    f"Spawned NPC: {npc_id} ({definition_name}, {definition.npc_type}) in {room_id} ({zone_key})"
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

        Args:
            npc_id: ID of the NPC to despawn

        Returns:
            True if NPC was despawned, False if not found
        """
        if npc_id not in self.active_npcs:
            logger.warning("Attempted to despawn non-existent NPC", npc_id=npc_id)
            return False

        npc_data = self.active_npcs[npc_id]
        room_id = npc_data["room_id"]

        # Update population statistics
        zone_key = self._get_zone_key_from_room_id(room_id)
        if zone_key in self.population_stats:
            stats = self.population_stats[zone_key]
            stats.remove_npc(npc_data["npc_type"], room_id, npc_data["is_required"], npc_data.get("definition_id"))

        # Remove from active NPCs
        del self.active_npcs[npc_id]

        logger.info("Despawned NPC", npc_id=npc_id, npc_name=npc_data["name"])
        return True

    def get_zone_population_summary(self) -> dict[str, Any]:
        """
        Get a summary of NPC populations across all zones.

        Returns:
            Dictionary containing population summaries
        """
        summary: dict[str, Any] = {"total_zones": len(self.population_stats), "total_active_npcs": len(self.active_npcs), "zones": {}}

        for zone_key, stats in self.population_stats.items():
            summary["zones"][zone_key] = stats.to_dict()

        return summary

    def clear_population_stats(self) -> None:
        """
        Clear all population statistics and active NPCs.

        This ensures a clean state when the server starts, as NPCs are ephemeral
        and should not persist across server restarts.
        """
        self.population_stats.clear()
        self.active_npcs.clear()
        logger.info("Population stats and active NPCs cleared")

    def cleanup_inactive_npcs(self, max_age_seconds: int = 3600) -> int:
        """
        Clean up NPCs that have been inactive for too long.

        Args:
            max_age_seconds: Maximum age in seconds before cleanup

        Returns:
            Number of NPCs cleaned up
        """
        current_time = time.time()
        npcs_to_remove = []

        for npc_id, npc_data in self.active_npcs.items():
            age = current_time - npc_data["spawned_at"]
            if age > max_age_seconds and not npc_data["is_required"]:
                npcs_to_remove.append(npc_id)

        for npc_id in npcs_to_remove:
            self.despawn_npc(npc_id)

        if npcs_to_remove:
            logger.info("Cleaned up inactive NPCs", count=len(npcs_to_remove))

        return len(npcs_to_remove)
