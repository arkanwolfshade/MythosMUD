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


def reset_shared_inventory_services_for_tests() -> None:
    """
    Clear lazy singletons so each test gets a fresh init path.

    For unit tests only; production code must not call this.
    """
    global _shared_inventory_service, _shared_wearable_container_service, _shared_equipment_service  # pylint: disable=global-statement  # Reason: Test reset of module singletons
    _shared_inventory_service = None
    _shared_wearable_container_service = None
    _shared_equipment_service = None


def _ensure_shared_services_initialized(request: object) -> None:
    """Resolve async_persistence from the request and construct shared singletons."""
    global _shared_inventory_service, _shared_wearable_container_service, _shared_equipment_service  # pylint: disable=global-statement  # Reason: Singleton pattern for shared services

    # getattr + cast: request/app/state are untyped objects
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


def get_shared_services(request: object) -> tuple[InventoryService, WearableContainerService, EquipmentService]:
    """
    Get shared service instances, initializing them lazily if needed.

    This ensures services are initialized with proper dependencies from the application container.

    Args:
        request: FastAPI request object to access app state

    Returns:
        Tuple of (inventory_service, wearable_container_service, equipment_service)
    """
    if _shared_inventory_service is None:
        _ensure_shared_services_initialized(request)

    # Explicit check (not assert): assertions are stripped under python -O.
    inv = _shared_inventory_service
    wear = _shared_wearable_container_service
    eq = _shared_equipment_service
    if inv is None or wear is None or eq is None:
        raise RuntimeError("Shared inventory services failed to initialize")
    return inv, wear, eq
