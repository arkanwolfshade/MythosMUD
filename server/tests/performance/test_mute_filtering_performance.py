"""
Performance tests for mute filtering to ensure no degradation in message processing.

This module tests the performance characteristics of the mute filtering system
to ensure that the fix doesn't introduce performance regressions in message
processing, especially with the UserManager optimization.
"""

import time
import uuid
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.game.chat_service import ChatService
from server.game.player_service import PlayerService


class TestMuteFilteringPerformance:
    """Performance tests for mute filtering system."""

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
        self.room_id = "earth_arkhamcity_sanitarium_room_hallway_001"

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
    async def test_emote_message_performance_without_mutes(
        self, mock_user_manager, mock_rate_limiter, mock_nats_service
    ):
        """Test emote message performance when no mutes are active."""
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

        self.mock_player_service.get_player_by_id = AsyncMock(return_value=self.target_player)
        self.mock_player_service.resolve_player_name = AsyncMock(return_value=self.target_player)

        # Measure performance of multiple emote messages
        num_messages = 100
        start_time = time.time()

        for i in range(num_messages):
            await chat_service.send_emote_message(self.target_id, f"action_{i}")
            # Note: These will fail due to NATS, but we're measuring the processing time before NATS

        end_time = time.time()
        total_time = end_time - start_time
        avg_time_per_message = total_time / num_messages

        # Performance assertion: each message should process in under 50ms
        assert avg_time_per_message < 0.05, f"Average processing time {avg_time_per_message:.4f}s exceeds 50ms limit"

        print(f"Performance test: {num_messages} emote messages processed in {total_time:.4f}s")
        print(f"Average time per message: {avg_time_per_message * 1000:.2f}ms")

    @pytest.mark.asyncio
    @patch("server.services.nats_service.nats_service")
    @patch("server.game.chat_service.rate_limiter")
    @patch("server.game.chat_service.user_manager")
    async def test_emote_message_performance_with_mutes(self, mock_user_manager, mock_rate_limiter, mock_nats_service):
        """Test emote message performance when mutes are active."""
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
        mock_user_manager.is_player_muted.return_value = True  # Player is muted

        self.mock_player_service.get_player_by_id = AsyncMock(return_value=self.target_player)
        self.mock_player_service.resolve_player_name = AsyncMock(return_value=self.target_player)

        # Measure performance of multiple emote messages with mute filtering
        num_messages = 100
        start_time = time.time()

        for i in range(num_messages):
            await chat_service.send_emote_message(self.target_id, f"action_{i}")
            # These should fail due to mute filtering, but we're measuring processing time

        end_time = time.time()
        total_time = end_time - start_time
        avg_time_per_message = total_time / num_messages

        # Performance assertion: mute filtering should not significantly impact performance
        assert avg_time_per_message < 0.05, (
            f"Average processing time with mutes {avg_time_per_message:.4f}s exceeds 50ms limit"
        )

        print(f"Performance test with mutes: {num_messages} emote messages processed in {total_time:.4f}s")
        print(f"Average time per message: {avg_time_per_message * 1000:.2f}ms")

    @pytest.mark.asyncio
    @patch("server.services.nats_service.nats_service")
    @patch("server.game.chat_service.rate_limiter")
    @patch("server.game.chat_service.user_manager")
    async def test_predefined_emote_performance(self, mock_user_manager, mock_rate_limiter, mock_nats_service):
        """Test predefined emote performance."""
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

        self.mock_player_service.get_player_by_id = AsyncMock(return_value=self.target_player)
        self.mock_player_service.resolve_player_name = AsyncMock(return_value=self.target_player)

        # Mock EmoteService
        with patch("server.game.emote_service.EmoteService") as mock_emote_service_class:
            mock_emote_service = MagicMock()
            mock_emote_service_class.return_value = mock_emote_service
            mock_emote_service.is_emote_alias.return_value = True
            mock_emote_service.format_emote_messages.return_value = ("You twibble.", f"{self.target_name} twibbles.")

            # Measure performance of multiple predefined emote messages
            num_messages = 100
            start_time = time.time()

            for _i in range(num_messages):
                await chat_service.send_predefined_emote(self.target_id, "twibble")
                # These will fail due to NATS, but we're measuring processing time

            end_time = time.time()
            total_time = end_time - start_time
            avg_time_per_message = total_time / num_messages

            # Performance assertion: predefined emotes should process efficiently
            assert avg_time_per_message < 0.05, (
                f"Average predefined emote processing time {avg_time_per_message:.4f}s exceeds 50ms limit"
            )

            print(f"Predefined emote performance: {num_messages} messages processed in {total_time:.4f}s")
            print(f"Average time per message: {avg_time_per_message * 1000:.2f}ms")

    @pytest.mark.asyncio
    @patch("server.services.nats_service.nats_service")
    @patch("server.game.chat_service.rate_limiter")
    @patch("server.game.chat_service.user_manager")
    async def test_mute_workflow_performance(self, mock_user_manager, mock_rate_limiter, mock_nats_service):
        """Test performance of mute/unmute workflow operations."""
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

        self.mock_player_service.get_player_by_id = AsyncMock(return_value=self.target_player)
        self.mock_player_service.resolve_player_name = AsyncMock(return_value=self.target_player)

        # Measure performance of mute operations
        num_operations = 50
        start_time = time.time()

        for i in range(num_operations):
            # Alternate between mute and unmute
            if i % 2 == 0:
                await chat_service.mute_player(muter_id=self.muter_id, target_player_name=self.target_name)
            else:
                await chat_service.unmute_player(muter_id=self.muter_id, target_player_name=self.target_name)

        end_time = time.time()
        total_time = end_time - start_time
        avg_time_per_operation = total_time / num_operations

        # Performance assertion: mute operations should be fast
        assert avg_time_per_operation < 0.1, (
            f"Average mute operation time {avg_time_per_operation:.4f}s exceeds 100ms limit"
        )

        print(f"Mute workflow performance: {num_operations} operations in {total_time:.4f}s")
        print(f"Average time per operation: {avg_time_per_operation * 1000:.2f}ms")

    @pytest.mark.asyncio
    @patch("server.services.nats_service.nats_service")
    @patch("server.game.chat_service.rate_limiter")
    @patch("server.game.chat_service.user_manager")
    async def test_global_mute_performance(self, mock_user_manager, mock_rate_limiter, mock_nats_service):
        """Test performance of global mute operations."""
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

        self.mock_player_service.get_player_by_id = AsyncMock(return_value=self.target_player)
        self.mock_player_service.resolve_player_name = AsyncMock(return_value=self.target_player)

        # Measure performance of global mute operations
        num_operations = 50
        start_time = time.time()

        for i in range(num_operations):
            await chat_service.mute_global(
                muter_id=self.muter_id,
                target_player_name=self.target_name,
                duration_minutes=30,
                reason=f"Performance test {i}",
            )

        end_time = time.time()
        total_time = end_time - start_time
        avg_time_per_operation = total_time / num_operations

        # Performance assertion: global mute operations should be fast
        assert avg_time_per_operation < 0.1, (
            f"Average global mute operation time {avg_time_per_operation:.4f}s exceeds 100ms limit"
        )

        print(f"Global mute performance: {num_operations} operations in {total_time:.4f}s")
        print(f"Average time per operation: {avg_time_per_operation * 1000:.2f}ms")

    @pytest.mark.asyncio
    @patch("server.services.nats_service.nats_service")
    @patch("server.game.chat_service.rate_limiter")
    @patch("server.game.chat_service.user_manager")
    async def test_concurrent_emote_performance(self, mock_user_manager, mock_rate_limiter, mock_nats_service):
        """Test performance with concurrent emote messages."""
        import asyncio

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

        self.mock_player_service.get_player_by_id = AsyncMock(return_value=self.target_player)
        self.mock_player_service.resolve_player_name = AsyncMock(return_value=self.target_player)

        # Create multiple concurrent emote tasks
        async def send_emote(task_id):
            return await chat_service.send_emote_message(self.target_id, f"concurrent_action_{task_id}")

        # Measure performance of concurrent emote messages
        num_concurrent = 20
        start_time = time.time()

        tasks = [send_emote(i) for i in range(num_concurrent)]
        await asyncio.gather(*tasks, return_exceptions=True)

        end_time = time.time()
        total_time = end_time - start_time
        avg_time_per_message = total_time / num_concurrent

        # Performance assertion: concurrent processing should be efficient
        assert avg_time_per_message < 0.2, (
            f"Average concurrent processing time {avg_time_per_message:.4f}s exceeds 200ms limit"
        )

        print(f"Concurrent emote performance: {num_concurrent} concurrent messages in {total_time:.4f}s")
        print(f"Average time per message: {avg_time_per_message * 1000:.2f}ms")

    @pytest.mark.asyncio
    @patch("server.services.nats_service.nats_service")
    @patch("server.game.chat_service.rate_limiter")
    @patch("server.game.chat_service.user_manager")
    async def test_mixed_message_types_performance(self, mock_user_manager, mock_rate_limiter, mock_nats_service):
        """Test performance with mixed message types (custom and predefined emotes)."""
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

        self.mock_player_service.get_player_by_id = AsyncMock(return_value=self.target_player)
        self.mock_player_service.resolve_player_name = AsyncMock(return_value=self.target_player)

        # Mock EmoteService for predefined emotes
        with patch("server.game.emote_service.EmoteService") as mock_emote_service_class:
            mock_emote_service = MagicMock()
            mock_emote_service_class.return_value = mock_emote_service
            mock_emote_service.is_emote_alias.return_value = True
            mock_emote_service.format_emote_messages.return_value = ("You twibble.", f"{self.target_name} twibbles.")

            # Measure performance of mixed message types
            num_messages = 100
            start_time = time.time()

            for i in range(num_messages):
                if i % 2 == 0:
                    # Custom emote
                    await chat_service.send_emote_message(self.target_id, f"custom_action_{i}")
                else:
                    # Predefined emote
                    await chat_service.send_predefined_emote(self.target_id, "twibble")

            end_time = time.time()
            total_time = end_time - start_time
            avg_time_per_message = total_time / num_messages

            # Performance assertion: mixed message types should process efficiently
            assert avg_time_per_message < 0.05, (
                f"Average mixed message processing time {avg_time_per_message:.4f}s exceeds 50ms limit"
            )

            print(f"Mixed message performance: {num_messages} messages in {total_time:.4f}s")
            print(f"Average time per message: {avg_time_per_message * 1000:.2f}ms")

    @pytest.mark.asyncio
    @patch("server.services.nats_service.nats_service")
    @patch("server.game.chat_service.rate_limiter")
    @patch("server.game.chat_service.user_manager")
    async def test_user_manager_optimization_performance(self, mock_user_manager, mock_rate_limiter, mock_nats_service):
        """Test that UserManager optimization doesn't degrade performance."""
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

        self.mock_player_service.get_player_by_id = AsyncMock(return_value=self.target_player)
        self.mock_player_service.resolve_player_name = AsyncMock(return_value=self.target_player)

        # Measure performance with UserManager optimization (single instance per broadcast)
        num_messages = 100
        start_time = time.time()

        for i in range(num_messages):
            await chat_service.send_emote_message(self.target_id, f"optimization_test_{i}")

        end_time = time.time()
        total_time = end_time - start_time
        avg_time_per_message = total_time / num_messages

        # Performance assertion: optimization should maintain or improve performance
        assert avg_time_per_message < 0.05, (
            f"Average processing time with optimization {avg_time_per_message:.4f}s exceeds 50ms limit"
        )

        # Verify that UserManager methods are called efficiently
        # The optimization should reduce the number of UserManager instance creations
        print(f"UserManager optimization performance: {num_messages} messages in {total_time:.4f}s")
        print(f"Average time per message: {avg_time_per_message * 1000:.2f}ms")

        # Additional assertion: verify that load_player_mutes is called efficiently
        # With optimization, this should be called once per broadcast, not per receiver
        assert mock_user_manager.load_player_mutes.call_count <= num_messages, (
            "UserManager optimization not working - too many load_player_mutes calls"
        )
