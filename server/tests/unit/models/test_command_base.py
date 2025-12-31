"""
Unit tests for base command models and enums.

Tests the Direction and CommandType enums, and BaseCommand class.
"""

from enum import Enum

import pytest
from pydantic import ValidationError

from server.models.command_base import BaseCommand, CommandType, Direction

# --- Tests for Direction enum ---


def test_direction_enum_values():
    """Test Direction enum contains all expected values."""
    assert Direction.NORTH == "north"
    assert Direction.SOUTH == "south"
    assert Direction.EAST == "east"
    assert Direction.WEST == "west"
    assert Direction.UP == "up"
    assert Direction.DOWN == "down"
    assert Direction.NORTHEAST == "northeast"
    assert Direction.NORTHWEST == "northwest"
    assert Direction.SOUTHEAST == "southeast"
    assert Direction.SOUTHWEST == "southwest"


def test_direction_enum_all_directions():
    """Test Direction enum contains all 10 expected directions."""
    expected_directions = {
        "north",
        "south",
        "east",
        "west",
        "up",
        "down",
        "northeast",
        "northwest",
        "southeast",
        "southwest",
    }
    actual_directions = {d.value for d in Direction}
    assert actual_directions == expected_directions


def test_direction_enum_string_comparison():
    """Test Direction enum values can be compared to strings."""
    assert Direction.NORTH == "north"
    assert Direction.SOUTH != "north"
    assert Direction.EAST.value == "east"


# --- Tests for CommandType enum ---


def test_command_type_enum_contains_look():
    """Test CommandType enum contains LOOK."""
    assert CommandType.LOOK == "look"
    assert CommandType.LOOK in CommandType


def test_command_type_enum_contains_communication_commands():
    """Test CommandType enum contains communication commands."""
    assert CommandType.SAY == "say"
    assert CommandType.LOCAL == "local"
    assert CommandType.WHISPER == "whisper"
    assert CommandType.REPLY == "reply"
    assert CommandType.EMOTE == "emote"


def test_command_type_enum_contains_exploration_commands():
    """Test CommandType enum contains exploration commands."""
    assert CommandType.LOOK == "look"
    assert CommandType.GO == "go"


def test_command_type_enum_contains_admin_commands():
    """Test CommandType enum contains admin commands."""
    assert CommandType.TELEPORT == "teleport"
    assert CommandType.GOTO == "goto"
    assert CommandType.SUMMON == "summon"
    assert CommandType.SHUTDOWN == "shutdown"
    assert CommandType.NPC == "npc"
    assert CommandType.ADMIN == "admin"


def test_command_type_enum_contains_inventory_commands():
    """Test CommandType enum contains inventory commands."""
    assert CommandType.INVENTORY == "inventory"
    assert CommandType.PICKUP == "pickup"
    assert CommandType.DROP == "drop"
    assert CommandType.EQUIP == "equip"
    assert CommandType.UNEQUIP == "unequip"


def test_command_type_enum_contains_combat_commands():
    """Test CommandType enum contains combat commands."""
    assert CommandType.ATTACK == "attack"
    assert CommandType.PUNCH == "punch"
    assert CommandType.KICK == "kick"
    assert CommandType.STRIKE == "strike"


def test_command_type_enum_contains_magic_commands():
    """Test CommandType enum contains magic commands."""
    assert CommandType.CAST == "cast"
    assert CommandType.SPELL == "spell"
    assert CommandType.SPELLS == "spells"
    assert CommandType.LEARN == "learn"


def test_command_type_enum_string_comparison():
    """Test CommandType enum values can be compared to strings."""
    assert CommandType.LOOK == "look"
    assert CommandType.GO != "look"
    assert CommandType.SAY.value == "say"


# --- Tests for BaseCommand class ---


def test_base_command_instantiation():
    """Test BaseCommand can be instantiated (though it's abstract)."""
    # BaseCommand is a Pydantic BaseModel, so it can be instantiated
    # but it's meant to be subclassed
    command = BaseCommand()
    assert isinstance(command, BaseCommand)


def test_base_command_rejects_extra_fields():
    """Test BaseCommand rejects unknown fields (extra='forbid')."""
    with pytest.raises(ValidationError) as exc_info:
        BaseCommand(unknown_field="value")

    error_str = str(exc_info.value).lower()
    assert "extra" in error_str and ("not permitted" in error_str or "forbidden" in error_str)


def test_base_command_model_config():
    """Test BaseCommand has correct model configuration."""
    command = BaseCommand()
    config = command.model_config

    assert config.get("extra") == "forbid"
    assert config.get("use_enum_values") is True
    assert config.get("validate_assignment") is True


def test_base_command_slots():
    """Test BaseCommand has __slots__ defined."""
    # __slots__ is defined as empty tuple for performance
    assert hasattr(BaseCommand, "__slots__")
    assert BaseCommand.__slots__ == ()


def test_direction_enum_inheritance():
    """Test Direction enum is a string enum."""
    assert issubclass(Direction, str)
    assert issubclass(Direction, Enum)


def test_command_type_enum_inheritance():
    """Test CommandType enum is a string enum."""
    assert issubclass(CommandType, str)
    assert issubclass(CommandType, Enum)
