"""
Integration tests for ChatService NATSSubjectManager migration.

This module tests the integration between ChatService and NATSSubjectManager,
ensuring that chat messages use standardized subject patterns instead of
ad-hoc subject construction.

AI: These tests verify the migration from manual subject construction to
AI: centralized pattern management in ChatService.
"""

import uuid
from unittest.mock import AsyncMock, Mock, patch

import pytest

from server.game.chat_service import ChatService
from server.services.nats_subject_manager import NATSSubjectManager

pytestmark = pytest.mark.integration


class TestChatServiceSubjectMigration:
    """Test ChatService integration with NATSSubjectManager."""

    mock_persistence: Mock
    mock_room_service: Mock
    mock_player_service: AsyncMock
    mock_nats_service: Mock
    mock_chat_logger: Mock
    mock_rate_limiter: Mock
    mock_user_manager: Mock
    subject_manager: NATSSubjectManager
    chat_service: ChatService
    test_player_id: str
    test_player_name: str
    test_room_id: str
    test_subzone: str

    def setup_method(self) -> None:
        """Set up test fixtures with NATSSubjectManager integration."""
        # Create mock dependencies
        self.mock_persistence = Mock()
        self.mock_room_service = Mock()
        self.mock_player_service = AsyncMock()

        # Create mock NATS service
        self.mock_nats_service = Mock()
        self.mock_nats_service.is_connected.return_value = True
        self.mock_nats_service.publish = AsyncMock(return_value=True)

        # Create mock services
        self.mock_chat_logger = Mock()
        self.mock_rate_limiter = Mock()
        self.mock_user_manager = Mock()

        # Mock user manager to allow all operations
        self.mock_user_manager.is_channel_muted.return_value = False
        self.mock_user_manager.is_globally_muted.return_value = False
        self.mock_user_manager.can_send_message.return_value = True
        self.mock_user_manager.is_admin.return_value = False
        self.mock_user_manager.load_player_mutes.return_value = None

        # Create NATSSubjectManager instance for testing
        self.subject_manager = NATSSubjectManager()

        # Create the service instance with NATSSubjectManager injection
        self.chat_service = ChatService(
            self.mock_persistence,
            self.mock_room_service,
            self.mock_player_service,
            nats_service=self.mock_nats_service,
            user_manager_instance=self.mock_user_manager,
        )

        # Replace remaining service dependencies with mocks
        self.chat_service.chat_logger = self.mock_chat_logger
        self.chat_service.rate_limiter = self.mock_rate_limiter

        # Inject NATSSubjectManager into ChatService
        self.chat_service.subject_manager = self.subject_manager

        # Create test data
        self.test_player_id = str(uuid.uuid4())
        self.test_player_name = "TestPlayer"
        self.test_room_id = "arkham_1"
        self.test_subzone = "arkham"

    @pytest.mark.asyncio
    async def test_say_message_uses_standardized_subject_pattern(self) -> None:
        """Test that say messages use the chat_say_room pattern."""
        message_content = "Hello, Arkham!"

        # Mock room service to return room info
        self.mock_room_service.get_room.return_value = {"id": self.test_room_id, "name": "Arkham Library"}

        # Mock player service to return player info
        mock_player = Mock()
        mock_player.id = self.test_player_id
        mock_player.name = self.test_player_name
        mock_player.current_room_id = self.test_room_id
        mock_player.level = 1  # Ensure player has level 1+ for global messages

        self.mock_player_service.get_player_by_id.return_value = mock_player

        # Send say message
        await self.chat_service.send_say_message(self.test_player_id, message_content)

        # Verify NATS publish was called
        assert self.mock_nats_service.publish.called

        # Get the subject used for publishing
        call_args = self.mock_nats_service.publish.call_args
        published_subject = call_args[0][0]  # First argument is subject

        # Verify subject follows standardized pattern
        assert published_subject == f"chat.say.room.{self.test_room_id}"

        # Verify subject is valid according to our manager
        assert self.subject_manager.validate_subject(published_subject)

    @pytest.mark.asyncio
    async def test_local_message_uses_standardized_subject_pattern(self) -> None:
        """Test that local messages use the chat_local_subzone pattern."""
        message_content = "Anyone here?"

        # Mock room service to return room info
        self.mock_room_service.get_room.return_value = {"id": self.test_room_id, "name": "Arkham Library"}

        # Mock player service to return player info
        mock_player = Mock()
        mock_player.id = self.test_player_id
        mock_player.name = self.test_player_name
        mock_player.current_room_id = self.test_room_id
        mock_player.level = 1  # Ensure player has level 1+ for global messages

        self.mock_player_service.get_player_by_id.return_value = mock_player

        # Mock subzone extraction
        with patch("server.utils.room_utils.extract_subzone_from_room_id", return_value=self.test_subzone):
            # Send local message
            await self.chat_service.send_local_message(self.test_player_id, message_content)

            # Verify NATS publish was called
            assert self.mock_nats_service.publish.called

            # Get the subject used for publishing
            call_args = self.mock_nats_service.publish.call_args
            published_subject = call_args[0][0]

            # Verify subject follows standardized pattern
            assert published_subject == f"chat.local.subzone.{self.test_subzone}"

            # Verify subject is valid according to our manager
            assert self.subject_manager.validate_subject(published_subject)

    @pytest.mark.asyncio
    async def test_global_message_uses_standardized_subject_pattern(self) -> None:
        """Test that global messages use the chat_global pattern."""
        message_content = "Hello, everyone!"

        # Mock room service to return room info
        self.mock_room_service.get_room.return_value = {"id": self.test_room_id, "name": "Arkham Library"}

        # Mock player service to return player info
        mock_player = Mock()
        mock_player.id = self.test_player_id
        mock_player.name = self.test_player_name
        mock_player.current_room_id = self.test_room_id
        mock_player.level = 1  # Ensure player has level 1+ for global messages

        self.mock_player_service.get_player_by_id.return_value = mock_player

        # Send global message
        await self.chat_service.send_global_message(self.test_player_id, message_content)

        # Verify NATS publish was called
        assert self.mock_nats_service.publish.called

        # Get the subject used for publishing
        call_args = self.mock_nats_service.publish.call_args
        published_subject = call_args[0][0]

        # Verify subject follows standardized pattern
        assert published_subject == "chat.global"

        # Verify subject is valid according to our manager
        assert self.subject_manager.validate_subject(published_subject)

    @pytest.mark.asyncio
    async def test_whisper_message_uses_standardized_subject_pattern(self) -> None:
        """Test that whisper messages use the chat_whisper_player pattern."""
        target_player_id = str(uuid.uuid4())
        target_player_name = "TargetPlayer"
        message_content = "Psst, secret message!"

        # Mock room service to return room info
        self.mock_room_service.get_room.return_value = {"id": self.test_room_id, "name": "Arkham Library"}

        # Mock player service to return player info
        mock_player = Mock()
        mock_player.id = self.test_player_id
        mock_player.name = self.test_player_name
        mock_player.current_room_id = self.test_room_id
        mock_player.level = 1  # Ensure player has level 1+ for global messages

        self.mock_player_service.get_player_by_id.return_value = mock_player

        # Mock target player lookup
        self.mock_player_service.get_player_by_name.return_value = {
            "id": target_player_id,
            "name": target_player_name,
            "room_id": self.test_room_id,
        }

        # Send whisper message
        await self.chat_service.send_whisper_message(self.test_player_id, target_player_id, message_content)

        # Verify NATS publish was called
        assert self.mock_nats_service.publish.called

        # Get the subject used for publishing
        call_args = self.mock_nats_service.publish.call_args
        published_subject = call_args[0][0]

        # Verify subject follows standardized pattern
        assert published_subject == f"chat.whisper.player.{target_player_id}"

        # Verify subject is valid according to our manager
        assert self.subject_manager.validate_subject(published_subject)

    @pytest.mark.asyncio
    async def test_emote_message_uses_standardized_subject_pattern(self) -> None:
        """Test that emote messages use the chat_emote_room pattern."""
        emote_command = "twibble"

        # Mock room service to return room info
        self.mock_room_service.get_room.return_value = {"id": self.test_room_id, "name": "Arkham Library"}

        # Mock player service to return player info
        mock_player = Mock()
        mock_player.id = self.test_player_id
        mock_player.name = self.test_player_name
        mock_player.current_room_id = self.test_room_id
        mock_player.level = 1  # Ensure player has level 1+ for global messages

        self.mock_player_service.get_player_by_id.return_value = mock_player

        # Mock EmoteService to avoid database dependency in test environment
        with patch("server.game.emote_service.EmoteService") as mock_emote_service_class:
            mock_emote_service = Mock()
            mock_emote_service_class.return_value = mock_emote_service
            mock_emote_service.is_emote_alias.return_value = True
            mock_emote_service.format_emote_messages.return_value = (
                "You twibble.",
                f"{self.test_player_name} twibbles.",
            )

            # Send emote message
            await self.chat_service.send_predefined_emote(self.test_player_id, emote_command)

        # Verify NATS publish was called
        assert self.mock_nats_service.publish.called

        # Get the subject used for publishing
        call_args = self.mock_nats_service.publish.call_args
        published_subject = call_args[0][0]

        # Verify subject follows standardized pattern
        assert published_subject == f"chat.emote.room.{self.test_room_id}"

        # Verify subject is valid according to our manager
        assert self.subject_manager.validate_subject(published_subject)

    @pytest.mark.asyncio
    async def test_pose_message_uses_standardized_subject_pattern(self) -> None:
        """Test that pose messages use the chat_pose_room pattern."""
        pose_content = "adjusts spectacles thoughtfully"

        # Mock room service to return room info
        self.mock_room_service.get_room.return_value = {"id": self.test_room_id, "name": "Arkham Library"}

        # Mock player service to return player info
        mock_player = Mock()
        mock_player.id = self.test_player_id
        mock_player.name = self.test_player_name
        mock_player.current_room_id = self.test_room_id
        mock_player.level = 1  # Ensure player has level 1+ for global messages

        self.mock_player_service.get_player_by_id.return_value = mock_player

        # Send pose message
        await self.chat_service.set_player_pose(self.test_player_id, pose_content)

        # Verify NATS publish was called
        assert self.mock_nats_service.publish.called

        # Get the subject used for publishing
        call_args = self.mock_nats_service.publish.call_args
        published_subject = call_args[0][0]

        # Verify subject follows standardized pattern
        assert published_subject == f"chat.pose.room.{self.test_room_id}"

        # Verify subject is valid according to our manager
        assert self.subject_manager.validate_subject(published_subject)

    @pytest.mark.asyncio
    async def test_system_message_uses_standardized_subject_pattern(self) -> None:
        """Test that system messages use the chat_system pattern."""
        message_content = "System maintenance in 5 minutes"

        # Mock room service to return room info
        self.mock_room_service.get_room.return_value = {"id": self.test_room_id, "name": "Arkham Library"}

        # Mock player service to return player info
        mock_player = Mock()
        mock_player.id = self.test_player_id
        mock_player.name = self.test_player_name
        mock_player.current_room_id = self.test_room_id
        mock_player.level = 1  # Ensure player has level 1+ for global messages

        self.mock_player_service.get_player_by_id.return_value = mock_player

        # Mock user manager to allow admin operations for system message
        self.mock_user_manager.is_admin.return_value = True
        await self.chat_service.send_system_message(self.test_player_id, message_content)

        # Verify NATS publish was called
        assert self.mock_nats_service.publish.called

        # Get the subject used for publishing
        call_args = self.mock_nats_service.publish.call_args
        published_subject = call_args[0][0]

        # Verify subject follows standardized pattern
        assert published_subject == "chat.system"

        # Verify subject is valid according to our manager
        assert self.subject_manager.validate_subject(published_subject)

    @pytest.mark.asyncio
    async def test_subject_manager_integration_without_injection(self) -> None:
        """Test that ChatService works without NATSSubjectManager injection (backward compatibility)."""
        # Create ChatService without subject manager injection
        chat_service_no_manager = ChatService(
            self.mock_persistence,
            self.mock_room_service,
            self.mock_player_service,
            nats_service=self.mock_nats_service,
            user_manager_instance=self.mock_user_manager,
        )

        # Replace service dependencies
        chat_service_no_manager.chat_logger = self.mock_chat_logger
        chat_service_no_manager.rate_limiter = self.mock_rate_limiter

        # Mock room service to return room info
        self.mock_room_service.get_room.return_value = {"id": self.test_room_id, "name": "Arkham Library"}

        # Mock player service to return player info
        mock_player = Mock()
        mock_player.id = self.test_player_id
        mock_player.name = self.test_player_name
        mock_player.current_room_id = self.test_room_id
        mock_player.level = 1  # Ensure player has level 1+ for global messages

        self.mock_player_service.get_player_by_id.return_value = mock_player

        # Send say message (should still work with old subject construction)
        await chat_service_no_manager.send_say_message(self.test_player_id, "Hello!")

        # Verify NATS publish was called
        assert self.mock_nats_service.publish.called

        # Get the subject used for publishing
        call_args = self.mock_nats_service.publish.call_args
        published_subject = call_args[0][0]

        # Should still use old pattern format
        assert published_subject == f"chat.say.{self.test_room_id}"

    @pytest.mark.asyncio
    async def test_subject_validation_failure_handling(self) -> None:
        """Test that invalid subjects are handled gracefully."""
        # Create a subject manager with strict validation
        strict_manager = NATSSubjectManager(strict_validation=True)

        # Inject strict manager
        self.chat_service.subject_manager = strict_manager

        # Mock room service to return room info with invalid characters
        invalid_room_id = "room@invalid"
        self.mock_room_service.get_room.return_value = {"id": invalid_room_id, "name": "Invalid Room"}

        # Mock player service to return player info
        mock_player = Mock()
        mock_player.id = self.test_player_id
        mock_player.name = self.test_player_name
        mock_player.current_room_id = invalid_room_id
        mock_player.level = 1

        self.mock_player_service.get_player_by_id.return_value = mock_player

        # Send say message with invalid room ID
        await self.chat_service.send_say_message(self.test_player_id, "Hello!")

        # Should handle validation failure gracefully
        # Either fall back to old pattern or handle error appropriately
        assert self.mock_nats_service.publish.called

    @pytest.mark.asyncio
    async def test_message_data_structure_consistency(self) -> None:
        """Test that message data structure remains consistent with subject manager integration."""
        message_content = "Test message"

        # Mock room service to return room info
        self.mock_room_service.get_room.return_value = {"id": self.test_room_id, "name": "Arkham Library"}

        # Mock player service to return player info
        mock_player = Mock()
        mock_player.id = self.test_player_id
        mock_player.name = self.test_player_name
        mock_player.current_room_id = self.test_room_id
        mock_player.level = 1  # Ensure player has level 1+ for global messages

        self.mock_player_service.get_player_by_id.return_value = mock_player

        # Send say message
        await self.chat_service.send_say_message(self.test_player_id, message_content)

        # Verify NATS publish was called
        assert self.mock_nats_service.publish.called

        # Get the message data
        call_args = self.mock_nats_service.publish.call_args
        message_data = call_args[0][1]  # Second argument is data

        # Verify message data structure
        assert "message_id" in message_data
        assert "sender_id" in message_data
        assert "sender_name" in message_data
        assert "channel" in message_data
        assert "content" in message_data
        assert "timestamp" in message_data
        assert "room_id" in message_data

        # Verify values
        assert message_data["sender_id"] == self.test_player_id
        assert message_data["sender_name"] == self.test_player_name
        assert message_data["content"] == message_content
        assert message_data["room_id"] == self.test_room_id

    @pytest.mark.asyncio
    async def test_performance_with_subject_manager(self) -> None:
        """Test that subject manager integration doesn't significantly impact performance."""
        import time

        # Mock room service to return room info
        self.mock_room_service.get_room.return_value = {"id": self.test_room_id, "name": "Arkham Library"}

        # Mock player service to return player info
        mock_player = Mock()
        mock_player.id = self.test_player_id
        mock_player.name = self.test_player_name
        mock_player.current_room_id = self.test_room_id
        mock_player.level = 1  # Ensure player has level 1+ for global messages

        self.mock_player_service.get_player_by_id.return_value = mock_player

        # Measure time for multiple messages
        start_time = time.time()
        for i in range(100):
            await self.chat_service.send_say_message(self.test_player_id, f"Message {i}")
        elapsed_time = time.time() - start_time

        # Should complete 100 messages in reasonable time (less than 2 seconds to account for system variability)
        assert elapsed_time < 2.0

        # Verify all messages were published
        assert self.mock_nats_service.publish.call_count == 100


class TestChatServiceSubjectManagerDependencyInjection:
    """Test NATSSubjectManager dependency injection patterns."""

    def test_chat_service_accepts_subject_manager_injection(self) -> None:
        """Test that ChatService can accept NATSSubjectManager via dependency injection."""
        # Create mock dependencies
        mock_persistence = Mock()
        mock_room_service = Mock()
        mock_player_service = AsyncMock()
        mock_nats_service = Mock()
        mock_user_manager = Mock()

        # Create subject manager
        subject_manager = NATSSubjectManager()

        # Create ChatService with subject manager injection
        chat_service = ChatService(
            mock_persistence,
            mock_room_service,
            mock_player_service,
            nats_service=mock_nats_service,
            user_manager_instance=mock_user_manager,
        )

        # Inject subject manager
        chat_service.subject_manager = subject_manager

        # Verify injection worked
        assert chat_service.subject_manager is subject_manager

    def test_chat_service_works_without_subject_manager(self) -> None:
        """Test that ChatService works without subject manager (backward compatibility)."""
        # Create mock dependencies
        mock_persistence = Mock()
        mock_room_service = Mock()
        mock_player_service = AsyncMock()
        mock_nats_service = Mock()
        mock_user_manager = Mock()

        # Create ChatService without subject manager
        chat_service = ChatService(
            mock_persistence,
            mock_room_service,
            mock_player_service,
            nats_service=mock_nats_service,
            user_manager_instance=mock_user_manager,
        )

        # Should not have subject manager initially
        assert not hasattr(chat_service, "subject_manager") or chat_service.subject_manager is None

    def test_subject_manager_can_be_set_after_creation(self) -> None:
        """Test that subject manager can be set after ChatService creation."""
        # Create mock dependencies
        mock_persistence = Mock()
        mock_room_service = Mock()
        mock_player_service = AsyncMock()
        mock_nats_service = Mock()
        mock_user_manager = Mock()

        # Create ChatService
        chat_service = ChatService(
            mock_persistence,
            mock_room_service,
            mock_player_service,
            nats_service=mock_nats_service,
            user_manager_instance=mock_user_manager,
        )

        # Create and inject subject manager
        subject_manager = NATSSubjectManager()
        chat_service.subject_manager = subject_manager

        # Verify injection worked
        assert chat_service.subject_manager is subject_manager

    def test_subject_manager_can_be_replaced(self) -> None:
        """Test that subject manager can be replaced with different configuration."""
        # Create mock dependencies
        mock_persistence = Mock()
        mock_room_service = Mock()
        mock_player_service = AsyncMock()
        mock_nats_service = Mock()
        mock_user_manager = Mock()

        # Create ChatService
        chat_service = ChatService(
            mock_persistence,
            mock_room_service,
            mock_player_service,
            nats_service=mock_nats_service,
            user_manager_instance=mock_user_manager,
        )

        # Inject first subject manager
        manager1 = NATSSubjectManager(strict_validation=False)
        chat_service.subject_manager = manager1
        assert chat_service.subject_manager is manager1

        # Replace with different configuration
        manager2 = NATSSubjectManager(strict_validation=True)
        chat_service.subject_manager = manager2
        assert chat_service.subject_manager is manager2
        assert chat_service.subject_manager is not manager1
