"""
Presence and health statistics schema for MythosMUD.

This module defines Pydantic models for connection statistics used in API responses.
"""

from typing import Any

from pydantic import BaseModel, ConfigDict, Field


class PresenceStatistics(BaseModel):
    """
    Presence statistics for connection monitoring.

    This model represents aggregate presence metrics across all connections.
    """

    model_config = ConfigDict(
        extra="allow",  # Allow extra fields for dynamic statistics
        validate_assignment=True,
        str_strip_whitespace=True,
        validate_default=True,
    )

    total_online: int | None = Field(default=None, description="Total number of online players")
    total_offline: int | None = Field(default=None, description="Total number of offline players")
    active_connections: int | None = Field(default=None, description="Number of active connections")


class SessionStatistics(BaseModel):
    """
    Session statistics for connection monitoring.

    This model represents aggregate session metrics.
    """

    model_config = ConfigDict(
        extra="allow",  # Allow extra fields for dynamic statistics
        validate_assignment=True,
        str_strip_whitespace=True,
        validate_default=True,
    )

    active_sessions: int | None = Field(default=None, description="Number of active sessions")
    total_sessions: int | None = Field(default=None, description="Total number of sessions")
    average_connections_per_session: float | None = Field(default=None, description="Average connections per session")


class ErrorStatistics(BaseModel):
    """
    Error statistics for connection monitoring.

    This model represents aggregate error metrics.
    """

    model_config = ConfigDict(
        extra="allow",  # Allow extra fields for dynamic statistics
        validate_assignment=True,
        str_strip_whitespace=True,
        validate_default=True,
    )

    total_errors: int | None = Field(default=None, description="Total number of errors")
    recent_errors: list[dict[str, Any]] = Field(default_factory=list, description="List of recent error details")
