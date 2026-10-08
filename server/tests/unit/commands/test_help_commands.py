"""
Unit tests for help command handlers.

Tests the help command functionality, including that the topic survives the real parser path.
"""

from typing import cast

import pytest

from server.commands.help_commands import handle_help_command
from server.utils.command_parser import parse_command
from server.utils.command_processor import CommandProcessor


def _text(result: dict[str, object]) -> str:
    text = result["result"]
    assert isinstance(text, str)
    return text


@pytest.mark.asyncio
async def test_handle_help_command_no_topic():
    """With no topic, help lists the topics and flags the result as HTML."""
    result = await handle_help_command({}, {}, None, None, "TestPlayer")

    assert result["is_html"] is True
    assert "MythosMUD Help" in _text(result)


@pytest.mark.asyncio
async def test_handle_help_command_with_topic():
    """The validated command's topic field selects one entry, not the general listing."""
    result = await handle_help_command({"topic": "look"}, {}, None, None, "TestPlayer")

    assert result["is_html"] is True
    assert "<strong>LOOK</strong>" in _text(result)
    assert "MythosMUD Help" not in _text(result)


@pytest.mark.asyncio
async def test_handle_help_command_positional_arg_fallback():
    """Callers that only supply args still reach the entry."""
    result = await handle_help_command({"args": ["look"]}, {}, None, None, "TestPlayer")

    assert "<strong>LOOK</strong>" in _text(result)


@pytest.mark.asyncio
async def test_handle_help_command_unknown_topic():
    """An unknown topic is reported as not found."""
    result = await handle_help_command({"args": ["nonexistent_topic"]}, {}, None, None, "TestPlayer")

    assert "Topic Not Found" in _text(result)


@pytest.mark.asyncio
async def test_handle_help_command_too_many_args():
    """More than one argument is a usage error."""
    result = await handle_help_command({"args": ["look", "north"]}, {}, None, None, "TestPlayer")

    assert result == {"result": "Usage: help [command]"}


@pytest.mark.asyncio
async def test_handle_help_command_hides_admin_commands_from_players():
    """npc is documented for admins only."""
    player = await handle_help_command({"topic": "npc"}, {}, None, None, "TestPlayer")
    admin = await handle_help_command({"topic": "npc"}, {"is_admin": True}, None, None, "TestAdmin")

    assert "Topic Not Found" in _text(player)
    assert "<strong>NPC</strong>" in _text(admin)


def test_the_topic_survives_extraction_from_the_parsed_command():
    """Regression: extract_command_data dropped `topic`, so `help look` always showed the general listing."""
    data = CommandProcessor().extract_command_data(parse_command("help look"))

    assert cast(object, data["topic"]) == "look"
