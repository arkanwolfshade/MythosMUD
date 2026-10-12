"""Tests for the shared command-result builders."""

from server.commands.command_results import command_error
from server.constants.message_category import MessageCategory


def test_command_error_marks_result_as_system_error() -> None:
    assert command_error("Usage: go <direction>") == {
        "result": "Usage: go <direction>",
        "category": MessageCategory.SYSTEM_ERROR,
    }


def test_command_error_returns_independent_dicts() -> None:
    first = command_error("a")
    first["result"] = "changed"
    assert command_error("a")["result"] == "a"
