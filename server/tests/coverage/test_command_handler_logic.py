"""
Core logic and error path tests for command_handler_unified.py.
"""

import uuid
from unittest.mock import AsyncMock, Mock, patch

import pytest

from server.command_handler_unified import (
    _is_predefined_emote,
    clean_command_input,
    get_help_content,
    get_username_from_user,
    normalize_command,
    process_command,
)
from server.exceptions import ValidationError
from server.middleware.command_rate_limiter import command_rate_limiter


class TestUtilityFunctions:
    """Test utility functions."""

    def test_get_username_from_user_dict(self) -> None:
        """Test extracting username from dictionary."""
        user_dict = {"username": "testuser"}
        assert get_username_from_user(user_dict) == "testuser"

    def test_get_username_from_user_object(self) -> None:
        """Test extracting username from object."""

        class UserObject:
            def __init__(self, username):
                self.username = username

        user_obj = UserObject("testuser")
        assert get_username_from_user(user_obj) == "testuser"

    def test_get_username_from_user_name_key(self) -> None:
        """Test extracting username using name key."""
        user_dict = {"name": "testuser"}
        assert get_username_from_user(user_dict) == "testuser"

    def test_get_username_from_user_name_attr(self) -> None:
        """Test extracting username using name attribute."""
        user_obj = Mock()
        user_obj.name = "testuser"
        del user_obj.username
        assert get_username_from_user(user_obj) == "testuser"

    def test_get_username_from_user_invalid(self) -> None:
        """Test extracting username from invalid object."""
        user_obj = Mock()
        del user_obj.username
        del user_obj.name
        with pytest.raises(ValidationError, match="User object must have username or name attribute or key"):
            get_username_from_user(user_obj)

    def test_normalize_command_edge_cases(self) -> None:
        """Test command normalization with edge cases."""
        # Fix mypy error: normalize_command expects str, but we test None
        assert normalize_command(None) is None  # type: ignore[arg-type]
        assert normalize_command("") == ""
        assert normalize_command("   ") == ""
        assert normalize_command("/   ") == ""

    def test_command_validation_edge_cases(self) -> None:
        """Test command validation with edge cases."""
        assert normalize_command("") == ""
        assert normalize_command("   ") == ""
        assert normalize_command("/   ") == ""

    def test_clean_command_input_edge_cases(self) -> None:
        """Test command input cleaning with edge cases."""
        assert clean_command_input("") == ""
        assert clean_command_input("   ") == ""
        assert clean_command_input("\t\n\r  test  \t\n\r") == "test"

    @patch("server.game.emote_service.EmoteService")
    def test_is_predefined_emote_success(self, mock_emote_service_class):
        """Test predefined emote detection success."""
        mock_emote_service = Mock()
        mock_emote_service.is_emote_alias.return_value = True
        mock_emote_service_class.return_value = mock_emote_service
        result = _is_predefined_emote("twibble")
        assert result is True

    @patch("server.game.emote_service.EmoteService")
    def test_is_predefined_emote_failure(self, mock_emote_service_class):
        """Test predefined emote detection failure."""
        mock_emote_service = Mock()
        mock_emote_service.is_emote_alias.return_value = False
        mock_emote_service_class.return_value = mock_emote_service
        result = _is_predefined_emote("unknown")
        assert result is False

    @patch("server.game.emote_service.EmoteService")
    def test_is_predefined_emote_exception(self, mock_emote_service_class):
        """Test predefined emote detection with exception."""
        mock_emote_service_class.side_effect = Exception("Service error")
        result = _is_predefined_emote("twibble")
        assert result is False

    def test_get_help_content_unknown_command(self) -> None:
        """Test getting help for unknown command."""
        result = get_help_content("nonexistent_command")
        assert "Command Not Found" in result
        assert "nonexistent_command" in result

    def test_get_help_content_no_command(self) -> None:
        """Test getting general help content."""
        result = get_help_content()
        assert "MythosMUD Help System" in result
        assert "Exploration Commands" in result
        assert "Movement Commands" in result
        assert "Communication Commands" in result
        assert "System Commands" in result


class TestCommandHandlerRateLimiting:
    """Test rate limiting paths in command handler."""

    @pytest.mark.asyncio
    async def test_process_command_rate_limit_exceeded(self) -> None:
        """Test command processing when rate limit is exceeded."""
        mock_request = Mock()
        mock_request.app.state.persistence = Mock()
        mock_alias_storage = Mock()
        mock_alias_storage.get_alias.return_value = None
        current_user = {"username": "ratelimituser"}
        try:
            for _ in range(12):
                command_rate_limiter.is_allowed("ratelimituser")
            result = await process_command(
                "say", ["test"], current_user, mock_request, mock_alias_storage, "ratelimituser"
            )
            assert "result" in result
            assert "too many commands" in result["result"].lower()
            assert "wait" in result["result"].lower()
        finally:
            command_rate_limiter.reset_player("ratelimituser")


class TestCommandHandlerValidation:
    """Test command validation paths."""

    @pytest.fixture(autouse=True)
    def reset_rate_limiter(self):
        """Reset rate limiter before each test."""
        command_rate_limiter.reset_player("testuser")
        yield
        command_rate_limiter.reset_player("testuser")

    @pytest.mark.asyncio
    async def test_process_command_validation_failure(self) -> None:
        """Test command processing when content validation fails."""
        mock_request = Mock()
        mock_request.app.state.persistence = Mock()
        mock_player = Mock()
        mock_player.player_id = uuid.uuid4()
        mock_request.app.state.persistence.get_player_by_name = AsyncMock(return_value=mock_player)
        mock_alias_storage = Mock()
        mock_alias_storage.get_alias.return_value = None
        current_user = {"username": "testuser"}
        malicious_command = "say'; DROP TABLE players; --"
        result = await process_command(
            "say", [malicious_command], current_user, mock_request, mock_alias_storage, "testuser"
        )
        assert "result" in result

    @pytest.mark.asyncio
    async def test_process_command_empty_after_normalization(self) -> None:
        """Test command that becomes empty after normalization."""
        mock_request = Mock()
        mock_request.app.state.persistence = Mock()
        mock_alias_storage = Mock()
        mock_alias_storage.get_alias.return_value = None
        current_user = {"username": "testuser"}
        with patch("server.command_handler_unified.normalize_command", return_value=""):
            result = await process_command("look", [], current_user, mock_request, mock_alias_storage, "testuser")
            assert "result" in result
            assert result["result"] == ""


class TestCommandHandlerAliasExpansion:
    """Test alias expansion edge cases."""

    @pytest.fixture(autouse=True)
    def reset_rate_limiter(self):
        """Reset rate limiter before each test."""
        command_rate_limiter.reset_player("testuser")
        yield
        command_rate_limiter.reset_player("testuser")

    @pytest.mark.asyncio
    async def test_circular_alias_detection(self) -> None:
        """Test detection of circular alias dependencies."""
        from server.models.alias import Alias

        mock_request = Mock()
        mock_request.app.state.persistence = Mock()
        mock_player = Mock()
        mock_player.player_id = uuid.uuid4()
        mock_request.app.state.persistence.get_player_by_name = AsyncMock(return_value=mock_player)
        alias_a = Alias(name="a", command="b")
        alias_b = Alias(name="b", command="a")
        mock_alias_storage = Mock()
        mock_alias_storage.get_player_aliases.return_value = [alias_a, alias_b]
        mock_alias_storage.get_alias.return_value = alias_a
        current_user = {"username": "testuser"}
        result = await process_command("a", [], current_user, mock_request, mock_alias_storage, "testuser")
        assert "result" in result
        assert "circular dependency" in result["result"].lower()

    @pytest.mark.asyncio
    async def test_alias_expansion_depth_exceeded(self) -> None:
        """Test alias with excessive expansion depth."""
        from server.models.alias import Alias

        mock_request = Mock()
        mock_request.app.state.persistence = Mock()
        mock_player = Mock()
        mock_player.player_id = uuid.uuid4()
        mock_request.app.state.persistence.get_player_by_name = AsyncMock(return_value=mock_player)
        deep_alias = Alias(name="deep", command="look north")
        mock_alias_storage = Mock()
        mock_alias_storage.get_player_aliases.return_value = [deep_alias]
        mock_alias_storage.get_alias.return_value = deep_alias
        current_user = {"username": "testuser"}
        with patch("server.utils.alias_graph.AliasGraph.get_expansion_depth", return_value=15):
            result = await process_command("deep", [], current_user, mock_request, mock_alias_storage, "testuser")
            assert "result" in result
            assert "excessive expansion depth" in result["result"].lower()

    @pytest.mark.asyncio
    async def test_expanded_command_too_long(self) -> None:
        """Test alias that expands to command exceeding length limit."""
        from server.models.alias import Alias

        mock_request = Mock()
        mock_request.app.state.persistence = Mock()
        mock_player = Mock()
        mock_player.player_id = uuid.uuid4()
        mock_request.app.state.persistence.get_player_by_name = AsyncMock(return_value=mock_player)
        long_command = "say " + ("a" * 10000)
        long_alias = Alias(name="spam", command=long_command)
        mock_alias_storage = Mock()
        mock_alias_storage.get_player_aliases.return_value = [long_alias]
        mock_alias_storage.get_alias.return_value = long_alias
        current_user = {"username": "testuser"}
        result = await process_command("spam", [], current_user, mock_request, mock_alias_storage, "testuser")
        assert "result" in result
        assert "too long" in result["result"].lower()

    @pytest.mark.asyncio
    async def test_expanded_command_validation_failure(self) -> None:
        """Test alias expansion where expanded command fails validation."""
        from server.models.alias import Alias

        mock_request = Mock()
        mock_request.app.state.persistence = Mock()
        mock_player = Mock()
        mock_player.player_id = uuid.uuid4()
        mock_request.app.state.persistence.get_player_by_name = AsyncMock(return_value=mock_player)
        malicious_alias = Alias(name="bad", command="say '; DROP TABLE players; --")
        mock_alias_storage = Mock()
        mock_alias_storage.get_player_aliases.return_value = [malicious_alias]
        mock_alias_storage.get_alias.return_value = malicious_alias
        current_user = {"username": "testuser"}
        result = await process_command("bad", [], current_user, mock_request, mock_alias_storage, "testuser")
        assert "result" in result


class TestCommandHandlerErrorPaths:
    """Test error handling in command handler."""

    @pytest.fixture(autouse=True)
    def reset_rate_limiter(self):
        """Reset rate limiter before each test."""
        command_rate_limiter.reset_player("testuser")
        yield
        command_rate_limiter.reset_player("testuser")

    @pytest.mark.asyncio
    async def test_command_execution_exception(self) -> None:
        """Test exception during command execution."""
        mock_request = Mock()
        mock_request.app.state.persistence = Mock()
        mock_player = Mock()
        mock_player.player_id = uuid.uuid4()
        mock_request.app.state.persistence.get_player_by_name = AsyncMock(return_value=mock_player)
        mock_alias_storage = Mock()
        mock_alias_storage.get_alias.return_value = None
        current_user = {"username": "testuser"}
        with patch("server.command_handler_unified.handle_command", side_effect=RuntimeError("Command error")):
            result = await process_command("look", [], current_user, mock_request, mock_alias_storage, "testuser")
            assert "result" in result
            assert "error" in result["result"].lower()
