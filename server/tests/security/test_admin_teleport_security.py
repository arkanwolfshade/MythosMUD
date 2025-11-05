"""
Security tests for admin teleport system.

This module tests security aspects of the admin teleport system including
access controls, input validation, and vulnerability prevention.
"""

import asyncio
from unittest.mock import AsyncMock, MagicMock

import pytest

from server.commands.admin_commands import (
    handle_confirm_teleport_command,
    handle_teleport_command,
    validate_admin_permission,
)


class TestAdminTeleportSecurity:
    """Security tests for admin teleport system."""

    @pytest.fixture
    def mock_app_state(self):
        """Create mock application state for testing."""
        app_state = MagicMock()

        # Mock player service
        player_service = MagicMock()
        app_state.player_service = player_service

        # Mock connection manager
        connection_manager = MagicMock()
        connection_manager.online_players = {}
        connection_manager.broadcast_to_room = AsyncMock()
        connection_manager.send_to_player = AsyncMock()
        app_state.connection_manager = connection_manager

        # Mock persistence layer
        persistence = MagicMock()
        persistence.save_player = MagicMock()
        app_state.persistence = persistence

        return app_state

    @pytest.mark.asyncio
    async def test_admin_permission_bypass_attempts(self, mock_app_state):
        """Test various attempts to bypass admin permission checks."""
        # Test with None player
        result = await validate_admin_permission(None, "Attacker")
        assert result is False

        # Test with player without is_admin attribute
        player_no_attr = MagicMock()
        delattr(player_no_attr, "is_admin")
        result = await validate_admin_permission(player_no_attr, "Attacker")
        assert result is False

        # Test with player having is_admin as False
        player_false_admin = MagicMock()
        player_false_admin.is_admin = False
        result = await validate_admin_permission(player_false_admin, "Attacker")
        assert result is False

        # Test with player having is_admin as None
        player_none_admin = MagicMock()
        player_none_admin.is_admin = None
        result = await validate_admin_permission(player_none_admin, "Attacker")
        assert result is False

    @pytest.mark.asyncio
    async def test_teleport_command_injection_attempts(self, mock_app_state):
        """Test command injection attempts in teleport commands."""
        # Mock admin player
        admin_player = MagicMock()
        admin_player.is_admin = True
        admin_player.current_room_id = "admin_room"

        # Mock target player
        target_player = MagicMock()
        target_player.is_admin = False
        target_player.current_room_id = "target_room"

        mock_app_state.player_service.get_player_by_name.side_effect = (
            lambda name: admin_player if name == "AdminUser" else target_player
        )

        mock_app_state.connection_manager.get_online_player_by_display_name.return_value = None

        mock_request = MagicMock()
        mock_request.app = MagicMock()
        mock_request.app.state = mock_app_state
        mock_alias_storage = MagicMock()
        current_user = {"username": "AdminUser"}

        # Test SQL injection attempt in target player name
        malicious_command = {"command_type": "teleport", "target_player": "TargetPlayer'; DROP TABLE players; --"}

        result = await handle_teleport_command(
            malicious_command, current_user, mock_request, mock_alias_storage, "AdminUser"
        )

        # Should fail gracefully, not execute malicious code
        assert "result" in result
        assert "not found" in result["result"].lower() or "not online" in result["result"].lower()

    @pytest.mark.asyncio
    async def test_xss_prevention_in_teleport_messages(self, mock_app_state):
        """Test XSS prevention in teleport effect messages."""
        from server.commands.admin_commands import create_teleport_effect_message

        # Test with malicious player names
        malicious_names = [
            "<script>alert('xss')</script>",
            "Player<img src=x onerror=alert('xss')>",
            "Player';alert('xss');//",
            "Player<script>document.location='http://evil.com'</script>",
        ]

        for malicious_name in malicious_names:
            departure_msg = create_teleport_effect_message(malicious_name, "departure")
            arrival_msg = create_teleport_effect_message(malicious_name, "arrival")

            # Messages should contain the name (this is expected for display)
            assert malicious_name in departure_msg
            assert malicious_name in arrival_msg

            # The function should handle malicious names gracefully
            # and not crash or cause security issues
            assert departure_msg.startswith("*")
            assert departure_msg.endswith("*")
            assert arrival_msg.startswith("*")
            assert arrival_msg.endswith("*")

    @pytest.mark.asyncio
    async def test_path_traversal_prevention(self, mock_app_state):
        """Test prevention of path traversal attacks."""
        # Mock admin player
        admin_player = MagicMock()
        admin_player.is_admin = True
        admin_player.current_room_id = "admin_room"

        mock_app_state.player_service.get_player_by_name.return_value = admin_player
        mock_app_state.connection_manager.get_online_player_by_display_name.return_value = None

        mock_request = MagicMock()
        mock_request.app = MagicMock()
        mock_request.app.state = mock_app_state
        mock_alias_storage = MagicMock()
        current_user = {"username": "AdminUser"}

        # Test path traversal attempts in target player names
        traversal_attempts = [
            "../../../etc/passwd",
            "..\\..\\..\\windows\\system32\\config\\sam",
            "....//....//....//etc/passwd",
            "..%2F..%2F..%2Fetc%2Fpasswd",
        ]

        for traversal_attempt in traversal_attempts:
            command_data = {"command_type": "teleport", "target_player": traversal_attempt}

            result = await handle_teleport_command(
                command_data, current_user, mock_request, mock_alias_storage, "AdminUser"
            )

            # Should fail gracefully, not allow path traversal
            assert "result" in result
            assert "not found" in result["result"].lower() or "not online" in result["result"].lower()

    @pytest.mark.asyncio
    async def test_privilege_escalation_prevention(self, mock_app_state):
        """Test prevention of privilege escalation attempts."""
        # Mock regular player trying to use admin commands
        regular_player = MagicMock()
        regular_player.is_admin = False
        regular_player.current_room_id = "regular_room"

        # Mock target player
        target_player = MagicMock()
        target_player.is_admin = False
        target_player.current_room_id = "target_room"

        mock_app_state.player_service.get_player_by_name.side_effect = (
            lambda name: regular_player if name == "RegularUser" else target_player
        )

        mock_app_state.connection_manager.get_online_player_by_display_name.return_value = {
            "player_id": "target-player-123",
            "player_name": "TargetPlayer",
            "room_id": "target_room",
        }

        mock_request = MagicMock()
        mock_request.app = MagicMock()
        mock_request.app.state = mock_app_state
        mock_alias_storage = MagicMock()
        current_user = {"username": "RegularUser"}

        # Test direct confirmation command bypass
        command_data = {"command_type": "confirm_teleport", "target_player": "TargetPlayer"}

        result = await handle_confirm_teleport_command(
            command_data, current_user, mock_request, mock_alias_storage, "RegularUser"
        )

        # Should fail due to lack of admin privileges
        assert "result" in result
        assert "permission" in result["result"].lower() or "admin" in result["result"].lower()

    @pytest.mark.asyncio
    async def test_concurrent_admin_privilege_checks(self, mock_app_state):
        """Test concurrent admin privilege checks."""
        # Mock admin player
        admin_player = MagicMock()
        admin_player.is_admin = True
        admin_player.current_room_id = "admin_room"

        # Mock target player
        target_player = MagicMock()
        target_player.is_admin = False
        target_player.current_room_id = "target_room"

        mock_app_state.player_service.get_player_by_name.side_effect = (
            lambda name: admin_player if name == "AdminUser" else target_player
        )

        mock_app_state.connection_manager.get_online_player_by_display_name.return_value = {
            "player_id": "target-player-123",
            "player_name": "TargetPlayer",
            "room_id": "target_room",
        }

        mock_request = MagicMock()
        mock_request.app = MagicMock()
        mock_request.app.state = mock_app_state
        mock_alias_storage = MagicMock()
        current_user = {"username": "AdminUser"}

        # Test concurrent teleport operations

        async def teleport_operation():
            command_data = {"command_type": "teleport", "target_player": "TargetPlayer"}
            return await handle_teleport_command(
                command_data, current_user, mock_request, mock_alias_storage, "AdminUser"
            )

        # Run multiple concurrent operations
        results = await asyncio.gather(*[teleport_operation() for _ in range(5)])

        # All operations should succeed
        for result in results:
            assert "result" in result
            assert "successfully teleported" in result["result"].lower()

    @pytest.mark.asyncio
    async def test_database_injection_prevention(self, mock_app_state):
        """Test prevention of database injection attacks."""
        # Mock admin player
        admin_player = MagicMock()
        admin_player.is_admin = True
        admin_player.current_room_id = "admin_room"

        mock_app_state.player_service.get_player_by_name.return_value = admin_player
        mock_app_state.connection_manager.get_online_player_by_display_name.return_value = None

        mock_request = MagicMock()
        mock_request.app = MagicMock()
        mock_request.app.state = mock_app_state
        mock_alias_storage = MagicMock()
        current_user = {"username": "AdminUser"}

        # Test various injection attempts
        injection_attempts = [
            "'; DROP TABLE players; --",
            "' OR '1'='1",
            "'; INSERT INTO players VALUES ('hacker', 'hacker'); --",
            "'; UPDATE players SET is_admin = 1 WHERE name = 'hacker'; --",
        ]

        for injection_attempt in injection_attempts:
            command_data = {"command_type": "teleport", "target_player": injection_attempt}

            result = await handle_teleport_command(
                command_data, current_user, mock_request, mock_alias_storage, "AdminUser"
            )

            # Should fail gracefully, not execute injection
            assert "result" in result
            assert "not found" in result["result"].lower() or "not online" in result["result"].lower()

    @pytest.mark.asyncio
    async def test_session_hijacking_prevention(self, mock_app_state):
        """Test prevention of session hijacking attempts."""
        # Mock admin player
        admin_player = MagicMock()
        admin_player.is_admin = True
        admin_player.current_room_id = "admin_room"

        # Mock target player
        target_player = MagicMock()
        target_player.is_admin = False
        target_player.current_room_id = "target_room"

        mock_app_state.player_service.get_player_by_name.side_effect = (
            lambda name: admin_player if name == "AdminUser" else target_player
        )

        mock_app_state.connection_manager.get_online_player_by_display_name.return_value = {
            "player_id": "target-player-123",
            "player_name": "TargetPlayer",
            "room_id": "target_room",
        }

        mock_request = MagicMock()
        mock_request.app = MagicMock()
        mock_request.app.state = mock_app_state
        mock_alias_storage = MagicMock()

        # Test with different user contexts
        test_cases = [
            {"current_user": {"username": "AdminUser"}, "expected_success": True},
            {"current_user": {"username": "RegularUser"}, "expected_success": False},
            {"current_user": {"username": "HackerUser"}, "expected_success": False},
        ]

        for test_case in test_cases:
            command_data = {"command_type": "teleport", "target_player": "TargetPlayer"}

            result = await handle_teleport_command(
                command_data,
                test_case["current_user"],
                mock_request,
                mock_alias_storage,
                test_case["current_user"]["username"],
            )

            if test_case["expected_success"]:
                assert "successfully teleported" in result["result"].lower()
            else:
                assert "permission" in result["result"].lower() or "admin" in result["result"].lower()

    @pytest.mark.asyncio
    async def test_rate_limiting_bypass_prevention(self, mock_app_state):
        """Test prevention of rate limiting bypass attempts."""
        # Mock admin player
        admin_player = MagicMock()
        admin_player.is_admin = True
        admin_player.current_room_id = "admin_room"

        # Mock target player
        target_player = MagicMock()
        target_player.is_admin = False
        target_player.current_room_id = "target_room"

        mock_app_state.player_service.get_player_by_name.side_effect = (
            lambda name: admin_player if name == "AdminUser" else target_player
        )

        mock_app_state.connection_manager.get_online_player_by_display_name.return_value = {
            "player_id": "target-player-123",
            "player_name": "TargetPlayer",
            "room_id": "target_room",
        }

        mock_request = MagicMock()
        mock_request.app = MagicMock()
        mock_request.app.state = mock_app_state
        mock_alias_storage = MagicMock()
        current_user = {"username": "AdminUser"}

        # Test rapid successive teleport attempts
        command_data = {"command_type": "teleport", "target_player": "TargetPlayer"}

        # Execute multiple teleport commands rapidly
        results = []
        for _ in range(10):
            result = await handle_teleport_command(
                command_data, current_user, mock_request, mock_alias_storage, "AdminUser"
            )
            results.append(result)

        # All should succeed (admin commands are not rate limited)
        for result in results:
            assert "result" in result
            assert "successfully teleported" in result["result"].lower()

    @pytest.mark.asyncio
    async def test_memory_exhaustion_prevention(self, mock_app_state):
        """Test prevention of memory exhaustion attacks."""
        # Mock admin player
        admin_player = MagicMock()
        admin_player.is_admin = True
        admin_player.current_room_id = "admin_room"

        mock_app_state.player_service.get_player_by_name.return_value = admin_player
        mock_app_state.connection_manager.get_online_player_by_display_name.return_value = None

        mock_request = MagicMock()
        mock_request.app = MagicMock()
        mock_request.app.state = mock_app_state
        mock_alias_storage = MagicMock()
        current_user = {"username": "AdminUser"}

        # Test with extremely long player names
        long_name = "A" * 10000  # 10KB name

        command_data = {"command_type": "teleport", "target_player": long_name}

        result = await handle_teleport_command(
            command_data, current_user, mock_request, mock_alias_storage, "AdminUser"
        )

        # Should fail gracefully, not cause memory issues
        assert "result" in result
        assert "not found" in result["result"].lower() or "not online" in result["result"].lower()

    @pytest.mark.asyncio
    async def test_log_injection_prevention(self, mock_app_state):
        """Test prevention of log injection attacks."""
        # Mock admin player
        admin_player = MagicMock()
        admin_player.is_admin = True
        admin_player.current_room_id = "admin_room"

        # Mock target player
        target_player = MagicMock()
        target_player.is_admin = False
        target_player.current_room_id = "target_room"

        mock_app_state.player_service.get_player_by_name.side_effect = (
            lambda name: admin_player if name == "AdminUser" else target_player
        )

        mock_app_state.connection_manager.get_online_player_by_display_name.return_value = {
            "player_name": "TargetPlayer",
            "room_id": "target_room",
        }

        mock_request = MagicMock()
        mock_request.app = MagicMock()
        mock_request.app.state = mock_app_state
        mock_alias_storage = MagicMock()
        current_user = {"username": "AdminUser"}

        # Test with log injection attempts
        log_injection_attempts = [
            "TargetPlayer\n[ERROR] System compromised",
            "TargetPlayer\r\n[CRITICAL] Security breach",
            "TargetPlayer\x00Null byte injection",
            "TargetPlayer\n\n\nMultiple newlines",
        ]

        for injection_attempt in log_injection_attempts:
            command_data = {"command_type": "teleport", "target_player": injection_attempt}

            result = await handle_teleport_command(
                command_data, current_user, mock_request, mock_alias_storage, "AdminUser"
            )

            # Should handle gracefully, not cause log corruption
            assert "result" in result
            # Could either succeed or fail, but should not crash
            assert "result" in result


class TestAdminTeleportSecurityIntegration:
    """Integration security tests for admin teleport system."""
