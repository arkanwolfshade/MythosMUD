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

    # Set up relationships without back_populates to avoid circular references
    # User -> Player (one-to-one)
    if not hasattr(User, "player") or User.player is None:
        User.player = relationship(Player, uselist=False)

    # User -> Invite (one-to-many for created invites)
    if not hasattr(User, "created_invites") or User.created_invites is None:
        User.created_invites = relationship(
            Invite,
            foreign_keys=[Invite.created_by_user_id],
        )

    # User -> Invite (one-to-one for used invite)
    if not hasattr(User, "used_invite") or User.used_invite is None:
        User.used_invite = relationship(
            Invite,
            uselist=False,
            foreign_keys=[Invite.used_by_user_id],
        )

    # Player -> User (many-to-one)
    if not hasattr(Player, "user") or Player.user is None:
        Player.user = relationship(User, lazy="joined", overlaps="player")

    # Invite -> User (many-to-one for created_by_user)
    if not hasattr(Invite, "created_by_user") or Invite.created_by_user is None:
        Invite.created_by_user = relationship(
            User, foreign_keys=[Invite.created_by_user_id], overlaps="created_invites"
        )

    # Invite -> User (many-to-one for used_by_user)
    if not hasattr(Invite, "used_by_user") or Invite.used_by_user is None:
        Invite.used_by_user = relationship(User, foreign_keys=[Invite.used_by_user_id], overlaps="used_invite")

    # Configure mappers to ensure all relationships are properly set up
    from sqlalchemy.orm import configure_mappers

    configure_mappers()
