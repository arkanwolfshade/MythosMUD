"""
Container lock and unlock operations.

Mixin host: ContainerService.
"""

from __future__ import annotations

from typing import cast
from uuid import UUID

from ..async_persistence import AsyncPersistenceLayer
from ..exceptions import ValidationError
from ..models.container import ContainerComponent, ContainerLockState, ContainerSourceType
from ..models.player import Player
from ..structured_logging.enhanced_logging_config import get_logger
from ..utils.error_logging import log_and_raise
from .container_service_access import ContainerAccessMixin
from .container_service_helpers import (
    ContainerAccessDeniedError,
    ContainerNotFoundError,
    ContainerServiceError,
    as_object_dict,
    filter_container_data,
)

logger = get_logger(__name__)


class ContainerLockMixin(ContainerAccessMixin):
    """Lock/unlock container state persistence."""

    # Host ContainerService rebinds this field on instances.
    # cast(object, None) only satisfies basedpyright reportUninitializedInstanceVariable
    # (same host-attr idea as ContainerAccessMixin._open_containers).
    persistence: AsyncPersistenceLayer = cast(AsyncPersistenceLayer, cast(object, None))

    async def _require_container_for_lock_ops(
        self, container_id: UUID, player_id: UUID, operation: str
    ) -> ContainerComponent:
        """Load container for lock/unlock ops, or raise ContainerNotFoundError."""
        raw_container = await self.persistence.get_container(container_id)
        if not raw_container:
            log_and_raise(
                ContainerNotFoundError,
                f"Container not found: {container_id}",
                operation=operation,
                container_id=str(container_id),
                player_id=str(player_id),
                details={"container_id": str(container_id)},
                user_friendly="Container not found",
            )
        return ContainerComponent.model_validate(filter_container_data(as_object_dict(raw_container)))

    async def _require_player_for_lock_ops(self, player_id: UUID, container_id: UUID, operation: str) -> Player:
        """Load player for lock/unlock ops, or raise ValidationError."""
        player = await self.persistence.get_player_by_id(player_id)
        if not player:
            log_and_raise(
                ValidationError,
                f"Player not found: {player_id}",
                operation=operation,
                container_id=str(container_id),
                player_id=str(player_id),
                details={"player_id": str(player_id)},
                user_friendly="Player not found",
            )
        return player

    def _raise_if_cannot_lock(
        self, container: ContainerComponent, player: Player, container_id: UUID, player_id: UUID
    ) -> None:
        """Require admin or ownership before locking (equipment entity or owner_id)."""
        if player.is_admin:
            return
        player_id_uuid = UUID(str(player.player_id))
        owns_equipment = (
            container.source_type == ContainerSourceType.EQUIPMENT and container.entity_id == player_id_uuid
        )
        owns_other = container.source_type != ContainerSourceType.EQUIPMENT and (
            not container.owner_id or container.owner_id == player_id_uuid
        )
        if owns_equipment or owns_other:
            return
        log_and_raise(
            ContainerAccessDeniedError,
            f"Player does not own container: {container_id}",
            operation="lock_container",
            container_id=str(container_id),
            player_id=str(player_id),
            details={"container_id": str(container_id), "player_id": str(player_id)},
            user_friendly="You do not own this container",
        )

    async def _persist_lock_state(
        self, container_id: UUID, player_id: UUID, lock_state_value: str, operation: str, failure_message: str
    ) -> dict[str, object]:
        """Persist container lock_state or raise ContainerServiceError."""
        updated = await self.persistence.update_container(container_id, lock_state=lock_state_value)
        if not updated:
            log_and_raise(
                ContainerServiceError,
                f"{failure_message}: {container_id}",
                operation=operation,
                container_id=str(container_id),
                player_id=str(player_id),
                details={"container_id": str(container_id)},
                user_friendly=failure_message,
            )
        return as_object_dict(updated)

    async def lock_container(
        self, container_id: UUID, player_id: UUID, lock_state: ContainerLockState
    ) -> dict[str, object]:
        """Lock a container (LOCKED or SEALED). Requires ownership or admin."""
        logger.info(
            "Locking container", container_id=str(container_id), player_id=str(player_id), lock_state=lock_state.value
        )
        container = await self._require_container_for_lock_ops(container_id, player_id, "lock_container")
        player = await self._require_player_for_lock_ops(player_id, container_id, "lock_container")
        self._raise_if_cannot_lock(container, player, container_id, player_id)
        result = await self._persist_lock_state(
            container_id, player_id, lock_state.value, "lock_container", "Failed to lock container"
        )
        logger.info(
            "Container locked", container_id=str(container_id), player_id=str(player_id), lock_state=lock_state.value
        )
        return result

    async def unlock_container(self, container_id: UUID, player_id: UUID) -> dict[str, object]:
        """Unlock a container. Requires access and unlock eligibility (key/admin)."""
        logger.info("Unlocking container", container_id=str(container_id), player_id=str(player_id))
        container = await self._require_container_for_lock_ops(container_id, player_id, "unlock_container")
        player = await self._require_player_for_lock_ops(player_id, container_id, "unlock_container")
        self._validate_container_access(container, player)
        if not self._can_unlock_container(container, player):
            log_and_raise(
                ContainerAccessDeniedError,
                f"Player cannot unlock container: {container_id}",
                operation="unlock_container",
                container_id=str(container_id),
                player_id=str(player_id),
                details={"container_id": str(container_id), "player_id": str(player_id)},
                user_friendly="You cannot unlock this container",
            )
        result = await self._persist_lock_state(
            container_id,
            player_id,
            ContainerLockState.UNLOCKED.value,
            "unlock_container",
            "Failed to unlock container",
        )
        logger.info("Container unlocked", container_id=str(container_id), player_id=str(player_id))
        return result
