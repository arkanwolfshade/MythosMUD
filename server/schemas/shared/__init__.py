"""Shared schemas: base models, target resolution, inventory validation."""

from .base import SecureBaseModel
from .inventory_schema import (
    PLAYER_INVENTORY_SCHEMA,
    InventorySchemaValidationError,
    validate_inventory_items,
    validate_inventory_payload,
)
from .target_resolution import TargetMatch, TargetResolutionResult, TargetType

__all__ = [
    "SecureBaseModel",
    "InventorySchemaValidationError",
    "PLAYER_INVENTORY_SCHEMA",
    "validate_inventory_items",
    "validate_inventory_payload",
    "TargetMatch",
    "TargetResolutionResult",
    "TargetType",
]
