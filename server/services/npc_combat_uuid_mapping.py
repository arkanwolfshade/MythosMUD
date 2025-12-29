"""
NPC Combat UUID Mapping Management.

This module handles UUID-to-string ID and UUID-to-XP mappings for NPC combat,
enabling reverse lookups during XP calculation when NPCs may have been removed.
"""

from uuid import UUID, uuid4

from ..structured_logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)


class NPCCombatUUIDMapping:
    """Manages UUID mappings for NPC combat."""

    def __init__(self):
        """Initialize UUID mapping storage."""
        # UUID to string ID mapping for reverse lookup during XP calculation
        self._uuid_to_string_id_mapping: dict[UUID, str] = {}

        # UUID to XP value mapping for direct XP lookup
        self._uuid_to_xp_mapping: dict[UUID, int] = {}

    def is_valid_uuid(self, uuid_string: str) -> bool:
        """
        Check if a string is a valid UUID.

        Args:
            uuid_string: String to check

        Returns:
            True if valid UUID, False otherwise
        """
        try:
            UUID(uuid_string)
            return True
        except ValueError:
            return False

    def convert_to_uuid(self, entity_id: str) -> UUID:
        """
        Convert string ID to UUID, creating new UUID if needed.

        Args:
            entity_id: String ID or UUID string

        Returns:
            UUID for the entity
        """
        if self.is_valid_uuid(entity_id):
            return UUID(entity_id)
        return uuid4()

    def store_string_id_mapping(self, uuid_id: UUID, string_id: str) -> None:
        """
        Store UUID-to-string ID mapping.

        Args:
            uuid_id: UUID of the entity
            string_id: Original string ID
        """
        self._uuid_to_string_id_mapping[uuid_id] = string_id
        logger.debug(
            "Stored UUID-to-string ID mapping",
            uuid_id=uuid_id,
            string_id=string_id,
        )

    def store_xp_mapping(self, uuid_id: UUID, xp_value: int) -> None:
        """
        Store UUID-to-XP mapping.

        Args:
            uuid_id: UUID of the NPC
            xp_value: XP value for the NPC
        """
        self._uuid_to_xp_mapping[uuid_id] = xp_value
        logger.debug(
            "Stored UUID-to-XP mapping",
            uuid_id=uuid_id,
            xp_value=xp_value,
        )

    def get_original_string_id(self, uuid_id: UUID) -> str | None:
        """
        Get the original string ID from a UUID.

        Args:
            uuid_id: The UUID to look up

        Returns:
            The original string ID if found, None otherwise
        """
        result = self._uuid_to_string_id_mapping.get(uuid_id)
        logger.debug(
            "UUID to string ID lookup",
            uuid_id=uuid_id,
            result=result,
            mapping_size=len(self._uuid_to_string_id_mapping),
        )
        return result

    def get_xp_value(self, uuid_id: UUID) -> int | None:
        """
        Get XP value for a UUID.

        Args:
            uuid_id: The UUID to look up

        Returns:
            XP value if found, None otherwise
        """
        return self._uuid_to_xp_mapping.get(uuid_id)
