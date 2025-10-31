"""
Tests for alias management commands.

This module tests the alias command handlers including creation, viewing,
listing, and deletion of player command aliases.

As noted in the Pnakotic Manuscripts: "Shortcuts through the labyrinth must be
tested thoroughly, lest they lead to unexpected dimensions."
"""

from unittest.mock import MagicMock

import pytest

from server.alias_storage import AliasStorage
from server.commands.alias_commands import (
    handle_alias_command,
    handle_aliases_command,
    handle_unalias_command,
)
from server.models.alias import Alias


@pytest.fixture
def mock_alias_storage():
    """Create a mock alias storage instance."""
    storage = MagicMock(spec=AliasStorage)
    # Ensure all needed methods are available
    storage.create_alias = MagicMock()
    storage.get_alias = MagicMock(return_value=None)
    storage.get_player_aliases = MagicMock(return_value=[])
    storage.remove_alias = MagicMock()
    return storage


@pytest.fixture
def mock_current_user():
    """Create mock current user."""
    return {"user_id": "test_user_001", "username": "testuser"}


@pytest.fixture
def mock_request():
    """Create mock FastAPI request."""
    request = MagicMock()
    request.client = MagicMock()
    request.client.host = "127.0.0.1"
    return request


@pytest.fixture
def sample_alias():
    """Create a sample alias."""
    return Alias(name="gw", command="go west")


class TestHandleAliasCommandCreate:
    """Test alias command handler for creating aliases."""

    @pytest.mark.asyncio
    async def test_create_alias_success(self, mock_alias_storage, mock_current_user, mock_request):
        """Test successful alias creation."""
        result = await handle_alias_command(
            command_data={"args": ["gw", "go", "west"]},
            current_user=mock_current_user,
            request=mock_request,
            alias_storage=mock_alias_storage,
            player_name="TestPlayer",
        )

        assert result["result"] == "Alias 'gw' created successfully."
        mock_alias_storage.create_alias.assert_called_once_with("TestPlayer", "gw", "go west")

    @pytest.mark.asyncio
    async def test_create_alias_handles_exception(self, mock_alias_storage, mock_current_user, mock_request):
        """Test alias creation handles exceptions."""
        mock_alias_storage.create_alias.side_effect = Exception("Database error")

        result = await handle_alias_command(
            command_data={"args": ["gw", "go", "west"]},
            current_user=mock_current_user,
            request=mock_request,
            alias_storage=mock_alias_storage,
            player_name="TestPlayer",
        )

        assert "Failed to create alias" in result["result"]

    @pytest.mark.asyncio
    async def test_alias_name_length_minimum(self, mock_alias_storage, mock_current_user, mock_request):
        """Test alias name length minimum."""
        result = await handle_alias_command(
            command_data={"args": ["a", "look"]},
            current_user=mock_current_user,
            request=mock_request,
            alias_storage=mock_alias_storage,
            player_name="TestPlayer",
        )

        assert "created successfully" in result["result"]


class TestHandleAliasCommandView:
    """Test viewing existing aliases."""

    @pytest.mark.asyncio
    async def test_view_existing_alias(self, mock_alias_storage, mock_current_user, mock_request, sample_alias):
        """Test viewing an existing alias."""
        mock_alias_storage.get_alias.return_value = sample_alias

        result = await handle_alias_command(
            command_data={"args": ["gw"]},
            current_user=mock_current_user,
            request=mock_request,
            alias_storage=mock_alias_storage,
            player_name="TestPlayer",
        )

        assert result["result"] == "Alias 'gw' = 'go west'"
        mock_alias_storage.get_alias.assert_called_once_with("TestPlayer", "gw")


class TestHandleAliasesCommand:
    """Test aliases command handler for listing aliases."""

    @pytest.mark.asyncio
    async def test_list_aliases_with_data(self, mock_alias_storage, mock_current_user, mock_request):
        """Test listing aliases when some exist."""
        aliases = [
            Alias(name="gw", command="go west"),
            Alias(name="ge", command="go east"),
            Alias(name="gs", command="go south"),
        ]
        mock_alias_storage.get_player_aliases.return_value = aliases

        result = await handle_aliases_command(
            command_data={"args": []},
            current_user=mock_current_user,
            request=mock_request,
            alias_storage=mock_alias_storage,
            player_name="TestPlayer",
        )

        assert "Your aliases:" in result["result"]
        assert "gw: go west" in result["result"]


class TestHandleUnaliasCommand:
    """Test unalias command handler for removing aliases."""

    @pytest.mark.asyncio
    async def test_unalias_success(self, mock_alias_storage, mock_current_user, mock_request, sample_alias):
        """Test successful alias removal."""
        mock_alias_storage.get_alias.return_value = sample_alias

        result = await handle_unalias_command(
            command_data={"args": ["gw"]},
            current_user=mock_current_user,
            request=mock_request,
            alias_storage=mock_alias_storage,
            player_name="TestPlayer",
        )

        assert result["result"] == "Alias 'gw' removed successfully."
        mock_alias_storage.get_alias.assert_called_once_with("TestPlayer", "gw")
        mock_alias_storage.remove_alias.assert_called_once_with("TestPlayer", "gw")

    @pytest.mark.asyncio
    async def test_unalias_not_found(self, mock_alias_storage, mock_current_user, mock_request):
        """Test unalias when alias doesn't exist."""
        mock_alias_storage.get_alias.return_value = None

        result = await handle_unalias_command(
            command_data={"args": ["gw"]},
            current_user=mock_current_user,
            request=mock_request,
            alias_storage=mock_alias_storage,
            player_name="TestPlayer",
        )

        assert result["result"] == "No alias found for 'gw'"
        mock_alias_storage.get_alias.assert_called_once_with("TestPlayer", "gw")
        # remove_alias should NOT be called when alias doesn't exist
        mock_alias_storage.remove_alias.assert_not_called()


class TestIntegrationScenarios:
    """Test integration scenarios combining multiple commands."""

    @pytest.mark.asyncio
    async def test_complete_alias_lifecycle(self, mock_alias_storage, mock_current_user, mock_request):
        """Test complete alias lifecycle: create, view, list, delete."""
        sample_alias = Alias(name="gw", command="go west")

        # 1. Create alias
        result = await handle_alias_command(
            command_data={"args": ["gw", "go", "west"]},
            current_user=mock_current_user,
            request=mock_request,
            alias_storage=mock_alias_storage,
            player_name="TestPlayer",
        )
        assert "created successfully" in result["result"]

        # 2. View alias
        mock_alias_storage.get_alias.return_value = sample_alias
        result = await handle_alias_command(
            command_data={"args": ["gw"]},
            current_user=mock_current_user,
            request=mock_request,
            alias_storage=mock_alias_storage,
            player_name="TestPlayer",
        )
        assert "Alias 'gw' = 'go west'" in result["result"]

        # 3. List aliases
        mock_alias_storage.get_player_aliases.return_value = [sample_alias]
        result = await handle_aliases_command(
            command_data={"args": []},
            current_user=mock_current_user,
            request=mock_request,
            alias_storage=mock_alias_storage,
            player_name="TestPlayer",
        )
        assert "Your aliases:" in result["result"]

        # 4. Delete alias
        result = await handle_unalias_command(
            command_data={"args": ["gw"]},
            current_user=mock_current_user,
            request=mock_request,
            alias_storage=mock_alias_storage,
            player_name="TestPlayer",
        )
        assert "removed successfully" in result["result"]

    @pytest.mark.asyncio
    async def test_multiple_aliases_management(self, mock_alias_storage, mock_current_user, mock_request):
        """Test managing multiple aliases."""
        aliases_to_create = [("gw", "go west"), ("ge", "go east"), ("look", "examine room")]

        # Create multiple aliases
        for name, cmd in aliases_to_create:
            result = await handle_alias_command(
                command_data={"args": [name] + cmd.split()},
                current_user=mock_current_user,
                request=mock_request,
                alias_storage=mock_alias_storage,
                player_name="TestPlayer",
            )
            assert "created successfully" in result["result"]

        # List all aliases
        alias_objects = [Alias(name=name, command=cmd) for name, cmd in aliases_to_create]
        mock_alias_storage.get_player_aliases.return_value = alias_objects

        result = await handle_aliases_command(
            command_data={"args": []},
            current_user=mock_current_user,
            request=mock_request,
            alias_storage=mock_alias_storage,
            player_name="TestPlayer",
        )

        assert "Your aliases:" in result["result"]
        for name, _ in aliases_to_create:
            assert name in result["result"]
