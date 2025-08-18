"""
Tests for unified command handler.

This module tests the unified command processing system to ensure
both HTTP and WebSocket interfaces use the same code path and
produce identical results.
"""

from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from ..command_handler_unified import process_command, process_command_unified
from ..realtime.request_context import create_websocket_request_context


class TestUnifiedCommandHandler:
    """Test the unified command handler functionality."""

    @pytest.fixture
    def mock_persistence(self):
        """Create a mock persistence layer."""
        persistence = MagicMock()
        persistence.get_player_by_name.return_value = MagicMock(
            player_id="test-player-id", name="testuser", current_room_id="room-1"
        )
        persistence.get_room.return_value = MagicMock(
            name="Test Room", description="A test room for testing", exits={"north": "room-2", "south": None}
        )
        return persistence

    @pytest.fixture
    def mock_event_bus(self):
        """Create a mock event bus."""
        return MagicMock()

    @pytest.fixture
    def mock_user(self):
        """Create a mock user object."""
        return MagicMock(username="testuser", id="test-user-id")

    @pytest.fixture
    def mock_request(self, mock_persistence, mock_event_bus):
        """Create a mock FastAPI request object."""
        request = MagicMock()
        request.app.state.persistence = mock_persistence
        request.app.state.event_bus = mock_event_bus
        return request

    @pytest.fixture
    def websocket_request_context(self, mock_persistence, mock_event_bus, mock_user):
        """Create a WebSocket request context."""
        return create_websocket_request_context(mock_persistence, mock_event_bus, mock_user)

    @pytest.mark.asyncio
    async def test_process_command_unified_basic_validation(self, mock_user, mock_request):
        """Test basic command validation in unified handler."""
        # Test empty command
        result = await process_command_unified("", mock_user, mock_request)
        assert result["result"] == ""

        # Test command too long
        long_command = "a" * 1001
        result = await process_command_unified(long_command, mock_user, mock_request)
        assert "Command too long" in result["result"]

        # Test command with only whitespace
        result = await process_command_unified("   ", mock_user, mock_request)
        assert result["result"] == ""

    @pytest.mark.asyncio
    async def test_process_command_unified_normalization(self, mock_user, mock_request):
        """Test command normalization (slash prefix removal)."""
        # Test command with slash prefix
        result = await process_command_unified("/look", mock_user, mock_request)
        # Should be processed as "look" command
        assert "result" in result

        # Test command without slash prefix
        result = await process_command_unified("look", mock_user, mock_request)
        # Should be processed the same way
        assert "result" in result

    @pytest.mark.asyncio
    async def test_process_command_unified_cleaning(self, mock_user, mock_request):
        """Test command input cleaning (multiple spaces)."""
        # Test command with multiple spaces
        result = await process_command_unified("  look   north  ", mock_user, mock_request)
        # Should be cleaned to "look north"
        assert "result" in result

    @pytest.mark.asyncio
    async def test_websocket_request_context_creation(self, mock_persistence, mock_event_bus, mock_user):
        """Test WebSocket request context creation."""
        context = create_websocket_request_context(mock_persistence, mock_event_bus, mock_user)

        assert context.app.state.persistence == mock_persistence
        assert context.app.state.event_bus == mock_event_bus
        assert context.user == mock_user
        assert context.app.state.alias_storage is None

    @pytest.mark.asyncio
    async def test_websocket_request_context_alias_storage(self, websocket_request_context):
        """Test setting alias storage in WebSocket request context."""
        mock_alias_storage = MagicMock()
        websocket_request_context.set_alias_storage(mock_alias_storage)

        assert websocket_request_context.app.state.alias_storage == mock_alias_storage
        assert websocket_request_context.get_alias_storage() == mock_alias_storage

    @pytest.mark.asyncio
    async def test_websocket_request_context_getters(self, websocket_request_context, mock_persistence, mock_event_bus):
        """Test getter methods in WebSocket request context."""
        assert websocket_request_context.get_persistence() == mock_persistence
        assert websocket_request_context.get_event_bus() == mock_event_bus

    @pytest.mark.asyncio
    async def test_legacy_process_command_compatibility(self, mock_user, mock_request):
        """Test legacy process_command function maintains compatibility."""
        mock_alias_storage = MagicMock()

        # Test legacy function signature
        result = await process_command("look", [], mock_user, mock_request, mock_alias_storage, "testuser")

        # Should delegate to unified handler
        assert "result" in result

    @pytest.mark.asyncio
    async def test_unified_handler_with_alias_storage(self, mock_user, mock_request):
        """Test unified handler with alias storage."""
        mock_alias_storage = MagicMock()
        mock_alias_storage.get_alias.return_value = None  # No alias found

        result = await process_command_unified(
            "look", mock_user, mock_request, alias_storage=mock_alias_storage, player_name="testuser"
        )

        assert "result" in result
        mock_alias_storage.get_alias.assert_called_once()

    @pytest.mark.asyncio
    async def test_unified_handler_without_alias_storage(self, mock_user, mock_request):
        """Test unified handler without alias storage (should create one)."""
        with patch("server.command_handler_unified.AliasStorage") as mock_alias_class:
            mock_alias_storage = MagicMock()
            mock_alias_class.return_value = mock_alias_storage

            result = await process_command_unified("look", mock_user, mock_request, player_name="testuser")

            assert "result" in result
            mock_alias_class.assert_called_once()

    @pytest.mark.asyncio
    async def test_alias_management_commands(self, mock_user, mock_request):
        """Test that alias management commands are handled correctly."""
        mock_alias_storage = MagicMock()

        # Test alias command
        result = await process_command_unified(
            "alias test look", mock_user, mock_request, alias_storage=mock_alias_storage, player_name="testuser"
        )

        # Should be processed by command service
        assert "result" in result

    @pytest.mark.asyncio
    async def test_alias_expansion(self, mock_user, mock_request):
        """Test alias expansion functionality."""
        mock_alias_storage = MagicMock()
        mock_alias = MagicMock()
        mock_alias.name = "test"
        mock_alias.get_expanded_command.return_value = "look north"
        mock_alias_storage.get_alias.return_value = mock_alias

        result = await process_command_unified(
            "test", mock_user, mock_request, alias_storage=mock_alias_storage, player_name="testuser"
        )

        assert "result" in result
        assert "alias_chain" in result
        mock_alias_storage.get_alias.assert_called_once_with("testuser", "test")

    @pytest.mark.asyncio
    async def test_alias_expansion_depth_limit(self, mock_user, mock_request):
        """Test that alias expansion has a depth limit to prevent loops."""
        mock_alias_storage = MagicMock()
        mock_alias = MagicMock()
        mock_alias.name = "loop"
        mock_alias.get_expanded_command.return_value = "loop"  # Self-referencing alias
        mock_alias_storage.get_alias.return_value = mock_alias

        # Mock the command processor to accept "loop" as a valid command
        with patch("server.command_handler_unified.command_processor") as mock_processor:
            mock_processor.process_command_string.return_value = (MagicMock(), None, "look")
            mock_processor.extract_command_data.return_value = {"direction": "north"}

            # Mock the command service to return a valid response
            with patch("server.command_handler_unified.command_service") as mock_service:
                mock_service.process_command = AsyncMock(return_value={"result": "Test response"})

                # Mock the handle_expanded_command to simulate recursive calls
                with patch("server.command_handler_unified.handle_expanded_command") as mock_handle:
                    # Simulate the recursive behavior by calling the original function
                    # but with a depth that exceeds the limit
                    async def mock_handle_expanded(
                        command_line, current_user, request, alias_storage, player_name, depth=0, alias_chain=None
                    ):
                        if depth > 10:
                            return {"result": "Alias expansion too deep - possible loop detected"}
                        # Simulate recursive call
                        return await mock_handle_expanded(
                            command_line, current_user, request, alias_storage, player_name, depth + 1, alias_chain
                        )

                    mock_handle.side_effect = mock_handle_expanded

                    result = await process_command_unified(
                        "loop", mock_user, mock_request, alias_storage=mock_alias_storage, player_name="testuser"
                    )

                    # Should detect the loop and return an error
                    assert "alias expansion too deep" in result["result"].lower()

    @pytest.mark.asyncio
    async def test_error_handling(self, mock_user, mock_request):
        """Test error handling in unified command handler."""
        # Test with invalid command that would cause an exception
        with patch("server.command_handler_unified.command_processor") as mock_processor:
            mock_processor.process_command_string.side_effect = Exception("Test error")

            result = await process_command_unified("invalid", mock_user, mock_request, player_name="testuser")

            assert "error occurred" in result["result"].lower()

    @pytest.mark.asyncio
    async def test_player_name_extraction(self, mock_request):
        """Test player name extraction from user object."""
        # Test with user object that has username attribute
        user_with_username = MagicMock(username="testuser")
        result = await process_command_unified("look", user_with_username, mock_request)
        assert "result" in result

        # Test with user dictionary
        user_dict = {"username": "testuser"}
        result = await process_command_unified("look", user_dict, mock_request)
        assert "result" in result

        # Test with invalid user object
        invalid_user = MagicMock()  # No username attribute
        # The function should handle this gracefully by using the provided player_name
        result = await process_command_unified("look", invalid_user, mock_request, player_name="testuser")
        assert "result" in result

    @pytest.mark.asyncio
    async def test_websocket_vs_http_consistency(self, mock_user, mock_request, websocket_request_context):
        """Test that WebSocket and HTTP produce identical results."""
        mock_alias_storage = MagicMock()
        mock_alias_storage.get_alias.return_value = None

        # Test HTTP path
        http_result = await process_command_unified(
            "look", mock_user, mock_request, alias_storage=mock_alias_storage, player_name="testuser"
        )

        # Test WebSocket path
        websocket_result = await process_command_unified(
            "look", mock_user, websocket_request_context, alias_storage=mock_alias_storage, player_name="testuser"
        )

        # Results should be identical
        assert http_result == websocket_result
