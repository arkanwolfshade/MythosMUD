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

    # ForeignKey
    # User -> Player (one-to-one)
    User.player = User.__table__.c.get("player", None)
    if not User.player:
        User.player = relationship("Player", back_populates="user", uselist=False)

    # User -> Invite (one-to-one for used invite)
    User.used_invite = User.__table__.c.get("used_invite", None)
    if not User.used_invite:
        User.used_invite = relationship(
            "Invite", primaryjoin="Invite.used_by_user_id == User.id", back_populates="user", uselist=False
        )

    # Player -> User (many-to-one)
    Player.user = Player.__table__.c.get("user", None)
    if not Player.user:
        Player.user = relationship("User", back_populates="player", lazy="joined")

    # Invite -> User (many-to-one for user)
    Invite.user = Invite.__table__.c.get("user", None)
    if not Invite.user:
        Invite.user = relationship(
            "User", primaryjoin="Invite.used_by_user_id == User.id", back_populates="used_invite"
        )
