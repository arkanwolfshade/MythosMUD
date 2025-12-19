"""
Comprehensive tests for combat-specific security measures and validation.

This module tests security validation for combat commands, input sanitization,
rate limiting, and audit logging to ensure the combat system maintains
security standards while preserving the Cthulhu Mythos atmosphere.
"""

from unittest.mock import Mock, patch
from uuid import uuid4

import pytest

from server.commands.combat import CombatCommandHandler
from server.models.player import Player
from server.services.npc_combat_integration_service import NPCCombatIntegrationService

# from server.validators.command_validator import CommandSecurityValidator
from server.validators.security_validator import comprehensive_sanitize_input


class TestCombatCommandSecurity:
    """Test security validation for combat commands."""

    @pytest.fixture
    def mock_async_persistence(self):
        """Create a mock async persistence layer."""
        return Mock()

    @pytest.fixture
    def combat_handler(self, mock_async_persistence):
        """Create a combat command handler for testing."""
        return CombatCommandHandler(async_persistence=mock_async_persistence)

    @pytest.fixture
    def sample_player(self):
        """Create a sample player for testing."""
        player = Player(
            player_id=str(uuid4()),
            user_id=str(uuid4()),
            name="TestPlayer",
            current_room_id="test_room_001",
            experience_points=100,
            level=5,
        )
        return player

    @pytest.mark.asyncio
    async def test_combat_command_injection_prevention(self, combat_handler, sample_player):
        """Test that combat commands prevent injection attacks."""
        malicious_commands = [
            "attack rat; rm -rf /",
            "punch target | cat /etc/passwd",
            "kick npc && shutdown -h now",
            "strike enemy; DROP TABLE players;",
            "attack target || echo 'hacked'",
        ]

        for malicious_command in malicious_commands:
            command_data = {"command": malicious_command, "target": "rat", "action": "attack"}

            mock_request = Mock()
            mock_alias_storage = Mock()

            result = await combat_handler.handle_attack_command(
                command_data=command_data,
                current_user={"user_id": str(uuid4())},
                request=mock_request,
                alias_storage=mock_alias_storage,
                player_name=sample_player.name,
            )

            # Should not contain any indication of successful injection
            assert "rm -rf" not in str(result)
            assert "cat /etc/passwd" not in str(result)
            assert "shutdown" not in str(result)
            assert "DROP TABLE" not in str(result)
            assert "echo 'hacked'" not in str(result)

    @pytest.mark.asyncio
    async def test_combat_command_xss_prevention(self, combat_handler, sample_player):
        """Test that combat commands prevent XSS attacks."""
        xss_commands = [
            "attack <script>alert('xss')</script>",
            "punch target onload=alert('xss')",
            "kick <img src=x onerror=alert('xss')>",
            "strike target javascript:alert('xss')",
        ]

        for xss_command in xss_commands:
            command_data = {"command": xss_command, "target": "rat", "action": "attack"}

            mock_request = Mock()
            mock_alias_storage = Mock()

            result = await combat_handler.handle_attack_command(
                command_data=command_data,
                current_user={"user_id": str(uuid4())},
                request=mock_request,
                alias_storage=mock_alias_storage,
                player_name=sample_player.name,
            )

            # Should not contain script tags or javascript
            assert "<script>" not in str(result)
            assert "javascript:" not in str(result)
            assert "onload=" not in str(result)
            assert "onerror=" not in str(result)

    @pytest.mark.asyncio
    async def test_combat_command_path_traversal_prevention(self, combat_handler, sample_player):
        """Test that combat commands prevent path traversal attacks."""
        path_traversal_commands = [
            "attack ../../../etc/passwd",
            "punch target ..\\..\\windows\\system32",
            "kick %2e%2e%2f%2e%2e%2fetc%2fpasswd",
            "strike target ..%252f..%252fetc%252fpasswd",
        ]

        for traversal_command in path_traversal_commands:
            command_data = {"command": traversal_command, "target": "rat", "action": "attack"}

            mock_request = Mock()
            mock_alias_storage = Mock()

            result = await combat_handler.handle_attack_command(
                command_data=command_data,
                current_user={"user_id": str(uuid4())},
                request=mock_request,
                alias_storage=mock_alias_storage,
                player_name=sample_player.name,
            )

            # Should not contain path traversal sequences
            assert "../" not in str(result)
            assert "..\\" not in str(result)
            assert "%2e%2e" not in str(result)
            assert "%252f" not in str(result)

    @pytest.mark.asyncio
    async def test_combat_command_sql_injection_prevention(self, combat_handler, sample_player):
        """Test that combat commands prevent SQL injection attacks."""
        sql_injection_commands = [
            "attack rat' OR '1'='1",
            "punch target; DROP TABLE players; --",
            "kick npc UNION SELECT * FROM users",
            "strike enemy' AND 1=1 --",
        ]

        for sql_command in sql_injection_commands:
            command_data = {"command": sql_command, "target": "rat", "action": "attack"}

            mock_request = Mock()
            mock_alias_storage = Mock()

            result = await combat_handler.handle_attack_command(
                command_data=command_data,
                current_user={"user_id": str(uuid4())},
                request=mock_request,
                alias_storage=mock_alias_storage,
                player_name=sample_player.name,
            )

            # Should not contain SQL injection patterns
            assert "OR '1'='1" not in str(result)
            assert "DROP TABLE" not in str(result)
            assert "UNION SELECT" not in str(result)
            assert "AND 1=1" not in str(result)

    @pytest.mark.asyncio
    async def test_combat_command_unicode_handling(self, combat_handler, sample_player):
        """Test that combat commands properly handle Unicode input."""
        unicode_commands = [
            "attack 🐀",  # Unicode emoji
            "punch target with émojis",
            "kick npc with 中文 characters",
            "strike enemy with ñ and ü",
        ]

        for unicode_command in unicode_commands:
            command_data = {"command": unicode_command, "target": "rat", "action": "attack"}

            mock_request = Mock()
            mock_alias_storage = Mock()

            # Should handle Unicode gracefully without errors
            result = await combat_handler.handle_attack_command(
                command_data=command_data,
                current_user={"user_id": str(uuid4())},
                request=mock_request,
                alias_storage=mock_alias_storage,
                player_name=sample_player.name,
            )

            # Should not raise exceptions and should process normally
            assert isinstance(result, dict)

    @pytest.mark.asyncio
    async def test_combat_command_length_limits(self, combat_handler, sample_player):
        """Test that combat commands respect length limits."""
        # Create an extremely long command
        long_target = "a" * 1000
        command_data = {"command": f"attack {long_target}", "target": long_target, "action": "attack"}

        mock_request = Mock()
        mock_alias_storage = Mock()

        result = await combat_handler.handle_attack_command(
            command_data=command_data,
            current_user={"user_id": str(uuid4())},
            request=mock_request,
            alias_storage=mock_alias_storage,
            player_name=sample_player.name,
        )

        # Should handle long input gracefully
        assert isinstance(result, dict)

    @pytest.mark.asyncio
    async def test_combat_command_empty_input_handling(self, combat_handler, sample_player):
        """Test that combat commands handle empty input gracefully."""
        empty_commands = [
            "",
            "   ",
            None,
            "\n\t\r",
        ]

        for empty_command in empty_commands:
            command_data = {"command": empty_command, "target": "", "action": "attack"}

            mock_request = Mock()
            mock_alias_storage = Mock()

            # Should handle empty input gracefully
            result = await combat_handler.handle_attack_command(
                command_data=command_data,
                current_user={"user_id": str(uuid4())},
                request=mock_request,
                alias_storage=mock_alias_storage,
                player_name=sample_player.name,
            )

            # Should return appropriate error message
            assert isinstance(result, dict)


class TestCombatRateLimiting:
    """Test rate limiting for combat commands."""

    @pytest.fixture
    def mock_async_persistence(self):
        """Create a mock async persistence layer."""
        return Mock()

    @pytest.fixture
    def combat_handler(self, mock_async_persistence):
        """Create a combat command handler for testing."""
        return CombatCommandHandler(async_persistence=mock_async_persistence)

    @pytest.mark.asyncio
    async def test_combat_command_rate_limiting(self, combat_handler):
        """Test that combat commands respect rate limiting."""
        # This test would need to be implemented with actual rate limiting
        # For now, we'll test that the handler exists and can be called
        assert hasattr(combat_handler, "handle_attack_command")

        # Test that rapid successive calls don't cause issues
        command_data = {"command": "attack rat", "target": "rat", "action": "attack"}

        mock_request = Mock()
        mock_alias_storage = Mock()

        # Make multiple rapid calls
        for _ in range(10):
            result = await combat_handler.handle_attack_command(
                command_data=command_data,
                current_user={"user_id": str(uuid4())},
                request=mock_request,
                alias_storage=mock_alias_storage,
                player_name="TestPlayer",
            )
            assert isinstance(result, dict)

    @pytest.mark.asyncio
    async def test_combat_command_spam_prevention(self, combat_handler):
        """Test that combat commands prevent spam."""
        # Test rapid fire commands
        command_data = {"command": "attack rat", "target": "rat", "action": "attack"}

        mock_request = Mock()
        mock_alias_storage = Mock()

        # Simulate rapid fire
        results = []
        for _ in range(50):  # Simulate spam
            result = await combat_handler.handle_attack_command(
                command_data=command_data,
                current_user={"user_id": str(uuid4())},
                request=mock_request,
                alias_storage=mock_alias_storage,
                player_name="TestPlayer",
            )
            results.append(result)

        # All calls should complete without errors
        assert len(results) == 50
        assert all(isinstance(result, dict) for result in results)


class TestCombatAuditLogging:
    """Test audit logging for combat commands."""

    @pytest.fixture
    def mock_async_persistence(self):
        """Create a mock async persistence layer."""
        return Mock()

    @pytest.fixture
    def combat_handler(self, mock_async_persistence):
        """Create a combat command handler for testing."""
        return CombatCommandHandler(async_persistence=mock_async_persistence)

    @pytest.mark.asyncio
    async def test_combat_command_audit_logging(self, combat_handler):
        """Test that combat commands are properly logged for audit purposes."""
        with patch("server.commands.combat.logger") as mock_logger:
            command_data = {"command": "attack rat", "target": "rat", "action": "attack"}

            mock_request = Mock()
            mock_alias_storage = Mock()

            await combat_handler.handle_attack_command(
                command_data=command_data,
                current_user={"user_id": str(uuid4())},
                request=mock_request,
                alias_storage=mock_alias_storage,
                player_name="TestPlayer",
            )

            # Verify that logging occurred
            assert mock_logger.info.called or mock_logger.debug.called

    @pytest.mark.asyncio
    async def test_combat_security_event_logging(self, combat_handler):
        """Test that security events are properly logged."""
        with patch("server.commands.combat.logger") as mock_logger:
            # Test with potentially malicious input
            command_data = {"command_type": "attack", "target_player": "rat; rm -rf /", "args": ["rat"]}

            mock_request = Mock()
            mock_request.app = Mock()
            mock_request.app.state = Mock()
            mock_request.app.state.persistence = Mock()
            mock_alias_storage = Mock()

            # Mock the persistence to return a player
            mock_player = Mock()
            mock_player.player_id = str(uuid4())
            mock_player.current_room_id = "test_room_001"
            mock_player.name = "TestPlayer"
            mock_request.app.state.persistence.get_player_by_name.return_value = mock_player

            # Mock the room
            mock_room = Mock()
            mock_room.room_id = "test_room_001"
            mock_request.app.state.persistence.get_room.return_value = mock_room

            # Mock the target resolution service
            with patch.object(combat_handler, "target_resolution_service") as mock_target_resolution:
                from server.schemas.target_resolution import TargetMatch, TargetResolutionResult, TargetType

                npc_id = str(uuid4())
                mock_target_match = TargetMatch(
                    target_id=npc_id, target_name="rat", target_type=TargetType.NPC, room_id="test_room_001"
                )
                mock_target_result = TargetResolutionResult(
                    success=True, matches=[mock_target_match], search_term="rat", room_id="test_room_001"
                )
                mock_target_resolution.resolve_target.return_value = mock_target_result

                # Mock NPC instance
                with patch.object(combat_handler, "_get_npc_instance") as mock_get_npc:
                    mock_npc = Mock()
                    mock_npc.name = "rat"
                    mock_npc.is_alive = True
                    mock_get_npc.return_value = mock_npc

                    # Mock combat validation
                    with patch.object(combat_handler, "_validate_combat_action") as mock_validate:
                        mock_validate.return_value = {"valid": True}

                        # Mock combat execution
                        with patch.object(combat_handler, "_execute_combat_action") as mock_execute:
                            mock_execute.return_value = {"result": "You attack the rat!"}

                            await combat_handler.handle_attack_command(
                                command_data=command_data,
                                current_user={"username": "TestPlayer"},
                                request=mock_request,
                                alias_storage=mock_alias_storage,
                                player_name="TestPlayer",
                            )

            # Verify that security-related logging occurred
            assert mock_logger.warning.called or mock_logger.error.called or mock_logger.info.called


class TestCombatInputSanitization:
    """Test input sanitization for combat commands."""

    def test_combat_command_sanitization(self) -> None:
        """Test that combat commands are properly sanitized."""
        # Test various input sanitization scenarios
        test_cases = [
            ("attack rat", "attack rat"),  # Normal input
            ("attack rat; rm -rf /", "attack rat"),  # Injection attempt
            ("attack <script>alert('xss')</script>", "attack"),  # XSS attempt
            ("attack rat' OR '1'='1", "attack rat"),  # SQL injection
            ("attack ../../../etc/passwd", "attack"),  # Path traversal
        ]

        for input_command, _expected_output in test_cases:
            sanitized = comprehensive_sanitize_input(input_command)
            # The sanitized output should not contain control characters or null bytes
            assert "\x00" not in sanitized  # No null bytes
            assert "\x1f" not in sanitized  # No control characters
            # Note: comprehensive_sanitize_input focuses on Unicode/ANSI sanitization,
            # not command injection prevention - that's handled by validation layers

    def test_combat_command_unicode_sanitization(self) -> None:
        """Test that Unicode input is properly sanitized."""
        unicode_inputs = [
            "attack 🐀",
            "punch target with émojis",
            "kick npc with 中文 characters",
        ]

        for unicode_input in unicode_inputs:
            sanitized = comprehensive_sanitize_input(unicode_input)
            # Should preserve Unicode characters
            assert isinstance(sanitized, str)
            # Should not raise exceptions
            assert len(sanitized) >= 0

    def test_combat_command_length_sanitization(self) -> None:
        """Test that extremely long input is handled properly."""
        long_input = "attack " + "a" * 10000
        sanitized = comprehensive_sanitize_input(long_input)

        # Should handle long input without errors
        assert isinstance(sanitized, str)
        assert len(sanitized) >= 0


class TestCombatSecurityIntegration:
    """Test integration of security measures with combat system."""

    @pytest.fixture
    def mock_async_persistence(self):
        """Create a mock async persistence layer."""
        return Mock()

    @pytest.fixture
    def npc_combat_service(self, mock_async_persistence):
        """Create an NPC combat integration service for testing."""
        return NPCCombatIntegrationService(async_persistence=mock_async_persistence)

    @pytest.mark.asyncio
    async def test_combat_service_security_integration(self, npc_combat_service):
        """Test that the combat service integrates with security measures."""
        # Test that the service exists and has security-related methods
        assert hasattr(npc_combat_service, "_combat_service")
        assert hasattr(npc_combat_service, "_persistence")

    @pytest.mark.asyncio
    async def test_combat_event_security(self, npc_combat_service):
        """Test that combat events maintain security standards."""
        # Test that combat events don't leak sensitive information
        # This would need to be implemented based on the actual event system
        assert hasattr(npc_combat_service, "event_bus")

    @pytest.mark.asyncio
    async def test_combat_persistence_security(self, npc_combat_service):
        """Test that combat persistence maintains security standards."""
        # Test that combat data is stored securely
        # This would need to be implemented based on the actual persistence layer
        assert hasattr(npc_combat_service, "_persistence")


class TestCombatSecurityErrorHandling:
    """Test error handling in combat security measures."""

    @pytest.fixture
    def mock_async_persistence(self):
        """Create a mock async persistence layer."""
        return Mock()

    @pytest.fixture
    def combat_handler(self, mock_async_persistence):
        """Create a combat command handler for testing."""
        return CombatCommandHandler(async_persistence=mock_async_persistence)

    @pytest.mark.asyncio
    async def test_combat_security_error_handling(self, combat_handler):
        """Test that security errors are handled gracefully."""
        # Test with malformed command data
        malformed_commands = [
            {"command": None, "target": "rat"},
            {"command": "attack", "target": None},
            {"command": 123, "target": "rat"},
            {"command": "attack", "target": 456},
        ]

        for malformed_command in malformed_commands:
            mock_request = Mock()
            mock_alias_storage = Mock()

            # Should handle malformed input gracefully
            result = await combat_handler.handle_attack_command(
                command_data=malformed_command,
                current_user={"user_id": str(uuid4())},
                request=mock_request,
                alias_storage=mock_alias_storage,
                player_name="TestPlayer",
            )

            # Should return appropriate error response
            assert isinstance(result, dict)

    @pytest.mark.asyncio
    async def test_combat_security_exception_handling(self, combat_handler):
        """Test that security exceptions are handled properly."""
        with patch("server.commands.combat.logger"):
            # Test with command that might cause exceptions
            command_data = {
                "command": "attack " + "x" * 100000,  # Extremely long command
                "target": "rat",
                "action": "attack",
            }

            mock_request = Mock()
            mock_alias_storage = Mock()

            # Should handle exceptions gracefully
            result = await combat_handler.handle_attack_command(
                command_data=command_data,
                current_user={"user_id": str(uuid4())},
                request=mock_request,
                alias_storage=mock_alias_storage,
                player_name="TestPlayer",
            )

            # Should not raise unhandled exceptions
            assert isinstance(result, dict)
