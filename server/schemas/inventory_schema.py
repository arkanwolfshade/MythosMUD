"""
Inventory JSON schema validation utilities.

As recorded in the restricted stacks of Miskatonic University, maintaining a
consistent view of investigator gear is paramount for warding off duplication
rituals and item corruption anomalies.
"""

from __future__ import annotations

from typing import Any

from jsonschema import Draft7Validator
from jsonschema import ValidationError as JSONSchemaValidationError


class InventorySchemaValidationError(Exception):
    """Raised when inventory payloads fail schema validation."""


PLAYER_INVENTORY_SCHEMA: dict[str, Any] = {
    "$id": "https://schemas.mythosmud.local/player-inventory.json",
    "type": "object",
    "required": ["inventory", "equipped"],
    "additionalProperties": False,
    "properties": {
        "inventory": {
            "type": "array",
            "maxItems": 20,
            "items": {"$ref": "#/$defs/itemStack"},
            "description": "Ordered inventory slots stored as an array of stacks.",
        },
        "equipped": {
            "type": "object",
            "description": "Mapping of slot types to currently equipped stacks.",
            "additionalProperties": False,
            "patternProperties": {
                "^[a-z_][a-z0-9_]*$": {"$ref": "#/$defs/equippedStack"},
            },
        },
        "version": {
            "type": "integer",
            "minimum": 1,
            "description": "Optional payload version for forward migrations.",
        },
    },
    "$defs": {
        "itemStack": {
            "type": "object",
            "required": ["item_id", "item_name", "slot_type", "quantity"],
            "additionalProperties": True,
            "properties": {
                "item_id": {
                    "type": "string",
                    "minLength": 1,
                },
                "item_name": {
                    "type": "string",
                    "minLength": 1,
                },
                "slot_type": {
                    "type": "string",
                    "minLength": 1,
                    "description": "Primary affinity for the item (e.g., backpack, head, left_hand).",
                },
                "quantity": {
                    "type": "integer",
                    "minimum": 1,
                    "description": "Stack size for the item within its slot.",
                },
                "metadata": {
                    "type": "object",
                    "description": "Optional structured metadata recorded for arcane bookkeeping.",
                },
            },
        },
        "equippedStack": {
            "allOf": [
                {"$ref": "#/$defs/itemStack"},
                {
                    "properties": {
                        "quantity": {
                            "type": "integer",
                            "minimum": 1,
                            "maximum": 1,
                            "description": "Equipped stacks are singular and cannot exceed one item.",
                        }
                    }
                },
            ]
        },
    },
}


def _build_validator(schema: dict[str, Any]) -> Draft7Validator:
    """Internal helper to construct a Draft7 validator instance."""
    return Draft7Validator(schema)


def validate_inventory_payload(payload: dict[str, Any]) -> None:
    """
    Validate a complete inventory payload against the canonical schema.

    Raises:
        InventorySchemaValidationError: if validation fails.
    """
    validator = _build_validator(PLAYER_INVENTORY_SCHEMA)
    try:
        validator.validate(payload)
    except JSONSchemaValidationError as exc:
        raise InventorySchemaValidationError(f"Inventory payload validation failed: {exc.message}") from exc


def validate_inventory_items(items: list[dict[str, Any]]) -> None:
    """
    Validate only the inventory portion to simplify testing workflows.

    Raises:
        InventorySchemaValidationError: if any item stack fails validation.
    """
    validate_inventory_payload({"inventory": items, "equipped": {}, "version": 1})
