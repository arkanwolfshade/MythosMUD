"""
Shared SQLAlchemy DeclarativeBase for all models.

This module provides a single shared Base class that all models must use
to ensure SQLAlchemy can resolve relationships across models.

CRITICAL: All models MUST use this shared Base class, not their own.
         Otherwise SQLAlchemy cannot resolve string references in relationships.
"""

from sqlalchemy.orm import DeclarativeBase

from ..metadata import metadata


class Base(DeclarativeBase):
    """
    Shared declarative base for all MythosMUD models.

    All models (User, Player, Invite, etc.) must inherit from this Base
    so SQLAlchemy can resolve cross-model relationships via string references.

    AI: This fixes the "failed to locate a name" error by ensuring all models
        are registered in the same SQLAlchemy registry.
    """

    metadata = metadata
