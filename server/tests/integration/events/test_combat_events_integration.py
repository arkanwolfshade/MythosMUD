"""
Tests for combat event integration with NATS.

This module tests the integration of combat events with the NATS
messaging system for real-time distribution.
"""

from unittest.mock import AsyncMock, Mock
from uuid import uuid4

import pytest

from server.events.combat_events import (
    CombatEndedEvent,
    CombatStartedEvent,
    CombatTimeoutEvent,
    CombatTurnAdvancedEvent,
    NPCAttackedEvent,
    NPCDiedEvent,
    NPCTookDamageEvent,
    PlayerAttackedEvent,
)
from server.events.event_types import NPCAttacked, NPCDied, NPCTookDamage
from server.services.combat_event_publisher import CombatEventPublisher


class TestCombatEventPublisher:
    """Test combat event publisher integration with NATS."""

    def setup_method(self):
        """Set up test fixtures."""
        # Create mock NATS service
        self.mock_nats_service = Mock()
        self.mock_nats_service.is_connected.return_value = True
        self.mock_nats_service.publish = AsyncMock(return_value=True)

        # Create combat event publisher with mock NATS service
        self.publisher = CombatEventPublisher(nats_service=self.mock_nats_service)

        # Test data
        self.test_combat_id = uuid4()
        self.test_room_id = "test_room_001"
        self.test_player_id = uuid4()
        self.test_npc_id = uuid4()

    @pytest.mark.asyncio
    async def test_publish_combat_started_success(self):
        """Test successful combat started event publishing."""
        # Create combat started event
        event = CombatStartedEvent(
            combat_id=self.test_combat_id,
            room_id=self.test_room_id,
            participants={"player1": {"id": str(self.test_player_id), "name": "TestPlayer"}},
            turn_order=["player1"],
        )

        # Execute
        result = await self.publisher.publish_combat_started(event)

        # Verify
        assert result is True
        self.mock_nats_service.publish.assert_called_once()

        # Verify the published data
        call_args = self.mock_nats_service.publish.call_args
        subject = call_args[0][0]
        message_data = call_args[0][1]

        assert subject == f"combat.started.{self.test_room_id}"
        assert message_data["event_type"] == "combat_started"
        assert message_data["data"]["combat_id"] == str(self.test_combat_id)
        assert message_data["data"]["room_id"] == self.test_room_id
        assert message_data["data"]["participants"] == {
            "player1": {"id": str(self.test_player_id), "name": "TestPlayer"}
        }
        assert message_data["data"]["turn_order"] == ["player1"]

    @pytest.mark.asyncio
    async def test_publish_combat_ended_success(self):
        """Test successful combat ended event publishing."""
        # Create combat ended event
        event = CombatEndedEvent(
            combat_id=self.test_combat_id,
            room_id=self.test_room_id,
            reason="npc_died",
            duration_seconds=30,
            participants={"player1": {"id": str(self.test_player_id), "name": "TestPlayer"}},
        )

        # Execute
        result = await self.publisher.publish_combat_ended(event)

        # Verify
        assert result is True
        self.mock_nats_service.publish.assert_called_once()

        # Verify the published data
        call_args = self.mock_nats_service.publish.call_args
        subject = call_args[0][0]
        message_data = call_args[0][1]

        assert subject == f"combat.ended.{self.test_room_id}"
        assert message_data["event_type"] == "combat_ended"
        assert message_data["data"]["combat_id"] == str(self.test_combat_id)
        assert message_data["data"]["room_id"] == self.test_room_id
        assert message_data["data"]["reason"] == "npc_died"
        assert message_data["data"]["duration_seconds"] == 30

    @pytest.mark.asyncio
    async def test_publish_player_attacked_success(self):
        """Test successful player attacked event publishing."""
        # Create player attacked event
        event = PlayerAttackedEvent(
            combat_id=self.test_combat_id,
            room_id=self.test_room_id,
            attacker_id=self.test_player_id,
            attacker_name="TestPlayer",
            target_id=self.test_npc_id,
            target_name="TestNPC",
            damage=5,
            action_type="punch",
            target_current_hp=45,
            target_max_hp=50,
        )

        # Execute
        result = await self.publisher.publish_player_attacked(event)

        # Verify
        assert result is True
        self.mock_nats_service.publish.assert_called_once()

        # Verify the published data
        call_args = self.mock_nats_service.publish.call_args
        subject = call_args[0][0]
        message_data = call_args[0][1]

        assert subject == f"combat.attack.{event.room_id}"
        assert message_data["event_type"] == "player_attacked"
        assert message_data["data"]["combat_id"] == str(self.test_combat_id)
        assert message_data["data"]["attacker_id"] == str(self.test_player_id)
        assert message_data["data"]["attacker_name"] == "TestPlayer"
        assert message_data["data"]["target_id"] == str(self.test_npc_id)
        assert message_data["data"]["target_name"] == "TestNPC"
        assert message_data["data"]["damage"] == 5
        assert message_data["data"]["action_type"] == "punch"

    @pytest.mark.asyncio
    async def test_publish_npc_attacked_success(self):
        """Test successful NPC attacked event publishing."""
        # Create NPC attacked event
        event = NPCAttackedEvent(
            combat_id=self.test_combat_id,
            room_id=self.test_room_id,
            attacker_id=self.test_player_id,
            attacker_name="TestPlayer",
            npc_id=self.test_npc_id,
            npc_name="TestNPC",
            damage=3,
            action_type="kick",
            target_current_hp=47,
            target_max_hp=50,
        )

        # Execute
        result = await self.publisher.publish_npc_attacked(event)

        # Verify
        assert result is True
        self.mock_nats_service.publish.assert_called_once()

        # Verify the published data
        call_args = self.mock_nats_service.publish.call_args
        subject = call_args[0][0]
        message_data = call_args[0][1]

        assert subject == f"combat.npc_attacked.{event.room_id}"
        assert message_data["event_type"] == "npc_attacked"
        assert message_data["data"]["combat_id"] == str(self.test_combat_id)
        assert message_data["data"]["attacker_id"] == str(self.test_player_id)
        assert message_data["data"]["attacker_name"] == "TestPlayer"
        assert message_data["data"]["npc_id"] == str(self.test_npc_id)
        assert message_data["data"]["npc_name"] == "TestNPC"
        assert message_data["data"]["damage"] == 3
        assert message_data["data"]["action_type"] == "kick"

    @pytest.mark.asyncio
    async def test_publish_npc_took_damage_success(self):
        """Test successful NPC took damage event publishing."""
        # Create NPC took damage event
        event = NPCTookDamageEvent(
            combat_id=self.test_combat_id,
            room_id=self.test_room_id,
            npc_id=self.test_npc_id,
            npc_name="TestNPC",
            damage=5,
            current_hp=10,
            max_hp=15,
        )

        # Execute
        result = await self.publisher.publish_npc_took_damage(event)

        # Verify
        assert result is True
        self.mock_nats_service.publish.assert_called_once()

        # Verify the published data
        call_args = self.mock_nats_service.publish.call_args
        subject = call_args[0][0]
        message_data = call_args[0][1]

        assert subject == f"combat.damage.{event.room_id}"
        assert message_data["event_type"] == "npc_took_damage"
        assert message_data["data"]["combat_id"] == str(self.test_combat_id)
        assert message_data["data"]["npc_id"] == str(self.test_npc_id)
        assert message_data["data"]["npc_name"] == "TestNPC"
        assert message_data["data"]["damage"] == 5
        assert message_data["data"]["current_hp"] == 10
        assert message_data["data"]["max_hp"] == 15

    @pytest.mark.asyncio
    async def test_publish_npc_died_success(self):
        """Test successful NPC died event publishing."""
        # Create NPC died event
        event = NPCDiedEvent(
            combat_id=self.test_combat_id,
            room_id=self.test_room_id,
            npc_id=self.test_npc_id,
            npc_name="TestNPC",
            xp_reward=10,
        )

        # Execute
        result = await self.publisher.publish_npc_died(event)

        # Verify
        assert result is True
        self.mock_nats_service.publish.assert_called_once()

        # Verify the published data
        call_args = self.mock_nats_service.publish.call_args
        subject = call_args[0][0]
        message_data = call_args[0][1]

        assert subject == f"combat.npc_died.{event.room_id}"
        assert message_data["event_type"] == "npc_died"
        assert message_data["data"]["combat_id"] == str(self.test_combat_id)
        assert message_data["data"]["npc_id"] == str(self.test_npc_id)
        assert message_data["data"]["npc_name"] == "TestNPC"
        assert message_data["data"]["xp_reward"] == 10

    @pytest.mark.asyncio
    async def test_publish_combat_turn_advanced_success(self):
        """Test successful combat turn advanced event publishing."""
        # Create combat turn advanced event
        event = CombatTurnAdvancedEvent(
            combat_id=self.test_combat_id,
            room_id=self.test_room_id,
            current_turn=2,
            combat_round=1,
            next_participant="player1",
        )

        # Execute
        result = await self.publisher.publish_combat_turn_advanced(event)

        # Verify
        assert result is True
        self.mock_nats_service.publish.assert_called_once()

        # Verify the published data
        call_args = self.mock_nats_service.publish.call_args
        subject = call_args[0][0]
        message_data = call_args[0][1]

        assert subject == f"combat.turn.{self.test_room_id}"
        assert message_data["event_type"] == "combat_turn_advanced"
        assert message_data["data"]["combat_id"] == str(self.test_combat_id)
        assert message_data["data"]["room_id"] == self.test_room_id
        assert message_data["data"]["current_turn"] == 2
        assert message_data["data"]["combat_round"] == 1
        assert message_data["data"]["next_participant"] == "player1"

    @pytest.mark.asyncio
    async def test_publish_combat_timeout_success(self):
        """Test successful combat timeout event publishing."""
        # Create combat timeout event
        event = CombatTimeoutEvent(
            combat_id=self.test_combat_id,
            room_id=self.test_room_id,
            timeout_minutes=5,
            last_activity=None,
        )

        # Execute
        result = await self.publisher.publish_combat_timeout(event)

        # Verify
        assert result is True
        self.mock_nats_service.publish.assert_called_once()

        # Verify the published data
        call_args = self.mock_nats_service.publish.call_args
        subject = call_args[0][0]
        message_data = call_args[0][1]

        assert subject == f"combat.timeout.{self.test_room_id}"
        assert message_data["event_type"] == "combat_timeout"
        assert message_data["data"]["combat_id"] == str(self.test_combat_id)
        assert message_data["data"]["room_id"] == self.test_room_id
        assert message_data["data"]["timeout_minutes"] == 5

    @pytest.mark.asyncio
    async def test_publish_nats_not_connected(self):
        """Test publishing when NATS is not connected."""
        # Setup NATS service as not connected
        self.mock_nats_service.is_connected.return_value = False

        # Create combat started event
        event = CombatStartedEvent(
            combat_id=self.test_combat_id,
            room_id=self.test_room_id,
            participants={},
            turn_order=[],
        )

        # Execute
        result = await self.publisher.publish_combat_started(event)

        # Verify
        assert result is False
        self.mock_nats_service.publish.assert_not_called()

    @pytest.mark.asyncio
    async def test_publish_nats_service_none(self):
        """Test publishing when NATS service is None."""
        # Create publisher with None NATS service
        publisher = CombatEventPublisher(nats_service=None)

        # Create combat started event
        event = CombatStartedEvent(
            combat_id=self.test_combat_id,
            room_id=self.test_room_id,
            participants={},
            turn_order=[],
        )

        # Execute
        result = await publisher.publish_combat_started(event)

        # Verify
        assert result is False

    @pytest.mark.asyncio
    async def test_publish_nats_publish_fails(self):
        """Test publishing when NATS publish fails."""
        # Setup NATS service to raise exception (publish now raises instead of returning False)
        from server.services.nats_exceptions import NATSPublishError

        self.mock_nats_service.publish.side_effect = NATSPublishError("Publish failed", subject="combat.started.test")

        # Create combat started event
        event = CombatStartedEvent(
            combat_id=self.test_combat_id,
            room_id=self.test_room_id,
            participants={},
            turn_order=[],
        )

        # Execute
        result = await self.publisher.publish_combat_started(event)

        # Verify
        assert result is False
        self.mock_nats_service.publish.assert_called_once()

    @pytest.mark.asyncio
    async def test_publish_nats_exception(self):
        """Test publishing when NATS raises an exception."""
        # Setup NATS service to raise an exception (generic exception, not NATSPublishError)
        self.mock_nats_service.publish.side_effect = Exception("NATS error")

        # Create combat started event
        event = CombatStartedEvent(
            combat_id=self.test_combat_id,
            room_id=self.test_room_id,
            participants={},
            turn_order=[],
        )

        # Execute - should catch exception and return False
        result = await self.publisher.publish_combat_started(event)

        # Verify
        assert result is False
        self.mock_nats_service.publish.assert_called_once()


class TestExtendedEventTypes:
    """Test extended event types with combat data."""

    def test_npc_attacked_event_with_combat_data(self):
        """Test NPCAttacked event with combat data."""
        event = NPCAttacked(
            npc_id="npc_001",
            target_id="player_001",
            room_id="room_001",
            damage=5,
            attack_type="physical",
            combat_id="combat_001",
            npc_name="Goblin",
            target_name="TestPlayer",
        )

        assert event.npc_id == "npc_001"
        assert event.target_id == "player_001"
        assert event.room_id == "room_001"
        assert event.damage == 5
        assert event.attack_type == "physical"
        assert event.combat_id == "combat_001"
        assert event.npc_name == "Goblin"
        assert event.target_name == "TestPlayer"

    def test_npc_took_damage_event_with_combat_data(self):
        """Test NPCTookDamage event with combat data."""
        event = NPCTookDamage(
            npc_id="npc_001",
            room_id="room_001",
            damage=5,
            damage_type="physical",
            source_id="player_001",
            combat_id="combat_001",
            npc_name="Goblin",
            current_hp=10,
            max_hp=15,
        )

        assert event.npc_id == "npc_001"
        assert event.room_id == "room_001"
        assert event.damage == 5
        assert event.damage_type == "physical"
        assert event.source_id == "player_001"
        assert event.combat_id == "combat_001"
        assert event.npc_name == "Goblin"
        assert event.current_hp == 10
        assert event.max_hp == 15

    def test_npc_died_event_with_combat_data(self):
        """Test NPCDied event with combat data."""
        event = NPCDied(
            npc_id="npc_001",
            room_id="room_001",
            cause="combat",
            killer_id="player_001",
            combat_id="combat_001",
            npc_name="Goblin",
            xp_reward=10,
        )

        assert event.npc_id == "npc_001"
        assert event.room_id == "room_001"
        assert event.cause == "combat"
        assert event.killer_id == "player_001"
        assert event.combat_id == "combat_001"
        assert event.npc_name == "Goblin"
        assert event.xp_reward == 10
