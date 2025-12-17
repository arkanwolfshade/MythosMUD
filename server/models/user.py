"""
User model for FastAPI Users integration.

This module defines the User model that will be used by FastAPI Users
for authentication and user management.

TYPING NOTE: Uses SQLAlchemy 2.0 Mapped[] annotations for proper mypy support.
The base class fields (email, hashed_password) use legacy Column() but we type
our custom fields with Mapped[] for better type safety.
"""

from datetime import UTC, datetime
from typing import TYPE_CHECKING

from fastapi_users.db import SQLAlchemyBaseUserTableUUID
from sqlalchemy import Boolean, DateTime, String, event
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base  # ARCHITECTURE FIX Phase 3.1: Use shared Base

# Forward references for type checking (resolves circular imports)
# Note: SQLAlchemy will resolve string references via registry at runtime
if TYPE_CHECKING:
    from .invite import Invite
    from .player import Player


class User(SQLAlchemyBaseUserTableUUID, Base):
    """
    User model for FastAPI Users v14+ with SQLAlchemy 2.0 typing.

    Extends SQLAlchemyBaseUserTableUUID to provide all necessary fields
    for FastAPI Users authentication system with UUID primary keys.

    Uses Mapped[] type annotations for proper mypy support and IDE autocomplete.
    """

    __tablename__ = "users"
    __table_args__ = {"extend_existing": True}

    # Use standard SQLAlchemy UUID primary key - let SQLAlchemy handle the UUID generation
    # The base class SQLAlchemyBaseUserTableUUID already provides the proper UUID handling

    # User authentication fields (email and hashed_password are inherited from base)
    # MULTI-CHARACTER: Removed unique=True - uniqueness enforced by case-insensitive unique index
    # in database (idx_users_username_lower_unique) for case-insensitive uniqueness
    # Using Mapped[] with mapped_column for SQLAlchemy 2.0 type safety
    username: Mapped[str] = mapped_column(String(length=255), nullable=False, index=True)

    # Display name - defaults to username if not provided
    # Note: We'll set this explicitly in registration, but provide a default for safety
    display_name: Mapped[str] = mapped_column(String(length=255), nullable=False, server_default="")

    # Legacy password hash field (nullable, separate from hashed_password used by FastAPI Users)
    password_hash: Mapped[str | None] = mapped_column(String(length=255), nullable=True)

    # Admin flag (separate from is_superuser)
    is_admin: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)

    # User status fields (is_active, is_superuser, is_verified are inherited from base)

    # Timestamps (persist naive UTC)
    # Using Mapped[] with Column for compatibility with existing schema
    created_at: Mapped[datetime] = mapped_column(
        DateTime(), default=lambda: datetime.now(UTC).replace(tzinfo=None), nullable=False
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(),
        default=lambda: datetime.now(UTC).replace(tzinfo=None),
        onupdate=lambda: datetime.now(UTC).replace(tzinfo=None),
        nullable=False,
    )

    # ARCHITECTURE FIX Phase 3.1: Relationships defined directly in model (no circular imports)
    # MULTI-CHARACTER: Changed to one-to-many relationship (uselist=True) to support multiple characters per user
    # Using simple string references - SQLAlchemy resolves via registry after all models imported
    players: Mapped[list["Player"]] = relationship("Player", uselist=True, back_populates="user", lazy="select")
    created_invites: Mapped[list["Invite"]] = relationship(
        "Invite", foreign_keys="Invite.created_by_user_id", back_populates="created_by_user"
    )
    used_invite: Mapped["Invite | None"] = relationship(
        "Invite", foreign_keys="Invite.used_by_user_id", back_populates="used_by_user", uselist=False
    )

    def __repr__(self) -> str:
        """String representation of the user."""
        return f"<User(id={self.id}, username={self.username}, is_active={self.is_active})>"

    # The id property is already provided by the base class

    @property
    def is_authenticated(self) -> bool:
        """Check if user is authenticated."""
        return bool(self.is_active)

    def get_display_name(self) -> str:
        """Get display name for the user."""
        # Return display_name if set and not empty, otherwise fall back to username
        if hasattr(self, "display_name") and self.display_name:
            return str(self.display_name)
        return str(self.username) if self.username else str(self.id)


# Event listener to ensure display_name defaults to username if not set
# This handles cases where display_name is not explicitly provided during User creation
@event.listens_for(User, "before_insert", propagate=True)
def set_display_name_default(mapper, connection, target):
    """
    Ensure display_name is set to username if not provided or empty.

    This event listener runs before INSERT operations to guarantee that
    display_name always has a value, even if it wasn't explicitly set.
    This is critical for PostgreSQL NOT NULL constraint compliance.
    """
    # If display_name is None, empty string, or not set, use username
    if not target.display_name or target.display_name == "":
        if target.username:
            target.display_name = target.username
        # If username is also not set (shouldn't happen, but safety first)
        elif hasattr(target, "id") and target.id:
            target.display_name = str(target.id)
        else:
            # Last resort: use a placeholder (should never happen in practice)
            target.display_name = "user"
