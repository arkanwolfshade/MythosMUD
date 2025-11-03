"""
Invite model for MythosMUD.

This module defines the Invite model for managing user registration invites.
Invites are used to control access to the MUD, ensuring only invited users
can create accounts.
"""

import uuid
from datetime import UTC, datetime, timedelta
from typing import TYPE_CHECKING

from sqlalchemy import Boolean, Column, DateTime, ForeignKey, String
from sqlalchemy.orm import DeclarativeBase, Mapped, relationship

from ..metadata import metadata

# Forward references for relationships (resolves circular imports)
if TYPE_CHECKING:
    from .user import User


class Base(DeclarativeBase):
    metadata = metadata


class Invite(Base):
    """Model for user registration invites."""

    __tablename__ = "invites"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    invite_code = Column(String, unique=True, nullable=False, index=True)
    created_by_user_id = Column(String, ForeignKey("users.id"), nullable=True)
    used_by_user_id = Column(String, ForeignKey("users.id"), nullable=True)
    used = Column(Boolean, default=False, nullable=False)
    expires_at = Column(DateTime, nullable=False)
    # Store datetimes in database as naive UTC to keep SQLite comparisons simple.
    created_at = Column(DateTime, default=lambda: datetime.now(UTC).replace(tzinfo=None), nullable=False)

    # ARCHITECTURE FIX Phase 3.1: Relationships defined directly in model (no circular imports)
    # Using string references to avoid circular imports
    created_by_user: Mapped["User | None"] = relationship(
        "User", foreign_keys=[created_by_user_id], back_populates="created_invites"
    )
    used_by_user: Mapped["User | None"] = relationship(
        "User", foreign_keys=[used_by_user_id], back_populates="used_invite"
    )

    def __repr__(self) -> str:
        return f"<Invite(id='{self.id}', code='{self.invite_code}', used={self.used})>"

    def is_expired(self) -> bool:
        """Check if the invite has expired. Handles naive timestamps as UTC."""
        now_utc = datetime.now(UTC)
        expires_at_utc = (
            self.expires_at
            if getattr(self.expires_at, "tzinfo", None) is not None
            else self.expires_at.replace(tzinfo=UTC)
        )
        return bool(now_utc > expires_at_utc)

    def is_valid(self) -> bool:
        """Check if the invite is valid (not used and not expired)."""
        return not self.used and not self.is_expired()

    def use_invite(self, user_id: str) -> None:
        """Mark this invite as used by a specific user."""
        self.used = True  # type: ignore[assignment]
        self.used_by_user_id = user_id  # type: ignore[assignment]

    @classmethod
    def create_invite(cls, created_by_user_id: str | None = None, expires_in_days: int = 30) -> "Invite":
        """Create a new invite with the specified parameters."""
        return cls(
            invite_code=cls._generate_invite_code(),
            created_by_user_id=created_by_user_id,
            # Persist naive UTC in DB
            expires_at=(datetime.now(UTC) + timedelta(days=expires_in_days)).replace(tzinfo=None),
        )

    @staticmethod
    def _generate_invite_code() -> str:
        """Generate a unique invite code."""
        # Generate a 12-character alphanumeric code
        import secrets
        import string

        alphabet = string.ascii_uppercase + string.digits
        return "".join(secrets.choice(alphabet) for _ in range(12))
