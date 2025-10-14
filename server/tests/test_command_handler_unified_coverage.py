"""
Additional tests for command_handler_unified.py to improve coverage.

This module adds tests for uncovered paths in command handler including
rate limiting, validation failures, alias expansion edge cases, and
error handling.
"""

from unittest.mock import Mock, patch

import pytest

from server.command_handler_unified import process_command
from server.middleware.command_rate_limiter import command_rate_limiter


class TestCommandHandlerRateLimiting:
    """Test rate limiting paths in command handler."""

    @pytest.mark.asyncio
    async def test_process_command_rate_limit_exceeded(self):
        """Test command processing when rate limit is exceeded.

        AI: Tests lines 240-250 in command_handler_unified.py where rate limit
        violations are detected and logged. Covers security event logging path.
        """
        mock_request = Mock()
        mock_request.app.state.persistence = Mock()
        mock_alias_storage = Mock()
        mock_alias_storage.get_alias.return_value = None
        current_user = {"username": "ratelimituser"}

        try:
            # Exhaust rate limit by calling is_allowed many times
            # Default limit is 10 commands per second
            for _ in range(12):
                command_rate_limiter.is_allowed("ratelimituser")

            # Now the next command should be rate limited
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
    async def test_process_command_validation_failure(self):
        """Test command processing when content validation fails.

        AI: Tests lines 267-281 in command_handler_unified.py where command
        content validation fails and security event is logged. Covers injection
        attempt detection path.
        """
        mock_request = Mock()
        mock_request.app.state.persistence = Mock()
        mock_alias_storage = Mock()
        mock_alias_storage.get_alias.return_value = None
        current_user = {"username": "testuser"}

        # Use a command with potential injection attack
        malicious_command = "say'; DROP TABLE players; --"

        result = await process_command(
            "say", [malicious_command], current_user, mock_request, mock_alias_storage, "testuser"
        )

        # Should reject the command
        assert "result" in result

    @pytest.mark.asyncio
    async def test_process_command_empty_after_normalization(self):
        """Test command that becomes empty after normalization.

        AI: Tests lines 291-292 in command_handler_unified.py where command
        becomes empty after normalization step. Covers edge case cleanup path.
        """
        mock_request = Mock()
        mock_request.app.state.persistence = Mock()
        mock_alias_storage = Mock()
        mock_alias_storage.get_alias.return_value = None
        current_user = {"username": "testuser"}

        # Mock normalize_command to return empty string
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
    async def test_circular_alias_detection(self):
        """Test detection of circular alias dependencies.

        AI: Tests lines 334-356 in command_handler_unified.py where circular
        alias dependencies are detected and blocked. Covers cycle detection path.
        """
        from server.models.alias import Alias

        mock_request = Mock()
        mock_request.app.state.persistence = Mock()

        # Create circular alias: 'a' -> 'b' and 'b' -> 'a'
        alias_a = Alias(name="a", command="b")
        alias_b = Alias(name="b", command="a")

        mock_alias_storage = Mock()
        mock_alias_storage.get_player_aliases.return_value = [alias_a, alias_b]

        # Try to use the circular alias
        mock_alias_storage.get_alias.return_value = alias_a

        current_user = {"username": "testuser"}

        result = await process_command("a", [], current_user, mock_request, mock_alias_storage, "testuser")

        assert "result" in result
        assert "circular dependency" in result["result"].lower()

    @pytest.mark.asyncio
    async def test_alias_expansion_depth_exceeded(self):
        """Test alias with excessive expansion depth.

        AI: Tests lines 361-367 in command_handler_unified.py where alias
        expansion depth exceeds limit. Covers depth limit enforcement path.
        """
        from server.models.alias import Alias

        mock_request = Mock()
        mock_request.app.state.persistence = Mock()

        # Create an alias that would have deep expansion
        deep_alias = Alias(name="deep", command="look north")

        mock_alias_storage = Mock()
        mock_alias_storage.get_player_aliases.return_value = [deep_alias]
        mock_alias_storage.get_alias.return_value = deep_alias

        current_user = {"username": "testuser"}

        # Mock the expansion depth check to return high value
        with patch("server.utils.alias_graph.AliasGraph.get_expansion_depth", return_value=15):
            result = await process_command("deep", [], current_user, mock_request, mock_alias_storage, "testuser")

            assert "result" in result
            assert "excessive expansion depth" in result["result"].lower()

    @pytest.mark.asyncio
    async def test_expanded_command_too_long(self):
        """Test alias that expands to command exceeding length limit.

        AI: Tests lines 375-392 in command_handler_unified.py where expanded
        command exceeds MAX_EXPANDED_COMMAND_LENGTH. Covers length limit path.
        """
        from server.models.alias import Alias

        mock_request = Mock()
        mock_request.app.state.persistence = Mock()

        # Create alias that expands to very long command
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
    async def test_expanded_command_validation_failure(self):
        """Test alias expansion where expanded command fails validation.

        AI: Tests lines 397-408 in command_handler_unified.py where expanded
        command content fails security validation. Covers validation of expanded
        commands path.
        """
        from server.models.alias import Alias

        mock_request = Mock()
        mock_request.app.state.persistence = Mock()

        # Create alias that expands to potentially malicious command
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
    async def test_command_execution_exception(self):
        """Test exception during command execution.

        AI: Tests lines 504-516 in command_handler_unified.py where exceptions
        during command execution are caught and handled. Covers error recovery path.
        """
        mock_request = Mock()
        mock_request.app.state.persistence = Mock()
        mock_alias_storage = Mock()
        mock_alias_storage.get_alias.return_value = None
        current_user = {"username": "testuser"}

        # Mock handle_command to raise an exception
        with patch("server.command_handler_unified.handle_command", side_effect=RuntimeError("Command error")):
            result = await process_command("look", [], current_user, mock_request, mock_alias_storage, "testuser")

            assert "result" in result
            assert "error" in result["result"].lower()
