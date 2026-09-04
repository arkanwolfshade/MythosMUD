"""
Unit tests for admin command models.

Tests the admin command models and their validators.
"""

from unittest.mock import patch

import pytest
from pydantic import ValidationError

from server.models.command_admin import (
    GotoCommand,
    NPCCommand,
    ShutdownCommand,
    SummonCommand,
    TeleportCommand,
)
from server.models.command_base import Direction

# --- Tests for NPCCommand ---


def test_npc_command_default_values():
    """Test NPCCommand has correct default values."""
    command = NPCCommand()

    assert command.command_type == "npc"  # type: ignore[comparison-overlap]  # Testing str enum comparison - valid at runtime
    # Reason: Testing default value - mypy sees as unreachable but valid at runtime
    assert command.subcommand is None  # type: ignore[unreachable]
    assert command.args == []


def test_npc_command_with_subcommand():
    """Test NPCCommand can have subcommand."""
    command = NPCCommand(subcommand="spawn")

    assert command.subcommand == "spawn"


def test_npc_command_with_args():
    """Test NPCCommand can have args."""
    command = NPCCommand(subcommand="spawn", args=["npc1", "npc2"])

    assert command.args == ["npc1", "npc2"]


def test_npc_command_subcommand_min_length():
    """Test NPCCommand validates subcommand min length."""
    with pytest.raises(ValidationError):
        NPCCommand(subcommand="")


def test_npc_command_subcommand_max_length():
    """Test NPCCommand validates subcommand max length."""
    long_subcommand = "a" * 31  # Exceeds max_length=30
    with pytest.raises(ValidationError):
        NPCCommand(subcommand=long_subcommand)


# --- Tests for SummonCommand ---


def test_summon_command_required_fields():
    """Test SummonCommand requires prototype_id."""
    command = SummonCommand(prototype_id="test_item_123")

    # Reason: Testing str enum direct comparison - valid at runtime for str enums, but mypy sees as non-overlapping
    assert command.command_type == "summon"  # type: ignore[comparison-overlap]
    # Reason: Testing field value - mypy sees as unreachable but valid at runtime
    assert command.prototype_id == "test_item_123"  # type: ignore[unreachable]
    assert command.quantity == 1  # Default
    assert command.target_type == "item"  # Default


def test_summon_command_validate_prototype_id_valid():
    """Test SummonCommand validates valid prototype_id."""
    valid_ids = ["item123", "item_123", "item-123", "item.123", "Item123"]

    for proto_id in valid_ids:
        command = SummonCommand(prototype_id=proto_id)
        assert command.prototype_id == proto_id.strip()


def test_summon_command_validate_prototype_id_strips():
    """Test SummonCommand strips whitespace from prototype_id."""
    command = SummonCommand(prototype_id="  item123  ")

    assert command.prototype_id == "item123"


def test_summon_command_validate_prototype_id_invalid_characters():
    """Test SummonCommand rejects invalid characters in prototype_id."""
    invalid_ids = ["item 123", "item@123", "item#123", "item$123", "item%123"]

    for proto_id in invalid_ids:
        with pytest.raises(ValidationError) as exc_info:
            SummonCommand(prototype_id=proto_id)

        error_str = str(exc_info.value).lower()
        assert "prototype id" in error_str or "letters, numbers" in error_str or "validation" in error_str


def test_summon_command_quantity_default():
    """Test SummonCommand defaults quantity to 1."""
    command = SummonCommand(prototype_id="item123")

    assert command.quantity == 1


def test_summon_command_quantity_validation_min():
    """Test SummonCommand validates quantity is >= 1."""
    with pytest.raises(ValidationError):
        SummonCommand(prototype_id="item123", quantity=0)


def test_summon_command_quantity_validation_max():
    """Test SummonCommand validates quantity is <= 5."""
    with pytest.raises(ValidationError):
        SummonCommand(prototype_id="item123", quantity=6)


def test_summon_command_quantity_valid_range():
    """Test SummonCommand accepts quantity in valid range."""
    command1 = SummonCommand(prototype_id="item123", quantity=1)
    assert command1.quantity == 1

    command2 = SummonCommand(prototype_id="item123", quantity=5)
    assert command2.quantity == 5

    command3 = SummonCommand(prototype_id="item123", quantity=3)
    assert command3.quantity == 3


def test_summon_command_target_type_default():
    """Test SummonCommand defaults target_type to 'item'."""
    command = SummonCommand(prototype_id="item123")

    assert command.target_type == "item"


def test_summon_command_target_type_npc():
    """Test SummonCommand can have target_type 'npc'."""
    command = SummonCommand(prototype_id="npc123", target_type="npc")

    assert command.target_type == "npc"


def test_summon_command_prototype_id_min_length():
    """Test SummonCommand validates prototype_id min length."""
    with pytest.raises(ValidationError):
        SummonCommand(prototype_id="")


def test_summon_command_prototype_id_max_length():
    """Test SummonCommand validates prototype_id max length."""
    long_id = "a" * 121  # Exceeds max_length=120
    with pytest.raises(ValidationError):
        SummonCommand(prototype_id=long_id)


# --- Tests for TeleportCommand ---


def test_teleport_command_required_fields():
    """Test TeleportCommand requires player_name."""
    with patch("server.models.command_admin.validate_player_name", return_value="TestPlayer"):
        command = TeleportCommand(player_name="TestPlayer")

        assert command.command_type == "teleport"  # type: ignore[comparison-overlap]  # Testing str enum comparison - valid at runtime
        # Reason: Testing field value - mypy sees as unreachable but valid at runtime
        assert command.player_name == "TestPlayer"  # type: ignore[unreachable]
        assert command.direction is None


def test_teleport_command_with_direction():
    """Test TeleportCommand can have optional direction."""
    with patch("server.models.command_admin.validate_player_name", return_value="TestPlayer"):
        command = TeleportCommand(player_name="TestPlayer", direction=Direction.NORTH)

        assert command.direction == Direction.NORTH


def test_teleport_command_validate_player_name_calls_validator():
    """Test TeleportCommand calls validate_player_name."""
    with patch("server.models.command_admin.validate_player_name", return_value="validated") as mock_validator:
        command = TeleportCommand(player_name="test")

        mock_validator.assert_called_once_with("test")
        assert command.player_name == "validated"


def test_teleport_command_validate_direction_valid():
    """Test TeleportCommand validates valid direction."""
    with patch("server.models.command_admin.validate_player_name", return_value="TestPlayer"):
        command = TeleportCommand(player_name="TestPlayer", direction=Direction.SOUTH)

        assert command.direction == Direction.SOUTH


def test_teleport_command_validate_direction_invalid():
    """Test TeleportCommand rejects invalid direction."""
    with patch("server.models.command_admin.validate_player_name", return_value="TestPlayer"):
        with pytest.raises(ValidationError) as exc_info:
            TeleportCommand(player_name="TestPlayer", direction="invalid_direction")

        error_str = str(exc_info.value).lower()
        assert "invalid direction" in error_str or "validation" in error_str


def test_teleport_command_validate_direction_none():
    """Test TeleportCommand accepts None for direction."""
    with patch("server.models.command_admin.validate_player_name", return_value="TestPlayer"):
        command = TeleportCommand(player_name="TestPlayer", direction=None)

        assert command.direction is None


def test_teleport_command_player_name_min_length():
    """Test TeleportCommand validates player_name min length."""
    with patch("server.models.command_admin.validate_player_name", side_effect=ValidationError):
        with pytest.raises(ValidationError):
            TeleportCommand(player_name="")


def test_teleport_command_player_name_max_length():
    """Test TeleportCommand validates player_name max length."""
    long_name = "a" * 51  # Exceeds max_length=50
    with patch("server.models.command_admin.validate_player_name", side_effect=ValidationError):
        with pytest.raises(ValidationError):
            TeleportCommand(player_name=long_name)


# --- Tests for GotoCommand ---


def test_goto_command_required_fields():
    """Test GotoCommand requires player_name."""
    with patch("server.models.command_admin.validate_player_name", return_value="TestPlayer"):
        command = GotoCommand(player_name="TestPlayer")

        # Reason: Testing str enum direct comparison - valid at runtime for str enums, but mypy sees as non-overlapping
        assert command.command_type == "goto"  # type: ignore[comparison-overlap]
        # Reason: Testing field value - mypy sees as unreachable but valid at runtime
        assert command.player_name == "TestPlayer"  # type: ignore[unreachable]


def test_goto_command_validate_player_name_calls_validator():
    """Test GotoCommand calls validate_player_name."""
    with patch("server.models.command_admin.validate_player_name", return_value="validated") as mock_validator:
        command = GotoCommand(player_name="test")

        mock_validator.assert_called_once_with("test")
        assert command.player_name == "validated"


def test_goto_command_player_name_min_length():
    """Test GotoCommand validates player_name min length."""
    with patch("server.models.command_admin.validate_player_name", side_effect=ValidationError):
        with pytest.raises(ValidationError):
            GotoCommand(player_name="")


def test_goto_command_player_name_max_length():
    """Test GotoCommand validates player_name max length."""
    long_name = "a" * 51  # Exceeds max_length=50
    with patch("server.models.command_admin.validate_player_name", side_effect=ValidationError):
        with pytest.raises(ValidationError):
            GotoCommand(player_name=long_name)


# --- Tests for ShutdownCommand ---


def test_shutdown_command_default_values():
    """Test ShutdownCommand has correct default values."""
    command = ShutdownCommand()

    assert command.command_type == "shutdown"  # type: ignore[comparison-overlap]  # Testing str enum comparison - valid at runtime
    # Reason: Testing default value - mypy sees as unreachable but valid at runtime
    assert command.args == []  # type: ignore[unreachable]


def test_shutdown_command_with_args():
    """Test ShutdownCommand can have args."""
    command = ShutdownCommand(args=["30"])

    assert command.args == ["30"]


def test_shutdown_command_with_cancel():
    """Test ShutdownCommand can have cancel arg."""
    command = ShutdownCommand(args=["cancel"])

    assert command.args == ["cancel"]


def test_shutdown_command_with_multiple_args():
    """Test ShutdownCommand can have multiple args."""
    command = ShutdownCommand(args=["30", "reason"])

    assert command.args == ["30", "reason"]
