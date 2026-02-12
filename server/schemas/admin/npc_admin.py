"""
NPC Admin API response schemas for MythosMUD server.

This module provides Pydantic models for NPC admin API responses,
ensuring type safety and automatic OpenAPI documentation.
"""

from typing import Any

from pydantic import BaseModel, ConfigDict, Field


class NPCSpawnResponse(BaseModel):
    """Response model for NPC spawn operations."""

    npc_id: str = Field(..., description="ID of the spawned NPC instance")
    definition_id: int = Field(..., description="ID of the NPC definition used")
    room_id: str = Field(..., description="Room where NPC was spawned")
    success: bool = Field(default=True, description="Whether spawn was successful")
    message: str | None = Field(default=None, description="Status message")

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "npc_id": "npc-123",
                "definition_id": 1,
                "room_id": "arkham_001",
                "success": True,
                "message": "NPC spawned successfully",
            }
        }
    )


class NPCDespawnResponse(BaseModel):
    """Response model for NPC despawn operations."""

    npc_id: str = Field(..., description="ID of the despawned NPC instance")
    npc_name: str | None = Field(default=None, description="Name of the despawned NPC")
    success: bool = Field(default=True, description="Whether despawn was successful")
    message: str | None = Field(default=None, description="Status message")

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "npc_id": "npc-123",
                "npc_name": "Guard",
                "success": True,
                "message": "NPC despawned successfully",
            }
        }
    )


class NPCMoveResponse(BaseModel):
    """Response model for NPC move operations."""

    npc_id: str = Field(..., description="ID of the moved NPC instance")
    npc_name: str | None = Field(default=None, description="Name of the moved NPC")
    old_room_id: str | None = Field(default=None, description="Previous room ID")
    new_room_id: str = Field(..., description="New room ID")
    success: bool = Field(default=True, description="Whether move was successful")
    message: str | None = Field(default=None, description="Status message")

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "npc_id": "npc-123",
                "npc_name": "Guard",
                "old_room_id": "arkham_001",
                "new_room_id": "arkham_002",
                "success": True,
                "message": "NPC moved successfully",
            }
        }
    )


class NPCStatsResponse(BaseModel):
    """Response model for NPC stats.

    This model uses a flexible structure to accommodate dynamic NPC stats
    returned by the NPC instance service.
    """

    model_config = ConfigDict(extra="allow", json_schema_extra={"example": {"npc_id": "npc-123", "name": "Guard"}})


class NPCPopulationStatsResponse(BaseModel):
    """Response model for NPC population statistics.

    This model uses a flexible structure to accommodate dynamic population stats.
    """

    model_config = ConfigDict(
        extra="allow", json_schema_extra={"example": {"total_npcs": 50, "active_npcs": 45, "inactive_npcs": 5}}
    )


class NPCZoneStatsResponse(BaseModel):
    """Response model for NPC zone statistics.

    This model uses a flexible structure to accommodate dynamic zone stats.
    """

    model_config = ConfigDict(
        extra="allow",
        json_schema_extra={"example": {"total_zones": 10, "total_npcs": 50, "zones": {"arkham": 20, "dunwich": 30}}},
    )


class NPCSystemStatusResponse(BaseModel):
    """Response model for NPC system status.

    This model uses a flexible structure to accommodate dynamic system status.
    """

    model_config = ConfigDict(
        extra="allow",
        json_schema_extra={
            "example": {
                "system_status": "healthy",
                "active_npcs": 45,
                "total_npcs": 50,
                "last_update": "2024-01-01T00:00:00Z",
            }
        },
    )


class AdminSessionsResponse(BaseModel):
    """Response model for admin sessions."""

    sessions: list[dict[str, Any]] = Field(..., description="List of active admin sessions")
    count: int = Field(..., description="Number of active sessions")

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "sessions": [{"user_id": "123", "username": "admin", "last_activity": "2024-01-01T00:00:00Z"}],
                "count": 1,
            }
        }
    )


class AdminAuditLogResponse(BaseModel):
    """Response model for admin audit log."""

    audit_log: list[dict[str, Any]] = Field(..., description="List of audit log entries")
    count: int = Field(..., description="Number of audit log entries")

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "audit_log": [
                    {
                        "action": "spawn_npc",
                        "user_id": "123",
                        "timestamp": "2024-01-01T00:00:00Z",
                    }
                ],
                "count": 1,
            }
        }
    )


class AdminCleanupSessionsResponse(BaseModel):
    """Response model for admin session cleanup."""

    message: str = Field(..., description="Cleanup status message")
    cleaned_count: int = Field(..., description="Number of sessions cleaned up")

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "message": "Cleaned up 5 expired sessions",
                "cleaned_count": 5,
            }
        }
    )
