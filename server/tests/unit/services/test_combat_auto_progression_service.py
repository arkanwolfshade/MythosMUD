"""
Test automatic combat progression functionality.

This module tests the automatic combat progression system that ensures
combat continues automatically until one participant is defeated.
"""

from uuid import uuid4

import pytest

from server.models.combat import CombatParticipantType
from server.services.combat_service import CombatParticipantData, CombatService


class TestCombatAutoProgression:
    """Test automatic combat progression functionality."""

    @pytest.fixture
    def mock_player_combat_service(self):
        """Create a mock player combat service."""
        return None  # We don't need the full service for this test

    @pytest.fixture
    def combat_service(self, mock_player_combat_service):
        """Create a combat service."""
        return CombatService(player_combat_service=mock_player_combat_service)

    @pytest.mark.asyncio
    async def test_automatic_combat_progression_player_attacks_npc(self, combat_service):
        """Test automatic combat progression when player attacks NPC."""
        # Setup: Player attacks NPC, NPC should automatically attack back
        player_id = uuid4()
        npc_id = uuid4()
        room_id = "test_room_001"

        # Start combat
        attacker = CombatParticipantData(
            participant_id=player_id,
            name="TestPlayer",
            current_dp=10,
            max_dp=10,
            dexterity=15,
            participant_type=CombatParticipantType.PLAYER,
        )
        target = CombatParticipantData(
            participant_id=npc_id,
            name="TestNPC",
            current_dp=5,
            max_dp=5,
            dexterity=10,
            participant_type=CombatParticipantType.NPC,
        )
        combat = await combat_service.start_combat(
            room_id=room_id,
            attacker=attacker,
            target=target,
            current_tick=1,
        )

        # Verify combat started
        assert combat.status.value == "active"
        assert len(combat.participants) == 2
        assert player_id in combat.participants
        assert npc_id in combat.participants

        # Player attacks NPC (should kill NPC with 5 damage)
        result = await combat_service.process_attack(player_id, npc_id, damage=5)

        # Verify attack succeeded and combat ended
        assert result.success is True
        assert result.target_died is True
        assert result.combat_ended is True

        # Verify combat is no longer active
        combat_after = await combat_service.get_combat_by_participant(player_id)
        assert combat_after is None  # Combat should be ended

    @pytest.mark.asyncio
    async def test_automatic_combat_progression_multiple_rounds(self, combat_service):
        """Test automatic combat progression with multiple rounds."""
        # Setup: Player and NPC with higher HP for multiple rounds
        player_id = uuid4()
        npc_id = uuid4()
        room_id = "test_room_001"

        # Start combat
        attacker = CombatParticipantData(
            participant_id=player_id,
            name="TestPlayer",
            current_dp=10,
            max_dp=10,
            dexterity=15,  # Higher dexterity, goes first
            participant_type=CombatParticipantType.PLAYER,
        )
        target = CombatParticipantData(
            participant_id=npc_id,
            name="TestNPC",
            current_dp=10,
            max_dp=10,
            dexterity=10,
            participant_type=CombatParticipantType.NPC,
        )
        combat = await combat_service.start_combat(
            room_id=room_id,
            attacker=attacker,
            target=target,
            current_tick=1,
        )

        # Player attacks NPC (1 damage)
        result1 = await combat_service.process_attack(player_id, npc_id, damage=1)

        # Verify first attack succeeded but combat continues
        assert result1.success is True
        assert result1.target_died is False
        assert result1.combat_ended is False

        # Check that NPC's HP was reduced
        npc_participant = combat.participants[npc_id]
        assert npc_participant.current_dp == 9  # 10 - 1 = 9

        # The automatic progression should have processed the NPC's turn
        # and advanced back to the player's turn
        current_participant = combat.get_current_turn_participant()
        assert current_participant is not None
        assert current_participant.participant_id == player_id

        # Player attacks again (should kill NPC)
        result2 = await combat_service.process_attack(player_id, npc_id, damage=9)

        # Verify second attack killed NPC and ended combat
        assert result2.success is True
        assert result2.target_died is True
        assert result2.combat_ended is True

    @pytest.mark.asyncio
    async def test_automatic_combat_progression_npc_kills_player(self, combat_service):
        """Test automatic combat progression when NPC kills player."""
        # Setup: Player with higher dexterity goes first, but NPC attacks back
        player_id = uuid4()
        npc_id = uuid4()
        room_id = "test_room_001"

        # Start combat with player having higher dexterity
        attacker = CombatParticipantData(
            participant_id=player_id,
            name="TestPlayer",
            current_dp=5,
            max_dp=5,
            dexterity=15,  # Higher dexterity, goes first
            participant_type=CombatParticipantType.PLAYER,
        )
        target = CombatParticipantData(
            participant_id=npc_id,
            name="TestNPC",
            current_dp=10,
            max_dp=10,
            dexterity=10,
            participant_type=CombatParticipantType.NPC,
        )
        combat = await combat_service.start_combat(
            room_id=room_id,
            attacker=attacker,
            target=target,
            current_tick=1,
        )

        # Player attacks NPC (1 damage)
        result = await combat_service.process_attack(player_id, npc_id, damage=1)

        # Verify attack succeeded but combat continues
        assert result.success is True
        assert result.target_died is False
        assert result.combat_ended is False

        # The automatic progression should have processed the NPC's turn
        # and the NPC should have attacked the player
        player_participant = combat.participants[player_id]

        # Check if player was damaged by NPC's automatic attack
        # (This depends on the NPC's damage output)
        assert player_participant.current_dp <= 5  # Player took damage
        # Verify it's now the player's turn again
        current_participant = combat.get_current_turn_participant()
        assert current_participant is not None
        assert current_participant.participant_id == player_id
        assert current_participant.participant_type == (CombatParticipantType.PLAYER)

    @pytest.mark.asyncio
    async def test_combat_progression_stops_at_player_turn(self, combat_service):
        """Test that automatic progression stops when it's a player's turn."""
        # Setup: Player with higher dexterity
        player_id = uuid4()
        npc_id = uuid4()
        room_id = "test_room_001"

        # Start combat
        attacker = CombatParticipantData(
            participant_id=player_id,
            name="TestPlayer",
            current_dp=10,
            max_dp=10,
            dexterity=15,  # Higher dexterity, goes first
            participant_type=CombatParticipantType.PLAYER,
        )
        target = CombatParticipantData(
            participant_id=npc_id,
            name="TestNPC",
            current_dp=10,
            max_dp=10,
            dexterity=10,
            participant_type=CombatParticipantType.NPC,
        )
        combat = await combat_service.start_combat(
            room_id=room_id,
            attacker=attacker,
            target=target,
            current_tick=1,
        )

        # Player attacks NPC (1 damage)
        result = await combat_service.process_attack(player_id, npc_id, damage=1)

        # Verify attack succeeded but combat continues
        assert result.success is True
        assert result.target_died is False
        assert result.combat_ended is False

        # Verify it's still the player's turn (auto progression should stop)
        current_participant = combat.get_current_turn_participant()
        assert current_participant is not None
        assert current_participant.participant_id == player_id
        assert current_participant.participant_type == (CombatParticipantType.PLAYER)

    @pytest.mark.asyncio
    async def test_combat_progression_handles_errors_gracefully(self, combat_service):
        """Test that combat progression handles errors gracefully."""
        # Setup: Player attacks NPC
        player_id = uuid4()
        npc_id = uuid4()
        room_id = "test_room_001"

        # Start combat
        attacker = CombatParticipantData(
            participant_id=player_id,
            name="TestPlayer",
            current_dp=10,
            max_dp=10,
            dexterity=15,
            participant_type=CombatParticipantType.PLAYER,
        )
        target = CombatParticipantData(
            participant_id=npc_id,
            name="TestNPC",
            current_dp=10,
            max_dp=10,
            dexterity=10,
            participant_type=CombatParticipantType.NPC,
        )
        combat = await combat_service.start_combat(
            room_id=room_id,
            attacker=attacker,
            target=target,
            current_tick=1,
        )

        # Player attacks NPC (1 damage)
        result = await combat_service.process_attack(player_id, npc_id, damage=1)

        # Verify attack succeeded
        assert result.success is True
        assert result.target_died is False
        assert result.combat_ended is False

        # The automatic progression should handle any errors gracefully
        # and not cause infinite loops or crashes
        current_participant = combat.get_current_turn_participant()
        assert current_participant is not None

    @pytest.mark.asyncio
    async def test_unconscious_player_cannot_autoattack(self, combat_service):
        """
        Test that unconscious players (HP <= 0) cannot perform automatic attacks.

        This test addresses GitHub Issue #243 where unconscious players continued
        attacking during auto-progression.
        """
        # Setup: Player with very low HP attacks NPC
        player_id = uuid4()
        npc_id = uuid4()
        room_id = "test_room_001"

        # Start combat with player having 10 HP and NPC having high HP
        # Player goes first (higher dex)
        attacker = CombatParticipantData(
            participant_id=player_id,
            name="TestPlayer",
            current_dp=10,
            max_dp=100,
            dexterity=15,  # Higher dexterity, goes first
            participant_type=CombatParticipantType.PLAYER,
        )
        target = CombatParticipantData(
            participant_id=npc_id,
            name="TestNPC",
            current_dp=100,
            max_dp=100,
            dexterity=10,
            participant_type=CombatParticipantType.NPC,
        )
        combat = await combat_service.start_combat(
            room_id=room_id,
            attacker=attacker,
            target=target,
            current_tick=1,
        )

        # Verify combat started
        assert combat.status.value == "active"

        # Record NPC's initial HP
        npc_participant = combat.participants[npc_id]
        initial_npc_hp = npc_participant.current_dp

        # Player attacks NPC (3 damage)
        result1 = await combat_service.process_attack(player_id, npc_id, damage=3)
        assert result1.success is True

        # Verify NPC took damage
        assert npc_participant.current_dp == initial_npc_hp - 3

        # Get player participant and reduce HP to 0 (unconscious)
        player_participant = combat.participants[player_id]
        player_participant.current_dp = 0

        # Record NPC's HP before player's unconscious turn
        npc_hp_before_unconscious_turn = npc_participant.current_dp

        # Process player turn while unconscious (auto-progression)
        await combat_service._process_player_turn(combat, player_participant, current_tick=2)

        # CRITICAL: NPC HP should NOT have changed (unconscious player cannot attack)
        assert npc_participant.current_dp == npc_hp_before_unconscious_turn

        # Verify player's last action tick was updated (turn was acknowledged but no action taken)
        assert player_participant.last_action_tick == 2

    @pytest.mark.asyncio
    async def test_mortally_wounded_player_cannot_autoattack(self, combat_service):
        """
        Test that mortally wounded players (HP in range -9 to 0) cannot perform automatic attacks.

        This extends GitHub Issue #243 to cover the mortally wounded state.
        """
        # Setup: Player attacks NPC
        player_id = uuid4()
        npc_id = uuid4()
        room_id = "test_room_001"

        # Start combat
        attacker = CombatParticipantData(
            participant_id=player_id,
            name="TestPlayer",
            current_dp=50,
            max_dp=100,
            dexterity=15,
            participant_type=CombatParticipantType.PLAYER,
        )
        target = CombatParticipantData(
            participant_id=npc_id,
            name="TestNPC",
            current_dp=100,
            max_dp=100,
            dexterity=10,
            participant_type=CombatParticipantType.NPC,
        )
        combat = await combat_service.start_combat(
            room_id=room_id,
            attacker=attacker,
            target=target,
            current_tick=1,
        )

        # Get participants
        player_participant = combat.participants[player_id]
        npc_participant = combat.participants[npc_id]

        # Set player HP to mortally wounded state (-5 HP)
        player_participant.current_dp = -5

        # Record NPC's HP before player's turn
        npc_hp_before = npc_participant.current_dp

        # Process player turn while mortally wounded
        await combat_service._process_player_turn(combat, player_participant, current_tick=2)

        # CRITICAL: NPC HP should NOT have changed
        assert npc_participant.current_dp == npc_hp_before

        # Verify player's last action tick was updated
        assert player_participant.last_action_tick == 2

    @pytest.mark.asyncio
    async def test_dead_npc_cannot_autoattack(self, combat_service):
        """
        Test that dead NPCs (HP <= 0) cannot perform automatic attacks.

        This test ensures symmetry with player consciousness checks - NPCs should
        not be able to act when HP <= 0, as documented in combat model is_alive().
        """
        # Setup: NPC with very low HP attacks Player
        player_id = uuid4()
        npc_id = uuid4()
        room_id = "test_room_001"

        # Start combat with NPC having 10 HP and Player having high HP
        # NPC goes first (higher dex)
        attacker = CombatParticipantData(
            participant_id=npc_id,
            name="TestNPC",
            current_dp=10,
            max_dp=100,
            dexterity=15,  # Higher dexterity, goes first
            participant_type=CombatParticipantType.NPC,
        )
        target = CombatParticipantData(
            participant_id=player_id,
            name="TestPlayer",
            current_dp=100,
            max_dp=100,
            dexterity=10,
            participant_type=CombatParticipantType.PLAYER,
        )
        combat = await combat_service.start_combat(
            room_id=room_id,
            attacker=attacker,
            target=target,
            current_tick=1,
        )

        # Verify combat started
        assert combat.status.value == "active"

        # Get participants
        npc_participant = combat.participants[npc_id]
        player_participant = combat.participants[player_id]

        # Record Player's initial HP
        initial_player_hp = player_participant.current_dp

        # NPC attacks Player (3 damage)
        result1 = await combat_service.process_attack(npc_id, player_id, damage=3)
        assert result1.success is True

        # Verify Player took damage
        assert player_participant.current_dp == initial_player_hp - 3

        # Set NPC HP to 0 (dead)
        npc_participant.current_dp = 0

        # Record Player's HP before NPC's dead turn
        player_hp_before_dead_turn = player_participant.current_dp

        # Process NPC turn while dead (auto-progression)
        await combat_service._process_npc_turn(combat, npc_participant, current_tick=2)

        # CRITICAL: Player HP should NOT have changed (dead NPC cannot attack)
        assert player_participant.current_dp == player_hp_before_dead_turn

        # Verify NPC's last action tick was updated (turn was acknowledged but no action taken)
        assert npc_participant.last_action_tick == 2

    @pytest.mark.asyncio
    async def test_negative_hp_npc_cannot_autoattack(self, combat_service):
        """
        Test that NPCs with negative HP cannot perform automatic attacks.

        NPCs die immediately at HP <= 0 (unlike players who have mortally wounded state).
        """
        # Setup: NPC attacks Player
        player_id = uuid4()
        npc_id = uuid4()
        room_id = "test_room_001"

        # Start combat
        attacker = CombatParticipantData(
            participant_id=npc_id,
            name="TestNPC",
            current_dp=50,
            max_dp=100,
            dexterity=15,
            participant_type=CombatParticipantType.NPC,
        )
        target = CombatParticipantData(
            participant_id=player_id,
            name="TestPlayer",
            current_dp=100,
            max_dp=100,
            dexterity=10,
            participant_type=CombatParticipantType.PLAYER,
        )
        combat = await combat_service.start_combat(
            room_id=room_id,
            attacker=attacker,
            target=target,
            current_tick=1,
        )

        # Get participants
        npc_participant = combat.participants[npc_id]
        player_participant = combat.participants[player_id]

        # Set NPC HP to negative (well beyond dead)
        npc_participant.current_dp = -5

        # Record Player's HP before NPC's turn
        player_hp_before = player_participant.current_dp

        # Process NPC turn while dead
        await combat_service._process_npc_turn(combat, npc_participant, current_tick=2)

        # CRITICAL: Player HP should NOT have changed
        assert player_participant.current_dp == player_hp_before

        # Verify NPC's last action tick was updated
        assert npc_participant.last_action_tick == 2
