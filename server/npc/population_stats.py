"""
Population Statistics Module.

This module provides the PopulationStats class for tracking NPC population
statistics in zones and sub-zones.
"""

import time
from typing import Any


class PopulationStats:  # pylint: disable=too-many-instance-attributes  # Reason: Population stats requires many fields to capture complete population metrics
    """Statistics for NPC population in a zone or sub-zone."""

    def __init__(self, zone_id: str, sub_zone_id: str) -> None:
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
