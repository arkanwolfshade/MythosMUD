"""
Comprehensive tests for the combat system.

This module tests the core combat logic, state management, messaging,
and integration with the existing systems.
"""

from datetime import datetime, timedelta
from uuid import uuid4

import pytest

from server.events.combat_events import (
    CombatEndedEvent,
    CombatStartedEvent,
    PlayerAttackedEvent,
)
from server.exceptions import MythosMUDError
from server.models.combat import CombatInstance, CombatParticipant, CombatParticipantType, CombatStatus
from server.services.combat_messaging_service import CombatMessagingService
from server.services.combat_service import CombatService


class TestCombatModels:
    """Test combat model classes."""

    def test_combat_participant_creation(self):
        """Test creating a combat participant."""
        participant = CombatParticipant(
            participant_id=uuid4(),
            participant_type=CombatParticipantType.PLAYER,
            name="TestPlayer",
            current_hp=100,
            max_hp=100,
            dexterity=15,
        )

        assert participant.name == "TestPlayer"
        assert participant.current_hp == 100
        assert participant.max_hp == 100
        assert participant.dexterity == 15
        assert participant.is_alive() is True

    def test_combat_participant_death(self):
        """Test combat participant death state."""
        participant = CombatParticipant(
            participant_id=uuid4(),
            participant_type=CombatParticipantType.PLAYER,
            name="TestPlayer",
            current_hp=0,
            max_hp=100,
            dexterity=15,
        )

        assert participant.is_alive() is False

    def test_combat_instance_creation(self):
        """Test creating a combat instance."""
        combat = CombatInstance(room_id="test_room")

        assert combat.room_id == "test_room"
        assert combat.status == CombatStatus.ACTIVE
        assert combat.combat_round == 0
        assert combat.current_turn == 0
        assert len(combat.participants) == 0
        assert len(combat.turn_order) == 0

    def test_combat_turn_management(self):
        """Test combat turn management."""
        combat = CombatInstance(room_id="test_room")

        # Add participants
        player_id = uuid4()
        npc_id = uuid4()

        player = CombatParticipant(
            participant_id=player_id,
            participant_type=CombatParticipantType.PLAYER,
            name="Player",
            current_hp=100,
            max_hp=100,
            dexterity=15,
        )

        npc = CombatParticipant(
            participant_id=npc_id,
            participant_type=CombatParticipantType.NPC,
            name="NPC",
            current_hp=50,
            max_hp=50,
            dexterity=10,
        )

        combat.participants[player_id] = player
        combat.participants[npc_id] = npc
        combat.turn_order = [player_id, npc_id]  # Player goes first (higher dex)

        # Test turn management
        assert combat.get_current_turn_participant() == player
        assert combat.current_turn == 0

        combat.advance_turn(current_tick=1)
        assert combat.get_current_turn_participant() == npc
        assert combat.current_turn == 1

        combat.advance_turn(current_tick=1)
        assert combat.get_current_turn_participant() == player
        assert combat.current_turn == 0
        assert combat.combat_round == 1

    def test_combat_end_conditions(self):
        """Test combat end conditions."""
        combat = CombatInstance(room_id="test_room")

        # Add participants
        player_id = uuid4()
        npc_id = uuid4()

        player = CombatParticipant(
            participant_id=player_id,
            participant_type=CombatParticipantType.PLAYER,
            name="Player",
            current_hp=100,
            max_hp=100,
            dexterity=15,
        )

        npc = CombatParticipant(
            participant_id=npc_id,
            participant_type=CombatParticipantType.NPC,
            name="NPC",
            current_hp=50,
            max_hp=50,
            dexterity=10,
        )

        combat.participants[player_id] = player
        combat.participants[npc_id] = npc

        # Both alive - combat should continue
        assert combat.is_combat_over() is False

        # One dies - combat should end
        npc.current_hp = 0
        assert combat.is_combat_over() is True

        # Both die - combat should end
        player.current_hp = 0
        assert combat.is_combat_over() is True


class TestCombatService:
    """Test the combat service."""

    @pytest.fixture
    def combat_service(self):
        """Create a combat service instance for testing."""
        return CombatService()

    @pytest.mark.asyncio
    async def test_start_combat(self, combat_service):
        """Test starting a new combat."""
        player_id = uuid4()
        npc_id = uuid4()

        combat = await combat_service.start_combat(
            room_id="test_room",
            attacker_id=player_id,
            target_id=npc_id,
            attacker_name="TestPlayer",
            target_name="TestNPC",
            attacker_hp=100,
            attacker_max_hp=100,
            attacker_dex=15,
            target_hp=50,
            target_max_hp=50,
            target_dex=10,
            current_tick=1,
        )

        assert combat.room_id == "test_room"
        assert len(combat.participants) == 2
        assert player_id in combat.participants
        assert npc_id in combat.participants
        assert len(combat.turn_order) == 2
        assert combat.turn_order[0] == player_id  # Higher dexterity goes first

    @pytest.mark.asyncio
    async def test_get_combat_by_participant(self, combat_service):
        """Test getting combat by participant ID."""
        player_id = uuid4()
        npc_id = uuid4()

        # Start combat
        combat = await combat_service.start_combat(
            room_id="test_room",
            attacker_id=player_id,
            target_id=npc_id,
            attacker_name="TestPlayer",
            target_name="TestNPC",
            attacker_hp=100,
            attacker_max_hp=100,
            attacker_dex=15,
            target_hp=50,
            target_max_hp=50,
            target_dex=10,
            current_tick=1,
        )

        # Test getting combat by participant
        found_combat = await combat_service.get_combat_by_participant(player_id)
        assert found_combat == combat

        found_combat = await combat_service.get_combat_by_participant(npc_id)
        assert found_combat == combat

        # Test non-existent participant
        non_existent_id = uuid4()
        found_combat = await combat_service.get_combat_by_participant(non_existent_id)
        assert found_combat is None

    @pytest.mark.asyncio
    async def test_process_attack(self, combat_service):
        """Test processing an attack action."""
        player_id = uuid4()
        npc_id = uuid4()

        # Start combat
        combat = await combat_service.start_combat(
            room_id="test_room",
            attacker_id=player_id,
            target_id=npc_id,
            attacker_name="TestPlayer",
            target_name="TestNPC",
            attacker_hp=100,
            attacker_max_hp=100,
            attacker_dex=15,
            target_hp=50,
            target_max_hp=50,
            target_dex=10,
            current_tick=1,
        )

        # Process attack
        result = await combat_service.process_attack(player_id, npc_id, damage=5)

        assert result.success is True
        assert result.damage == 5
        assert result.target_died is False
        assert result.combat_ended is False

        # Check that damage was applied
        npc = combat.participants[npc_id]
        assert npc.current_hp == 45  # 50 - 5

    @pytest.mark.asyncio
    async def test_process_attack_kills_target(self, combat_service):
        """Test processing an attack that kills the target."""
        player_id = uuid4()
        npc_id = uuid4()

        # Start combat
        combat = await combat_service.start_combat(
            room_id="test_room",
            attacker_id=player_id,
            target_id=npc_id,
            attacker_name="TestPlayer",
            target_name="TestNPC",
            attacker_hp=100,
            attacker_max_hp=100,
            attacker_dex=15,
            target_hp=5,
            target_max_hp=50,
            target_dex=10,
            current_tick=1,
        )

        # Process attack that kills target
        result = await combat_service.process_attack(player_id, npc_id, damage=10)

        assert result.success is True
        assert result.damage == 10
        assert result.target_died is True
        assert result.combat_ended is True
        assert result.xp_awarded > 0

        # Check that target is dead
        npc = combat.participants[npc_id]
        assert npc.current_hp == 0

        # Check that combat ended
        assert combat.status == CombatStatus.ENDED

    @pytest.mark.asyncio
    async def test_invalid_attack_not_in_combat(self, combat_service):
        """Test attacking when not in combat."""
        player_id = uuid4()
        npc_id = uuid4()

        with pytest.raises(ValueError, match="Attacker is not in combat"):
            await combat_service.process_attack(player_id, npc_id, damage=5)

    @pytest.mark.asyncio
    async def test_invalid_attack_wrong_turn(self, combat_service):
        """Test attacking when it's not the attacker's turn."""
        player_id = uuid4()
        npc_id = uuid4()

        # Start combat
        await combat_service.start_combat(
            room_id="test_room",
            attacker_id=player_id,
            target_id=npc_id,
            attacker_name="TestPlayer",
            target_name="TestNPC",
            attacker_hp=100,
            attacker_max_hp=100,
            attacker_dex=10,  # Lower dex - goes second
            target_hp=50,
            target_max_hp=50,
            target_dex=15,  # Higher dex - goes first
            current_tick=1,
        )

        # Try to attack when it's not player's turn
        with pytest.raises(ValueError, match="It is not the attacker's turn"):
            await combat_service.process_attack(player_id, npc_id, damage=5)

    @pytest.mark.asyncio
    async def test_end_combat(self, combat_service):
        """Test ending a combat."""
        player_id = uuid4()
        npc_id = uuid4()

        # Start combat
        combat = await combat_service.start_combat(
            room_id="test_room",
            attacker_id=player_id,
            target_id=npc_id,
            attacker_name="TestPlayer",
            target_name="TestNPC",
            attacker_hp=100,
            attacker_max_hp=100,
            attacker_dex=15,
            target_hp=50,
            target_max_hp=50,
            target_dex=10,
            current_tick=1,
        )

        combat_id = combat.combat_id

        # End combat
        await combat_service.end_combat(combat_id, "Test end")

        # Verify combat is ended
        assert combat.status == CombatStatus.ENDED
        assert combat.combat_id not in combat_service._active_combats
        assert player_id not in combat_service._player_combats
        assert npc_id not in combat_service._npc_combats

    @pytest.mark.asyncio
    async def test_cleanup_stale_combats(self, combat_service):
        """Test cleaning up stale combats."""
        player_id = uuid4()
        npc_id = uuid4()

        # Start combat
        combat = await combat_service.start_combat(
            room_id="test_room",
            attacker_id=player_id,
            target_id=npc_id,
            attacker_name="TestPlayer",
            target_name="TestNPC",
            attacker_hp=100,
            attacker_max_hp=100,
            attacker_dex=15,
            target_hp=50,
            target_max_hp=50,
            target_dex=10,
            current_tick=1,
        )

        # Manually set last activity to be stale
        combat.last_activity = datetime.utcnow() - timedelta(minutes=35)

        # Clean up stale combats
        cleaned_count = await combat_service.cleanup_stale_combats()

        assert cleaned_count == 1
        assert combat.status == CombatStatus.ENDED
        assert combat.combat_id not in combat_service._active_combats


class TestCombatMessagingService:
    """Test the combat messaging service."""

    @pytest.fixture
    def messaging_service(self):
        """Create a combat messaging service instance for testing."""
        return CombatMessagingService()

    @pytest.mark.asyncio
    async def test_get_attack_message_attacker_perspective(self, messaging_service):
        """Test generating attack message from attacker's perspective."""
        message = await messaging_service.get_attack_message(
            attacker_name="Player", target_name="Rat", damage=5, action_type="punch", perspective="attacker"
        )

        assert "You" in message
        assert "Rat" in message
        assert "5" in message
        assert "punch" in message

    @pytest.mark.asyncio
    async def test_get_attack_message_defender_perspective(self, messaging_service):
        """Test generating attack message from defender's perspective."""
        message = await messaging_service.get_attack_message(
            attacker_name="Player", target_name="Rat", damage=5, action_type="punch", perspective="defender"
        )

        assert "Player" in message
        assert "you" in message
        assert "5" in message
        assert "punch" in message

    @pytest.mark.asyncio
    async def test_get_attack_message_other_perspective(self, messaging_service):
        """Test generating attack message from other's perspective."""
        message = await messaging_service.get_attack_message(
            attacker_name="Player", target_name="Rat", damage=5, action_type="punch", perspective="other"
        )

        assert "Player" in message
        assert "Rat" in message
        assert "5" in message
        assert "punch" in message

    @pytest.mark.asyncio
    async def test_get_death_message(self, messaging_service):
        """Test generating death message."""
        message = await messaging_service.get_death_message("Rat")

        assert "Rat" in message
        assert "dead" in message.lower() or "dies" in message.lower()

    @pytest.mark.asyncio
    async def test_get_combat_start_messages(self, messaging_service):
        """Test generating combat start messages."""
        messages = await messaging_service.get_combat_start_messages(
            attacker_name="Player", target_name="Rat", room_occupants=["Player", "Rat", "Observer"]
        )

        assert len(messages) == 3
        assert "You attack Rat!" in messages["Player"]
        assert "Player attacks you!" in messages["Rat"]
        assert "Player attacks Rat!" in messages["Observer"]

    @pytest.mark.asyncio
    async def test_get_combat_end_messages(self, messaging_service):
        """Test generating combat end messages."""
        messages = await messaging_service.get_combat_end_messages(
            winner_name="Player", loser_name="Rat", room_occupants=["Player", "Rat", "Observer"]
        )

        assert len(messages) == 3
        assert "You defeat Rat!" in messages["Player"]
        assert "You are defeated by Player!" in messages["Rat"]
        assert "Player defeats Rat!" in messages["Observer"]

    @pytest.mark.asyncio
    async def test_get_error_message(self, messaging_service):
        """Test generating error messages."""
        message = await messaging_service.get_error_message(error_type="no_target", player_name="Player")

        assert "Player" in message
        assert "target" in message.lower()

    @pytest.mark.asyncio
    async def test_validate_npc_messages(self, messaging_service):
        """Test validating NPC message templates."""
        valid_messages = {
            "attack_attacker": "You {action_type} {target_name} for {damage} damage.",
            "attack_defender": "{attacker_name} {action_type}s you for {damage} damage.",
            "attack_other": "{attacker_name} {action_type}s {target_name} for {damage} damage.",
            "death_message": "{npc_name} dies.",
        }

        validated = await messaging_service.validate_npc_messages(valid_messages)
        assert validated is not None

        # Test invalid messages
        invalid_messages = {"attack_attacker": "Invalid template without required variables"}

        with pytest.raises(MythosMUDError):  # Should raise validation error
            await messaging_service.validate_npc_messages(invalid_messages)


class TestCombatEvents:
    """Test combat event classes."""

    def test_combat_started_event(self):
        """Test creating a combat started event."""
        event = CombatStartedEvent(
            combat_id=uuid4(),
            room_id="test_room",
            participants={"player": "Player", "npc": "Rat"},
            turn_order=["player", "npc"],
            event_type="combat_started",
            timestamp=datetime.utcnow(),
        )

        assert event.room_id == "test_room"
        assert len(event.participants) == 2
        assert len(event.turn_order) == 2

    def test_combat_ended_event(self):
        """Test creating a combat ended event."""
        event = CombatEndedEvent(
            combat_id=uuid4(),
            room_id="test_room",
            reason="Target defeated",
            duration_seconds=30,
            participants={"player": "Player", "npc": "Rat"},
            event_type="combat_ended",
            timestamp=datetime.utcnow(),
        )

        assert event.room_id == "test_room"
        assert event.reason == "Target defeated"
        assert event.duration_seconds == 30

    def test_player_attacked_event(self):
        """Test creating a player attacked event."""
        event = PlayerAttackedEvent(
            combat_id=uuid4(),
            room_id="test_room_001",
            attacker_id=uuid4(),
            attacker_name="Player",
            target_id=uuid4(),
            target_name="Rat",
            damage=5,
            action_type="punch",
            target_current_hp=45,
            target_max_hp=50,
            event_type="player_attacked",
            timestamp=datetime.utcnow(),
        )

        assert event.attacker_name == "Player"
        assert event.target_name == "Rat"
        assert event.damage == 5
        assert event.action_type == "punch"
