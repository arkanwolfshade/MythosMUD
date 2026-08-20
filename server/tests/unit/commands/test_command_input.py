"""
Unit tests for command input processing.

Tests command normalization, cleaning, and emote detection.
"""

from unittest.mock import MagicMock, patch

from server.command_handler.command_input import (
    _is_predefined_emote,
    clean_command_input,
    normalize_command,
    should_treat_as_emote,
)


def _mock_request(emote_service):
    """Build a mock request whose app.state.emote_service is the given value."""
    request = MagicMock()
    request.app.state.emote_service = emote_service
    return request


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

    def test_is_predefined_emote_true(self):
        """Test _is_predefined_emote() returns True for predefined emote."""
        mock_service = MagicMock()
        mock_service.is_emote_alias.return_value = True
        request = _mock_request(mock_service)

        result = _is_predefined_emote("smile", request)
        assert result is True

    def test_is_predefined_emote_false(self):
        """Test _is_predefined_emote() returns False for non-emote."""
        mock_service = MagicMock()
        mock_service.is_emote_alias.return_value = False
        request = _mock_request(mock_service)

        result = _is_predefined_emote("look", request)
        assert result is False

    def test_is_predefined_emote_no_request(self):
        """Test _is_predefined_emote() returns False when no request is available."""
        result = _is_predefined_emote("test")
        assert result is False

    def test_is_predefined_emote_no_emote_service(self):
        """Test _is_predefined_emote() returns False when app.state has no emote_service."""
        request = _mock_request(None)
        result = _is_predefined_emote("test", request)
        assert result is False

    def test_is_predefined_emote_handles_error(self):
        """Test _is_predefined_emote() handles errors from the emote service gracefully."""
        mock_service = MagicMock()
        mock_service.is_emote_alias.side_effect = RuntimeError("boom")
        request = _mock_request(mock_service)

        result = _is_predefined_emote("test", request)
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
