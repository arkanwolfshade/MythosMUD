"""
Unit tests for combat command factories.

Tests the CombatCommandFactory class methods.
"""

import pytest

from server.exceptions import ValidationError
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
