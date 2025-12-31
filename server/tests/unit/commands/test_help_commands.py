"""
Unit tests for help command handlers.

Tests the help command functionality.
"""

from unittest.mock import MagicMock

import pytest

from server.commands.help_commands import handle_help_command


@pytest.mark.asyncio
async def test_handle_help_command_no_topic():
    """Test handle_help_command() returns general help when no topic."""
    result = await handle_help_command({}, {}, MagicMock(), None, "TestPlayer")
    assert "result" in result
    assert isinstance(result["result"], str)
    assert len(result["result"]) > 0


@pytest.mark.asyncio
async def test_handle_help_command_with_topic():
    """Test handle_help_command() returns help for specific topic."""
    result = await handle_help_command({"topic": "look"}, {}, MagicMock(), None, "TestPlayer")
    assert "result" in result
    assert isinstance(result["result"], str)


@pytest.mark.asyncio
async def test_handle_help_command_unknown_topic():
    """Test handle_help_command() handles unknown topic."""
    result = await handle_help_command({"args": ["nonexistent_topic"]}, {}, MagicMock(), None, "TestPlayer")
    assert "result" in result
    assert "not found" in result["result"].lower() or "command not found" in result["result"].lower()
