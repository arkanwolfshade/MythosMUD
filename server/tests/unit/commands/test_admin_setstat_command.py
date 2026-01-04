"""
Unit tests for admin set stat command handler.

Tests the admin set command handler function.
"""

import uuid
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.commands.admin_setstat_command import _handle_admin_set_stat_command


@pytest.mark.asyncio
async def test_handle_admin_set_stat_command_success_str():
    """Test successful setting of STR stat."""
    mock_request = MagicMock()
    mock_app = MagicMock()
    mock_state = MagicMock()
    mock_user_manager = MagicMock()
    mock_user_manager.is_admin = MagicMock(return_value=True)
    mock_player_service = AsyncMock()
    mock_persistence = AsyncMock()
    mock_current_player = MagicMock()
    mock_current_player.id = uuid.uuid4()
    mock_target_player = MagicMock()
    mock_target_player.player_id = uuid.uuid4()
    mock_target_player.get_stats = MagicMock(return_value={"strength": 50, "constitution": 50, "size": 50, "power": 50})
    mock_target_player.set_stats = MagicMock()
    mock_player_service.resolve_player_name = AsyncMock(side_effect=[mock_current_player, mock_target_player])
    mock_persistence.get_player_by_name = AsyncMock(return_value=mock_target_player)
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
    mock_target_player.set_stats.assert_called_once()
    mock_persistence.save_player.assert_called_once_with(mock_target_player)


@pytest.mark.asyncio
async def test_handle_admin_set_stat_command_success_all_stat_types():
    """Test successful setting of various stat types."""
    mock_request = MagicMock()
    mock_app = MagicMock()
    mock_state = MagicMock()
    mock_user_manager = MagicMock()
    mock_user_manager.is_admin = MagicMock(return_value=True)
    mock_player_service = AsyncMock()
    mock_persistence = AsyncMock()
    mock_current_player = MagicMock()
    mock_current_player.id = uuid.uuid4()
    mock_target_player = MagicMock()
    mock_target_player.player_id = uuid.uuid4()
    mock_target_player.get_stats = MagicMock(
        return_value={
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
    )
    mock_target_player.set_stats = MagicMock()

    # Use return_value instead of side_effect so it can be called multiple times
    async def resolve_player_side_effect(name):
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

    # Test various stat types
    test_cases = [
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

    for stat_input, value in test_cases:
        mock_target_player.get_stats = MagicMock(
            return_value={
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
        )
        mock_target_player.set_stats = MagicMock()

        result = await _handle_admin_set_stat_command(
            {"args": [stat_input, "TargetPlayer", str(value)]},
            {"name": "AdminPlayer"},
            mock_request,
            None,
            "AdminPlayer",
        )

        assert "result" in result
        assert "Set TargetPlayer's" in result["result"]
        mock_target_player.set_stats.assert_called_once()


@pytest.mark.asyncio
async def test_handle_admin_set_stat_command_invalid_stat_name():
    """Test invalid stat name handling."""
    mock_request = MagicMock()
    mock_app = MagicMock()
    mock_state = MagicMock()
    mock_user_manager = MagicMock()
    mock_user_manager.is_admin = MagicMock(return_value=True)
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
    mock_user_manager.is_admin = MagicMock(return_value=True)
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
    mock_user_manager.is_admin = MagicMock(return_value=True)
    mock_player_service = AsyncMock()
    mock_persistence = AsyncMock()
    mock_current_player = MagicMock()
    mock_current_player.id = uuid.uuid4()
    mock_target_player = MagicMock()
    mock_target_player.player_id = uuid.uuid4()
    mock_target_player.get_stats = MagicMock(return_value={"strength": 50})
    mock_target_player.set_stats = MagicMock()

    async def resolve_player_side_effect(name):
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
    mock_target_player.set_stats.assert_called_once()

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
    mock_user_manager.is_admin = MagicMock(return_value=True)
    mock_player_service = AsyncMock()
    mock_persistence = AsyncMock()
    mock_current_player = MagicMock()
    mock_current_player.id = uuid.uuid4()
    mock_target_player = MagicMock()
    mock_target_player.player_id = uuid.uuid4()
    # CON=50, SIZ=50, max_dp = (50+50)//5 = 20
    mock_target_player.get_stats = MagicMock(return_value={"current_dp": 20, "constitution": 50, "size": 50})
    mock_target_player.set_stats = MagicMock()
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
    mock_target_player.set_stats.assert_called_once()


@pytest.mark.asyncio
async def test_handle_admin_set_stat_command_mp_above_maximum():
    """Test MP above maximum (warn but allow)."""
    mock_request = MagicMock()
    mock_app = MagicMock()
    mock_state = MagicMock()
    mock_user_manager = MagicMock()
    mock_user_manager.is_admin = MagicMock(return_value=True)
    mock_player_service = AsyncMock()
    mock_persistence = AsyncMock()
    mock_current_player = MagicMock()
    mock_current_player.id = uuid.uuid4()
    mock_target_player = MagicMock()
    mock_target_player.player_id = uuid.uuid4()
    # POW=50, max_mp = ceil(50 * 0.2) = 10
    mock_target_player.get_stats = MagicMock(return_value={"magic_points": 10, "power": 50})
    mock_target_player.set_stats = MagicMock()
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
    mock_target_player.set_stats.assert_called_once()


@pytest.mark.asyncio
async def test_handle_admin_set_stat_command_non_admin_denied():
    """Test non-admin user is denied."""
    mock_request = MagicMock()
    mock_app = MagicMock()
    mock_state = MagicMock()
    mock_user_manager = MagicMock()
    mock_user_manager.is_admin = MagicMock(return_value=False)
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
    mock_user_manager.is_admin = MagicMock(return_value=True)
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


@pytest.mark.asyncio
async def test_handle_admin_set_stat_command_case_insensitive_stat_names():
    """Test case-insensitive stat name handling."""
    mock_request = MagicMock()
    mock_app = MagicMock()
    mock_state = MagicMock()
    mock_user_manager = MagicMock()
    mock_user_manager.is_admin = MagicMock(return_value=True)
    mock_player_service = AsyncMock()
    mock_persistence = AsyncMock()
    mock_current_player = MagicMock()
    mock_current_player.id = uuid.uuid4()
    mock_target_player = MagicMock()
    mock_target_player.player_id = uuid.uuid4()
    mock_target_player.get_stats = MagicMock(return_value={"strength": 50})
    mock_target_player.set_stats = MagicMock()

    async def resolve_player_side_effect(name):
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

    # Test lowercase
    result = await _handle_admin_set_stat_command(
        {"args": ["str", "TargetPlayer", "60"]}, {"name": "AdminPlayer"}, mock_request, None, "AdminPlayer"
    )

    assert "result" in result
    assert "Set TargetPlayer's str" in result["result"]

    # Test uppercase
    mock_target_player.get_stats = MagicMock(return_value={"strength": 60})
    mock_target_player.set_stats = MagicMock()
    result = await _handle_admin_set_stat_command(
        {"args": ["STR", "TargetPlayer", "65"]}, {"name": "AdminPlayer"}, mock_request, None, "AdminPlayer"
    )

    assert "result" in result
    assert "Set TargetPlayer's STR" in result["result"]

    # Test full name
    mock_target_player.get_stats = MagicMock(return_value={"strength": 65})
    mock_target_player.set_stats = MagicMock()
    result = await _handle_admin_set_stat_command(
        {"args": ["strength", "TargetPlayer", "70"]}, {"name": "AdminPlayer"}, mock_request, None, "AdminPlayer"
    )

    assert "result" in result
    assert "Set TargetPlayer's strength" in result["result"]


@pytest.mark.asyncio
async def test_handle_admin_set_stat_command_no_app_context():
    """Test handling when app context is not available."""
    mock_request = MagicMock()
    mock_request.app = None

    result = await _handle_admin_set_stat_command(
        {"args": ["STR", "TargetPlayer", "75"]}, {"name": "AdminPlayer"}, mock_request, None, "AdminPlayer"
    )

    assert "result" in result
    assert "not available" in result["result"]


@pytest.mark.asyncio
async def test_handle_admin_set_stat_command_no_user_manager():
    """Test handling when user manager is not available."""
    mock_request = MagicMock()
    mock_app = MagicMock()
    mock_state = MagicMock()
    mock_state.user_manager = None
    mock_app.state = mock_state
    mock_request.app = mock_app

    result = await _handle_admin_set_stat_command(
        {"args": ["STR", "TargetPlayer", "75"]}, {"name": "AdminPlayer"}, mock_request, None, "AdminPlayer"
    )

    assert "result" in result
    assert "not available" in result["result"]


@pytest.mark.asyncio
async def test_handle_admin_set_stat_command_no_player_service():
    """Test handling when player service is not available."""
    mock_request = MagicMock()
    mock_app = MagicMock()
    mock_state = MagicMock()
    mock_user_manager = MagicMock()
    mock_state.user_manager = mock_user_manager
    mock_state.player_service = None
    mock_app.state = mock_state
    mock_request.app = mock_app

    result = await _handle_admin_set_stat_command(
        {"args": ["STR", "TargetPlayer", "75"]}, {"name": "AdminPlayer"}, mock_request, None, "AdminPlayer"
    )

    assert "result" in result
    assert "not available" in result["result"]


@pytest.mark.asyncio
async def test_handle_admin_set_stat_command_no_persistence():
    """Test handling when persistence layer is not available."""
    mock_request = MagicMock()
    mock_app = MagicMock()
    mock_state = MagicMock()
    mock_user_manager = MagicMock()
    mock_user_manager.is_admin = MagicMock(return_value=True)
    mock_player_service = AsyncMock()
    mock_current_player = MagicMock()
    mock_current_player.id = uuid.uuid4()
    mock_player_service.resolve_player_name = AsyncMock(return_value=mock_current_player)
    mock_state.user_manager = mock_user_manager
    mock_state.player_service = mock_player_service
    mock_state.persistence = None
    mock_app.state = mock_state
    mock_request.app = mock_app

    result = await _handle_admin_set_stat_command(
        {"args": ["STR", "TargetPlayer", "75"]}, {"name": "AdminPlayer"}, mock_request, None, "AdminPlayer"
    )

    assert "result" in result
    assert "not available" in result["result"]


@pytest.mark.asyncio
@patch("server.commands.admin_setstat_command.get_admin_actions_logger")
async def test_handle_admin_set_stat_command_logging(mock_get_logger):
    """Test admin action logging."""
    mock_request = MagicMock()
    mock_app = MagicMock()
    mock_state = MagicMock()
    mock_user_manager = MagicMock()
    mock_user_manager.is_admin = MagicMock(return_value=True)
    mock_player_service = AsyncMock()
    mock_persistence = AsyncMock()
    mock_admin_logger = MagicMock()
    mock_get_logger.return_value = mock_admin_logger
    mock_current_player = MagicMock()
    mock_current_player.id = uuid.uuid4()
    mock_target_player = MagicMock()
    mock_target_player.player_id = uuid.uuid4()
    mock_target_player.get_stats = MagicMock(return_value={"strength": 50})
    mock_target_player.set_stats = MagicMock()
    mock_player_service.resolve_player_name = AsyncMock(side_effect=[mock_current_player, mock_target_player])
    mock_persistence.get_player_by_name = AsyncMock(return_value=mock_target_player)
    mock_state.user_manager = mock_user_manager
    mock_state.player_service = mock_player_service
    mock_state.persistence = mock_persistence
    mock_app.state = mock_state
    mock_request.app = mock_app

    await _handle_admin_set_stat_command(
        {"args": ["STR", "TargetPlayer", "75"]}, {"name": "AdminPlayer"}, mock_request, None, "AdminPlayer"
    )

    mock_admin_logger.log_admin_command.assert_called_once()
    call_args = mock_admin_logger.log_admin_command.call_args
    assert call_args[1]["admin_name"] == "AdminPlayer"
    assert "admin set STR TargetPlayer 75" in call_args[1]["command"]
    assert call_args[1]["success"] is True
    assert "target_player" in call_args[1]["additional_data"]
    assert "stat_name" in call_args[1]["additional_data"]
    assert "old_value" in call_args[1]["additional_data"]
    assert "new_value" in call_args[1]["additional_data"]
