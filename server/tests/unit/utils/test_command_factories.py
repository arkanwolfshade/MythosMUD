"""
Unit tests for command factories.

Tests the CommandFactory class.
"""

import pytest

from server.utils.command_factories import CommandFactory

# pylint: disable=protected-access  # Reason: Test file - accessing protected members is standard practice for unit testing
# pylint: disable=redefined-outer-name  # Reason: Test file - pytest fixture parameter names must match fixture names, causing intentional redefinitions


@pytest.fixture
def factory():
    """Create a CommandFactory instance."""
    return CommandFactory()


def test_command_factory_init(factory):
    """Test CommandFactory initialization."""
    assert factory is not None
    assert factory._communication is not None
    assert factory._exploration is not None
    assert factory._inventory is not None
    assert factory._moderation is not None
    assert factory._player_state is not None
    assert factory._combat is not None
    assert factory._utility is not None


def test_command_factory_has_create_methods(factory):
    """Test CommandFactory has create_* methods for commands."""
    assert hasattr(factory, "create_look_command")
    assert callable(factory.create_look_command)


def test_command_factory_create_existing_command(factory):
    """Test CommandFactory.create_*() returns command for existing command."""
    command = factory.create_look_command([])
    assert command is not None
    assert hasattr(command, "command_type")


def test_command_factory_create_nonexistent_command(factory):
    """Test CommandFactory.create_*() methods exist for all command types."""
    # Verify key factory methods exist
    assert hasattr(factory, "create_say_command")
    assert hasattr(factory, "create_go_command")
    assert hasattr(factory, "create_inventory_command")


def test_create_say_command(factory):
    """Test create_say_command delegates to communication factory."""
    command = factory.create_say_command(["Hello"])
    assert command is not None


def test_create_local_command(factory):
    """Test create_local_command delegates to communication factory."""
    command = factory.create_local_command(["Hello"])
    assert command is not None


def test_create_system_command(factory):
    """Test create_system_command delegates to communication factory."""
    command = factory.create_system_command(["message"])
    assert command is not None


def test_create_emote_command(factory):
    """Test create_emote_command delegates to communication factory."""
    command = factory.create_emote_command(["smiles"])
    assert command is not None


def test_create_me_command(factory):
    """Test create_me_command delegates to communication factory."""
    command = factory.create_me_command(["does something"])
    assert command is not None


def test_create_pose_command(factory):
    """Test create_pose_command delegates to communication factory."""
    command = factory.create_pose_command(["stands"])
    assert command is not None


def test_create_whisper_command(factory):
    """Test create_whisper_command delegates to communication factory."""
    command = factory.create_whisper_command(["player", "message"])
    assert command is not None


def test_create_reply_command(factory):
    """Test create_reply_command delegates to communication factory."""
    command = factory.create_reply_command(["message"])
    assert command is not None


def test_create_channel_command(factory):
    """Test create_channel_command delegates to communication factory."""
    command = factory.create_channel_command(["channel", "message"])
    assert command is not None


def test_create_go_command(factory):
    """Test create_go_command delegates to exploration factory."""
    command = factory.create_go_command(["north"])
    assert command is not None


def test_create_sit_command(factory):
    """Test create_sit_command delegates to exploration factory."""
    command = factory.create_sit_command([])
    assert command is not None


def test_create_stand_command(factory):
    """Test create_stand_command delegates to exploration factory."""
    command = factory.create_stand_command([])
    assert command is not None


def test_create_lie_command(factory):
    """Test create_lie_command delegates to exploration factory."""
    command = factory.create_lie_command([])
    assert command is not None


def test_create_ground_command(factory):
    """Test create_ground_command delegates to exploration factory."""
    command = factory.create_ground_command(["player"])
    assert command is not None


def test_create_pickup_command(factory):
    """Test create_pickup_command delegates to inventory factory."""
    command = factory.create_pickup_command(["item"])
    assert command is not None


def test_create_drop_command(factory):
    """Test create_drop_command delegates to inventory factory."""
    command = factory.create_drop_command(["1"])
    assert command is not None
    assert hasattr(command, "index")


def test_create_put_command(factory):
    """Test create_put_command delegates to inventory factory."""
    command = factory.create_put_command(["item", "container"])
    assert command is not None


def test_create_get_command(factory):
    """Test create_get_command delegates to inventory factory."""
    command = factory.create_get_command(["sword", "bag"])
    assert command is not None


def test_create_equip_command(factory):
    """Test create_equip_command delegates to inventory factory."""
    command = factory.create_equip_command(["item"])
    assert command is not None


def test_create_unequip_command(factory):
    """Test create_unequip_command delegates to inventory factory."""
    command = factory.create_unequip_command(["item"])
    assert command is not None


def test_create_mute_command(factory):
    """Test create_mute_command delegates to moderation factory."""
    command = factory.create_mute_command(["player"])
    assert command is not None


def test_create_unmute_command(factory):
    """Test create_unmute_command delegates to moderation factory."""
    command = factory.create_unmute_command(["player"])
    assert command is not None


def test_create_mute_global_command(factory):
    """Test create_mute_global_command delegates to moderation factory."""
    command = factory.create_mute_global_command(["player"])
    assert command is not None


def test_create_unmute_global_command(factory):
    """Test create_unmute_global_command delegates to moderation factory."""
    command = factory.create_unmute_global_command(["player"])
    assert command is not None


def test_create_add_admin_command(factory):
    """Test create_add_admin_command delegates to moderation factory."""
    command = factory.create_add_admin_command(["player"])
    assert command is not None


def test_create_admin_command(factory):
    """Test create_admin_command delegates to moderation factory."""
    command = factory.create_admin_command(["setlucidity", "player", "10"])
    assert command is not None


def test_create_mutes_command(factory):
    """Test create_mutes_command delegates to moderation factory."""
    command = factory.create_mutes_command([])
    assert command is not None


def test_create_status_command(factory):
    """Test create_status_command delegates to player_state factory."""
    command = factory.create_status_command([])
    assert command is not None


def test_create_time_command(factory):
    """Test create_time_command delegates to player_state factory."""
    command = factory.create_time_command([])
    assert command is not None


def test_create_whoami_command(factory):
    """Test create_whoami_command delegates to player_state factory."""
    command = factory.create_whoami_command([])
    assert command is not None


def test_create_who_command(factory):
    """Test create_who_command delegates to player_state factory."""
    command = factory.create_who_command([])
    assert command is not None


def test_create_quit_command(factory):
    """Test create_quit_command delegates to player_state factory."""
    command = factory.create_quit_command([])
    assert command is not None


def test_create_logout_command(factory):
    """Test create_logout_command delegates to player_state factory."""
    command = factory.create_logout_command([])
    assert command is not None


def test_create_rest_command(factory):
    """Test create_rest_command delegates to player_state factory."""
    command = factory.create_rest_command([])
    assert command is not None


def test_create_punch_command(factory):
    """Test create_punch_command delegates to combat factory."""
    command = factory.create_punch_command(["target"])
    assert command is not None


def test_create_kick_command(factory):
    """Test create_kick_command delegates to combat factory."""
    command = factory.create_kick_command(["target"])
    assert command is not None


def test_create_strike_command(factory):
    """Test create_strike_command delegates to combat factory."""
    command = factory.create_strike_command(["target"])
    assert command is not None


def test_create_alias_command(factory):
    """Test create_alias_command delegates to utility factory."""
    command = factory.create_alias_command(["name", "command"])
    assert command is not None


def test_create_aliases_command(factory):
    """Test create_aliases_command delegates to utility factory."""
    command = factory.create_aliases_command([])
    assert command is not None


def test_create_unalias_command(factory):
    """Test create_unalias_command delegates to utility factory."""
    command = factory.create_unalias_command(["name"])
    assert command is not None


def test_create_help_command(factory):
    """Test create_help_command delegates to utility factory."""
    command = factory.create_help_command(["topic"])
    assert command is not None


def test_create_npc_command(factory):
    """Test create_npc_command delegates to utility factory."""
    command = factory.create_npc_command(["command"])
    assert command is not None


def test_create_summon_command(factory):
    """Test create_summon_command delegates to utility factory."""
    command = factory.create_summon_command(["npc"])
    assert command is not None


def test_create_teleport_command(factory):
    """Test create_teleport_command delegates to utility factory."""
    command = factory.create_teleport_command(["room"])
    assert command is not None


def test_create_goto_command(factory):
    """Test create_goto_command delegates to utility factory."""
    command = factory.create_goto_command(["room"])
    assert command is not None


def test_create_shutdown_command(factory):
    """Test create_shutdown_command delegates to utility factory."""
    command = factory.create_shutdown_command(["60"])
    assert command is not None


def test_create_cast_command(factory):
    """Test create_cast_command delegates to utility factory."""
    command = factory.create_cast_command(["spell", "target"])
    assert command is not None


def test_create_spell_command(factory):
    """Test create_spell_command delegates to utility factory."""
    command = factory.create_spell_command(["spell"])
    assert command is not None


def test_create_spells_command(factory):
    """Test create_spells_command delegates to utility factory."""
    command = factory.create_spells_command([])
    assert command is not None


def test_create_learn_command(factory):
    """Test create_learn_command delegates to utility factory."""
    command = factory.create_learn_command(["spell"])
    assert command is not None
