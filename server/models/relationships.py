"""
Model relationships setup.

This module sets up the relationships between models after all models
are defined to avoid circular dependency issues.
"""

from pathlib import Path  # noqa: F401

from sqlalchemy.orm import relationship


def setup_relationships():
    """Set up all model relationships."""

    # Import models here to avoid circular imports
    from .invite import Invite
    from .player import Player
    from .user import User

    # User -> Player (one-to-one)
    if not hasattr(User, "player") or User.player is None:
        User.player = relationship(Player, back_populates="user", uselist=False)

    # User -> Invite (one-to-one for used invite)
    if not hasattr(User, "used_invite") or User.used_invite is None:
        User.used_invite = relationship(
            Invite, primaryjoin="Invite.used_by_user_id == User.user_id", back_populates="user", uselist=False
        )

    # Player -> User (many-to-one)
    if not hasattr(Player, "user") or Player.user is None:
        Player.user = relationship(User, back_populates="player", lazy="joined")

    # Invite -> User (many-to-one for user)
    if not hasattr(Invite, "user") or Invite.user is None:
        Invite.user = relationship(
            User, primaryjoin="Invite.used_by_user_id == User.user_id", back_populates="used_invite"
        )
