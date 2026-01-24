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
    assert Direction.NORTH.value == "north"
    assert Direction.SOUTH.value == "south"
    assert Direction.EAST.value == "east"
    assert Direction.WEST.value == "west"
    assert Direction.UP.value == "up"
    assert Direction.DOWN.value == "down"
    assert Direction.NORTHEAST.value == "northeast"
    assert Direction.NORTHWEST.value == "northwest"
    assert Direction.SOUTHEAST.value == "southeast"
    assert Direction.SOUTHWEST.value == "southwest"


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
    assert Direction.NORTH.value == "north"
    # Reason: Testing inequality comparison - mypy sees as non-overlapping but valid at runtime
    assert Direction.SOUTH.value != "north"  # type: ignore[comparison-overlap]
    assert Direction.EAST.value == "east"


# --- Tests for CommandType enum ---


def test_command_type_enum_contains_look():
    """Test CommandType enum contains LOOK."""
    assert CommandType.LOOK == "look"  # type: ignore[comparison-overlap]  # Testing str enum comparison - valid at runtime
    # Reason: Testing enum membership - always true but validates enum structure at runtime
    assert CommandType.LOOK in CommandType  # type: ignore[unreachable]


def test_command_type_enum_contains_communication_commands():
    """Test CommandType enum contains communication commands."""
    assert CommandType.SAY.value == "say"
    assert CommandType.LOCAL.value == "local"
    assert CommandType.WHISPER.value == "whisper"
    assert CommandType.REPLY.value == "reply"
    assert CommandType.EMOTE.value == "emote"


def test_command_type_enum_contains_exploration_commands():
    """Test CommandType enum contains exploration commands."""
    assert CommandType.LOOK.value == "look"
    assert CommandType.GO.value == "go"


def test_command_type_enum_contains_admin_commands():
    """Test CommandType enum contains admin commands."""
    # Reason: Testing str enum direct comparison - valid at runtime for str enums, but mypy sees as non-overlapping
    assert CommandType.TELEPORT == "teleport"  # type: ignore[comparison-overlap]
    # Reason: Testing str enum - mypy sees as unreachable but valid at runtime
    assert CommandType.GOTO == "goto"  # type: ignore[unreachable]
    assert CommandType.SUMMON == "summon"
    assert CommandType.SHUTDOWN == "shutdown"
    assert CommandType.NPC == "npc"
    assert CommandType.ADMIN == "admin"


def test_command_type_enum_contains_inventory_commands():
    """Test CommandType enum contains inventory commands."""
    assert CommandType.INVENTORY.value == "inventory"
    assert CommandType.PICKUP.value == "pickup"
    assert CommandType.DROP.value == "drop"
    assert CommandType.EQUIP.value == "equip"
    assert CommandType.UNEQUIP.value == "unequip"


def test_command_type_enum_contains_combat_commands():
    """Test CommandType enum contains combat commands."""
    assert CommandType.ATTACK.value == "attack"
    assert CommandType.PUNCH.value == "punch"
    assert CommandType.KICK.value == "kick"
    assert CommandType.STRIKE.value == "strike"


def test_command_type_enum_contains_magic_commands():
    """Test CommandType enum contains magic commands."""
    # Reason: Testing str enum direct comparison - valid at runtime for str enums, but mypy sees as non-overlapping
    assert CommandType.CAST == "cast"  # type: ignore[comparison-overlap]
    # Reason: Testing str enum - mypy sees as unreachable but valid at runtime
    assert CommandType.SPELL == "spell"  # type: ignore[unreachable]
    assert CommandType.SPELLS == "spells"
    assert CommandType.LEARN == "learn"


def test_command_type_enum_string_comparison():
    """Test CommandType enum values can be compared to strings."""
    assert CommandType.LOOK.value == "look"
    # Reason: Testing inequality comparison - mypy sees as non-overlapping but valid at runtime
    assert CommandType.GO.value != "look"  # type: ignore[comparison-overlap]
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
        # Reason: Intentionally testing Pydantic validation with extra='forbid' - extra fields should be rejected
        BaseCommand(unknown_field="value")  # type: ignore[call-arg]

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
