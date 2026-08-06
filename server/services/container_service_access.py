"""
Container access validation (ownership, proximity, roles, corpse grace).

Mixin host: ContainerService.
"""

from __future__ import annotations

from datetime import UTC, datetime, timedelta
from typing import cast
from uuid import UUID

from ..models.container import ContainerComponent, ContainerLockState, ContainerSourceType
from ..structured_logging.enhanced_logging_config import get_logger
from ..utils.error_logging import log_and_raise
from .container_service_helpers import (
    ContainerAccessDeniedError,
    ContainerServiceError,
)

logger = get_logger(__name__)


class ContainerAccessMixin:  # pylint: disable=too-few-public-methods  # Reason: mixin of private access helpers for ContainerService
    """Access checks for open containers and unlock eligibility."""

    # Host ContainerService rebinds via field(default_factory=dict) on instances.
    # Empty default only satisfies basedpyright reportUninitializedInstanceVariable.
    _open_containers: dict[UUID, dict[UUID, str]] = {}

    def _verify_container_open(self, container_id: UUID, player_id: UUID, mutation_token: str) -> None:
        """
        Verify that a container is open by the specified player with the given token.

        Args:
            container_id: Container UUID
            player_id: Player UUID
            mutation_token: Mutation token

        Raises:
            ContainerServiceError: If container is not open or token is invalid
        """
        if container_id not in self._open_containers:
            raise ContainerServiceError(f"Container not open: {container_id}")

        if player_id not in self._open_containers[container_id]:
            raise ContainerServiceError(f"Container not open by player: {container_id}")

        stored_token = self._open_containers[container_id][player_id]
        if stored_token != mutation_token:
            raise ContainerServiceError(f"Invalid mutation token: {container_id}")

    def _validate_proximity(self, container: ContainerComponent, player: object, player_id: str) -> None:
        """Validate player is in same room as container for environment/corpse containers."""
        if container.source_type in (ContainerSourceType.ENVIRONMENT, ContainerSourceType.CORPSE):
            player_room_id = getattr(player, "current_room_id", None)
            if player_room_id != container.room_id:
                log_and_raise(
                    ContainerAccessDeniedError,
                    f"Player not in same room as container: {container.container_id}",
                    operation="validate_proximity",
                    container_id=str(container.container_id),
                    player_id=str(player_id),
                    container_room_id=container.room_id,
                    player_room_id=player_room_id,
                    details={
                        "container_id": str(container.container_id),
                        "player_id": str(player_id),
                        "container_room_id": container.room_id,
                        "player_room_id": player_room_id,
                    },
                    user_friendly="You must be in the same room as the container",
                )

    def _validate_ownership(self, container: ContainerComponent, player_id: str) -> None:
        """Validate player owns equipment container."""
        if container.source_type == ContainerSourceType.EQUIPMENT:
            player_id_uuid = UUID(str(player_id)) if player_id else None
            container_entity_id_uuid = UUID(str(container.entity_id)) if container.entity_id else None
            if container_entity_id_uuid != player_id_uuid:
                log_and_raise(
                    ContainerAccessDeniedError,
                    f"Player does not own equipment container: {container.container_id}",
                    operation="validate_ownership",
                    container_id=str(container.container_id),
                    player_id=str(player_id),
                    owner_id=str(container.entity_id),
                    details={
                        "container_id": str(container.container_id),
                        "player_id": str(player_id),
                        "owner_id": str(container.entity_id),
                    },
                    user_friendly="You do not own this container",
                )

    def _validate_role_access(self, container: ContainerComponent, player_id: str, is_admin: bool) -> None:
        """Validate player has required role for container access."""
        if container.allowed_roles and not is_admin:
            player_role = "admin" if is_admin else "player"
            if player_role not in container.allowed_roles:
                log_and_raise(
                    ContainerAccessDeniedError,
                    f"Player role not allowed: {container.container_id}",
                    operation="validate_role_access",
                    container_id=str(container.container_id),
                    player_id=str(player_id),
                    player_role=player_role,
                    allowed_roles=container.allowed_roles,
                    details={
                        "container_id": str(container.container_id),
                        "player_id": str(player_id),
                        "player_role": player_role,
                        "allowed_roles": container.allowed_roles,
                    },
                    user_friendly="You do not have permission to access this container",
                )

    @staticmethod
    def _raise_corpse_grace_denied(
        container: ContainerComponent,
        player_id: str,
        grace_period_end: str | None = None,
    ) -> None:
        """Deny non-owner corpse access during (or without) a timed grace period."""
        details: dict[str, object] = {
            "container_id": str(container.container_id),
            "player_id": str(player_id),
            "owner_id": str(container.owner_id),
        }
        if grace_period_end is not None:
            details["grace_period_end"] = grace_period_end
            log_and_raise(
                ContainerAccessDeniedError,
                f"Corpse grace period active: {container.container_id}",
                operation="validate_corpse_grace_period",
                container_id=str(container.container_id),
                player_id=str(player_id),
                owner_id=str(container.owner_id),
                grace_period_end=grace_period_end,
                details=details,
                user_friendly="The corpse's owner has exclusive access during the grace period",
            )
        log_and_raise(
            ContainerAccessDeniedError,
            f"Corpse grace period active: {container.container_id}",
            operation="validate_corpse_grace_period",
            container_id=str(container.container_id),
            player_id=str(player_id),
            owner_id=str(container.owner_id),
            details=details,
            user_friendly="The corpse's owner has exclusive access during the grace period",
        )

    def _validate_corpse_grace_period(self, container: ContainerComponent, player_id: str, is_admin: bool) -> None:
        """Validate corpse grace period access rules."""
        if container.source_type != ContainerSourceType.CORPSE or not container.owner_id:
            return
        if container.owner_id == player_id or is_admin:
            return

        metadata = cast(dict[str, object], container.metadata)
        grace_raw = metadata.get("grace_period_seconds", 300)
        grace_period_seconds = int(grace_raw) if isinstance(grace_raw, int | float | str) else 300
        grace_period_start_raw = metadata.get("grace_period_start")

        if not isinstance(grace_period_start_raw, str):
            self._raise_corpse_grace_denied(container, player_id)
            return

        grace_period_start = datetime.fromisoformat(grace_period_start_raw.replace("Z", "+00:00"))
        grace_period_end = grace_period_start + timedelta(seconds=grace_period_seconds)
        if datetime.now(UTC) >= grace_period_end:
            return
        self._raise_corpse_grace_denied(container, player_id, grace_period_end.isoformat())

    def _validate_container_access(self, container: ContainerComponent, player: object) -> None:
        """
        Validate that player has access to the container.

        Checks proximity, ownership, roles, and grace periods.

        Args:
            container: Container to check access for
            player: Player object (may be a real Player or a lightweight mock)

        Raises:
            ContainerAccessDeniedError: If access is denied
        """
        # getattr: command/API players expose player_id; older mocks may only set id.
        player_id = getattr(player, "player_id", None) or getattr(player, "id", None)
        is_admin = bool(getattr(player, "is_admin", False))

        self._validate_proximity(container, player, str(player_id))
        self._validate_ownership(container, str(player_id))
        self._validate_role_access(container, str(player_id), is_admin)
        self._validate_corpse_grace_period(container, str(player_id), is_admin)

    @staticmethod
    def _player_has_key_item(player: object, key_item_id: object) -> bool:
        """Return True if player inventory contains the required key item_id."""
        # Prefer inventory attribute (mocks/tests); fall back to Player.get_inventory.
        player_inventory_raw: object = getattr(player, "inventory", None)
        if player_inventory_raw is None:
            get_inventory = getattr(player, "get_inventory", None)
            player_inventory_raw = get_inventory() if callable(get_inventory) else []
        if not isinstance(player_inventory_raw, list):
            return False
        # list alone is list[Unknown] under basedpyright; cast elements to object.
        player_inventory = cast(list[object], player_inventory_raw)
        for item in player_inventory:
            if cast(dict[str, object], item).get("item_id") == key_item_id:
                return True
        return False

    def _can_unlock_container(self, container: ContainerComponent, player: object) -> bool:
        """
        Check if player can unlock the container.

        Args:
            container: Container to check
            player: Player object (may be a real Player or a lightweight mock)

        Returns:
            bool: True if player can unlock, False otherwise
        """
        # Admins can always unlock
        if getattr(player, "is_admin", False):
            return True

        # Sealed containers cannot be unlocked by non-admins
        if container.lock_state == ContainerLockState.SEALED:
            return False

        # Check if container requires a key
        metadata = cast(dict[str, object], container.metadata)
        key_item_id = metadata.get("key_item_id")
        if key_item_id is not None:
            return self._player_has_key_item(player, key_item_id)

        # Locked containers without a key requirement still require admin to unlock
        # If no key is specified, only admins can unlock locked containers
        if container.lock_state == ContainerLockState.LOCKED:
            return False

        # Unlocked containers can be opened
        return container.lock_state == ContainerLockState.UNLOCKED
