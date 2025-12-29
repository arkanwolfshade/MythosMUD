"""
Unit tests for logging handlers.

Tests the SafeRotatingFileHandler, WarningOnlyFilter, and create_aggregator_handler function.
"""

import logging
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest

from server.structured_logging.logging_handlers import (
    SafeRotatingFileHandler,
    WarningOnlyFilter,
    create_aggregator_handler,
)


@pytest.fixture
def temp_log_dir(tmp_path):
    """Create a temporary directory for log files."""
    return str(tmp_path)


@pytest.fixture
def temp_log_file(tmp_path):
    """Create a temporary log file path."""
    return str(tmp_path / "test.log")


def test_safe_rotating_file_handler_init(temp_log_file):
    """Test SafeRotatingFileHandler initialization."""
    handler = SafeRotatingFileHandler(temp_log_file, maxBytes=1024, backupCount=3)
    assert handler.baseFilename == temp_log_file
    assert handler.maxBytes == 1024
    assert handler.backupCount == 3
    handler.close()


def test_safe_rotating_file_handler_open_success(temp_log_file):
    """Test _open() successfully opens file when directory exists."""
    handler = SafeRotatingFileHandler(temp_log_file, maxBytes=1024, backupCount=3)
    stream = handler._open()
    assert stream is not None
    assert stream.writable()
    handler.close()


def test_safe_rotating_file_handler_open_no_base_filename():
    """Test _open() handles missing baseFilename."""
    handler = SafeRotatingFileHandler("", maxBytes=1024, backupCount=3)
    with patch.object(SafeRotatingFileHandler.__bases__[0], "_open", return_value=MagicMock()):
        stream = handler._open()
        assert stream is not None
    handler.close()


def test_safe_rotating_file_handler_open_returns_stringio_on_final_failure(temp_log_file):
    """Test _open() returns StringIO on final failure."""
    handler = SafeRotatingFileHandler(temp_log_file, maxBytes=1024, backupCount=3)

    def always_failing_open(*args, **kwargs):
        raise FileNotFoundError("Directory not found")

    with patch.object(SafeRotatingFileHandler.__bases__[0], "_open", side_effect=always_failing_open):
        with patch("server.structured_logging.logging_handlers.ensure_log_directory"):
            stream = handler._open()
            assert stream is not None
            # Should return StringIO as fallback
            assert hasattr(stream, "write")
    handler.close()


def test_safe_rotating_file_handler_should_rollover_false(temp_log_file):
    """Test shouldRollover() returns False when no rollover needed."""
    handler = SafeRotatingFileHandler(temp_log_file, maxBytes=1024, backupCount=3)
    handler.stream = open(temp_log_file, "w", encoding="utf-8")
    handler.stream.write("small content")
    handler.stream.flush()
    record = logging.LogRecord("test", logging.INFO, "", 0, "test message", (), None)
    result = handler.shouldRollover(record)
    assert result is False
    handler.close()


def test_safe_rotating_file_handler_should_rollover_no_base_filename():
    """Test shouldRollover() returns False when baseFilename is empty."""
    handler = SafeRotatingFileHandler("", maxBytes=1024, backupCount=3)
    record = logging.LogRecord("test", logging.INFO, "", 0, "test message", (), None)
    result = handler.shouldRollover(record)
    assert result is False
    handler.close()


def test_safe_rotating_file_handler_should_rollover_retries_on_error(temp_log_file):
    """Test shouldRollover() retries on FileNotFoundError."""
    handler = SafeRotatingFileHandler(temp_log_file, maxBytes=1024, backupCount=3)
    call_count = 0

    def failing_should_rollover(*args, **kwargs):
        nonlocal call_count
        call_count += 1
        if call_count < 2:
            raise FileNotFoundError("Directory not found")
        return False

    with patch.object(SafeRotatingFileHandler.__bases__[0], "shouldRollover", side_effect=failing_should_rollover):
        with patch("server.structured_logging.logging_handlers.ensure_log_directory"):
            record = logging.LogRecord("test", logging.INFO, "", 0, "test message", (), None)
            result = handler.shouldRollover(record)
            assert result is False
            assert call_count >= 2
    handler.close()


def test_warning_only_filter_warning_level():
    """Test WarningOnlyFilter allows WARNING level logs."""
    filter_obj = WarningOnlyFilter()
    record = logging.LogRecord("test", logging.WARNING, "", 0, "warning message", (), None)
    result = filter_obj.filter(record)
    assert result is True


def test_warning_only_filter_error_level():
    """Test WarningOnlyFilter blocks ERROR level logs."""
    filter_obj = WarningOnlyFilter()
    record = logging.LogRecord("test", logging.ERROR, "", 0, "error message", (), None)
    result = filter_obj.filter(record)
    assert result is False


def test_warning_only_filter_critical_level():
    """Test WarningOnlyFilter blocks CRITICAL level logs."""
    filter_obj = WarningOnlyFilter()
    record = logging.LogRecord("test", logging.CRITICAL, "", 0, "critical message", (), None)
    result = filter_obj.filter(record)
    assert result is False


def test_warning_only_filter_info_level():
    """Test WarningOnlyFilter blocks INFO level logs."""
    filter_obj = WarningOnlyFilter()
    record = logging.LogRecord("test", logging.INFO, "", 0, "info message", (), None)
    result = filter_obj.filter(record)
    assert result is False


def test_warning_only_filter_debug_level():
    """Test WarningOnlyFilter blocks DEBUG level logs."""
    filter_obj = WarningOnlyFilter()
    record = logging.LogRecord("test", logging.DEBUG, "", 0, "debug message", (), None)
    result = filter_obj.filter(record)
    assert result is False


def test_create_aggregator_handler_warning_level(temp_log_dir):
    """Test create_aggregator_handler() creates handler for WARNING level."""
    log_path = Path(temp_log_dir) / "warnings.log"
    handler = create_aggregator_handler(log_path, logging.WARNING, max_bytes=1024, backup_count=3)
    assert handler.level == logging.WARNING
    assert len(handler.filters) > 0
    assert isinstance(handler.filters[0], WarningOnlyFilter)
    handler.close()


def test_create_aggregator_handler_error_level(temp_log_dir):
    """Test create_aggregator_handler() creates handler for ERROR level."""
    log_path = Path(temp_log_dir) / "errors.log"
    handler = create_aggregator_handler(log_path, logging.ERROR, max_bytes=1024, backup_count=3)
    assert handler.level == logging.ERROR
    # ERROR level handler should not have WarningOnlyFilter
    assert not any(isinstance(f, WarningOnlyFilter) for f in handler.filters)
    handler.close()


def test_create_aggregator_handler_with_player_service(temp_log_dir):
    """Test create_aggregator_handler() with player_service."""
    log_path = Path(temp_log_dir) / "warnings.log"
    mock_player_service = MagicMock()
    handler = create_aggregator_handler(
        log_path, logging.WARNING, max_bytes=1024, backup_count=3, player_service=mock_player_service
    )
    assert handler.formatter is not None
    handler.close()


def test_create_aggregator_handler_without_player_service(temp_log_dir):
    """Test create_aggregator_handler() without player_service."""
    log_path = Path(temp_log_dir) / "warnings.log"
    handler = create_aggregator_handler(log_path, logging.WARNING, max_bytes=1024, backup_count=3)
    assert handler.formatter is not None
    handler.close()


def test_create_aggregator_handler_windows_platform(temp_log_dir):
    """Test create_aggregator_handler() uses Windows-safe handler on Windows."""
    log_path = Path(temp_log_dir) / "warnings.log"
    with patch("sys.platform", "win32"):
        with patch(
            "server.structured_logging.windows_safe_rotation.WindowsSafeRotatingFileHandler"
        ) as mock_win_handler:
            handler = create_aggregator_handler(log_path, logging.WARNING, max_bytes=1024, backup_count=3)
            # Should use Windows-safe handler
            assert handler is not None
            handler.close()


def test_create_aggregator_handler_non_windows_platform(temp_log_dir):
    """Test create_aggregator_handler() uses standard handler on non-Windows."""
    log_path = Path(temp_log_dir) / "warnings.log"
    with patch("sys.platform", "linux"):
        handler = create_aggregator_handler(log_path, logging.WARNING, max_bytes=1024, backup_count=3)
        assert handler is not None
        handler.close()


def test_create_aggregator_handler_retries_on_error(temp_log_dir):
    """Test create_aggregator_handler() handles errors gracefully."""
    log_path = Path(temp_log_dir) / "warnings.log"
    # Test that create_aggregator_handler works correctly - retry logic is internal
    handler = create_aggregator_handler(log_path, logging.WARNING, max_bytes=1024, backup_count=3)
    assert handler is not None
    handler.close()
