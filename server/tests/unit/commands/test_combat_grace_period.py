"""
Unit tests for combat command blocking during login grace period.

Tests that combat commands are properly blocked when players
are in login grace period.
"""

import uuid
from unittest.mock import AsyncMock, MagicMock

import pytest

# Lazy imports to avoid circular import issues
# Import inside functions that need them to avoid triggering circular import chain
from server.realtime.login_grace_period import (
    is_player_in_login_grace_period,
    start_login_grace_period,
)


@pytest.fixture
def mock_connection_manager():
    """Create a mock ConnectionManager."""
    manager = MagicMock()
    manager.login_grace_period_players = {}
    manager.login_grace_period_start_times = {}
    return manager


@pytest.fixture
def mock_persistence():
    """Create a mock persistence layer."""
    persistence = MagicMock()
    persistence.get_player_by_name = AsyncMock()
    return persistence


@pytest.fixture
def mock_request(mock_connection_manager, mock_persistence):  # pylint: disable=redefined-outer-name
    """Create a mock FastAPI request."""
    request = MagicMock()
    app = MagicMock()
    app.state.connection_manager = mock_connection_manager
    app.state.persistence = mock_persistence
    # CombatCommandHandler also needs async_persistence
    mock_async_persistence = AsyncMock()
    mock_async_persistence.get_player_by_name = AsyncMock()
    app.state.async_persistence = mock_async_persistence
    request.app = app
    return request


@pytest.mark.asyncio
async def test_attack_command_blocked_during_grace_period(mock_request, mock_connection_manager):  # pylint: disable=redefined-outer-name
    """Test that attack commands are blocked during login grace period."""
    player_id = uuid.uuid4()
    player_name = "TestPlayer"
    mock_player = MagicMock()
    mock_player.player_id = player_id
    persistence = mock_request.app.state.persistence
    persistence.get_player_by_name = AsyncMock(return_value=mock_player)
    # Also set async_persistence (though combat.py uses persistence)
    async_persistence = mock_request.app.state.async_persistence
    async_persistence.get_player_by_name = AsyncMock(return_value=mock_player)

    # Start grace period
    await start_login_grace_period(player_id, mock_connection_manager)

    # Lazy import to avoid circular import
    from server.commands.combat import CombatCommandHandler  # noqa: E402

    # Create command handler with async_persistence
    handler = CombatCommandHandler(async_persistence=async_persistence)

    # Try to execute attack command
    command_data = {"command_type": "attack", "target_player": "TargetPlayer"}
    current_user = {"username": player_name}

    result = await handler.handle_attack_command(
        command_data=command_data,
        current_user=current_user,
        request=mock_request,
        alias_storage=None,
        player_name=player_name,
    )

    # Should be blocked with appropriate message
    assert "result" in result
    assert "warded" in result["result"].lower() or "protected" in result["result"].lower()
    assert "combat" in result["result"].lower()


@pytest.mark.asyncio
async def test_attack_command_allowed_after_grace_period(mock_request):  # pylint: disable=redefined-outer-name
    """Test that attack commands work normally after grace period expires."""
    player_id = uuid.uuid4()
    player_name = "TestPlayer"
    mock_player = MagicMock()
    mock_player.player_id = player_id
    persistence = mock_request.app.state.persistence
    persistence.get_player_by_name = AsyncMock(return_value=mock_player)
    async_persistence = mock_request.app.state.async_persistence
    async_persistence.get_player_by_name = AsyncMock(return_value=mock_player)

    # Don't start grace period - player should be able to attack

    # Lazy import to avoid circular import
    from server.commands.combat import CombatCommandHandler  # noqa: E402

    # Create command handler with async_persistence
    handler = CombatCommandHandler(async_persistence=async_persistence)

    # Try to execute attack command
    command_data = {"command_type": "attack", "target_player": "TargetPlayer"}
    current_user = {"username": player_name}

    # Mock the NPC combat service to allow the attack to proceed
    # The handler's npc_combat_service is created during initialization
    handler.npc_combat_service.handle_player_attack_on_npc = AsyncMock(return_value=True)

    # The command should proceed (we're just testing the grace period check)
    # In a real scenario, this would continue to combat logic
    result = await handler.handle_attack_command(
        command_data=command_data,
        current_user=current_user,
        request=mock_request,
        alias_storage=None,
        player_name=player_name,
    )

    # Should not be blocked by grace period
    # (may fail for other reasons, but not grace period)
    if "result" in result:
        assert "warded" not in result["result"].lower()
        assert "protected" not in result["result"].lower() or "combat" not in result["result"].lower()


@pytest.mark.asyncio
async def test_attack_command_works_when_not_in_grace_period(mock_request, mock_connection_manager):  # pylint: disable=redefined-outer-name
    """Test that attack commands work when player is not in grace period."""
    player_id = uuid.uuid4()
    player_name = "TestPlayer"
    mock_player = MagicMock()
    mock_player.player_id = player_id
    persistence = mock_request.app.state.persistence
    persistence.get_player_by_name = AsyncMock(return_value=mock_player)
    async_persistence = mock_request.app.state.async_persistence
    async_persistence.get_player_by_name = AsyncMock(return_value=mock_player)

    # Verify player is not in grace period
    assert is_player_in_login_grace_period(player_id, mock_connection_manager) is False

    # Lazy import to avoid circular import
    from server.commands.combat import CombatCommandHandler  # noqa: E402

    # Create command handler with async_persistence
    handler = CombatCommandHandler(async_persistence=async_persistence)

    # Try to execute attack command
    command_data = {"command_type": "attack", "target_player": "TargetPlayer"}
    current_user = {"username": player_name}

    # Mock the NPC combat service to allow the attack to proceed
    handler.npc_combat_service.handle_player_attack_on_npc = AsyncMock(return_value=True)

    # The command should not be blocked by grace period check
    # (it may fail for other reasons like target not found, but not grace period)
    result = await handler.handle_attack_command(
        command_data=command_data,
        current_user=current_user,
        request=mock_request,
        alias_storage=None,
        player_name=player_name,
    )

    # Should not contain grace period blocking message
    if "result" in result and isinstance(result["result"], str):
        assert "warded" not in result["result"].lower() or "cannot engage" not in result["result"].lower()
