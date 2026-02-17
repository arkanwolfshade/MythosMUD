"""
Unit tests for damage blocking during login grace period.

Tests that damage and negative effects are properly blocked
when players are in login grace period.
"""

import uuid
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.game.magic.spell_effects import SpellEffects
from server.models.combat import CombatParticipant, CombatParticipantType
from server.models.game import StatusEffectType
from server.npc.combat_integration import NPCCombatIntegration
from server.realtime.login_grace_period import start_login_grace_period
from server.schemas.shared import TargetMatch, TargetType
from server.services.combat_attack_handler import CombatAttackHandler


@pytest.fixture
def mock_connection_manager():
    """Create a mock ConnectionManager."""
    manager = MagicMock()
    manager.login_grace_period_players = {}
    manager.login_grace_period_start_times = {}
    return manager


@pytest.fixture
def mock_combat_service():
    """Create a mock combat service."""
    return MagicMock()


@pytest.fixture
def mock_combat():
    """Create a mock combat instance."""
    combat = MagicMock()
    return combat


@pytest.fixture
def player_participant():
    """Create a player combat participant."""
    participant = CombatParticipant(
        participant_id=uuid.uuid4(),
        name="TestPlayer",
        participant_type=CombatParticipantType.PLAYER,
        current_dp=100,
        max_dp=100,
        dexterity=10,
    )
    return participant


@pytest.mark.asyncio
async def test_apply_damage_blocked_during_grace_period(
    mock_combat_service, player_participant, mock_connection_manager
):  # pylint: disable=redefined-outer-name  # Reason: Fixture parameter names match fixture function names, pytest standard pattern
    """Test that damage is blocked when target is in login grace period."""
    # Start grace period for player
    await start_login_grace_period(player_participant.participant_id, mock_connection_manager)

    # Create attack handler
    handler = CombatAttackHandler(mock_combat_service)

    # Mock config and app state
    with patch("server.services.combat_attack_handler.get_config") as mock_get_config:
        mock_config = MagicMock()
        mock_app = MagicMock()
        mock_app.state.connection_manager = mock_connection_manager
        mock_config._app_instance = mock_app  # pylint: disable=protected-access  # Reason: Testing internal config structure
        mock_get_config.return_value = mock_config

        # Try to apply damage
        old_dp = player_participant.current_dp
        old_dp_result, target_died, target_mortally_wounded = handler._apply_damage(player_participant, 50)  # pylint: disable=protected-access  # Reason: Testing internal damage application logic

        # Damage should be blocked - DP should not change
        assert old_dp_result == old_dp
        assert player_participant.current_dp == old_dp
        assert target_died is False
        assert target_mortally_wounded is False


def test_apply_damage_allowed_after_grace_period(mock_combat_service, player_participant, mock_connection_manager):  # pylint: disable=redefined-outer-name  # Reason: Fixture parameter names match fixture function names, pytest standard pattern
    """Test that damage is applied normally after grace period."""
    # Don't start grace period

    # Create attack handler
    handler = CombatAttackHandler(mock_combat_service)

    # Mock config and app state (but player not in grace period)
    with patch("server.services.combat_attack_handler.get_config") as mock_get_config:
        mock_config = MagicMock()
        mock_app = MagicMock()
        mock_app.state.connection_manager = mock_connection_manager
        mock_config._app_instance = mock_app  # pylint: disable=protected-access  # Reason: Testing internal config structure
        mock_get_config.return_value = mock_config

        # Try to apply damage
        old_dp = player_participant.current_dp
        old_dp_result, target_died, target_mortally_wounded = handler._apply_damage(player_participant, 30)  # pylint: disable=protected-access  # Reason: Testing internal damage application logic

        # Damage should be applied
        assert player_participant.current_dp == old_dp - 30
        assert old_dp_result == old_dp
        assert target_died is False  # Should not die from 30 damage
        assert target_mortally_wounded is False  # Should not be mortally wounded from 30 damage


def test_apply_damage_fails_open_on_error(mock_combat_service, player_participant):  # pylint: disable=redefined-outer-name  # Reason: Fixture parameter names match fixture function names, pytest standard pattern
    """Test that damage application fails open if grace period check errors."""
    # Create attack handler
    handler = CombatAttackHandler(mock_combat_service)

    # Mock config to raise an error, but catch it in the try/except
    with patch("server.services.combat_attack_handler.get_config", side_effect=Exception("Config error")):
        # Should still apply damage (fail open) - the exception is caught in the try/except
        old_dp = player_participant.current_dp
        _old_dp_result, _target_died, _target_mortally_wounded = handler._apply_damage(player_participant, 20)  # pylint: disable=protected-access  # Reason: Testing internal damage application logic

        # Damage should be applied (fail open) - exception is caught and damage proceeds
        assert player_participant.current_dp < old_dp


@pytest.mark.asyncio
async def test_npc_damage_blocked_during_grace_period(mock_connection_manager):  # pylint: disable=redefined-outer-name  # Reason: Fixture parameter name matches fixture function name, pytest standard pattern
    """Test that NPC damage is blocked when target is in login grace period."""
    player_id = str(uuid.uuid4())
    await start_login_grace_period(uuid.UUID(player_id), mock_connection_manager)

    # Create combat integration
    mock_event_bus = MagicMock()
    mock_persistence = MagicMock()
    combat_integration = NPCCombatIntegration(event_bus=mock_event_bus, async_persistence=mock_persistence)

    # Mock the internal game mechanics service
    mock_game_mechanics = MagicMock()
    combat_integration._game_mechanics = mock_game_mechanics  # pylint: disable=protected-access  # Reason: Testing internal service mocking for verification

    # Mock config and app state
    with patch("server.npc.combat_integration.get_config") as mock_get_config:
        mock_config = MagicMock()
        mock_app = MagicMock()
        mock_app.state.connection_manager = mock_connection_manager
        mock_config._app_instance = mock_app  # pylint: disable=protected-access  # Reason: Testing internal config structure
        mock_get_config.return_value = mock_config

        # Try to apply damage
        result = await combat_integration._apply_player_combat_effects(player_id, 50, "physical")  # pylint: disable=protected-access  # Reason: Testing internal combat effects logic

        # Damage should be blocked
        assert result is False
        # Verify damage_player was not called
        mock_game_mechanics.damage_player.assert_not_called()


@pytest.mark.asyncio
async def test_negative_status_effect_blocked_during_grace_period(mock_connection_manager):  # pylint: disable=redefined-outer-name  # Reason: Fixture parameter name matches fixture function name, pytest standard pattern
    """Test that negative status effects are blocked during grace period."""
    player_id = uuid.uuid4()
    await start_login_grace_period(player_id, mock_connection_manager)

    # Create spell effects processor
    mock_player_service = MagicMock()
    mock_persistence = MagicMock()
    mock_player = MagicMock()
    mock_player.get_status_effects.return_value = []
    mock_persistence.get_player_by_id = AsyncMock(return_value=mock_player)
    mock_player_service.persistence = mock_persistence

    processor = SpellEffects(mock_player_service)

    # Create a spell with negative effect
    mock_spell = MagicMock()
    mock_spell.spell_id = "test_spell"
    mock_spell.effect_data = {
        "status_effect_type": StatusEffectType.POISONED.value,
        "duration": 10,
        "intensity": 5,
    }

    # Create target
    target = TargetMatch(
        target_id=str(player_id),
        target_name="TestPlayer",
        target_type=TargetType.PLAYER,
        room_id="test_room_123",
    )

    # Mock config and app state
    with patch("server.game.magic.spell_effects.get_config") as mock_get_config:
        mock_config = MagicMock()
        mock_app = MagicMock()
        mock_app.state.connection_manager = mock_connection_manager
        mock_config._app_instance = mock_app  # pylint: disable=protected-access  # Reason: Testing internal config structure
        mock_get_config.return_value = mock_config

        # Try to apply negative status effect
        result = await processor._process_status_effect(mock_spell, target, 1.0)  # pylint: disable=protected-access  # Reason: Testing internal status effect processing logic for grace period blocking

        # Effect should be blocked
        assert result["success"] is False
        assert result["effect_applied"] is False
        assert "protected" in result["message"].lower() or "immune" in result["message"].lower()


@pytest.mark.asyncio
async def test_positive_status_effect_allowed_during_grace_period(mock_connection_manager):  # pylint: disable=redefined-outer-name  # Reason: Fixture parameter name matches fixture function name, pytest standard pattern
    """Test that positive status effects (buffs) are allowed during grace period."""
    player_id = uuid.uuid4()
    await start_login_grace_period(player_id, mock_connection_manager)

    # Create spell effects processor
    mock_player_service = MagicMock()
    mock_persistence = MagicMock()
    mock_player = MagicMock()
    mock_player.get_status_effects.return_value = []
    mock_persistence.get_player_by_id = AsyncMock(return_value=mock_player)
    mock_persistence.save_player = AsyncMock()
    mock_player_service.persistence = mock_persistence

    processor = SpellEffects(mock_player_service)

    # Create a spell with positive effect (buff)
    mock_spell = MagicMock()
    mock_spell.spell_id = "test_spell"
    mock_spell.effect_data = {
        "status_effect_type": StatusEffectType.BUFF.value,
        "duration": 10,
        "intensity": 5,
    }

    # Create target
    target = TargetMatch(
        target_id=str(player_id),
        target_name="TestPlayer",
        target_type=TargetType.PLAYER,
        room_id="test_room_123",
    )

    # Mock config and app state
    with patch("server.game.magic.spell_effects.get_config") as mock_get_config:
        mock_config = MagicMock()
        mock_app = MagicMock()
        mock_app.state.connection_manager = mock_connection_manager
        mock_config._app_instance = mock_app  # pylint: disable=protected-access  # Reason: Testing internal config structure
        mock_get_config.return_value = mock_config

        # Try to apply positive status effect
        result = await processor._process_status_effect(mock_spell, target, 1.0)  # pylint: disable=protected-access  # Reason: Testing internal status effect processing logic

        # Effect should be allowed (positive effects pass through)
        assert result["success"] is True
        assert result["effect_applied"] is True
