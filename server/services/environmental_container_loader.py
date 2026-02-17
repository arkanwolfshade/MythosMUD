"""
Environmental container loader for unified container system.

As documented in the restricted archives of Miskatonic University, environmental
container loading requires careful orchestration to ensure proper migration
from JSON definitions to PostgreSQL and subsequent retrieval.
"""

from __future__ import annotations

import uuid
from typing import Any
from uuid import UUID

from ..exceptions import ValidationError
from ..models.container import ContainerComponent, ContainerLockState, ContainerSourceType
from ..structured_logging.enhanced_logging_config import get_logger

# Removed: from ..persistence import get_persistence - now using async_persistence parameter
from ..utils.error_logging import log_and_raise

logger = get_logger(__name__)


class EnvironmentalContainerLoader:
    """
    Service for loading environmental containers from JSON and PostgreSQL.

    Handles migration from room JSON definitions to PostgreSQL and
    retrieval of containers when loading rooms.
    """

    def __init__(self, persistence: Any | None = None) -> None:
        """
        Initialize the environmental container loader.

        Args:
            persistence: Persistence layer instance (optional, will get if not provided)
        """
        if persistence is None:
            raise ValueError("persistence (async_persistence) is required for EnvironmentalContainerLoader")
        self.persistence = persistence

    def load_container_from_room_json(self, room_json: dict[str, Any], room_id: str) -> ContainerComponent | None:
        """
        Load a container definition from room JSON.

        Args:
            room_json: Room JSON data dictionary
            room_id: Room ID (for validation)

        Returns:
            ContainerComponent if container is defined and enabled, None otherwise
        """
        container_block = room_json.get("container")
        if not container_block:
            return None

        # Check if container is enabled
        if not container_block.get("enabled", True):
            return None

        # Validate room_id matches
        if room_json.get("id") != room_id:
            logger.warning(
                "Room ID mismatch",
                json_room_id=room_json.get("id"),
                provided_room_id=room_id,
            )

        # Extract container configuration
        capacity_slots = container_block.get("capacity_slots", 20)
        lock_state_str = container_block.get("lock_state", "unlocked")
        weight_limit = container_block.get("weight_limit")
        allowed_roles = container_block.get("allowed_roles", [])
        key_item_id = container_block.get("key_item_id")

        # Validate capacity
        if not 1 <= capacity_slots <= 20:
            log_and_raise(
                ValidationError,
                f"Invalid capacity_slots: {capacity_slots}. Must be between 1 and 20",
                operation="load_environmental_container",
                capacity_slots=capacity_slots,
                room_id=room_id,
                details={"capacity_slots": capacity_slots, "room_id": room_id},
                user_friendly="Invalid container capacity",
            )

        # Validate lock state
        try:
            lock_state = ContainerLockState(lock_state_str)
        except ValueError:
            log_and_raise(
                ValidationError,
                f"Invalid lock_state: {lock_state_str}. Must be 'unlocked', 'locked', or 'sealed'",
                operation="load_environmental_container",
                lock_state=lock_state_str,
                room_id=room_id,
                details={"lock_state": lock_state_str, "room_id": room_id},
                user_friendly="Invalid container lock state",
            )

        # Build metadata
        metadata = {}
        if key_item_id:
            metadata["key_item_id"] = key_item_id

        # Create container component
        container = ContainerComponent(
            container_id=uuid.uuid4(),
            source_type=ContainerSourceType.ENVIRONMENT,
            room_id=room_id,
            capacity_slots=capacity_slots,
            lock_state=lock_state,
            weight_limit=weight_limit,
            allowed_roles=allowed_roles if isinstance(allowed_roles, list) else [],
            items=[],
            metadata=metadata,
        )

        logger.debug(
            "Container loaded from room JSON",
            room_id=room_id,
            container_id=str(container.container_id),
            capacity_slots=capacity_slots,
            lock_state=lock_state.value,
        )

        return container

    async def migrate_room_container_to_postgresql(self, room_json: dict[str, Any], room_id: str) -> UUID | None:
        """
        Migrate a container from room JSON to PostgreSQL.

        Checks if container already exists before creating.

        Args:
            room_json: Room JSON data dictionary
            room_id: Room ID

        Returns:
            UUID of the container if created/exists, None if no container defined
        """
        # Load container from JSON
        container = self.load_container_from_room_json(room_json, room_id)
        if not container:
            return None

        # Check if container already exists for this room (async)
        existing_containers = await self.persistence.get_containers_by_room_id(room_id)
        for existing in existing_containers:
            if existing.get("source_type") == "environment":
                # Container already exists, return its ID
                existing_id = existing.get("container_id")
                if existing_id:
                    logger.debug(
                        "Container already exists for room",
                        room_id=room_id,
                        container_id=existing_id,
                    )
                    return UUID(existing_id) if isinstance(existing_id, str) else existing_id

        # Create new container in PostgreSQL
        try:
            # Handle enum values - they may be strings due to use_enum_values=True
            source_type_value = (
                container.source_type.value if hasattr(container.source_type, "value") else str(container.source_type)
            )
            lock_state_value = (
                container.lock_state.value if hasattr(container.lock_state, "value") else str(container.lock_state)
            )
            container_data = await self.persistence.create_container(
                source_type=source_type_value,
                room_id=container.room_id,
                capacity_slots=container.capacity_slots,
                lock_state=lock_state_value,
                weight_limit=container.weight_limit,
                allowed_roles=container.allowed_roles,
                items_json=[],
                metadata_json=container.metadata,
            )

            container_id = UUID(container_data["container_id"])

            logger.info(
                "Container migrated to PostgreSQL",
                room_id=room_id,
                container_id=str(container_id),
            )

            return container_id

        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Container loading errors must be caught and converted to domain exceptions, all exceptions must be handled
            log_and_raise(
                ValidationError,
                f"Failed to migrate container to PostgreSQL: {str(e)}",
                operation="load_environmental_container",
                room_id=room_id,
                details={"room_id": room_id, "error": str(e)},
                user_friendly="Failed to create container",
            )

    async def load_containers_for_room(self, room_id: str) -> list[ContainerComponent]:
        """
        Load all environmental containers for a room from PostgreSQL.

        Args:
            room_id: Room ID

        Returns:
            list[ContainerComponent]: List of containers in the room
        """
        containers_data = await self.persistence.get_containers_by_room_id(room_id)
        if not containers_data:
            return []

        containers = []
        for container_data in containers_data:
            try:
                # Only load environmental containers
                if container_data.get("source_type") == "environment":
                    container = ContainerComponent.model_validate(container_data)
                    containers.append(container)
            except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Container loading errors must allow processing of other containers to continue, all exceptions must be caught to prevent batch failure
                logger.warning(
                    "Error loading container for room",
                    error=str(e),
                    room_id=room_id,
                    container_data=container_data,
                )
                continue

        logger.debug(
            "Containers loaded for room",
            room_id=room_id,
            container_count=len(containers),
        )

        return containers
