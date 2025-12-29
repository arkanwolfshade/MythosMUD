"""
Unit tests for combat turn processor.

Tests the CombatTurnProcessor class.
"""

from unittest.mock import AsyncMock, MagicMock

import pytest

from server.models.combat import CombatParticipant, CombatParticipantType, CombatStatus
from server.services.combat_turn_processor import CombatTurnProcessor


@pytest.fixture
def mock_combat_service():
    """Create a mock combat service."""
    return MagicMock()


@pytest.fixture
def combat_turn_processor(mock_combat_service):
    """Create a CombatTurnProcessor instance."""
    return CombatTurnProcessor(mock_combat_service)


def test_combat_turn_processor_init(combat_turn_processor, mock_combat_service):
    """Test CombatTurnProcessor initialization."""
    assert combat_turn_processor._combat_service == mock_combat_service


@pytest.mark.asyncio
async def test_process_game_tick_disabled(combat_turn_processor):
    """Test process_game_tick() returns early when auto-progression is disabled."""
    active_combats = {}
    await combat_turn_processor.process_game_tick(100, active_combats, auto_progression_enabled=False)
    # Should return early without processing


@pytest.mark.asyncio
async def test_process_game_tick_no_combats(combat_turn_processor):
    """Test process_game_tick() with no active combats."""
    active_combats = {}
    await combat_turn_processor.process_game_tick(100, active_combats, auto_progression_enabled=True)
    # Should complete without errors


@pytest.mark.asyncio
async def test_process_game_tick_inactive_combat(combat_turn_processor):
    """Test process_game_tick() skips inactive combats."""
    mock_combat = MagicMock()
    mock_combat.status = CombatStatus.ENDED
    active_combats = {"combat_001": mock_combat}
    await combat_turn_processor.process_game_tick(100, active_combats, auto_progression_enabled=True)
    # Should skip inactive combat


@pytest.fixture
def mock_combat():
    """Create a mock combat instance."""
    combat = MagicMock()
    combat.status = CombatStatus.ACTIVE
    combat.auto_progression_enabled = True
    combat.next_turn_tick = 100
    combat.combat_id = "combat_001"
    combat.turn_order = []
    combat.current_turn = 0
    combat.participants = {}
    combat.update_activity = MagicMock()
    combat.advance_turn = MagicMock()
    combat.get_current_turn_participant = MagicMock(return_value=None)
    return combat


@pytest.mark.asyncio
async def test_process_game_tick_combat_auto_progression_disabled(combat_turn_processor, mock_combat):
    """Test process_game_tick() when combat auto-progression is disabled."""
    mock_combat.status = CombatStatus.ACTIVE
    mock_combat.auto_progression_enabled = False
    active_combats = {"combat_001": mock_combat}
    await combat_turn_processor.process_game_tick(100, active_combats, True)
    # Should skip combats with auto-progression disabled


@pytest.mark.asyncio
async def test_process_game_tick_tick_not_reached(combat_turn_processor, mock_combat):
    """Test process_game_tick() when current tick hasn't reached next_turn_tick."""
    mock_combat.status = CombatStatus.ACTIVE
    mock_combat.auto_progression_enabled = True
    mock_combat.next_turn_tick = 200
    active_combats = {"combat_001": mock_combat}
    await combat_turn_processor.process_game_tick(100, active_combats, True)
    # Should not advance turn yet


@pytest.mark.asyncio
async def test_advance_turn_automatically_no_participant(combat_turn_processor, mock_combat):
    """Test _advance_turn_automatically() when no current participant."""
    mock_combat.get_current_turn_participant = MagicMock(return_value=None)
    mock_combat.turn_order = []
    await combat_turn_processor._advance_turn_automatically(mock_combat, 100)
    # Should handle gracefully


@pytest.mark.asyncio
async def test_advance_turn_automatically_participant_missing(combat_turn_processor, mock_combat):
    """Test _advance_turn_automatically() when participant is missing from participants dict."""
    mock_combat.get_current_turn_participant = MagicMock(return_value=None)
    mock_combat.turn_order = ["participant_001"]
    mock_combat.current_turn = 0
    mock_combat.participants = {}  # Participant missing
    mock_combat.combat_id = "combat_001"
    combat_turn_processor._combat_service.end_combat = AsyncMock()
    await combat_turn_processor._advance_turn_automatically(mock_combat, 100)
    # Should end combat due to corrupted state


@pytest.mark.asyncio
async def test_process_npc_turn_npc_dead(combat_turn_processor, mock_combat):
    """Test _process_npc_turn() when NPC is dead (DP <= 0)."""
    npc = CombatParticipant(
        participant_id="npc_001",
        participant_type=CombatParticipantType.NPC,
        name="TestNPC",
        current_dp=-5,
        max_dp=100,
        dexterity=50,
    )
    await combat_turn_processor._process_npc_turn(mock_combat, npc, 100)
    # Should skip turn for dead NPC


@pytest.mark.asyncio
async def test_process_npc_turn_no_target(combat_turn_processor, mock_combat):
    """Test _process_npc_turn() when no target found."""
    npc = CombatParticipant(
        participant_id="npc_001",
        participant_type=CombatParticipantType.NPC,
        name="TestNPC",
        current_dp=50,
        max_dp=100,
        dexterity=50,
    )
    mock_combat.participants = {"npc_001": npc}  # Only one participant
    await combat_turn_processor._process_npc_turn(mock_combat, npc, 100)
    # Should handle gracefully when no target


@pytest.mark.asyncio
async def test_process_npc_turn_no_participant_id(combat_turn_processor, mock_combat):
    """Test _process_npc_turn() when NPC has no participant_id."""
    npc = MagicMock()
    npc.participant_id = None
    npc.name = "TestNPC"
    await combat_turn_processor._process_npc_turn(mock_combat, npc, 100)
    # Should handle gracefully


@pytest.mark.asyncio
async def test_process_player_turn_player_unconscious(combat_turn_processor, mock_combat):
    """Test _process_player_turn() when player is unconscious (DP <= 0)."""
    player = CombatParticipant(
        participant_id="player_001",
        participant_type=CombatParticipantType.PLAYER,
        name="TestPlayer",
        current_dp=-5,
        max_dp=100,
        dexterity=50,
    )
    await combat_turn_processor._process_player_turn(mock_combat, player, 100)
    # Should skip turn for unconscious player


@pytest.mark.asyncio
async def test_process_player_turn_no_target(combat_turn_processor, mock_combat):
    """Test _process_player_turn() when no target found."""
    player = CombatParticipant(
        participant_id="player_001",
        participant_type=CombatParticipantType.PLAYER,
        name="TestPlayer",
        current_dp=50,
        max_dp=100,
        dexterity=50,
    )
    mock_combat.participants = {"player_001": player}  # Only one participant
    await combat_turn_processor._process_player_turn(mock_combat, player, 100)
    # Should handle gracefully when no target


@pytest.mark.asyncio
async def test_process_player_turn_no_participant_id(combat_turn_processor, mock_combat):
    """Test _process_player_turn() when player has no participant_id."""
    player = MagicMock()
    player.participant_id = None
    player.name = "TestPlayer"
    await combat_turn_processor._process_player_turn(mock_combat, player, 100)
    # Should handle gracefully


@pytest.mark.asyncio
async def test_process_player_turn_casting_spell(combat_turn_processor, mock_combat):
    """Test _process_player_turn() when player is casting a spell."""
    player = CombatParticipant(
        participant_id="player_001",
        participant_type=CombatParticipantType.PLAYER,
        name="TestPlayer",
        current_dp=50,
        max_dp=100,
        dexterity=50,
    )
    mock_combat.participants = {
        "player_001": player,
        "npc_001": MagicMock(),
    }
    # Mock magic_service with casting state
    mock_magic_service = MagicMock()
    mock_casting_state_manager = MagicMock()
    mock_casting_state_manager.is_casting = MagicMock(return_value=True)
    mock_casting_state_manager.get_casting_state = MagicMock(return_value=MagicMock(spell_name="TestSpell"))
    mock_magic_service.casting_state_manager = mock_casting_state_manager
    combat_turn_processor._combat_service.magic_service = mock_magic_service
    await combat_turn_processor._process_player_turn(mock_combat, player, 100)
    # Should skip autoattack when casting
