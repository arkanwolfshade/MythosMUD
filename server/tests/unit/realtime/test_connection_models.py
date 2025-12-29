"""
Unit tests for connection models.

Tests the connection_models module classes.
"""

import time
import uuid

import pytest

from server.realtime.connection_models import ConnectionMetadata


def test_connection_metadata_init():
    """Test ConnectionMetadata.__init__() creates metadata with required fields."""
    connection_id = "conn_123"
    player_id = uuid.uuid4()
    current_time = time.time()

    metadata = ConnectionMetadata(
        connection_id=connection_id,
        player_id=player_id,
        connection_type="websocket",
        established_at=current_time,
        last_seen=current_time,
        is_healthy=True,
    )

    assert metadata.connection_id == connection_id
    assert metadata.player_id == player_id
    assert metadata.connection_type == "websocket"
    assert metadata.established_at == current_time
    assert metadata.last_seen == current_time
    assert metadata.is_healthy is True
    assert metadata.session_id is None
    assert metadata.token is None
    assert metadata.last_token_validation is None


def test_connection_metadata_with_optional_fields():
    """Test ConnectionMetadata.__init__() with optional fields."""
    connection_id = "conn_123"
    player_id = uuid.uuid4()
    current_time = time.time()
    session_id = "session_123"
    token = "jwt_token"

    metadata = ConnectionMetadata(
        connection_id=connection_id,
        player_id=player_id,
        connection_type="websocket",
        established_at=current_time,
        last_seen=current_time,
        is_healthy=True,
        session_id=session_id,
        token=token,
        last_token_validation=current_time,
    )

    assert metadata.session_id == session_id
    assert metadata.token == token
    assert metadata.last_token_validation == current_time


def test_connection_metadata_dataclass_fields():
    """Test ConnectionMetadata has all expected dataclass fields."""
    connection_id = "conn_123"
    player_id = uuid.uuid4()
    current_time = time.time()

    metadata = ConnectionMetadata(
        connection_id=connection_id,
        player_id=player_id,
        connection_type="websocket",
        established_at=current_time,
        last_seen=current_time,
        is_healthy=False,
    )

    # Verify all fields are accessible
    assert hasattr(metadata, "connection_id")
    assert hasattr(metadata, "player_id")
    assert hasattr(metadata, "connection_type")
    assert hasattr(metadata, "established_at")
    assert hasattr(metadata, "last_seen")
    assert hasattr(metadata, "is_healthy")
    assert hasattr(metadata, "session_id")
    assert hasattr(metadata, "token")
    assert hasattr(metadata, "last_token_validation")


def test_connection_metadata_equality():
    """Test ConnectionMetadata equality comparison."""
    connection_id = "conn_123"
    player_id = uuid.uuid4()
    current_time = time.time()

    metadata1 = ConnectionMetadata(
        connection_id=connection_id,
        player_id=player_id,
        connection_type="websocket",
        established_at=current_time,
        last_seen=current_time,
        is_healthy=True,
    )

    metadata2 = ConnectionMetadata(
        connection_id=connection_id,
        player_id=player_id,
        connection_type="websocket",
        established_at=current_time,
        last_seen=current_time,
        is_healthy=True,
    )

    assert metadata1 == metadata2


def test_connection_metadata_inequality():
    """Test ConnectionMetadata inequality comparison."""
    connection_id = "conn_123"
    player_id = uuid.uuid4()
    current_time = time.time()

    metadata1 = ConnectionMetadata(
        connection_id=connection_id,
        player_id=player_id,
        connection_type="websocket",
        established_at=current_time,
        last_seen=current_time,
        is_healthy=True,
    )

    metadata2 = ConnectionMetadata(
        connection_id="conn_456",
        player_id=player_id,
        connection_type="websocket",
        established_at=current_time,
        last_seen=current_time,
        is_healthy=True,
    )

    assert metadata1 != metadata2
