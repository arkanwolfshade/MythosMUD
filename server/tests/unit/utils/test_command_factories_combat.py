"""
Unit tests for combat command factories.

Tests the CombatCommandFactory class methods.
"""

from server.utils.command_factories_combat import CombatCommandFactory


def test_create_attack_command():
    """Test create_attack_command() creates AttackCommand."""
    command = CombatCommandFactory.create_attack_command(["target"])
    assert command.target == "target"
    assert command.command_type.value == "attack"


def test_create_attack_command_no_args():
    """Test create_attack_command() allows None target (validation happens later)."""
    command = CombatCommandFactory.create_attack_command([])
    assert command.target is None
    assert command.command_type.value == "attack"


def test_create_punch_command():
    """Test create_punch_command() creates PunchCommand."""
    command = CombatCommandFactory.create_punch_command(["target"])
    assert command.target == "target"
    assert command.command_type.value == "punch"


def test_create_punch_command_no_args():
    """Test create_punch_command() allows None target (validation happens later)."""
    command = CombatCommandFactory.create_punch_command([])
    assert command.target is None
    assert command.command_type.value == "punch"


def test_create_kick_command():
    """Test create_kick_command() creates KickCommand."""
    command = CombatCommandFactory.create_kick_command(["target"])
    assert command.target == "target"
    assert command.command_type.value == "kick"


def test_create_kick_command_no_args():
    """Test create_kick_command() allows None target (validation happens later)."""
    command = CombatCommandFactory.create_kick_command([])
    assert command.target is None
    assert command.command_type.value == "kick"


def test_create_strike_command():
    """Test create_strike_command() creates StrikeCommand."""
    command = CombatCommandFactory.create_strike_command(["target"])
    assert command.target == "target"
    assert command.command_type.value == "strike"


def test_create_strike_command_no_args():
    """Test create_strike_command() allows None target (validation happens later)."""
    command = CombatCommandFactory.create_strike_command([])
    assert command.target is None
    assert command.command_type.value == "strike"


def test_create_flee_command():
    """Test create_flee_command() creates FleeCommand (no arguments)."""
    command = CombatCommandFactory.create_flee_command([])
    assert command.command_type.value == "flee"


def test_create_taunt_command():
    """Test create_taunt_command() creates TauntCommand with target."""
    command = CombatCommandFactory.create_taunt_command(["npc_name"])
    assert command.target == "npc_name"
    assert command.command_type.value == "taunt"


def test_create_taunt_command_no_args():
    """Test create_taunt_command() allows None target (validation happens later)."""
    command = CombatCommandFactory.create_taunt_command([])
    assert command.target is None
    assert command.command_type.value == "taunt"
