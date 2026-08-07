"""
Container open/close session and mutation-token helpers.

Mixin host: ContainerService (persistence, mutation_guard, _open_containers).
"""

from __future__ import annotations

import uuid
from typing import cast
from uuid import UUID

from ..async_persistence import AsyncPersistenceLayer
from ..exceptions import ValidationError
from ..models.container import ContainerComponent, ContainerLockState
from ..models.player import Player
from ..structured_logging.enhanced_logging_config import get_logger
from ..utils.audit_logger import audit_logger
from ..utils.error_logging import log_and_raise
from .container_service_access import ContainerAccessMixin
from .container_service_helpers import (
    ContainerAccessDeniedError,
    ContainerLockedError,
    ContainerNotFoundError,
    ContainerServiceError,
    as_object_dict,
    filter_container_data,
    get_enum_value,
)

logger = get_logger(__name__)


class ContainerSessionMixin(ContainerAccessMixin):
    """Open/close sessions for containers."""

    # Host ContainerService rebinds this field on instances.
    # cast(object, None) only satisfies basedpyright reportUninitializedInstanceVariable
    # (same host-attr idea as ContainerAccessMixin._open_containers / ContainerLockMixin).
    persistence: AsyncPersistenceLayer = cast(AsyncPersistenceLayer, cast(object, None))

    def _raise_if_cannot_open_locks(
        self, container: ContainerComponent, player: Player, container_id: UUID, player_id: UUID
    ) -> None:
        """Sealed/locked gates for open_container (admin/key exceptions included)."""
        if container.lock_state == ContainerLockState.SEALED:
            if not player.is_admin:
                log_and_raise(
                    ContainerAccessDeniedError,
                    f"Container is sealed: {container_id}",
                    operation="open_container",
                    container_id=str(container_id),
                    player_id=str(player_id),
                    lock_state=get_enum_value(container.lock_state),
                    details={
                        "container_id": str(container_id),
                        "lock_state": get_enum_value(container.lock_state),
                    },
                    user_friendly="Container is sealed",
                )
        if container.is_locked() and not self._can_unlock_container(container, player):
            log_and_raise(
                ContainerLockedError,
                f"Container is locked: {container_id}",
                operation="open_container",
                container_id=str(container_id),
                player_id=str(player_id),
                lock_state=get_enum_value(container.lock_state),
                details={"container_id": str(container_id), "lock_state": get_enum_value(container.lock_state)},
                user_friendly="Container is locked",
            )

    def register_open_session(self, container_id: UUID, player_id: UUID, mutation_token: str | None = None) -> str:
        """Track open token; error if this player already has the container open."""
        if container_id in self._open_containers and player_id in self._open_containers[container_id]:
            log_and_raise(
                ContainerServiceError,
                f"Container already open: {container_id}",
                operation="open_container",
                container_id=str(container_id),
                player_id=str(player_id),
                details={"container_id": str(container_id), "player_id": str(player_id)},
                user_friendly="Container is already open",
            )
        token = mutation_token if mutation_token is not None else str(uuid.uuid4())
        if container_id not in self._open_containers:
            self._open_containers[container_id] = {}
        self._open_containers[container_id][player_id] = token
        return token

    def _audit_container_open(
        self, container: ContainerComponent, player: Player, container_id: UUID, player_id: UUID
    ) -> None:
        """Best-effort audit for container_open."""
        try:
            source_type_value = (
                container.source_type.value if hasattr(container.source_type, "value") else str(container.source_type)
            )
            audit_logger.log_container_interaction(
                player_id=str(player_id),
                player_name=str(player.name),
                container_id=str(container_id),
                event_type="container_open",
                source_type=source_type_value,
                room_id=container.room_id,
                success=True,
            )
        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Audit logging errors unpredictable, must not fail container operation
            logger.warning("Failed to log container open to audit log", error=str(e))

    async def open_container(self, container_id: UUID, player_id: UUID) -> dict[str, object]:
        """
        Open a container for interaction.

        Raises:
            ContainerNotFoundError: If container doesn't exist
            ContainerLockedError: If container is locked
            ContainerServiceError: If container is already open
        """
        logger.info("Opening container", container_id=str(container_id), player_id=str(player_id))
        raw_container = await self.persistence.get_container(container_id)
        if not raw_container:
            log_and_raise(
                ContainerNotFoundError,
                f"Container not found: {container_id}",
                operation="open_container",
                container_id=str(container_id),
                player_id=str(player_id),
                details={"container_id": str(container_id)},
                user_friendly="Container not found",
            )
        container = ContainerComponent.model_validate(filter_container_data(as_object_dict(raw_container)))
        player = await self.persistence.get_player_by_id(player_id)
        if not player:
            log_and_raise(
                ValidationError,
                f"Player not found: {player_id}",
                operation="open_container",
                container_id=str(container_id),
                player_id=str(player_id),
                details={"player_id": str(player_id)},
                user_friendly="Player not found",
            )
        self._validate_container_access(container, player)
        self._raise_if_cannot_open_locks(container, player, container_id, player_id)
        mutation_token = self.register_open_session(container_id, player_id)
        logger.info(
            "Container opened",
            container_id=str(container_id),
            player_id=str(player_id),
            mutation_token=mutation_token,
        )
        self._audit_container_open(container, player, container_id, player_id)
        return {
            "container": container.model_dump(),
            "mutation_token": mutation_token,
        }

    def _validate_container_close(self, container_id: UUID, player_id: UUID, mutation_token: str) -> None:
        """Validate that container is open and mutation token is valid."""
        if container_id not in self._open_containers:
            log_and_raise(
                ContainerServiceError,
                f"Container not open: {container_id}",
                operation="validate_container_close",
                container_id=str(container_id),
                player_id=str(player_id),
                details={"container_id": str(container_id)},
                user_friendly="Container is not open",
            )

        if player_id not in self._open_containers[container_id]:
            log_and_raise(
                ContainerServiceError,
                f"Container not open by player: {container_id}",
                operation="validate_container_close",
                container_id=str(container_id),
                player_id=str(player_id),
                details={"container_id": str(container_id), "player_id": str(player_id)},
                user_friendly="Container is not open",
            )

        stored_token = self._open_containers[container_id][player_id]
        if stored_token != mutation_token:
            log_and_raise(
                ContainerServiceError,
                f"Invalid mutation token: {container_id}",
                operation="validate_container_close",
                container_id=str(container_id),
                player_id=str(player_id),
                details={"container_id": str(container_id), "player_id": str(player_id)},
                user_friendly="Invalid mutation token",
            )

    def _remove_container_from_open_list(self, container_id: UUID, player_id: UUID) -> None:
        """Remove container from open containers dictionary."""
        del self._open_containers[container_id][player_id]
        if not self._open_containers[container_id]:
            del self._open_containers[container_id]

    async def _audit_log_container_close(self, container_id: UUID, player_id: UUID) -> None:
        """Log container close event to audit log."""
        try:
            raw_container = await self.persistence.get_container(container_id)
            player = await self.persistence.get_player_by_id(player_id)
            if raw_container and player:
                container = ContainerComponent.model_validate(filter_container_data(as_object_dict(raw_container)))
                source_type_value = get_enum_value(container.source_type)
                audit_logger.log_container_interaction(
                    player_id=str(player_id),
                    player_name=str(player.name),
                    container_id=str(container_id),
                    event_type="container_close",
                    source_type=source_type_value,
                    room_id=container.room_id,
                    success=True,
                )
        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Audit logging errors unpredictable, must not fail container operation
            logger.warning("Failed to log container close to audit log", error=str(e))

    async def close_container(self, container_id: UUID, player_id: UUID, mutation_token: str) -> None:
        """
        Close a container and release mutation guard.

        Args:
            container_id: Container UUID to close
            player_id: Player UUID closing the container
            mutation_token: Mutation token from open operation

        Raises:
            ContainerServiceError: If container is not open or token is invalid
        """
        logger.info("Closing container", container_id=str(container_id), player_id=str(player_id))

        # Validate container is open and token is valid
        self._validate_container_close(container_id, player_id, mutation_token)

        # Remove from open containers
        self._remove_container_from_open_list(container_id, player_id)

        logger.info("Container closed", container_id=str(container_id), player_id=str(player_id))

        # Audit log container close
        await self._audit_log_container_close(container_id, player_id)

    def get_container_token(self, container_id: UUID, player_id: UUID) -> str | None:
        """
        Get existing mutation token if container is already open by this player.

        Args:
            container_id: Container UUID
            player_id: Player UUID

        Returns:
            Mutation token string if container is open, None otherwise
        """
        if container_id in self._open_containers:
            return self._open_containers[container_id].get(player_id)
        return None
