"""Integration tests for alias system with command handler.

As noted in the restricted archives of Miskatonic University, these tests
validate the integration between the alias system and command processing.
"""

from unittest.mock import Mock, patch

import pytest

from ..command_handler import handle_command
from ..models import Alias


class TestAliasIntegration:
    """Test integration between alias system and command handler."""

    def test_alias_expansion_basic(self):
        """Test basic alias expansion."""
        mock_command_request = Mock()
        mock_command_request.command = "l"

        mock_user = {"username": "testuser"}

        mock_request = Mock()
        # Mock the persistence layer
        mock_app = Mock()
        mock_persistence = Mock()
        mock_app.state.persistence = mock_persistence
        mock_request.app = mock_app

        # Mock player and room data
        mock_player = Mock()
        mock_player.current_room_id = "arkham_001"
        mock_persistence.get_player_by_name.return_value = mock_player

        mock_room = {
            "name": "Test Room",
            "description": "A test room for testing.",
            "exits": {"north": "arkham_002", "south": "arkham_003"},
        }
        mock_persistence.get_room.return_value = mock_room

        with patch("server.command_handler.AliasStorage") as mock_storage_class:
            mock_storage = Mock()
            # First call: check if "l" is an alias
            mock_storage.get_alias.side_effect = [
                Alias(name="l", command="look"),  # "l" is an alias
                None,  # "look" is not an alias
            ]
            mock_storage.get_alias_count.return_value = 0
            mock_storage_class.return_value = mock_storage

            handle_command(mock_command_request, mock_user, mock_request)

            # Should call get_alias twice: first with "l", then with "look"
            assert mock_storage.get_alias.call_count == 2
            mock_storage.get_alias.assert_any_call("testuser", "l")
            mock_storage.get_alias.assert_any_call("testuser", "look")

    def test_alias_creation_command(self):
        """Test alias creation via command."""
        mock_command_request = Mock()
        mock_command_request.command = "alias l look"

        mock_user = {"username": "testuser"}

        mock_request = Mock()

        with patch("server.command_handler.AliasStorage") as mock_storage_class:
            mock_storage = Mock()
            mock_storage.create_alias.return_value = Alias(name="l", command="look")
            mock_storage.get_alias_count.return_value = 0
            mock_storage_class.return_value = mock_storage

            handle_command(mock_command_request, mock_user, mock_request)

            # Should call create_alias
            mock_storage.create_alias.assert_called_with("testuser", "l", "look")

    def test_alias_listing_command(self):
        """Test alias listing via command."""
        mock_command_request = Mock()
        mock_command_request.command = "aliases"

        mock_user = {"username": "testuser"}

        mock_request = Mock()

        with patch("server.command_handler.AliasStorage") as mock_storage_class:
            mock_storage = Mock()
            mock_storage.get_player_aliases.return_value = [
                Alias(name="l", command="look"),
                Alias(name="n", command="go north"),
            ]
            mock_storage_class.return_value = mock_storage

            handle_command(mock_command_request, mock_user, mock_request)

            # Should call get_player_aliases
            mock_storage.get_player_aliases.assert_called_with("testuser")

    def test_alias_removal_command(self):
        """Test alias removal via command."""
        mock_command_request = Mock()
        mock_command_request.command = "unalias l"

        mock_user = {"username": "testuser"}

        mock_request = Mock()

        with patch("server.command_handler.AliasStorage") as mock_storage_class:
            mock_storage = Mock()
            mock_storage.remove_alias.return_value = True
            mock_storage_class.return_value = mock_storage

            handle_command(mock_command_request, mock_user, mock_request)

            # Should call remove_alias
            mock_storage.remove_alias.assert_called_with("testuser", "l")

    def test_alias_command_without_args(self):
        """Test alias command without arguments."""
        mock_command_request = Mock()
        mock_command_request.command = "alias"

        mock_user = {"username": "testuser"}

        mock_request = Mock()

        with patch("server.command_handler.AliasStorage") as mock_storage_class:
            mock_storage = Mock()
            mock_storage_class.return_value = mock_storage

            handle_command(mock_command_request, mock_user, mock_request)

            # Should not call any alias methods
            mock_storage.get_alias.assert_not_called()
            mock_storage.create_alias.assert_not_called()

    def test_unalias_command_without_args(self):
        """Test unalias command without arguments."""
        mock_command_request = Mock()
        mock_command_request.command = "unalias"

        mock_user = {"username": "testuser"}

        mock_request = Mock()

        with patch("server.command_handler.AliasStorage") as mock_storage_class:
            mock_storage = Mock()
            mock_storage_class.return_value = mock_storage

            handle_command(mock_command_request, mock_user, mock_request)

            # Should not call any alias methods
            mock_storage.remove_alias.assert_not_called()

    def test_alias_validation_integration(self):
        """Test alias validation integration."""
        mock_command_request = Mock()
        mock_command_request.command = "alias 1look look"

        mock_user = {"username": "testuser"}

        mock_request = Mock()

        with patch("server.command_handler.AliasStorage") as mock_storage_class:
            mock_storage = Mock()
            mock_storage.create_alias.return_value = None  # Invalid name
            mock_storage.get_alias_count.return_value = 0
            mock_storage_class.return_value = mock_storage

            handle_command(mock_command_request, mock_user, mock_request)

            # Should call create_alias but return None for invalid name
            mock_storage.create_alias.assert_called_with("testuser", "1look", "look")

    def test_alias_limit_enforcement(self):
        """Test alias limit enforcement."""
        mock_command_request = Mock()
        mock_command_request.command = "alias extra command"

        mock_user = {"username": "testuser"}

        mock_request = Mock()

        with patch("server.command_handler.AliasStorage") as mock_storage_class:
            mock_storage = Mock()
            mock_storage.create_alias.return_value = None  # Limit reached
            mock_storage.get_alias_count.return_value = 50  # At limit
            mock_storage_class.return_value = mock_storage

            handle_command(mock_command_request, mock_user, mock_request)

            # Should call create_alias but return None for limit
            mock_storage.create_alias.assert_called_with("testuser", "extra", "command")

    def test_alias_loop_detection(self):
        """Test alias loop detection."""
        mock_command_request = Mock()
        mock_command_request.command = "l"

        mock_user = {"username": "testuser"}

        mock_request = Mock()

        with patch("server.command_handler.AliasStorage") as mock_storage_class:
            mock_storage = Mock()
            # Create a loop: l -> l (provide enough values for the loop)
            mock_storage.get_alias.side_effect = [
                Alias(name="l", command="l"),  # "l" is an alias for "l"
                Alias(name="l", command="l"),  # "l" is an alias for "l" (loop)
                Alias(name="l", command="l"),  # "l" is an alias for "l" (loop)
                Alias(name="l", command="l"),  # "l" is an alias for "l" (loop)
                Alias(name="l", command="l"),  # "l" is an alias for "l" (loop)
                Alias(name="l", command="l"),  # "l" is an alias for "l" (loop)
                Alias(name="l", command="l"),  # "l" is an alias for "l" (loop)
                Alias(name="l", command="l"),  # "l" is an alias for "l" (loop)
                Alias(name="l", command="l"),  # "l" is an alias for "l" (loop)
                Alias(name="l", command="l"),  # "l" is an alias for "l" (loop)
                Alias(name="l", command="l"),  # "l" is an alias for "l" (loop)
                Alias(name="l", command="l"),  # "l" is an alias for "l" (loop)
                Alias(name="l", command="l"),  # "l" is an alias for "l" (loop)
                Alias(name="l", command="l"),  # "l" is an alias for "l" (loop)
                Alias(name="l", command="l"),  # "l" is an alias for "l" (loop)
                Alias(name="l", command="l"),  # "l" is an alias for "l" (loop)
            ]
            mock_storage.get_alias_count.return_value = 0
            mock_storage_class.return_value = mock_storage

            result = handle_command(mock_command_request, mock_user, mock_request)

            # Should detect the loop and return error message
            assert "Error: Alias loop detected" in result["result"]
            # Should call get_alias multiple times due to loop
            assert mock_storage.get_alias.call_count >= 10

    def test_alias_case_insensitivity(self):
        """Test alias case insensitivity."""
        mock_command_request = Mock()
        mock_command_request.command = "L"

        mock_user = {"username": "testuser"}

        mock_request = Mock()
        # Mock the persistence layer
        mock_app = Mock()
        mock_persistence = Mock()
        mock_app.state.persistence = mock_persistence
        mock_request.app = mock_app

        # Mock player and room data
        mock_player = Mock()
        mock_player.current_room_id = "arkham_001"
        mock_persistence.get_player_by_name.return_value = mock_player

        mock_room = {
            "name": "Test Room",
            "description": "A test room for testing.",
            "exits": {"north": "arkham_002", "south": "arkham_003"},
        }
        mock_persistence.get_room.return_value = mock_room

        with patch("server.command_handler.AliasStorage") as mock_storage_class:
            mock_storage = Mock()
            mock_storage.get_alias.side_effect = [
                Alias(name="l", command="look"),  # "L" is an alias
                None,  # "look" is not an alias
            ]
            mock_storage.get_alias_count.return_value = 0
            mock_storage_class.return_value = mock_storage

            handle_command(mock_command_request, mock_user, mock_request)

            # Should call get_alias with lowercase version (command handler converts to lowercase)
            mock_storage.get_alias.assert_any_call("testuser", "l")

    def test_alias_with_quotes(self):
        """Test alias with quoted command."""
        mock_command_request = Mock()
        mock_command_request.command = "alias say_hello 'say Hello there!'"

        mock_user = {"username": "testuser"}

        mock_request = Mock()

        with patch("server.command_handler.AliasStorage") as mock_storage_class:
            mock_storage = Mock()
            mock_storage.create_alias.return_value = Alias(name="say_hello", command="say Hello there!")
            mock_storage.get_alias_count.return_value = 0
            mock_storage_class.return_value = mock_storage

            handle_command(mock_command_request, mock_user, mock_request)

            # Should call create_alias with quoted command (quotes are preserved)
            mock_storage.create_alias.assert_called_with("testuser", "say_hello", "'say Hello there!'")

    def test_alias_reserved_command_validation(self):
        """Test that reserved commands cannot be aliased."""
        mock_command_request = Mock()
        mock_command_request.command = "alias help_command help"

        mock_user = {"username": "testuser"}

        mock_request = Mock()

        with patch("server.command_handler.AliasStorage") as mock_storage_class:
            mock_storage = Mock()
            mock_storage.create_alias.return_value = None  # Reserved command
            mock_storage.get_alias_count.return_value = 0
            mock_storage_class.return_value = mock_storage

            handle_command(mock_command_request, mock_user, mock_request)

            # Should call create_alias but return None for reserved command
            mock_storage.create_alias.assert_called_with("testuser", "help_command", "help")

    def test_alias_update_existing(self):
        """Test updating an existing alias."""
        mock_command_request = Mock()
        mock_command_request.command = "alias l look around"

        mock_user = {"username": "testuser"}

        mock_request = Mock()

        with patch("server.command_handler.AliasStorage") as mock_storage_class:
            mock_storage = Mock()
            mock_storage.create_alias.return_value = Alias(name="l", command="look around")
            mock_storage.get_alias_count.return_value = 0
            mock_storage_class.return_value = mock_storage

            handle_command(mock_command_request, mock_user, mock_request)

            # Should call create_alias to update existing alias
            mock_storage.create_alias.assert_called_with("testuser", "l", "look around")

    def test_alias_error_handling(self):
        """Test error handling in alias system."""
        mock_command_request = Mock()
        mock_command_request.command = "l"

        mock_user = {"username": "testuser"}

        mock_request = Mock()

        with patch("server.command_handler.AliasStorage") as mock_storage_class:
            mock_storage = Mock()
            mock_storage.get_alias.side_effect = Exception("Storage error")
            mock_storage.get_alias_count.return_value = 0
            mock_storage_class.return_value = mock_storage

            # Should raise the exception since there's no error handling
            with pytest.raises(Exception, match="Storage error"):
                handle_command(mock_command_request, mock_user, mock_request)

            # Should still call get_alias
            mock_storage.get_alias.assert_called_with("testuser", "l")

    def test_alias_chain_in_response(self):
        """Test that alias chain information is included in response."""
        mock_command_request = Mock()
        mock_command_request.command = "l"

        mock_user = {"username": "testuser"}

        mock_request = Mock()
        # Mock the persistence layer
        mock_app = Mock()
        mock_persistence = Mock()
        mock_app.state.persistence = mock_persistence
        mock_request.app = mock_app

        # Mock player and room data
        mock_player = Mock()
        mock_player.current_room_id = "arkham_001"
        mock_persistence.get_player_by_name.return_value = mock_player

        mock_room = {
            "name": "Test Room",
            "description": "A test room for testing.",
            "exits": {"north": "arkham_002", "south": "arkham_003"},
        }
        mock_persistence.get_room.return_value = mock_room

        with patch("server.command_handler.AliasStorage") as mock_storage_class:
            mock_storage = Mock()
            # First call: check if "l" is an alias
            mock_storage.get_alias.side_effect = [
                Alias(name="l", command="look"),  # "l" is an alias
                None,  # "look" is not an alias
            ]
            mock_storage.get_alias_count.return_value = 0
            mock_storage_class.return_value = mock_storage

            result = handle_command(mock_command_request, mock_user, mock_request)

            # Should include alias chain information
            assert "alias_chain" in result
            assert len(result["alias_chain"]) == 1
            assert result["alias_chain"][0]["original"] == "l"
            assert result["alias_chain"][0]["expanded"] == "look"
            assert result["alias_chain"][0]["alias_name"] == "l"
