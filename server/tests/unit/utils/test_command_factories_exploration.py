"""
Unit tests for exploration command factories.

Tests the ExplorationCommandFactory class methods.
"""

import pytest

from server.exceptions import ValidationError
from server.models.command import Direction
from server.utils.command_factories_exploration import ExplorationCommandFactory


def test_create_go_command():
    """Test create_go_command() creates GoCommand."""
    command = ExplorationCommandFactory.create_go_command(["north"])
    assert command.direction == Direction.NORTH


def test_create_go_command_no_args():
    """Test create_go_command() raises error with no args."""
    with pytest.raises(ValidationError):
        ExplorationCommandFactory.create_go_command([])


def test_create_go_command_invalid_direction():
    """Test create_go_command() raises error with invalid direction."""
    from pydantic import ValidationError as PydanticValidationError

    # Pydantic raises its own ValidationError for enum validation
    with pytest.raises(PydanticValidationError):
        ExplorationCommandFactory.create_go_command(["invalid"])


def test_create_look_command():
    """Test create_look_command() creates LookCommand."""
    command = ExplorationCommandFactory.create_look_command([])
    assert command.target is None


def test_create_look_command_with_target():
    """Test create_look_command() creates LookCommand with target."""
    command = ExplorationCommandFactory.create_look_command(["target"])
    assert command.target == "target"


def test_create_look_command_with_explicit_player_type():
    """Test create_look_command() with explicit player target type."""
    command = ExplorationCommandFactory.create_look_command(["player", "Armitage"])
    assert command.target == "Armitage"
    assert command.target_type == "player"


def test_create_look_command_with_explicit_npc_type():
    """Test create_look_command() with explicit NPC target type."""
    command = ExplorationCommandFactory.create_look_command(["npc", "guard"])
    assert command.target == "guard"
    assert command.target_type == "npc"


def test_create_look_command_with_explicit_item_type():
    """Test create_look_command() with explicit item target type."""
    command = ExplorationCommandFactory.create_look_command(["item", "lantern"])
    assert command.target == "lantern"
    assert command.target_type == "item"


def test_create_look_command_with_explicit_container_type():
    """Test create_look_command() with explicit container target type."""
    command = ExplorationCommandFactory.create_look_command(["container", "backpack"])
    assert command.target == "backpack"
    assert command.target_type == "container"


def test_create_look_command_with_explicit_type_no_target():
    """Test create_look_command() with explicit type but no target."""
    command = ExplorationCommandFactory.create_look_command(["player"])
    assert command.target is None


def test_create_look_command_with_instance_hyphen():
    """Test create_look_command() parses instance number with hyphen syntax."""
    command = ExplorationCommandFactory.create_look_command(["backpack-2"])
    assert command.target == "backpack"
    assert command.instance_number == 2


def test_create_look_command_with_instance_space():
    """Test create_look_command() parses instance number with space syntax."""
    command = ExplorationCommandFactory.create_look_command(["backpack", "2"])
    assert command.target == "backpack"
    assert command.instance_number == 2


def test_create_look_command_with_in_syntax():
    """Test create_look_command() with 'in' container inspection syntax."""
    command = ExplorationCommandFactory.create_look_command(["in", "backpack"])
    assert command.target == "backpack"
    assert command.look_in is True


def test_create_look_command_with_in_no_target():
    """Test create_look_command() with 'in' but no target."""
    command = ExplorationCommandFactory.create_look_command(["in"])
    assert command.target is None


def test_create_look_command_with_direction():
    """Test create_look_command() with direction target."""
    command = ExplorationCommandFactory.create_look_command(["north"])
    assert command.direction == Direction.NORTH
    assert command.target == "north"


def test_create_look_command_with_direction_instance():
    """Test create_look_command() with direction and instance number."""
    command = ExplorationCommandFactory.create_look_command(["north-2"])
    assert command.direction == Direction.NORTH
    assert command.instance_number == 2


def test_create_sit_command():
    """Test create_sit_command() creates SitCommand."""
    command = ExplorationCommandFactory.create_sit_command([])
    assert command is not None


def test_create_sit_command_with_args():
    """Test create_sit_command() raises error with args."""
    with pytest.raises(ValidationError):
        ExplorationCommandFactory.create_sit_command(["chair"])


def test_create_stand_command():
    """Test create_stand_command() creates StandCommand."""
    command = ExplorationCommandFactory.create_stand_command([])
    assert command is not None


def test_create_stand_command_with_args():
    """Test create_stand_command() raises error with args."""
    with pytest.raises(ValidationError):
        ExplorationCommandFactory.create_stand_command(["quickly"])


def test_create_lie_command():
    """Test create_lie_command() creates LieCommand."""
    command = ExplorationCommandFactory.create_lie_command([])
    assert command.modifier is None


def test_create_lie_command_with_down():
    """Test create_lie_command() with 'down' modifier."""
    command = ExplorationCommandFactory.create_lie_command(["down"])
    assert command.modifier == "down"


def test_create_lie_command_with_invalid_args():
    """Test create_lie_command() raises error with invalid args."""
    with pytest.raises(ValidationError):
        ExplorationCommandFactory.create_lie_command(["up"])


def test_create_lie_command_with_multiple_args():
    """Test create_lie_command() raises error with multiple args."""
    with pytest.raises(ValidationError):
        ExplorationCommandFactory.create_lie_command(["down", "quickly"])


def test_create_ground_command():
    """Test create_ground_command() creates GroundCommand."""
    command = ExplorationCommandFactory.create_ground_command(["player"])
    assert command.target_player == "player"


def test_create_ground_command_no_args():
    """Test create_ground_command() raises error with no args."""
    with pytest.raises(ValidationError):
        ExplorationCommandFactory.create_ground_command([])


def test_create_ground_command_empty_target():
    """Test create_ground_command() raises error with empty target."""
    with pytest.raises(ValidationError):
        ExplorationCommandFactory.create_ground_command(["   "])


def test_create_follow_command():
    """Test create_follow_command() creates FollowCommand with target."""
    command = ExplorationCommandFactory.create_follow_command(["Professor", "Armitage"])
    assert command.target == "Professor Armitage"


def test_create_follow_command_no_args():
    """Test create_follow_command() raises error with no args."""
    with pytest.raises(ValidationError):
        ExplorationCommandFactory.create_follow_command([])


def test_create_follow_command_empty_target():
    """Test create_follow_command() raises error with empty target."""
    with pytest.raises(ValidationError):
        ExplorationCommandFactory.create_follow_command(["   "])


def test_create_unfollow_command():
    """Test create_unfollow_command() creates UnfollowCommand with no args."""
    command = ExplorationCommandFactory.create_unfollow_command([])
    assert command is not None


def test_create_unfollow_command_with_args():
    """Test create_unfollow_command() raises error with args."""
    with pytest.raises(ValidationError):
        ExplorationCommandFactory.create_unfollow_command(["extra"])


def test_create_following_command():
    """Test create_following_command() creates FollowingCommand with no args."""
    command = ExplorationCommandFactory.create_following_command([])
    assert command is not None


def test_create_following_command_with_args():
    """Test create_following_command() raises error with args."""
    with pytest.raises(ValidationError):
        ExplorationCommandFactory.create_following_command(["extra"])


def test_create_party_command_no_args():
    """Test create_party_command() with no args returns status-only command."""
    command = ExplorationCommandFactory.create_party_command([])
    assert command.subcommand == ""
    assert command.target is None
    assert command.message is None


def test_create_party_command_invite_with_target():
    """Test create_party_command() with invite and target."""
    command = ExplorationCommandFactory.create_party_command(["invite", "Armitage"])
    assert command.subcommand == "invite"
    assert command.target == "Armitage"
    assert command.message is None


def test_create_party_command_invite_no_target():
    """Test create_party_command() with invite but no target raises."""
    with pytest.raises(ValidationError):
        ExplorationCommandFactory.create_party_command(["invite"])


def test_create_party_command_kick_with_target():
    """Test create_party_command() with kick and target."""
    command = ExplorationCommandFactory.create_party_command(["kick", "SomePlayer"])
    assert command.subcommand == "kick"
    assert command.target == "SomePlayer"
    assert command.message is None


def test_create_party_command_kick_no_target():
    """Test create_party_command() with kick but no target raises."""
    with pytest.raises(ValidationError):
        ExplorationCommandFactory.create_party_command(["kick"])


def test_create_party_command_leave():
    """Test create_party_command() with leave subcommand."""
    command = ExplorationCommandFactory.create_party_command(["leave"])
    assert command.subcommand == "leave"
    assert command.target is None
    assert command.message is None


def test_create_party_command_list():
    """Test create_party_command() with list subcommand."""
    command = ExplorationCommandFactory.create_party_command(["list"])
    assert command.subcommand == "list"
    assert command.target is None
    assert command.message is None


def test_create_party_command_message():
    """Test create_party_command() with message (no subcommand)."""
    command = ExplorationCommandFactory.create_party_command(["hello", "party"])
    assert command.subcommand == ""
    assert command.target is None
    assert command.message == "hello party"
