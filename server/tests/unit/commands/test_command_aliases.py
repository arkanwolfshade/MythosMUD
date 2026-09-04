"""
Unit tests for command alias handling.

Tests alias storage, expansion, and special command routing.
"""

from unittest.mock import MagicMock, patch

import pytest

from server.command_handler_unified import (
    _ensure_alias_storage,
    _handle_special_command_routing,
    _process_alias_expansion,
)


class TestEnsureAliasStorage:
    """Test _ensure_alias_storage function."""

    def test_ensure_alias_storage_returns_existing(self):
        """Test _ensure_alias_storage returns existing storage if provided."""
        mock_storage = MagicMock()
        result = _ensure_alias_storage(mock_storage)
        assert result == mock_storage

    def test_ensure_alias_storage_initializes_new(self):
        """Test _ensure_alias_storage initializes new storage when None."""
        with (
            patch("server.command_handler_unified.get_config") as mock_config,
            patch("server.command_handler_unified.AliasStorage") as mock_alias_class,
        ):
            mock_config_instance = MagicMock()
            mock_config_instance.game.aliases_dir = "/test/aliases"
            mock_config.return_value = mock_config_instance
            mock_storage = MagicMock()
            mock_alias_class.return_value = mock_storage

            result = _ensure_alias_storage(None)
            assert result == mock_storage
            mock_alias_class.assert_called_once_with(storage_dir="/test/aliases")

    def test_ensure_alias_storage_handles_error(self):
        """Test _ensure_alias_storage returns None on initialization error."""
        with (
            patch("server.command_handler_unified.get_config", side_effect=OSError("Config error")),
            patch("server.command_handler_unified.AliasStorage"),
        ):
            result = _ensure_alias_storage(None)
            assert result is None


class TestProcessAliasExpansion:
    """Test _process_alias_expansion function."""

    @pytest.mark.asyncio
    async def test_process_alias_expansion_no_alias_storage(self):
        """Test _process_alias_expansion returns None when no alias storage."""
        result = await _process_alias_expansion("cmd", [], None, "testplayer", {}, MagicMock())
        assert result is None

    @pytest.mark.asyncio
    async def test_process_alias_expansion_no_alias(self):
        """Test _process_alias_expansion returns None when alias not found."""
        mock_storage = MagicMock()
        mock_storage.get_alias.return_value = None

        result = await _process_alias_expansion("cmd", [], mock_storage, "testplayer", {}, MagicMock())
        assert result is None

    @pytest.mark.asyncio
    async def test_process_alias_expansion_unsafe_alias(self):
        """Test _process_alias_expansion returns error for unsafe alias."""
        mock_storage = MagicMock()
        mock_alias = MagicMock()
        mock_alias.name = "testalias"
        mock_storage.get_alias.return_value = mock_alias

        with (
            patch("server.command_handler_unified.check_alias_safety", return_value=(False, "Unsafe alias", 0)),
        ):
            result = await _process_alias_expansion("testalias", [], mock_storage, "testplayer", {}, MagicMock())
            assert result == {"result": "Unsafe alias"}

    @pytest.mark.asyncio
    async def test_process_alias_expansion_invalid_expanded(self):
        """Test _process_alias_expansion returns error for invalid expanded command."""
        mock_storage = MagicMock()
        mock_alias = MagicMock()
        mock_alias.name = "testalias"
        mock_alias.get_expanded_command.return_value = "invalid; command"
        mock_storage.get_alias.return_value = mock_alias

        with (
            patch("server.command_handler_unified.check_alias_safety", return_value=(True, None, 1)),
            patch("server.command_handler_unified.validate_expanded_command", return_value=(False, "Invalid command")),
        ):
            result = await _process_alias_expansion("testalias", [], mock_storage, "testplayer", {}, MagicMock())
            assert result == {"result": "Invalid command"}


class TestHandleSpecialCommandRouting:
    """Test _handle_special_command_routing function."""

    @pytest.mark.asyncio
    async def test_handle_special_command_routing_alias_command(self):
        """Test _handle_special_command_routing handles alias management commands."""
        mock_storage = MagicMock()
        mock_request = MagicMock()

        with patch(
            "server.command_handler_unified.command_service.process_command", return_value={"result": "Alias set"}
        ):
            result = await _handle_special_command_routing(
                "alias", [], "alias test=look", mock_storage, "testplayer", {}, mock_request
            )
            assert result == {"result": "Alias set"}

    @pytest.mark.asyncio
    async def test_handle_special_command_routing_alias_command_no_storage(self):
        """Test _handle_special_command_routing returns error when alias storage unavailable."""
        result = await _handle_special_command_routing(
            "alias", [], "alias test=look", None, "testplayer", {}, MagicMock()
        )
        assert result == {"result": "Alias system not available"}

    @pytest.mark.asyncio
    async def test_handle_special_command_routing_emote_conversion(self):
        """Test _handle_special_command_routing converts single-word emotes."""
        mock_storage = MagicMock()
        mock_storage.get_alias.return_value = None  # No alias found
        mock_request = MagicMock()

        with (
            patch("server.command_handler_unified._process_alias_expansion", return_value=None),
            patch("server.command_handler_unified.should_treat_as_emote", return_value=True),
            patch(
                "server.command_handler_unified.command_service.process_command", return_value={"result": "Emote sent"}
            ),
        ):
            result = await _handle_special_command_routing(
                "smile", [], "smile", mock_storage, "testplayer", {}, mock_request
            )
            assert result == {"result": "Emote sent"}
