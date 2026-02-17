"""
Admin data schema for MythosMUD.

This module defines Pydantic models for admin session and audit log data structures.
"""

from typing import Any

from pydantic import BaseModel, ConfigDict, Field


class AdminSession(BaseModel):
    """
    Admin session information.

    This model represents an active admin session with user and activity details.
    """

    model_config = ConfigDict(
        extra="forbid",
        validate_assignment=True,
        str_strip_whitespace=True,
        validate_default=True,
    )

    user_id: str = Field(..., description="User ID of the admin")
    username: str = Field(..., description="Username of the admin")
    role: str = Field(..., description="Admin role")
    ip_address: str = Field(..., description="IP address of the session")
    created_at: str = Field(..., description="ISO format creation timestamp")
    last_activity: str = Field(..., description="ISO format last activity timestamp")
    action_count: int = Field(default=0, ge=0, description="Number of actions performed in this session")


class AuditLogEntry(BaseModel):
    """
    Audit log entry for admin actions.

    This model represents a single audit log entry tracking administrative actions.
    """

    model_config = ConfigDict(
        extra="allow",  # Allow extra fields for dynamic audit data
        validate_assignment=True,
        str_strip_whitespace=True,
        validate_default=True,
    )

    timestamp: str = Field(..., description="ISO format timestamp of the action")
    action_type: str | None = Field(default=None, description="Type of action (e.g., 'admin_command', 'player_action')")
    event_type: str | None = Field(default=None, description="Event type (alternative to action_type)")
    admin_name: str | None = Field(default=None, description="Name of the admin who performed the action")
    admin: str | None = Field(default=None, description="Admin identifier (alternative to admin_name)")
    command: str | None = Field(default=None, description="Command that was executed")
    action: str | None = Field(default=None, description="Action performed (alternative to command)")
    target_player: str | None = Field(default=None, description="Target player if applicable")
    success: bool | None = Field(default=None, description="Whether the action was successful")
    error_message: str | None = Field(default=None, description="Error message if the action failed")
    additional_data: dict[str, Any] | None = Field(default=None, description="Additional action data")
