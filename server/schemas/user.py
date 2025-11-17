"""
Pydantic schemas for User model.

This module defines Pydantic schemas for user creation, reading,
and updating operations.
"""

import uuid
from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class UserBase(BaseModel):
    """Base user schema with common fields."""

    __slots__ = ()  # Performance optimization

    username: str = Field(..., description="User's username")
    is_active: bool = Field(default=True, description="Whether user is active")
    is_superuser: bool = Field(default=False, description="Whether user is superuser")


class UserCreate(UserBase):
    """Schema for creating a new user."""

    __slots__ = ()  # Performance optimization

    password: str = Field(..., min_length=8, description="User's password")

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "username": "user",
                "password": "securepassword123",
                "is_active": True,
                "is_superuser": False,
                "is_verified": False,
            }
        }
    )


class UserRead(UserBase):
    """Schema for reading user data."""

    __slots__ = ()  # Performance optimization

    user_id: uuid.UUID = Field(..., description="User's unique identifier")
    created_at: datetime = Field(..., description="User creation timestamp")
    updated_at: datetime = Field(..., description="User last update timestamp")

    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {
                "id": "123e4567-e89b-12d3-a456-426614174000",
                "username": "user",
                "is_active": True,
                "is_superuser": False,
                "is_verified": False,
                "created_at": "2024-01-01T00:00:00Z",
                "updated_at": "2024-01-01T00:00:00Z",
            }
        },
    )


class UserUpdate(BaseModel):
    """Schema for updating user data."""

    __slots__ = ()  # Performance optimization

    username: str | None = Field(None, description="User's username")
    password: str | None = Field(None, min_length=8, description="User's password")
    is_active: bool | None = Field(None, description="Whether user is active")
    is_superuser: bool | None = Field(None, description="Whether user is superuser")

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "username": "neweuser",
                "password": "newsecurepassword123",
                "is_active": True,
                "is_superuser": False,
                "is_verified": True,
            }
        }
    )
