"""
User model for FastAPI Users integration.

This module defines the User model that will be used by FastAPI Users
for authentication and user management.
"""

from datetime import UTC, datetime

from fastapi_users.db import SQLAlchemyBaseUserTableUUID
from sqlalchemy import Column, DateTime, String
from sqlalchemy.orm import declarative_base

from ..metadata import metadata

# Create base class for declarative models
Base = declarative_base(metadata=metadata)


class User(SQLAlchemyBaseUserTableUUID, Base):
    """
    User model for FastAPI Users v14+.

    Extends SQLAlchemyBaseUserTableUUID to provide all necessary fields
    for FastAPI Users authentication system with UUID primary keys.
    """

    __tablename__ = "users"
    __table_args__ = {"extend_existing": True}

    # Override the id column to match our database schema
    id = Column("user_id", String(length=255), primary_key=True, index=True)

    # User authentication fields (email and hashed_password are inherited from base)
    username = Column(String(length=255), unique=True, nullable=False, index=True)

    # User status fields (is_active, is_superuser, is_verified are inherited from base)

    # Timestamps (persist naive UTC for SQLite)
    created_at = Column(DateTime(), default=lambda: datetime.now(UTC).replace(tzinfo=None), nullable=False)
    updated_at = Column(
        DateTime(),
        default=lambda: datetime.now(UTC).replace(tzinfo=None),
        onupdate=lambda: datetime.now(UTC).replace(tzinfo=None),
        nullable=False,
    )

    def __repr__(self) -> str:
        """String representation of the user."""
        return f"<User(id={self.id}, username={self.username}, is_active={self.is_active})>"

    @property
    def user_id(self) -> str:
        """Get the user ID for backward compatibility."""
        return str(self.id)

    @property
    def is_authenticated(self) -> bool:
        """Check if user is authenticated."""
        return self.is_active

    def get_display_name(self) -> str:
        """Get display name for the user."""
        return self.username if self.username else str(self.id)
