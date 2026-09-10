"""
Unit tests for hallucination-related additions to GameStateProvider (#625, #626, #714).

Split out of test_game_state_provider.py to keep that module under the project's
too-many-lines limit -- mirrors the existing split for test_websocket_room_updates_build_event.py.
"""

import uuid
from typing import cast
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.realtime.integration.game_state_provider import GameStateProvider


@pytest.fixture
def mock_room_manager() -> MagicMock:
    """Create a mock room manager."""
    return MagicMock()


@pytest.fixture
def mock_get_async_persistence() -> MagicMock:
    """Create a mock get_async_persistence callback."""
    return MagicMock(return_value=MagicMock())


@pytest.fixture
def mock_send_personal_message() -> AsyncMock:
    """Create a mock send_personal_message callback."""
    return AsyncMock(return_value={"success": True})


@pytest.fixture
def mock_get_app() -> MagicMock:
    """Create a mock get_app callback."""
    return MagicMock(return_value=MagicMock())


@pytest.fixture
def game_state_provider(
    mock_room_manager: MagicMock,
    mock_get_async_persistence: MagicMock,
    mock_send_personal_message: AsyncMock,
    mock_get_app: MagicMock,
) -> GameStateProvider:
    """Create a GameStateProvider instance."""
    return GameStateProvider(
        room_manager=mock_room_manager,
        get_async_persistence=mock_get_async_persistence,
        send_personal_message_callback=mock_send_personal_message,
        get_app=mock_get_app,
    )


def _wire_room(mock_get_async_persistence: MagicMock, mock_room_manager: MagicMock, room_id: str) -> None:
    """Wire the fixtures so send_initial_game_state resolves a minimal, real room dict."""
    mock_room = MagicMock(to_dict=MagicMock(return_value={"id": room_id, "npcs": [], "players": []}))
    mock_persistence = MagicMock(get_room_by_id=MagicMock(return_value=mock_room))
    mock_get_async_persistence.return_value = mock_persistence
    mock_room_manager.get_room_occupants = AsyncMock(return_value=[])


@pytest.mark.asyncio
async def test_send_initial_game_state_includes_viewer_phantom(
    game_state_provider: GameStateProvider,
    mock_send_personal_message: AsyncMock,
    mock_get_async_persistence: MagicMock,
    mock_room_manager: MagicMock,
):
    """#625/#714: the game_state room payload includes this viewer's own active phantom."""
    player_id = uuid.uuid4()
    mock_player = MagicMock(current_room_id="room_001")
    room_id = "room_001"
    online_players: dict[uuid.UUID, dict[str, object]] = {}
    _wire_room(mock_get_async_persistence, mock_room_manager, room_id)

    with patch(
        "server.realtime.integration.game_state_provider.get_viewer_phantom_names",
        return_value=["Shambling Horror"],
    ):
        await game_state_provider.send_initial_game_state(player_id, mock_player, room_id, online_players)

    call = cast(tuple[object, ...], mock_send_personal_message.call_args.args)
    sent_event = cast(dict[str, object], call[1])
    data = cast(dict[str, object], sent_event["data"])
    room_data = cast(dict[str, object], data["room"])
    assert "Shambling Horror" in cast(list[object], room_data["npcs"])
    assert "Shambling Horror" in cast(list[object], data["occupants"])


@pytest.mark.asyncio
async def test_send_initial_game_state_hallucinates_exits_for_deranged_viewer(
    game_state_provider: GameStateProvider,
    mock_send_personal_message: AsyncMock,
    mock_get_async_persistence: MagicMock,
    mock_room_manager: MagicMock,
):
    """#626/#714: a deranged connecting player's initial game_state shows the seeded lie."""
    player_id = uuid.uuid4()
    mock_player = MagicMock(current_room_id="room_001")
    room_id = "room_001"
    online_players: dict[uuid.UUID, dict[str, object]] = {}
    _wire_room(mock_get_async_persistence, mock_room_manager, room_id)

    with (
        patch(
            "server.realtime.integration.game_state_provider.lucidity_tier_cache.is_deranged",
            return_value=True,
        ),
        patch(
            "server.realtime.integration.game_state_provider.get_hallucinated_exits",
            return_value=["east", "up"],
        ) as mock_get_hallucinated,
    ):
        await game_state_provider.send_initial_game_state(player_id, mock_player, room_id, online_players)

    mock_get_hallucinated.assert_called_once_with(room_id, str(player_id))
    call = cast(tuple[object, ...], mock_send_personal_message.call_args.args)
    sent_event = cast(dict[str, object], call[1])
    data = cast(dict[str, object], sent_event["data"])
    room_data = cast(dict[str, object], data["room"])
    assert room_data["exits"] == {"east": "?", "up": "?"}
