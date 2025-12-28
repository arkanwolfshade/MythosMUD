"""
Unit tests for metadata modules.

Tests the shared SQLAlchemy metadata instances.
"""

from sqlalchemy import MetaData

from server.metadata import metadata
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
