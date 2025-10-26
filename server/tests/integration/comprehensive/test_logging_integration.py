"""
Unit tests for logging integration with PlayerGuidFormatter.

These tests verify the integration of PlayerGuidFormatter with the existing
logging system, including formatter injection, log category coverage, and
integration with structlog infrastructure.
"""

import logging
import tempfile
from pathlib import Path
from unittest.mock import Mock, patch

from server.logging.enhanced_logging_config import (
    _setup_enhanced_file_logging,
    configure_enhanced_structlog,
)
from server.logging.player_guid_formatter import PlayerGuidFormatter


class TestLoggingIntegration:
    """Test suite for logging integration with PlayerGuidFormatter."""

    def setup_method(self):
        """Set up test fixtures."""
        # Create mock player service
        self.mock_player_service = Mock()

        # Create mock persistence layer (the fix uses this instead of async)
        self.mock_persistence = Mock()
        self.mock_player_service.persistence = self.mock_persistence

        # Create temporary directory for test logs
        self.temp_dir = tempfile.mkdtemp()
        self.log_dir = Path(self.temp_dir)

    def teardown_method(self):
        """Clean up test fixtures."""
        import shutil

        shutil.rmtree(self.temp_dir, ignore_errors=True)

    def test_player_guid_formatter_integration(self):
        """Test PlayerGuidFormatter integration with logging."""
        # Create formatter instance
        formatter = PlayerGuidFormatter(
            player_service=self.mock_player_service,
            fmt="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )

        # Verify formatter is properly initialized
        assert formatter.player_service == self.mock_player_service
        assert hasattr(formatter, "uuid_pattern")

        # Test that formatter can be used with a handler
        handler = logging.StreamHandler()
        handler.setFormatter(formatter)

        # Verify handler has the formatter
        assert handler.formatter == formatter

    def test_setup_file_logging_with_custom_formatter(self):
        """Test _setup_file_logging with custom PlayerGuidFormatter."""
        # Mock player data
        mock_player = Mock()
        mock_player.name = "ProfessorWolfshade"
        self.mock_persistence.get_player.return_value = mock_player

        # Create custom formatter
        custom_formatter = PlayerGuidFormatter(
            player_service=self.mock_player_service,
            fmt="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )

        # Mock the formatter creation in _setup_file_logging
        with patch("server.logging.enhanced_logging_config.logging.Formatter") as mock_formatter_class:
            mock_formatter_class.return_value = custom_formatter

            # Set up logging with test configuration
            log_config = {
                "log_base": str(self.log_dir),
                "rotation": {"max_size": "1MB", "backup_count": 2},
            }

            _setup_enhanced_file_logging("test", log_config, "INFO")

            # Verify formatter was created
            mock_formatter_class.assert_called()

    def test_log_categories_coverage(self):
        """Test that all log categories can use PlayerGuidFormatter."""
        # Expected log categories from logging_config.py
        expected_categories = {
            "server": ["server", "uvicorn"],
            "persistence": ["persistence", "PersistenceLayer", "aiosqlite"],
            "authentication": ["auth"],
            "world": ["world"],
            "communications": ["realtime", "communications"],
            "commands": ["commands"],
            "errors": ["errors"],
            "access": ["access", "server.app.factory"],
        }

        # Create formatter for each category
        for _category_name, prefixes in expected_categories.items():
            formatter = PlayerGuidFormatter(
                player_service=self.mock_player_service,
                fmt="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
                datefmt="%Y-%m-%d %H:%M:%S",
            )

            # Verify formatter can be created for each category
            assert formatter is not None
            assert hasattr(formatter, "uuid_pattern")

            # Test that formatter works with category-specific loggers
            for prefix in prefixes:
                logger = logging.getLogger(prefix)
                handler = logging.StreamHandler()
                handler.setFormatter(formatter)
                logger.addHandler(handler)

                # Verify handler was added
                assert handler in logger.handlers

                # Clean up
                logger.removeHandler(handler)

    def test_formatter_with_real_logging_scenario(self):
        """Test PlayerGuidFormatter with realistic logging scenario."""
        # Mock player data
        mock_player = Mock()
        mock_player.name = "ProfessorWolfshade"
        self.mock_persistence.get_player.return_value = mock_player

        # Create formatter
        formatter = PlayerGuidFormatter(
            player_service=self.mock_player_service,
            fmt="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )

        # Create logger and handler
        logger = logging.getLogger("test.logger")
        handler = logging.StreamHandler()
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)

        # Test logging with player GUID in message text (formatter extracts from text)
        test_guid = "123e4567-e89b-12d3-a456-426614174000"
        logger.info("Player 123e4567-e89b-12d3-a456-426614174000 connected")

        # Verify player service was called
        self.mock_persistence.get_player.assert_called_with(test_guid)

    def test_formatter_with_multiple_log_categories(self):
        """Test PlayerGuidFormatter across multiple log categories."""
        # Mock player data
        mock_player = Mock()
        mock_player.name = "ProfessorWolfshade"
        self.mock_persistence.get_player.return_value = mock_player

        # Create formatter
        formatter = PlayerGuidFormatter(
            player_service=self.mock_player_service,
            fmt="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )

        # Test multiple log categories
        categories = ["server", "persistence", "communications", "errors"]

        for category in categories:
            logger = logging.getLogger(category)
            handler = logging.StreamHandler()
            handler.setFormatter(formatter)
            logger.addHandler(handler)
            logger.setLevel(logging.INFO)

            # Log message with GUID (formatter extracts from message text)
            logger.info("Category action: Player 123e4567-e89b-12d3-a456-426614174000 performed action")

            # Clean up
            logger.removeHandler(handler)

        # Verify player service was called for each category
        assert self.mock_persistence.get_player.call_count == len(categories)

    def test_formatter_error_handling_integration(self):
        """Test that formatter error handling works with logging system."""
        # Mock persistence layer to raise exception
        self.mock_persistence.get_player.side_effect = Exception("Database error")

        # Create formatter
        formatter = PlayerGuidFormatter(
            player_service=self.mock_player_service,
            fmt="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )

        # Create logger and handler
        logger = logging.getLogger("test.error.logger")
        handler = logging.StreamHandler()
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)

        # Test logging with player GUID (should handle error gracefully)
        test_guid = "123e4567-e89b-12d3-a456-426614174000"

        # This should not raise an exception
        logger.info("Player 123e4567-e89b-12d3-a456-426614174000 connected")

        # Verify player service was called despite error
        self.mock_persistence.get_player.assert_called_with(test_guid)

    def test_formatter_with_structlog_integration(self):
        """Test PlayerGuidFormatter integration with structlog."""
        # Mock player data
        mock_player = Mock()
        mock_player.name = "ProfessorWolfshade"
        self.mock_persistence.get_player.return_value = mock_player

        # Create formatter
        formatter = PlayerGuidFormatter(
            player_service=self.mock_player_service,
            fmt="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )

        # Configure structlog (minimal setup for testing)
        configure_enhanced_structlog("test", "INFO", {"disable_logging": True})

        # Create logger that would be used by structlog
        logger = logging.getLogger("structlog.test")
        handler = logging.StreamHandler()
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)

        # Test logging with GUID
        test_guid = "123e4567-e89b-12d3-a456-426614174000"
        logger.info("Structlog message: Player 123e4567-e89b-12d3-a456-426614174000 connected")

        # Verify player service was called
        self.mock_persistence.get_player.assert_called_with(test_guid)

    def test_formatter_performance_with_logging(self):
        """Test formatter performance in realistic logging scenario."""
        # Mock player data
        mock_player = Mock()
        mock_player.name = "ProfessorWolfshade"
        self.mock_persistence.get_player.return_value = mock_player

        # Create formatter
        formatter = PlayerGuidFormatter(
            player_service=self.mock_player_service,
            fmt="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )

        # Create logger
        logger = logging.getLogger("test.performance")
        handler = logging.StreamHandler()
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)

        # Test multiple log messages
        num_messages = 50

        import time

        start_time = time.time()

        for i in range(num_messages):
            logger.info(
                "Message " + str(i) + ": Player 123e4567-e89b-12d3-a456-426614174000 performed action " + str(i)
            )

        end_time = time.time()
        duration = end_time - start_time

        # Should complete quickly (less than 1 second for 50 messages)
        assert duration < 1.0

        # Verify all messages were processed
        assert self.mock_persistence.get_player.call_count == num_messages

        # Clean up
        logger.removeHandler(handler)

    def test_formatter_with_different_log_levels(self):
        """Test PlayerGuidFormatter with different log levels."""
        # Mock player data
        mock_player = Mock()
        mock_player.name = "ProfessorWolfshade"
        self.mock_persistence.get_player.return_value = mock_player

        # Create formatter
        formatter = PlayerGuidFormatter(
            player_service=self.mock_player_service,
            fmt="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )

        # Create logger using standard logging for test setup
        logger = logging.getLogger("test.levels")
        handler = logging.StreamHandler()
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(logging.DEBUG)

        # Test different log levels - PlayerGuidFormatter extracts GUID from message text

        logger.debug("DEBUG: Player 123e4567-e89b-12d3-a456-426614174000 debug action")
        logger.info("INFO: Player 123e4567-e89b-12d3-a456-426614174000 info action")
        logger.warning("WARNING: Player 123e4567-e89b-12d3-a456-426614174000 warning action")
        logger.error("ERROR: Player 123e4567-e89b-12d3-a456-426614174000 error action")

        # Verify persistence layer was called for each level
        assert self.mock_persistence.get_player.call_count == 4

        # Clean up
        logger.removeHandler(handler)

    def test_formatter_with_complex_log_messages(self):
        """Test PlayerGuidFormatter with complex log messages."""
        # Mock player data
        mock_player = Mock()
        mock_player.name = "ProfessorWolfshade"
        self.mock_persistence.get_player.return_value = mock_player

        # Create formatter
        formatter = PlayerGuidFormatter(
            player_service=self.mock_player_service,
            fmt="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )

        # Create logger
        logger = logging.getLogger("test.complex")
        handler = logging.StreamHandler()
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)

        # Test complex messages
        complex_messages = [
            "Player 123e4567-e89b-12d3-a456-426614174000 moved from room A to room B",
            "Multiple players: 123e4567-e89b-12d3-a456-426614174000 and 550e8400-e29b-41d4-a716-446655440000 in room",
            "Database query for player 123e4567-e89b-12d3-a456-426614174000 returned 5 results",
            "Player 123e4567-e89b-12d3-a456-426614174000 completed quest successfully",
        ]

        for message in complex_messages:
            logger.info(message)

        # Verify player service was called for each GUID in each message
        # Message 1: 1 GUID, Message 2: 2 GUIDs, Message 3: 1 GUID,
        # Message 4: 1 GUID = 5 total calls
        expected_calls = 5  # 1 + 2 + 1 + 1 = 5 GUIDs total
        assert self.mock_persistence.get_player.call_count == expected_calls
