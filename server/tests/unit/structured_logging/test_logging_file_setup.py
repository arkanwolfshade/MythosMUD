"""
Unit tests for logging file setup.

Verifies aggregator handlers attached to root/listener (H1), WARNING/ERROR
propagation (H2), QueueListener started with aggregator handlers (H3), log
directory behavior (H4 covered in test_logging_utilities), and handlers
receiving records (H5).
"""

import logging
from pathlib import Path

import pytest

from server.structured_logging.logging_file_setup import (
    get_queue_listener,
    setup_enhanced_file_logging,
    stop_queue_listener,
)

# pylint: disable=redefined-outer-name  # Reason: Test fixture names match pytest convention


@pytest.fixture
def temp_log_base(tmp_path):
    """Temporary directory used as log_base for setup."""
    return tmp_path


@pytest.fixture
def default_log_config(temp_log_base):
    """Default log config with rotation."""
    return {
        "log_base": str(temp_log_base),
        "rotation": {"max_size": "1MB", "backup_count": 2},
    }


def _root_handlers_snapshot():
    """Return a copy of root logger handlers (for restore)."""
    return list(logging.getLogger().handlers)


def _restore_root_handlers(handlers):
    """Replace root logger handlers with the given list."""
    logging.getLogger().handlers = handlers


def test_aggregator_handlers_on_root_when_async(temp_log_base, default_log_config):  # pylint: disable=unused-argument  # Reason: temp_log_base used by default_log_config fixture
    """H1: With async enabled, root logger has QueueHandlers for aggregator path."""
    root = logging.getLogger()
    before = _root_handlers_snapshot()
    try:
        setup_enhanced_file_logging(
            environment="test",
            log_config=default_log_config,
            log_level="INFO",
            player_service=None,
            enable_async=True,
        )
        queue_handlers = [h for h in root.handlers if type(h).__name__ == "QueueHandler"]
        assert len(queue_handlers) >= 2, "Root should have at least two QueueHandlers (warnings + errors)"
    finally:
        stop_queue_listener()
        _restore_root_handlers(before)


def test_queue_listener_has_aggregator_handlers(temp_log_base, default_log_config):  # pylint: disable=unused-argument  # Reason: temp_log_base used by default_log_config fixture
    """H3: QueueListener is started and includes aggregator handlers."""
    before = _root_handlers_snapshot()
    try:
        setup_enhanced_file_logging(
            environment="test",
            log_config=default_log_config,
            log_level="INFO",
            player_service=None,
            enable_async=True,
        )
        listener = get_queue_listener()
        assert listener is not None
        # QueueListener stores handlers in .handlers
        base_filenames = []
        for h in getattr(listener, "handlers", []):
            if getattr(h, "baseFilename", None):
                base_filenames.append(Path(h.baseFilename).name)
        assert "warnings.log" in base_filenames, "Listener should have warnings.log handler"
        assert "errors.log" in base_filenames, "Listener should have errors.log handler"
    finally:
        stop_queue_listener()
        _restore_root_handlers(before)


def test_warning_and_error_reach_aggregator_files(temp_log_base, default_log_config):
    """H2/H5: WARNING and ERROR logged from root appear in warnings.log and errors.log."""
    root = logging.getLogger()
    before = _root_handlers_snapshot()
    try:
        setup_enhanced_file_logging(
            environment="test",
            log_config=default_log_config,
            log_level="DEBUG",
            player_service=None,
            enable_async=True,
        )
        listener = get_queue_listener()
        assert listener is not None

        root.warning("aggregator_test_warning_placeholder")
        root.error("aggregator_test_error_placeholder")

        stop_queue_listener()

        warnings_log = temp_log_base / "test" / "warnings.log"
        errors_log = temp_log_base / "test" / "errors.log"
        assert warnings_log.exists(), "warnings.log should exist"
        assert errors_log.exists(), "errors.log should exist"

        warnings_content = warnings_log.read_text(encoding="utf-8")
        errors_content = errors_log.read_text(encoding="utf-8")
        assert "aggregator_test_warning_placeholder" in warnings_content
        assert "aggregator_test_error_placeholder" in errors_content
    finally:
        stop_queue_listener()
        _restore_root_handlers(before)


def test_log_directory_under_env(temp_log_base, default_log_config):
    """H4 (setup): Log files are created under env_log_dir (e.g. .../test/)."""
    before = _root_handlers_snapshot()
    try:
        setup_enhanced_file_logging(
            environment="test",
            log_config=default_log_config,
            log_level="INFO",
            player_service=None,
            enable_async=False,
        )
        env_dir = temp_log_base / "test"
        assert env_dir.is_dir()
        # Aggregator files are created on first write; at least console/server may exist
        assert env_dir.exists()
    finally:
        _restore_root_handlers(before)
