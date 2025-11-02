"""
Pydantic schemas for Invite model.

This module defines Pydantic schemas for invite creation, reading,
and updating operations.
"""

from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class InviteBase(BaseModel):
    """Base invite schema with common fields."""

    invite_code: str = Field(..., min_length=1, max_length=50, description="Invite code")
    used: bool = Field(default=False, description="Whether invite has been used")


class InviteCreate(InviteBase):
    """Schema for creating a new invite."""

    expires_at: datetime | None = Field(None, description="When the invite expires")

    model_config = ConfigDict(
        json_schema_extra={
            "example": {"invite_code": "ABC123DEF456", "used": False, "expires_at": "2024-12-31T23:59:59Z"}
        }
    )


class InviteRead(InviteBase):
    """Schema for reading invite data."""

    id: str = Field(..., description="Invite's unique identifier (UUID as string)")
    used_by_user_id: str | None = Field(None, description="User who used the invite (UUID as string)")
    expires_at: datetime | None = Field(None, description="When the invite expires")
    created_at: datetime = Field(..., description="Invite creation timestamp")

    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {
                "id": "123e4567-e89b-12d3-a456-426614174000",
                "invite_code": "ABC123DEF456",
                "used_by_user_id": None,
                "used": False,
                "expires_at": "2024-12-31T23:59:59Z",
                "created_at": "2024-01-01T00:00:00Z",
            }
        },
    )


class InviteUpdate(BaseModel):
    """Schema for updating invite data."""

    invite_code: str | None = Field(None, min_length=1, max_length=50, description="Invite code")
    used: bool | None = Field(None, description="Whether invite has been used")
    used_by_user_id: str | None = Field(None, description="User who used the invite (UUID as string)")
    expires_at: datetime | None = Field(None, description="When the invite expires")

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "invite_code": "NEW123CODE456",
                "used": True,
                "used_by_user_id": "123e4567-e89b-12d3-a456-426614174000",
                "expires_at": "2024-12-31T23:59:59Z",
            }
        }
    )
