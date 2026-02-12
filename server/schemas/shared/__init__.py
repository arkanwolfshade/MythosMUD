"""Shared schemas: base models, target resolution, inventory validation."""

from .base import ResponseBaseModel, SecureBaseModel
from .inventory_schema import (
    PLAYER_INVENTORY_SCHEMA,
    InventorySchemaValidationError,
    validate_inventory_items,
    validate_inventory_payload,
)
from .target_resolution import TargetMatch, TargetResolutionResult, TargetType

__all__ = [
    "ResponseBaseModel",
    "SecureBaseModel",
    "InventorySchemaValidationError",
    "PLAYER_INVENTORY_SCHEMA",
    "validate_inventory_items",
    "validate_inventory_payload",
    "TargetMatch",
    "TargetResolutionResult",
    "TargetType",
]
