"""
Unit tests for combat turn processor.

Tests the CombatTurnProcessor class.
"""

from typing import Any
from unittest.mock import AsyncMock, MagicMock

import pytest

from server.models.combat import CombatAction, CombatParticipant, CombatParticipantType, CombatStatus
from server.services.combat_turn_processor import CombatTurnProcessor

# pylint: disable=protected-access  # Reason: Test file - accessing protected members is standard practice for unit testing
# pylint: disable=redefined-outer-name  # Reason: Test file - pytest fixture parameter names must match fixture names, causing intentional redefinitions


@pytest.fixture
def mock_combat_service() -> MagicMock:
    """Create a mock combat service."""
    return MagicMock()


@pytest.fixture
def combat_turn_processor(
    mock_combat_service: MagicMock,
) -> CombatTurnProcessor:  # pylint: disable=redefined-outer-name  # Reason: pytest fixture dependency injection - parameter name must match fixture name
    """Create a CombatTurnProcessor instance."""
    return CombatTurnProcessor(mock_combat_service)


def test_combat_turn_processor_init(combat_turn_processor):  # pylint: disable=redefined-outer-name  # Reason: pytest fixture parameter injection - parameter names must match fixture names
    """Test CombatTurnProcessor initialization."""
    # Verify the combat service was injected correctly
    assert combat_turn_processor._combat_service is not None  # pylint: disable=protected-access  # noqa: SLF001  # Reason: Test assertion requires access to protected member
    assert isinstance(combat_turn_processor._combat_service, MagicMock)  # pylint: disable=protected-access  # noqa: SLF001  # Reason: Test assertion requires access to protected member


@pytest.mark.asyncio
async def test_process_game_tick_disabled(combat_turn_processor):  # pylint: disable=redefined-outer-name  # Reason: pytest fixture parameter injection - parameter name must match fixture name
    """Test process_game_tick() returns early when auto-progression is disabled."""
    active_combats: dict[str, Any] = {}
    await combat_turn_processor.process_game_tick(100, active_combats, auto_progression_enabled=False)
    # Should return early without processing


@pytest.mark.asyncio
async def test_process_game_tick_no_combats(combat_turn_processor):  # pylint: disable=redefined-outer-name  # Reason: pytest fixture parameter injection - parameter name must match fixture name
    """Test process_game_tick() with no active combats."""
    active_combats: dict[str, Any] = {}
    await combat_turn_processor.process_game_tick(100, active_combats, auto_progression_enabled=True)
    # Should complete without errors


@pytest.mark.asyncio
async def test_process_game_tick_inactive_combat(combat_turn_processor):  # pylint: disable=redefined-outer-name  # Reason: pytest fixture parameter injection - parameter name must match fixture name
    """Test process_game_tick() skips inactive combats."""
    inactive_combat = MagicMock()
    inactive_combat.status = CombatStatus.ENDED
    active_combats: dict[str, Any] = {"combat_001": inactive_combat}
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
    combat.combat_round = 0
    combat.turn_order = []
    combat.current_turn = 0
    combat.participants = {}
    combat.queued_actions = {}
    combat.round_actions = {}
    combat.update_activity = MagicMock()
    combat.advance_turn = MagicMock()
    combat.get_current_turn_participant = MagicMock(return_value=None)
    combat.get_participants_by_initiative = MagicMock(return_value=[])
    combat.get_alive_participants = MagicMock(return_value=[])
    combat.clear_queued_actions = MagicMock()
    return combat


@pytest.mark.asyncio
async def test_process_game_tick_combat_auto_progression_disabled(combat_turn_processor, mock_combat):  # pylint: disable=redefined-outer-name  # Reason: pytest fixture parameter injection - parameter names must match fixture names
    """Test process_game_tick() when combat auto-progression is disabled."""
    mock_combat.status = CombatStatus.ACTIVE
    mock_combat.auto_progression_enabled = False
    active_combats: dict[str, Any] = {"combat_001": mock_combat}
    await combat_turn_processor.process_game_tick(100, active_combats, True)
    # Should skip combats with auto-progression disabled


@pytest.mark.asyncio
async def test_process_game_tick_tick_not_reached(combat_turn_processor, mock_combat):  # pylint: disable=redefined-outer-name  # Reason: pytest fixture parameter injection - parameter names must match fixture names
    """Test process_game_tick() when current tick hasn't reached next_turn_tick."""
    mock_combat.status = CombatStatus.ACTIVE
    mock_combat.auto_progression_enabled = True
    mock_combat.next_turn_tick = 200
    active_combats: dict[str, Any] = {"combat_001": mock_combat}
    await combat_turn_processor.process_game_tick(100, active_combats, True)
    # Should not advance turn yet


@pytest.mark.asyncio
async def test_execute_round_no_participants(combat_turn_processor, mock_combat):  # pylint: disable=redefined-outer-name  # Reason: pytest fixture parameter injection - parameter names must match fixture names
    """Test _execute_round() when no alive participants."""
    mock_combat.get_alive_participants = MagicMock(return_value=[])
    mock_combat.combat_id = "combat_001"
    combat_turn_processor._combat_service.end_combat = AsyncMock()  # pylint: disable=protected-access  # noqa: SLF001  # Reason: Test setup requires access to protected member for mock injection
    await combat_turn_processor._execute_round(mock_combat, 100)  # pylint: disable=protected-access  # noqa: SLF001  # Reason: Test requires direct access to protected method for unit testing
    # Should end combat when no alive participants
    combat_turn_processor._combat_service.end_combat.assert_called_once()  # pylint: disable=protected-access  # noqa: SLF001  # Reason: Test assertion requires access to protected member


@pytest.mark.asyncio
async def test_execute_round_with_participants(combat_turn_processor, mock_combat):  # pylint: disable=redefined-outer-name  # Reason: pytest fixture parameter injection - parameter names must match fixture names
    """Test _execute_round() processes all participants in initiative order."""
    from uuid import uuid4

    participant1_id = uuid4()
    participant1 = CombatParticipant(
        participant_id=participant1_id,
        participant_type=CombatParticipantType.PLAYER,
        name="Player1",
        current_dp=50,
        max_dp=100,
        dexterity=90,
    )
    participant2_id = uuid4()
    participant2 = CombatParticipant(
        participant_id=participant2_id,
        participant_type=CombatParticipantType.NPC,
        name="NPC1",
        current_dp=50,
        max_dp=100,
        dexterity=50,
    )

    mock_combat.get_participants_by_initiative = MagicMock(return_value=[participant1, participant2])
    mock_combat.round_actions = {}  # No queued actions
    combat_turn_processor._execute_default_action = AsyncMock()  # pylint: disable=protected-access  # noqa: SLF001  # Reason: Test setup requires access to protected member for mock injection

    await combat_turn_processor._execute_round(mock_combat, 100)  # pylint: disable=protected-access  # noqa: SLF001  # Reason: Test requires direct access to protected method for unit testing

    # Should execute default actions for both participants
    assert combat_turn_processor._execute_default_action.call_count == 2  # pylint: disable=protected-access  # noqa: SLF001  # Reason: Test assertion requires access to protected member
    mock_combat.advance_turn.assert_called_once_with(100)


@pytest.mark.asyncio
async def test_execute_round_stale_queued_attack_uses_default_action(combat_turn_processor, mock_combat):  # pylint: disable=redefined-outer-name  # Reason: pytest fixture parameter injection
    """Stale queued attack (target not in combat) does not raise and uses default action instead.

    Simulates: first combat ended, new combat started with second NPC; a queued action
    still references the first (slain) NPC. We must not call process_attack with that
    target_id and must not raise 'Target is not in this combat'.
    """
    from uuid import uuid4

    player_id = uuid4()
    npc_second_id = uuid4()
    stale_npc_id = uuid4()  # First NPC (not in this combat)

    player = CombatParticipant(
        participant_id=player_id,
        participant_type=CombatParticipantType.PLAYER,
        name="Player",
        current_dp=50,
        max_dp=100,
        dexterity=90,
    )
    npc_second = CombatParticipant(
        participant_id=npc_second_id,
        participant_type=CombatParticipantType.NPC,
        name="NPC_second",
        current_dp=50,
        max_dp=100,
        dexterity=50,
    )

    next_round = 1
    stale_action = CombatAction(
        attacker_id=player_id,
        target_id=stale_npc_id,  # Not in combat.participants
        action_type="attack",
        damage=10,
        round=next_round,
    )

    mock_combat.combat_round = 0
    mock_combat.combat_id = uuid4()
    mock_combat.participants = {player_id: player, npc_second_id: npc_second}
    mock_combat.queued_actions = {player_id: [stale_action]}
    mock_combat.round_actions = {}
    mock_combat.get_participants_by_initiative = MagicMock(return_value=[player, npc_second])
    mock_combat.clear_queued_actions = MagicMock()
    mock_combat.advance_turn = MagicMock()
    mock_combat.update_activity = MagicMock()

    combat_turn_processor._combat_service.process_attack = AsyncMock()
    combat_turn_processor._combat_service.end_combat = AsyncMock()
    combat_turn_processor._execute_default_action = AsyncMock()

    await combat_turn_processor._execute_round(mock_combat, 100)  # pylint: disable=protected-access  # noqa: SLF001  # Reason: Test requires direct access to protected method

    # Must not call process_attack with the stale target (would raise "Target is not in this combat")
    process_attack_calls = combat_turn_processor._combat_service.process_attack.call_args_list  # pylint: disable=protected-access  # noqa: SLF001
    for call in process_attack_calls:
        kwargs = call[1] if len(call) > 1 else {}
        target_id = kwargs.get("target_id")
        assert target_id != stale_npc_id, "process_attack must not be called with stale target_id"

    # Stale path: we fall back to default action for the player, then default for NPC
    assert combat_turn_processor._execute_default_action.call_count >= 1  # pylint: disable=protected-access  # noqa: SLF001
    mock_combat.advance_turn.assert_called_once_with(100)


@pytest.mark.asyncio
async def test_process_npc_turn_npc_dead(combat_turn_processor, mock_combat):  # pylint: disable=redefined-outer-name  # Reason: pytest fixture parameter injection - parameter names must match fixture names
    """Test _process_npc_turn() when NPC is dead (DP <= 0)."""
    npc = CombatParticipant(
        participant_id="npc_001",  # type: ignore[arg-type]
        participant_type=CombatParticipantType.NPC,
        name="TestNPC",
        current_dp=-5,
        max_dp=100,
        dexterity=50,
    )
    await combat_turn_processor._process_npc_turn(mock_combat, npc, 100)  # pylint: disable=protected-access  # noqa: SLF001  # Reason: Test requires direct access to protected method for unit testing
    # Should skip turn for dead NPC


@pytest.mark.asyncio
async def test_process_npc_turn_no_target(combat_turn_processor, mock_combat):  # pylint: disable=redefined-outer-name  # Reason: pytest fixture parameter injection - parameter names must match fixture names
    """Test _process_npc_turn() when no target found."""
    npc = CombatParticipant(
        participant_id="npc_001",  # type: ignore[arg-type]
        participant_type=CombatParticipantType.NPC,
        name="TestNPC",
        current_dp=50,
        max_dp=100,
        dexterity=50,
    )
    mock_combat.participants = {"npc_001": npc}  # Only one participant
    await combat_turn_processor._process_npc_turn(mock_combat, npc, 100)  # pylint: disable=protected-access  # noqa: SLF001  # Reason: Test requires direct access to protected method for unit testing
    # Should handle gracefully when no target


@pytest.mark.asyncio
async def test_process_npc_turn_no_participant_id(combat_turn_processor, mock_combat):  # pylint: disable=redefined-outer-name  # Reason: pytest fixture parameter injection - parameter names must match fixture names
    """Test _process_npc_turn() when NPC has no participant_id."""
    npc = MagicMock()
    npc.participant_id = None
    npc.name = "TestNPC"
    await combat_turn_processor._process_npc_turn(mock_combat, npc, 100)  # pylint: disable=protected-access  # noqa: SLF001  # Reason: Test requires direct access to protected method for unit testing
    # Should handle gracefully


@pytest.mark.asyncio
async def test_process_player_turn_player_unconscious(combat_turn_processor, mock_combat):  # pylint: disable=redefined-outer-name  # Reason: pytest fixture parameter injection - parameter names must match fixture names
    """Test _process_player_turn() when player is unconscious (DP <= 0)."""
    player = CombatParticipant(
        participant_id="player_001",  # type: ignore[arg-type]
        participant_type=CombatParticipantType.PLAYER,
        name="TestPlayer",
        current_dp=-5,
        max_dp=100,
        dexterity=50,
    )
    await combat_turn_processor._process_player_turn(mock_combat, player, 100)  # pylint: disable=protected-access  # noqa: SLF001  # Reason: Test requires direct access to protected method for unit testing
    # Should skip turn for unconscious player


@pytest.mark.asyncio
async def test_process_player_turn_no_target(combat_turn_processor, mock_combat):  # pylint: disable=redefined-outer-name  # Reason: pytest fixture parameter injection - parameter names must match fixture names
    """Test _process_player_turn() when no target found."""
    player = CombatParticipant(
        participant_id="player_001",  # type: ignore[arg-type]
        participant_type=CombatParticipantType.PLAYER,
        name="TestPlayer",
        current_dp=50,
        max_dp=100,
        dexterity=50,
    )
    mock_combat.participants = {"player_001": player}  # Only one participant
    await combat_turn_processor._process_player_turn(mock_combat, player, 100)  # pylint: disable=protected-access  # noqa: SLF001  # Reason: Test requires direct access to protected method for unit testing
    # Should handle gracefully when no target


@pytest.mark.asyncio
async def test_process_player_turn_no_participant_id(combat_turn_processor, mock_combat):  # pylint: disable=redefined-outer-name  # Reason: pytest fixture parameter injection - parameter names must match fixture names
    """Test _process_player_turn() when player has no participant_id."""
    player = MagicMock()
    player.participant_id = None
    player.name = "TestPlayer"
    await combat_turn_processor._process_player_turn(mock_combat, player, 100)  # pylint: disable=protected-access  # noqa: SLF001  # Reason: Test requires direct access to protected method for unit testing
    # Should handle gracefully


@pytest.mark.asyncio
async def test_process_player_turn_casting_spell(combat_turn_processor, mock_combat):  # pylint: disable=redefined-outer-name  # Reason: pytest fixture parameter injection - parameter names must match fixture names
    """Test _process_player_turn() when player is casting a spell."""
    player = CombatParticipant(
        participant_id="player_001",  # type: ignore[arg-type]
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
    combat_turn_processor._combat_service.magic_service = mock_magic_service  # pylint: disable=protected-access  # noqa: SLF001  # Reason: Test setup requires access to protected member for mock injection
    await combat_turn_processor._process_player_turn(mock_combat, player, 100)  # pylint: disable=protected-access  # noqa: SLF001  # Reason: Test requires direct access to protected method for unit testing
    # Should skip autoattack when casting


@pytest.mark.asyncio
async def test_process_player_turn_fallback_to_basic_unarmed_damage_when_no_app(
    combat_turn_processor, mock_combat, monkeypatch
):  # pylint: disable=redefined-outer-name  # Reason: pytest fixture parameter injection
    """When config has no _app_instance, process_attack is called with basic_unarmed_damage and damage_type physical."""
    from uuid import uuid4

    player_id = uuid4()
    target_id = uuid4()
    player = CombatParticipant(
        participant_id=player_id,
        participant_type=CombatParticipantType.PLAYER,
        name="Player",
        current_dp=50,
        max_dp=50,
        dexterity=12,
        is_active=True,
        last_action_tick=None,
    )
    target = CombatParticipant(
        participant_id=target_id,
        participant_type=CombatParticipantType.NPC,
        name="Target",
        current_dp=30,
        max_dp=30,
        dexterity=10,
        is_active=True,
        last_action_tick=None,
    )
    mock_combat.participants = {player_id: player, target_id: target}

    mock_config = MagicMock()
    mock_config.game.basic_unarmed_damage = 10
    mock_config._app_instance = None
    combat_turn_processor._combat_service.process_attack = AsyncMock()  # pylint: disable=protected-access  # noqa: SLF001  # Reason: Test assertion requires mock
    combat_turn_processor._combat_service.magic_service = None  # pylint: disable=protected-access  # noqa: SLF001  # Reason: Ensure casting check does not skip autoattack

    # Patch get_config where it is used: combat_turn_participant_actions (player turn runs there)
    monkeypatch.setattr("server.services.combat_turn_participant_actions.get_config", lambda: mock_config)
    await combat_turn_processor._process_player_turn(mock_combat, player, 100)  # pylint: disable=protected-access  # noqa: SLF001  # Reason: Test requires direct access to protected method

    combat_turn_processor._combat_service.process_attack.assert_called_once()  # pylint: disable=protected-access  # noqa: SLF001  # Reason: Test assertion
    call_kw = combat_turn_processor._combat_service.process_attack.call_args[1]  # pylint: disable=protected-access  # noqa: SLF001  # Reason: Test assertion
    assert call_kw["damage"] == 10
    assert call_kw["damage_type"] == "physical"


@pytest.mark.asyncio
async def test_process_player_turn_fallback_to_basic_unarmed_damage_when_no_player_from_persistence(
    combat_turn_processor, mock_combat, monkeypatch
):  # pylint: disable=redefined-outer-name  # Reason: pytest fixture parameter injection
    """When player_service.get_player_by_id returns None, process_attack uses basic_unarmed_damage."""
    from uuid import uuid4

    player_id = uuid4()
    target_id = uuid4()
    player = CombatParticipant(
        participant_id=player_id,
        participant_type=CombatParticipantType.PLAYER,
        name="Player",
        current_dp=50,
        max_dp=50,
        dexterity=12,
        is_active=True,
        last_action_tick=None,
    )
    target = CombatParticipant(
        participant_id=target_id,
        participant_type=CombatParticipantType.NPC,
        name="Target",
        current_dp=30,
        max_dp=30,
        dexterity=10,
        is_active=True,
        last_action_tick=None,
    )
    mock_combat.participants = {player_id: player, target_id: target}

    mock_config = MagicMock()
    mock_config.game.basic_unarmed_damage = 10
    mock_app = MagicMock()
    mock_app.state.container.player_service = MagicMock()
    mock_app.state.container.player_service.persistence.get_player_by_id = AsyncMock(return_value=None)
    mock_app.state.container.item_prototype_registry = MagicMock()
    mock_app.state.container.async_persistence = MagicMock()
    mock_config._app_instance = mock_app

    combat_turn_processor._combat_service.process_attack = AsyncMock()  # pylint: disable=protected-access  # noqa: SLF001  # Reason: Test assertion requires mock
    combat_turn_processor._combat_service.magic_service = None  # pylint: disable=protected-access  # noqa: SLF001  # Reason: Ensure casting check does not skip autoattack

    # Patch get_config where it is used: combat_turn_participant_actions (player turn runs there)
    monkeypatch.setattr("server.services.combat_turn_participant_actions.get_config", lambda: mock_config)
    await combat_turn_processor._process_player_turn(mock_combat, player, 100)  # pylint: disable=protected-access  # noqa: SLF001  # Reason: Test requires direct access to protected method

    combat_turn_processor._combat_service.process_attack.assert_called_once()  # pylint: disable=protected-access  # noqa: SLF001  # Reason: Test assertion
    call_kw = combat_turn_processor._combat_service.process_attack.call_args[1]  # pylint: disable=protected-access  # noqa: SLF001  # Reason: Test assertion
    assert call_kw["damage"] == 10
    assert call_kw["damage_type"] == "physical"
