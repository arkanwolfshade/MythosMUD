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
from sqlalchemy import DateTime, String
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
    # Using Mapped[] with mapped_column for SQLAlchemy 2.0 type safety
    username: Mapped[str] = mapped_column(String(length=255), unique=True, nullable=False, index=True)

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
    # Using simple string references - SQLAlchemy resolves via registry after all models imported
    player: Mapped["Player"] = relationship("Player", uselist=False, back_populates="user", lazy="joined")
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
        return str(self.username) if self.username else str(self.id)
