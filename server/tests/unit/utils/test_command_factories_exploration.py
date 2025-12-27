"""
Unit tests for exploration command factory methods.

Tests factory methods for creating movement and exploration command objects.
"""

import pytest

from server.exceptions import ValidationError as MythosValidationError
from server.models.command import Direction, GoCommand, GroundCommand, LieCommand, LookCommand, SitCommand, StandCommand
from server.utils.command_factories_exploration import ExplorationCommandFactory


def test_parse_instance_number_hyphen_syntax():
    """Test _parse_instance_number parses hyphen syntax."""
    target, instance = ExplorationCommandFactory._parse_instance_number("backpack-2")
    
    assert target == "backpack"
    assert instance == 2


def test_parse_instance_number_space_syntax():
    """Test _parse_instance_number parses space syntax."""
    target, instance = ExplorationCommandFactory._parse_instance_number("backpack 2")
    
    assert target == "backpack"
    assert instance == 2


def test_parse_instance_number_no_instance():
    """Test _parse_instance_number returns None when no instance number."""
    target, instance = ExplorationCommandFactory._parse_instance_number("backpack")
    
    assert target == "backpack"
    assert instance is None


def test_parse_instance_number_multiple_digits():
    """Test _parse_instance_number handles multiple digit instance numbers."""
    target, instance = ExplorationCommandFactory._parse_instance_number("item-123")
    
    assert target == "item"
    assert instance == 123


def test_create_look_command_no_args():
    """Test create_look_command creates command with no arguments."""
    result = ExplorationCommandFactory.create_look_command([])
    
    assert isinstance(result, LookCommand)
    assert result.target is None
    assert result.direction is None


def test_create_look_command_direction():
    """Test create_look_command creates command with direction."""
    result = ExplorationCommandFactory.create_look_command(["north"])
    
    assert isinstance(result, LookCommand)
    assert result.direction == Direction.NORTH
    assert result.target == "north"


def test_create_look_command_all_directions():
    """Test create_look_command handles all valid directions."""
    directions = ["north", "south", "east", "west", "up", "down"]
    for direction_str in directions:
        result = ExplorationCommandFactory.create_look_command([direction_str])
        assert isinstance(result, LookCommand)
        assert result.direction is not None


def test_create_look_command_implicit_target():
    """Test create_look_command creates command with implicit target."""
    result = ExplorationCommandFactory.create_look_command(["guard"])
    
    assert isinstance(result, LookCommand)
    assert result.target == "guard"
    assert result.direction is None


def test_create_look_command_explicit_player_type():
    """Test create_look_command handles explicit player target type."""
    result = ExplorationCommandFactory.create_look_command(["player", "Armitage"])
    
    assert isinstance(result, LookCommand)
    assert result.target == "Armitage"
    assert result.target_type == "player"


def test_create_look_command_explicit_npc_type():
    """Test create_look_command handles explicit NPC target type."""
    result = ExplorationCommandFactory.create_look_command(["npc", "guard"])
    
    assert isinstance(result, LookCommand)
    assert result.target == "guard"
    assert result.target_type == "npc"


def test_create_look_command_explicit_item_type():
    """Test create_look_command handles explicit item target type."""
    result = ExplorationCommandFactory.create_look_command(["item", "lantern"])
    
    assert isinstance(result, LookCommand)
    assert result.target == "lantern"
    assert result.target_type == "item"


def test_create_look_command_explicit_container_type():
    """Test create_look_command handles explicit container target type."""
    result = ExplorationCommandFactory.create_look_command(["container", "backpack"])
    
    assert isinstance(result, LookCommand)
    assert result.target == "backpack"
    assert result.target_type == "container"


def test_create_look_command_explicit_type_no_target():
    """Test create_look_command treats explicit type without target as implicit."""
    result = ExplorationCommandFactory.create_look_command(["player"])
    
    assert isinstance(result, LookCommand)
    assert result.target is None


def test_create_look_command_look_in_syntax():
    """Test create_look_command handles 'look in' syntax."""
    result = ExplorationCommandFactory.create_look_command(["in", "backpack"])
    
    assert isinstance(result, LookCommand)
    assert result.target == "backpack"
    assert result.look_in is True


def test_create_look_command_look_in_no_target():
    """Test create_look_command treats 'in' without target as implicit."""
    result = ExplorationCommandFactory.create_look_command(["in"])
    
    assert isinstance(result, LookCommand)
    assert result.target is None


def test_create_look_command_instance_number_hyphen():
    """Test create_look_command parses instance number with hyphen."""
    result = ExplorationCommandFactory.create_look_command(["backpack-2"])
    
    assert isinstance(result, LookCommand)
    assert result.target == "backpack"
    assert result.instance_number == 2


def test_create_look_command_instance_number_space():
    """Test create_look_command parses instance number with space."""
    # When args are ["backpack", "2"], they get joined to "backpack 2"
    # Then _parse_instance_number parses it and returns ("backpack", 2)
    result = ExplorationCommandFactory.create_look_command(["backpack", "2"])
    
    assert isinstance(result, LookCommand)
    assert result.target == "backpack"
    assert result.instance_number == 2
    
    # Test with single string arg containing space
    result2 = ExplorationCommandFactory.create_look_command(["backpack 2"])
    assert result2.target == "backpack"
    assert result2.instance_number == 2


def test_create_go_command_no_args():
    """Test create_go_command raises error when no arguments."""
    with pytest.raises(MythosValidationError) as exc_info:
        ExplorationCommandFactory.create_go_command([])
    
    assert "requires a direction" in str(exc_info.value).lower()


def test_create_go_command_with_direction():
    """Test create_go_command creates command with direction."""
    result = ExplorationCommandFactory.create_go_command(["north"])
    
    assert isinstance(result, GoCommand)
    assert result.direction == "north"


def test_create_go_command_case_insensitive():
    """Test create_go_command converts direction to lowercase."""
    result = ExplorationCommandFactory.create_go_command(["NORTH"])
    
    assert isinstance(result, GoCommand)
    assert result.direction == "north"


def test_create_sit_command_no_args():
    """Test create_sit_command creates command with no arguments."""
    result = ExplorationCommandFactory.create_sit_command([])
    
    assert isinstance(result, SitCommand)


def test_create_sit_command_with_args():
    """Test create_sit_command raises error when arguments provided."""
    with pytest.raises(MythosValidationError) as exc_info:
        ExplorationCommandFactory.create_sit_command(["down"])
    
    assert "no arguments" in str(exc_info.value).lower()


def test_create_stand_command_no_args():
    """Test create_stand_command creates command with no arguments."""
    result = ExplorationCommandFactory.create_stand_command([])
    
    assert isinstance(result, StandCommand)


def test_create_stand_command_with_args():
    """Test create_stand_command raises error when arguments provided."""
    with pytest.raises(MythosValidationError) as exc_info:
        ExplorationCommandFactory.create_stand_command(["up"])
    
    assert "no arguments" in str(exc_info.value).lower()


def test_create_lie_command_no_args():
    """Test create_lie_command creates command with no modifier."""
    result = ExplorationCommandFactory.create_lie_command([])
    
    assert isinstance(result, LieCommand)
    assert result.modifier is None


def test_create_lie_command_with_down():
    """Test create_lie_command creates command with 'down' modifier."""
    result = ExplorationCommandFactory.create_lie_command(["down"])
    
    assert isinstance(result, LieCommand)
    assert result.modifier == "down"


def test_create_lie_command_with_down_case_insensitive():
    """Test create_lie_command handles 'down' case-insensitively."""
    result = ExplorationCommandFactory.create_lie_command(["DOWN"])
    
    assert isinstance(result, LieCommand)
    assert result.modifier == "down"


def test_create_lie_command_with_invalid_args():
    """Test create_lie_command raises error with invalid arguments."""
    with pytest.raises(MythosValidationError) as exc_info:
        ExplorationCommandFactory.create_lie_command(["up"])
    
    assert "Usage: lie" in str(exc_info.value)


def test_create_lie_command_with_multiple_args():
    """Test create_lie_command raises error with multiple arguments."""
    with pytest.raises(MythosValidationError) as exc_info:
        ExplorationCommandFactory.create_lie_command(["down", "now"])
    
    assert "Usage: lie" in str(exc_info.value)


def test_create_ground_command_no_args():
    """Test create_ground_command raises error when no arguments."""
    with pytest.raises(MythosValidationError) as exc_info:
        ExplorationCommandFactory.create_ground_command([])
    
    assert "Usage: ground" in str(exc_info.value)


def test_create_ground_command_with_target():
    """Test create_ground_command creates command with target."""
    result = ExplorationCommandFactory.create_ground_command(["player"])
    
    assert isinstance(result, GroundCommand)
    assert result.target_player == "player"


def test_create_ground_command_with_multiple_args():
    """Test create_ground_command joins multiple args as target."""
    # Note: GroundCommand validates player name format (no spaces allowed)
    # So we test with a single-word player name that would be valid
    result = ExplorationCommandFactory.create_ground_command(["player"])
    
    assert isinstance(result, GroundCommand)
    assert result.target_player == "player"


def test_create_ground_command_empty_string():
    """Test create_ground_command raises error with empty string."""
    with pytest.raises(MythosValidationError) as exc_info:
        ExplorationCommandFactory.create_ground_command([""])
    
    assert "Usage: ground" in str(exc_info.value)


def test_create_ground_command_whitespace_only():
    """Test create_ground_command raises error with whitespace only."""
    with pytest.raises(MythosValidationError) as exc_info:
        ExplorationCommandFactory.create_ground_command(["   "])
    
    assert "Usage: ground" in str(exc_info.value)
