"""
Container API response schemas for MythosMUD server.

This module provides Pydantic models for container-related API responses,
ensuring type safety and automatic OpenAPI documentation.
"""

from typing import Any

from pydantic import BaseModel, ConfigDict, Field

# InventoryStack is a TypedDict from services, use dict[str, Any] for Pydantic compatibility
# from ..services.inventory_service import InventoryStack


class ContainerOpenResponse(BaseModel):
    """Response model for opening a container."""

    container: dict[str, Any] = Field(..., description="Container data including inventory and metadata")
    mutation_token: str = Field(..., description="Token required for subsequent container operations")

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "container": {
                    "id": "123e4567-e89b-12d3-a456-426614174000",
                    "name": "Wooden Chest",
                    "inventory": [],
                    "capacity": 10,
                },
                "mutation_token": "abc123def456",
            }
        }
    )


class ContainerTransferResponse(BaseModel):
    """Response model for transferring items between container and inventory."""

    container: dict[str, Any] = Field(..., description="Updated container data")
    player_inventory: list[dict[str, Any]] = Field(
        ..., description="Updated player inventory (list of InventoryStack items)"
    )

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "container": {
                    "id": "123e4567-e89b-12d3-a456-426614174000",
                    "inventory": [],
                },
                "player_inventory": [
                    {
                        "item_id": "sword_001",
                        "quantity": 1,
                        "slot": 0,
                    }
                ],
            }
        }
    )


class ContainerCloseResponse(BaseModel):
    """Response model for closing a container."""

    status: str = Field(..., description="Status of the close operation")

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "status": "closed",
            }
        }
    )


class ContainerLootAllResponse(BaseModel):
    """Response model for looting all items from a container."""

    container: dict[str, Any] = Field(..., description="Updated container data after looting")
    player_inventory: list[dict[str, Any]] = Field(
        ..., description="Updated player inventory with looted items (list of InventoryStack items)"
    )
    items_looted: int = Field(..., description="Number of items successfully looted")

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "container": {
                    "id": "123e4567-e89b-12d3-a456-426614174000",
                    "inventory": [],
                },
                "player_inventory": [
                    {
                        "item_id": "sword_001",
                        "quantity": 1,
                        "slot": 0,
                    }
                ],
                "items_looted": 1,
            }
        }
    )
