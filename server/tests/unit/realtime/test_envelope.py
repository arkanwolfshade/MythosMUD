"""
Unit tests for envelope utilities.

Tests the build_event function, UUIDEncoder, and related utilities.
"""

import json
import threading
import uuid
from datetime import UTC, datetime

import pytest

from server.realtime.envelope import UUIDEncoder, build_event, utc_now_z

# pylint: disable=protected-access  # Reason: Test file - accessing protected members is standard practice for unit testing
# pylint: disable=redefined-outer-name  # Reason: Test file - pytest fixture parameter names must match fixture names, causing intentional redefinitions


def test_uuid_encoder_handles_uuid():
    """Test UUIDEncoder handles UUID objects."""
    encoder = UUIDEncoder()
    test_uuid = uuid.uuid4()
    result = encoder.default(test_uuid)
    assert result == str(test_uuid)
    assert isinstance(result, str)


def test_uuid_encoder_handles_other_types():
    """Test UUIDEncoder falls back to default for non-UUID types."""
    encoder = UUIDEncoder()
    # Should raise TypeError for types it can't handle
    with pytest.raises(TypeError):
        encoder.default(object())


def test_uuid_encoder_json_dumps():
    """Test UUIDEncoder works with json.dumps()."""
    test_uuid = uuid.uuid4()
    data = {"id": test_uuid, "name": "test"}
    result = json.dumps(data, cls=UUIDEncoder)
    parsed = json.loads(result)
    assert parsed["id"] == str(test_uuid)
    assert parsed["name"] == "test"


def test_utc_now_z_format():
    """Test utc_now_z() returns ISO 8601 format with Z suffix."""
    result = utc_now_z()
    assert result.endswith("Z")
    # Should be valid ISO format
    parsed = datetime.fromisoformat(result.replace("Z", "+00:00"))
    assert parsed.tzinfo is not None


def test_utc_now_z_is_utc():
    """Test utc_now_z() returns UTC time."""
    result = utc_now_z()
    parsed = datetime.fromisoformat(result.replace("Z", "+00:00"))
    assert parsed.tzinfo == UTC


def test_build_event_basic():
    """Test build_event() creates basic event."""
    event = build_event("test.event", {"key": "value"})
    assert event["event_type"] == "test.event"
    assert event["data"] == {"key": "value"}
    assert "timestamp" in event
    assert "sequence_number" in event
    assert isinstance(event["sequence_number"], int)


def test_build_event_with_room_id():
    """Test build_event() includes room_id when provided."""
    event = build_event("test.event", room_id="room-123")
    assert event["room_id"] == "room-123"


def test_build_event_with_player_id_uuid():
    """Test build_event() includes player_id when provided as UUID."""
    player_id = uuid.uuid4()
    event = build_event("test.event", player_id=player_id)
    assert event["player_id"] == player_id
    assert isinstance(event["player_id"], uuid.UUID)


def test_build_event_with_player_id_string():
    """Test build_event() includes player_id when provided as string."""
    player_id_str = str(uuid.uuid4())
    event = build_event("test.event", player_id=player_id_str)
    assert event["player_id"] == player_id_str
    assert isinstance(event["player_id"], str)


def test_build_event_with_sequence_number():
    """Test build_event() uses provided sequence_number."""
    event = build_event("test.event", sequence_number=42)
    assert event["sequence_number"] == 42


def test_build_event_with_connection_manager():
    """Test build_event() uses connection_manager for sequence."""
    mock_connection_manager = type("MockCM", (), {"_get_next_sequence": lambda self: 100})()
    event = build_event("test.event", connection_manager=mock_connection_manager)
    assert event["sequence_number"] == 100


def test_build_event_uses_global_sequence_when_no_manager():
    """Test build_event() uses global sequence when no connection_manager."""
    # Reset global counter by importing fresh
    import server.realtime.envelope as envelope_module

    envelope_module._global_sequence_counter = 0
    event1 = build_event("test.event1")
    event2 = build_event("test.event2")
    assert event2["sequence_number"] > event1["sequence_number"]


def test_build_event_sequence_priority():
    """Test build_event() prioritizes explicit sequence_number over connection_manager."""
    mock_connection_manager = type("MockCM", (), {"_get_next_sequence": lambda self: 100})()
    event = build_event("test.event", sequence_number=42, connection_manager=mock_connection_manager)
    assert event["sequence_number"] == 42


def test_build_event_empty_data():
    """Test build_event() handles None data."""
    event = build_event("test.event", data=None)
    assert event["data"] == {}


def test_build_event_no_data_parameter():
    """Test build_event() handles missing data parameter."""
    event = build_event("test.event")
    assert event["data"] == {}


def test_build_event_timestamp_format():
    """Test build_event() includes properly formatted timestamp."""
    event = build_event("test.event")
    timestamp = event["timestamp"]
    assert timestamp.endswith("Z")
    # Should be parseable
    parsed = datetime.fromisoformat(timestamp.replace("Z", "+00:00"))
    assert parsed.tzinfo is not None


def test_build_event_all_parameters():
    """Test build_event() with all parameters."""
    player_id = uuid.uuid4()
    event = build_event(
        "test.event",
        data={"key": "value"},
        room_id="room-123",
        player_id=player_id,
        sequence_number=42,
    )
    assert event["event_type"] == "test.event"
    assert event["data"] == {"key": "value"}
    assert event["room_id"] == "room-123"
    assert event["player_id"] == player_id
    assert event["sequence_number"] == 42
    assert "timestamp" in event


def test_build_event_optional_parameters_none():
    """Test build_event() handles None for optional parameters."""
    event = build_event("test.event", room_id=None, player_id=None)
    assert "room_id" not in event
    assert "player_id" not in event


def test_get_next_global_sequence_thread_safe():
    """Test _get_next_global_sequence() is thread-safe."""
    import server.realtime.envelope as envelope_module

    # Reset counter
    envelope_module._global_sequence_counter = 0
    envelope_module._sequence_lock = None

    results: list[int] = []
    errors: list[RuntimeError | AttributeError | OSError] = []

    def get_sequence():
        try:
            results.append(envelope_module._get_next_global_sequence())
        except (RuntimeError, AttributeError, OSError) as e:
            # Reason: Threading operations can raise RuntimeError (threading issues),
            # AttributeError (missing lock/attributes), or OSError (system-level issues)
            errors.append(e)

    # Create multiple threads
    threads = [threading.Thread(target=get_sequence) for _ in range(10)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()

    # Should have no errors
    assert len(errors) == 0
    # Should have 10 results
    assert len(results) == 10
    # All should be unique
    assert len(set(results)) == 10
    # Should be sequential
    assert sorted(results) == list(range(1, 11))


def test_build_event_json_serializable():
    """Test build_event() produces JSON-serializable output."""
    player_id = uuid.uuid4()
    event = build_event("test.event", data={"key": "value"}, player_id=player_id)
    # Should be able to serialize with UUIDEncoder
    json_str = json.dumps(event, cls=UUIDEncoder)
    parsed = json.loads(json_str)
    assert parsed["event_type"] == "test.event"
    assert parsed["data"] == {"key": "value"}
    assert parsed["player_id"] == str(player_id)
