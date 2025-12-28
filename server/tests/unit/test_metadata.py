"""
Unit tests for metadata modules.

Tests the shared SQLAlchemy metadata instances.
"""

from sqlalchemy import MetaData
from sqlalchemy.orm import DeclarativeBase

from server.metadata import metadata
from server.models.base import Base
from server.npc_metadata import npc_metadata


def test_metadata_is_metadata_instance():
    """Test that metadata is a MetaData instance."""
    assert isinstance(metadata, MetaData)


def test_npc_metadata_is_metadata_instance():
    """Test that npc_metadata is a MetaData instance."""
    assert isinstance(npc_metadata, MetaData)


def test_metadata_and_npc_metadata_are_different():
    """Test that metadata and npc_metadata are separate instances."""
    assert metadata is not npc_metadata


def test_base_is_declarative_base():
    """Test that Base is a DeclarativeBase subclass."""
    assert issubclass(Base, DeclarativeBase)


def test_base_has_metadata():
    """Test that Base has metadata attribute set to shared metadata."""
    assert hasattr(Base, "metadata")
    assert Base.metadata is metadata


def test_base_can_be_instantiated():
    """Test that Base can be instantiated (though meant to be subclassed)."""
    # Base is a DeclarativeBase, so it can be instantiated
    base = Base()
    assert isinstance(base, Base)
    assert isinstance(base, DeclarativeBase)
