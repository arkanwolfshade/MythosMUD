"""
User model for FastAPI Users integration.

This module defines the User model that will be used by FastAPI Users
for authentication and user management.
"""

import uuid
from datetime import datetime

from fastapi_users.db import SQLAlchemyBaseUserTable
from sqlalchemy import Boolean, Column, DateTime, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base

from database import metadata

# Create base class for declarative models
Base = declarative_base(metadata=metadata)


class User(SQLAlchemyBaseUserTable[uuid.UUID], Base):
    """
    User model for FastAPI Users.

    Extends SQLAlchemyBaseUserTable to provide all necessary fields
    for FastAPI Users authentication system.
    """

    __tablename__ = "users"

    # Primary key - UUID
    user_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    # User authentication fields
    email = Column(String(length=255), unique=True, nullable=False, index=True)
    hashed_password = Column(String(length=255), nullable=False)

    # User status fields
    is_active = Column(Boolean(), default=True, nullable=False)
    is_superuser = Column(Boolean(), default=False, nullable=False)

    # Timestamps
    created_at = Column(DateTime(), default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime(), default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    def __repr__(self) -> str:
        """String representation of the user."""
        return f"<User(user_id={self.user_id}, email={self.email}, is_active={self.is_active})>"

    @property
    def is_authenticated(self) -> bool:
        """Check if user is authenticated."""
        return self.is_active

    def get_display_name(self) -> str:
        """Get display name for the user."""
        return self.email.split("@")[0] if self.email else str(self.user_id)
