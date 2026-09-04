"""
Services package for MythosMUD.

This package contains various services for handling game functionality,
including direct WebSocket broadcasting, chat services, and other real-time features.
"""

from .active_lucidity_service import (
    ActiveLucidityService,
    LucidityActionError,
    LucidityActionOnCooldownError,
    UnknownEncounterCategoryError,
    UnknownLucidityActionError,
)
from .admin_auth_service import AdminAuthService, admin_auth_service, get_admin_auth_service
from .catatonia_registry import CatatoniaRegistry
from .container_service import (
    ContainerAccessDeniedError,
    ContainerCapacityError,
    ContainerLockedError,
    ContainerNotFoundError,
    ContainerService,
    ContainerServiceError,
)
from .equipment_service import (
    EquipmentCapacityError,
    EquipmentService,
    EquipmentServiceError,
    SlotValidationError,
)
from .holiday_service import HolidayService
from .inventory_mutation_guard import InventoryMutationGuard, MutationDecision
from .inventory_service import (
    InventoryCapacityError,
    InventoryService,
    InventoryServiceError,
    InventorySplitError,
    InventoryValidationError,
)
from .npc_instance_service import NPCInstanceService, get_npc_instance_service, initialize_npc_instance_service
from .npc_service import NPCService, npc_service
from .passive_lucidity_flux_service import PassiveFluxContext, PassiveLucidityFluxService
from .schedule_service import ScheduleService
from .wearable_container_service import (
    WearableContainerService,
    WearableContainerServiceError,
)

__all__ = [
    "NPCService",
    "npc_service",
    "NPCInstanceService",
    "get_npc_instance_service",
    "initialize_npc_instance_service",
    "AdminAuthService",
    "get_admin_auth_service",
    "admin_auth_service",
    "ContainerService",
    "ContainerServiceError",
    "ContainerNotFoundError",
    "ContainerLockedError",
    "ContainerCapacityError",
    "ContainerAccessDeniedError",
    "EquipmentService",
    "EquipmentServiceError",
    "SlotValidationError",
    "EquipmentCapacityError",
    "WearableContainerService",
    "WearableContainerServiceError",
    "InventoryService",
    "InventoryServiceError",
    "InventoryValidationError",
    "InventoryCapacityError",
    "InventorySplitError",
    "InventoryMutationGuard",
    "MutationDecision",
    "PassiveLucidityFluxService",
    "PassiveFluxContext",
    "ActiveLucidityService",
    "LucidityActionError",
    "LucidityActionOnCooldownError",
    "UnknownLucidityActionError",
    "UnknownEncounterCategoryError",
    "CatatoniaRegistry",
    "HolidayService",
    "ScheduleService",
]
