"""
Unit tests for connection utils.

Tests the connection_utils module functions.
"""

from unittest.mock import MagicMock, patch

from server.realtime.connection_utils import get_npc_name_from_instance


def test_get_npc_name_from_instance_success():
    """Test get_npc_name_from_instance() returns NPC name when found."""
    npc_id = "npc_123"
    npc_name = "Test NPC"
    mock_npc = MagicMock()
    mock_npc.name = npc_name

    with patch("server.services.npc_instance_service.get_npc_instance_service") as mock_get_service:
        mock_service = MagicMock()
        mock_service.lifecycle_manager.active_npcs = {npc_id: mock_npc}
        mock_get_service.return_value = mock_service

        result = get_npc_name_from_instance(npc_id)
        assert result == npc_name


def test_get_npc_name_from_instance_not_found():
    """Test get_npc_name_from_instance() returns None when NPC not found."""
    npc_id = "npc_123"

    with patch("server.services.npc_instance_service.get_npc_instance_service") as mock_get_service:
        mock_service = MagicMock()
        mock_service.lifecycle_manager.active_npcs = {}
        mock_get_service.return_value = mock_service

        result = get_npc_name_from_instance(npc_id)
        assert result is None


def test_get_npc_name_from_instance_no_name():
    """Test get_npc_name_from_instance() returns None when NPC has no name."""
    npc_id = "npc_123"
    mock_npc = MagicMock()
    del mock_npc.name  # Remove name attribute

    with patch("server.services.npc_instance_service.get_npc_instance_service") as mock_get_service:
        mock_service = MagicMock()
        mock_service.lifecycle_manager.active_npcs = {npc_id: mock_npc}
        mock_get_service.return_value = mock_service

        result = get_npc_name_from_instance(npc_id)
        assert result is None


def test_get_npc_name_from_instance_no_service():
    """Test get_npc_name_from_instance() returns None when service not available."""
    npc_id = "npc_123"

    with patch("server.services.npc_instance_service.get_npc_instance_service", return_value=None):
        result = get_npc_name_from_instance(npc_id)
        assert result is None


def test_get_npc_name_from_instance_no_lifecycle_manager():
    """Test get_npc_name_from_instance() returns None when no lifecycle manager."""
    npc_id = "npc_123"

    with patch("server.services.npc_instance_service.get_npc_instance_service") as mock_get_service:
        mock_service = MagicMock()
        del mock_service.lifecycle_manager  # Remove lifecycle_manager
        mock_get_service.return_value = mock_service

        result = get_npc_name_from_instance(npc_id)
        assert result is None


def test_get_npc_name_from_instance_handles_exception():
    """Test get_npc_name_from_instance() handles exceptions."""
    npc_id = "npc_123"

    with patch("server.services.npc_instance_service.get_npc_instance_service", side_effect=AttributeError("Error")):
        result = get_npc_name_from_instance(npc_id)
        assert result is None
