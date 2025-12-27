"""
Unit tests for command factory methods.

Tests the CommandFactory class that delegates to specialized factory classes.
"""

from unittest.mock import MagicMock, patch

import pytest

from server.utils.command_factories import CommandFactory


@pytest.fixture
def command_factory():
    """Create a CommandFactory instance."""
    return CommandFactory()


def test_command_factory_initialization(command_factory):
    """Test CommandFactory initializes with all sub-factories."""
    assert command_factory._communication is not None
    assert command_factory._exploration is not None
    assert command_factory._inventory is not None
    assert command_factory._moderation is not None
    assert command_factory._player_state is not None
    assert command_factory._combat is not None
    assert command_factory._utility is not None


def test_create_say_command(command_factory):
    """Test create_say_command delegates to communication factory."""
    with patch.object(command_factory._communication, "create_say_command", return_value=MagicMock()) as mock_create:
        args = ["hello", "world"]
        result = command_factory.create_say_command(args)
        mock_create.assert_called_once_with(args)
        assert result is not None


def test_create_local_command(command_factory):
    """Test create_local_command delegates to communication factory."""
    with patch.object(command_factory._communication, "create_local_command", return_value=MagicMock()) as mock_create:
        args = ["hello"]
        result = command_factory.create_local_command(args)
        mock_create.assert_called_once_with(args)
        assert result is not None


def test_create_system_command(command_factory):
    """Test create_system_command delegates to communication factory."""
    with patch.object(command_factory._communication, "create_system_command", return_value=MagicMock()) as mock_create:
        args = ["message"]
        result = command_factory.create_system_command(args)
        mock_create.assert_called_once_with(args)
        assert result is not None


def test_create_emote_command(command_factory):
    """Test create_emote_command delegates to communication factory."""
    with patch.object(command_factory._communication, "create_emote_command", return_value=MagicMock()) as mock_create:
        args = ["waves"]
        result = command_factory.create_emote_command(args)
        mock_create.assert_called_once_with(args)
        assert result is not None


def test_create_me_command(command_factory):
    """Test create_me_command delegates to communication factory."""
    with patch.object(command_factory._communication, "create_me_command", return_value=MagicMock()) as mock_create:
        args = ["does something"]
        result = command_factory.create_me_command(args)
        mock_create.assert_called_once_with(args)
        assert result is not None


def test_create_pose_command(command_factory):
    """Test create_pose_command delegates to communication factory."""
    with patch.object(command_factory._communication, "create_pose_command", return_value=MagicMock()) as mock_create:
        args = ["is standing"]
        result = command_factory.create_pose_command(args)
        mock_create.assert_called_once_with(args)
        assert result is not None


def test_create_whisper_command(command_factory):
    """Test create_whisper_command delegates to communication factory."""
    with patch.object(command_factory._communication, "create_whisper_command", return_value=MagicMock()) as mock_create:
        args = ["player", "message"]
        result = command_factory.create_whisper_command(args)
        mock_create.assert_called_once_with(args)
        assert result is not None


def test_create_reply_command(command_factory):
    """Test create_reply_command delegates to communication factory."""
    with patch.object(command_factory._communication, "create_reply_command", return_value=MagicMock()) as mock_create:
        args = ["message"]
        result = command_factory.create_reply_command(args)
        mock_create.assert_called_once_with(args)
        assert result is not None


def test_create_look_command(command_factory):
    """Test create_look_command delegates to exploration factory."""
    with patch.object(command_factory._exploration, "create_look_command", return_value=MagicMock()) as mock_create:
        args = []
        result = command_factory.create_look_command(args)
        mock_create.assert_called_once_with(args)
        assert result is not None


def test_create_go_command(command_factory):
    """Test create_go_command delegates to exploration factory."""
    with patch.object(command_factory._exploration, "create_go_command", return_value=MagicMock()) as mock_create:
        args = ["north"]
        result = command_factory.create_go_command(args)
        mock_create.assert_called_once_with(args)
        assert result is not None


def test_create_sit_command(command_factory):
    """Test create_sit_command delegates to exploration factory."""
    with patch.object(command_factory._exploration, "create_sit_command", return_value=MagicMock()) as mock_create:
        args = []
        result = command_factory.create_sit_command(args)
        mock_create.assert_called_once_with(args)
        assert result is not None


def test_create_stand_command(command_factory):
    """Test create_stand_command delegates to exploration factory."""
    with patch.object(command_factory._exploration, "create_stand_command", return_value=MagicMock()) as mock_create:
        args = []
        result = command_factory.create_stand_command(args)
        mock_create.assert_called_once_with(args)
        assert result is not None


def test_create_lie_command(command_factory):
    """Test create_lie_command delegates to exploration factory."""
    with patch.object(command_factory._exploration, "create_lie_command", return_value=MagicMock()) as mock_create:
        args = []
        result = command_factory.create_lie_command(args)
        mock_create.assert_called_once_with(args)
        assert result is not None


def test_create_ground_command(command_factory):
    """Test create_ground_command delegates to exploration factory."""
    with patch.object(command_factory._exploration, "create_ground_command", return_value=MagicMock()) as mock_create:
        args = []
        result = command_factory.create_ground_command(args)
        mock_create.assert_called_once_with(args)
        assert result is not None


def test_create_inventory_command(command_factory):
    """Test create_inventory_command delegates to inventory factory."""
    with patch.object(command_factory._inventory, "create_inventory_command", return_value=MagicMock()) as mock_create:
        args = []
        result = command_factory.create_inventory_command(args)
        mock_create.assert_called_once_with(args)
        assert result is not None


def test_create_pickup_command(command_factory):
    """Test create_pickup_command delegates to inventory factory."""
    with patch.object(command_factory._inventory, "create_pickup_command", return_value=MagicMock()) as mock_create:
        args = ["item"]
        result = command_factory.create_pickup_command(args)
        mock_create.assert_called_once_with(args)
        assert result is not None


def test_create_drop_command(command_factory):
    """Test create_drop_command delegates to inventory factory."""
    with patch.object(command_factory._inventory, "create_drop_command", return_value=MagicMock()) as mock_create:
        args = ["item"]
        result = command_factory.create_drop_command(args)
        mock_create.assert_called_once_with(args)
        assert result is not None


def test_create_put_command(command_factory):
    """Test create_put_command delegates to inventory factory."""
    with patch.object(command_factory._inventory, "create_put_command", return_value=MagicMock()) as mock_create:
        args = ["item", "container"]
        result = command_factory.create_put_command(args)
        mock_create.assert_called_once_with(args)
        assert result is not None


def test_create_get_command(command_factory):
    """Test create_get_command delegates to inventory factory."""
    with patch.object(command_factory._inventory, "create_get_command", return_value=MagicMock()) as mock_create:
        args = ["item", "container"]
        result = command_factory.create_get_command(args)
        mock_create.assert_called_once_with(args)
        assert result is not None


def test_create_equip_command(command_factory):
    """Test create_equip_command delegates to inventory factory."""
    with patch.object(command_factory._inventory, "create_equip_command", return_value=MagicMock()) as mock_create:
        args = ["item"]
        result = command_factory.create_equip_command(args)
        mock_create.assert_called_once_with(args)
        assert result is not None


def test_create_unequip_command(command_factory):
    """Test create_unequip_command delegates to inventory factory."""
    with patch.object(command_factory._inventory, "create_unequip_command", return_value=MagicMock()) as mock_create:
        args = ["item"]
        result = command_factory.create_unequip_command(args)
        mock_create.assert_called_once_with(args)
        assert result is not None


def test_create_mute_command(command_factory):
    """Test create_mute_command delegates to moderation factory."""
    with patch.object(command_factory._moderation, "create_mute_command", return_value=MagicMock()) as mock_create:
        args = ["player"]
        result = command_factory.create_mute_command(args)
        mock_create.assert_called_once_with(args)
        assert result is not None


def test_create_unmute_command(command_factory):
    """Test create_unmute_command delegates to moderation factory."""
    with patch.object(command_factory._moderation, "create_unmute_command", return_value=MagicMock()) as mock_create:
        args = ["player"]
        result = command_factory.create_unmute_command(args)
        mock_create.assert_called_once_with(args)
        assert result is not None


def test_create_mute_global_command(command_factory):
    """Test create_mute_global_command delegates to moderation factory."""
    with patch.object(command_factory._moderation, "create_mute_global_command", return_value=MagicMock()) as mock_create:
        args = ["player"]
        result = command_factory.create_mute_global_command(args)
        mock_create.assert_called_once_with(args)
        assert result is not None


def test_create_unmute_global_command(command_factory):
    """Test create_unmute_global_command delegates to moderation factory."""
    with patch.object(command_factory._moderation, "create_unmute_global_command", return_value=MagicMock()) as mock_create:
        args = ["player"]
        result = command_factory.create_unmute_global_command(args)
        mock_create.assert_called_once_with(args)
        assert result is not None


def test_create_add_admin_command(command_factory):
    """Test create_add_admin_command delegates to moderation factory."""
    with patch.object(command_factory._moderation, "create_add_admin_command", return_value=MagicMock()) as mock_create:
        args = ["player"]
        result = command_factory.create_add_admin_command(args)
        mock_create.assert_called_once_with(args)
        assert result is not None


def test_create_admin_command(command_factory):
    """Test create_admin_command delegates to moderation factory."""
    with patch.object(command_factory._moderation, "create_admin_command", return_value=MagicMock()) as mock_create:
        args = []
        result = command_factory.create_admin_command(args)
        mock_create.assert_called_once_with(args)
        assert result is not None


def test_create_mutes_command(command_factory):
    """Test create_mutes_command delegates to moderation factory."""
    with patch.object(command_factory._moderation, "create_mutes_command", return_value=MagicMock()) as mock_create:
        args = []
        result = command_factory.create_mutes_command(args)
        mock_create.assert_called_once_with(args)
        assert result is not None


def test_create_status_command(command_factory):
    """Test create_status_command delegates to player_state factory."""
    with patch.object(command_factory._player_state, "create_status_command", return_value=MagicMock()) as mock_create:
        args = []
        result = command_factory.create_status_command(args)
        mock_create.assert_called_once_with(args)
        assert result is not None


def test_create_time_command(command_factory):
    """Test create_time_command delegates to player_state factory."""
    with patch.object(command_factory._player_state, "create_time_command", return_value=MagicMock()) as mock_create:
        args = []
        result = command_factory.create_time_command(args)
        mock_create.assert_called_once_with(args)
        assert result is not None


def test_create_whoami_command(command_factory):
    """Test create_whoami_command delegates to player_state factory."""
    with patch.object(command_factory._player_state, "create_whoami_command", return_value=MagicMock()) as mock_create:
        args = []
        result = command_factory.create_whoami_command(args)
        mock_create.assert_called_once_with(args)
        assert result is not None


def test_create_who_command(command_factory):
    """Test create_who_command delegates to player_state factory."""
    with patch.object(command_factory._player_state, "create_who_command", return_value=MagicMock()) as mock_create:
        args = []
        result = command_factory.create_who_command(args)
        mock_create.assert_called_once_with(args)
        assert result is not None


def test_create_quit_command(command_factory):
    """Test create_quit_command delegates to player_state factory."""
    with patch.object(command_factory._player_state, "create_quit_command", return_value=MagicMock()) as mock_create:
        args = []
        result = command_factory.create_quit_command(args)
        mock_create.assert_called_once_with(args)
        assert result is not None


def test_create_logout_command(command_factory):
    """Test create_logout_command delegates to player_state factory."""
    with patch.object(command_factory._player_state, "create_logout_command", return_value=MagicMock()) as mock_create:
        args = []
        result = command_factory.create_logout_command(args)
        mock_create.assert_called_once_with(args)
        assert result is not None


def test_create_attack_command(command_factory):
    """Test create_attack_command delegates to combat factory."""
    with patch.object(command_factory._combat, "create_attack_command", return_value=MagicMock()) as mock_create:
        args = ["target"]
        result = command_factory.create_attack_command(args)
        mock_create.assert_called_once_with(args)
        assert result is not None


def test_create_punch_command(command_factory):
    """Test create_punch_command delegates to combat factory."""
    with patch.object(command_factory._combat, "create_punch_command", return_value=MagicMock()) as mock_create:
        args = ["target"]
        result = command_factory.create_punch_command(args)
        mock_create.assert_called_once_with(args)
        assert result is not None


def test_create_kick_command(command_factory):
    """Test create_kick_command delegates to combat factory."""
    with patch.object(command_factory._combat, "create_kick_command", return_value=MagicMock()) as mock_create:
        args = ["target"]
        result = command_factory.create_kick_command(args)
        mock_create.assert_called_once_with(args)
        assert result is not None


def test_create_strike_command(command_factory):
    """Test create_strike_command delegates to combat factory."""
    with patch.object(command_factory._combat, "create_strike_command", return_value=MagicMock()) as mock_create:
        args = ["target"]
        result = command_factory.create_strike_command(args)
        mock_create.assert_called_once_with(args)
        assert result is not None


def test_create_alias_command(command_factory):
    """Test create_alias_command delegates to utility factory."""
    with patch.object(command_factory._utility, "create_alias_command", return_value=MagicMock()) as mock_create:
        args = ["w", "whisper"]
        result = command_factory.create_alias_command(args)
        mock_create.assert_called_once_with(args)
        assert result is not None


def test_create_aliases_command(command_factory):
    """Test create_aliases_command delegates to utility factory."""
    with patch.object(command_factory._utility, "create_aliases_command", return_value=MagicMock()) as mock_create:
        args = []
        result = command_factory.create_aliases_command(args)
        mock_create.assert_called_once_with(args)
        assert result is not None


def test_create_unalias_command(command_factory):
    """Test create_unalias_command delegates to utility factory."""
    with patch.object(command_factory._utility, "create_unalias_command", return_value=MagicMock()) as mock_create:
        args = ["w"]
        result = command_factory.create_unalias_command(args)
        mock_create.assert_called_once_with(args)
        assert result is not None


def test_create_help_command(command_factory):
    """Test create_help_command delegates to utility factory."""
    with patch.object(command_factory._utility, "create_help_command", return_value=MagicMock()) as mock_create:
        args = []
        result = command_factory.create_help_command(args)
        mock_create.assert_called_once_with(args)
        assert result is not None


def test_create_npc_command(command_factory):
    """Test create_npc_command delegates to utility factory."""
    with patch.object(command_factory._utility, "create_npc_command", return_value=MagicMock()) as mock_create:
        args = ["npc_name"]
        result = command_factory.create_npc_command(args)
        mock_create.assert_called_once_with(args)
        assert result is not None


def test_create_summon_command(command_factory):
    """Test create_summon_command delegates to utility factory."""
    with patch.object(command_factory._utility, "create_summon_command", return_value=MagicMock()) as mock_create:
        args = ["target"]
        result = command_factory.create_summon_command(args)
        mock_create.assert_called_once_with(args)
        assert result is not None


def test_create_teleport_command(command_factory):
    """Test create_teleport_command delegates to utility factory."""
    with patch.object(command_factory._utility, "create_teleport_command", return_value=MagicMock()) as mock_create:
        args = ["target", "room_id"]
        result = command_factory.create_teleport_command(args)
        mock_create.assert_called_once_with(args)
        assert result is not None


def test_create_goto_command(command_factory):
    """Test create_goto_command delegates to utility factory."""
    with patch.object(command_factory._utility, "create_goto_command", return_value=MagicMock()) as mock_create:
        args = ["room_id"]
        result = command_factory.create_goto_command(args)
        mock_create.assert_called_once_with(args)
        assert result is not None


def test_create_shutdown_command(command_factory):
    """Test create_shutdown_command delegates to utility factory."""
    with patch.object(command_factory._utility, "create_shutdown_command", return_value=MagicMock()) as mock_create:
        args = []
        result = command_factory.create_shutdown_command(args)
        mock_create.assert_called_once_with(args)
        assert result is not None


def test_create_cast_command(command_factory):
    """Test create_cast_command delegates to utility factory."""
    with patch.object(command_factory._utility, "create_cast_command", return_value=MagicMock()) as mock_create:
        args = ["spell", "target"]
        result = command_factory.create_cast_command(args)
        mock_create.assert_called_once_with(args)
        assert result is not None


def test_create_spell_command(command_factory):
    """Test create_spell_command delegates to utility factory."""
    with patch.object(command_factory._utility, "create_spell_command", return_value=MagicMock()) as mock_create:
        args = ["spell_name"]
        result = command_factory.create_spell_command(args)
        mock_create.assert_called_once_with(args)
        assert result is not None


def test_create_spells_command(command_factory):
    """Test create_spells_command delegates to utility factory."""
    with patch.object(command_factory._utility, "create_spells_command", return_value=MagicMock()) as mock_create:
        args = []
        result = command_factory.create_spells_command(args)
        mock_create.assert_called_once_with(args)
        assert result is not None


def test_create_learn_command(command_factory):
    """Test create_learn_command delegates to utility factory."""
    with patch.object(command_factory._utility, "create_learn_command", return_value=MagicMock()) as mock_create:
        args = ["spell"]
        result = command_factory.create_learn_command(args)
        mock_create.assert_called_once_with(args)
        assert result is not None
