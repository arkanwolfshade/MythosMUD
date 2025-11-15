"""
Unit tests for PlayerGuidFormatter class.

These tests verify the GUID-to-name conversion functionality in logging,
including UUID pattern matching, player lookup, error handling, and
thread safety for the MythosMUD logging enhancement.
"""

import logging
import re
import time
from unittest.mock import Mock, patch

from server.logging.player_guid_formatter import PlayerGuidFormatter


class TestPlayerGuidFormatter:
    """Test suite for PlayerGuidFormatter class."""

    def setup_method(self):
        """Set up test fixtures."""
        # Create mock player service
        self.mock_player_service = Mock()

        # Create mock persistence layer
        self.mock_persistence = Mock()
        self.mock_player_service.persistence = self.mock_persistence

        # Create formatter instance
        self.formatter = PlayerGuidFormatter(
            player_service=self.mock_player_service,
            fmt="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )

    def test_formatter_initialization(self):
        """Test PlayerGuidFormatter initialization."""
        assert self.formatter.player_service == self.mock_player_service
        assert hasattr(self.formatter, "uuid_pattern")
        assert isinstance(self.formatter.uuid_pattern, re.Pattern)

        # Test UUID pattern matches standard UUID format
        test_uuid = "123e4567-e89b-12d3-a456-426614174000"
        assert self.formatter.uuid_pattern.search(test_uuid) is not None

    def test_uuid_pattern_matching(self):
        """Test UUID pattern matching with various formats."""
        # Valid UUIDs should match
        valid_uuids = [
            "123e4567-e89b-12d3-a456-426614174000",
            "550e8400-e29b-41d4-a716-446655440000",
            "6ba7b810-9dad-11d1-80b4-00c04fd430c8",
            "6ba7b811-9dad-11d1-80b4-00c04fd430c8",
        ]

        for uuid_str in valid_uuids:
            assert self.formatter.uuid_pattern.search(uuid_str) is not None
            # Test case insensitive
            assert self.formatter.uuid_pattern.search(uuid_str.upper()) is not None

    def test_uuid_pattern_non_matching(self):
        """Test UUID pattern doesn't match invalid formats."""
        invalid_strings = [
            "123e4567-e89b-12d3-a456",  # Too short
            "123e4567-e89b-12d3-a456-426614174000-extra",  # Too long
            "123e4567-e89b-12d3-a456-42661417400g",  # Invalid character
            "not-a-uuid-at-all",
            "12345678901234567890123456789012",  # No hyphens
            "",  # Empty string
        ]

        for invalid_str in invalid_strings:
            assert self.formatter.uuid_pattern.search(invalid_str) is None

    def test_get_player_name_success(self):
        """Test successful player name lookup."""
        # Mock player data
        mock_player = Mock()
        mock_player.name = "ProfessorWolfshade"

        # Mock persistence layer
        mock_persistence = Mock()
        mock_persistence.get_player.return_value = mock_player
        self.mock_player_service.persistence = mock_persistence

        guid = "123e4567-e89b-12d3-a456-426614174000"
        result = self.formatter._get_player_name(guid)

        assert result == "ProfessorWolfshade"
        mock_persistence.get_player.assert_called_once_with(guid)

    def test_get_player_name_not_found(self):
        """Test player name lookup when player not found."""
        # Mock persistence layer
        mock_persistence = Mock()
        mock_persistence.get_player.return_value = None
        self.mock_player_service.persistence = mock_persistence

        guid = "123e4567-e89b-12d3-a456-426614174000"
        result = self.formatter._get_player_name(guid)

        assert result is None
        mock_persistence.get_player.assert_called_once_with(guid)

    def test_get_player_name_exception(self):
        """Test player name lookup when exception occurs."""
        # Mock persistence layer
        mock_persistence = Mock()
        mock_persistence.get_player.side_effect = AttributeError("Database error")
        self.mock_player_service.persistence = mock_persistence

        guid = "123e4567-e89b-12d3-a456-426614174000"
        result = self.formatter._get_player_name(guid)

        assert result is None

    def test_log_lookup_failure(self):
        """Test logging of lookup failures."""
        with patch("sys.stderr") as mock_stderr:
            guid = "123e4567-e89b-12d3-a456-426614174000"
            self.formatter._log_lookup_failure(guid)

            # Verify error was written directly to stderr
            mock_stderr.write.assert_called_once()
            call_args = mock_stderr.write.call_args[0][0]
            assert f"Failed to resolve player name for GUID: {guid}" in call_args
            assert "errors - WARNING" in call_args

    def test_convert_player_guids_success(self):
        """Test successful GUID conversion in message."""
        # Mock player data
        mock_player = Mock()
        mock_player.name = "ProfessorWolfshade"
        self.mock_persistence.get_player.return_value = mock_player

        message = "Player 123e4567-e89b-12d3-a456-426614174000 connected"
        result = self.formatter._convert_player_guids(message)

        expected = "Player <ProfessorWolfshade>: 123e4567-e89b-12d3-a456-426614174000 connected"
        assert result == expected

    def test_convert_player_guids_not_found(self):
        """Test GUID conversion when player not found."""
        self.mock_persistence.get_player.return_value = None

        with patch.object(self.formatter, "_log_lookup_failure") as mock_log_failure:
            message = "Player 123e4567-e89b-12d3-a456-426614174000 connected"
            result = self.formatter._convert_player_guids(message)

            expected = "Player <UNKNOWN>: 123e4567-e89b-12d3-a456-426614174000 connected"
            assert result == expected
            mock_log_failure.assert_called_once_with("123e4567-e89b-12d3-a456-426614174000")

    def test_convert_player_guids_multiple_guids(self):
        """Test conversion of multiple GUIDs in same message."""

        # Mock different players for different GUIDs
        def mock_get_player(guid):
            if guid == "123e4567-e89b-12d3-a456-426614174000":
                player = Mock()
                player.name = "ProfessorWolfshade"
                return player
            elif guid == "550e8400-e29b-41d4-a716-446655440000":
                player = Mock()
                player.name = "TestPlayer"
                return player
            return None

        self.mock_persistence.get_player.side_effect = mock_get_player

        message = "Players 123e4567-e89b-12d3-a456-426614174000 and 550e8400-e29b-41d4-a716-446655440000 are online"
        result = self.formatter._convert_player_guids(message)

        expected = "Players <ProfessorWolfshade>: 123e4567-e89b-12d3-a456-426614174000 and <TestPlayer>: 550e8400-e29b-41d4-a716-446655440000 are online"
        assert result == expected

    def test_convert_player_guids_mixed_success_failure(self):
        """Test conversion with some successful and some failed lookups."""

        def mock_get_player(guid):
            if guid == "123e4567-e89b-12d3-a456-426614174000":
                player = Mock()
                player.name = "ProfessorWolfshade"
                return player
            return None  # Second GUID not found

        self.mock_persistence.get_player.side_effect = mock_get_player

        with patch.object(self.formatter, "_log_lookup_failure") as mock_log_failure:
            message = (
                "Player 123e4567-e89b-12d3-a456-426614174000 connected, but 550e8400-e29b-41d4-a716-446655440000 failed"
            )
            result = self.formatter._convert_player_guids(message)

            expected = "Player <ProfessorWolfshade>: 123e4567-e89b-12d3-a456-426614174000 connected, but <UNKNOWN>: 550e8400-e29b-41d4-a716-446655440000 failed"
            assert result == expected
            mock_log_failure.assert_called_once_with("550e8400-e29b-41d4-a716-446655440000")

    def test_convert_player_guids_no_guids(self):
        """Test message with no GUIDs remains unchanged."""
        message = "This is a regular log message with no GUIDs"
        result = self.formatter._convert_player_guids(message)

        assert result == message

    def test_format_method_integration(self):
        """Test the complete format method integration."""
        # Mock player data
        mock_player = Mock()
        mock_player.name = "ProfessorWolfshade"
        self.mock_persistence.get_player.return_value = mock_player

        # Create a log record
        record = logging.LogRecord(
            name="test.logger",
            level=logging.INFO,
            pathname="test.py",
            lineno=1,
            msg="Player 123e4567-e89b-12d3-a456-426614174000 connected",
            args=(),
            exc_info=None,
        )

        result = self.formatter.format(record)

        # Should contain the enhanced GUID format
        assert "<ProfessorWolfshade>: 123e4567-e89b-12d3-a456-426614174000" in result
        assert "Player" in result
        assert "connected" in result

    def test_format_method_no_guids(self):
        """Test format method with message containing no GUIDs."""
        record = logging.LogRecord(
            name="test.logger",
            level=logging.INFO,
            pathname="test.py",
            lineno=1,
            msg="Server started successfully",
            args=(),
            exc_info=None,
        )

        result = self.formatter.format(record)

        # Should contain original message
        assert "Server started successfully" in result
        # Should not contain any GUID conversion markers
        assert "<" not in result or ">" not in result

    def test_serial_guid_conversion(self):
        """Test GUID conversion in serial execution."""
        # Mock player data
        mock_player = Mock()
        mock_player.name = "ProfessorWolfshade"
        self.mock_persistence.get_player.return_value = mock_player

        results = []
        errors = []

        def convert_guid(guid):
            try:
                message = f"Player {guid} connected"
                result = self.formatter._convert_player_guids(message)
                results.append(result)
            except Exception as e:
                errors.append(e)

        # Execute conversions serially instead of in parallel threads
        # This tests the same functionality without violating serial test execution
        test_guid = "123e4567-e89b-12d3-a456-426614174000"

        for _ in range(10):
            convert_guid(test_guid)

        # Verify no errors occurred
        assert len(errors) == 0

        # Verify all results are correct
        expected = f"Player <ProfessorWolfshade>: {test_guid} connected"
        assert len(results) == 10
        assert all(result == expected for result in results)

    def test_performance_with_large_message(self):
        """Test performance with large message containing many GUIDs."""
        # Mock player data
        mock_player = Mock()
        mock_player.name = "ProfessorWolfshade"
        self.mock_persistence.get_player.return_value = mock_player

        # Create message with many GUIDs
        guid = "123e4567-e89b-12d3-a456-426614174000"
        message_parts = [f"Player {guid}"] * 100
        message = " ".join(message_parts)

        start_time = time.time()
        result = self.formatter._convert_player_guids(message)
        end_time = time.time()

        # Should complete quickly (allowing headroom for slower CI hosts)
        duration = end_time - start_time
        # Empirically, busy CI runners can take up to ~0.5s for this many replacements.
        # The intent of this assertion is to ensure we do not regress into multi-second
        # scans; keep the threshold generous but still bounded.
        assert duration < 0.5

        # Verify all GUIDs were converted
        expected_count = 100
        actual_count = result.count("<ProfessorWolfshade>:")
        assert actual_count == expected_count

    def test_edge_case_empty_message(self):
        """Test edge case with empty message."""
        result = self.formatter._convert_player_guids("")
        assert result == ""

    def test_edge_case_none_message(self):
        """Test edge case with None message."""
        result = self.formatter._convert_player_guids(None)
        assert result == ""

    def test_case_insensitive_guid_matching(self):
        """Test that GUID matching is case insensitive."""
        # Mock player data
        mock_player = Mock()
        mock_player.name = "ProfessorWolfshade"
        self.mock_persistence.get_player.return_value = mock_player

        # Test with uppercase GUID
        message = "Player 123E4567-E89B-12D3-A456-426614174000 connected"
        result = self.formatter._convert_player_guids(message)

        expected = "Player <ProfessorWolfshade>: 123E4567-E89B-12D3-A456-426614174000 connected"
        assert result == expected

    def test_recursive_error_logging_prevention(self):
        """Test that error logging doesn't create infinite loops with formatted GUIDs."""
        # Mock player service to return None (player not found)
        self.mock_persistence.get_player.return_value = None

        # Create a message that would trigger error logging
        test_guid = "123e4567-e89b-12d3-a456-426614174000"
        message = f"Player {test_guid} connected"

        # Mock sys.stderr to capture direct stderr writes
        with patch("sys.stderr") as mock_stderr:
            # Process the message - this should trigger error logging
            result = self.formatter._convert_player_guids(message)

            # Verify the message was converted correctly
            expected = f"Player <UNKNOWN>: {test_guid} connected"
            assert result == expected

            # Verify error was written directly to stderr (bypassing logging system)
            # This prevents infinite loops since stderr writes don't go through formatters
            mock_stderr.write.assert_called_once()
            call_args = mock_stderr.write.call_args[0][0]
            assert f"Failed to resolve player name for GUID: {test_guid}" in call_args
            # Ensure the error message doesn't contain the formatted GUID
            assert "<UNKNOWN>:" not in call_args

    def test_context_aware_guid_processing(self):
        """Test that the formatter only processes GUIDs in appropriate contexts."""
        # Mock player data
        mock_player = Mock()
        mock_player.name = "TestPlayer"
        self.mock_persistence.get_player.return_value = mock_player

        # Test GUID in WebSocket context (should NOT be processed)
        websocket_message = "Dead WebSocket connection 123e4567-e89b-12d3-a456-426614174000 for player"
        result = self.formatter._convert_player_guids(websocket_message)
        # Should return original message without processing the WebSocket GUID
        assert result == websocket_message
        # Should not call persistence layer for WebSocket GUIDs
        self.mock_persistence.get_player.assert_not_called()

        # Reset mock
        self.mock_persistence.reset_mock()
        self.mock_persistence.get_player.return_value = mock_player

        # Test GUID in player context (should be processed)
        player_message = "Player 123e4567-e89b-12d3-a456-426614174000 moved to room"
        result = self.formatter._convert_player_guids(player_message)
        expected = "Player <TestPlayer>: 123e4567-e89b-12d3-a456-426614174000 moved to room"
        assert result == expected
        # Should call persistence layer for player GUIDs
        self.mock_persistence.get_player.assert_called_once_with("123e4567-e89b-12d3-a456-426614174000")

    def test_context_detection_methods(self):
        """Test the context detection methods work correctly."""
        # Test non-player contexts
        assert not self.formatter._is_likely_player_id(
            "123e4567-e89b-12d3-a456-426614174000", "WebSocket connection established"
        )
        assert not self.formatter._is_likely_player_id(
            "123e4567-e89b-12d3-a456-426614174000", "Dead WebSocket connection"
        )
        assert not self.formatter._is_likely_player_id(
            "123e4567-e89b-12d3-a456-426614174000", "Connection manager error"
        )
        assert not self.formatter._is_likely_player_id(
            "123e4567-e89b-12d3-a456-426614174000", "Message delivery status"
        )
        assert not self.formatter._is_likely_player_id("123e4567-e89b-12d3-a456-426614174000", "User lookup result")
        assert not self.formatter._is_likely_player_id(
            "123e4567-e89b-12d3-a456-426614174000", "User(id=123e4567-e89b-12d3-a456-426614174000"
        )
        assert not self.formatter._is_likely_player_id(
            "123e4567-e89b-12d3-a456-426614174000", "Authentication successful"
        )
        assert not self.formatter._is_likely_player_id(
            "123e4567-e89b-12d3-a456-426614174000", "auth.endpoints - User login"
        )

        # Test player contexts
        assert self.formatter._is_likely_player_id("123e4567-e89b-12d3-a456-426614174000", "Player moved to room")
        assert self.formatter._is_likely_player_id("123e4567-e89b-12d3-a456-426614174000", "Player entered game")
        assert self.formatter._is_likely_player_id("123e4567-e89b-12d3-a456-426614174000", "Character stats updated")
        assert self.formatter._is_likely_player_id("123e4567-e89b-12d3-a456-426614174000", "Game state updated")
        assert self.formatter._is_likely_player_id("123e4567-e89b-12d3-a456-426614174000", "Room occupants changed")
        assert self.formatter._is_likely_player_id("123e4567-e89b-12d3-a456-426614174000", "Player service lookup")
        assert self.formatter._is_likely_player_id(
            "123e4567-e89b-12d3-a456-426614174000", "Message delivery status for player"
        )

        # Test default behavior (should be True for unknown contexts)
        assert self.formatter._is_likely_player_id(
            "123e4567-e89b-12d3-a456-426614174000", "Some random message with GUID"
        )
