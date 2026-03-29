"""Shared service initialization for inventory commands."""

from typing import cast

from ..services.equipment_service import EquipmentService
from ..services.inventory_service import InventoryService
from ..services.wearable_container_service import WearableContainerService

# Lazy-initialized shared services (initialized on first use).
# Use mixed-case names so basedpyright does not treat assignments as constant redefinition.
_shared_inventory_service: InventoryService | None = None
_shared_wearable_container_service: WearableContainerService | None = None
_shared_equipment_service: EquipmentService | None = None


def get_shared_services(request: object) -> tuple[InventoryService, WearableContainerService, EquipmentService]:
    """
    Get shared service instances, initializing them lazily if needed.

    This ensures services are initialized with proper dependencies from the application container.

    Args:
        request: FastAPI request object to access app state

    Returns:
        Tuple of (inventory_service, wearable_container_service, equipment_service)
    """
    global _shared_inventory_service, _shared_wearable_container_service, _shared_equipment_service  # pylint: disable=global-statement  # Reason: Singleton pattern for shared services

    if _shared_inventory_service is None:
        # Get async_persistence from container (getattr + cast: request/app/state are untyped objects)
        app: object | None = cast(object | None, getattr(request, "app", None))
        state: object | None = cast(object | None, getattr(app, "state", None)) if app is not None else None
        container: object | None = cast(object | None, getattr(state, "container", None)) if state is not None else None
        async_persistence: object | None = (
            cast(object | None, getattr(container, "async_persistence", None)) if container is not None else None
        )

        if async_persistence is None:
            raise ValueError("async_persistence is required but not available from container")

        _shared_inventory_service = InventoryService()
        _shared_wearable_container_service = WearableContainerService(persistence=async_persistence)
        _shared_equipment_service = EquipmentService(
            inventory_service=_shared_inventory_service,
            wearable_container_service=_shared_wearable_container_service,
        )

    assert _shared_inventory_service is not None
    assert _shared_wearable_container_service is not None
    assert _shared_equipment_service is not None
    return _shared_inventory_service, _shared_wearable_container_service, _shared_equipment_service
