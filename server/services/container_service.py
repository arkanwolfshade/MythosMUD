"""
Container service for unified container system operations.

As documented in the restricted archives of Miskatonic University, container
service operations require careful orchestration to ensure proper handling
of investigator artifacts, secure storage, and auditable interactions.

ASYNC MIGRATION (Phase 2):
All service methods made async to prevent event loop blocking.
Uses asyncio.to_thread() for synchronous persistence calls.

Implementation is split across mixins to keep each module under Lizard file-nloc.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from uuid import UUID

from ..async_persistence import AsyncPersistenceLayer
from ..utils.audit_logger import audit_logger
from .container_service_helpers import (
    ContainerAccessDeniedError,
    ContainerCapacityError,
    ContainerLockedError,
    ContainerNotFoundError,
    ContainerServiceError,
    filter_container_data,
    get_enum_value,
)
from .container_service_lock import ContainerLockMixin
from .container_service_session import ContainerSessionMixin
from .container_service_transfer_from import ContainerTransferFromMixin
from .inventory_mutation_guard import InventoryMutationGuard
from .inventory_service import InventoryService

# Public API re-exports (stable import path: server.services.container_service)
__all__ = [
    "ContainerService",
    "ContainerServiceError",
    "ContainerNotFoundError",
    "ContainerLockedError",
    "ContainerCapacityError",
    "ContainerAccessDeniedError",
    "audit_logger",
    "filter_container_data",
    "get_enum_value",
]


@dataclass
class ContainerService(
    ContainerSessionMixin,
    ContainerTransferFromMixin,
    ContainerLockMixin,
):
    """
    Service for managing container operations.

    Orchestrates open/close, transfer operations, and mutation guards
    for the unified container system.

    MRO note: TransferFromMixin inherits TransferToMixin and AccessMixin;
    SessionMixin inherits AccessMixin. Listing To/Access again breaks method order.
    """

    persistence: AsyncPersistenceLayer
    inventory_service: InventoryService = field(default_factory=lambda: InventoryService(max_slots=20))
    mutation_guard: InventoryMutationGuard = field(default_factory=InventoryMutationGuard)

    # Track open containers: {container_id: {player_id: mutation_token}}
    _open_containers: dict[UUID, dict[UUID, str]] = field(default_factory=dict, init=False)
