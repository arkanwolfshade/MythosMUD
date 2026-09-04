"""
Unit tests for command preparation.

Tests command preparation and processing pipeline.
"""

from unittest.mock import patch

from server.command_handler_unified import _prepare_command_for_processing


class TestPrepareCommandForProcessing:
    """Test _prepare_command_for_processing function."""

    def test_prepare_command_rate_limited(self):
        """Test _prepare_command_for_processing returns rate limit result when rate limited."""
        with patch("server.command_handler_unified._check_rate_limit", return_value={"result": "Rate limited"}):
            result = _prepare_command_for_processing("look", "testplayer", None)
            assert result[4] == {"result": "Rate limited"}

    def test_prepare_command_validation_failed(self):
        """Test _prepare_command_for_processing returns validation result when validation fails."""
        with (
            patch("server.command_handler_unified._check_rate_limit", return_value=None),
            patch("server.command_handler_unified._validate_command_basics", return_value={"result": "Invalid"}),
        ):
            result = _prepare_command_for_processing("look", "testplayer", None)
            assert result[4] == {"result": "Invalid"}

    def test_prepare_command_empty_after_cleaning(self):
        """Test _prepare_command_for_processing handles empty command after cleaning."""
        with (
            patch("server.command_handler_unified._check_rate_limit", return_value=None),
            patch("server.command_handler_unified._validate_command_basics", return_value=None),
            patch("server.command_handler_unified.clean_command_input", return_value=""),
        ):
            result = _prepare_command_for_processing("   ", "testplayer", None)
            assert result[4] == {"result": ""}

    def test_prepare_command_empty_after_normalization(self):
        """Test _prepare_command_for_processing handles empty command after normalization."""
        with (
            patch("server.command_handler_unified._check_rate_limit", return_value=None),
            patch("server.command_handler_unified._validate_command_basics", return_value=None),
            patch("server.command_handler_unified.clean_command_input", return_value="/"),
            patch("server.command_handler_unified.normalize_command", return_value=""),
        ):
            result = _prepare_command_for_processing("/", "testplayer", None)
            assert result[4] == {"result": ""}

    def test_prepare_command_success(self):
        """Test _prepare_command_for_processing successfully prepares command."""
        with (
            patch("server.command_handler_unified._check_rate_limit", return_value=None),
            patch("server.command_handler_unified._validate_command_basics", return_value=None),
            patch("server.command_handler_unified.clean_command_input", return_value="look north"),
            patch("server.command_handler_unified.normalize_command", return_value="look north"),
            patch("server.command_handler_unified._ensure_alias_storage", return_value=None),
        ):
            result = _prepare_command_for_processing("look north", "testplayer", None)
            assert result[0] == "look north"
            assert result[1] == "look"
            assert result[2] == ["north"]
            assert result[4] is None
