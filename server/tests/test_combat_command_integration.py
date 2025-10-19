"""
Tests for combat command integration with the command system.

This module tests the integration of combat commands with the existing
command validation and routing system.
"""

from unittest.mock import MagicMock

import pytest

from server.commands.combat import CombatCommandHandler
from server.commands.command_service import CommandService


class TestCombatCommandIntegration:
    """Test combat command integration with command system."""

    def test_combat_commands_registered(self):
        """Test that combat commands are registered in command service."""
        command_service = CommandService()

        # Check that combat commands are registered
        assert "attack" in command_service.command_handlers
        assert "punch" in command_service.command_handlers
        assert "kick" in command_service.command_handlers
        assert "strike" in command_service.command_handlers

    @pytest.mark.asyncio
    async def test_attack_command_no_target(self):
        """Test attack command with no target specified."""
        handler = CombatCommandHandler()

        command_data = {
            "command_type": "attack",
            "args": [],
            "target_player": None,
        }

        result = await handler.handle_attack_command(
            command_data=command_data,
            current_user={},
            request=MagicMock(),
            alias_storage=MagicMock(),
            player_name="TestPlayer",
        )

        # Check that we get a no_target error message (could be any of several thematic messages)
        error_messages = [
            "You must focus your wrath upon a specific target, lest your fury be wasted.",
            "The void stares back at you, demanding a name to direct your hatred.",
            "Your anger needs direction - who shall bear the brunt of your assault?",
            "The cosmic forces require a target for your destructive intent.",
        ]
        assert result["result"] in error_messages

    @pytest.mark.asyncio
    async def test_attack_command_with_target(self):
        """Test attack command with target specified."""
        handler = CombatCommandHandler()

        command_data = {
            "command_type": "attack",
            "args": ["goblin"],
            "target_player": "goblin",
        }

        # Mock current_user with player_id and room_id (use a real room ID)
        current_user = {
            "player_id": "test_player_123",
            "room_id": "earth_arkhamcity_campus_intersection_boundary_crane",
        }

        result = await handler.handle_attack_command(
            command_data=command_data,
            current_user=current_user,
            request=MagicMock(),
            alias_storage=MagicMock(),
            player_name="TestPlayer",
        )

        # Since we don't have a real player or NPC in the test, expect a "No target named" message
        assert "No target named 'goblin' found" in result["result"]

    @pytest.mark.asyncio
    async def test_punch_command_alias(self):
        """Test punch command alias."""
        handler = CombatCommandHandler()

        command_data = {
            "command_type": "punch",
            "args": ["rat"],
            "target_player": "rat",
        }

        # Mock current_user with player_id and room_id (use a real room ID)
        current_user = {
            "player_id": "test_player_123",
            "room_id": "earth_arkhamcity_campus_intersection_boundary_crane",
        }

        result = await handler.handle_attack_command(
            command_data=command_data,
            current_user=current_user,
            request=MagicMock(),
            alias_storage=MagicMock(),
            player_name="TestPlayer",
        )

        # Since we don't have a real player or NPC in the test, expect a "No target named" message
        assert "No target named 'rat' found" in result["result"]

    @pytest.mark.asyncio
    async def test_kick_command_alias(self):
        """Test kick command alias."""
        handler = CombatCommandHandler()

        command_data = {
            "command_type": "kick",
            "args": ["skeleton"],
            "target_player": "skeleton",
        }

        # Mock current_user with player_id and room_id (use a real room ID)
        current_user = {
            "player_id": "test_player_123",
            "room_id": "earth_arkhamcity_campus_intersection_boundary_crane",
        }

        result = await handler.handle_attack_command(
            command_data=command_data,
            current_user=current_user,
            request=MagicMock(),
            alias_storage=MagicMock(),
            player_name="TestPlayer",
        )

        # Since we don't have a real player or NPC in the test, expect a "No target named" message
        assert "No target named 'skeleton' found" in result["result"]

    @pytest.mark.asyncio
    async def test_strike_command_alias(self):
        """Test strike command alias."""
        handler = CombatCommandHandler()

        command_data = {
            "command_type": "strike",
            "args": ["orc"],
            "target_player": "orc",
        }

        # Mock current_user with player_id and room_id (use a real room ID)
        current_user = {
            "player_id": "test_player_123",
            "room_id": "earth_arkhamcity_campus_intersection_boundary_crane",
        }

        result = await handler.handle_attack_command(
            command_data=command_data,
            current_user=current_user,
            request=MagicMock(),
            alias_storage=MagicMock(),
            player_name="TestPlayer",
        )

        # Since we don't have a real player or NPC in the test, expect a "No target named" message
        assert "No target named 'orc' found" in result["result"]

    @pytest.mark.asyncio
    async def test_invalid_combat_command(self):
        """Test invalid combat command."""
        handler = CombatCommandHandler()

        command_data = {
            "command_type": "invalid_command",
            "args": ["target"],
            "target_player": "target",
        }

        result = await handler.handle_attack_command(
            command_data=command_data,
            current_user={},
            request=MagicMock(),
            alias_storage=MagicMock(),
            player_name="TestPlayer",
        )

        # Since we don't have a room_id in current_user, expect "You are not in a room." message
        assert "You are not in a room." in result["result"]

    def test_attack_aliases_defined(self):
        """Test that attack aliases are properly defined."""
        handler = CombatCommandHandler()

        expected_aliases = {"attack", "punch", "kick", "strike", "hit", "smack", "thump"}

        assert handler.attack_aliases == expected_aliases
