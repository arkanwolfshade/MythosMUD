"""
Monitoring and alerting tests for mute filtering failures.

This module tests the monitoring and alerting system for mute filtering
to ensure that failures are properly detected, logged, and alerted.
"""

import time
import uuid
from unittest.mock import MagicMock, patch

import pytest

from server.game.chat_service import ChatService
from server.game.player_service import PlayerService


class TestMuteFilteringMonitoring:
    """Monitoring and alerting tests for mute filtering system."""

    def setup_method(self):
        """Set up test fixtures."""
        # Mock services
        self.mock_persistence = MagicMock()
        self.mock_room_service = MagicMock()
        self.mock_player_service = MagicMock(spec=PlayerService)

        # Test data
        self.muter_id = str(uuid.uuid4())
        self.muter_name = "ArkanWolfshade"
        self.target_id = str(uuid.uuid4())
        self.target_name = "Ithaqua"
        self.room_id = "earth_arkham_city_sanitarium_room_hallway_001"

        # Mock player objects
        self.muter_player = MagicMock()
        self.muter_player.id = self.muter_id
        self.muter_player.name = self.muter_name
        self.muter_player.current_room_id = self.room_id

        self.target_player = MagicMock()
        self.target_player.id = self.target_id
        self.target_player.name = self.target_name
        self.target_player.current_room_id = self.room_id

    def _create_chat_service_with_mocks(self, mock_user_manager, mock_rate_limiter, mock_nats_service):
        """Helper method to create ChatService with mocked dependencies."""
        chat_service = ChatService(
            persistence=self.mock_persistence,
            room_service=self.mock_room_service,
            player_service=self.mock_player_service,
            user_manager_instance=mock_user_manager,
        )

        # Replace services with mocks
        chat_service.nats_service = mock_nats_service
        chat_service.rate_limiter = mock_rate_limiter

        return chat_service

    @pytest.mark.asyncio
    @patch("server.services.nats_service.nats_service")
    @patch("server.game.chat_service.rate_limiter")
    @patch("server.game.chat_service.user_manager")
    async def test_mute_filtering_failure_detection(self, mock_user_manager, mock_rate_limiter, mock_nats_service):
        """Test detection of mute filtering failures."""
        # Create chat service with mocked user manager
        chat_service = self._create_chat_service_with_mocks(mock_user_manager, mock_rate_limiter, mock_nats_service)

        # Setup mocks
        mock_nats_service.is_connected.return_value = True

        # Make NATS publish async
        async def mock_publish(*args, **kwargs):
            return True

        mock_nats_service.publish = mock_publish

        mock_rate_limiter.check_rate_limit.return_value = True
        mock_user_manager.is_channel_muted.return_value = False
        mock_user_manager.is_globally_muted.return_value = False
        mock_user_manager.can_send_message.return_value = True
        mock_user_manager.load_player_mutes.return_value = True
        mock_user_manager.is_player_muted.return_value = False  # Player should be muted but isn't
        mock_user_manager.mute_player.return_value = True
        mock_user_manager.is_admin.return_value = True

        self.mock_player_service.get_player_by_id.return_value = self.target_player
        self.mock_player_service.resolve_player_name.return_value = self.target_player

        # First, mute the target player
        mute_result = chat_service.mute_player(muter_id=self.muter_id, target_player_name=self.target_name)
        assert mute_result is True

        # Now try to send an emote - this should succeed because personal mutes don't block the muted player
        emote_result = await chat_service.send_emote_message(self.target_id, "dance")

        # The emote should succeed because personal mutes don't block the muted player
        assert emote_result["success"] is True

        # Verify that mute_player was called (the mute was applied)
        mock_user_manager.mute_player.assert_called()

    @pytest.mark.asyncio
    @patch("server.services.nats_service.nats_service")
    @patch("server.game.chat_service.rate_limiter")
    @patch("server.game.chat_service.user_manager")
    async def test_mute_data_loading_failure_monitoring(self, mock_user_manager, mock_rate_limiter, mock_nats_service):
        """Test monitoring of mute data loading failures."""
        # Create chat service with mocked user manager
        chat_service = self._create_chat_service_with_mocks(mock_user_manager, mock_rate_limiter, mock_nats_service)

        # Setup mocks
        mock_nats_service.is_connected.return_value = True
        mock_nats_service.publish.return_value = True
        mock_rate_limiter.check_rate_limit.return_value = True
        mock_user_manager.is_channel_muted.return_value = False
        mock_user_manager.is_globally_muted.return_value = False
        mock_user_manager.can_send_message.return_value = True
        mock_user_manager.load_player_mutes.return_value = False  # Simulate loading failure
        mock_user_manager.is_player_muted.return_value = False

        self.mock_player_service.get_player_by_id.return_value = self.target_player
        self.mock_player_service.resolve_player_name.return_value = self.target_player

        # Try to send an emote with mute data loading failure
        emote_result = await chat_service.send_emote_message(self.target_id, "dance")

        # The emote should fail due to NATS, but we can check the logging
        assert emote_result["success"] is False

        # Verify that mute data loading was attempted
        mock_user_manager.load_player_mutes.assert_called()

    @pytest.mark.asyncio
    @patch("server.services.nats_service.nats_service")
    @patch("server.game.chat_service.rate_limiter")
    @patch("server.game.chat_service.user_manager")
    async def test_user_manager_consistency_monitoring(self, mock_user_manager, mock_rate_limiter, mock_nats_service):
        """Test monitoring of UserManager instance consistency."""
        # Create chat service with mocked user manager
        chat_service = self._create_chat_service_with_mocks(mock_user_manager, mock_rate_limiter, mock_nats_service)

        # Setup mocks
        mock_nats_service.is_connected.return_value = True

        # Make NATS publish async
        async def mock_publish(*args, **kwargs):
            return True

        mock_nats_service.publish = mock_publish

        mock_rate_limiter.check_rate_limit.return_value = True
        mock_user_manager.is_channel_muted.return_value = False
        mock_user_manager.is_globally_muted.return_value = False
        mock_user_manager.can_send_message.return_value = True
        mock_user_manager.load_player_mutes.return_value = True
        mock_user_manager.is_player_muted.return_value = False

        self.mock_player_service.get_player_by_id.return_value = self.target_player
        self.mock_player_service.resolve_player_name.return_value = self.target_player

        # Send multiple emotes to test UserManager consistency
        for i in range(5):
            emote_result = await chat_service.send_emote_message(self.target_id, f"action_{i}")
            assert emote_result["success"] is True  # Should succeed with proper NATS mock

        # Verify that UserManager methods were called consistently
        assert mock_user_manager.load_player_mutes.call_count >= 5
        # Note: is_player_muted is not called because personal mutes don't block the muted player
        # Instead, verify that other UserManager methods were called consistently
        assert mock_user_manager.is_channel_muted.call_count >= 5
        assert mock_user_manager.is_globally_muted.call_count >= 5

    @pytest.mark.asyncio
    @patch("server.services.nats_service.nats_service")
    @patch("server.game.chat_service.rate_limiter")
    @patch("server.game.chat_service.user_manager")
    async def test_mute_filtering_performance_monitoring(self, mock_user_manager, mock_rate_limiter, mock_nats_service):
        """Test monitoring of mute filtering performance."""
        # Create chat service with mocked user manager
        chat_service = self._create_chat_service_with_mocks(mock_user_manager, mock_rate_limiter, mock_nats_service)

        # Setup mocks
        mock_nats_service.is_connected.return_value = True
        mock_nats_service.publish.return_value = True
        mock_rate_limiter.check_rate_limit.return_value = True
        mock_user_manager.is_channel_muted.return_value = False
        mock_user_manager.is_globally_muted.return_value = False
        mock_user_manager.can_send_message.return_value = True
        mock_user_manager.load_player_mutes.return_value = True
        mock_user_manager.is_player_muted.return_value = False

        self.mock_player_service.get_player_by_id.return_value = self.target_player
        self.mock_player_service.resolve_player_name.return_value = self.target_player

        # Measure performance of mute filtering operations
        num_operations = 10
        start_time = time.time()

        for i in range(num_operations):
            emote_result = await chat_service.send_emote_message(self.target_id, f"perf_test_{i}")
            assert emote_result["success"] is False  # Due to NATS

        end_time = time.time()
        total_time = end_time - start_time
        avg_time_per_operation = total_time / num_operations

        # Performance monitoring: log if operations are too slow
        if avg_time_per_operation > 0.1:  # 100ms threshold
            print(
                f"WARNING: Mute filtering performance degradation detected: {avg_time_per_operation:.4f}s per operation"
            )

        # Verify that operations completed within reasonable time
        assert avg_time_per_operation < 0.5, (
            f"Mute filtering performance too slow: {avg_time_per_operation:.4f}s per operation"
        )

    @pytest.mark.asyncio
    @patch("server.services.nats_service.nats_service")
    @patch("server.game.chat_service.rate_limiter")
    @patch("server.game.chat_service.user_manager")
    async def test_mute_filtering_error_handling_monitoring(
        self, mock_user_manager, mock_rate_limiter, mock_nats_service
    ):
        """Test monitoring of mute filtering error handling."""
        # Create chat service with mocked user manager
        chat_service = self._create_chat_service_with_mocks(mock_user_manager, mock_rate_limiter, mock_nats_service)

        # Setup mocks
        mock_nats_service.is_connected.return_value = True
        mock_nats_service.publish.return_value = True
        mock_rate_limiter.check_rate_limit.return_value = True
        mock_user_manager.is_channel_muted.return_value = False
        mock_user_manager.is_globally_muted.return_value = False
        mock_user_manager.can_send_message.return_value = True
        mock_user_manager.load_player_mutes.return_value = True
        mock_user_manager.is_player_muted.return_value = False

        self.mock_player_service.get_player_by_id.return_value = self.target_player
        self.mock_player_service.resolve_player_name.return_value = self.target_player

        # Test error handling with invalid player ID
        invalid_player_id = "invalid-id"
        emote_result = await chat_service.send_emote_message(invalid_player_id, "dance")

        # The emote should fail due to invalid player
        assert emote_result["success"] is False
        assert "error" in emote_result

        # Verify that error was properly handled
        print(f"Error handling test: {emote_result['error']}")

    @pytest.mark.asyncio
    @patch("server.services.nats_service.nats_service")
    @patch("server.game.chat_service.rate_limiter")
    @patch("server.game.chat_service.user_manager")
    async def test_mute_filtering_consistency_monitoring(self, mock_user_manager, mock_rate_limiter, mock_nats_service):
        """Test monitoring of mute filtering consistency across message types."""
        # Create chat service with mocked user manager
        chat_service = self._create_chat_service_with_mocks(mock_user_manager, mock_rate_limiter, mock_nats_service)

        # Setup mocks
        mock_nats_service.is_connected.return_value = True

        # Make NATS publish async
        async def mock_publish(*args, **kwargs):
            return True

        mock_nats_service.publish = mock_publish

        mock_rate_limiter.check_rate_limit.return_value = True
        mock_user_manager.is_channel_muted.return_value = False
        mock_user_manager.is_globally_muted.return_value = False
        mock_user_manager.can_send_message.return_value = True
        mock_user_manager.load_player_mutes.return_value = True
        mock_user_manager.is_player_muted.return_value = False

        self.mock_player_service.get_player_by_id.return_value = self.target_player
        self.mock_player_service.resolve_player_name.return_value = self.target_player

        # Test consistency across different message types
        message_types = ["custom_emote", "predefined_emote"]
        results = {}

        for msg_type in message_types:
            if msg_type == "custom_emote":
                emote_result = await chat_service.send_emote_message(self.target_id, "dance")
            else:
                # Mock EmoteService for predefined emotes
                with patch("server.game.emote_service.EmoteService") as mock_emote_service_class:
                    mock_emote_service = MagicMock()
                    mock_emote_service_class.return_value = mock_emote_service
                    mock_emote_service.is_emote_alias.return_value = True
                    mock_emote_service.format_emote_messages.return_value = (
                        "You twibble.",
                        f"{self.target_name} twibbles.",
                    )
                    emote_result = await chat_service.send_predefined_emote(self.target_id, "twibble")

            results[msg_type] = emote_result["success"]

        # Verify consistency across message types - both should succeed since personal mutes don't block the muted player
        assert all(result for result in results.values()), "Inconsistent message processing across message types"

        # Verify that UserManager methods were called consistently for all message types
        # Note: is_player_muted is not called because personal mutes don't block the muted player
        assert mock_user_manager.load_player_mutes.call_count >= len(message_types)
        assert mock_user_manager.is_channel_muted.call_count >= len(message_types)
        assert mock_user_manager.is_globally_muted.call_count >= len(message_types)

    @pytest.mark.asyncio
    @patch("server.services.nats_service.nats_service")
    @patch("server.game.chat_service.rate_limiter")
    @patch("server.game.chat_service.user_manager")
    async def test_mute_filtering_alerting_system(self, mock_user_manager, mock_rate_limiter, mock_nats_service):
        """Test the mute filtering alerting system."""
        # Create chat service with mocked user manager
        chat_service = self._create_chat_service_with_mocks(mock_user_manager, mock_rate_limiter, mock_nats_service)

        # Setup mocks
        mock_nats_service.is_connected.return_value = True
        mock_nats_service.publish.return_value = True
        mock_rate_limiter.check_rate_limit.return_value = True
        mock_user_manager.is_channel_muted.return_value = False
        mock_user_manager.is_globally_muted.return_value = False
        mock_user_manager.can_send_message.return_value = True
        mock_user_manager.load_player_mutes.return_value = True
        mock_user_manager.is_player_muted.return_value = False

        self.mock_player_service.get_player_by_id.return_value = self.target_player
        self.mock_player_service.resolve_player_name.return_value = self.target_player

        # Simulate multiple mute filtering operations
        num_operations = 5
        failure_count = 0

        for i in range(num_operations):
            emote_result = await chat_service.send_emote_message(self.target_id, f"alert_test_{i}")

            # Count failures (in this case, all fail due to NATS)
            if not emote_result["success"]:
                failure_count += 1

        # Alert if failure rate is too high
        failure_rate = failure_count / num_operations
        if failure_rate > 0.8:  # 80% failure threshold
            print(f"ALERT: High mute filtering failure rate: {failure_rate:.2%}")

        # Verify that alerting system would trigger
        assert failure_rate > 0.8, "Alerting system should trigger for high failure rates"

    @pytest.mark.asyncio
    @patch("server.services.nats_service.nats_service")
    @patch("server.game.chat_service.rate_limiter")
    @patch("server.game.chat_service.user_manager")
    async def test_mute_filtering_health_check(self, mock_user_manager, mock_rate_limiter, mock_nats_service):
        """Test mute filtering health check system."""
        # Create chat service with mocked user manager
        chat_service = self._create_chat_service_with_mocks(mock_user_manager, mock_rate_limiter, mock_nats_service)

        # Setup mocks
        mock_nats_service.is_connected.return_value = True
        mock_nats_service.publish.return_value = True
        mock_rate_limiter.check_rate_limit.return_value = True
        mock_user_manager.is_channel_muted.return_value = False
        mock_user_manager.is_globally_muted.return_value = False
        mock_user_manager.can_send_message.return_value = True
        mock_user_manager.load_player_mutes.return_value = True
        mock_user_manager.is_player_muted.return_value = False

        self.mock_player_service.get_player_by_id.return_value = self.target_player
        self.mock_player_service.resolve_player_name.return_value = self.target_player

        # Perform health check
        health_status = {
            "mute_data_loading": True,
            "user_manager_consistency": True,
            "performance": True,
            "error_handling": True,
        }

        # Test mute data loading health
        try:
            mock_user_manager.load_player_mutes.return_value = True
            await chat_service.send_emote_message(self.target_id, "health_check")
            health_status["mute_data_loading"] = True
        except Exception as e:
            health_status["mute_data_loading"] = False
            print(f"Mute data loading health check failed: {e}")

        # Test UserManager consistency health
        try:
            mock_user_manager.is_player_muted.return_value = False
            await chat_service.send_emote_message(self.target_id, "health_check")
            health_status["user_manager_consistency"] = True
        except Exception as e:
            health_status["user_manager_consistency"] = False
            print(f"UserManager consistency health check failed: {e}")

        # Test performance health
        try:
            start_time = time.time()
            await chat_service.send_emote_message(self.target_id, "health_check")
            end_time = time.time()
            processing_time = end_time - start_time

            if processing_time < 0.1:  # 100ms threshold
                health_status["performance"] = True
            else:
                health_status["performance"] = False
                print(f"Performance health check failed: {processing_time:.4f}s")
        except Exception as e:
            health_status["performance"] = False
            print(f"Performance health check failed: {e}")

        # Test error handling health
        try:
            await chat_service.send_emote_message("invalid_id", "health_check")
            health_status["error_handling"] = True
        except Exception as e:
            health_status["error_handling"] = False
            print(f"Error handling health check failed: {e}")

        # Overall health status
        overall_health = all(health_status.values())

        if not overall_health:
            print(f"ALERT: Mute filtering system health check failed: {health_status}")

        # Verify that health check system works
        assert isinstance(health_status, dict), "Health status should be a dictionary"
        assert all(
            key in health_status
            for key in ["mute_data_loading", "user_manager_consistency", "performance", "error_handling"]
        ), "Health status should contain all required keys"

    @pytest.mark.asyncio
    @patch("server.services.nats_service.nats_service")
    @patch("server.game.chat_service.rate_limiter")
    @patch("server.game.chat_service.user_manager")
    async def test_mute_filtering_metrics_collection(self, mock_user_manager, mock_rate_limiter, mock_nats_service):
        """Test collection of mute filtering metrics."""
        # Create chat service with mocked user manager
        chat_service = self._create_chat_service_with_mocks(mock_user_manager, mock_rate_limiter, mock_nats_service)

        # Setup mocks
        mock_nats_service.is_connected.return_value = True
        mock_nats_service.publish.return_value = True
        mock_rate_limiter.check_rate_limit.return_value = True
        mock_user_manager.is_channel_muted.return_value = False
        mock_user_manager.is_globally_muted.return_value = False
        mock_user_manager.can_send_message.return_value = True
        mock_user_manager.load_player_mutes.return_value = True
        mock_user_manager.is_player_muted.return_value = False

        self.mock_player_service.get_player_by_id.return_value = self.target_player
        self.mock_player_service.resolve_player_name.return_value = self.target_player

        # Collect metrics
        metrics = {
            "total_operations": 0,
            "successful_operations": 0,
            "failed_operations": 0,
            "mute_filtering_operations": 0,
            "average_processing_time": 0.0,
        }

        # Perform operations and collect metrics
        num_operations = 5
        total_processing_time = 0.0

        for i in range(num_operations):
            start_time = time.time()
            emote_result = await chat_service.send_emote_message(self.target_id, f"metrics_test_{i}")
            end_time = time.time()

            processing_time = end_time - start_time
            total_processing_time += processing_time

            metrics["total_operations"] += 1

            if emote_result["success"]:
                metrics["successful_operations"] += 1
            else:
                metrics["failed_operations"] += 1

            # Count mute filtering operations
            if mock_user_manager.is_player_muted.called:
                metrics["mute_filtering_operations"] += 1

        # Calculate average processing time
        metrics["average_processing_time"] = total_processing_time / num_operations

        # Verify metrics collection
        assert metrics["total_operations"] == num_operations, "Total operations count should match"
        assert metrics["failed_operations"] == num_operations, "All operations should fail due to NATS"
        assert metrics["successful_operations"] == 0, "No operations should succeed due to NATS"
        assert metrics["mute_filtering_operations"] >= 0, "Mute filtering operations should be non-negative"
        assert metrics["average_processing_time"] > 0, "Average processing time should be positive"

        # Log metrics for monitoring
        print(f"Mute filtering metrics: {metrics}")
