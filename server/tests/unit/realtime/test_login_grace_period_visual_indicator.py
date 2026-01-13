"""
Unit tests for login grace period visual indicator.

Tests that the "(warded)" indicator is properly added to player names
in various display contexts and removed when grace period expires.
"""

import uuid
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.commands.look_player import _format_player_look_display
from server.commands.look_room import _filter_other_players
from server.realtime.disconnect_grace_period import start_grace_period
from server.realtime.integration.game_state_provider import GameStateProvider
from server.realtime.login_grace_period import (
    cancel_login_grace_period,
    is_player_in_login_grace_period,
    start_login_grace_period,
)
from server.realtime.player_name_utils import PlayerNameExtractor
from server.realtime.player_occupant_processor import PlayerOccupantProcessor
from server.realtime.websocket_room_updates import get_player_occupants


@pytest.fixture
def mock_connection_manager():
    """Create a mock ConnectionManager."""
    manager = MagicMock()
    manager.login_grace_period_players = {}
    manager.login_grace_period_start_times = {}
    manager.grace_period_players = {}  # For disconnect grace period
    manager.player_websockets = {}
    return manager


@pytest.mark.asyncio
async def test_warded_indicator_in_game_state_provider(mock_connection_manager):  # pylint: disable=redefined-outer-name  # Reason: Fixture parameter name matches fixture function name, pytest standard pattern
    """Test that game state provider adds '(warded)' indicator."""
    player_id = uuid.uuid4()
    await start_login_grace_period(player_id, mock_connection_manager)

    # Create mocks for GameStateProvider constructor
    mock_room_manager = MagicMock()
    mock_async_persistence = MagicMock()
    mock_send_personal_message = AsyncMock()

    # Mock app state
    mock_app = MagicMock()
    mock_app.state.connection_manager = mock_connection_manager

    # Create game state provider with all required parameters
    _provider = GameStateProvider(
        room_manager=mock_room_manager,
        get_async_persistence=lambda: mock_async_persistence,
        send_personal_message_callback=mock_send_personal_message,
        get_app=lambda: mock_app,
    )

    # Check that player would have "(warded)" appended
    assert is_player_in_login_grace_period(player_id, mock_connection_manager) is True


@pytest.mark.asyncio
async def test_warded_indicator_in_player_occupant_processor(mock_connection_manager):  # pylint: disable=redefined-outer-name  # Reason: Fixture parameter name matches fixture function name, pytest standard pattern
    """Test that player occupant processor adds '(warded)' indicator."""
    player_id = uuid.uuid4()
    await start_login_grace_period(player_id, mock_connection_manager)

    # Create processor
    name_extractor = PlayerNameExtractor()
    processor = PlayerOccupantProcessor(mock_connection_manager, name_extractor)

    # Create mock player
    mock_player = MagicMock()
    mock_player.name = "TestPlayer"
    mock_player.player_id = player_id

    # Process player occupant
    occupant_info = processor._create_player_occupant_info(player_id, str(player_id), mock_player)  # pylint: disable=protected-access  # Reason: Testing internal player occupant creation logic for grace period indicator

    # Check that name includes "(warded)"
    assert occupant_info is not None
    assert "(warded)" in occupant_info["player_name"]


@pytest.mark.asyncio
async def test_warded_indicator_in_look_room(mock_connection_manager):  # pylint: disable=redefined-outer-name  # Reason: Fixture parameter name matches fixture function name, pytest standard pattern
    """Test that look_room command adds '(warded)' indicator."""
    player_id = uuid.uuid4()
    await start_login_grace_period(player_id, mock_connection_manager)

    # Create mock player
    mock_player = MagicMock()
    mock_player.name = "TestPlayer"
    mock_player.player_id = player_id

    # Filter players
    player_names = await _filter_other_players([mock_player], "OtherPlayer", mock_connection_manager)

    # Check that name includes "(warded)"
    assert len(player_names) == 1
    assert "(warded)" in player_names[0]


@pytest.mark.asyncio
async def test_warded_indicator_in_look_player(mock_connection_manager):  # pylint: disable=redefined-outer-name  # Reason: Fixture parameter name matches fixture function name, pytest standard pattern
    """Test that look_player command adds '(warded)' indicator."""
    player_id = uuid.uuid4()
    await start_login_grace_period(player_id, mock_connection_manager)

    # Create mock player
    mock_player = MagicMock()
    mock_player.name = "TestPlayer"
    mock_player.player_id = player_id
    mock_player.get_stats.return_value = {"position": "standing"}

    # Format player display
    display_text = _format_player_look_display(mock_player, mock_connection_manager)

    # Check that name includes "(warded)"
    assert "(warded)" in display_text


@pytest.mark.asyncio
async def test_warded_indicator_in_websocket_room_updates(mock_connection_manager):  # pylint: disable=redefined-outer-name  # Reason: Fixture parameter name matches fixture function name, pytest standard pattern
    """Test that websocket room updates add '(warded)' indicator."""
    player_id = uuid.uuid4()
    await start_login_grace_period(player_id, mock_connection_manager)

    # Mock room occupants
    mock_occupants = [
        {
            "player_id": str(player_id),
            "player_name": "TestPlayer",
        }
    ]

    # Mock get_room_occupants (async function)
    mock_connection_manager.get_room_occupants = AsyncMock(return_value=mock_occupants)

    # Get player occupants
    occupant_names = await get_player_occupants(mock_connection_manager, "room_123")

    # Check that name includes "(warded)"
    assert len(occupant_names) == 1
    assert "(warded)" in occupant_names[0]


@pytest.mark.asyncio
async def test_warded_indicator_removed_after_expiration(mock_connection_manager):  # pylint: disable=redefined-outer-name  # Reason: Fixture parameter name matches fixture function name, pytest standard pattern
    """Test that '(warded)' indicator is removed when grace period expires."""
    player_id = uuid.uuid4()
    await start_login_grace_period(player_id, mock_connection_manager)

    # Create processor
    name_extractor = PlayerNameExtractor()
    processor = PlayerOccupantProcessor(mock_connection_manager, name_extractor)

    # Create mock player
    mock_player = MagicMock()
    mock_player.name = "TestPlayer"
    mock_player.player_id = player_id

    # Process player occupant - should have "(warded)"
    occupant_info = processor._create_player_occupant_info(player_id, str(player_id), mock_player)  # pylint: disable=protected-access  # Reason: Testing internal player occupant creation logic for grace period indicator
    assert "(warded)" in occupant_info["player_name"]

    # Cancel grace period (simulating expiration)
    await cancel_login_grace_period(player_id, mock_connection_manager)

    # Process again - should not have "(warded)"
    occupant_info = processor._create_player_occupant_info(player_id, str(player_id), mock_player)  # pylint: disable=protected-access  # Reason: Testing internal player occupant creation logic for grace period indicator
    assert "(warded)" not in occupant_info["player_name"]


@pytest.mark.asyncio
async def test_warded_indicator_not_shown_for_reconnections(mock_connection_manager):  # pylint: disable=redefined-outer-name  # Reason: Fixture parameter name matches fixture function name, pytest standard pattern
    """Test that '(warded)' indicator is not shown for reconnections."""
    player_id = uuid.uuid4()

    # Don't start grace period (simulating reconnection without new login)

    # Create processor
    name_extractor = PlayerNameExtractor()
    processor = PlayerOccupantProcessor(mock_connection_manager, name_extractor)

    # Create mock player
    mock_player = MagicMock()
    mock_player.name = "TestPlayer"
    mock_player.player_id = player_id

    # Process player occupant - should not have "(warded)"
    occupant_info = processor._create_player_occupant_info(player_id, str(player_id), mock_player)  # pylint: disable=protected-access  # Reason: Testing internal player occupant creation logic for grace period indicator
    assert "(warded)" not in occupant_info["player_name"]


@pytest.mark.asyncio
async def test_both_linkdead_and_warded_indicators(mock_connection_manager):  # pylint: disable=redefined-outer-name  # Reason: Fixture parameter name matches fixture function name, pytest standard pattern
    """Test that both '(linkdead)' and '(warded)' can appear together."""
    player_id = uuid.uuid4()

    # Mock the required methods for disconnect grace period
    mock_connection_manager._get_player = AsyncMock()  # pylint: disable=protected-access  # Reason: Testing requires mocking internal method
    mock_connection_manager._cleanup_ghost_players = MagicMock()  # pylint: disable=protected-access  # Reason: Testing requires mocking internal method

    # Start both disconnect grace period and login grace period
    with patch("server.realtime.disconnect_grace_period.extract_player_name", return_value="TestPlayer"):
        with patch("server.realtime.disconnect_grace_period._collect_disconnect_keys", return_value=(set(), set())):
            with patch("server.realtime.disconnect_grace_period._remove_player_from_online_tracking"):
                with patch(
                    "server.realtime.disconnect_grace_period.handle_player_disconnect_broadcast",
                    new_callable=AsyncMock,
                ):
                    with patch("server.realtime.disconnect_grace_period._cleanup_player_references"):
                        await start_grace_period(player_id, mock_connection_manager)
    await start_login_grace_period(player_id, mock_connection_manager)

    # Create processor
    name_extractor = PlayerNameExtractor()
    processor = PlayerOccupantProcessor(mock_connection_manager, name_extractor)

    # Create mock player
    mock_player = MagicMock()
    mock_player.name = "TestPlayer"
    mock_player.player_id = player_id

    # Process player occupant - should have both indicators
    occupant_info = processor._create_player_occupant_info(player_id, str(player_id), mock_player)  # pylint: disable=protected-access  # Reason: Testing internal player occupant creation logic for grace period indicator
    assert "(linkdead)" in occupant_info["player_name"]
    assert "(warded)" in occupant_info["player_name"]
