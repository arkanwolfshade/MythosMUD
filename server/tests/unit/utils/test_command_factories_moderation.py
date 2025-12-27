"""
Unit tests for moderation command factories.

Tests factory methods for moderation commands.
"""

import pytest

from server.exceptions import ValidationError as MythosValidationError
from server.utils.command_factories_moderation import ModerationCommandFactory


def test_create_mute_command_no_args():
    """Test create_mute_command raises error with no arguments."""
    with pytest.raises(MythosValidationError, match="requires a player name"):
        ModerationCommandFactory.create_mute_command([])


def test_create_mute_command_with_player_name():
    """Test create_mute_command with player name only."""
    result = ModerationCommandFactory.create_mute_command(["TestPlayer"])
    
    assert result.player_name == "TestPlayer"
    assert result.duration_minutes is None
    assert result.reason is None


def test_create_mute_command_with_duration():
    """Test create_mute_command with player name and duration."""
    result = ModerationCommandFactory.create_mute_command(["TestPlayer", "60"])
    
    assert result.player_name == "TestPlayer"
    assert result.duration_minutes == 60
    assert result.reason is None


def test_create_mute_command_with_duration_and_reason():
    """Test create_mute_command with player name, duration, and reason."""
    result = ModerationCommandFactory.create_mute_command(["TestPlayer", "60", "spam"])
    
    assert result.player_name == "TestPlayer"
    assert result.duration_minutes == 60
    assert result.reason == "spam"


def test_create_mute_command_with_multi_word_reason():
    """Test create_mute_command with multi-word reason."""
    result = ModerationCommandFactory.create_mute_command(["TestPlayer", "60", "spam", "and", "harassment"])
    
    assert result.player_name == "TestPlayer"
    assert result.duration_minutes == 60
    assert result.reason == "spam and harassment"


def test_create_mute_command_with_reason_no_duration():
    """Test create_mute_command with reason but no duration."""
    result = ModerationCommandFactory.create_mute_command(["TestPlayer", "spam"])
    
    assert result.player_name == "TestPlayer"
    assert result.duration_minutes is None
    assert result.reason == "spam"


def test_create_unmute_command_no_args():
    """Test create_unmute_command raises error with no arguments."""
    with pytest.raises(MythosValidationError, match="requires a player name"):
        ModerationCommandFactory.create_unmute_command([])


def test_create_unmute_command_with_player_name():
    """Test create_unmute_command with player name."""
    result = ModerationCommandFactory.create_unmute_command(["TestPlayer"])
    
    assert result.player_name == "TestPlayer"


def test_create_unmute_command_too_many_args():
    """Test create_unmute_command raises error with too many arguments."""
    with pytest.raises(MythosValidationError, match="only one argument"):
        ModerationCommandFactory.create_unmute_command(["TestPlayer", "extra"])


def test_create_mute_global_command_no_args():
    """Test create_mute_global_command raises error with no arguments."""
    with pytest.raises(MythosValidationError, match="requires a player name"):
        ModerationCommandFactory.create_mute_global_command([])


def test_create_mute_global_command_with_player_name():
    """Test create_mute_global_command with player name only."""
    result = ModerationCommandFactory.create_mute_global_command(["TestPlayer"])
    
    assert result.player_name == "TestPlayer"
    assert result.duration_minutes is None
    assert result.reason is None


def test_create_mute_global_command_with_duration():
    """Test create_mute_global_command with player name and duration."""
    result = ModerationCommandFactory.create_mute_global_command(["TestPlayer", "60"])
    
    assert result.player_name == "TestPlayer"
    assert result.duration_minutes == 60
    assert result.reason is None


def test_create_mute_global_command_with_duration_and_reason():
    """Test create_mute_global_command with player name, duration, and reason."""
    result = ModerationCommandFactory.create_mute_global_command(["TestPlayer", "60", "spam"])
    
    assert result.player_name == "TestPlayer"
    assert result.duration_minutes == 60
    assert result.reason == "spam"


def test_create_unmute_global_command_no_args():
    """Test create_unmute_global_command raises error with no arguments."""
    with pytest.raises(MythosValidationError, match="requires a player name"):
        ModerationCommandFactory.create_unmute_global_command([])


def test_create_unmute_global_command_with_player_name():
    """Test create_unmute_global_command with player name."""
    result = ModerationCommandFactory.create_unmute_global_command(["TestPlayer"])
    
    assert result.player_name == "TestPlayer"


def test_create_unmute_global_command_too_many_args():
    """Test create_unmute_global_command raises error with too many arguments."""
    with pytest.raises(MythosValidationError, match="only one argument"):
        ModerationCommandFactory.create_unmute_global_command(["TestPlayer", "extra"])


def test_create_mutes_command_no_args():
    """Test create_mutes_command with no arguments."""
    result = ModerationCommandFactory.create_mutes_command([])
    
    assert result is not None
    assert hasattr(result, "command_type")


def test_create_mutes_command_with_args():
    """Test create_mutes_command raises error with arguments."""
    with pytest.raises(MythosValidationError, match="takes no arguments"):
        ModerationCommandFactory.create_mutes_command(["extra"])


def test_create_add_admin_command_no_args():
    """Test create_add_admin_command raises error with no arguments."""
    with pytest.raises(MythosValidationError, match="requires a player name"):
        ModerationCommandFactory.create_add_admin_command([])


def test_create_add_admin_command_with_player_name():
    """Test create_add_admin_command with player name."""
    result = ModerationCommandFactory.create_add_admin_command(["TestPlayer"])
    
    assert result.player_name == "TestPlayer"


def test_create_add_admin_command_too_many_args():
    """Test create_add_admin_command raises error with too many arguments."""
    with pytest.raises(MythosValidationError, match="only one argument"):
        ModerationCommandFactory.create_add_admin_command(["TestPlayer", "extra"])


def test_create_admin_command_no_args():
    """Test create_admin_command raises error with no arguments."""
    with pytest.raises(MythosValidationError, match="requires a subcommand"):
        ModerationCommandFactory.create_admin_command([])


def test_create_admin_command_with_subcommand():
    """Test create_admin_command with subcommand."""
    result = ModerationCommandFactory.create_admin_command(["status"])
    
    assert result.subcommand == "status"
    assert result.args == []


def test_create_admin_command_status_with_args():
    """Test create_admin_command raises error when status subcommand has args."""
    with pytest.raises(MythosValidationError, match="does not accept additional arguments"):
        ModerationCommandFactory.create_admin_command(["status", "extra"])


def test_create_admin_command_subcommand_lowercase():
    """Test create_admin_command lowercases subcommand."""
    result = ModerationCommandFactory.create_admin_command(["STATUS"])
    
    assert result.subcommand == "status"
