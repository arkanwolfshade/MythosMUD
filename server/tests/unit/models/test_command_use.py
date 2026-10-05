"""Unit tests for UseCommand and its wiring into the command factory and help (#870)."""

import pytest
from pydantic import ValidationError

from server.models.command import UseCommand
from server.models.command_base import CommandType
from server.utils.command_factories import CommandFactory
from server.utils.command_helpers import get_command_help


def test_use_command_type_is_use() -> None:
    assert UseCommand(index=1).command_type == CommandType.USE


def test_use_command_accepts_index_or_name() -> None:
    assert UseCommand(index=2, search_term=None).index == 2
    assert UseCommand(index=None, search_term="folk tonic").search_term == "folk tonic"


def test_use_command_strips_the_search_term() -> None:
    assert UseCommand(index=None, search_term="  tonic  ").search_term == "tonic"


@pytest.mark.parametrize("index", [0, -1])
def test_use_command_rejects_non_positive_index(index: int) -> None:
    with pytest.raises(ValidationError):
        _ = UseCommand(index=index, search_term=None)


def test_use_command_requires_a_selector() -> None:
    with pytest.raises(ValidationError, match="requires an item number or name"):
        _ = UseCommand(index=None, search_term=None)
    with pytest.raises(ValidationError, match="requires an item number or name"):
        _ = UseCommand(index=None, search_term="   ")


def test_command_factory_builds_use_command() -> None:
    command = CommandFactory().create_use_command(["folk", "tonic"])

    assert isinstance(command, UseCommand)
    assert command.search_term == "folk tonic"


def test_use_has_help_text_naming_its_aliases() -> None:
    help_text = get_command_help(CommandType.USE.value)

    assert help_text.startswith("use ")
    assert "drink" in help_text
    assert "quaff" in help_text
