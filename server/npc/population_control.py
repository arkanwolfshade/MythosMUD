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

from ..logging_config import get_logger

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
        self.npcs_by_room: dict[str, int] = {}
        self.required_npcs = 0
        self.optional_npcs = 0
        self.last_updated = time.time()

    def add_npc(self, npc_type: str, room_id: str, is_required: bool) -> None:
        """
        Add an NPC to the population statistics.

        Args:
            npc_type: Type of the NPC
            room_id: Room where the NPC is located
            is_required: Whether the NPC is required
        """
        self.total_npcs += 1
        self.npcs_by_type[npc_type] = self.npcs_by_type.get(npc_type, 0) + 1
        self.npcs_by_room[room_id] = self.npcs_by_room.get(room_id, 0) + 1

        if is_required:
            self.required_npcs += 1
        else:
            self.optional_npcs += 1

        self.last_updated = time.time()

    def remove_npc(self, npc_type: str, room_id: str, is_required: bool) -> None:
        """
        Remove an NPC from the population statistics.

        Args:
            npc_type: Type of the NPC
            room_id: Room where the NPC was located
            is_required: Whether the NPC was required
        """
        self.total_npcs = max(0, self.total_npcs - 1)
        self.npcs_by_type[npc_type] = max(0, self.npcs_by_type.get(npc_type, 0) - 1)
        self.npcs_by_room[room_id] = max(0, self.npcs_by_room.get(room_id, 0) - 1)

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

    def __init__(self, event_bus: EventBus, rooms_data_path: str = "data/rooms"):
        """
        Initialize the NPC population controller.

        Args:
            event_bus: Event bus for publishing and subscribing to events
            rooms_data_path: Path to the rooms data directory
        """
        self.event_bus = event_bus
        self.rooms_data_path = Path(rooms_data_path)

        # Population tracking
        self.population_stats: dict[str, PopulationStats] = {}
        self.active_npcs: dict[str, dict[str, Any]] = {}  # npc_id -> npc_data
        self.zone_configurations: dict[str, ZoneConfiguration] = {}

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

        logger.info(f"NPC Population Controller initialized with {len(self.zone_configurations)} zones loaded")

    def _load_zone_configurations(self) -> None:
        """Load zone and sub-zone configurations from JSON files."""
        try:
            for zone_dir in self.rooms_data_path.iterdir():
                if not zone_dir.is_dir():
                    continue

                # Load zone configuration
                zone_config_file = zone_dir / "zone_config.json"
                if zone_config_file.exists():
                    with open(zone_config_file) as f:
                        zone_data = json.load(f)
                        zone_config = ZoneConfiguration(zone_data)
                        self.zone_configurations[zone_dir.name] = zone_config

                # Load sub-zone configurations
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

        except Exception as e:
            logger.error(f"Error loading zone configurations: {str(e)}")

    def _subscribe_to_events(self) -> None:
        """Subscribe to relevant game events."""
        self.event_bus.subscribe(PlayerEnteredRoom, self._handle_player_entered_room)
        self.event_bus.subscribe(PlayerLeftRoom, self._handle_player_left_room)
        self.event_bus.subscribe(NPCEnteredRoom, self._handle_npc_entered_room)
        self.event_bus.subscribe(NPCLeftRoom, self._handle_npc_left_room)

    def _handle_player_entered_room(self, event: PlayerEnteredRoom) -> None:
        """Handle player entering a room."""
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
        # Update population statistics
        if event.npc_id in self.active_npcs:
            npc_data = self.active_npcs[event.npc_id]
            zone_key = self._get_zone_key_from_room_id(event.room_id)
            if zone_key in self.population_stats:
                stats = self.population_stats[zone_key]
                stats.add_npc(npc_data.get("npc_type", "unknown"), event.room_id, npc_data.get("is_required", False))

    def _handle_npc_left_room(self, event: NPCLeftRoom) -> None:
        """Handle NPC leaving a room."""
        # Update population statistics
        if event.npc_id in self.active_npcs:
            npc_data = self.active_npcs[event.npc_id]
            zone_key = self._get_zone_key_from_room_id(event.room_id)
            if zone_key in self.population_stats:
                stats = self.population_stats[zone_key]
                stats.remove_npc(npc_data.get("npc_type", "unknown"), event.room_id, npc_data.get("is_required", False))

    def _get_zone_key_from_room_id(self, room_id: str) -> str:
        """
        Extract zone key from room ID.

        Args:
            room_id: The room identifier

        Returns:
            Zone key in format "zone/sub_zone"
        """
        # Room IDs are typically in format: "plane_zone_sub_zone_room_number"
        # Examples: "earth_arkhamcity_downtown_001" -> "arkhamcity/downtown"
        #           "earth_innsmouth_waterfront_002" -> "innsmouth/waterfront"
        parts = room_id.split("_")
        if len(parts) >= 4:
            # Find the last part that looks like a room number (numeric)
            room_number_idx = -1
            for i in range(len(parts) - 1, 0, -1):
                if parts[i].isdigit():
                    room_number_idx = i
                    break

            if room_number_idx >= 3:
                # Everything between parts[1] and room_number_idx-1 is zone/sub_zone
                zone_parts = parts[1:room_number_idx]
                if len(zone_parts) >= 2:
                    # Last part is sub_zone, everything before is zone
                    zone = "_".join(zone_parts[:-1])
                    sub_zone = zone_parts[-1]
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
            logger.debug(f"Loaded NPC definition: {definition.id} - {definition.name} ({definition.npc_type})")

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
            logger.debug(f"Loaded spawn rule: {rule.id} for NPC {rule.npc_definition_id} in {rule.sub_zone_id}")

    def update_game_state(self, new_state: dict[str, Any]) -> None:
        """
        Update the current game state.

        Args:
            new_state: Dictionary containing new game state values
        """
        self.current_game_state.update(new_state)
        logger.debug(f"Updated game state: {new_state}")

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
        zone_key = self._get_zone_key_from_room_id(room_id)
        zone_config = self.get_zone_configuration(zone_key)

        if not zone_config:
            logger.warning(f"No zone configuration found for {zone_key} (room: {room_id})")
            return

        # Check each NPC definition for spawn requirements
        for _npc_def_id, definition in self.npc_definitions.items():
            if definition.sub_zone_id not in zone_key:
                continue

            # Check if this NPC should spawn
            if self._should_spawn_npc(definition, zone_config, room_id):
                self._spawn_npc(definition, room_id)

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
        # Check population limits
        zone_key = self._get_zone_key_from_room_id(room_id)
        stats = self.get_population_stats(zone_key)
        if stats:
            current_count = stats.npcs_by_type.get(definition.npc_type, 0)
            if not definition.can_spawn(current_count):
                return False

        # Check spawn rules
        if definition.id in self.spawn_rules:
            for rule in self.spawn_rules[definition.id]:
                if not rule.can_spawn_for_player_count(self.current_game_state["player_count"]):
                    continue

                if not rule.check_spawn_conditions(self.current_game_state):
                    continue

                # Check spawn probability with zone modifier
                effective_probability = zone_config.get_effective_spawn_probability(definition.spawn_probability)
                if random.random() <= effective_probability:
                    return True

        # Required NPCs always spawn if conditions are met
        if definition.is_required():
            return True

        return False

    def _spawn_npc(self, definition: NPCDefinition, room_id: str) -> str:
        """
        Spawn an NPC instance.

        Args:
            definition: NPC definition
            room_id: Room where to spawn the NPC

        Returns:
            Generated NPC instance ID
        """
        npc_id = f"{definition.name.lower().replace(' ', '_')}_{int(time.time())}"

        # Create NPC instance data
        npc_data = {
            "npc_id": npc_id,
            "definition_id": definition.id,
            "npc_type": definition.npc_type,
            "name": definition.name,
            "room_id": room_id,
            "is_required": definition.is_required(),
            "spawned_at": time.time(),
            "stats": definition.get_base_stats(),
            "behavior_config": definition.get_behavior_config(),
            "ai_config": definition.get_ai_integration_stub(),
        }

        # Store active NPC
        self.active_npcs[npc_id] = npc_data

        # Update population statistics
        zone_key = self._get_zone_key_from_room_id(room_id)
        if zone_key not in self.population_stats:
            zone_parts = zone_key.split("/")
            self.population_stats[zone_key] = PopulationStats(zone_parts[0], zone_parts[1])

        stats = self.population_stats[zone_key]
        stats.add_npc(definition.npc_type, room_id, definition.is_required())

        logger.info(f"Spawned NPC: {npc_id} ({definition.name}, {definition.npc_type}) in {room_id} ({zone_key})")

        return npc_id

    def despawn_npc(self, npc_id: str) -> bool:
        """
        Despawn an NPC instance.

        Args:
            npc_id: ID of the NPC to despawn

        Returns:
            True if NPC was despawned, False if not found
        """
        if npc_id not in self.active_npcs:
            logger.warning(f"Attempted to despawn non-existent NPC: {npc_id}")
            return False

        npc_data = self.active_npcs[npc_id]
        room_id = npc_data["room_id"]

        # Update population statistics
        zone_key = self._get_zone_key_from_room_id(room_id)
        if zone_key in self.population_stats:
            stats = self.population_stats[zone_key]
            stats.remove_npc(npc_data["npc_type"], room_id, npc_data["is_required"])

        # Remove from active NPCs
        del self.active_npcs[npc_id]

        logger.info(f"Despawned NPC: {npc_id} ({npc_data['name']})")
        return True

    def get_zone_population_summary(self) -> dict[str, Any]:
        """
        Get a summary of NPC populations across all zones.

        Returns:
            Dictionary containing population summaries
        """
        summary = {"total_zones": len(self.population_stats), "total_active_npcs": len(self.active_npcs), "zones": {}}

        for zone_key, stats in self.population_stats.items():
            summary["zones"][zone_key] = stats.to_dict()

        return summary

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
            logger.info(f"Cleaned up {len(npcs_to_remove)} inactive NPCs")

        return len(npcs_to_remove)
