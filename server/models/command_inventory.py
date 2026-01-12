"""
Inventory command models for MythosMUD.

This module provides command models for inventory management and item manipulation.
"""

from typing import Literal

from pydantic import Field, field_validator, model_validator

from .command_base import BaseCommand, CommandType


class InventoryCommand(BaseCommand):
    """Command for showing player inventory."""

    command_type: Literal[CommandType.INVENTORY] = CommandType.INVENTORY


class PickupCommand(BaseCommand):
    """Command for picking up items from room drops."""

    command_type: Literal[CommandType.PICKUP] = CommandType.PICKUP
    index: int | None = Field(
        None,
        ge=1,
        description="Index of the room drop to collect (1-based).",
    )
    search_term: str | None = Field(
        None,
        min_length=1,
        max_length=120,
        description="Name fragment or prototype identifier for fuzzy selection.",
    )
    quantity: int | None = Field(None, ge=1, description="Quantity to pick up (defaults to full stack)")

    @field_validator("search_term")
    @classmethod
    def validate_search_term(cls, v: str | None) -> str | None:
        """Strip and validate search term."""
        if v is None:
            return v
        stripped = v.strip()
        if not stripped:
            return None
        return stripped

    @model_validator(mode="after")
    def validate_pickup_requirements(self) -> "PickupCommand":
        """Ensure either index or search_term is provided."""
        if self.index is None and self.search_term is None:
            raise ValueError("Pickup command requires an item number or name.")
        return self


class DropCommand(BaseCommand):
    """Command for dropping items from inventory into the room."""

    command_type: Literal[CommandType.DROP] = CommandType.DROP
    index: int = Field(..., ge=1, description="Index of the inventory slot to drop")
    quantity: int | None = Field(None, ge=1, description="Quantity to drop (defaults to full stack)")


class PutCommand(BaseCommand):
    """Command for putting items from inventory into a container."""

    command_type: Literal[CommandType.PUT] = CommandType.PUT
    item: str = Field(..., min_length=1, description="Item name or inventory index to put")
    container: str = Field(..., min_length=1, description="Container name to put item into")
    quantity: int | None = Field(None, ge=1, description="Quantity to put (defaults to full stack)")


class GetCommand(BaseCommand):
    """Command for getting items from a container into inventory."""

    command_type: Literal[CommandType.GET] = CommandType.GET
    item: str = Field(..., min_length=1, description="Item name or container index to get")
    container: str = Field(..., min_length=1, description="Container name to get item from")
    quantity: int | None = Field(None, ge=1, description="Quantity to get (defaults to full stack)")


class EquipCommand(BaseCommand):
    """Command for equipping an item from inventory."""

    command_type: Literal[CommandType.EQUIP] = CommandType.EQUIP
    index: int | None = Field(
        None,
        ge=1,
        description="Inventory slot index to equip (1-based).",
    )
    search_term: str | None = Field(
        None,
        min_length=1,
        max_length=120,
        description="Name fragment or prototype identifier to resolve inventory item.",
    )
    target_slot: str | None = Field(None, max_length=30, description="Optional slot override")

    @field_validator("search_term")
    @classmethod
    def validate_search_term(cls, v: str | None) -> str | None:
        """Strip and validate search term."""
        if v is None:
            return v
        stripped = v.strip()
        if not stripped:
            return None
        return stripped

    @model_validator(mode="after")
    def validate_equip_requirements(self) -> "EquipCommand":
        """Ensure either index or search_term is provided."""
        if self.index is None and self.search_term is None:
            raise ValueError("Equip command requires an item number or name.")
        return self

    @field_validator("target_slot")
    @classmethod
    def validate_slot(cls, value: str | None) -> str | None:
        """Validate target slot value.

        Args:
            value: The target slot value to validate (can be None)

        Returns:
            str | None: The validated target slot or None
        """
        if value is None:
            return None
        normalized = value.strip().lower()
        if not normalized:
            raise ValueError("Slot cannot be empty")
        return normalized


class UnequipCommand(BaseCommand):
    """Command for unequipping an item back to inventory."""

    command_type: Literal[CommandType.UNEQUIP] = CommandType.UNEQUIP
    slot: str | None = Field(
        default=None,
        min_length=1,
        max_length=30,
        description="Slot to unequip (optional when providing item name).",
    )
    search_term: str | None = Field(
        default=None,
        min_length=1,
        max_length=120,
        description="Name fragment identifying the equipped item to remove.",
    )

    @field_validator("slot")
    @classmethod
    def validate_slot(cls, v: str | None) -> str | None:
        """Strip and normalize slot name."""
        if v is None:
            return v
        normalized = v.strip().lower()
        if not normalized:
            return None
        return normalized

    @field_validator("search_term")
    @classmethod
    def validate_search_term(cls, v: str | None) -> str | None:
        """Strip and validate search term."""
        if v is None:
            return v
        stripped = v.strip()
        if not stripped:
            return None
        return stripped

    @model_validator(mode="after")
    def validate_unequip_requirements(self) -> "UnequipCommand":
        """Ensure either slot or search_term is provided."""
        slot_empty = self.slot is None
        search_term_empty = self.search_term is None
        if slot_empty and search_term_empty:
            raise ValueError("Unequip command requires a slot or item name.")
        return self
