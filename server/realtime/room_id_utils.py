"""
Room ID normalization and comparison utilities.

This module provides utilities for normalizing and comparing room IDs,
ensuring consistent room matching across the system.

As documented in "Dimensional Occupancy Tracking" - Dr. Armitage, 1929
"""

from typing import Any


class RoomIDUtils:
    """Utilities for room ID normalization and comparison."""

    def __init__(self, connection_manager: Any) -> None:
        """
        Initialize room ID utilities.

        Args:
            connection_manager: ConnectionManager instance
        """
        self.connection_manager = connection_manager

    def get_canonical_room_id(self, room_id: str) -> str:
        """
        Get canonical room ID for consistent comparison.

        Args:
            room_id: The room ID

        Returns:
            Canonical room ID
        """
        if self.connection_manager and hasattr(self.connection_manager, "canonical_room_id"):
            return self.connection_manager.canonical_room_id(room_id) or room_id
        return room_id

    @staticmethod
    def normalize_room_id_for_comparison(rid: str | None) -> str | None:
        """
        Normalize room ID for comparison.

        Args:
            rid: Room ID to normalize

        Returns:
            Normalized room ID string or None
        """
        if rid is None:
            return None
        # Convert to string and strip whitespace
        rid_str = str(rid).strip()
        # Return empty string as None for consistency
        return rid_str if rid_str else None

    @staticmethod
    def check_normalized_ids_match(id1: str | None, id2: str | None) -> bool:
        """
        Check if two normalized room IDs match.

        Args:
            id1: First normalized room ID
            id2: Second normalized room ID

        Returns:
            True if both IDs are not None and match, False otherwise
        """
        if id1 is None or id2 is None:
            return False
        return id1 == id2

    @staticmethod
    def check_normalized_room_matches(
        normalized_npc_room_id: str | None,
        normalized_npc_canonical_room_id: str | None,
        normalized_room_id: str | None,
        normalized_canonical_room_id: str | None,
    ) -> bool:
        """
        Check if normalized NPC room IDs match normalized target room IDs.

        Args:
            normalized_npc_room_id: Normalized NPC current room ID
            normalized_npc_canonical_room_id: Normalized NPC canonical room ID
            normalized_room_id: Normalized target room ID
            normalized_canonical_room_id: Normalized target canonical room ID

        Returns:
            True if any normalized IDs match, False otherwise
        """
        return (
            RoomIDUtils.check_normalized_ids_match(normalized_npc_room_id, normalized_room_id)
            or RoomIDUtils.check_normalized_ids_match(normalized_npc_room_id, normalized_canonical_room_id)
            or RoomIDUtils.check_normalized_ids_match(normalized_npc_canonical_room_id, normalized_room_id)
            or RoomIDUtils.check_normalized_ids_match(normalized_npc_canonical_room_id, normalized_canonical_room_id)
        )

    @staticmethod
    def check_fallback_room_matches(
        npc_room_id: str, npc_canonical_room_id: str | None, room_id: str, canonical_room_id: str
    ) -> bool:
        """
        Check if NPC room IDs match target room IDs using fallback comparison.

        Args:
            npc_room_id: NPC's current room ID
            npc_canonical_room_id: NPC's canonical room ID
            room_id: Target room ID
            canonical_room_id: Target canonical room ID

        Returns:
            True if any fallback IDs match, False otherwise
        """
        # Check direct matches first
        if npc_room_id in (room_id, canonical_room_id):
            return True

        # Check canonical room ID matches if available
        if npc_canonical_room_id is not None:
            return npc_canonical_room_id in (room_id, canonical_room_id)

        return False

    def check_npc_room_match(
        self, npc_room_id: str, npc_canonical_room_id: str | None, room_id: str, canonical_room_id: str
    ) -> bool:
        """
        Check if NPC room matches target room using normalized comparison.

        Args:
            npc_room_id: NPC's current room ID
            npc_canonical_room_id: NPC's canonical room ID
            room_id: Target room ID
            canonical_room_id: Target canonical room ID

        Returns:
            True if rooms match, False otherwise
        """
        # Normalize all room IDs for comparison
        normalized_room_id = self.normalize_room_id_for_comparison(room_id)
        normalized_canonical_room_id = self.normalize_room_id_for_comparison(canonical_room_id)
        normalized_npc_room_id = self.normalize_room_id_for_comparison(npc_room_id)
        normalized_npc_canonical_room_id = self.normalize_room_id_for_comparison(npc_canonical_room_id)

        # Check normalized matches first (preferred method)
        if self.check_normalized_room_matches(
            normalized_npc_room_id, normalized_npc_canonical_room_id, normalized_room_id, normalized_canonical_room_id
        ):
            return True

        # Fallback to original comparison for backward compatibility
        return self.check_fallback_room_matches(npc_room_id, npc_canonical_room_id, room_id, canonical_room_id)
