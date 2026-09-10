"""
Unit tests for the in-memory fake whisper sender registry (#625, #714).

This registry is what lets `reply` answer in-fiction instead of leaking "player not found" the
moment someone reacts naturally to a fake NPC whisper -- see
communication_commands_flows._deliver_reply_to_last_whisper.
"""

import uuid

from server.services.fake_sender_registry import FakeSenderRegistry


def test_get_last_fake_sender_is_none_for_unrecorded_player():
    """A player with no fake whisper history has no recorded sender."""
    registry = FakeSenderRegistry()
    assert registry.get_last_fake_sender(uuid.uuid4()) is None


def test_record_then_get_last_fake_sender():
    """The most recently recorded fake NPC name is returned."""
    registry = FakeSenderRegistry()
    player_id = uuid.uuid4()
    registry.record_fake_whisper(player_id, "The Whisperer")
    assert registry.get_last_fake_sender(player_id) == "The Whisperer"


def test_record_fake_whisper_overwrites_the_previous_sender():
    """Only the most recent fake sender is tracked -- no history list."""
    registry = FakeSenderRegistry()
    player_id = uuid.uuid4()
    registry.record_fake_whisper(player_id, "The Whisperer")
    registry.record_fake_whisper(player_id, "Echo of the Depths")
    assert registry.get_last_fake_sender(player_id) == "Echo of the Depths"


def test_record_fake_whisper_accepts_str_or_uuid_for_the_same_player():
    """A UUID and its string form must key into the same registry entry."""
    registry = FakeSenderRegistry()
    player_id = uuid.uuid4()
    registry.record_fake_whisper(player_id, "The Whisperer")
    assert registry.get_last_fake_sender(str(player_id)) == "The Whisperer"


def test_clear_removes_the_recorded_sender():
    """clear() drops the entry entirely -- reply falls through to the real whisper tracker."""
    registry = FakeSenderRegistry()
    player_id = uuid.uuid4()
    registry.record_fake_whisper(player_id, "The Whisperer")
    registry.clear(player_id)
    assert registry.get_last_fake_sender(player_id) is None


def test_clear_on_unrecorded_player_does_not_raise():
    """Clearing a player with no entry is a safe no-op."""
    registry = FakeSenderRegistry()
    registry.clear(uuid.uuid4())
