"""
Unit tests for command input processing.

Tests command normalization, cleaning, and emote detection.
"""

from unittest.mock import MagicMock, Mock, patch

from server.command_handler.command_input import (
    _is_predefined_emote,
    clean_command_input,
    normalize_command,
    should_treat_as_emote,
)


class TestCommandNormalization:
    """Test command normalization functions."""

    def test_clean_command_input_basic(self):
        """Test clean_command_input() with normal command."""
        result = clean_command_input("look around")
        assert result == "look around"

    def test_clean_command_input_multiple_spaces(self):
        """Test clean_command_input() collapses multiple spaces."""
        result = clean_command_input("look    around   here")
        assert result == "look around here"

    def test_clean_command_input_leading_trailing_whitespace(self):
        """Test clean_command_input() strips leading/trailing whitespace."""
        result = clean_command_input("  look around  ")
        assert result == "look around"

    def test_clean_command_input_tabs(self):
        """Test clean_command_input() handles tabs."""
        result = clean_command_input("look\taround")
        assert result == "look around"

    def test_normalize_command_no_slash(self):
        """Test normalize_command() with no slash prefix."""
        result = normalize_command("look around")
        assert result == "look around"

    def test_normalize_command_with_slash(self):
        """Test normalize_command() removes slash prefix."""
        result = normalize_command("/look around")
        assert result == "look around"

    def test_normalize_command_empty(self):
        """Test normalize_command() with empty string."""
        result = normalize_command("")
        assert result == ""

    def test_normalize_command_whitespace_only(self):
        """Test normalize_command() with whitespace only."""
        result = normalize_command("   ")
        assert result == ""

    def test_normalize_command_slash_only(self):
        """Test normalize_command() with slash only."""
        result = normalize_command("/")
        assert result == ""

    def test_normalize_command_slash_with_spaces(self):
        """Test normalize_command() removes slash and trims spaces."""
        result = normalize_command("  /look  ")
        assert result == "look"


class TestEmoteDetection:
    """Test emote detection functions."""

    @patch("server.command_handler.command_input.EmoteService")
    def test_is_predefined_emote_true(self, mock_emote_service_class):
        """Test _is_predefined_emote() returns True for predefined emote."""
        mock_service = MagicMock()
        mock_service.is_emote_alias = Mock(return_value=True)
        mock_emote_service_class.return_value = mock_service

        result = _is_predefined_emote("smile")
        assert result is True

    @patch("server.command_handler.command_input.EmoteService")
    def test_is_predefined_emote_false(self, mock_emote_service_class):
        """Test _is_predefined_emote() returns False for non-emote."""
        mock_service = MagicMock()
        mock_service.is_emote_alias = Mock(return_value=False)
        mock_emote_service_class.return_value = mock_service

        result = _is_predefined_emote("look")
        assert result is False

    @patch("server.command_handler.command_input.EmoteService")
    def test_is_predefined_emote_handles_error(self, mock_emote_service_class):
        """Test _is_predefined_emote() handles errors gracefully."""
        mock_emote_service_class.side_effect = ImportError("Module not found")
        result = _is_predefined_emote("test")
        assert result is False

    def test_should_treat_as_emote_system_command(self):
        """Test should_treat_as_emote() returns False for system commands."""
        result = should_treat_as_emote("look")
        assert result is False

    def test_should_treat_as_emote_unknown_word(self):
        """Test should_treat_as_emote() returns False for unknown words."""
        with patch("server.command_handler.command_input._is_predefined_emote", return_value=False):
            result = should_treat_as_emote("unknownword")
            assert result is False

    def test_should_treat_as_emote_predefined_emote(self):
        """Test should_treat_as_emote() returns True for predefined emotes."""
        with patch("server.command_handler.command_input._is_predefined_emote", return_value=True):
            result = should_treat_as_emote("smile")
            assert result is True
