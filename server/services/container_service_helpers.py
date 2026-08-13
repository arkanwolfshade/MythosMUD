"""
Helpers and exceptions for the unified container service.

Extracted so container_service modules stay under Lizard file-nloc limits.
"""

from __future__ import annotations

from collections.abc import Mapping
from enum import Enum
from typing import cast

from ..exceptions import MythosMUDError
from ..structured_logging.enhanced_logging_config import get_logger
from .inventory_service import InventoryStack

logger = get_logger(__name__)

# Dummy stack for error logging only (_require_container_component uses item_id).
# Public: shared across container_service_* modules after Lizard NLOC split.
UNKNOWN_STACK: InventoryStack = {
    "item_instance_id": "unknown",
    "prototype_id": "unknown",
    "item_id": "unknown",
    "item_name": "unknown",
    "slot_type": "unknown",
    "quantity": 1,
}


def get_enum_value(enum_or_str: object) -> str:
    """
    Safely get enum value, handling both enum instances and string values.

    When containers are deserialized from the database, enum fields may be strings
    instead of enum instances. This helper handles both cases.

    Args:
        enum_or_str: Either an enum instance or a string value

    Returns:
        String value of the enum
    """
    if isinstance(enum_or_str, Enum):
        # Enum.value is typed Any in typeshed; coerce via object for reportAny.
        return str(cast(object, enum_or_str.value))
    return str(enum_or_str)


def as_object_dict(data: object) -> dict[str, object]:
    """Narrow persistence / payload dicts to object values for static analysis."""
    if not isinstance(data, dict):
        return {}
    return cast(dict[str, object], data)


def filter_container_data(container_data: Mapping[str, object]) -> dict[str, object]:
    """
    Filter out database-specific fields that are not part of the ContainerComponent model.

    The database returns created_at and updated_at fields, but the ContainerComponent
    model has extra="forbid", so these fields must be removed before validation.

    Also converts items_json to items and metadata_json to metadata to match
    the ContainerComponent model field names.

    Args:
        container_data: Raw container data from database

    Returns:
        Filtered container data without database-specific fields, with field names converted
    """
    # Mapping (not dict) so callers may pass narrower value types (dict value invariance).
    filtered: dict[str, object] = {k: v for k, v in container_data.items() if k not in ("created_at", "updated_at")}

    # Convert items_json to items and metadata_json to metadata for ContainerComponent model
    if "items_json" in filtered:
        filtered["items"] = filtered.pop("items_json")
    if "metadata_json" in filtered:
        filtered["metadata"] = filtered.pop("metadata_json")

    return filtered


def items_json_for_persist(items: list[InventoryStack]) -> list[dict[str, object]]:
    """Narrow InventoryStack TypedDict rows for persistence dict[str, object] APIs."""
    # TypedDict is not a subtype of dict[str, object]; cast via object first.
    return [cast(dict[str, object], cast(object, item)) for item in items]


def player_inventory_for_response(player: object) -> list[InventoryStack]:
    """Read player.inventory (tests/mocks) as typed stacks; empty if missing."""
    inventory = getattr(player, "inventory", None)
    if not isinstance(inventory, list):
        return []
    return cast(list[InventoryStack], inventory)


class ContainerServiceError(MythosMUDError):
    """Base exception for container service operations."""


class ContainerNotFoundError(ContainerServiceError):
    """Raised when a container is not found."""


class ContainerLockedError(ContainerServiceError):
    """Raised when attempting to access a locked container."""


class ContainerCapacityError(ContainerServiceError):
    """Raised when container capacity is exceeded."""


class ContainerAccessDeniedError(ContainerServiceError):
    """Raised when access to container is denied."""
