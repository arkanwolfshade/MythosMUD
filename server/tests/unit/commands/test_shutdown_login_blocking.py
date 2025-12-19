"""
Tests for login and character progression blocking during shutdown.

This module tests that players are prevented from logging in or progressing
through character creation when a server shutdown is pending.

As documented in the Pnakotic Manuscripts, one must not admit new initiates
to the Archives when the emergency protocols have been activated.
"""

from unittest.mock import MagicMock

# Tests will verify that shutdown checks are integrated into endpoints
# Actual endpoint modifications will be done in subsequent subtasks


class TestLoginBlockingDuringShutdown:
    """Test login blocking when shutdown is pending."""

    def test_shutdown_check_helper_function_exists(self) -> None:
        """Test that shutdown check helper function exists."""
        from server.commands.admin_shutdown_command import is_shutdown_pending

        # Function should exist and be callable
        assert callable(is_shutdown_pending)

    def test_is_shutdown_pending_true(self) -> None:
        """Test shutdown check returns True when shutdown is pending."""
        from server.commands.admin_shutdown_command import is_shutdown_pending

        mock_app = MagicMock()
        mock_app.state.server_shutdown_pending = True

        result = is_shutdown_pending(mock_app)

        assert result is True

    def test_is_shutdown_pending_false(self) -> None:
        """Test shutdown check returns False when no shutdown."""
        from server.commands.admin_shutdown_command import is_shutdown_pending

        mock_app = MagicMock()
        mock_app.state.server_shutdown_pending = False

        result = is_shutdown_pending(mock_app)

        assert result is False

    def test_is_shutdown_pending_missing_attribute(self) -> None:
        """Test shutdown check handles missing attribute gracefully."""
        from server.commands.admin_shutdown_command import is_shutdown_pending

        mock_app = MagicMock(spec=[])  # No server_shutdown_pending attribute

        result = is_shutdown_pending(mock_app)

        # Should default to False when attribute doesn't exist
        assert result is False


class TestCharacterCreationBlockingDuringShutdown:
    """Test character creation blocking when shutdown is pending."""

    def test_character_creation_blocked_message(self) -> None:
        """Test that appropriate message is returned when creation blocked."""
        from server.commands.admin_shutdown_command import get_shutdown_blocking_message

        message = get_shutdown_blocking_message("character_creation")

        assert "shutting" in message.lower() or "shutdown" in message.lower()
        assert "character" in message.lower() or "creation" in message.lower()

    def test_stats_rolling_blocked_message(self) -> None:
        """Test that appropriate message is returned when stats rolling blocked."""
        from server.commands.admin_shutdown_command import get_shutdown_blocking_message

        message = get_shutdown_blocking_message("stats_rolling")

        assert "shutting" in message.lower() or "shutdown" in message.lower()


class TestMOTDProgressionBlockingDuringShutdown:
    """Test MOTD progression blocking when shutdown is pending."""

    def test_motd_progression_blocked_message(self) -> None:
        """Test that appropriate message is returned when MOTD progression blocked."""
        from server.commands.admin_shutdown_command import get_shutdown_blocking_message

        message = get_shutdown_blocking_message("motd_progression")

        assert "shutting" in message.lower() or "shutdown" in message.lower()
        assert "later" in message.lower() or "try again" in message.lower()


class TestShutdownBlockingIntegration:
    """Test integration of shutdown blocking across multiple endpoints."""

    def test_get_shutdown_blocking_message_various_contexts(self) -> None:
        """Test shutdown blocking messages for different contexts."""
        from server.commands.admin_shutdown_command import get_shutdown_blocking_message

        contexts = ["login", "character_creation", "stats_rolling", "motd_progression"]

        for context in contexts:
            message = get_shutdown_blocking_message(context)
            assert isinstance(message, str)
            assert len(message) > 0
            assert "shutting" in message.lower() or "shutdown" in message.lower()
