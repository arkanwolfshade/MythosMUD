"""
Invite model for custom invite system.

This module defines the Invite model that handles the invite-only
registration system for MythosMUD.
"""

import uuid
from datetime import datetime

from sqlalchemy import Boolean, Column, DateTime, ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base

from ..metadata import metadata

Base = declarative_base(metadata=metadata)


class Invite(Base):
    """
    Invite model for invite-only registration.

    Stores invite codes and tracks their usage for the
    invite-only registration system.
    """

    __tablename__ = "invites"
    __table_args__ = {"extend_existing": True}

    # Primary key - UUID
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    # Invite code (unique identifier)
    invite_code = Column(String(length=50), unique=True, nullable=False, index=True)

    # Foreign key to users table
    used_by_user_id = Column(UUID(as_uuid=True), ForeignKey("users.user_id"), nullable=True)

    # Invite status
    is_used = Column(Boolean(), default=False, nullable=False)

    # Timestamps
    expires_at = Column(DateTime(), nullable=True)
    created_at = Column(DateTime(), default=datetime.utcnow, nullable=False)

    def __repr__(self) -> str:
        """String representation of the invite."""
        return f"<Invite(id={self.id}, code={self.invite_code}, is_used={self.is_used})>"

    def is_valid(self) -> bool:
        """Check if invite is still valid."""
        if self.is_used:
            return False

        if self.expires_at and datetime.utcnow() > self.expires_at:
            return False

        return True

    def use_invite(self, user_id: uuid.UUID) -> None:
        """Mark invite as used by a specific user."""
        self.is_used = True
        self.used_by_user_id = user_id

    def get_display_code(self) -> str:
        """Get formatted invite code for display."""
        return f"{self.invite_code[:4]}-{self.invite_code[4:8]}-{self.invite_code[8:]}"

    @classmethod
    def generate_code(cls) -> str:
        """Generate a new invite code."""
        return str(uuid.uuid4()).replace("-", "")[:12].upper()
