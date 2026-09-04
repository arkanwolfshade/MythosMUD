"""
Unit tests for admin set stat command handler.

Tests the admin set command handler function.
"""

# pyright: reportPrivateUsage=false
# Reason: Unit tests intentionally call admin_setstat_command private helpers.

import uuid
from unittest.mock import AsyncMock, MagicMock

import pytest

from server.commands.admin_setstat_command import _handle_admin_set_stat_command

_BASELINE_STATS: dict[str, int] = {
    "strength": 50,
    "constitution": 50,
    "intelligence": 50,
    "education": 50,
    "luck": 50,
    "dexterity": 50,
    "size": 50,
    "power": 50,
    "charisma": 50,
    "current_dp": 20,
    "magic_points": 10,
    "lucidity": 100,
    "occult": 0,
    "corruption": 0,
}

_ALL_STAT_TYPE_CASES: list[tuple[str, int]] = [
    ("CON", 80),
    ("INT", 70),
    ("DEX", 65),
    ("EDU", 75),
    ("LUCK", 60),
    ("SIZ", 55),
    ("POW", 85),
    ("CHA", 90),
    ("DP", 25),
    ("MP", 15),
    ("LCD", 85),
    ("Occult", 25),
    ("Corruption", 15),
]


def _make_all_stat_types_harness() -> tuple[MagicMock, MagicMock, MagicMock]:
    """Build request/target/apply_dp mocks for the all-stat-types success path."""
    request: MagicMock = MagicMock()
    app: MagicMock = MagicMock()
    state: MagicMock = MagicMock()
    user_manager: MagicMock = MagicMock()
    user_manager.is_admin = AsyncMock(return_value=True)
    player_service: AsyncMock = AsyncMock()
    persistence: AsyncMock = AsyncMock()
    current: MagicMock = MagicMock()
    current.id = uuid.uuid4()
    target: MagicMock = MagicMock()
    target.player_id = uuid.uuid4()
    target.get_stats = MagicMock(return_value=dict(_BASELINE_STATS))
    apply_dp: MagicMock = MagicMock(return_value=(25, False, False))
    target.apply_dp_change = apply_dp

    async def resolve(name: str) -> MagicMock:
        return current if name == "AdminPlayer" else target

    player_service.resolve_player_name = AsyncMock(side_effect=resolve)
    persistence.get_player_by_name = AsyncMock(return_value=target)
    state.user_manager = user_manager
    state.player_service = player_service
    state.persistence = persistence
    state.connection_manager = None
    app.state = state
    request.app = app
    return request, target, apply_dp


def _assert_stat_write_path(stat_input: str, value: int, set_stats: MagicMock, apply_dp: MagicMock) -> None:
    if stat_input == "DP":
        apply_dp.assert_called_once_with(value)
        set_stats.assert_not_called()
    else:
        set_stats.assert_called_once()
        apply_dp.assert_not_called()
    set_stats.reset_mock()
    apply_dp.reset_mock()


@pytest.mark.asyncio
async def test_handle_admin_set_stat_command_success_str():
    """Test successful setting of STR stat."""
    mock_request = MagicMock()
    mock_app = MagicMock()
    mock_state = MagicMock()
    mock_user_manager = MagicMock()
    mock_user_manager.is_admin = AsyncMock(return_value=True)
    mock_player_service = AsyncMock()
    mock_persistence = AsyncMock()
    mock_current_player = MagicMock()
    mock_current_player.id = uuid.uuid4()
    mock_target_player = MagicMock()
    mock_target_player.player_id = uuid.uuid4()
    mock_target_player.get_stats = MagicMock(return_value={"strength": 50, "constitution": 50, "size": 50, "power": 50})
    set_stats: MagicMock = MagicMock()
    mock_target_player.set_stats = set_stats
    mock_player_service.resolve_player_name = AsyncMock(side_effect=[mock_current_player, mock_target_player])
    mock_persistence.get_player_by_name = AsyncMock(return_value=mock_target_player)
    save_player: AsyncMock = AsyncMock()
    mock_persistence.save_player = save_player
    mock_state.user_manager = mock_user_manager
    mock_state.player_service = mock_player_service
    mock_state.persistence = mock_persistence
    mock_app.state = mock_state
    mock_request.app = mock_app

    result = await _handle_admin_set_stat_command(
        {"args": ["STR", "TargetPlayer", "75"]}, {"name": "AdminPlayer"}, mock_request, None, "AdminPlayer"
    )

    assert "result" in result
    assert "Set TargetPlayer's STR from 50 to 75" in result["result"]
    set_stats.assert_called_once()
    save_player.assert_called_once_with(mock_target_player)


@pytest.mark.asyncio
async def test_handle_admin_set_stat_command_success_all_stat_types():
    """Test successful setting of various stat types."""
    request, target, apply_dp = _make_all_stat_types_harness()
    for stat_input, value in _ALL_STAT_TYPE_CASES:
        target.get_stats = MagicMock(return_value=dict(_BASELINE_STATS))
        set_stats: MagicMock = MagicMock()
        target.set_stats = set_stats
        result = await _handle_admin_set_stat_command(
            {"args": [stat_input, "TargetPlayer", str(value)]},
            {"name": "AdminPlayer"},
            request,
            None,
            "AdminPlayer",
        )
        assert "result" in result
        assert "Set TargetPlayer's" in result["result"]
        _assert_stat_write_path(stat_input, value, set_stats, apply_dp)


@pytest.mark.asyncio
async def test_handle_admin_set_stat_command_invalid_stat_name():
    """Test invalid stat name handling."""
    mock_request = MagicMock()
    mock_app = MagicMock()
    mock_state = MagicMock()
    mock_user_manager = MagicMock()
    mock_user_manager.is_admin = AsyncMock(return_value=True)
    mock_player_service = AsyncMock()
    mock_current_player = MagicMock()
    mock_current_player.id = uuid.uuid4()
    mock_player_service.resolve_player_name = AsyncMock(return_value=mock_current_player)
    mock_state.user_manager = mock_user_manager
    mock_state.player_service = mock_player_service
    mock_app.state = mock_state
    mock_request.app = mock_app

    result = await _handle_admin_set_stat_command(
        {"args": ["INVALID", "TargetPlayer", "50"]}, {"name": "AdminPlayer"}, mock_request, None, "AdminPlayer"
    )

    assert "result" in result
    assert "Invalid stat name" in result["result"]
    assert "INVALID" in result["result"]


@pytest.mark.asyncio
async def test_handle_admin_set_stat_command_invalid_value():
    """Test invalid value (non-integer) handling."""
    mock_request = MagicMock()
    mock_app = MagicMock()
    mock_state = MagicMock()
    mock_user_manager = MagicMock()
    mock_user_manager.is_admin = AsyncMock(return_value=True)
    mock_player_service = AsyncMock()
    mock_current_player = MagicMock()
    mock_current_player.id = uuid.uuid4()
    mock_player_service.resolve_player_name = AsyncMock(return_value=mock_current_player)
    mock_state.user_manager = mock_user_manager
    mock_state.player_service = mock_player_service
    mock_app.state = mock_state
    mock_request.app = mock_app

    result = await _handle_admin_set_stat_command(
        {"args": ["STR", "TargetPlayer", "abc"]}, {"name": "AdminPlayer"}, mock_request, None, "AdminPlayer"
    )

    assert "result" in result
    assert "Invalid value" in result["result"]
    assert "abc" in result["result"]


@pytest.mark.asyncio
async def test_handle_admin_set_stat_command_value_out_of_range():
    """Test value out of range (warn but allow)."""
    mock_request = MagicMock()
    mock_app = MagicMock()
    mock_state = MagicMock()
    mock_user_manager = MagicMock()
    mock_user_manager.is_admin = AsyncMock(return_value=True)
    mock_player_service = AsyncMock()
    mock_persistence = AsyncMock()
    mock_current_player = MagicMock()
    mock_current_player.id = uuid.uuid4()
    mock_target_player = MagicMock()
    mock_target_player.player_id = uuid.uuid4()
    mock_target_player.get_stats = MagicMock(return_value={"strength": 50})
    set_stats: MagicMock = MagicMock()
    mock_target_player.set_stats = set_stats

    async def resolve_player_side_effect(name: str):
        if name == "AdminPlayer":
            return mock_current_player
        return mock_target_player

    mock_player_service.resolve_player_name = AsyncMock(side_effect=resolve_player_side_effect)
    mock_persistence.get_player_by_name = AsyncMock(return_value=mock_target_player)
    mock_state.user_manager = mock_user_manager
    mock_state.player_service = mock_player_service
    mock_state.persistence = mock_persistence
    mock_app.state = mock_state
    mock_request.app = mock_app

    # Test value above range
    result = await _handle_admin_set_stat_command(
        {"args": ["STR", "TargetPlayer", "150"]}, {"name": "AdminPlayer"}, mock_request, None, "AdminPlayer"
    )

    assert "result" in result
    assert "Set TargetPlayer's STR" in result["result"]
    assert "Warning" in result["result"]
    assert "outside normal range" in result["result"]
    set_stats.assert_called_once()

    # Test value below range
    mock_target_player.get_stats = MagicMock(return_value={"strength": 50})
    mock_target_player.set_stats = MagicMock()
    result = await _handle_admin_set_stat_command(
        {"args": ["STR", "TargetPlayer", "-10"]}, {"name": "AdminPlayer"}, mock_request, None, "AdminPlayer"
    )

    assert "result" in result
    assert "Set TargetPlayer's STR" in result["result"]
    assert "Warning" in result["result"]


@pytest.mark.asyncio
async def test_handle_admin_set_stat_command_dp_above_maximum():
    """Test DP above maximum (warn but allow)."""
    mock_request = MagicMock()
    mock_app = MagicMock()
    mock_state = MagicMock()
    mock_user_manager = MagicMock()
    mock_user_manager.is_admin = AsyncMock(return_value=True)
    mock_player_service = AsyncMock()
    mock_persistence = AsyncMock()
    mock_current_player = MagicMock()
    mock_current_player.id = uuid.uuid4()
    mock_target_player = MagicMock()
    mock_target_player.player_id = uuid.uuid4()
    # CON=50, SIZ=50, max_dp = (50+50)//5 = 20
    mock_target_player.get_stats = MagicMock(return_value={"current_dp": 20, "constitution": 50, "size": 50})
    set_stats: MagicMock = MagicMock()
    mock_target_player.set_stats = set_stats
    apply_dp_change: MagicMock = MagicMock(return_value=(25, False, False))
    mock_target_player.apply_dp_change = apply_dp_change
    mock_player_service.resolve_player_name = AsyncMock(side_effect=[mock_current_player, mock_target_player])
    mock_persistence.get_player_by_name = AsyncMock(return_value=mock_target_player)
    mock_state.user_manager = mock_user_manager
    mock_state.player_service = mock_player_service
    mock_state.persistence = mock_persistence
    mock_app.state = mock_state
    mock_request.app = mock_app

    result = await _handle_admin_set_stat_command(
        {"args": ["DP", "TargetPlayer", "25"]}, {"name": "AdminPlayer"}, mock_request, None, "AdminPlayer"
    )

    assert "result" in result
    assert "Set TargetPlayer's DP" in result["result"]
    assert "Warning" in result["result"]
    assert "exceeds calculated maximum" in result["result"]
    apply_dp_change.assert_called_once_with(25)
    set_stats.assert_not_called()


@pytest.mark.asyncio
async def test_handle_admin_set_stat_command_mp_above_maximum():
    """Test MP above maximum (warn but allow)."""
    mock_request = MagicMock()
    mock_app = MagicMock()
    mock_state = MagicMock()
    mock_user_manager = MagicMock()
    mock_user_manager.is_admin = AsyncMock(return_value=True)
    mock_player_service = AsyncMock()
    mock_persistence = AsyncMock()
    mock_current_player = MagicMock()
    mock_current_player.id = uuid.uuid4()
    mock_target_player = MagicMock()
    mock_target_player.player_id = uuid.uuid4()
    # POW=50, max_mp = ceil(50 * 0.2) = 10
    mock_target_player.get_stats = MagicMock(return_value={"magic_points": 10, "power": 50})
    set_stats: MagicMock = MagicMock()
    mock_target_player.set_stats = set_stats
    mock_player_service.resolve_player_name = AsyncMock(side_effect=[mock_current_player, mock_target_player])
    mock_persistence.get_player_by_name = AsyncMock(return_value=mock_target_player)
    mock_state.user_manager = mock_user_manager
    mock_state.player_service = mock_player_service
    mock_state.persistence = mock_persistence
    mock_app.state = mock_state
    mock_request.app = mock_app

    result = await _handle_admin_set_stat_command(
        {"args": ["MP", "TargetPlayer", "15"]}, {"name": "AdminPlayer"}, mock_request, None, "AdminPlayer"
    )

    assert "result" in result
    assert "Set TargetPlayer's MP" in result["result"]
    assert "Warning" in result["result"]
    assert "exceeds calculated maximum" in result["result"]
    set_stats.assert_called_once()


@pytest.mark.asyncio
async def test_handle_admin_set_stat_command_non_admin_denied():
    """Test non-admin user is denied."""
    mock_request = MagicMock()
    mock_app = MagicMock()
    mock_state = MagicMock()
    mock_user_manager = MagicMock()
    mock_user_manager.is_admin = AsyncMock(return_value=False)
    mock_player_service = AsyncMock()
    mock_current_player = MagicMock()
    mock_current_player.id = uuid.uuid4()
    mock_player_service.resolve_player_name = AsyncMock(return_value=mock_current_player)
    mock_state.user_manager = mock_user_manager
    mock_state.player_service = mock_player_service
    mock_app.state = mock_state
    mock_request.app = mock_app

    result = await _handle_admin_set_stat_command(
        {"args": ["STR", "TargetPlayer", "75"]}, {"name": "NonAdminPlayer"}, mock_request, None, "NonAdminPlayer"
    )

    assert "result" in result
    assert "permission" in result["result"].lower()


@pytest.mark.asyncio
async def test_handle_admin_set_stat_command_target_player_not_found():
    """Test target player not found handling."""
    mock_request = MagicMock()
    mock_app = MagicMock()
    mock_state = MagicMock()
    mock_user_manager = MagicMock()
    mock_user_manager.is_admin = AsyncMock(return_value=True)
    mock_player_service = AsyncMock()
    mock_persistence = AsyncMock()
    mock_current_player = MagicMock()
    mock_current_player.id = uuid.uuid4()
    mock_player_service.resolve_player_name = AsyncMock(side_effect=[mock_current_player, None])
    mock_persistence.get_player_by_name = AsyncMock(return_value=None)
    mock_state.user_manager = mock_user_manager
    mock_state.player_service = mock_player_service
    mock_state.persistence = mock_persistence
    mock_app.state = mock_state
    mock_request.app = mock_app

    result = await _handle_admin_set_stat_command(
        {"args": ["STR", "NonExistentPlayer", "75"]}, {"name": "AdminPlayer"}, mock_request, None, "AdminPlayer"
    )

    assert "result" in result
    assert "not found" in result["result"]
    assert "NonExistentPlayer" in result["result"]


@pytest.mark.asyncio
async def test_handle_admin_set_stat_command_missing_stat_name():
    """Test missing stat name handling."""
    mock_request = MagicMock()
    mock_app = MagicMock()
    mock_state = MagicMock()
    mock_state.user_manager = MagicMock()
    mock_app.state = mock_state
    mock_request.app = mock_app

    result = await _handle_admin_set_stat_command(
        {"args": ["", "TargetPlayer", "75"]}, {"name": "AdminPlayer"}, mock_request, None, "AdminPlayer"
    )

    assert "result" in result
    assert "Usage" in result["result"]


@pytest.mark.asyncio
async def test_handle_admin_set_stat_command_missing_target_player():
    """Test missing target player handling."""
    mock_request = MagicMock()
    mock_app = MagicMock()
    mock_state = MagicMock()
    mock_state.user_manager = MagicMock()
    mock_app.state = mock_state
    mock_request.app = mock_app

    result = await _handle_admin_set_stat_command(
        {"args": ["STR", "", "75"]}, {"name": "AdminPlayer"}, mock_request, None, "AdminPlayer"
    )

    assert "result" in result
    assert "Usage" in result["result"]


@pytest.mark.asyncio
async def test_handle_admin_set_stat_command_missing_value():
    """Test missing value handling."""
    mock_request = MagicMock()
    mock_app = MagicMock()
    mock_state = MagicMock()
    mock_state.user_manager = MagicMock()
    mock_app.state = mock_state
    mock_request.app = mock_app

    result = await _handle_admin_set_stat_command(
        {"args": ["STR", "TargetPlayer"]}, {"name": "AdminPlayer"}, mock_request, None, "AdminPlayer"
    )

    assert "result" in result
    assert "Usage" in result["result"]
