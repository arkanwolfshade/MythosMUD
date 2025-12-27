"""
Unit tests for system command handlers.

Tests handlers for system-level commands like help.
"""

from unittest.mock import MagicMock, patch

import pytest

from server.commands.system_commands import handle_help_command


@pytest.mark.asyncio
async def test_handle_help_command_no_args():
    """Test handle_help_command returns general help when no arguments."""
    mock_request = MagicMock()
    
    with patch("server.commands.system_commands.get_help_content", return_value="General help content"):
        result = await handle_help_command({}, {}, mock_request, None, "testplayer")
    
    assert result["result"] == "General help content"


@pytest.mark.asyncio
async def test_handle_help_command_with_command_name():
    """Test handle_help_command returns help for specific command."""
    command_data = {"args": ["look"]}
    mock_request = MagicMock()
    
    with patch("server.commands.system_commands.get_help_content", return_value="Look command help"):
        result = await handle_help_command(command_data, {}, mock_request, None, "testplayer")
    
    assert result["result"] == "Look command help"


@pytest.mark.asyncio
async def test_handle_help_command_too_many_args():
    """Test handle_help_command returns usage error when too many arguments."""
    command_data = {"args": ["look", "north", "extra"]}
    mock_request = MagicMock()
    
    result = await handle_help_command(command_data, {}, mock_request, None, "testplayer")
    
    assert "Usage: help" in result["result"]


@pytest.mark.asyncio
async def test_handle_help_command_empty_args():
    """Test handle_help_command handles empty args list."""
    command_data = {"args": []}
    mock_request = MagicMock()
    
    with patch("server.commands.system_commands.get_help_content", return_value="General help"):
        result = await handle_help_command(command_data, {}, mock_request, None, "testplayer")
    
    assert result["result"] == "General help"


@pytest.mark.asyncio
async def test_handle_help_command_missing_args_key():
    """Test handle_help_command handles missing args key."""
    command_data = {}
    mock_request = MagicMock()
    
    with patch("server.commands.system_commands.get_help_content", return_value="General help"):
        result = await handle_help_command(command_data, {}, mock_request, None, "testplayer")
    
    assert result["result"] == "General help"
