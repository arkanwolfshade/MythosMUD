"""
Unit tests for Windows-safe log rotation handlers.

Tests the WindowsSafeRotatingFileHandler and WindowsSafeTimedRotatingFileHandler classes.
"""

import os
from pathlib import Path
from unittest.mock import patch

import pytest

from server.structured_logging.windows_safe_rotation import (
    WindowsSafeRotatingFileHandler,
    WindowsSafeTimedRotatingFileHandler,
    _copy_then_truncate,
)


@pytest.fixture
def temp_log_file(tmp_path):
    """Create a temporary log file for testing."""
    log_file = tmp_path / "test.log"
    log_file.write_text("test log content\n")
    return str(log_file)


@pytest.fixture
def temp_log_dir(tmp_path):
    """Create a temporary directory for log files."""
    return str(tmp_path)


def test_copy_then_truncate_success(temp_log_file, tmp_path):
    """Test _copy_then_truncate() successfully copies and truncates."""
    dest_file = str(tmp_path / "test.log.1")
    _copy_then_truncate(temp_log_file, dest_file)
    assert Path(dest_file).exists()
    assert Path(dest_file).read_text() == "test log content\n"
    assert Path(temp_log_file).read_text() == ""


def test_copy_then_truncate_creates_directory(tmp_path):
    """Test _copy_then_truncate() creates destination directory if needed."""
    src_file = tmp_path / "test.log"
    src_file.write_text("test content\n")
    dest_dir = tmp_path / "subdir"
    dest_file = str(dest_dir / "test.log.1")
    _copy_then_truncate(str(src_file), dest_file)
    assert dest_dir.exists()
    assert Path(dest_file).exists()


def test_copy_then_truncate_retries_on_failure(tmp_path):
    """Test _copy_then_truncate() retries on transient failures."""
    src_file = tmp_path / "test.log"
    src_file.write_text("test content\n")
    dest_file = str(tmp_path / "test.log.1")

    call_count = 0

    def failing_copy2(src, dst):
        nonlocal call_count
        call_count += 1
        if call_count < 2:
            raise OSError("File locked")
        shutil_copy2(src, dst)

    import shutil

    shutil_copy2 = shutil.copy2
    with patch("shutil.copy2", side_effect=failing_copy2):
        _copy_then_truncate(str(src_file), dest_file)
    assert Path(dest_file).exists()
    assert call_count >= 2


def test_copy_then_truncate_raises_after_retries(tmp_path):
    """Test _copy_then_truncate() raises exception after all retries fail."""
    src_file = tmp_path / "test.log"
    src_file.write_text("test content\n")
    dest_file = str(tmp_path / "test.log.1")

    with patch("shutil.copy2", side_effect=OSError("Persistent error")):
        with pytest.raises(OSError, match="Persistent error"):
            _copy_then_truncate(str(src_file), dest_file)


def test_windows_safe_rotating_file_handler_init(temp_log_dir):
    """Test WindowsSafeRotatingFileHandler initialization."""
    log_file = os.path.join(temp_log_dir, "test.log")
    handler = WindowsSafeRotatingFileHandler(log_file, maxBytes=1024, backupCount=3)
    assert handler.baseFilename == log_file
    assert handler.maxBytes == 1024
    assert handler.backupCount == 3
    handler.close()


def test_windows_safe_rotating_file_handler_do_rollover_no_backup(temp_log_dir):
    """Test doRollover() when backupCount is 0."""
    log_file = os.path.join(temp_log_dir, "test.log")
    handler = WindowsSafeRotatingFileHandler(log_file, maxBytes=10, backupCount=0)
    handler.stream = open(log_file, "w", encoding="utf-8")
    handler.stream.write("test content")
    handler.stream.flush()
    handler.doRollover()
    # Should not create backup files
    assert not Path(f"{log_file}.1").exists()
    handler.close()


def test_windows_safe_rotating_file_handler_do_rollover_with_backup(temp_log_dir):
    """Test doRollover() creates backup files."""
    log_file = os.path.join(temp_log_dir, "test.log")
    handler = WindowsSafeRotatingFileHandler(log_file, maxBytes=10, backupCount=2)
    handler.stream = open(log_file, "w", encoding="utf-8")
    handler.stream.write("test content")
    handler.stream.flush()
    handler.doRollover()
    # Should create backup file
    assert Path(f"{log_file}.1").exists()
    handler.close()


def test_windows_safe_rotating_file_handler_do_rollover_rotates_existing_backups(temp_log_dir):
    """Test doRollover() rotates existing backup files."""
    log_file = os.path.join(temp_log_dir, "test.log")
    backup1 = Path(f"{log_file}.1")
    backup1.write_text("old backup 1")
    handler = WindowsSafeRotatingFileHandler(log_file, maxBytes=10, backupCount=2)
    handler.stream = open(log_file, "w", encoding="utf-8")
    handler.stream.write("new content")
    handler.stream.flush()
    handler.doRollover()
    # Should rotate existing backup
    assert Path(f"{log_file}.2").exists()
    handler.close()


def test_windows_safe_rotating_file_handler_do_rollover_handles_os_error(temp_log_dir):
    """Test doRollover() handles OSError during rotation gracefully."""
    log_file = os.path.join(temp_log_dir, "test.log")
    handler = WindowsSafeRotatingFileHandler(log_file, maxBytes=10, backupCount=2)
    handler.stream = open(log_file, "w", encoding="utf-8")
    handler.stream.write("test content")
    handler.stream.flush()

    with patch("os.rename", side_effect=OSError("Permission denied")):
        # Should not raise, should fall back to copy-then-truncate
        handler.doRollover()
    handler.close()


def test_windows_safe_rotating_file_handler_do_rollover_windows_platform(temp_log_dir):
    """Test doRollover() uses copy-then-truncate on Windows."""
    log_file = os.path.join(temp_log_dir, "test.log")
    handler = WindowsSafeRotatingFileHandler(log_file, maxBytes=10, backupCount=1)
    handler.stream = open(log_file, "w", encoding="utf-8")
    handler.stream.write("test content")
    handler.stream.flush()

    with patch("sys.platform", "win32"):
        with patch("server.structured_logging.windows_safe_rotation._copy_then_truncate") as mock_copy:
            handler.doRollover()
            mock_copy.assert_called_once()
    handler.close()


def test_windows_safe_rotating_file_handler_do_rollover_non_windows_platform(temp_log_dir):
    """Test doRollover() uses rename on non-Windows platforms."""
    log_file = os.path.join(temp_log_dir, "test.log")
    handler = WindowsSafeRotatingFileHandler(log_file, maxBytes=10, backupCount=1)
    handler.stream = open(log_file, "w", encoding="utf-8")
    handler.stream.write("test content")
    handler.stream.flush()

    with patch("sys.platform", "linux"):
        with patch("os.rename") as mock_rename:
            handler.doRollover()
            mock_rename.assert_called()
    handler.close()


def test_windows_safe_rotating_file_handler_do_rollover_no_stream(temp_log_dir):
    """Test doRollover() handles case when stream is None."""
    log_file = os.path.join(temp_log_dir, "test.log")
    handler = WindowsSafeRotatingFileHandler(log_file, maxBytes=10, backupCount=1)
    handler.stream = None
    handler.doRollover()
    # Should not raise
    handler.close()


def test_windows_safe_timed_rotating_file_handler_init(temp_log_dir):
    """Test WindowsSafeTimedRotatingFileHandler initialization."""
    log_file = os.path.join(temp_log_dir, "test.log")
    handler = WindowsSafeTimedRotatingFileHandler(log_file, when="midnight", interval=1, backupCount=5)
    assert handler.baseFilename == log_file
    assert handler.backupCount == 5
    handler.close()


def test_windows_safe_timed_rotating_file_handler_rotation_filename(temp_log_dir):
    """Test rotation_filename() returns default name."""
    log_file = os.path.join(temp_log_dir, "test.log")
    handler = WindowsSafeTimedRotatingFileHandler(log_file)
    result = handler.rotation_filename("test.log.2024-01-01")
    assert result == "test.log.2024-01-01"
    handler.close()


def test_windows_safe_timed_rotating_file_handler_rotate_windows_platform(temp_log_dir):
    """Test rotate() uses copy-then-truncate on Windows."""
    log_file = os.path.join(temp_log_dir, "test.log")
    handler = WindowsSafeTimedRotatingFileHandler(log_file)
    Path(log_file).write_text("test content")

    with patch("sys.platform", "win32"):
        with patch("server.structured_logging.windows_safe_rotation._copy_then_truncate") as mock_copy:
            handler.rotate(log_file, f"{log_file}.2024-01-01")
            mock_copy.assert_called_once()
    handler.close()


def test_windows_safe_timed_rotating_file_handler_rotate_non_windows_platform(temp_log_dir):
    """Test rotate() uses rename on non-Windows platforms."""
    log_file = os.path.join(temp_log_dir, "test.log")
    handler = WindowsSafeTimedRotatingFileHandler(log_file)
    Path(log_file).write_text("test content")

    with patch("sys.platform", "linux"):
        with patch("os.rename") as mock_rename:
            handler.rotate(log_file, f"{log_file}.2024-01-01")
            mock_rename.assert_called_once()
    handler.close()


def test_windows_safe_timed_rotating_file_handler_rotate_fallback_on_error(temp_log_dir):
    """Test rotate() falls back to copy-then-truncate on OSError."""
    log_file = os.path.join(temp_log_dir, "test.log")
    handler = WindowsSafeTimedRotatingFileHandler(log_file)
    Path(log_file).write_text("test content")

    with patch("sys.platform", "linux"):
        with patch("os.rename", side_effect=OSError("Permission denied")):
            with patch("server.structured_logging.windows_safe_rotation._copy_then_truncate") as mock_copy:
                handler.rotate(log_file, f"{log_file}.2024-01-01")
                mock_copy.assert_called_once()
    handler.close()
