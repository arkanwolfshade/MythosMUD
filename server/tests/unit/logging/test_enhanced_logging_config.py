"""
Tests for enhanced logging configuration.
"""

import logging
import tempfile
import time
from pathlib import Path
from unittest.mock import Mock, patch

from server.exceptions import LoggedException
from server.logging.enhanced_logging_config import (
    add_correlation_id,
    add_request_context,
    bind_request_context,
    clear_request_context,
    configure_enhanced_structlog,
    get_current_context,
    get_enhanced_logger,
    get_logger,
    log_exception_once,
    sanitize_sensitive_data,
    setup_enhanced_logging,
)


def _close_all_logging_handlers():
    """
    Close all logging handlers to release file handles on Windows.

    This is necessary because Windows holds file handles open until explicitly closed,
    which prevents tempfile.TemporaryDirectory from cleaning up.
    """
    # Get all loggers
    root_logger = logging.getLogger()

    # List of all known subsystem loggers
    subsystem_loggers = [
        "server",
        "persistence",
        "authentication",
        "inventory",
        "npc",
        "game",
        "api",
        "middleware",
        "monitoring",
        "time",
        "caching",
        "communications",
        "commands",
        "events",
        "infrastructure",
        "validators",
        "combat",
        "access",
        "security",
        "uvicorn",
        "uvicorn.access",
        "uvicorn.error",
    ]

    # Close all root logger handlers
    for handler in root_logger.handlers[:]:
        try:
            handler.flush()
            handler.close()
            root_logger.removeHandler(handler)
        except (OSError, AttributeError, ValueError):
            pass  # Ignore errors during cleanup

    # Close all subsystem logger handlers
    for subsystem in subsystem_loggers:
        logger = logging.getLogger(subsystem)
        for handler in logger.handlers[:]:
            try:
                handler.flush()
                handler.close()
                logger.removeHandler(handler)
            except (OSError, AttributeError, ValueError):
                pass  # Ignore errors during cleanup

    # Also check for any other loggers that might have handlers
    # This is a fallback to catch any we might have missed
    manager = logging.Logger.manager
    for logger_name in list(manager.loggerDict.keys()):
        logger = logging.getLogger(logger_name)
        for handler in logger.handlers[:]:
            try:
                handler.flush()
                handler.close()
                logger.removeHandler(handler)
            except (OSError, AttributeError, ValueError):
                pass  # Ignore errors during cleanup

    # Give Windows a moment to release file handles
    time.sleep(0.1)


class TestEnhancedLoggingConfig:
    """Test enhanced logging configuration functionality."""

    def test_sanitize_sensitive_data(self):
        """Test that sensitive data is properly sanitized."""
        # Test data with sensitive information
        event_dict = {
            "user_id": "123",
            "password": "secret123",
            "token": "abc123",
            "api_key": "key456",
            "normal_field": "value",
        }

        result = sanitize_sensitive_data(None, None, event_dict)

        # Sensitive data should be redacted
        assert result["password"] == "[REDACTED]"
        assert result["token"] == "[REDACTED]"
        assert result["api_key"] == "[REDACTED]"

        # Normal data should remain unchanged
        assert result["user_id"] == "123"
        assert result["normal_field"] == "value"

    def test_sanitize_sensitive_data_case_insensitive(self):
        """Test that sensitive data sanitization is case insensitive."""
        event_dict = {
            "Password": "secret123",
            "API_KEY": "key456",
            "Secret": "hidden",
        }

        result = sanitize_sensitive_data(None, None, event_dict)

        assert result["Password"] == "[REDACTED]"
        assert result["API_KEY"] == "[REDACTED]"
        assert result["Secret"] == "[REDACTED]"

    def test_add_correlation_id(self):
        """Test that correlation IDs are added correctly."""
        event_dict = {"message": "test"}

        result = add_correlation_id(None, None, event_dict)

        assert "correlation_id" in result
        assert result["correlation_id"] is not None

    def test_add_request_context(self):
        """Test that request context is added correctly."""
        event_dict = {"message": "test"}

        result = add_request_context(None, None, event_dict)

        assert "request_id" in result
        assert result["request_id"] is not None

    @patch("server.logging.enhanced_logging_config.get_logger")
    @patch("server.logging.enhanced_logging_config.structlog.wrap_logger")
    def test_get_enhanced_logger(self, mock_wrap_logger, mock_get_logger):
        """Test that get_enhanced_logger returns an enhanced logger instance."""
        mock_base_logger = Mock()
        mock_enhanced_logger = Mock()
        mock_get_logger.return_value = mock_base_logger
        mock_wrap_logger.return_value = mock_enhanced_logger

        result = get_enhanced_logger("test")

        assert result == mock_enhanced_logger
        mock_get_logger.assert_called_once_with("test")
        mock_wrap_logger.assert_called_once_with(mock_base_logger)

    @patch("server.logging.logging_context.bind_contextvars")
    def test_bind_request_context(self, mock_bind_contextvars):
        """Test that request context is bound correctly."""
        correlation_id = "test-correlation-id"
        user_id = "test-user-id"

        bind_request_context(correlation_id=correlation_id, user_id=user_id)

        mock_bind_contextvars.assert_called_once_with(correlation_id=correlation_id, user_id=user_id)

    def test_clear_request_context(self):
        """Test that request context is cleared correctly."""
        # This should not raise an exception
        clear_request_context()

    def test_get_current_context(self):
        """Test that current context is retrieved correctly."""
        context = get_current_context()
        assert isinstance(context, dict)

    @patch("server.logging.enhanced_logging_config._configure_enhanced_uvicorn_logging")
    @patch("server.logging.enhanced_logging_config.configure_enhanced_structlog")
    @patch("server.logging.enhanced_logging_config.get_logger")
    def test_setup_enhanced_logging_is_idempotent(self, mock_get_logger, mock_configure_structlog, mock_uvicorn):
        """Multiple invocations should not add duplicate handlers."""
        from server.logging import enhanced_logging_config as logging_config

        info_logger = Mock()
        debug_logger = Mock()
        mock_get_logger.side_effect = [info_logger, debug_logger]

        # Reset logging state to ensure clean test
        logging_config._logging_state.initialized = False
        logging_config._logging_state.signature = None

        config = {"logging": {"environment": "local", "level": "INFO", "log_base": "logs"}}

        setup_enhanced_logging(config)
        setup_enhanced_logging(config)

        assert mock_configure_structlog.call_count == 1
        assert mock_uvicorn.call_count == 1
        assert info_logger.info.call_count == 1
        assert debug_logger.debug.call_count == 1

        # Reset for downstream tests
        logging_config._logging_state.initialized = False
        logging_config._logging_state.signature = None

    def test_log_exception_once_marks_logged_exceptions(self):
        """Ensure log_exception_once honors logged exception markers."""
        logger = Mock()
        error = LoggedException("ritual failure")

        log_exception_once(logger, "error", "First log", exc=error)
        log_exception_once(logger, "error", "Second log", exc=error)

        logger.error.assert_called_once()
        assert error.already_logged is True

    def test_subsystem_log_files_created(self):
        """Test that all subsystem log files are created."""

        with tempfile.TemporaryDirectory() as tmpdir:
            log_config = {
                "log_base": tmpdir,
                "environment": "unit_test",
                "level": "INFO",
                "rotation": {"max_size": "10MB", "backup_count": 5},
            }

            configure_enhanced_structlog(
                environment="unit_test",
                log_level="INFO",
                log_config=log_config,
            )

            log_dir = Path(tmpdir) / "unit_test"

            # Check that subsystem log files exist
            expected_subsystems = [
                "server",
                "persistence",
                "authentication",
                "inventory",
                "npc",
                "game",
                "api",
                "middleware",
                "monitoring",
                "time",
                "caching",
                "communications",
                "commands",
                "events",
                "infrastructure",
                "validators",
                "combat",
                "access",
                "security",
            ]

            for subsystem in expected_subsystems:
                log_file = log_dir / f"{subsystem}.log"
                assert log_file.exists(), f"{subsystem}.log should exist"

            # Close all handlers to release file handles (Windows requirement)
            _close_all_logging_handlers()

    def test_world_log_not_created(self):
        """Test that world.log is NOT created (removed from subsystems)."""

        with tempfile.TemporaryDirectory() as tmpdir:
            log_config = {
                "log_base": tmpdir,
                "environment": "unit_test",
                "level": "INFO",
                "rotation": {"max_size": "10MB", "backup_count": 5},
            }

            configure_enhanced_structlog(
                environment="unit_test",
                log_level="INFO",
                log_config=log_config,
            )

            log_dir = Path(tmpdir) / "unit_test"
            world_log = log_dir / "world.log"

            assert not world_log.exists(), "world.log should NOT exist"

            # Close all handlers to release file handles (Windows requirement)
            _close_all_logging_handlers()

    def test_warnings_aggregator_created(self):
        """Test that warnings.log aggregator is created."""

        with tempfile.TemporaryDirectory() as tmpdir:
            log_config = {
                "log_base": tmpdir,
                "environment": "unit_test",
                "level": "INFO",
                "rotation": {"max_size": "10MB", "backup_count": 5},
            }

            configure_enhanced_structlog(
                environment="unit_test",
                log_level="INFO",
                log_config=log_config,
            )

            log_dir = Path(tmpdir) / "unit_test"
            warnings_log = log_dir / "warnings.log"

            assert warnings_log.exists(), "warnings.log should exist"

            # Close all handlers to release file handles (Windows requirement)
            _close_all_logging_handlers()

    def test_errors_aggregator_created(self):
        """Test that errors.log aggregator is created."""

        with tempfile.TemporaryDirectory() as tmpdir:
            log_config = {
                "log_base": tmpdir,
                "environment": "unit_test",
                "level": "INFO",
                "rotation": {"max_size": "10MB", "backup_count": 5},
            }

            configure_enhanced_structlog(
                environment="unit_test",
                log_level="INFO",
                log_config=log_config,
            )

            log_dir = Path(tmpdir) / "unit_test"
            errors_log = log_dir / "errors.log"

            assert errors_log.exists(), "errors.log should exist"

            # Close all handlers to release file handles (Windows requirement)
            _close_all_logging_handlers()

    def test_dual_logging_warnings(self):
        """Test that warnings appear in both subsystem log and warnings.log."""
        with tempfile.TemporaryDirectory() as tmpdir:
            log_config = {
                "log_base": tmpdir,
                "environment": "unit_test",
                "level": "INFO",
                "rotation": {"max_size": "10MB", "backup_count": 5},
            }

            configure_enhanced_structlog(
                environment="unit_test",
                log_level="INFO",
                log_config=log_config,
            )

            log_dir = Path(tmpdir) / "unit_test"

            # Get a logger for a specific subsystem (persistence)
            logger = get_logger("persistence.test")
            logger.warning("Test warning message", test_key="test_value")

            # Force handlers to flush
            root_logger = logging.getLogger()
            for handler in root_logger.handlers:
                handler.flush()

            # Check that warning appears in both files
            persistence_log = log_dir / "persistence.log"
            warnings_log = log_dir / "warnings.log"

            assert persistence_log.exists(), "persistence.log should exist"
            assert warnings_log.exists(), "warnings.log should exist"

            persistence_content = persistence_log.read_text(encoding="utf-8")
            warnings_content = warnings_log.read_text(encoding="utf-8")

            assert "Test warning message" in persistence_content, "Warning should be in persistence.log"
            assert "Test warning message" in warnings_content, "Warning should be in warnings.log"

            # Close all handlers to release file handles (Windows requirement)
            _close_all_logging_handlers()

    def test_errors_not_in_warnings_log(self):
        """Test that ERROR level logs do NOT appear in warnings.log (only in errors.log)."""
        with tempfile.TemporaryDirectory() as tmpdir:
            log_config = {
                "log_base": tmpdir,
                "environment": "unit_test",
                "level": "INFO",
                "rotation": {"max_size": "10MB", "backup_count": 5},
            }

            configure_enhanced_structlog(
                environment="unit_test",
                log_level="INFO",
                log_config=log_config,
            )

            log_dir = Path(tmpdir) / "unit_test"

            # Get a logger and log an ERROR
            logger = get_logger("test.module")
            logger.error("Test error message - should NOT be in warnings.log", test_key="test_value")

            # Force handlers to flush
            root_logger = logging.getLogger()
            for handler in root_logger.handlers:
                handler.flush()

            # Check that error does NOT appear in warnings.log
            warnings_log = log_dir / "warnings.log"
            errors_log = log_dir / "errors.log"

            assert warnings_log.exists(), "warnings.log should exist"
            assert errors_log.exists(), "errors.log should exist"

            warnings_content = warnings_log.read_text(encoding="utf-8")
            errors_content = errors_log.read_text(encoding="utf-8")

            assert "Test error message" not in warnings_content, "ERROR should NOT be in warnings.log"
            assert "Test error message" in errors_content, "ERROR should be in errors.log"

            # Close all handlers to release file handles (Windows requirement)
            _close_all_logging_handlers()

    def test_dual_logging_errors(self):
        """Test that errors appear in both subsystem log and errors.log."""
        with tempfile.TemporaryDirectory() as tmpdir:
            log_config = {
                "log_base": tmpdir,
                "environment": "unit_test",
                "level": "INFO",
                "rotation": {"max_size": "10MB", "backup_count": 5},
            }

            configure_enhanced_structlog(
                environment="unit_test",
                log_level="INFO",
                log_config=log_config,
            )

            log_dir = Path(tmpdir) / "unit_test"

            # Get a logger for a specific subsystem (authentication)
            logger = get_logger("auth.test")
            logger.error("Test error message", test_key="test_value")

            # Force handlers to flush
            root_logger = logging.getLogger()
            for handler in root_logger.handlers:
                handler.flush()

            # Check that error appears in both files
            auth_log = log_dir / "authentication.log"
            errors_log = log_dir / "errors.log"

            assert auth_log.exists(), "authentication.log should exist"
            assert errors_log.exists(), "errors.log should exist"

            auth_content = auth_log.read_text(encoding="utf-8")
            errors_content = errors_log.read_text(encoding="utf-8")

            assert "Test error message" in auth_content, "Error should be in authentication.log"
            assert "Test error message" in errors_content, "Error should be in errors.log"

            # Close all handlers to release file handles (Windows requirement)
            _close_all_logging_handlers()

    def test_new_subsystem_loggers(self):
        """Test that new subsystem loggers (inventory, npc, game, etc.) work correctly."""
        with tempfile.TemporaryDirectory() as tmpdir:
            log_config = {
                "log_base": tmpdir,
                "environment": "unit_test",
                "level": "INFO",
                "rotation": {"max_size": "10MB", "backup_count": 5},
            }

            configure_enhanced_structlog(
                environment="unit_test",
                log_level="INFO",
                log_config=log_config,
            )

            log_dir = Path(tmpdir) / "unit_test"

            # Test inventory subsystem
            inventory_logger = get_logger("inventory.test")
            inventory_logger.info("Inventory test message")
            inventory_log = log_dir / "inventory.log"
            assert inventory_log.exists(), "inventory.log should exist"

            # Test npc subsystem
            npc_logger = get_logger("npc.test")
            npc_logger.info("NPC test message")
            npc_log = log_dir / "npc.log"
            assert npc_log.exists(), "npc.log should exist"

            # Test game subsystem
            game_logger = get_logger("game.test")
            game_logger.info("Game test message")
            game_log = log_dir / "game.log"
            assert game_log.exists(), "game.log should exist"

            # Test api subsystem
            api_logger = get_logger("api.test")
            api_logger.info("API test message")
            api_log = log_dir / "api.log"
            assert api_log.exists(), "api.log should exist"

            # Test events subsystem
            events_logger = get_logger("events.test")
            events_logger.info("Events test message")
            events_log = log_dir / "events.log"
            assert events_log.exists(), "events.log should exist"

            # Test infrastructure subsystem
            infrastructure_logger = get_logger("infrastructure.test")
            infrastructure_logger.info("Infrastructure test message")
            infrastructure_log = log_dir / "infrastructure.log"
            assert infrastructure_log.exists(), "infrastructure.log should exist"

            # Test validators subsystem
            validators_logger = get_logger("validators.test")
            validators_logger.info("Validators test message")
            validators_log = log_dir / "validators.log"
            assert validators_log.exists(), "validators.log should exist"

            # Close all handlers to release file handles (Windows requirement)
            _close_all_logging_handlers()
