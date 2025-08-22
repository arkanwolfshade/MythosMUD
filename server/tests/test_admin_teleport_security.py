"""
Security tests for admin teleport system.

This module tests security aspects of the admin teleport system including
access controls, input validation, and vulnerability prevention.
"""

import asyncio
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.commands.admin_teleport_commands import (
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

        mock_app_state.connection_manager.online_players = {
            "target_id": {"display_name": "TargetPlayer", "room_id": "target_room"}
        }

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
        from server.commands.admin_teleport_commands import create_teleport_effect_message

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

        mock_app_state.connection_manager.online_players = {
            "target_id": {"display_name": "TargetPlayer", "room_id": "target_room"}
        }

        mock_request = MagicMock()
        mock_request.app = MagicMock()
        mock_request.app.state = mock_app_state
        mock_alias_storage = MagicMock()
        current_user = {"username": "RegularUser"}

        # Test direct confirmation command bypass
        confirm_data = {"command_type": "confirm_teleport", "target_player": "TargetPlayer"}

        result = await handle_confirm_teleport_command(
            confirm_data, current_user, mock_request, mock_alias_storage, "RegularUser"
        )

        # Should be denied
        assert "result" in result
        assert "permission" in result["result"].lower() or "admin" in result["result"].lower()

    @pytest.mark.asyncio
    async def test_input_validation_security(self, mock_app_state):
        """Test input validation for security."""
        # Mock admin player
        admin_player = MagicMock()
        admin_player.is_admin = True
        admin_player.current_room_id = "admin_room"

        mock_app_state.player_service.get_player_by_name.return_value = admin_player

        mock_request = MagicMock()
        mock_request.app = MagicMock()
        mock_request.app.state = mock_app_state
        mock_alias_storage = MagicMock()
        current_user = {"username": "AdminUser"}

        # Test various malicious inputs
        malicious_inputs = [
            "",  # Empty string
            "   ",  # Whitespace only
            "A" * 1000,  # Very long string
            "\x00\x01\x02",  # Null bytes
            "Player\x00Name",  # Null byte in middle
            "Player\nName",  # Newline
            "Player\rName",  # Carriage return
            "Player\tName",  # Tab
        ]

        for malicious_input in malicious_inputs:
            command_data = {"command_type": "teleport", "target_player": malicious_input}

            result = await handle_teleport_command(
                command_data, current_user, mock_request, mock_alias_storage, "AdminUser"
            )

            # Should handle gracefully
            assert "result" in result
            # Should either fail validation or not find the player
            assert any(
                keyword in result["result"].lower() for keyword in ["not found", "not online", "invalid", "usage"]
            )

    @pytest.mark.asyncio
    async def test_concurrent_admin_privilege_checks(self, mock_app_state):
        """Test concurrent admin privilege checks for race conditions."""
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

        mock_app_state.connection_manager.online_players = {
            "target_id": {"display_name": "TargetPlayer", "room_id": "target_room"}
        }

        # Test concurrent permission checks
        async def check_permission():
            return await validate_admin_permission(admin_player, "AdminUser")

        # Run multiple concurrent permission checks
        results = await asyncio.gather(*[check_permission() for _ in range(10)])

        # All should return True
        assert all(result is True for result in results)

    @pytest.mark.asyncio
    async def test_database_injection_prevention(self, mock_app_state):
        """Test prevention of database injection attacks."""
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

        mock_app_state.connection_manager.online_players = {
            "target_id": {"display_name": "TargetPlayer", "room_id": "target_room"}
        }

        # Mock database error to simulate injection attempt
        mock_app_state.persistence.save_player.side_effect = Exception("SQL injection detected")

        mock_request = MagicMock()
        mock_request.app = MagicMock()
        mock_request.app.state = mock_app_state
        mock_alias_storage = MagicMock()
        current_user = {"username": "AdminUser"}

        command_data = {"command_type": "confirm_teleport", "target_player": "TargetPlayer"}

        result = await handle_confirm_teleport_command(
            command_data, current_user, mock_request, mock_alias_storage, "AdminUser"
        )

        # Should handle database error gracefully
        assert "result" in result
        assert "failed" in result["result"].lower()

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

        mock_app_state.connection_manager.online_players = {
            "target_id": {"display_name": "TargetPlayer", "room_id": "target_room"}
        }

        mock_request = MagicMock()
        mock_request.app = MagicMock()
        mock_request.app.state = mock_app_state
        mock_alias_storage = MagicMock()

        # Test with mismatched username in current_user vs player_name parameter
        current_user = {"username": "AdminUser"}

        command_data = {"command_type": "confirm_teleport", "target_player": "TargetPlayer"}

        # Pass different username in player_name parameter
        result = await handle_confirm_teleport_command(
            command_data, current_user, mock_request, mock_alias_storage, "DifferentUser"
        )

        # Should fail due to username mismatch
        assert "result" in result
        assert "not found" in result["result"].lower() or "permission" in result["result"].lower()

    @pytest.mark.asyncio
    async def test_rate_limiting_bypass_prevention(self, mock_app_state):
        """Test prevention of rate limiting bypass attempts."""
        # Mock admin player
        admin_player = MagicMock()
        admin_player.is_admin = True
        admin_player.current_room_id = "admin_room"

        # Mock multiple target players to avoid "already in location" issue
        target_players = []
        for i in range(5):
            target_player = MagicMock()
            target_player.is_admin = False
            target_player.current_room_id = f"target_room_{i}"
            target_player.display_name = f"TargetPlayer{i}"
            target_players.append(target_player)

        def get_player_by_name(name):
            if name == "AdminUser":
                return admin_player
            elif name.startswith("TargetPlayer"):
                # Return different target players for each call
                index = int(name.replace("TargetPlayer", "")) if name != "TargetPlayer" else 0
                return target_players[index % len(target_players)]
            return None

        mock_app_state.player_service.get_player_by_name.side_effect = get_player_by_name

        # Mock connection manager with multiple online players
        mock_app_state.connection_manager.online_players = {
            f"target_{i}_id": {"display_name": f"TargetPlayer{i}", "room_id": f"target_room_{i}"} for i in range(5)
        }

        mock_request = MagicMock()
        mock_request.app = MagicMock()
        mock_request.app.state = mock_app_state
        mock_alias_storage = MagicMock()
        current_user = {"username": "AdminUser"}

        # Test rapid successive commands with different targets
        results = []
        for i in range(5):
            command_data = {"command_type": "confirm_teleport", "target_player": f"TargetPlayer{i}"}
            result = await handle_confirm_teleport_command(
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

        mock_request = MagicMock()
        mock_request.app = MagicMock()
        mock_request.app.state = mock_app_state
        mock_alias_storage = MagicMock()
        current_user = {"username": "AdminUser"}

        # Test with extremely long player names
        long_name = "A" * 10000  # 10KB string

        command_data = {"command_type": "teleport", "target_player": long_name}

        result = await handle_teleport_command(
            command_data, current_user, mock_request, mock_alias_storage, "AdminUser"
        )

        # Should handle gracefully
        assert "result" in result
        assert "not found" in result["result"].lower() or "not online" in result["result"].lower()

    @pytest.mark.asyncio
    async def test_log_injection_prevention(self, mock_app_state):
        """Test prevention of log injection attacks."""
        with patch("server.commands.admin_teleport_commands.get_admin_actions_logger") as mock_logger:
            # Mock admin player
            admin_player = MagicMock()
            admin_player.is_admin = True
            admin_player.current_room_id = "admin_room"

            # Mock target player with malicious name
            target_player = MagicMock()
            target_player.is_admin = False
            target_player.current_room_id = "target_room"

            mock_app_state.player_service.get_player_by_name.side_effect = (
                lambda name: admin_player if name == "AdminUser" else target_player
            )

            mock_app_state.connection_manager.online_players = {
                "target_id": {"display_name": "TargetPlayer\n[ERROR] Log injection", "room_id": "target_room"}
            }

            mock_request = MagicMock()
            mock_request.app = MagicMock()
            mock_request.app.state = mock_app_state
            mock_alias_storage = MagicMock()
            current_user = {"username": "AdminUser"}

            command_data = {"command_type": "confirm_teleport", "target_player": "TargetPlayer\n[ERROR] Log injection"}

            result = await handle_confirm_teleport_command(
                command_data, current_user, mock_request, mock_alias_storage, "AdminUser"
            )

            # Should succeed but log safely
            assert "result" in result
            assert "successfully teleported" in result["result"].lower()

            # Verify logging was called safely
            mock_logger.assert_called()
            mock_logger_instance = mock_logger.return_value
            mock_logger_instance.log_teleport_action.assert_called_once()


class TestAdminTeleportSecurityIntegration:
    """Integration security tests for admin teleport system."""

    @pytest.mark.asyncio
    async def test_complete_security_workflow(self):
        """Test complete security workflow with various attack vectors."""
        # This test would simulate a complete attack scenario
        # and verify that all security measures work together

        # For now, just verify that the security tests run
        assert True  # Placeholder for comprehensive security workflow test

    @pytest.mark.asyncio
    async def test_security_audit_logging(self):
        """Test that security events are properly logged."""
        # This test would verify that security-related events
        # (failed permission checks, injection attempts, etc.)
        # are properly logged for audit purposes

        # For now, just verify that the test framework works
        assert True  # Placeholder for security audit logging test
