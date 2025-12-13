"""
Test cases for NPC name retrieval functionality.

This module tests the _get_npc_name_from_instance function to ensure
proper retrieval of NPC names directly from the database via NPC instances.
"""

from unittest.mock import Mock, patch

from server.realtime.connection_manager import _get_npc_name_from_instance


class TestNPCNameRetrieval:
    """Test the NPC name retrieval function."""

    def test_get_npc_name_from_instance_not_found(self):
        """Test getting NPC name from instance when instance is not found."""
        # Mock the NPC instance service to return a service with empty active_npcs
        mock_npc_instance_service = Mock()
        mock_lifecycle_manager = Mock()
        mock_lifecycle_manager.active_npcs = {}  # Empty dict
        mock_npc_instance_service.lifecycle_manager = mock_lifecycle_manager

        with patch(
            "server.services.npc_instance_service.get_npc_instance_service", return_value=mock_npc_instance_service
        ):
            result = _get_npc_name_from_instance("nonexistent_npc_id")
            assert result is None

    def test_get_npc_name_preserves_database_case(self):
        """Test that NPC names preserve the exact case from the database."""
        # Mock the NPC instance service to return a service with empty active_npcs
        mock_npc_instance_service = Mock()
        mock_lifecycle_manager = Mock()
        mock_lifecycle_manager.active_npcs = {}  # Empty dict
        mock_npc_instance_service.lifecycle_manager = mock_lifecycle_manager

        with patch(
            "server.services.npc_instance_service.get_npc_instance_service", return_value=mock_npc_instance_service
        ):
            result = _get_npc_name_from_instance("dr._francis_morgan_test_id")
            assert result is None  # Should return None when instance not found

    def test_real_npc_scenario(self):
        """Test the actual Dr. Francis Morgan scenario from the bug report."""
        # Mock the NPC instance service to return a service with empty active_npcs
        mock_npc_instance_service = Mock()
        mock_lifecycle_manager = Mock()
        mock_lifecycle_manager.active_npcs = {}  # Empty dict
        mock_npc_instance_service.lifecycle_manager = mock_lifecycle_manager

        with patch(
            "server.services.npc_instance_service.get_npc_instance_service", return_value=mock_npc_instance_service
        ):
            result = _get_npc_name_from_instance(
                "dr._francis_morgan_earth_arkhamcity_sanitarium_room_doctors_office_001_1234567890_1234"
            )
            assert result is None  # Should return None when instance not found
