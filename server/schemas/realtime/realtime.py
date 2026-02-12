"""
Real-time API response schemas for MythosMUD server.

This module provides Pydantic models for real-time connection API responses,
ensuring type safety and automatic OpenAPI documentation.
"""

import time

from pydantic import BaseModel, ConfigDict, Field

from .presence_data import ErrorStatistics, PresenceStatistics, SessionStatistics


class PresenceInfo(BaseModel):
    """Presence information for a player connection."""

    is_online: bool = Field(..., description="Whether player is currently online")
    last_seen: float | None = Field(default=None, description="Last seen timestamp")
    connection_count: int = Field(default=0, description="Number of active connections")

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "is_online": True,
                "last_seen": 1234567890.0,
                "connection_count": 2,
            }
        }
    )


class SessionInfo(BaseModel):
    """Session information for a player connection."""

    session_id: str | None = Field(default=None, description="Current session ID")
    session_connections: list[str] = Field(default_factory=list, description="List of connection IDs in this session")
    is_valid: bool = Field(default=False, description="Whether the session is valid")

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "session_id": "session-123",
                "session_connections": ["conn-1", "conn-2"],
                "is_valid": True,
            }
        }
    )


class HealthInfo(BaseModel):
    """Health information for a player connection."""

    is_healthy: bool = Field(..., description="Whether connection is healthy")
    last_heartbeat: float | None = Field(default=None, description="Last heartbeat timestamp")
    latency: float | None = Field(default=None, description="Connection latency in milliseconds")

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "is_healthy": True,
                "last_heartbeat": 1234567890.0,
                "latency": 50.5,
            }
        }
    )


class PlayerConnectionsResponse(BaseModel):
    """Response model for player connection information endpoint."""

    player_id: str = Field(..., description="Player ID")
    presence: PresenceInfo = Field(..., description="Presence information")
    session: SessionInfo = Field(..., description="Session information")
    health: HealthInfo = Field(..., description="Health information")
    timestamp: float = Field(default_factory=time.time, description="Response timestamp")

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "player_id": "123e4567-e89b-12d3-a456-426614174000",
                "presence": {"is_online": True, "last_seen": 1234567890.0},
                "session": {
                    "session_id": "session-123",
                    "session_connections": ["conn-1"],
                    "is_valid": True,
                },
                "health": {"is_healthy": True, "last_heartbeat": 1234567890.0},
                "timestamp": 1234567890.0,
            }
        }
    )


class NewGameSessionResponse(BaseModel):
    """Response model for new game session endpoint."""

    success: bool = Field(..., description="Whether session was created successfully")
    session_id: str = Field(..., description="New session ID")
    disconnected_connections: int = Field(default=0, description="Number of connections that were disconnected")
    message: str | None = Field(default=None, description="Status message")

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "success": True,
                "session_id": "session-123",
                "disconnected_connections": 2,
                "message": "New game session created",
            }
        }
    )


class ConnectionStatisticsResponse(BaseModel):
    """Response model for connection statistics endpoint."""

    presence: PresenceStatistics = Field(..., description="Presence statistics")
    sessions: SessionStatistics = Field(..., description="Session statistics")
    errors: ErrorStatistics = Field(..., description="Error statistics")
    timestamp: float = Field(default_factory=time.time, description="Response timestamp")

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "presence": {"total_online": 10, "total_offline": 5},
                "sessions": {"active_sessions": 8, "total_sessions": 15},
                "errors": {"total_errors": 2, "recent_errors": []},
                "timestamp": 1234567890.0,
            }
        }
    )
