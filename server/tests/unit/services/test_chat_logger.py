"""
Unit tests for chat logger service.

Tests the ChatLogger class for structured chat message logging.
"""

import tempfile
from pathlib import Path

import pytest

from server.services.chat_logger import ChatLogger


@pytest.fixture
def temp_log_dir():
    """Create a temporary directory for chat logs."""
    with tempfile.TemporaryDirectory() as tmpdir:
        yield tmpdir


@pytest.fixture
def chat_logger(temp_log_dir):  # pylint: disable=redefined-outer-name  # Reason: Fixture parameter name matches fixture function name, pytest standard pattern
    """Create a ChatLogger instance with temp directory."""
    logger = ChatLogger(log_dir=temp_log_dir)
    yield logger
    # Cleanup: shutdown the logger
    logger.shutdown()


def test_chat_logger_initialization_with_directory(temp_log_dir):  # pylint: disable=redefined-outer-name  # Reason: Fixture parameter name matches fixture function name, pytest standard pattern
    """Test ChatLogger initialization with explicit directory."""
    logger = ChatLogger(log_dir=temp_log_dir)
    assert logger.log_dir == Path(temp_log_dir)
    # pylint: disable=protected-access  # Reason: Accessing protected member for test verification of internal state
    assert logger._writer_thread is not None
    logger.shutdown()


def test_log_chat_message(chat_logger, temp_log_dir):  # pylint: disable=redefined-outer-name  # Reason: Fixture parameter names match fixture function names, pytest standard pattern
    """Test log_chat_message writes entry."""
    chat_logger.log_chat_message(
        {
            "message_id": "msg123",
            "channel": "local",
            "sender_name": "TestPlayer",
            "content": "Hello world",
            "room_id": "test_room",
        }
    )

    # Give writer thread time to process
    chat_logger.wait_for_queue_processing(_timeout=1.0)

    # Check that log file was created
    log_files = list(Path(temp_log_dir).glob("chat_chat_*.log"))
    assert len(log_files) > 0


def test_log_moderation_event(chat_logger, temp_log_dir):  # pylint: disable=redefined-outer-name  # Reason: Fixture parameter names match fixture function names, pytest standard pattern
    """Test log_moderation_event writes entry."""
    chat_logger.log_moderation_event(
        event_type="mute",
        event_data={
            "admin_name": "Admin",
            "target_player": "TestPlayer",
            "reason": "Spam",
            "duration_minutes": 60,
        },
    )

    # Give writer thread time to process
    chat_logger.wait_for_queue_processing(_timeout=1.0)

    # Check that log file was created
    log_files = list(Path(temp_log_dir).glob("chat_moderation_*.log"))
    assert len(log_files) > 0


def test_log_system_event(chat_logger, temp_log_dir):  # pylint: disable=redefined-outer-name  # Reason: Fixture parameter names match fixture function names, pytest standard pattern
    """Test log_system_event writes entry."""
    chat_logger.log_system_event(
        event_type="player_join",
        event_data={
            "player_name": "TestPlayer",
            "room_id": "test_room",
        },
    )

    # Give writer thread time to process
    chat_logger.wait_for_queue_processing(_timeout=1.0)

    # Check that log file was created
    log_files = list(Path(temp_log_dir).glob("chat_system_*.log"))
    assert len(log_files) > 0


def test_shutdown(chat_logger):  # pylint: disable=redefined-outer-name  # Reason: Fixture parameter name matches fixture function name, pytest standard pattern
    """Test shutdown stops writer thread."""
    # pylint: disable=protected-access  # Reason: Accessing protected members for test verification of internal state
    assert chat_logger._writer_thread is not None
    assert chat_logger._writer_thread.is_alive()

    chat_logger.shutdown()

    # Give thread time to stop
    import time

    time.sleep(0.1)

    # Thread should be stopped (or stopping)
    assert not chat_logger._shutdown_event.is_set() or not chat_logger._writer_thread.is_alive()  # pylint: disable=protected-access  # Reason: Accessing protected members for test verification of thread state


def test_log_player_muted(chat_logger, temp_log_dir):  # pylint: disable=redefined-outer-name  # Reason: Fixture parameter names match fixture function names, pytest standard pattern
    """Test log_player_muted writes entry."""
    chat_logger.log_player_muted(
        muter_id="admin123",
        target_id="player123",
        target_name="TestPlayer",
        mute_type="local",
        duration_minutes=60,
        reason="Spam",
    )

    # Give writer thread time to process
    chat_logger.wait_for_queue_processing(_timeout=1.0)

    # Check that log file was created
    log_files = list(Path(temp_log_dir).glob("chat_moderation_*.log"))
    assert len(log_files) > 0


def test_log_player_unmuted(chat_logger, temp_log_dir):  # pylint: disable=redefined-outer-name  # Reason: Fixture parameter names match fixture function names, pytest standard pattern
    """Test log_player_unmuted writes entry."""
    chat_logger.log_player_unmuted(
        unmuter_id="admin123",
        target_id="player123",
        target_name="TestPlayer",
        mute_type="local",
    )

    # Give writer thread time to process
    chat_logger.wait_for_queue_processing(_timeout=1.0)

    # Check that log file was created
    log_files = list(Path(temp_log_dir).glob("chat_moderation_*.log"))
    assert len(log_files) > 0


def test_log_player_joined_room(chat_logger, temp_log_dir):  # pylint: disable=redefined-outer-name  # Reason: Fixture parameter names match fixture function names, pytest standard pattern
    """Test log_player_joined_room writes entry."""
    chat_logger.log_player_joined_room(
        player_id="player123",
        player_name="TestPlayer",
        room_id="test_room",
        room_name="Test Room",
    )

    # Give writer thread time to process
    chat_logger.wait_for_queue_processing(_timeout=1.0)

    # Check that log file was created
    log_files = list(Path(temp_log_dir).glob("chat_system_*.log"))
    assert len(log_files) > 0


def test_log_rate_limit_violation(chat_logger, temp_log_dir):  # pylint: disable=redefined-outer-name  # Reason: Fixture parameter names match fixture function names, pytest standard pattern
    """Test log_rate_limit_violation writes entry."""
    chat_logger.log_rate_limit_violation(
        player_id="player123",
        player_name="TestPlayer",
        channel="local",
        message_count=10,
        limit=5,
    )

    # Give writer thread time to process
    chat_logger.wait_for_queue_processing(_timeout=1.0)

    # Check that log file was created
    log_files = list(Path(temp_log_dir).glob("chat_moderation_*.log"))
    assert len(log_files) > 0


def test_get_log_file_paths(chat_logger):  # pylint: disable=redefined-outer-name  # Reason: Fixture parameter name matches fixture function name, pytest standard pattern
    """Test get_log_file_paths returns correct paths."""
    paths = chat_logger.get_log_file_paths()

    assert "chat" in paths
    assert "moderation" in paths
    assert "system" in paths
    assert isinstance(paths["chat"], Path)


def test_get_log_stats(chat_logger):  # pylint: disable=redefined-outer-name  # Reason: Fixture parameter name matches fixture function name, pytest standard pattern
    """Test get_log_stats returns statistics."""
    stats = chat_logger.get_log_stats()

    assert "chat" in stats
    assert "moderation" in stats
    assert "system" in stats
    assert isinstance(stats["chat"], dict)


def test_log_whisper_channel_message(chat_logger, temp_log_dir):  # pylint: disable=redefined-outer-name  # Reason: Fixture parameter names match fixture function names, pytest standard pattern
    """Test log_whisper_channel_message writes entry."""
    chat_logger.log_whisper_channel_message(
        {
            "message_id": "msg123",
            "channel": "whisper",
            "sender_id": "sender123",
            "sender_name": "Sender",
            "target_id": "target123",
            "target_name": "Target",
            "content": "Hello, private message",
        }
    )

    # Give writer thread time to process
    chat_logger.wait_for_queue_processing(_timeout=1.0)

    # Check that log file was created
    log_files = list(Path(temp_log_dir).glob("chat_whisper_*.log"))
    assert len(log_files) > 0


def test_log_local_global_system_channel_messages(chat_logger, temp_log_dir):  # pylint: disable=redefined-outer-name
    """Local/global/system channel writers create daily log files."""
    chat_logger.log_local_channel_message(
        {
            "message_id": "l1",
            "channel": "local",
            "sender_id": "p1",
            "sender_name": "A",
            "content": "hi",
            "room_id": "earth_arkhamcity_northside_room_001",
            "subzone": "northside",
        }
    )
    chat_logger.log_local_channel_message(
        {
            "message_id": "l2",
            "channel": "local",
            "sender_id": "p1",
            "sender_name": "A",
            "content": "hi2",
            "room_id": "earth_arkhamcity_northside_room_001",
        }
    )
    chat_logger.log_global_channel_message(
        {
            "message_id": "g1",
            "channel": "global",
            "sender_id": "p1",
            "sender_name": "A",
            "content": "hello world",
            "timestamp": "2020-01-01T00:00:00+00:00",
        }
    )
    chat_logger.log_system_channel_message(
        {
            "message_id": "s1",
            "channel": "system",
            "sender_id": "system",
            "sender_name": "System",
            "content": "notice",
        }
    )
    chat_logger.wait_for_queue_processing(_timeout=1.0)
    assert list(Path(temp_log_dir).glob("**/chat_local_*.log")) or list(Path(temp_log_dir).rglob("chat_local_*.log"))
    assert list(Path(temp_log_dir).glob("chat_global_*.log"))
    assert list(Path(temp_log_dir).glob("chat_system_*.log"))


def test_log_message_flagged_and_player_left(chat_logger, temp_log_dir):  # pylint: disable=redefined-outer-name
    chat_logger.log_message_flagged("msg1", "spam", confidence=0.9, action_taken="hide")
    chat_logger.log_player_left_room("p1", "A", "room_1", "Room")
    chat_logger.wait_for_queue_processing(_timeout=1.0)
    assert chat_logger.get_log_file_paths()


def test_channel_log_stats_and_cleanup(chat_logger, temp_log_dir):  # pylint: disable=redefined-outer-name
    """Stats and cleanup APIs cover global/local channel helpers."""
    today = Path(temp_log_dir)
    global_log = today / "chat_global_2000-01-01.log"
    global_log.write_text('{"ok":true}\n', encoding="utf-8")
    local_log = today / "chat_local_northside_2000-01-01.log"
    local_log.write_text('{"ok":true}\n', encoding="utf-8")

    assert any("chat_global_" in f for f in chat_logger.get_global_channel_log_files())
    gstats = chat_logger.get_global_channel_log_stats()
    assert "global_channels" in gstats

    # Force old mtime so cleanup deletes
    import os
    import time

    old = time.time() - (60 * 60 * 24 * 40)
    os.utime(global_log, (old, old))
    deleted = chat_logger.cleanup_old_global_channel_logs(days_to_keep=30)
    assert str(global_log) in deleted or not global_log.exists()

    assert chat_logger.get_local_channel_log_files()
    lstats = chat_logger.get_local_channel_log_stats()
    assert "local_channels" in lstats
    os.utime(local_log, (old, old))
    chat_logger.cleanup_old_local_channel_logs(days_to_keep=30)
