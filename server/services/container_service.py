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
from typing import cast
from uuid import UUID

from ..async_persistence import AsyncPersistenceLayer
from ..utils.audit_logger import audit_logger
from .container_service_helpers import (
    ContainerAccessDeniedError,
    ContainerCapacityError,
    ContainerLockedError,
    ContainerNotFoundError,
    ContainerOpenByAnotherPlayerError,
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
    "ContainerOpenByAnotherPlayerError",
    "audit_logger",
    "filter_container_data",
    "get_container_service",
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


_container_service_cache: dict[int, ContainerService] = {}


def get_container_service(persistence: object) -> ContainerService:
    """
    Get the ContainerService for this persistence layer, reusing one across calls.

    ContainerService tracks open-container sessions and mutation tokens in an
    instance-level dict (see ContainerService._open_containers). A fresh instance per
    call -- which this used to construct unconditionally -- gives every HTTP request
    (and every text command) its own empty session store, so an open() from one
    request is invisible to the transfer()/close() of the next: the whole exclusivity
    and idempotent-reopen contract silently never worked outside a single call. Caching
    by persistence identity fixes that for the real server (one long-lived persistence
    singleton -> one shared ContainerService) while keeping unit tests isolated (each
    test's own mock persistence gets its own service).

    Lives in the service layer (re-exported by server.api.container_helpers) so realtime
    disconnect cleanup can release a departing player's sessions on the same instance (#964).
    """
    # Accepts any object, as before the move: callers pass the persistence singleton or test doubles.
    layer = cast(AsyncPersistenceLayer, persistence)
    key = id(layer)
    service = _container_service_cache.get(key)
    if service is None:
        service = ContainerService(persistence=layer)
        _container_service_cache[key] = service
    return service
