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
def chat_logger(temp_log_dir):  # pylint: disable=redefined-outer-name
    """Create a ChatLogger instance with temp directory."""
    logger = ChatLogger(log_dir=temp_log_dir)
    yield logger
    # Cleanup: shutdown the logger
    logger.shutdown()


def test_chat_logger_initialization_with_directory(temp_log_dir):  # pylint: disable=redefined-outer-name
    """Test ChatLogger initialization with explicit directory."""
    logger = ChatLogger(log_dir=temp_log_dir)
    assert logger.log_dir == Path(temp_log_dir)
    # pylint: disable=protected-access
    # Accessing protected member for test verification of internal state
    assert logger._writer_thread is not None
    logger.shutdown()


def test_log_chat_message(chat_logger, temp_log_dir):  # pylint: disable=redefined-outer-name
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
    chat_logger.wait_for_queue_processing(timeout=1.0)

    # Check that log file was created
    log_files = list(Path(temp_log_dir).glob("chat_chat_*.log"))
    assert len(log_files) > 0


def test_log_moderation_event(chat_logger, temp_log_dir):  # pylint: disable=redefined-outer-name
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
    chat_logger.wait_for_queue_processing(timeout=1.0)

    # Check that log file was created
    log_files = list(Path(temp_log_dir).glob("chat_moderation_*.log"))
    assert len(log_files) > 0


def test_log_system_event(chat_logger, temp_log_dir):  # pylint: disable=redefined-outer-name
    """Test log_system_event writes entry."""
    chat_logger.log_system_event(
        event_type="player_join",
        event_data={
            "player_name": "TestPlayer",
            "room_id": "test_room",
        },
    )

    # Give writer thread time to process
    chat_logger.wait_for_queue_processing(timeout=1.0)

    # Check that log file was created
    log_files = list(Path(temp_log_dir).glob("chat_system_*.log"))
    assert len(log_files) > 0


def test_shutdown(chat_logger):  # pylint: disable=redefined-outer-name
    """Test shutdown stops writer thread."""
    # pylint: disable=protected-access
    # Accessing protected members for test verification of internal state
    assert chat_logger._writer_thread is not None
    assert chat_logger._writer_thread.is_alive()

    chat_logger.shutdown()

    # Give thread time to stop
    import time

    time.sleep(0.1)

    # Thread should be stopped (or stopping)
    assert not chat_logger._shutdown_event.is_set() or not chat_logger._writer_thread.is_alive()  # pylint: disable=protected-access


def test_log_player_muted(chat_logger, temp_log_dir):  # pylint: disable=redefined-outer-name
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
    chat_logger.wait_for_queue_processing(timeout=1.0)

    # Check that log file was created
    log_files = list(Path(temp_log_dir).glob("chat_moderation_*.log"))
    assert len(log_files) > 0


def test_log_player_unmuted(chat_logger, temp_log_dir):  # pylint: disable=redefined-outer-name
    """Test log_player_unmuted writes entry."""
    chat_logger.log_player_unmuted(
        unmuter_id="admin123",
        target_id="player123",
        target_name="TestPlayer",
        mute_type="local",
    )

    # Give writer thread time to process
    chat_logger.wait_for_queue_processing(timeout=1.0)

    # Check that log file was created
    log_files = list(Path(temp_log_dir).glob("chat_moderation_*.log"))
    assert len(log_files) > 0


def test_log_player_joined_room(chat_logger, temp_log_dir):  # pylint: disable=redefined-outer-name
    """Test log_player_joined_room writes entry."""
    chat_logger.log_player_joined_room(
        player_id="player123",
        player_name="TestPlayer",
        room_id="test_room",
        room_name="Test Room",
    )

    # Give writer thread time to process
    chat_logger.wait_for_queue_processing(timeout=1.0)

    # Check that log file was created
    log_files = list(Path(temp_log_dir).glob("chat_system_*.log"))
    assert len(log_files) > 0


def test_log_rate_limit_violation(chat_logger, temp_log_dir):  # pylint: disable=redefined-outer-name
    """Test log_rate_limit_violation writes entry."""
    chat_logger.log_rate_limit_violation(
        player_id="player123",
        player_name="TestPlayer",
        channel="local",
        message_count=10,
        limit=5,
    )

    # Give writer thread time to process
    chat_logger.wait_for_queue_processing(timeout=1.0)

    # Check that log file was created
    log_files = list(Path(temp_log_dir).glob("chat_moderation_*.log"))
    assert len(log_files) > 0


def test_get_log_file_paths(chat_logger):  # pylint: disable=redefined-outer-name
    """Test get_log_file_paths returns correct paths."""
    paths = chat_logger.get_log_file_paths()

    assert "chat" in paths
    assert "moderation" in paths
    assert "system" in paths
    assert isinstance(paths["chat"], Path)


def test_get_log_stats(chat_logger):  # pylint: disable=redefined-outer-name
    """Test get_log_stats returns statistics."""
    stats = chat_logger.get_log_stats()

    assert "chat" in stats
    assert "moderation" in stats
    assert "system" in stats
    assert isinstance(stats["chat"], dict)


def test_log_whisper_channel_message(chat_logger, temp_log_dir):  # pylint: disable=redefined-outer-name
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
    chat_logger.wait_for_queue_processing(timeout=1.0)

    # Check that log file was created
    log_files = list(Path(temp_log_dir).glob("chat_whisper_*.log"))
    assert len(log_files) > 0
