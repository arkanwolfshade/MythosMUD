"""
Tests for NPC admin command permission validation.

This module tests permission validation for NPC admin commands.
"""

from server.commands.npc_admin_commands import validate_npc_admin_permission


class TestNPCAdminPermissions:
    """Test class for NPC admin permission validation."""

    def test_validate_npc_admin_permission_admin_user(self, mock_admin_player):
        """Test that admin users have NPC admin permissions."""
        result = validate_npc_admin_permission(mock_admin_player, "admin_player")
        assert result is True

    def test_validate_npc_admin_permission_regular_user(self, mock_regular_player):
        """Test that regular users do not have NPC admin permissions."""
        result = validate_npc_admin_permission(mock_regular_player, "regular_player")
        assert result is False

    def test_validate_npc_admin_permission_no_player(self):
        """Test that None player returns False."""
        result = validate_npc_admin_permission(None, "nonexistent_player")
        assert result is False

    def test_validate_npc_admin_permission_no_admin_attr(self):
        """Test that player without is_admin attribute returns False."""

        class MockPlayer:
            def __init__(self):
                self.name = "test_player"
                # No is_admin attribute

        player = MockPlayer()
        result = validate_npc_admin_permission(player, "test_player")
        assert result is False
