"""
Tests for mute data loading consistency across message types.

This module tests the synchronization issues where mute data loaded in one
part of the message processing pipeline (e.g., ChatService) is not available
in another part (e.g., NATSMessageHandler).
"""

from unittest.mock import MagicMock, patch

from server.realtime.nats_message_handler import NATSMessageHandler
from server.services.nats_service import NATSService
from server.services.user_manager import UserManager


class TestMuteDataConsistency:
    """Test mute data loading consistency across message processing pipeline."""

    def setup_method(self):
        """Set up test fixtures."""
        self.mock_nats_service = MagicMock(spec=NATSService)
        self.mock_connection_manager = MagicMock()
        self.handler = NATSMessageHandler(self.mock_nats_service)

    @patch("server.realtime.nats_message_handler.connection_manager")
    @patch("server.services.user_manager.UserManager")
    def test_mute_data_not_shared_between_user_manager_instances(
        self, mock_user_manager_class, mock_connection_manager
    ):
        """Test that mute data loaded in one UserManager instance is not available in another."""
        # Create a UserManager instance that will be used in NATSMessageHandler
        user_manager = MagicMock(spec=UserManager)
        mock_user_manager_class.return_value = user_manager

        # Simulate the scenario where mute data was loaded in ChatService but not in NATSMessageHandler
        # The UserManager instance in NATSMessageHandler doesn't have the mute data loaded
        user_manager._player_mutes = {}  # No mute data loaded
        user_manager.is_player_muted.return_value = False  # No mute found
        user_manager.is_player_muted_by_others.return_value = False
        user_manager.is_admin.return_value = False

        # Test that mute check fails because data isn't loaded in this instance
        result = self.handler._is_player_muted_by_receiver("receiver_1", "sender_1")

        # Should return False because the UserManager instance doesn't have the mute data
        assert result is False

        # Verify UserManager was created
        mock_user_manager_class.assert_called_once()

    @patch("server.realtime.nats_message_handler.connection_manager")
    @patch("server.services.user_manager.UserManager")
    def test_mute_data_loading_timing_issue(self, mock_user_manager_class, mock_connection_manager):
        """Test that mute data loading timing can cause inconsistent results."""
        user_manager = MagicMock(spec=UserManager)
        mock_user_manager_class.return_value = user_manager

        # Simulate mute data not being loaded yet
        user_manager._player_mutes = None
        user_manager.is_player_muted.return_value = False
        user_manager.is_player_muted_by_others.return_value = False
        user_manager.is_admin.return_value = False

        # Test mute check when data isn't loaded
        result = self.handler._is_player_muted_by_receiver("receiver_1", "sender_1")

        # Should return False because mute data isn't available
        assert result is False

        # Verify UserManager was created
        mock_user_manager_class.assert_called_once()

    @patch("server.realtime.nats_message_handler.connection_manager")
    @patch("server.services.user_manager.UserManager")
    def test_load_player_mutes_called_during_filtering(self, mock_user_manager_class, mock_connection_manager):
        """Test that load_player_mutes is called during mute filtering."""
        user_manager = MagicMock(spec=UserManager)
        mock_user_manager_class.return_value = user_manager

        # Set up mute data
        user_manager._player_mutes = {
            "receiver_1": {"sender_1": {"reason": "test", "timestamp": "2024-01-01T00:00:00Z"}}
        }
        user_manager.is_player_muted.return_value = True
        user_manager.is_player_muted_by_others.return_value = False
        user_manager.is_admin.return_value = False

        # Test mute check
        result = self.handler._is_player_muted_by_receiver("receiver_1", "sender_1")

        # Should return True
        assert result is True

        # Verify load_player_mutes was called (this is good - it ensures data is loaded)
        user_manager.load_player_mutes.assert_called_once_with("receiver_1")

    @patch("server.realtime.nats_message_handler.connection_manager")
    @patch("server.services.user_manager.UserManager")
    def test_mute_data_consistency_across_message_types(self, mock_user_manager_class, mock_connection_manager):
        """Test that mute data is consistent across different message types."""
        user_manager = MagicMock(spec=UserManager)
        mock_user_manager_class.return_value = user_manager

        # Set up mute data
        user_manager._player_mutes = {
            "receiver_1": {"sender_1": {"reason": "test", "timestamp": "2024-01-01T00:00:00Z"}}
        }
        user_manager.is_player_muted.return_value = True
        user_manager.is_player_muted_by_others.return_value = False
        user_manager.is_admin.return_value = False

        # Test mute check for different message types
        channels = ["say", "emote", "pose", "local"]
        for channel in channels:
            result = self.handler._is_player_muted_by_receiver("receiver_1", "sender_1")
            assert result is True, f"Mute check failed for channel: {channel}"

        # Verify UserManager was created for each check (this is inefficient)
        assert mock_user_manager_class.call_count == len(channels)

    @patch("server.realtime.nats_message_handler.connection_manager")
    @patch("server.services.user_manager.UserManager")
    def test_user_manager_instance_creation_overhead(self, mock_user_manager_class, mock_connection_manager):
        """Test that creating new UserManager instances for each mute check is inefficient."""
        user_manager = MagicMock(spec=UserManager)
        mock_user_manager_class.return_value = user_manager

        # Set up mute data
        user_manager._player_mutes = {
            "receiver_1": {"sender_1": {"reason": "test", "timestamp": "2024-01-01T00:00:00Z"}}
        }
        user_manager.is_player_muted.return_value = True
        user_manager.is_player_muted_by_others.return_value = False
        user_manager.is_admin.return_value = False

        # Simulate multiple mute checks (as would happen in a room with multiple players)
        receiver_ids = ["receiver_1", "receiver_2", "receiver_3"]
        sender_id = "sender_1"

        for receiver_id in receiver_ids:
            result = self.handler._is_player_muted_by_receiver(receiver_id, sender_id)
            assert result is True

        # Verify a new UserManager was created for each check
        assert mock_user_manager_class.call_count == len(receiver_ids)

    @patch("server.realtime.nats_message_handler.connection_manager")
    @patch("server.services.user_manager.UserManager")
    def test_mute_data_loading_failure_handling(self, mock_user_manager_class, mock_connection_manager):
        """Test that mute data loading failures are handled gracefully."""
        user_manager = MagicMock(spec=UserManager)
        mock_user_manager_class.return_value = user_manager

        # Simulate mute data loading failure
        user_manager.load_player_mutes.side_effect = Exception("Database error")
        user_manager._player_mutes = None
        user_manager.is_player_muted.return_value = False
        user_manager.is_player_muted_by_others.return_value = False
        user_manager.is_admin.return_value = False

        # Test mute check when loading fails
        result = self.handler._is_player_muted_by_receiver("receiver_1", "sender_1")

        # Should return False (not muted) when loading fails
        assert result is False

    @patch("server.realtime.nats_message_handler.connection_manager")
    @patch("server.services.user_manager.UserManager")
    def test_global_mute_consistency(self, mock_user_manager_class, mock_connection_manager):
        """Test that global mute data is consistent across UserManager instances."""
        user_manager = MagicMock(spec=UserManager)
        mock_user_manager_class.return_value = user_manager

        # Set up global mute data
        user_manager._player_mutes = {}
        user_manager.is_player_muted.return_value = False
        user_manager.is_player_muted_by_others.return_value = True  # Globally muted
        user_manager.is_admin.return_value = False

        # Test mute check for global mute
        result = self.handler._is_player_muted_by_receiver("receiver_1", "sender_1")

        # Should return True because sender is globally muted
        assert result is True

    @patch("server.realtime.nats_message_handler.connection_manager")
    @patch("server.services.user_manager.UserManager")
    def test_admin_override_consistency(self, mock_user_manager_class, mock_connection_manager):
        """Test that admin override for global mutes is consistent."""
        user_manager = MagicMock(spec=UserManager)
        mock_user_manager_class.return_value = user_manager

        # Set up global mute with admin receiver
        user_manager._player_mutes = {}
        user_manager.is_player_muted.return_value = False
        user_manager.is_player_muted_by_others.return_value = True  # Globally muted
        user_manager.is_admin.return_value = True  # Receiver is admin

        # Test mute check for admin receiver
        result = self.handler._is_player_muted_by_receiver("receiver_1", "sender_1")

        # Should return False because admin can see globally muted players
        assert result is False
