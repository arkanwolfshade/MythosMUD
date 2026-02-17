"""
Unit tests for combat attack handler.

Tests the CombatAttackHandler class for attack validation, damage application,
and attack event publishing.
"""

import uuid
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.models.combat import CombatInstance, CombatParticipant, CombatParticipantType, CombatStatus
from server.services.combat_attack_handler import CombatAttackHandler

# pylint: disable=protected-access  # Reason: Test file - accessing protected members is standard practice for unit testing
# pylint: disable=redefined-outer-name  # Reason: Test file - pytest fixture parameter names must match fixture names, causing intentional redefinitions


@pytest.fixture
def mock_combat_service():
    """Create mock combat service."""
    return MagicMock()


@pytest.fixture
def attack_handler(mock_combat_service):
    """Create CombatAttackHandler instance."""
    return CombatAttackHandler(mock_combat_service)


@pytest.fixture
def mock_combat():
    """Create mock combat instance."""
    combat = MagicMock(spec=CombatInstance)
    combat.combat_id = uuid.uuid4()
    combat.status = CombatStatus.ACTIVE
    combat.participants = {}
    combat.update_activity = MagicMock()
    return combat


@pytest.fixture
def mock_attacker():
    """Create mock attacker participant."""
    attacker = MagicMock(spec=CombatParticipant)
    attacker.participant_id = uuid.uuid4()
    attacker.name = "Attacker"
    attacker.current_dp = 100
    attacker.max_dp = 100
    attacker.participant_type = CombatParticipantType.PLAYER
    attacker.is_alive = MagicMock(return_value=True)
    return attacker


@pytest.fixture
def mock_target_player():
    """Create target participant (player) for damage tests - uses real CombatParticipant for domain logic."""
    return CombatParticipant(
        participant_id=uuid.uuid4(),
        name="Target",
        participant_type=CombatParticipantType.PLAYER,
        current_dp=50,
        max_dp=50,
        dexterity=10,
    )


@pytest.fixture
def mock_target_npc():
    """Create target participant (NPC) for damage tests - uses real CombatParticipant for domain logic."""
    return CombatParticipant(
        participant_id=uuid.uuid4(),
        name="NPC",
        participant_type=CombatParticipantType.NPC,
        current_dp=30,
        max_dp=30,
        dexterity=10,
    )


def test_attack_handler_init(attack_handler, mock_combat_service):
    """Test CombatAttackHandler initialization."""
    assert attack_handler._combat_service == mock_combat_service


def test_validate_attack_active(attack_handler, mock_combat):
    """Test _validate_attack with active combat."""
    # Should not raise
    attack_handler._validate_attack(mock_combat, False)


def test_validate_attack_inactive(attack_handler, mock_combat):
    """Test _validate_attack with inactive combat."""
    mock_combat.status = CombatStatus.ENDED
    with pytest.raises(ValueError, match="not active"):
        attack_handler._validate_attack(mock_combat, False)


def test_apply_damage_player(attack_handler, mock_target_player):
    """Test _apply_damage applies damage to player."""
    old_dp, died, mortally_wounded = attack_handler._apply_damage(mock_target_player, 20)

    assert old_dp == 50
    assert mock_target_player.current_dp == 30
    assert died is False
    assert mortally_wounded is False


def test_apply_damage_player_kills(attack_handler, mock_target_player):
    """Test _apply_damage kills player when DP <= -10."""
    mock_target_player.current_dp = 5
    old_dp, died, mortally_wounded = attack_handler._apply_damage(mock_target_player, 15)

    assert old_dp == 5
    assert mock_target_player.current_dp == -10
    assert died is True
    assert mortally_wounded is False


def test_apply_damage_player_mortally_wounded(attack_handler, mock_target_player):
    """Test _apply_damage marks player as mortally wounded."""
    mock_target_player.current_dp = 5
    old_dp, died, mortally_wounded = attack_handler._apply_damage(mock_target_player, 5)

    assert old_dp == 5
    assert mock_target_player.current_dp == 0
    assert died is False
    assert mortally_wounded is True


def test_apply_damage_player_negative_cap(attack_handler, mock_target_player):
    """Test _apply_damage caps player DP at -10."""
    mock_target_player.current_dp = 5
    _old_dp, died, _mortally_wounded = attack_handler._apply_damage(mock_target_player, 100)

    assert mock_target_player.current_dp == -10
    assert died is True


def test_apply_damage_npc(attack_handler, mock_target_npc):
    """Test _apply_damage applies damage to NPC."""
    old_dp, died, mortally_wounded = attack_handler._apply_damage(mock_target_npc, 15)

    assert old_dp == 30
    assert mock_target_npc.current_dp == 15
    assert died is False
    assert mortally_wounded is False


def test_apply_damage_npc_kills(attack_handler, mock_target_npc):
    """Test _apply_damage kills NPC when DP <= 0."""
    mock_target_npc.current_dp = 5
    old_dp, died, mortally_wounded = attack_handler._apply_damage(mock_target_npc, 5)

    assert old_dp == 5
    assert mock_target_npc.current_dp == 0
    assert died is True
    assert mortally_wounded is False


def test_apply_damage_npc_zero_cap(attack_handler, mock_target_npc):
    """Test _apply_damage caps NPC DP at 0."""
    mock_target_npc.current_dp = 5
    _old_dp, died, _mortally_wounded = attack_handler._apply_damage(mock_target_npc, 100)

    assert mock_target_npc.current_dp == 0
    assert died is True


def test_apply_damage_player_grace_period(attack_handler, mock_target_player):
    """Test _apply_damage blocks damage when player in login grace period."""
    with patch("server.services.combat_attack_handler.get_config") as mock_get_config:
        mock_config = MagicMock()
        mock_app = MagicMock()
        mock_connection_manager = MagicMock()
        mock_app.state.connection_manager = mock_connection_manager
        mock_config._app_instance = mock_app
        mock_get_config.return_value = mock_config

        with patch("server.services.combat_attack_handler.is_player_in_login_grace_period", return_value=True):
            old_dp, died, mortally_wounded = attack_handler._apply_damage(mock_target_player, 20)

            assert old_dp == 50
            assert mock_target_player.current_dp == 50  # No damage applied
            assert died is False
            assert mortally_wounded is False


def test_apply_damage_player_grace_period_no_app(attack_handler, mock_target_player):
    """Test _apply_damage proceeds when app not available."""
    with patch("server.services.combat_attack_handler.get_config") as mock_get_config:
        mock_config = MagicMock()
        mock_config._app_instance = None  # No app
        mock_get_config.return_value = mock_config
        # Should proceed with damage
        attack_handler._apply_damage(mock_target_player, 20)
        assert mock_target_player.current_dp == 30  # Damage applied


def test_apply_damage_player_grace_period_no_connection_manager(attack_handler, mock_target_player):
    """Test _apply_damage proceeds when connection_manager not available."""
    with patch("server.services.combat_attack_handler.get_config") as mock_get_config:
        mock_config = MagicMock()
        mock_app = MagicMock()
        mock_app.state.connection_manager = None  # No connection manager
        mock_config._app_instance = mock_app
        mock_get_config.return_value = mock_config
        # Should proceed with damage
        attack_handler._apply_damage(mock_target_player, 20)
        assert mock_target_player.current_dp == 30  # Damage applied


def test_apply_damage_player_grace_period_error(attack_handler, mock_target_player):
    """Test _apply_damage proceeds when grace period check fails."""
    with patch("server.services.combat_attack_handler.get_config", side_effect=Exception("Config error")):
        # Should proceed with damage despite error
        old_dp, _died, _mortally_wounded = attack_handler._apply_damage(mock_target_player, 20)

        assert old_dp == 50
        assert mock_target_player.current_dp == 30  # Damage applied


def test_apply_damage_player_no_death_room_caps_damage(attack_handler, mock_target_player):
    """Test _apply_damage caps damage in no_death rooms so player DP never goes below 0."""
    mock_target_player.current_dp = 10
    mock_combat = MagicMock(spec=CombatInstance)
    mock_combat.room_id = "tutorial_room_001"

    with patch("server.async_persistence.get_async_persistence") as mock_get_persist:
        mock_persistence = MagicMock()
        mock_room = MagicMock()
        mock_room.attributes = {"no_death": True}
        mock_persistence.get_room_by_id.return_value = mock_room
        mock_get_persist.return_value = mock_persistence

        old_dp, died, mortally_wounded = attack_handler._apply_damage(mock_target_player, 50, mock_combat)

        # Damage capped to 10 (only enough to bring to 0), no death
        assert old_dp == 10
        assert mock_target_player.current_dp == 0
        assert died is False
        assert mortally_wounded is True


def test_apply_damage_player_no_death_room_zero_damage_when_at_zero(attack_handler, mock_target_player):
    """Test _apply_damage in no_death room when player already at 0 DP - no further damage."""
    mock_target_player.current_dp = 0
    mock_combat = MagicMock(spec=CombatInstance)
    mock_combat.room_id = "tutorial_room_001"

    with patch("server.async_persistence.get_async_persistence") as mock_get_persist:
        mock_persistence = MagicMock()
        mock_room = MagicMock()
        mock_room.attributes = {"no_death": True}
        mock_persistence.get_room_by_id.return_value = mock_room
        mock_get_persist.return_value = mock_persistence

        old_dp, died, mortally_wounded = attack_handler._apply_damage(mock_target_player, 50, mock_combat)

        assert old_dp == 0
        assert mock_target_player.current_dp == 0
        assert died is False
        assert mortally_wounded is False


@pytest.mark.asyncio
async def test_apply_attack_damage(attack_handler, mock_combat, mock_target_player):
    """Test apply_attack_damage applies damage and updates combat."""
    old_dp, died, mortally_wounded = await attack_handler.apply_attack_damage(mock_combat, mock_target_player, 20)

    assert old_dp == 50
    assert mock_target_player.current_dp == 30
    assert died is False
    assert mortally_wounded is False
    mock_combat.update_activity.assert_called_once_with(0)


@pytest.mark.asyncio
async def test_validate_and_get_combat_participants_success(
    attack_handler, mock_combat_service, mock_combat, mock_attacker, mock_target_player
):
    """Test validate_and_get_combat_participants returns participants."""
    attacker_id = mock_attacker.participant_id
    target_id = mock_target_player.participant_id
    mock_combat.participants = {attacker_id: mock_attacker, target_id: mock_target_player}
    mock_combat_service.get_combat_by_participant = AsyncMock(return_value=mock_combat)

    combat, attacker, target = await attack_handler.validate_and_get_combat_participants(attacker_id, target_id, False)

    assert combat == mock_combat
    assert attacker == mock_attacker
    assert target == mock_target_player


@pytest.mark.asyncio
async def test_validate_and_get_combat_participants_not_in_combat(attack_handler, mock_combat_service):
    """Test validate_and_get_combat_participants raises when attacker not in combat."""
    attacker_id = uuid.uuid4()
    target_id = uuid.uuid4()
    mock_combat_service.get_combat_by_participant = AsyncMock(return_value=None)

    with pytest.raises(ValueError, match="not in combat"):
        await attack_handler.validate_and_get_combat_participants(attacker_id, target_id, False)


@pytest.mark.asyncio
async def test_validate_and_get_combat_participants_inactive_combat(attack_handler, mock_combat_service, mock_combat):
    """Test validate_and_get_combat_participants raises when combat inactive."""
    attacker_id = uuid.uuid4()
    target_id = uuid.uuid4()
    mock_combat.status = CombatStatus.ENDED
    mock_combat.participants = {}
    mock_combat_service.get_combat_by_participant = AsyncMock(return_value=mock_combat)

    with pytest.raises(ValueError, match="not active"):
        await attack_handler.validate_and_get_combat_participants(attacker_id, target_id, False)


@pytest.mark.asyncio
async def test_validate_and_get_combat_participants_target_not_found(
    attack_handler, mock_combat_service, mock_combat, mock_attacker
):
    """Test validate_and_get_combat_participants raises when target not in combat."""
    attacker_id = mock_attacker.participant_id
    target_id = uuid.uuid4()
    mock_combat.participants = {attacker_id: mock_attacker}
    mock_combat_service.get_combat_by_participant = AsyncMock(return_value=mock_combat)

    with pytest.raises(ValueError, match="not in this combat"):
        await attack_handler.validate_and_get_combat_participants(attacker_id, target_id, False)


@pytest.mark.asyncio
async def test_validate_and_get_combat_participants_target_dead(
    attack_handler, mock_combat_service, mock_combat, mock_attacker, mock_target_player
):
    """Test validate_and_get_combat_participants raises when target is dead."""
    attacker_id = mock_attacker.participant_id
    target_id = mock_target_player.participant_id
    mock_target_player.current_dp = -10  # Dead for player (DP <= -10)
    mock_combat.participants = {attacker_id: mock_attacker, target_id: mock_target_player}
    mock_combat_service.get_combat_by_participant = AsyncMock(return_value=mock_combat)

    with pytest.raises(ValueError, match="already dead"):
        await attack_handler.validate_and_get_combat_participants(attacker_id, target_id, False)


@pytest.mark.asyncio
async def test_validate_and_get_combat_participants_attacker_not_found(
    attack_handler, mock_combat_service, mock_combat, mock_target_player
):
    """Test validate_and_get_combat_participants raises when attacker not found."""
    attacker_id = uuid.uuid4()
    target_id = mock_target_player.participant_id
    mock_combat.participants = {target_id: mock_target_player}
    mock_combat_service.get_combat_by_participant = AsyncMock(return_value=mock_combat)

    with pytest.raises(ValueError, match="not found in combat"):
        await attack_handler.validate_and_get_combat_participants(attacker_id, target_id, False)
