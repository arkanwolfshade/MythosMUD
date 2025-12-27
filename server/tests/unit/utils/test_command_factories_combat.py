"""
Unit tests for combat command factory methods.

Tests factory methods for creating combat-related command objects.
"""

import pytest

from server.exceptions import ValidationError as MythosValidationError
from server.models.command import AttackCommand, KickCommand, PunchCommand, StrikeCommand
from server.utils.command_factories_combat import CombatCommandFactory


def test_create_attack_command_no_args():
    """Test create_attack_command creates command with no target."""
    result = CombatCommandFactory.create_attack_command([])
    
    assert isinstance(result, AttackCommand)
    assert result.target is None


def test_create_attack_command_with_target():
    """Test create_attack_command creates command with target."""
    result = CombatCommandFactory.create_attack_command(["enemy"])
    
    assert isinstance(result, AttackCommand)
    assert result.target == "enemy"


def test_create_attack_command_with_multiple_args():
    """Test create_attack_command joins multiple args as target."""
    result = CombatCommandFactory.create_attack_command(["the", "enemy", "npc"])
    
    assert isinstance(result, AttackCommand)
    assert result.target == "the enemy npc"


def test_create_punch_command_no_args():
    """Test create_punch_command creates command with no target."""
    result = CombatCommandFactory.create_punch_command([])
    
    assert isinstance(result, PunchCommand)
    assert result.target is None


def test_create_punch_command_with_target():
    """Test create_punch_command creates command with target."""
    result = CombatCommandFactory.create_punch_command(["enemy"])
    
    assert isinstance(result, PunchCommand)
    assert result.target == "enemy"


def test_create_punch_command_with_multiple_args():
    """Test create_punch_command joins multiple args as target."""
    result = CombatCommandFactory.create_punch_command(["the", "enemy"])
    
    assert isinstance(result, PunchCommand)
    assert result.target == "the enemy"


def test_create_kick_command_no_args():
    """Test create_kick_command creates command with no target."""
    result = CombatCommandFactory.create_kick_command([])
    
    assert isinstance(result, KickCommand)
    assert result.target is None


def test_create_kick_command_with_target():
    """Test create_kick_command creates command with target."""
    result = CombatCommandFactory.create_kick_command(["enemy"])
    
    assert isinstance(result, KickCommand)
    assert result.target == "enemy"


def test_create_kick_command_with_multiple_args():
    """Test create_kick_command joins multiple args as target."""
    result = CombatCommandFactory.create_kick_command(["the", "enemy", "npc"])
    
    assert isinstance(result, KickCommand)
    assert result.target == "the enemy npc"


def test_create_strike_command_no_args():
    """Test create_strike_command creates command with no target."""
    result = CombatCommandFactory.create_strike_command([])
    
    assert isinstance(result, StrikeCommand)
    assert result.target is None


def test_create_strike_command_with_target():
    """Test create_strike_command creates command with target."""
    result = CombatCommandFactory.create_strike_command(["enemy"])
    
    assert isinstance(result, StrikeCommand)
    assert result.target == "enemy"


def test_create_strike_command_with_multiple_args():
    """Test create_strike_command joins multiple args as target."""
    result = CombatCommandFactory.create_strike_command(["the", "enemy"])
    
    assert isinstance(result, StrikeCommand)
    assert result.target == "the enemy"
