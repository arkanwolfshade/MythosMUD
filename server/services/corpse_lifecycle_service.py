"""
Corpse lifecycle service for unified container system.

As documented in the restricted archives of Miskatonic University, corpse
lifecycle automation requires careful orchestration to ensure proper handling
of player death, grace periods, decay timers, and item redistribution.
"""

from __future__ import annotations

import uuid
from datetime import UTC, datetime, timedelta
from typing import Any, cast
from uuid import UUID

from ..exceptions import MythosMUDError
from ..structured_logging.enhanced_logging_config import get_logger
from ..models.container import ContainerComponent, ContainerLockState, ContainerSourceType

# Removed: from ..persistence import get_persistence - now using async_persistence parameter
from ..utils.error_logging import create_error_context, log_and_raise

logger = get_logger(__name__)


def _get_enum_value(enum_or_str: Any) -> str:
    """
    Safely get enum value, handling both enum instances and string values.

    When containers are deserialized from the database, enum fields may be strings
    instead of enum instances. This helper handles both cases.

    Args:
        enum_or_str: Either an enum instance or a string value

    Returns:
        String value of the enum
    """
    if hasattr(enum_or_str, "value"):
        return enum_or_str.value
    return str(enum_or_str)


class CorpseServiceError(MythosMUDError):
    """Base exception for corpse service operations."""


class CorpseNotFoundError(CorpseServiceError):
    """Raised when a corpse container is not found."""


class CorpseLifecycleService:
    """
    Service for managing corpse container lifecycle.

    Handles creation on death, grace period enforcement, decay timers,
    and cleanup with item redistribution.
    """

    def __init__(
        self,
        persistence: Any | None = None,
        connection_manager: Any | None = None,
        time_service: Any | None = None,
    ):
        """
        Initialize the corpse lifecycle service.

        Args:
            persistence: Persistence layer instance (optional, will get if not provided)
            connection_manager: ConnectionManager instance for WebSocket events (optional)
            time_service: Time service instance for decay checks (optional)
        """
        if persistence is None:
            raise ValueError("persistence (async_persistence) is required for CorpseLifecycleService")
        self.persistence = persistence
        self.connection_manager = connection_manager
        self.time_service = time_service

    async def create_corpse_on_death(
        self,
        player_id: UUID,
        room_id: str,
        grace_period_seconds: int = 300,
        decay_hours: int = 1,
    ) -> ContainerComponent:
        """
        Create a corpse container when a player dies.

        Args:
            player_id: UUID of the dead player
            room_id: Room ID where the player died
            grace_period_seconds: Grace period duration in seconds (default: 300 = 5 minutes)
            decay_hours: Hours until corpse decays (default: 1)

        Returns:
            ContainerComponent: The created corpse container

        Raises:
            CorpseServiceError: If player not found or creation fails
        """
        context = create_error_context()
        context.metadata["operation"] = "create_corpse_on_death"
        context.metadata["player_id"] = str(player_id)
        context.metadata["room_id"] = room_id

        logger.info("Creating corpse container on death", player_id=str(player_id), room_id=room_id)

        # Get player
        player = await self.persistence.get_player_by_id(player_id)
        if not player:
            log_and_raise(
                CorpseServiceError,
                f"Player not found: {player_id}",
                context=context,
                details={"player_id": str(player_id)},
                user_friendly="Player not found",
            )

        # Get player inventory using the proper method that handles JSON string conversion
        player_inventory = player.get_inventory()
        player_name = getattr(player, "name", "Unknown")

        # Calculate timestamps
        now = datetime.now(UTC)
        decay_at = now + timedelta(hours=decay_hours)

        # Create corpse container
        corpse = ContainerComponent(
            container_id=uuid.uuid4(),
            source_type=ContainerSourceType.CORPSE,
            owner_id=player_id,
            room_id=room_id,
            capacity_slots=20,  # Corpses have standard capacity
            lock_state=ContainerLockState.UNLOCKED,
            decay_at=decay_at,
            items=player_inventory.copy(),  # Copy inventory to corpse
            metadata={
                "grace_period_seconds": grace_period_seconds,
                "grace_period_start": now.isoformat(),
                "player_name": player_name,
                "death_timestamp": now.isoformat(),
            },
        )

        # Persist corpse container
        try:
            # Convert InventoryStack objects to dicts for persistence
            items_dicts: list[dict[str, Any]] = [
                cast(dict[str, Any], dict(item) if not isinstance(item, dict) else item) for item in corpse.items
            ]
            container_data = await self.persistence.create_container(
                source_type=_get_enum_value(corpse.source_type),
                owner_id=corpse.owner_id,
                room_id=corpse.room_id,
                capacity_slots=corpse.capacity_slots,
                decay_at=corpse.decay_at,
                items_json=items_dicts,
                metadata_json=corpse.metadata,
            )
            corpse.container_id = UUID(container_data["container_id"])

            logger.info(
                "Corpse container created",
                container_id=str(corpse.container_id),
                player_id=str(player_id),
                room_id=room_id,
                items_count=len(corpse.items),
            )

            return corpse

        except Exception as e:
            log_and_raise(
                CorpseServiceError,
                f"Failed to create corpse container: {str(e)}",
                context=context,
                details={"player_id": str(player_id), "room_id": room_id},
                user_friendly="Failed to create corpse container",
            )

    def can_access_corpse(self, corpse: ContainerComponent, player_id: UUID, is_admin: bool = False) -> bool:
        """
        Check if a player can access a corpse container.

        During grace period, only the owner can access. After grace period,
        anyone can access.

        Args:
            corpse: Corpse container to check
            player_id: UUID of the player attempting access
            is_admin: Whether the player is an admin (admins can always access)

        Returns:
            bool: True if player can access, False otherwise
        """
        # Admins can always access
        if is_admin:
            return True

        # If no owner, anyone can access
        if not corpse.owner_id:
            return True

        # Owner can always access
        if corpse.owner_id == player_id:
            return True

        # Check grace period
        grace_period_seconds = corpse.metadata.get("grace_period_seconds", 300)
        grace_period_start_str = corpse.metadata.get("grace_period_start")

        if not grace_period_start_str:
            # No grace period set, anyone can access
            return True

        try:
            grace_period_start = datetime.fromisoformat(grace_period_start_str.replace("Z", "+00:00"))
            grace_period_end = grace_period_start + timedelta(seconds=grace_period_seconds)
            current_time = datetime.now(UTC)

            # If still in grace period, only owner can access
            if current_time < grace_period_end:
                return False

            # Grace period expired, anyone can access
            return True

        except (ValueError, TypeError) as e:
            logger.warning(
                "Error parsing grace period",
                error=str(e),
                container_id=str(corpse.container_id),
                grace_period_start=grace_period_start_str,
            )
            # On error, allow access (fail open)
            return True

    def is_corpse_decayed(self, corpse: ContainerComponent) -> bool:
        """
        Check if a corpse container has decayed.

        Args:
            corpse: Corpse container to check

        Returns:
            bool: True if decayed, False otherwise
        """
        if not corpse.decay_at:
            return False

        # Use time service if available, otherwise use system time
        if self.time_service:
            current_time = self.time_service.get_current_mythos_datetime()
        else:
            current_time = datetime.now(UTC)

        return current_time >= corpse.decay_at

    async def get_decayed_corpses_in_room(self, room_id: str) -> list[ContainerComponent]:
        """
        Get all decayed corpse containers in a room.

        Args:
            room_id: Room ID to check

        Returns:
            list[ContainerComponent]: List of decayed corpse containers
        """
        # Get all containers in room
        containers_data = await self.persistence.get_containers_by_room_id(room_id)
        if not containers_data:
            return []

        decayed = []
        for container_data in containers_data:
            try:
                container = ContainerComponent.model_validate(container_data)
                if container.source_type == ContainerSourceType.CORPSE and self.is_corpse_decayed(container):
                    decayed.append(container)
            except Exception as e:
                logger.warning(
                    "Error validating container for decay check",
                    error=str(e),
                    container_data=container_data,
                )
                continue

        return decayed

    async def cleanup_decayed_corpse(self, container_id: UUID) -> None:
        """
        Clean up a decayed corpse container.

        Deletes the container and emits decay event. Items are not redistributed
        in this method - they remain in the container until it's deleted.

        Args:
            container_id: UUID of the corpse container to clean up

        Raises:
            CorpseNotFoundError: If corpse doesn't exist
            CorpseServiceError: If cleanup fails
        """
        context = create_error_context()
        context.metadata["operation"] = "cleanup_decayed_corpse"
        context.metadata["container_id"] = str(container_id)

        logger.info("Cleaning up decayed corpse", container_id=str(container_id))

        # Get container
        container_data = await self.persistence.get_container(container_id)
        if not container_data:
            log_and_raise(
                CorpseNotFoundError,
                f"Corpse container not found: {container_id}",
                context=context,
                details={"container_id": str(container_id)},
                user_friendly="Corpse container not found",
            )

        container = ContainerComponent.model_validate(container_data)

        # Verify it's a corpse
        if container.source_type != ContainerSourceType.CORPSE:
            log_and_raise(
                CorpseServiceError,
                f"Container is not a corpse: {container_id}",
                context=context,
                details={"container_id": str(container_id), "source_type": _get_enum_value(container.source_type)},
                user_friendly="Container is not a corpse",
            )

        # Note: emit_container_decayed is async, but this method is sync
        # We'll handle event emission in the async cleanup task in lifespan.py

        # Delete container
        try:
            await self.persistence.delete_container(container_id)

            logger.info(
                "Decayed corpse cleaned up",
                container_id=str(container_id),
                room_id=container.room_id,
                items_count=len(container.items),
            )

        except Exception as e:
            log_and_raise(
                CorpseServiceError,
                f"Failed to delete decayed corpse: {str(e)}",
                context=context,
                details={"container_id": str(container_id)},
                user_friendly="Failed to clean up corpse",
            )

    async def cleanup_decayed_corpses_in_room(self, room_id: str) -> int:
        """
        Clean up all decayed corpse containers in a room.

        Args:
            room_id: Room ID to clean up

        Returns:
            int: Number of corpses cleaned up
        """
        logger.info("Cleaning up decayed corpses in room", room_id=room_id)

        decayed = await self.get_decayed_corpses_in_room(room_id)
        cleaned_count = 0

        for corpse in decayed:
            try:
                await self.cleanup_decayed_corpse(corpse.container_id)
                cleaned_count += 1
            except Exception as e:
                logger.error(
                    "Error cleaning up decayed corpse",
                    error=str(e),
                    container_id=str(corpse.container_id),
                    room_id=room_id,
                )
                continue

        logger.info(
            "Decayed corpses cleanup completed",
            room_id=room_id,
            cleaned_count=cleaned_count,
            total_decayed=len(decayed),
        )

        return cleaned_count

    async def get_all_decayed_corpses(self) -> list[ContainerComponent]:
        """
        Get all decayed corpse containers across all rooms.

        Returns:
            list[ContainerComponent]: List of all decayed corpse containers
        """
        # Use time service if available, otherwise use system time
        if self.time_service:
            current_time = self.time_service.get_current_mythos_datetime()
        else:
            current_time = datetime.now(UTC)

        # Get all decayed containers from persistence
        decayed_data = await self.persistence.get_decayed_containers(current_time)
        if not decayed_data:
            return []

        decayed_corpses = []
        for container_data in decayed_data:
            try:
                container = ContainerComponent.model_validate(container_data)
                if container.source_type == ContainerSourceType.CORPSE:
                    decayed_corpses.append(container)
            except Exception as e:
                logger.warning(
                    "Error validating decayed container",
                    error=str(e),
                    container_data=container_data,
                )
                continue

        return decayed_corpses

    async def cleanup_all_decayed_corpses(self) -> int:
        """
        Clean up all decayed corpse containers across all rooms.

        Returns:
            int: Number of corpses cleaned up
        """
        logger.info("Cleaning up all decayed corpses")

        decayed = await self.get_all_decayed_corpses()
        cleaned_count = 0

        for corpse in decayed:
            try:
                await self.cleanup_decayed_corpse(corpse.container_id)
                cleaned_count += 1
            except Exception as e:
                logger.error(
                    "Error cleaning up decayed corpse",
                    error=str(e),
                    container_id=str(corpse.container_id),
                )
                continue

        logger.info(
            "All decayed corpses cleanup completed",
            cleaned_count=cleaned_count,
            total_decayed=len(decayed),
        )

        return cleaned_count
