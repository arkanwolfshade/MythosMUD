"""
Unit tests for unified command handler.

Tests core command processing, HTTP endpoints, and legacy compatibility.
"""

from typing import Any
from unittest.mock import MagicMock, Mock, patch

import pytest
from fastapi import HTTPException, Request

from server.command_handler_unified import (
    CommandRequest,
    get_help_content,
    handle_command,
    process_command,
    process_command_unified,
)

# pylint: disable=redefined-outer-name  # Reason: Test file - pytest fixture parameter names must match fixture names, causing intentional redefinitions
# pylint: disable=protected-access  # Reason: Test file - accessing protected members is standard practice for unit testing


class TestLegacyFunctions:
    """Test legacy compatibility functions."""

    @pytest.mark.asyncio
    async def test_process_command_legacy(self):
        """Test process_command() legacy function."""
        mock_current_user = {"username": "testuser"}
        mock_request = Mock(spec=Request)
        mock_alias_storage = MagicMock()
        player_name = "testuser"

        with patch("server.command_handler_unified.process_command_unified") as mock_unified:
            mock_unified.return_value = {"result": "Success"}
            result = await process_command(
                cmd="look",
                args=[],
                current_user=mock_current_user,
                request=mock_request,
                alias_storage=mock_alias_storage,
                player_name=player_name,
            )
            assert "result" in result
            mock_unified.assert_awaited_once()

    def test_get_help_content(self):
        """Test get_help_content() delegates to help system."""
        with patch("server.command_handler_unified.get_help_content_new", return_value="Help text"):
            result = get_help_content("look")
            assert result == "Help text"

    def test_get_help_content_none(self):
        """Test get_help_content() with None command."""
        with patch("server.command_handler_unified.get_help_content_new", return_value="General help"):
            result = get_help_content(None)
            assert result == "General help"


class TestProcessCommandUnified:
    """Test process_command_unified function."""

    @pytest.mark.asyncio
    async def test_process_command_unified_rate_limited(self):
        """Test process_command_unified returns rate limit result."""
        mock_request = MagicMock()
        mock_user = {"username": "testplayer"}

        with patch(
            "server.command_handler_unified._prepare_command_for_processing",
            return_value=("", "", [], None, {"result": "Rate limited"}),
        ):
            result = await process_command_unified("look", mock_user, mock_request)
            assert result == {"result": "Rate limited"}

    @pytest.mark.asyncio
    async def test_process_command_unified_blocked(self):
        """Test process_command_unified returns block result."""
        mock_request = MagicMock()
        mock_user = {"username": "testplayer"}

        with (
            patch(
                "server.command_handler_unified._prepare_command_for_processing",
                return_value=("look", "look", [], None, None),
            ),
            patch("server.command_handler_unified._check_all_command_blocks", return_value={"result": "Blocked"}),
        ):
            result = await process_command_unified("look", mock_user, mock_request)
            assert result == {"result": "Blocked"}

    @pytest.mark.asyncio
    async def test_process_command_unified_special_routing(self):
        """Test process_command_unified handles special command routing."""
        mock_request = MagicMock()
        mock_user = {"username": "testplayer"}

        with (
            patch(
                "server.command_handler_unified._prepare_command_for_processing",
                return_value=("alias test=look", "alias", ["test=look"], MagicMock(), None),
            ),
            patch("server.command_handler_unified._check_all_command_blocks", return_value=None),
            patch(
                "server.command_handler_unified._handle_special_command_routing", return_value={"result": "Alias set"}
            ),
        ):
            result = await process_command_unified("alias test=look", mock_user, mock_request)
            assert result == {"result": "Alias set"}

    @pytest.mark.asyncio
    async def test_process_command_unified_normal_processing(self):
        """Test process_command_unified processes normal commands."""
        mock_request = MagicMock()
        mock_user = {"username": "testplayer"}

        with (
            patch(
                "server.command_handler_unified._prepare_command_for_processing",
                return_value=("look", "look", [], None, None),
            ),
            patch("server.command_handler_unified._check_all_command_blocks", return_value=None),
            patch("server.command_handler_unified._handle_special_command_routing", return_value=None),
            patch(
                "server.command_handler_unified.process_command_with_validation",
                return_value={"result": "You look around"},
            ),
        ):
            result = await process_command_unified("look", mock_user, mock_request)
            assert result == {"result": "You look around"}


class TestHandleCommand:
    """Test handle_command HTTP endpoint."""

    @pytest.mark.asyncio
    async def test_handle_command_unauthorized(self):
        """Test handle_command raises HTTPException when not authenticated."""

        mock_request = MagicMock()
        mock_user: dict[str, Any] = {}  # Empty dict represents unauthenticated user

        with pytest.raises(HTTPException, match="Authentication required"):
            await handle_command(CommandRequest(command="look"), mock_request, mock_user)

    @pytest.mark.asyncio
    async def test_handle_command_success(self):
        """Test handle_command successfully processes command."""
        mock_request = MagicMock()
        mock_user = {"username": "testplayer"}

        with patch("server.command_handler_unified.process_command_unified", return_value={"result": "Success"}):
            result = await handle_command(CommandRequest(command="look"), mock_request, mock_user)
            assert result == {"result": "Success"}
