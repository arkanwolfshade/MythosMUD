"""Shared service initialization for inventory commands."""

from typing import Any

from ..services.equipment_service import EquipmentService
from ..services.inventory_service import InventoryService
from ..services.wearable_container_service import WearableContainerService

# Lazy-initialized shared services (initialized on first use)
_SHARED_INVENTORY_SERVICE: InventoryService | None = None
_SHARED_WEARABLE_CONTAINER_SERVICE: WearableContainerService | None = None
_SHARED_EQUIPMENT_SERVICE: EquipmentService | None = None


def get_shared_services(request: Any) -> tuple[InventoryService, WearableContainerService, EquipmentService]:
    """
    Get shared service instances, initializing them lazily if needed.

    This ensures services are initialized with proper dependencies from the application container.

    Args:
        request: FastAPI request object to access app state

    Returns:
        Tuple of (inventory_service, wearable_container_service, equipment_service)
    """
    global _SHARED_INVENTORY_SERVICE, _SHARED_WEARABLE_CONTAINER_SERVICE, _SHARED_EQUIPMENT_SERVICE  # pylint: disable=global-statement  # Reason: Singleton pattern for shared services

    if _SHARED_INVENTORY_SERVICE is None:
        # Get async_persistence from container
        app = getattr(request, "app", None)
        container = getattr(app.state, "container", None) if app else None
        async_persistence = getattr(container, "async_persistence", None) if container else None

        if async_persistence is None:
            raise ValueError("async_persistence is required but not available from container")

        _SHARED_INVENTORY_SERVICE = InventoryService()
        _SHARED_WEARABLE_CONTAINER_SERVICE = WearableContainerService(persistence=async_persistence)
        _SHARED_EQUIPMENT_SERVICE = EquipmentService(
            inventory_service=_SHARED_INVENTORY_SERVICE,
            wearable_container_service=_SHARED_WEARABLE_CONTAINER_SERVICE,
        )

    # Type narrowing: After initialization, these are guaranteed to be non-None
    if _SHARED_INVENTORY_SERVICE is None:
        raise RuntimeError("Inventory service must be initialized")
    if _SHARED_WEARABLE_CONTAINER_SERVICE is None:
        raise RuntimeError("Wearable container service must be initialized")
    if _SHARED_EQUIPMENT_SERVICE is None:
        raise RuntimeError("Equipment service must be initialized")

    return _SHARED_INVENTORY_SERVICE, _SHARED_WEARABLE_CONTAINER_SERVICE, _SHARED_EQUIPMENT_SERVICE
