"""
Tests for combat messaging integration with real-time messaging system.

These tests verify that combat messages are properly integrated with the
existing real-time messaging infrastructure for room broadcasting.
"""

from unittest.mock import AsyncMock, patch

import pytest

from server.services.combat_messaging_integration import (
    CombatMessagingIntegration,
)


class TestCombatMessagingIntegration:
    """Test cases for CombatMessagingIntegration."""

    mock_connection_manager: AsyncMock
    integration: CombatMessagingIntegration
    room_id: str
    combat_id: str
    attacker_id: str
    attacker_name: str
    target_name: str
    damage: int
    action_type: str
    xp_reward: int

    def setup_method(self) -> None:
        """Set up test fixtures."""
        # AI Agent: Inject mock connection_manager via constructor (no longer a global)
        #           Post-migration: CombatMessagingIntegration requires connection_manager
        # Use MagicMock as base to prevent automatic AsyncMock creation for all attributes
        # Only specific async methods will be AsyncMock instances
        from unittest.mock import MagicMock

        self.mock_connection_manager = MagicMock()
        self.integration = CombatMessagingIntegration(connection_manager=self.mock_connection_manager)
        self.room_id = "test_room_001"
        self.combat_id = "combat_123"
        self.attacker_id = "player_001"
        self.attacker_name = "TestPlayer"
        self.target_name = "TestNPC"
        self.damage = 1
        self.action_type = "punch"
        self.xp_reward = 5

    @pytest.mark.asyncio
    async def test_broadcast_combat_start(self) -> None:
        """Test broadcasting combat start messages."""
        # AI Agent: Use mock from setup_method (injected via constructor)
        self.mock_connection_manager.broadcast_to_room = AsyncMock(return_value={"successful_deliveries": 2})

        result = await self.integration.broadcast_combat_start(
            room_id=self.room_id,
            attacker_name=self.attacker_name,
            target_name=self.target_name,
            combat_id=self.combat_id,
        )

        # Verify broadcast was called with correct parameters
        self.mock_connection_manager.broadcast_to_room.assert_called_once()
        call_args = self.mock_connection_manager.broadcast_to_room.call_args
        assert call_args[0][0] == self.room_id  # room_id
        event = call_args[0][1]  # event
        assert event["event_type"] == "combat_started"
        assert event["data"]["combat_id"] == self.combat_id
        assert event["data"]["attacker_name"] == self.attacker_name
        assert event["data"]["target_name"] == self.target_name
        assert "messages" in event["data"]

        assert result == {"successful_deliveries": 2}

    @pytest.mark.asyncio
    async def test_broadcast_combat_attack(self) -> None:
        """Test broadcasting combat attack messages."""
        # AI Agent: Use mock from setup_method (injected via constructor)
        self.mock_connection_manager.broadcast_to_room = AsyncMock(return_value={"successful_deliveries": 2})
        self.mock_connection_manager.send_personal_message = AsyncMock(return_value={"success": True})

        result = await self.integration.broadcast_combat_attack(
            room_id=self.room_id,
            attacker_name=self.attacker_name,
            target_name=self.target_name,
            damage=self.damage,
            action_type=self.action_type,
            combat_id=self.combat_id,
            attacker_id=self.attacker_id,
        )

        # Verify broadcast was called with correct parameters
        self.mock_connection_manager.broadcast_to_room.assert_called_once()
        call_args = self.mock_connection_manager.broadcast_to_room.call_args
        assert call_args[0][0] == self.room_id  # room_id
        assert call_args[1]["exclude_player"] == self.attacker_id  # exclude_player
        event = call_args[0][1]  # event
        assert event["event_type"] == "combat_attack"
        assert event["data"]["combat_id"] == self.combat_id
        assert event["data"]["attacker_name"] == self.attacker_name
        assert event["data"]["target_name"] == self.target_name
        assert event["data"]["damage"] == self.damage
        assert event["data"]["action_type"] == self.action_type

        # Verify personal message was sent to attacker
        self.mock_connection_manager.send_personal_message.assert_called_once()
        personal_call_args = self.mock_connection_manager.send_personal_message.call_args
        assert personal_call_args[0][0] == self.attacker_id
        personal_event = personal_call_args[0][1]
        assert personal_event["event_type"] == "combat_attack_personal"

        assert result == {"successful_deliveries": 2}

    @pytest.mark.asyncio
    async def test_broadcast_combat_death(self) -> None:
        """Test broadcasting combat death messages."""
        # AI Agent: Use mock from setup_method (injected via constructor)
        self.mock_connection_manager.broadcast_to_room = AsyncMock(return_value={"successful_deliveries": 2})

        result = await self.integration.broadcast_combat_death(
            room_id=self.room_id,
            npc_name=self.target_name,
            xp_reward=self.xp_reward,
            combat_id=self.combat_id,
        )

        # Verify broadcast was called with correct parameters
        self.mock_connection_manager.broadcast_to_room.assert_called_once()
        call_args = self.mock_connection_manager.broadcast_to_room.call_args
        assert call_args[0][0] == self.room_id  # room_id
        event = call_args[0][1]  # event
        assert event["event_type"] == "combat_death"
        assert event["data"]["combat_id"] == self.combat_id
        assert event["data"]["npc_name"] == self.target_name
        assert event["data"]["xp_reward"] == self.xp_reward
        assert "messages" in event["data"]

        assert result == {"successful_deliveries": 2}

    @pytest.mark.asyncio
    async def test_broadcast_combat_end(self) -> None:
        """Test broadcasting combat end messages."""
        # AI Agent: Use mock from setup_method (injected via constructor)
        self.mock_connection_manager.broadcast_to_room = AsyncMock(return_value={"successful_deliveries": 2})

        result = await self.integration.broadcast_combat_end(
            room_id=self.room_id,
            combat_id=self.combat_id,
            reason="npc_died",
        )

        # Verify broadcast was called with correct parameters
        self.mock_connection_manager.broadcast_to_room.assert_called_once()
        call_args = self.mock_connection_manager.broadcast_to_room.call_args
        assert call_args[0][0] == self.room_id  # room_id
        event = call_args[0][1]  # event
        assert event["event_type"] == "combat_ended"
        assert event["data"]["combat_id"] == self.combat_id
        assert event["data"]["reason"] == "npc_died"
        assert "messages" in event["data"]

        assert result == {"successful_deliveries": 2}

    @pytest.mark.asyncio
    async def test_broadcast_combat_error(self) -> None:
        """Test broadcasting combat error messages."""
        error_message = "You can't attack that target."

        # AI Agent: Use mock from setup_method (injected via constructor)
        self.mock_connection_manager.send_personal_message = AsyncMock(return_value={"success": True})

        result = await self.integration.broadcast_combat_error(
            room_id=self.room_id,
            error_message=error_message,
            player_id=self.attacker_id,
        )

        # Verify personal message was sent with correct parameters
        self.mock_connection_manager.send_personal_message.assert_called_once()
        call_args = self.mock_connection_manager.send_personal_message.call_args
        assert call_args[0][0] == self.attacker_id
        event = call_args[0][1]
        assert event["event_type"] == "combat_error"
        assert event["data"]["error_message"] == error_message

        assert result == {"success": True}

    @pytest.mark.asyncio
    async def test_broadcast_combat_attack_no_personal_message(self) -> None:
        """Test that attack broadcast works even if personal message fails."""
        # AI Agent: Use mock from setup_method (injected via constructor)
        self.mock_connection_manager.broadcast_to_room = AsyncMock(return_value={"successful_deliveries": 2})
        self.mock_connection_manager.send_personal_message = AsyncMock(side_effect=RuntimeError("NATS error"))

        # Should not raise exception even if personal message fails
        result = await self.integration.broadcast_combat_attack(
            room_id=self.room_id,
            attacker_name=self.attacker_name,
            target_name=self.target_name,
            damage=self.damage,
            action_type=self.action_type,
            combat_id=self.combat_id,
            attacker_id=self.attacker_id,
        )

        # Verify broadcast still succeeded
        self.mock_connection_manager.broadcast_to_room.assert_called_once()
        assert result == {"successful_deliveries": 2}

    @pytest.mark.asyncio
    async def test_broadcast_combat_start_with_messaging_service_error(self) -> None:
        """Test that combat start works even if messaging service fails."""
        # AI Agent: Use mock from setup_method (injected via constructor)
        self.mock_connection_manager.broadcast_to_room = AsyncMock(return_value={"successful_deliveries": 2})

        # Mock messaging service to raise an exception
        with patch.object(
            self.integration.messaging_service,
            "get_combat_start_messages",
            side_effect=Exception("Messaging error"),
        ):
            # Should not raise exception, should use fallback messages
            result = await self.integration.broadcast_combat_start(
                room_id=self.room_id,
                attacker_name=self.attacker_name,
                target_name=self.target_name,
                combat_id=self.combat_id,
            )

            # Verify broadcast still succeeded
            self.mock_connection_manager.broadcast_to_room.assert_called_once()
            assert result == {"successful_deliveries": 2}
