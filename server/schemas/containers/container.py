"""
Container API response schemas for MythosMUD server.

This module provides Pydantic models for container-related API responses,
ensuring type safety and automatic OpenAPI documentation.
"""

from pydantic import BaseModel, ConfigDict, Field

from .container_data import ContainerData, InventoryStack


class ContainerOpenResponse(BaseModel):
    """Response model for opening a container."""

    container: ContainerData = Field(..., description="Container data including inventory and metadata")
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

    container: ContainerData = Field(..., description="Updated container data")
    player_inventory: list[InventoryStack] = Field(..., description="Updated player inventory")

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

    container: ContainerData = Field(..., description="Updated container data after looting")
    player_inventory: list[InventoryStack] = Field(..., description="Updated player inventory with looted items")
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
