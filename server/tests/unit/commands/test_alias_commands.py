"""
Unit tests for alias command handlers.

Tests the alias, aliases, and unalias commands.
"""

from unittest.mock import MagicMock

import pytest

from server.commands.alias_commands import handle_alias_command, handle_aliases_command, handle_unalias_command


@pytest.fixture
def mock_alias_storage():
    """Create a mock alias storage."""
    storage = MagicMock()
    return storage


@pytest.fixture
def mock_alias():
    """Create a mock alias object."""
    alias = MagicMock()
    alias.name = "n"
    alias.command = "go north"
    return alias


@pytest.mark.asyncio
async def test_handle_alias_command_no_storage():
    """Test handle_alias_command when alias storage is not available."""
    result = await handle_alias_command(
        command_data={},
        current_user={},
        request=MagicMock(),
        alias_storage=None,
        player_name="TestPlayer",
    )

    assert "not available" in result["result"]


@pytest.mark.asyncio
async def test_handle_alias_command_no_args():
    """Test handle_alias_command with no arguments."""
    result = await handle_alias_command(
        command_data={"args": []},
        current_user={},
        request=MagicMock(),
        alias_storage=MagicMock(),
        player_name="TestPlayer",
    )

    assert "Usage:" in result["result"]


@pytest.mark.asyncio
async def test_handle_alias_command_view_existing(mock_alias_storage, mock_alias):
    """Test handle_alias_command viewing existing alias."""
    mock_alias_storage.get_alias.return_value = mock_alias

    result = await handle_alias_command(
        command_data={"args": ["n"]},
        current_user={},
        request=MagicMock(),
        alias_storage=mock_alias_storage,
        player_name="TestPlayer",
    )

    assert "Alias 'n' = 'go north'" in result["result"]
    mock_alias_storage.get_alias.assert_called_once_with("TestPlayer", "n")


@pytest.mark.asyncio
async def test_handle_alias_command_view_nonexistent(mock_alias_storage):
    """Test handle_alias_command viewing nonexistent alias."""
    mock_alias_storage.get_alias.return_value = None

    result = await handle_alias_command(
        command_data={"args": ["nonexistent"]},
        current_user={},
        request=MagicMock(),
        alias_storage=mock_alias_storage,
        player_name="TestPlayer",
    )

    assert "No alias found" in result["result"]


@pytest.mark.asyncio
async def test_handle_alias_command_create_from_args(mock_alias_storage):
    """Test handle_alias_command creating alias from args."""
    result = await handle_alias_command(
        command_data={"args": ["move", "go", "north"]},
        current_user={},
        request=MagicMock(),
        alias_storage=mock_alias_storage,
        player_name="TestPlayer",
    )

    assert "created successfully" in result["result"]
    mock_alias_storage.create_alias.assert_called_once_with("TestPlayer", "move", "go north")


@pytest.mark.asyncio
async def test_handle_alias_command_create_from_structured_data(mock_alias_storage):
    """Test handle_alias_command creating alias from structured data."""
    result = await handle_alias_command(
        command_data={"alias_name": "move", "command": "go north"},
        current_user={},
        request=MagicMock(),
        alias_storage=mock_alias_storage,
        player_name="TestPlayer",
    )

    assert "created successfully" in result["result"]
    mock_alias_storage.create_alias.assert_called_once_with("TestPlayer", "move", "go north")


@pytest.mark.asyncio
async def test_handle_alias_command_invalid_name_too_long(mock_alias_storage):
    """Test handle_alias_command with alias name too long."""
    long_name = "a" * 21
    result = await handle_alias_command(
        command_data={"alias_name": long_name, "command": "go north"},
        current_user={},
        request=MagicMock(),
        alias_storage=mock_alias_storage,
        player_name="TestPlayer",
    )

    assert "1-20 characters" in result["result"]


@pytest.mark.asyncio
async def test_handle_alias_command_invalid_command_too_long(mock_alias_storage):
    """Test handle_alias_command with command too long."""
    long_command = "a" * 201
    result = await handle_alias_command(
        command_data={"alias_name": "n", "command": long_command},
        current_user={},
        request=MagicMock(),
        alias_storage=mock_alias_storage,
        player_name="TestPlayer",
    )

    assert "1-200 characters" in result["result"]


@pytest.mark.asyncio
async def test_handle_alias_command_circular_reference(mock_alias_storage):
    """Test handle_alias_command with circular reference."""
    result = await handle_alias_command(
        command_data={"alias_name": "n", "command": "n"},
        current_user={},
        request=MagicMock(),
        alias_storage=mock_alias_storage,
        player_name="TestPlayer",
    )

    assert "cannot reference itself" in result["result"]


@pytest.mark.asyncio
async def test_handle_alias_command_create_error(mock_alias_storage):
    """Test handle_alias_command when creation fails."""
    mock_alias_storage.create_alias.side_effect = Exception("Storage error")

    result = await handle_alias_command(
        command_data={"alias_name": "move", "command": "go north"},
        current_user={},
        request=MagicMock(),
        alias_storage=mock_alias_storage,
        player_name="TestPlayer",
    )

    assert "Failed to create alias" in result["result"]


@pytest.mark.asyncio
async def test_handle_aliases_command_no_storage():
    """Test handle_aliases_command when alias storage is not available."""
    result = await handle_aliases_command(
        command_data={},
        current_user={},
        request=MagicMock(),
        alias_storage=None,
        player_name="TestPlayer",
    )

    assert "not available" in result["result"]


@pytest.mark.asyncio
async def test_handle_aliases_command_no_aliases(mock_alias_storage):
    """Test handle_aliases_command when player has no aliases."""
    mock_alias_storage.get_player_aliases.return_value = []

    result = await handle_aliases_command(
        command_data={},
        current_user={},
        request=MagicMock(),
        alias_storage=mock_alias_storage,
        player_name="TestPlayer",
    )

    assert "no aliases defined" in result["result"]


@pytest.mark.asyncio
async def test_handle_aliases_command_with_aliases(mock_alias_storage, mock_alias):
    """Test handle_aliases_command listing aliases."""
    mock_alias2 = MagicMock()
    mock_alias2.name = "s"
    mock_alias2.command = "go south"
    mock_alias_storage.get_player_aliases.return_value = [mock_alias, mock_alias2]

    result = await handle_aliases_command(
        command_data={},
        current_user={},
        request=MagicMock(),
        alias_storage=mock_alias_storage,
        player_name="TestPlayer",
    )

    assert "Your aliases:" in result["result"]
    assert "n: go north" in result["result"]
    assert "s: go south" in result["result"]


@pytest.mark.asyncio
async def test_handle_aliases_command_error(mock_alias_storage):
    """Test handle_aliases_command when listing fails."""
    mock_alias_storage.get_player_aliases.side_effect = Exception("Storage error")

    result = await handle_aliases_command(
        command_data={},
        current_user={},
        request=MagicMock(),
        alias_storage=mock_alias_storage,
        player_name="TestPlayer",
    )

    assert "Failed to list aliases" in result["result"]


@pytest.mark.asyncio
async def test_handle_unalias_command_no_storage():
    """Test handle_unalias_command when alias storage is not available."""
    result = await handle_unalias_command(
        command_data={},
        current_user={},
        request=MagicMock(),
        alias_storage=None,
        player_name="TestPlayer",
    )

    assert "not available" in result["result"]


@pytest.mark.asyncio
async def test_handle_unalias_command_no_args(mock_alias_storage):
    """Test handle_unalias_command with no arguments."""
    result = await handle_unalias_command(
        command_data={"args": []},
        current_user={},
        request=MagicMock(),
        alias_storage=mock_alias_storage,
        player_name="TestPlayer",
    )

    assert "Usage:" in result["result"]


@pytest.mark.asyncio
async def test_handle_unalias_command_alias_not_found(mock_alias_storage):
    """Test handle_unalias_command when alias doesn't exist."""
    mock_alias_storage.get_alias.return_value = None

    result = await handle_unalias_command(
        command_data={"args": ["nonexistent"]},
        current_user={},
        request=MagicMock(),
        alias_storage=mock_alias_storage,
        player_name="TestPlayer",
    )

    assert "No alias found" in result["result"]


@pytest.mark.asyncio
async def test_handle_unalias_command_success(mock_alias_storage, mock_alias):
    """Test handle_unalias_command successful removal."""
    mock_alias_storage.get_alias.return_value = mock_alias

    result = await handle_unalias_command(
        command_data={"args": ["n"]},
        current_user={},
        request=MagicMock(),
        alias_storage=mock_alias_storage,
        player_name="TestPlayer",
    )

    assert "removed successfully" in result["result"]
    mock_alias_storage.remove_alias.assert_called_once_with("TestPlayer", "n")


@pytest.mark.asyncio
async def test_handle_unalias_command_error(mock_alias_storage, mock_alias):
    """Test handle_unalias_command when removal fails."""
    mock_alias_storage.get_alias.return_value = mock_alias
    mock_alias_storage.remove_alias.side_effect = Exception("Storage error")

    result = await handle_unalias_command(
        command_data={"args": ["n"]},
        current_user={},
        request=MagicMock(),
        alias_storage=mock_alias_storage,
        player_name="TestPlayer",
    )

    assert "Failed to remove alias" in result["result"]


@pytest.mark.asyncio
async def test_handle_alias_command_invalid_name_empty(mock_alias_storage):
    """Test handle_alias_command with empty alias name."""
    result = await handle_alias_command(
        command_data={"alias_name": "", "command": "go north"},
        current_user={},
        request=MagicMock(),
        alias_storage=mock_alias_storage,
        player_name="TestPlayer",
    )
    assert "1-20 characters" in result["result"]


@pytest.mark.asyncio
async def test_handle_alias_command_invalid_command_empty(mock_alias_storage):
    """Test handle_alias_command with empty command."""
    result = await handle_alias_command(
        command_data={"alias_name": "n", "command": ""},
        current_user={},
        request=MagicMock(),
        alias_storage=mock_alias_storage,
        player_name="TestPlayer",
    )
    assert "1-200 characters" in result["result"]


@pytest.mark.asyncio
async def test_handle_alias_command_view_from_structured_data(mock_alias_storage, mock_alias):
    """Test handle_alias_command viewing alias from structured data."""
    mock_alias_storage.get_alias.return_value = mock_alias
    result = await handle_alias_command(
        command_data={"alias_name": "n", "command": None},
        current_user={},
        request=MagicMock(),
        alias_storage=mock_alias_storage,
        player_name="TestPlayer",
    )
    assert "Alias 'n' = 'go north'" in result["result"]


@pytest.mark.asyncio
async def test_handle_alias_command_update_existing(mock_alias_storage):
    """Test handle_alias_command updating existing alias."""
    mock_alias_storage.create_alias.return_value = True
    result = await handle_alias_command(
        command_data={"alias_name": "n", "command": "go south"},
        current_user={},
        request=MagicMock(),
        alias_storage=mock_alias_storage,
        player_name="TestPlayer",
    )
    assert "created successfully" in result["result"] or "updated" in result["result"].lower()
