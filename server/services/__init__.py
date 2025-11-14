"""
Services package for MythosMUD.

This package contains various services for handling game functionality,
including direct WebSocket broadcasting, chat services, and other real-time features.
"""

from .active_sanity_service import (
    ActiveSanityService,
    SanityActionError,
    SanityActionOnCooldownError,
    UnknownEncounterCategoryError,
    UnknownSanityActionError,
)
from .admin_auth_service import AdminAuthService, admin_auth_service, get_admin_auth_service
from .catatonia_registry import CatatoniaRegistry
from .equipment_service import (
    EquipmentCapacityError,
    EquipmentService,
    EquipmentServiceError,
    SlotValidationError,
)
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
from .passive_sanity_flux_service import PassiveFluxContext, PassiveSanityFluxService

__all__ = [
    "NPCService",
    "npc_service",
    "NPCInstanceService",
    "get_npc_instance_service",
    "initialize_npc_instance_service",
    "AdminAuthService",
    "get_admin_auth_service",
    "admin_auth_service",
    "EquipmentService",
    "EquipmentServiceError",
    "SlotValidationError",
    "EquipmentCapacityError",
    "InventoryService",
    "InventoryServiceError",
    "InventoryValidationError",
    "InventoryCapacityError",
    "InventorySplitError",
    "InventoryMutationGuard",
    "MutationDecision",
    "PassiveSanityFluxService",
    "PassiveFluxContext",
    "ActiveSanityService",
    "SanityActionError",
    "SanityActionOnCooldownError",
    "UnknownSanityActionError",
    "UnknownEncounterCategoryError",
    "CatatoniaRegistry",
]
