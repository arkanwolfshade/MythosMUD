"""
NPC occupant processing utilities.

This module handles querying and processing NPC occupants for rooms.

As documented in "Dimensional Occupancy Tracking" - Dr. Armitage, 1929
"""

from typing import Any

from sqlalchemy.exc import SQLAlchemyError

from ..structured_logging.enhanced_logging_config import get_logger
from .room_id_utils import RoomIDUtils


class NPCOccupantProcessor:
    """Processes NPC occupants for rooms."""

    def __init__(self, connection_manager: Any, room_id_utils: RoomIDUtils) -> None:
        """
        Initialize NPC occupant processor.

        Args:
            connection_manager: ConnectionManager instance
            room_id_utils: RoomIDUtils instance
        """
        self.connection_manager = connection_manager
        self.room_id_utils = room_id_utils
        self._logger = get_logger("NPCOccupantProcessor")

    def _get_npc_lifecycle_manager(self, room_id: str) -> Any | None:
        """
        Get and validate NPC lifecycle manager.

        Args:
            room_id: The room ID for logging

        Returns:
            Lifecycle manager instance or None if unavailable
        """
        from ..services.npc_instance_service import get_npc_instance_service

        npc_instance_service = get_npc_instance_service()
        if not npc_instance_service or not hasattr(npc_instance_service, "lifecycle_manager"):
            self._logger.warning(
                "NPC instance service not available",
                room_id=room_id,
                service_available=(npc_instance_service is not None),
                has_lifecycle_manager_attr=(
                    npc_instance_service is not None and hasattr(npc_instance_service, "lifecycle_manager")
                ),
            )
            return None

        lifecycle_manager = npc_instance_service.lifecycle_manager
        if not lifecycle_manager or not hasattr(lifecycle_manager, "active_npcs"):
            self._logger.warning(
                "Lifecycle manager or active_npcs not available",
                room_id=room_id,
                lifecycle_manager_available=(lifecycle_manager is not None),
                has_active_npcs_attr=(lifecycle_manager is not None and hasattr(lifecycle_manager, "active_npcs")),
            )
            return None

        return lifecycle_manager

    @staticmethod
    def _get_npc_room_id(npc_instance: Any) -> str | None:
        """
        Get NPC's current room ID from instance.

        Args:
            npc_instance: The NPC instance

        Returns:
            NPC room ID or None if not found
        """
        current_room = getattr(npc_instance, "current_room", None)
        current_room_id = getattr(npc_instance, "current_room_id", None)
        return current_room or current_room_id

    def _validate_npc_room_tracking(self, npc_id: str, npc_instance: Any, room_id: str) -> tuple[str | None, str]:
        """
        Validate NPC has room tracking and get room ID.

        Args:
            npc_id: The NPC ID
            npc_instance: The NPC instance
            room_id: Target room ID for logging

        Returns:
            Tuple of (npc_room_id, npc_name)
        """
        npc_room_id = self._get_npc_room_id(npc_instance)
        npc_name = getattr(npc_instance, "name", "Unknown")

        if not npc_room_id:
            current_room = getattr(npc_instance, "current_room", None)
            current_room_id = getattr(npc_instance, "current_room_id", None)
            self._logger.warning(
                "NPC instance missing room tracking",
                npc_id=npc_id,
                npc_name=npc_name,
                room_id=room_id,
                has_current_room=current_room is not None,
                has_current_room_id=current_room_id is not None,
            )

        return npc_room_id, npc_name

    def _should_include_npc_in_room(
        self, npc_id: str, npc_instance: Any, room_id: str, canonical_room_id: str
    ) -> tuple[bool, str | None]:
        """
        Determine if NPC should be included in room query results.

        Args:
            npc_id: The NPC ID
            npc_instance: The NPC instance
            room_id: Target room ID
            canonical_room_id: Target canonical room ID

        Returns:
            Tuple of (should_include, npc_room_id) where npc_room_id is None if NPC should be excluded
        """
        # Filter out dead NPCs
        if not getattr(npc_instance, "is_alive", True):
            self._logger.debug(
                "Skipping dead NPC from occupants",
                npc_id=npc_id,
                npc_name=getattr(npc_instance, "name", "unknown"),
                room_id=room_id,
            )
            return False, None

        # Validate NPC has room tracking
        npc_room_id, npc_name = self._validate_npc_room_tracking(npc_id, npc_instance, room_id)
        if not npc_room_id:
            return False, None

        # Get canonical room ID for NPC
        npc_canonical_room_id = self.room_id_utils.get_canonical_room_id(npc_room_id)

        # Check if NPC room matches target room
        room_matches = self.room_id_utils.check_npc_room_match(
            npc_room_id, npc_canonical_room_id, room_id, canonical_room_id
        )
        self._logger.debug(
            "Checking NPC for room match",
            room_id=room_id,
            canonical_room_id=canonical_room_id,
            npc_id=npc_id,
            npc_name=npc_name,
            npc_room_id=npc_room_id,
            npc_canonical_room_id=npc_canonical_room_id,
            matches_room=room_matches,
        )

        return room_matches, npc_room_id

    def _scan_active_npcs_for_room(
        self, active_npcs_dict: dict[str, Any], room_id: str, canonical_room_id: str
    ) -> list[str]:
        """
        Scan active NPCs to find those in the target room.

        Args:
            active_npcs_dict: Dictionary of active NPCs
            room_id: Target room ID
            canonical_room_id: Target canonical room ID

        Returns:
            List of NPC IDs in the room
        """
        npc_ids: list[str] = []
        npcs_checked = 0
        npcs_matched = 0
        npcs_without_room = 0

        # BUGFIX: Create snapshot of dict to prevent "dictionary changed size during iteration" errors
        for npc_id, npc_instance in list(active_npcs_dict.items()):
            npcs_checked += 1

            should_include, npc_room_id = self._should_include_npc_in_room(
                npc_id, npc_instance, room_id, canonical_room_id
            )

            if not should_include:
                if npc_room_id is None:
                    npcs_without_room += 1
                continue

            npc_ids.append(npc_id)
            npcs_matched += 1
            npc_name = getattr(npc_instance, "name", "Unknown")
            self._logger.info(
                "Found NPC in room",
                room_id=room_id,
                canonical_room_id=canonical_room_id,
                npc_id=npc_id,
                npc_name=npc_name,
            )

        self._logger.info(
            "Completed NPC query from lifecycle manager",
            room_id=room_id,
            canonical_room_id=canonical_room_id,
            npc_count=len(npc_ids),
            npcs_checked=npcs_checked,
            npcs_matched=npcs_matched,
            npcs_without_room=npcs_without_room,
            npc_ids=npc_ids[:5],
        )

        return npc_ids

    async def query_npcs_for_room(self, room_id: str, room: Any) -> list[str]:
        """
        Query NPCs for a room from lifecycle manager.

        Args:
            room_id: The room ID
            room: The room object (for fallback)

        Returns:
            List of NPC IDs in the room
        """
        try:
            canonical_room_id = self.room_id_utils.get_canonical_room_id(room_id)

            self._logger.info(
                "Querying NPCs from lifecycle manager",
                room_id=room_id,
                canonical_room_id=canonical_room_id,
                step="starting_npc_query",
            )

            lifecycle_manager = self._get_npc_lifecycle_manager(room_id)
            if not lifecycle_manager:
                return self._get_fallback_npcs(room_id, room)

            active_npcs_dict = lifecycle_manager.active_npcs
            total_active_npcs = len(active_npcs_dict)
            self._logger.info(
                "Scanning active NPCs for room match",
                room_id=room_id,
                canonical_room_id=canonical_room_id,
                total_active_npcs=total_active_npcs,
            )

            return self._scan_active_npcs_for_room(active_npcs_dict, room_id, canonical_room_id)

        except (ValueError, AttributeError, ImportError, SQLAlchemyError, TypeError) as npc_query_error:
            self._logger.error(
                "Error querying NPCs from lifecycle manager",
                room_id=room_id,
                error=str(npc_query_error),
                error_type=type(npc_query_error).__name__,
                exc_info=True,
            )
            return self._get_fallback_npcs(room_id, room)

    def _get_lifecycle_manager_for_filtering(self) -> Any | None:
        """
        Get lifecycle manager for filtering fallback NPCs.

        Returns:
            Lifecycle manager instance or None if unavailable
        """
        try:
            from ..services.npc_instance_service import get_npc_instance_service

            npc_instance_service = get_npc_instance_service()
            if not npc_instance_service or not hasattr(npc_instance_service, "lifecycle_manager"):
                return None

            lifecycle_manager = npc_instance_service.lifecycle_manager
            if not lifecycle_manager or not hasattr(lifecycle_manager, "active_npcs"):
                return None

            return lifecycle_manager
        except (ValueError, AttributeError, ImportError, SQLAlchemyError, TypeError):
            return None

    def _filter_single_fallback_npc(self, npc_id: str, lifecycle_manager: Any, room_id: str) -> bool:
        """
        Check if a single fallback NPC should be included.

        Args:
            npc_id: The NPC ID to check
            lifecycle_manager: Lifecycle manager instance
            room_id: The room ID for logging

        Returns:
            True if NPC should be included, False otherwise
        """
        if npc_id not in lifecycle_manager.active_npcs:
            return False

        npc_instance = lifecycle_manager.active_npcs[npc_id]
        if not getattr(npc_instance, "is_alive", True):
            self._logger.debug(
                "Filtered dead NPC from fallback occupants",
                npc_id=npc_id,
                room_id=room_id,
            )
            return False

        return True

    def _filter_fallback_npcs(self, room_npc_ids: list[str], room_id: str) -> list[str]:
        """
        Filter fallback NPCs to only include those in active_npcs and alive.

        Args:
            room_npc_ids: List of NPC IDs from room.get_npcs()
            room_id: The room ID for logging

        Returns:
            Filtered list of NPC IDs
        """
        lifecycle_manager = self._get_lifecycle_manager_for_filtering()
        if not lifecycle_manager:
            return room_npc_ids

        npc_ids = []
        try:
            for npc_id in room_npc_ids:
                if self._filter_single_fallback_npc(npc_id, lifecycle_manager, room_id):
                    npc_ids.append(npc_id)
        except (ValueError, AttributeError, ImportError, SQLAlchemyError, TypeError) as filter_error:
            self._logger.warning(
                "Error filtering fallback NPCs, using all room NPCs",
                room_id=room_id,
                error=str(filter_error),
            )
            return room_npc_ids

        return npc_ids

    def _get_fallback_npcs(self, room_id: str, room: Any) -> list[str]:
        """
        Get fallback NPCs from room.get_npcs() if lifecycle manager query fails.

        Args:
            room_id: The room ID
            room: The room object

        Returns:
            List of NPC IDs
        """
        room_npc_ids = room.get_npcs() if hasattr(room, "get_npcs") else []
        self._logger.warning(
            "Fell back to room.get_npcs() after lifecycle manager query failed",
            room_id=room_id,
            fallback_npc_count=len(room_npc_ids),
        )

        return self._filter_fallback_npcs(room_npc_ids, room_id)

    def process_npcs_for_occupants(self, npc_ids: list[str]) -> list[dict[str, Any]]:
        """
        Process NPC IDs and convert to occupant information.

        Args:
            npc_ids: List of NPC IDs

        Returns:
            List of NPC occupant information dictionaries
        """
        occupants: list[dict[str, Any]] = []

        # OPTIMIZATION: Batch load all NPC names at once to eliminate N+1 queries
        # Note: Using protected method for performance optimization - this is intentional
        npc_names = self.connection_manager._get_npcs_batch(list(npc_ids))  # noqa: SLF001  # pylint: disable=protected-access

        # Convert NPCs to occupant information using batch-loaded names
        for npc_id in npc_ids:
            npc_name = npc_names.get(npc_id, npc_id.split("_")[0].replace("_", " ").title())
            occupant_info = {
                "npc_id": npc_id,
                "npc_name": npc_name,
                "type": "npc",
            }
            occupants.append(occupant_info)

        return occupants
