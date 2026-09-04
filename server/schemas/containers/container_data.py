"""
Container data schema for MythosMUD.

This module defines Pydantic models for container and inventory stack data structures.
"""

from __future__ import annotations

from typing import Any

from pydantic import BaseModel, ConfigDict, Field

from ...schemas.game.weapon import WeaponStats


class InventoryStack(BaseModel):
    """
    Inventory stack model for items in containers and player inventories.

    This model represents a stack of items with metadata, flags, and optional weapon stats.
    """

    model_config = ConfigDict(
        extra="forbid",
        validate_assignment=True,
        str_strip_whitespace=True,
        validate_default=True,
    )

    item_instance_id: str = Field(..., description="Unique instance identifier for this item")
    prototype_id: str = Field(..., description="Prototype identifier for the item type")
    item_id: str = Field(..., description="Item identifier (legacy compatibility)")
    item_name: str = Field(..., description="Display name of the item")
    slot_type: str = Field(..., description="Slot type (e.g., backpack, head, left_hand)")
    quantity: int = Field(..., ge=1, description="Number of items in the stack")
    metadata: dict[str, Any] = Field(default_factory=dict, description="Optional structured metadata")
    weapon: WeaponStats | None = Field(default=None, description="Weapon stats when item is a weapon")
    flags: list[str] = Field(default_factory=list, description="Item flags")
    origin: dict[str, Any] = Field(default_factory=dict, description="Origin information")
    created_at: str | None = Field(default=None, description="ISO format creation timestamp")
    inner_container: InnerContainer | None = Field(default=None, description="Nested container for wearable items")


class InnerContainer(BaseModel):
    """Nested container structure for wearable items."""

    model_config = ConfigDict(
        extra="forbid",
        validate_assignment=True,
        str_strip_whitespace=True,
        validate_default=True,
    )

    capacity_slots: int = Field(..., ge=1, description="Capacity of the inner container")
    items: list[InventoryStack] = Field(default_factory=list, description="Items in the inner container")
    lock_state: str | None = Field(default=None, description="Lock state of the inner container")
    allowed_roles: list[str] = Field(default_factory=list, description="Roles allowed to access the inner container")


class ContainerData(BaseModel):
    """
    Container data structure for API responses.

    This model represents container information with inventory and metadata.
    """

    model_config = ConfigDict(
        extra="allow",  # Allow extra fields for dynamic container data
        validate_assignment=True,
        str_strip_whitespace=True,
        validate_default=True,
    )

    container_id: str = Field(..., description="Container instance identifier")
    source_type: str | None = Field(default=None, description="Type of container (environment, equipment, corpse)")
    owner_id: str | None = Field(default=None, description="Owner UUID")
    room_id: str | None = Field(default=None, description="Room identifier")
    entity_id: str | None = Field(default=None, description="Entity UUID for wearable containers")
    lock_state: str | None = Field(default=None, description="Lock state")
    capacity_slots: int | None = Field(default=None, description="Maximum number of inventory slots")
    weight_limit: int | None = Field(default=None, description="Weight limit")
    decay_at: str | None = Field(default=None, description="ISO format decay timestamp")
    allowed_roles: list[str] = Field(default_factory=list, description="Roles allowed to access")
    items: list[InventoryStack] = Field(default_factory=list, description="Items in the container")
    metadata: dict[str, Any] = Field(default_factory=dict, description="Container metadata")
    created_at: str | None = Field(default=None, description="ISO format creation timestamp")
    updated_at: str | None = Field(default=None, description="ISO format update timestamp")
