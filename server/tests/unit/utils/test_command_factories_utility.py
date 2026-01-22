"""
Unit tests for utility command factories.

Tests the UtilityCommandFactory class methods.
"""

import pytest

from server.exceptions import ValidationError
from server.models.command import Direction
from server.utils.command_factories_utility import UtilityCommandFactory


def test_create_alias_command():
    """Test create_alias_command() creates AliasCommand."""
    command = UtilityCommandFactory.create_alias_command(["test_alias", "go", "north"])
    assert command.alias_name == "test_alias"
    assert command.command == "go north"


def test_create_alias_command_no_args():
    """Test create_alias_command() raises error with no args."""
    with pytest.raises(ValidationError):
        UtilityCommandFactory.create_alias_command([])


def test_create_aliases_command():
    """Test create_aliases_command() creates AliasesCommand."""
    command = UtilityCommandFactory.create_aliases_command([])
    assert command is not None


def test_create_aliases_command_with_args():
    """Test create_aliases_command() raises error with args."""
    with pytest.raises(ValidationError):
        UtilityCommandFactory.create_aliases_command(["arg"])


def test_create_unalias_command():
    """Test create_unalias_command() creates UnaliasCommand."""
    command = UtilityCommandFactory.create_unalias_command(["test_alias"])
    assert command.alias_name == "test_alias"


def test_create_unalias_command_no_args():
    """Test create_unalias_command() raises error with no args."""
    with pytest.raises(ValidationError):
        UtilityCommandFactory.create_unalias_command([])


def test_create_help_command():
    """Test create_help_command() creates HelpCommand."""
    command = UtilityCommandFactory.create_help_command(["look"])
    assert command.topic == "look"


def test_create_help_command_no_args():
    """Test create_help_command() creates HelpCommand with no topic."""
    command = UtilityCommandFactory.create_help_command([])
    assert command.topic is None


def test_create_alias_command_no_command():
    """Test create_alias_command() with only alias name."""
    command = UtilityCommandFactory.create_alias_command(["test_alias"])
    assert command.alias_name == "test_alias"
    assert command.command is None


def test_create_unalias_command_multiple_args():
    """Test create_unalias_command() raises error with multiple args."""
    with pytest.raises(ValidationError, match="only one argument"):
        UtilityCommandFactory.create_unalias_command(["alias1", "alias2"])


def test_create_npc_command_no_args():
    """Test create_npc_command() with no args."""
    command = UtilityCommandFactory.create_npc_command([])
    assert command.subcommand is None
    assert command.args == []


def test_create_npc_command_with_subcommand():
    """Test create_npc_command() with subcommand."""
    command = UtilityCommandFactory.create_npc_command(["create", "guard"])
    assert command.subcommand == "create"
    assert command.args == ["guard"]


def test_create_summon_command():
    """Test create_summon_command() creates SummonCommand."""
    command = UtilityCommandFactory.create_summon_command(["prototype_001"])
    assert command.prototype_id == "prototype_001"
    assert command.quantity == 1
    assert command.target_type == "item"


def test_create_summon_command_no_args():
    """Test create_summon_command() raises error with no args."""
    with pytest.raises(ValidationError):
        UtilityCommandFactory.create_summon_command([])


def test_create_summon_command_with_quantity():
    """Test create_summon_command() with quantity."""
    command = UtilityCommandFactory.create_summon_command(["prototype_001", "5"])
    assert command.prototype_id == "prototype_001"
    assert command.quantity == 5
    assert command.target_type == "item"


def test_create_summon_command_with_target_type():
    """Test create_summon_command() with target type."""
    command = UtilityCommandFactory.create_summon_command(["prototype_001", "npc"])
    assert command.prototype_id == "prototype_001"
    assert command.quantity == 1
    assert command.target_type == "npc"


def test_create_summon_command_with_quantity_and_type():
    """Test create_summon_command() with quantity and target type."""
    command = UtilityCommandFactory.create_summon_command(["prototype_001", "5", "npc"])
    assert command.prototype_id == "prototype_001"
    assert command.quantity == 5
    assert command.target_type == "npc"


def test_create_summon_command_invalid_quantity():
    """Test create_summon_command() raises error with invalid quantity."""
    with pytest.raises(ValidationError, match="positive number"):
        UtilityCommandFactory.create_summon_command(["prototype_001", "0"])


def test_create_summon_command_negative_quantity():
    """Test create_summon_command() raises error with negative quantity."""
    with pytest.raises(ValidationError, match="positive number"):
        UtilityCommandFactory.create_summon_command(["prototype_001", "-1"])


def test_create_summon_command_invalid_token():
    """Test create_summon_command() raises error with invalid token."""
    with pytest.raises(ValidationError):
        UtilityCommandFactory.create_summon_command(["prototype_001", "invalid"])


def test_create_summon_command_extra_args():
    """Test create_summon_command() raises error with extra args."""
    with pytest.raises(ValidationError):
        UtilityCommandFactory.create_summon_command(["prototype_001", "5", "npc", "extra"])


def test_create_teleport_command():
    """Test create_teleport_command() creates TeleportCommand."""
    command = UtilityCommandFactory.create_teleport_command(["player"])
    assert command.player_name == "player"
    assert command.direction is None


def test_create_teleport_command_no_args():
    """Test create_teleport_command() raises error with no args."""
    with pytest.raises(ValidationError):
        UtilityCommandFactory.create_teleport_command([])


def test_create_teleport_command_with_direction():
    """Test create_teleport_command() with direction."""
    command = UtilityCommandFactory.create_teleport_command(["player", "north"])
    assert command.player_name == "player"
    assert command.direction == Direction.NORTH


def test_create_teleport_command_too_many_args():
    """Test create_teleport_command() raises error with too many args."""
    with pytest.raises(ValidationError, match="at most one direction"):
        UtilityCommandFactory.create_teleport_command(["player", "north", "extra"])


def test_create_teleport_command_invalid_direction():
    """Test create_teleport_command() raises error with invalid direction."""
    with pytest.raises(ValidationError, match="valid.*direction"):
        UtilityCommandFactory.create_teleport_command(["player", "invalid"])


def test_create_goto_command():
    """Test create_goto_command() creates GotoCommand."""
    command = UtilityCommandFactory.create_goto_command(["player"])
    assert command.player_name == "player"


def test_create_goto_command_no_args():
    """Test create_goto_command() raises error with no args."""
    with pytest.raises(ValidationError):
        UtilityCommandFactory.create_goto_command([])


def test_create_shutdown_command():
    """Test create_shutdown_command() creates ShutdownCommand."""
    command = UtilityCommandFactory.create_shutdown_command([])
    assert command.args == []


def test_create_shutdown_command_with_args():
    """Test create_shutdown_command() with args."""
    command = UtilityCommandFactory.create_shutdown_command(["60"])
    assert command.args == ["60"]


def test_create_cast_command():
    """Test create_cast_command() creates CastCommand."""
    command = UtilityCommandFactory.create_cast_command(["heal"])
    assert command.spell_name == "heal"
    assert command.target is None


def test_create_cast_command_no_args():
    """Test create_cast_command() raises error with no args."""
    with pytest.raises(ValidationError):
        UtilityCommandFactory.create_cast_command([])


def test_create_cast_command_multi_word():
    """Test create_cast_command() with multi-word spell name."""
    command = UtilityCommandFactory.create_cast_command(["basic", "heal"])
    assert command.spell_name == "basic heal"


def test_create_spell_command():
    """Test create_spell_command() creates SpellCommand."""
    command = UtilityCommandFactory.create_spell_command(["heal"])
    assert command.spell_name == "heal"


def test_create_spell_command_no_args():
    """Test create_spell_command() raises error with no args."""
    with pytest.raises(ValidationError):
        UtilityCommandFactory.create_spell_command([])


def test_create_spell_command_multi_word():
    """Test create_spell_command() with multi-word spell name."""
    command = UtilityCommandFactory.create_spell_command(["basic", "heal"])
    assert command.spell_name == "basic heal"


def test_create_spells_command():
    """Test create_spells_command() creates SpellsCommand."""
    command = UtilityCommandFactory.create_spells_command([])
    assert command is not None


def test_create_spells_command_with_args():
    """Test create_spells_command() raises error with args."""
    with pytest.raises(ValidationError):
        UtilityCommandFactory.create_spells_command(["extra"])


def test_create_learn_command():
    """Test create_learn_command() creates LearnCommand."""
    command = UtilityCommandFactory.create_learn_command(["heal"])
    assert command.spell_name == "heal"


def test_create_learn_command_no_args():
    """Test create_learn_command() raises error with no args."""
    with pytest.raises(ValidationError):
        UtilityCommandFactory.create_learn_command([])


def test_create_learn_command_multi_word():
    """Test create_learn_command() with multi-word spell name."""
    command = UtilityCommandFactory.create_learn_command(["basic", "heal"])
    assert command.spell_name == "basic heal"
