"""
Unit tests for utility command factories.

Tests factory methods for utility commands.
"""

import pytest

from server.exceptions import ValidationError as MythosValidationError
from server.utils.command_factories_utility import UtilityCommandFactory


def test_create_alias_command_no_args():
    """Test create_alias_command raises error with no arguments."""
    with pytest.raises(MythosValidationError, match="requires an alias name"):
        UtilityCommandFactory.create_alias_command([])


def test_create_alias_command_with_name():
    """Test create_alias_command with alias name only."""
    result = UtilityCommandFactory.create_alias_command(["w"])
    
    assert result.alias_name == "w"
    assert result.command is None


def test_create_alias_command_with_name_and_command():
    """Test create_alias_command with alias name and command."""
    result = UtilityCommandFactory.create_alias_command(["w", "whisper"])
    
    assert result.alias_name == "w"
    assert result.command == "whisper"


def test_create_alias_command_with_multi_word_command():
    """Test create_alias_command with multi-word command."""
    result = UtilityCommandFactory.create_alias_command(["w", "whisper", "player", "hello"])
    
    assert result.alias_name == "w"
    assert result.command == "whisper player hello"


def test_create_aliases_command_no_args():
    """Test create_aliases_command with no arguments."""
    result = UtilityCommandFactory.create_aliases_command([])
    
    assert result is not None
    assert hasattr(result, "command_type")


def test_create_aliases_command_with_args():
    """Test create_aliases_command raises error with arguments."""
    with pytest.raises(MythosValidationError, match="takes no arguments"):
        UtilityCommandFactory.create_aliases_command(["extra"])


def test_create_unalias_command_no_args():
    """Test create_unalias_command raises error with no arguments."""
    with pytest.raises(MythosValidationError, match="requires an alias name"):
        UtilityCommandFactory.create_unalias_command([])


def test_create_unalias_command_with_name():
    """Test create_unalias_command with alias name."""
    result = UtilityCommandFactory.create_unalias_command(["w"])
    
    assert result.alias_name == "w"


def test_create_unalias_command_too_many_args():
    """Test create_unalias_command raises error with too many arguments."""
    with pytest.raises(MythosValidationError, match="only one argument"):
        UtilityCommandFactory.create_unalias_command(["w", "extra"])


def test_create_help_command_no_args():
    """Test create_help_command with no arguments."""
    result = UtilityCommandFactory.create_help_command([])
    
    assert result.topic is None


def test_create_help_command_with_topic():
    """Test create_help_command with topic."""
    result = UtilityCommandFactory.create_help_command(["look"])
    
    assert result.topic == "look"


def test_create_npc_command_no_args():
    """Test create_npc_command with no arguments."""
    result = UtilityCommandFactory.create_npc_command([])
    
    assert result.subcommand is None
    assert result.args == []


def test_create_npc_command_with_subcommand():
    """Test create_npc_command with subcommand."""
    result = UtilityCommandFactory.create_npc_command(["list"])
    
    assert result.subcommand == "list"
    assert result.args == []


def test_create_npc_command_with_subcommand_and_args():
    """Test create_npc_command with subcommand and args."""
    result = UtilityCommandFactory.create_npc_command(["spawn", "goblin", "1"])
    
    assert result.subcommand == "spawn"
    assert result.args == ["goblin", "1"]


def test_create_npc_command_subcommand_lowercase():
    """Test create_npc_command lowercases subcommand."""
    result = UtilityCommandFactory.create_npc_command(["LIST"])
    
    assert result.subcommand == "list"


def test_create_summon_command_no_args():
    """Test create_summon_command raises error with no arguments."""
    with pytest.raises(MythosValidationError, match="Usage"):
        UtilityCommandFactory.create_summon_command([])


def test_create_summon_command_with_prototype_id():
    """Test create_summon_command with prototype ID."""
    result = UtilityCommandFactory.create_summon_command(["goblin_01"])
    
    assert result.prototype_id == "goblin_01"
    assert result.quantity == 1
    assert result.target_type == "item"


def test_create_summon_command_with_quantity():
    """Test create_summon_command with prototype ID and quantity."""
    result = UtilityCommandFactory.create_summon_command(["goblin_01", "5"])
    
    assert result.prototype_id == "goblin_01"
    assert result.quantity == 5
    assert result.target_type == "item"


def test_create_summon_command_with_target_type():
    """Test create_summon_command with prototype ID and target type."""
    result = UtilityCommandFactory.create_summon_command(["goblin_01", "npc"])
    
    assert result.prototype_id == "goblin_01"
    assert result.quantity == 1
    assert result.target_type == "npc"


def test_create_summon_command_with_quantity_and_target_type():
    """Test create_summon_command with prototype ID, quantity, and target type."""
    result = UtilityCommandFactory.create_summon_command(["goblin_01", "5", "npc"])
    
    assert result.prototype_id == "goblin_01"
    assert result.quantity == 5
    assert result.target_type == "npc"


def test_create_summon_command_negative_quantity():
    """Test create_summon_command raises error with negative quantity."""
    with pytest.raises(MythosValidationError, match="positive number"):
        UtilityCommandFactory.create_summon_command(["goblin_01", "-1"])


def test_create_summon_command_zero_quantity():
    """Test create_summon_command raises error with zero quantity."""
    with pytest.raises(MythosValidationError, match="positive number"):
        UtilityCommandFactory.create_summon_command(["goblin_01", "0"])


def test_create_summon_command_invalid_token():
    """Test create_summon_command raises error with invalid token."""
    with pytest.raises(MythosValidationError, match="Usage"):
        UtilityCommandFactory.create_summon_command(["goblin_01", "invalid"])


def test_create_summon_command_extra_args():
    """Test create_summon_command raises error with extra arguments."""
    with pytest.raises(MythosValidationError, match="Usage"):
        UtilityCommandFactory.create_summon_command(["goblin_01", "5", "npc", "extra"])


def test_create_teleport_command_no_args():
    """Test create_teleport_command raises error with no arguments."""
    with pytest.raises(MythosValidationError, match="requires a player name"):
        UtilityCommandFactory.create_teleport_command([])


def test_create_teleport_command_with_player_name():
    """Test create_teleport_command with player name."""
    result = UtilityCommandFactory.create_teleport_command(["TestPlayer"])
    
    assert result.player_name == "TestPlayer"
    assert result.direction is None


def test_create_teleport_command_with_player_and_direction():
    """Test create_teleport_command with player name and direction."""
    result = UtilityCommandFactory.create_teleport_command(["TestPlayer", "north"])
    
    assert result.player_name == "TestPlayer"
    assert result.direction is not None
    assert str(result.direction) == "north"


def test_create_teleport_command_invalid_direction():
    """Test create_teleport_command raises error with invalid direction."""
    with pytest.raises(MythosValidationError, match="valid.*direction"):
        UtilityCommandFactory.create_teleport_command(["TestPlayer", "invalid"])


def test_create_teleport_command_too_many_args():
    """Test create_teleport_command raises error with too many arguments."""
    with pytest.raises(MythosValidationError, match="at most one direction"):
        UtilityCommandFactory.create_teleport_command(["TestPlayer", "north", "extra"])


def test_create_goto_command_no_args():
    """Test create_goto_command raises error with no arguments."""
    with pytest.raises(MythosValidationError, match="requires a player name"):
        UtilityCommandFactory.create_goto_command([])


def test_create_goto_command_with_player_name():
    """Test create_goto_command with player name."""
    result = UtilityCommandFactory.create_goto_command(["TestPlayer"])
    
    assert result.player_name == "TestPlayer"


def test_create_shutdown_command_no_args():
    """Test create_shutdown_command with no arguments."""
    result = UtilityCommandFactory.create_shutdown_command([])
    
    assert result.args == []


def test_create_shutdown_command_with_countdown():
    """Test create_shutdown_command with countdown."""
    result = UtilityCommandFactory.create_shutdown_command(["60"])
    
    assert result.args == ["60"]


def test_create_shutdown_command_with_cancel():
    """Test create_shutdown_command with cancel."""
    result = UtilityCommandFactory.create_shutdown_command(["cancel"])
    
    assert result.args == ["cancel"]


def test_create_learn_command_no_args():
    """Test create_learn_command raises error with no arguments."""
    with pytest.raises(MythosValidationError, match="requires a spell name"):
        UtilityCommandFactory.create_learn_command([])


def test_create_learn_command_with_spell_name():
    """Test create_learn_command with spell name."""
    result = UtilityCommandFactory.create_learn_command(["Fireball"])
    
    assert result.spell_name == "Fireball"


def test_create_learn_command_with_multi_word_spell_name():
    """Test create_learn_command with multi-word spell name."""
    result = UtilityCommandFactory.create_learn_command(["Minor", "Heal"])
    
    assert result.spell_name == "Minor Heal"


def test_create_spell_command_no_args():
    """Test create_spell_command raises error with no arguments."""
    with pytest.raises(MythosValidationError, match="requires a spell name"):
        UtilityCommandFactory.create_spell_command([])


def test_create_spell_command_with_spell_name():
    """Test create_spell_command with spell name."""
    result = UtilityCommandFactory.create_spell_command(["Fireball"])
    
    assert result.spell_name == "Fireball"


def test_create_spells_command_no_args():
    """Test create_spells_command with no arguments."""
    result = UtilityCommandFactory.create_spells_command([])
    
    assert result is not None
    assert hasattr(result, "command_type")


def test_create_cast_command_no_args():
    """Test create_cast_command raises error with no arguments."""
    with pytest.raises(MythosValidationError, match="requires a spell name"):
        UtilityCommandFactory.create_cast_command([])


def test_create_cast_command_with_spell_name():
    """Test create_cast_command with spell name."""
    result = UtilityCommandFactory.create_cast_command(["Fireball"])
    
    assert result.spell_name == "Fireball"
    assert result.target is None


def test_create_cast_command_with_multi_word_spell():
    """Test create_cast_command with multi-word spell name."""
    result = UtilityCommandFactory.create_cast_command(["Minor", "Heal"])
    
    assert result.spell_name == "Minor Heal"
    assert result.target is None
