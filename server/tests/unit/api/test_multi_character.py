"""
Unit tests for multi-character support API endpoints.

Tests character creation limits, soft deletion, and character selection.
"""

import uuid
from unittest.mock import AsyncMock, MagicMock, patch

import pytest
from fastapi import HTTPException

from server.api.players import delete_character, get_user_characters, select_character
from server.models.user import User


@pytest.fixture
def mock_user():
    """Create a mock user for testing."""
    user = MagicMock(spec=User)
    user.id = uuid.uuid4()
    user.username = "testuser"
    return user


@pytest.fixture
def mock_player_service():
    """Create a mock player service."""
    service = MagicMock()
    return service


@pytest.mark.asyncio
async def test_get_user_characters_success(mock_user, mock_player_service):
    """Test successful retrieval of user characters."""
    from server.schemas.player import PlayerRead

    mock_characters = [
        PlayerRead(
            id=uuid.uuid4(),
            user_id=mock_user.id,
            name="Character1",
            profession_id=1,
            level=5,
            stats={},
            inventory=[],
            status_effects=[],
            created_at=None,
            last_active=None,
        ),
        PlayerRead(
            id=uuid.uuid4(),
            user_id=mock_user.id,
            name="Character2",
            profession_id=2,
            level=3,
            stats={},
            inventory=[],
            status_effects=[],
            created_at=None,
            last_active=None,
        ),
    ]

    mock_player_service.get_user_characters = AsyncMock(return_value=mock_characters)

    with patch("server.api.players.PlayerServiceDep", return_value=mock_player_service):
        result = await get_user_characters(
            request=MagicMock(), current_user=mock_user, player_service=mock_player_service
        )

    assert len(result) == 2
    assert result[0].name == "Character1"
    assert result[1].name == "Character2"
    mock_player_service.get_user_characters.assert_called_once_with(mock_user.id)


@pytest.mark.asyncio
async def test_delete_character_success(mock_user, mock_player_service):
    """Test successful character deletion."""
    character_id = str(uuid.uuid4())

    mock_player_service.soft_delete_character = AsyncMock(return_value=(True, "Character deleted"))

    with patch("server.api.players.PlayerServiceDep", return_value=mock_player_service):
        result = await delete_character(
            character_id=character_id,
            request=MagicMock(),
            current_user=mock_user,
            player_service=mock_player_service,
        )

    assert result["success"] is True
    assert "deleted" in result["message"].lower()
    mock_player_service.soft_delete_character.assert_called_once()


@pytest.mark.asyncio
async def test_delete_character_not_found(mock_user, mock_player_service):
    """Test character deletion when character not found."""
    character_id = str(uuid.uuid4())

    mock_player_service.soft_delete_character = AsyncMock(return_value=(False, "Character not found"))

    with patch("server.api.players.PlayerServiceDep", return_value=mock_player_service):
        with pytest.raises(HTTPException) as exc_info:
            await delete_character(
                character_id=character_id,
                request=MagicMock(),
                current_user=mock_user,
                player_service=mock_player_service,
            )

    assert exc_info.value.status_code == 404


@pytest.mark.asyncio
async def test_select_character_success(mock_user):
    """Test successful character selection."""
    character_id = str(uuid.uuid4())

    from server.schemas.player import PlayerRead

    mock_character = PlayerRead(
        id=uuid.UUID(character_id),
        user_id=mock_user.id,
        name="TestCharacter",
        profession_id=1,
        level=5,
        stats={},
        inventory=[],
        status_effects=[],
        created_at=None,
        last_active=None,
    )

    mock_player_service = MagicMock()
    mock_player_service.get_player_by_id = AsyncMock(return_value=mock_character)

    mock_persistence = MagicMock()
    mock_player = MagicMock()
    mock_player.player_id = uuid.UUID(character_id)
    mock_player.user_id = mock_user.id
    mock_player.is_deleted = False
    mock_persistence.get_player_by_id = AsyncMock(return_value=mock_player)
    mock_persistence.get_async_persistence = MagicMock(return_value=mock_persistence)

    with (
        patch("server.api.players.PlayerServiceDep", return_value=mock_player_service),
        patch("server.api.players.get_async_persistence", return_value=mock_persistence),
    ):
        result = await select_character(
            request_data=MagicMock(character_id=character_id),
            request=MagicMock(),
            current_user=mock_user,
            player_service=mock_player_service,
        )

    assert result["name"] == "TestCharacter"
    assert str(result["id"]) == character_id


@pytest.mark.asyncio
async def test_select_character_disconnects_other_characters(mock_user):
    """Test that selecting a character disconnects other user characters."""
    character_id_1 = uuid.uuid4()
    character_id_2 = uuid.uuid4()

    from server.schemas.player import PlayerRead

    mock_character = PlayerRead(
        id=character_id_2,
        user_id=mock_user.id,
        name="TestCharacter2",
        profession_id=1,
        level=5,
        stats={},
        inventory=[],
        status_effects=[],
        created_at=None,
        last_active=None,
    )

    mock_player_service = MagicMock()
    mock_player_service.get_player_by_id = AsyncMock(return_value=mock_character)

    # Mock persistence with two characters
    mock_persistence = MagicMock()
    mock_player_1 = MagicMock()
    mock_player_1.player_id = character_id_1
    mock_player_1.user_id = mock_user.id
    mock_player_1.name = "TestCharacter1"
    mock_player_1.is_deleted = False

    mock_player_2 = MagicMock()
    mock_player_2.player_id = character_id_2
    mock_player_2.user_id = mock_user.id
    mock_player_2.name = "TestCharacter2"
    mock_player_2.is_deleted = False

    mock_persistence.get_player_by_id = AsyncMock(return_value=mock_player_2)
    mock_persistence.get_active_players_by_user_id = AsyncMock(return_value=[mock_player_1, mock_player_2])

    # Mock connection manager
    mock_connection_manager = MagicMock()
    mock_connection_manager.player_websockets = {character_id_1: ["conn1", "conn2"]}
    mock_connection_manager.disconnect_websocket = AsyncMock()

    # Mock request with connection manager
    mock_request = MagicMock()
    mock_container = MagicMock()
    mock_container.connection_manager = mock_connection_manager
    mock_request.app.state.container = mock_container

    with (
        patch("server.api.players.PlayerServiceDep", return_value=mock_player_service),
        patch("server.api.players.get_async_persistence", return_value=mock_persistence),
    ):
        result = await select_character(
            request_data=MagicMock(character_id=str(character_id_2)),
            request=mock_request,
            current_user=mock_user,
            player_service=mock_player_service,
        )

    # Verify character 1 was disconnected
    mock_connection_manager.disconnect_websocket.assert_called_once_with(character_id_1, is_force_disconnect=True)

    # Verify character 2 was selected
    assert result["name"] == "TestCharacter2"
    assert str(result["id"]) == str(character_id_2)


@pytest.mark.asyncio
async def test_select_character_no_other_connections(mock_user):
    """Test character selection when user has no other active connections."""
    character_id = uuid.uuid4()

    from server.schemas.player import PlayerRead

    mock_character = PlayerRead(
        id=character_id,
        user_id=mock_user.id,
        name="TestCharacter",
        profession_id=1,
        level=5,
        stats={},
        inventory=[],
        status_effects=[],
        created_at=None,
        last_active=None,
    )

    mock_player_service = MagicMock()
    mock_player_service.get_player_by_id = AsyncMock(return_value=mock_character)

    mock_persistence = MagicMock()
    mock_player = MagicMock()
    mock_player.player_id = character_id
    mock_player.user_id = mock_user.id
    mock_player.is_deleted = False
    mock_persistence.get_player_by_id = AsyncMock(return_value=mock_player)
    mock_persistence.get_active_players_by_user_id = AsyncMock(return_value=[mock_player])

    # Mock connection manager with no active connections
    mock_connection_manager = MagicMock()
    mock_connection_manager.player_websockets = {}

    mock_request = MagicMock()
    mock_container = MagicMock()
    mock_container.connection_manager = mock_connection_manager
    mock_request.app.state.container = mock_container

    with (
        patch("server.api.players.PlayerServiceDep", return_value=mock_player_service),
        patch("server.api.players.get_async_persistence", return_value=mock_persistence),
    ):
        result = await select_character(
            request_data=MagicMock(character_id=str(character_id)),
            request=mock_request,
            current_user=mock_user,
            player_service=mock_player_service,
        )

    # Verify no disconnection was attempted (no other connections)
    mock_connection_manager.disconnect_websocket.assert_not_called()

    # Verify character was selected
    assert result["name"] == "TestCharacter"
    assert str(result["id"]) == str(character_id)
