"""
Constants and shared types for async persistence layer.

Extracted to keep async_persistence.py under file-nloc limit.
"""

from typing import Any, TypedDict

# Profession table columns for explicit SELECT queries
PROFESSION_COLUMNS = "id, name, description, flavor_text, is_available"


class CreateItemInstanceInput(TypedDict, total=False):
    """Optional fields for create_item_instance. owner_type, owner_id, etc. with defaults."""

    owner_type: str
    owner_id: str | None
    location_context: str | None
    quantity: int
    condition: int | None
    flags_override: list[str] | None
    binding_state: str | None
    attunement_state: dict[str, Any] | None
    custom_name: str | None
    metadata: dict[str, Any] | None
    metadata_payload: dict[str, Any] | None
    origin_source: str | None
    origin_metadata: dict[str, Any] | None


class EnsureItemInstanceInput(TypedDict, total=False):
    """Optional fields for ensure_item_instance."""

    owner_type: str
    owner_id: str | None
    quantity: int
    metadata: dict[str, Any] | None
    metadata_payload: dict[str, Any] | None
    origin_source: str | None
    origin_metadata: dict[str, Any] | None
