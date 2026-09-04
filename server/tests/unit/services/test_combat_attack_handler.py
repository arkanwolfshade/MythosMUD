"""
Unit tests for combat attack handler.

Tests the CombatAttackHandler class for attack validation, damage application,
and attack event publishing.
"""

# pyright: reportPrivateUsage=false
# Reason: Unit tests intentionally exercise CombatAttackHandler private helpers.

import uuid
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.models.combat import CombatInstance, CombatParticipant, CombatParticipantType, CombatStatus
from server.services.combat_attack_handler import CombatAttackHandler

# pylint: disable=protected-access  # Reason: Test file - accessing protected members is standard practice for unit testing
# pylint: disable=redefined-outer-name  # Reason: Test file - pytest fixture parameter names must match fixture names, causing intentional redefinitions


def _persistence_with_room_attributes(attributes: dict[str, bool]) -> MagicMock:
    mock_persistence: MagicMock = MagicMock()
    mock_room: MagicMock = MagicMock()
    mock_room.attributes = attributes
    get_room_by_id: MagicMock = MagicMock(return_value=mock_room)
    mock_persistence.get_room_by_id = get_room_by_id
    return mock_persistence


def _bind_get_combat_by_participant(mock_combat_service: MagicMock, return_value: CombatInstance | None) -> AsyncMock:
    get_combat_by_participant: AsyncMock = AsyncMock(return_value=return_value)
    mock_combat_service.get_combat_by_participant = get_combat_by_participant
    return get_combat_by_participant


@pytest.fixture
def mock_combat_service() -> MagicMock:
    """Create mock combat service."""
    return MagicMock()


@pytest.fixture
def attack_handler(mock_combat_service: MagicMock) -> CombatAttackHandler:
    """Create CombatAttackHandler instance."""
    return CombatAttackHandler(mock_combat_service)


@pytest.fixture
def mock_combat() -> CombatInstance:
    """Create combat instance for handler tests."""
    combat = CombatInstance()
    combat.combat_id = uuid.uuid4()
    combat.status = CombatStatus.ACTIVE
    combat.participants = {}
    return combat


@pytest.fixture
def mock_attacker() -> CombatParticipant:
    """Create attacker participant."""
    return CombatParticipant(
        participant_id=uuid.uuid4(),
        name="Attacker",
        participant_type=CombatParticipantType.PLAYER,
        current_dp=100,
        max_dp=100,
        dexterity=10,
    )


@pytest.fixture
def mock_target_player() -> CombatParticipant:
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
def mock_target_npc() -> CombatParticipant:
    """Create target participant (NPC) for damage tests - uses real CombatParticipant for domain logic."""
    return CombatParticipant(
        participant_id=uuid.uuid4(),
        name="NPC",
        participant_type=CombatParticipantType.NPC,
        current_dp=30,
        max_dp=30,
        dexterity=10,
    )


def test_attack_handler_init(attack_handler: CombatAttackHandler, mock_combat_service: MagicMock) -> None:
    """Test CombatAttackHandler initialization."""
    assert attack_handler._combat_service == mock_combat_service


def test_validate_attack_active(attack_handler: CombatAttackHandler, mock_combat: CombatInstance) -> None:
    """Test _validate_attack with active combat."""
    # Should not raise
    attack_handler._validate_attack(mock_combat, False)


def test_validate_attack_inactive(attack_handler: CombatAttackHandler, mock_combat: CombatInstance) -> None:
    """Test _validate_attack with inactive combat."""
    mock_combat.status = CombatStatus.ENDED
    with pytest.raises(ValueError, match="not active"):
        attack_handler._validate_attack(mock_combat, False)


def test_apply_damage_player(attack_handler: CombatAttackHandler, mock_target_player: CombatParticipant) -> None:
    """Test _apply_damage applies damage to player."""
    old_dp, died, mortally_wounded = attack_handler._apply_damage(mock_target_player, 20)

    assert old_dp == 50
    assert mock_target_player.current_dp == 30
    assert died is False
    assert mortally_wounded is False


def test_apply_damage_player_kills(attack_handler: CombatAttackHandler, mock_target_player: CombatParticipant) -> None:
    """Test _apply_damage kills player when DP <= -10."""
    mock_target_player.current_dp = 5
    old_dp, died, mortally_wounded = attack_handler._apply_damage(mock_target_player, 15)

    assert old_dp == 5
    assert mock_target_player.current_dp == -10
    assert died is True
    assert mortally_wounded is False


def test_apply_damage_player_mortally_wounded(
    attack_handler: CombatAttackHandler, mock_target_player: CombatParticipant
) -> None:
    """Test _apply_damage marks player as mortally wounded."""
    mock_target_player.current_dp = 5
    old_dp, died, mortally_wounded = attack_handler._apply_damage(mock_target_player, 5)

    assert old_dp == 5
    assert mock_target_player.current_dp == 0
    assert died is False
    assert mortally_wounded is True


def test_apply_damage_player_negative_cap(
    attack_handler: CombatAttackHandler, mock_target_player: CombatParticipant
) -> None:
    """Test _apply_damage caps player DP at -10."""
    mock_target_player.current_dp = 5
    _old_dp, died, _mortally_wounded = attack_handler._apply_damage(mock_target_player, 100)

    assert mock_target_player.current_dp == -10
    assert died is True


def test_apply_damage_npc(attack_handler: CombatAttackHandler, mock_target_npc: CombatParticipant) -> None:
    """Test _apply_damage applies damage to NPC."""
    old_dp, died, mortally_wounded = attack_handler._apply_damage(mock_target_npc, 15)

    assert old_dp == 30
    assert mock_target_npc.current_dp == 15
    assert died is False
    assert mortally_wounded is False


def test_apply_damage_npc_kills(attack_handler: CombatAttackHandler, mock_target_npc: CombatParticipant) -> None:
    """Test _apply_damage kills NPC when DP <= 0."""
    mock_target_npc.current_dp = 5
    old_dp, died, mortally_wounded = attack_handler._apply_damage(mock_target_npc, 5)

    assert old_dp == 5
    assert mock_target_npc.current_dp == 0
    assert died is True
    assert mortally_wounded is False


def test_apply_damage_npc_zero_cap(attack_handler: CombatAttackHandler, mock_target_npc: CombatParticipant) -> None:
    """Test _apply_damage caps NPC DP at 0."""
    mock_target_npc.current_dp = 5
    _old_dp, died, _mortally_wounded = attack_handler._apply_damage(mock_target_npc, 100)

    assert mock_target_npc.current_dp == 0
    assert died is True


def test_apply_damage_player_grace_period(
    attack_handler: CombatAttackHandler, mock_target_player: CombatParticipant
) -> None:
    """Test _apply_damage blocks damage when player in login grace period."""
    with patch("server.services.combat_attack_handler.get_config") as mock_get_config:
        mock_config: MagicMock = MagicMock()
        mock_app: MagicMock = MagicMock()
        mock_app_state: MagicMock = MagicMock()
        mock_connection_manager: MagicMock = MagicMock()
        mock_app_state.connection_manager = mock_connection_manager
        mock_app.state = mock_app_state
        mock_config._app_instance = mock_app
        mock_get_config.return_value = mock_config

        with patch("server.services.combat_attack_handler.is_player_in_login_grace_period", return_value=True):
            old_dp, died, mortally_wounded = attack_handler._apply_damage(mock_target_player, 20)

            assert old_dp == 50
            assert mock_target_player.current_dp == 50  # No damage applied
            assert died is False
            assert mortally_wounded is False


def test_apply_damage_player_grace_period_no_app(
    attack_handler: CombatAttackHandler, mock_target_player: CombatParticipant
) -> None:
    """Test _apply_damage proceeds when app not available."""
    with patch("server.services.combat_attack_handler.get_config") as mock_get_config:
        mock_config: MagicMock = MagicMock()
        mock_config._app_instance = None  # No app
        mock_get_config.return_value = mock_config
        # Should proceed with damage
        _ = attack_handler._apply_damage(mock_target_player, 20)
        assert mock_target_player.current_dp == 30  # Damage applied


def test_apply_damage_player_grace_period_no_connection_manager(
    attack_handler: CombatAttackHandler, mock_target_player: CombatParticipant
) -> None:
    """Test _apply_damage proceeds when connection_manager not available."""
    with patch("server.services.combat_attack_handler.get_config") as mock_get_config:
        mock_config: MagicMock = MagicMock()
        mock_app: MagicMock = MagicMock()
        mock_app_state: MagicMock = MagicMock()
        mock_app_state.connection_manager = None  # No connection manager
        mock_app.state = mock_app_state
        mock_config._app_instance = mock_app
        mock_get_config.return_value = mock_config
        # Should proceed with damage
        _ = attack_handler._apply_damage(mock_target_player, 20)
        assert mock_target_player.current_dp == 30  # Damage applied


def test_apply_damage_player_grace_period_error(
    attack_handler: CombatAttackHandler, mock_target_player: CombatParticipant
) -> None:
    """Test _apply_damage proceeds when grace period check fails."""
    with patch("server.services.combat_attack_handler.get_config", side_effect=Exception("Config error")):
        # Should proceed with damage despite error
        old_dp, _died, _mortally_wounded = attack_handler._apply_damage(mock_target_player, 20)

        assert old_dp == 50
        assert mock_target_player.current_dp == 30  # Damage applied


def test_apply_damage_player_no_death_room_caps_damage(
    attack_handler: CombatAttackHandler, mock_target_player: CombatParticipant
) -> None:
    """Test _apply_damage caps damage in no_death rooms so player DP never goes below 0."""
    mock_target_player.current_dp = 10
    mock_combat = CombatInstance()
    mock_combat.room_id = "tutorial_room_001"

    with patch("server.container.async_persistence_access.get_container_async_persistence") as mock_get_persist:
        mock_get_persist.return_value = _persistence_with_room_attributes({"no_death": True})

        old_dp, died, mortally_wounded = attack_handler._apply_damage(mock_target_player, 50, mock_combat)

        # Damage capped to 10 (only enough to bring to 0), no death
        assert old_dp == 10
        assert mock_target_player.current_dp == 0
        assert died is False
        assert mortally_wounded is True


def test_apply_damage_player_no_death_room_zero_damage_when_at_zero(
    attack_handler: CombatAttackHandler, mock_target_player: CombatParticipant
) -> None:
    """Test _apply_damage in no_death room when player already at 0 DP - no further damage."""
    mock_target_player.current_dp = 0
    mock_combat = CombatInstance()
    mock_combat.room_id = "tutorial_room_001"

    with patch("server.container.async_persistence_access.get_container_async_persistence") as mock_get_persist:
        mock_get_persist.return_value = _persistence_with_room_attributes({"no_death": True})

        old_dp, died, mortally_wounded = attack_handler._apply_damage(mock_target_player, 50, mock_combat)

        assert old_dp == 0
        assert mock_target_player.current_dp == 0
        assert died is False
        assert mortally_wounded is False


@pytest.mark.asyncio
async def test_apply_attack_damage(
    attack_handler: CombatAttackHandler, mock_combat: CombatInstance, mock_target_player: CombatParticipant
) -> None:
    """Test apply_attack_damage applies damage and updates combat."""
    with patch("server.container.async_persistence_access.get_container_async_persistence") as mock_get_persist:
        mock_get_persist.return_value = _persistence_with_room_attributes({})

        with patch.object(mock_combat, "update_activity") as update_activity:
            old_dp, died, mortally_wounded = await attack_handler.apply_attack_damage(
                mock_combat, mock_target_player, 20
            )

    assert old_dp == 50
    assert mock_target_player.current_dp == 30
    assert died is False
    assert mortally_wounded is False
    update_activity.assert_called_once_with(0)


@pytest.mark.asyncio
async def test_validate_and_get_combat_participants_success(
    attack_handler: CombatAttackHandler,
    mock_combat_service: MagicMock,
    mock_combat: CombatInstance,
    mock_attacker: CombatParticipant,
    mock_target_player: CombatParticipant,
) -> None:
    """Test validate_and_get_combat_participants returns participants."""
    attacker_id = mock_attacker.participant_id
    target_id = mock_target_player.participant_id
    mock_combat.participants = {attacker_id: mock_attacker, target_id: mock_target_player}
    _ = _bind_get_combat_by_participant(mock_combat_service, mock_combat)

    combat, attacker, target = await attack_handler.validate_and_get_combat_participants(attacker_id, target_id, False)

    assert combat == mock_combat
    assert attacker == mock_attacker
    assert target == mock_target_player


@pytest.mark.asyncio
async def test_validate_and_get_combat_participants_not_in_combat(
    attack_handler: CombatAttackHandler, mock_combat_service: MagicMock
) -> None:
    """Test validate_and_get_combat_participants raises when attacker not in combat."""
    attacker_id = uuid.uuid4()
    target_id = uuid.uuid4()
    _ = _bind_get_combat_by_participant(mock_combat_service, None)

    with pytest.raises(ValueError, match="not in combat"):
        _ = await attack_handler.validate_and_get_combat_participants(attacker_id, target_id, False)


@pytest.mark.asyncio
async def test_validate_and_get_combat_participants_inactive_combat(
    attack_handler: CombatAttackHandler, mock_combat_service: MagicMock, mock_combat: CombatInstance
) -> None:
    """Test validate_and_get_combat_participants raises when combat inactive."""
    attacker_id = uuid.uuid4()
    target_id = uuid.uuid4()
    mock_combat.status = CombatStatus.ENDED
    mock_combat.participants = {}
    _ = _bind_get_combat_by_participant(mock_combat_service, mock_combat)

    with pytest.raises(ValueError, match="not active"):
        _ = await attack_handler.validate_and_get_combat_participants(attacker_id, target_id, False)


@pytest.mark.asyncio
async def test_validate_and_get_combat_participants_target_not_found(
    attack_handler: CombatAttackHandler,
    mock_combat_service: MagicMock,
    mock_combat: CombatInstance,
    mock_attacker: CombatParticipant,
) -> None:
    """Test validate_and_get_combat_participants raises when target not in combat."""
    attacker_id = mock_attacker.participant_id
    target_id = uuid.uuid4()
    mock_combat.participants = {attacker_id: mock_attacker}
    _ = _bind_get_combat_by_participant(mock_combat_service, mock_combat)

    with pytest.raises(ValueError, match="not in this combat"):
        _ = await attack_handler.validate_and_get_combat_participants(attacker_id, target_id, False)


@pytest.mark.asyncio
async def test_validate_and_get_combat_participants_target_dead(
    attack_handler: CombatAttackHandler,
    mock_combat_service: MagicMock,
    mock_combat: CombatInstance,
    mock_attacker: CombatParticipant,
    mock_target_player: CombatParticipant,
) -> None:
    """Test validate_and_get_combat_participants raises when target is dead."""
    attacker_id = mock_attacker.participant_id
    target_id = mock_target_player.participant_id
    mock_target_player.current_dp = -10  # Dead for player (DP <= -10)
    mock_combat.participants = {attacker_id: mock_attacker, target_id: mock_target_player}
    _ = _bind_get_combat_by_participant(mock_combat_service, mock_combat)

    with pytest.raises(ValueError, match="already dead"):
        _ = await attack_handler.validate_and_get_combat_participants(attacker_id, target_id, False)


@pytest.mark.asyncio
async def test_validate_and_get_combat_participants_attacker_not_found(
    attack_handler: CombatAttackHandler,
    mock_combat_service: MagicMock,
    mock_combat: CombatInstance,
    mock_target_player: CombatParticipant,
) -> None:
    """Test validate_and_get_combat_participants raises when attacker not found."""
    attacker_id = uuid.uuid4()
    target_id = mock_target_player.participant_id
    mock_combat.participants = {target_id: mock_target_player}
    _ = _bind_get_combat_by_participant(mock_combat_service, mock_combat)

    with pytest.raises(ValueError, match="not found in combat"):
        _ = await attack_handler.validate_and_get_combat_participants(attacker_id, target_id, False)
