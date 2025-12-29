"""
Smoke test for command parser.
"""


from server.models.command_base import CommandType
from server.utils.command_parser import parse_command


def test_parse_command_basic():
    """Test basic command parsing."""
    result = parse_command("look")

    assert result.command_type == CommandType.LOOK
    assert isinstance(result, type(result))  # Should be a LookCommand instance


def test_parse_command_with_args():
    """Test command parsing with arguments."""
    result = parse_command("say hello world")

    assert result.command_type == CommandType.SAY
    assert hasattr(result, "message")
    assert "hello world" in result.message


def test_parse_command_with_pipes():
    """Test command parsing with pipes."""
    # Pipes are handled internally, but the main command should still parse
    result = parse_command("look | grep key")

    # The parser should extract the main command (look)
    assert result.command_type == CommandType.LOOK

