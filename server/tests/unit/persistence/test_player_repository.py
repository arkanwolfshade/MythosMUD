"""
Unit tests for player repository.

Tests the PlayerRepository class which handles player persistence operations.
Uses procedure-based persistence; mocks return rows compatible with row_to_player.
"""

import uuid
from datetime import UTC, datetime
from typing import Any
from unittest.mock import AsyncMock, MagicMock, patch

import pytest
from sqlalchemy.exc import SQLAlchemyError

from server.exceptions import DatabaseError
from server.models.player import Player
from server.models.room import Room
from server.persistence.repositories.player_repository import PlayerRepository

# pylint: disable=protected-access  # Reason: Test file - accessing protected members is standard practice for unit testing
# pylint: disable=redefined-outer-name  # Reason: Test file - pytest fixture parameter names must match fixture names, causing intentional redefinitions
# pylint: disable=too-many-lines  # Reason: Comprehensive test file for AsyncPersistenceLayer requires extensive test coverage across many scenarios


class _ScalarResult:
    """Minimal typed stand-in for the sqlalchemy Result returned by session.execute()
    when only .scalar() is used (the player_is_deleted guard read, #777). A bare
    MagicMock() types .scalar as Any; this keeps the mock's return type concrete."""

    def __init__(self, value: bool | None) -> None:
        self._value: bool | None = value

    def scalar(self) -> bool | None:
        return self._value


class _SessionCM:
    """Typed async context manager stand-in for `async with session_maker() as session:`.
    Avoids chaining through MagicMock.return_value (typed Any in typeshed) to wire up
    __aenter__/__aexit__ by hand."""

    def __init__(self, session: AsyncMock) -> None:
        self._session: AsyncMock = session

    async def __aenter__(self) -> AsyncMock:
        return self._session

    async def __aexit__(self, *_args: object) -> None:
        return None


def _session_maker_double(session: AsyncMock) -> MagicMock:
    """Build the `session_maker` callable that `get_session_maker()` returns: calling it
    (`session_maker()`) returns the async context manager over `session`. Assigned
    wholesale to `mock_get_session.return_value` so callers never need to read an
    Any-typed Mock attribute to chain further setup."""
    return MagicMock(return_value=_SessionCM(session))


def _make_mock_row(
    player_id: uuid.UUID | None = None,
    user_id: uuid.UUID | None = None,
    name: str = "TestPlayer",
) -> MagicMock:
    """Create a mock procedure result row for row_to_player."""
    pid = player_id or uuid.uuid4()
    uid = user_id or uuid.uuid4()
    row = MagicMock()
    row.player_id = pid
    row.user_id = uid
    row.name = name
    row.inventory = "[]"
    row.status_effects = "[]"
    row.current_room_id = "earth_arkhamcity_sanitarium_room_foyer_001"
    row.respawn_room_id = "earth_arkhamcity_sanitarium_room_foyer_001"
    row.experience_points = 0
    row.level = 1
    row.is_admin = 0
    row.profession_id = None
    row.created_at = datetime.now(UTC)
    row.last_active = datetime.now(UTC)
    row.stats = {"current_dp": 20, "constitution": 50, "size": 50}
    row.is_deleted = False
    row.deleted_at = None
    row.tutorial_instance_id = None
    row.inventory_json = "[]"
    row.equipped_json = "{}"
    return row


@pytest.fixture
def player_repository():
    """Create a PlayerRepository instance."""
    # Cache only checks key membership (player.current_room_id in room_cache); real Room
    # instances are cheap to build and keep the fixture correctly typed as dict[str, Room].
    room_cache = {
        "arkham_square": Room({"id": "arkham_square"}),
        "room1": Room({"id": "room1"}),
        "earth_arkhamcity_sanitarium_room_foyer_001": Room({"id": "earth_arkhamcity_sanitarium_room_foyer_001"}),
    }
    return PlayerRepository(room_cache=room_cache)


@pytest.fixture
def mock_player():
    """Create a mock player for save operations."""
    player = MagicMock(spec=Player)
    player.player_id = str(uuid.uuid4())
    player.user_id = str(uuid.uuid4())
    player.name = "TestPlayer"
    player.inventory = "[]"
    player.status_effects = "[]"
    player.current_room_id = "arkham_square"
    player.respawn_room_id = "arkham_square"
    player.experience_points = 0
    player.level = 1
    player.is_admin = 0
    player.profession_id = None
    player.created_at = datetime.now(UTC)
    player.last_active = datetime.now(UTC)
    player.stats = {}
    player.is_deleted = False
    player.deleted_at = None
    player.tutorial_instance_id = None
    player.get_inventory.return_value = []
    player.get_equipped_items.return_value = {}
    player.get_stats.return_value = {"current_dp": 20, "constitution": 50, "size": 50}
    return player


def test_player_repository_initialization():
    """Test PlayerRepository initializes correctly."""
    # PlayerRepository now requires room_cache to not be None
    room_cache: dict[str, Any] = {}
    repo = PlayerRepository(room_cache=room_cache)

    assert repo._room_cache == room_cache
    assert repo._event_bus is None


def test_player_repository_initialization_with_cache():
    """Test PlayerRepository initializes with room cache."""
    room_cache = {"room1": Room({"id": "room1"}), "room2": Room({"id": "room2"})}
    repo = PlayerRepository(room_cache=room_cache)

    assert repo._room_cache == room_cache


def test_player_repository_initialization_with_event_bus():
    """Test PlayerRepository initializes with event bus."""
    # PlayerRepository now requires room_cache to not be None
    room_cache: dict[str, Any] = {}
    event_bus = MagicMock()
    repo = PlayerRepository(room_cache=room_cache, event_bus=event_bus)

    assert repo._room_cache == room_cache
    assert repo._event_bus == event_bus


def test_validate_and_fix_player_room_valid(player_repository, mock_player):
    """Test validate_and_fix_player_room returns False for valid room."""
    mock_player.current_room_id = "arkham_square"

    result = player_repository.validate_and_fix_player_room(mock_player)

    assert result is False
    assert mock_player.current_room_id == "arkham_square"


def test_validate_and_fix_player_room_invalid(player_repository, mock_player):
    """Test validate_and_fix_player_room fixes invalid room."""
    mock_player.current_room_id = "invalid_room"

    result = player_repository.validate_and_fix_player_room(mock_player)

    assert result is True
    assert mock_player.current_room_id == "earth_arkhamcity_sanitarium_room_foyer_001"


@pytest.mark.asyncio
async def test_get_player_by_name_success(player_repository):
    """Test get_player_by_name successfully retrieves player."""
    mock_row = _make_mock_row()
    mock_session = AsyncMock()
    mock_result = MagicMock()
    mock_result.fetchall.return_value = [mock_row]
    mock_session.execute.return_value = mock_result

    with patch("server.persistence.repositories.player_repository.get_session_maker") as mock_get_session:
        mock_get_session.return_value = MagicMock()
        mock_get_session.return_value.return_value.__aenter__ = AsyncMock(return_value=mock_session)
        mock_get_session.return_value.return_value.__aexit__ = AsyncMock(return_value=None)

        result = await player_repository.get_player_by_name("TestPlayer")

        assert result is not None
        assert isinstance(result, Player)
        assert result.name == "TestPlayer"


@pytest.mark.asyncio
async def test_get_player_by_name_not_found(player_repository):
    """Test get_player_by_name returns None when player not found."""
    mock_session = AsyncMock()
    mock_result = MagicMock()
    mock_result.fetchall.return_value = []
    mock_session.execute.return_value = mock_result

    with patch("server.persistence.repositories.player_repository.get_session_maker") as mock_get_session:
        mock_get_session.return_value = MagicMock()
        mock_get_session.return_value.return_value.__aenter__ = AsyncMock(return_value=mock_session)
        mock_get_session.return_value.return_value.__aexit__ = AsyncMock(return_value=None)

        result = await player_repository.get_player_by_name("NonExistent")

        assert result is None


@pytest.mark.asyncio
async def test_get_player_by_name_database_error(player_repository):
    """Test get_player_by_name handles database errors."""
    mock_session = AsyncMock()
    mock_session.execute.side_effect = SQLAlchemyError("Database error")

    with patch("server.persistence.repositories.player_repository.get_session_maker") as mock_get_session:
        mock_get_session.return_value = MagicMock()
        mock_get_session.return_value.return_value.__aenter__ = AsyncMock(return_value=mock_session)
        mock_get_session.return_value.return_value.__aexit__ = AsyncMock(return_value=None)

        with pytest.raises(DatabaseError):
            await player_repository.get_player_by_name("TestPlayer")


@pytest.mark.asyncio
async def test_save_player_success(player_repository, mock_player):
    """Test save_player successfully saves player."""
    mock_session = AsyncMock()
    mock_session.execute = AsyncMock()
    mock_session.commit = AsyncMock()

    with patch("server.persistence.repositories.player_repository.get_session_maker") as mock_get_session:
        mock_get_session.return_value = MagicMock()
        mock_get_session.return_value.return_value.__aenter__ = AsyncMock(return_value=mock_session)
        mock_get_session.return_value.return_value.__aexit__ = AsyncMock(return_value=None)

        await player_repository.save_player(mock_player)

        mock_session.execute.assert_awaited()
        mock_session.commit.assert_awaited_once()


@pytest.mark.asyncio
async def test_save_player_with_bool_is_admin(player_repository, mock_player):
    """Test save_player converts bool is_admin to int."""
    mock_player.is_admin = True
    mock_session = AsyncMock()
    mock_session.execute = AsyncMock()
    mock_session.commit = AsyncMock()

    with patch("server.persistence.repositories.player_repository.get_session_maker") as mock_get_session:
        mock_get_session.return_value = MagicMock()
        mock_get_session.return_value.return_value.__aenter__ = AsyncMock(return_value=mock_session)
        mock_get_session.return_value.return_value.__aexit__ = AsyncMock(return_value=None)

        await player_repository.save_player(mock_player)

        assert mock_player.is_admin == 1


@pytest.mark.asyncio
async def test_save_player_refuses_deleted_player(player_repository: PlayerRepository, mock_player: MagicMock):
    """save_player must not resurrect a soft-deleted row (#777): when player_is_deleted()
    reports True for a stale in-memory Player, the upsert is skipped entirely and the
    session is never committed."""
    guard_result = _ScalarResult(True)
    mock_execute = AsyncMock(return_value=guard_result)
    mock_commit = AsyncMock()
    mock_session = AsyncMock()
    mock_session.execute = mock_execute
    mock_session.commit = mock_commit

    with patch("server.persistence.repositories.player_repository.get_session_maker") as mock_get_session:
        mock_get_session.return_value = _session_maker_double(mock_session)

        await player_repository.save_player(mock_player)

        mock_execute.assert_awaited_once()  # only the guard read, no upsert
        mock_commit.assert_not_awaited()


@pytest.mark.asyncio
async def test_save_player_allows_new_player(player_repository: PlayerRepository, mock_player: MagicMock):
    """save_player must still upsert a not-yet-inserted player, where player_is_deleted()
    returns NULL (no row) rather than True."""
    guard_result = _ScalarResult(None)
    upsert_result = MagicMock()
    mock_execute = AsyncMock(side_effect=[guard_result, upsert_result])
    mock_commit = AsyncMock()
    mock_session = AsyncMock()
    mock_session.execute = mock_execute
    mock_session.commit = mock_commit

    with patch("server.persistence.repositories.player_repository.get_session_maker") as mock_get_session:
        mock_get_session.return_value = _session_maker_double(mock_session)

        await player_repository.save_player(mock_player)

        assert mock_execute.await_count == 2
        mock_commit.assert_awaited_once()


@pytest.mark.asyncio
async def test_save_player_database_error(player_repository, mock_player):
    """Test save_player handles database errors."""
    mock_session = AsyncMock()
    mock_session.execute.side_effect = SQLAlchemyError("Database error")

    with patch("server.persistence.repositories.player_repository.get_session_maker") as mock_get_session:
        mock_get_session.return_value = MagicMock()
        mock_get_session.return_value.return_value.__aenter__ = AsyncMock(return_value=mock_session)
        mock_get_session.return_value.return_value.__aexit__ = AsyncMock(return_value=None)

        with pytest.raises(DatabaseError):
            await player_repository.save_player(mock_player)


@pytest.mark.asyncio
async def test_list_players_success(player_repository):
    """Test list_players successfully retrieves players."""
    mock_row1 = _make_mock_row(name="Player1")
    mock_row2 = _make_mock_row(name="Player2")

    mock_session = AsyncMock()
    mock_result = MagicMock()
    mock_result.fetchall.return_value = [mock_row1, mock_row2]
    mock_session.execute.return_value = mock_result

    with patch("server.persistence.repositories.player_repository.get_session_maker") as mock_get_session:
        mock_get_session.return_value = MagicMock()
        mock_get_session.return_value.return_value.__aenter__ = AsyncMock(return_value=mock_session)
        mock_get_session.return_value.return_value.__aexit__ = AsyncMock(return_value=None)

        result = await player_repository.list_players()

        assert len(result) == 2
        assert result[0].name == "Player1"
        assert result[1].name == "Player2"


@pytest.mark.asyncio
async def test_list_players_empty(player_repository):
    """Test list_players returns empty list when no players."""
    mock_session = AsyncMock()
    mock_result = MagicMock()
    mock_result.fetchall.return_value = []
    mock_session.execute.return_value = mock_result

    with patch("server.persistence.repositories.player_repository.get_session_maker") as mock_get_session:
        mock_get_session.return_value = MagicMock()
        mock_get_session.return_value.return_value.__aenter__ = AsyncMock(return_value=mock_session)
        mock_get_session.return_value.return_value.__aexit__ = AsyncMock(return_value=None)

        result = await player_repository.list_players()

        assert result == []


@pytest.mark.asyncio
async def test_list_players_database_error(player_repository):
    """Test list_players handles database errors."""
    mock_session = AsyncMock()
    mock_session.execute.side_effect = SQLAlchemyError("Database error")

    with patch("server.persistence.repositories.player_repository.get_session_maker") as mock_get_session:
        mock_get_session.return_value = MagicMock()
        mock_get_session.return_value.return_value.__aenter__ = AsyncMock(return_value=mock_session)
        mock_get_session.return_value.return_value.__aexit__ = AsyncMock(return_value=None)

        with pytest.raises(DatabaseError):
            await player_repository.list_players()


@pytest.mark.asyncio
async def test_get_player_by_id_success(player_repository):
    """Test get_player_by_id successfully retrieves player."""
    player_id = uuid.uuid4()
    mock_row = _make_mock_row(player_id=player_id)

    mock_session = AsyncMock()
    mock_result = MagicMock()
    mock_result.fetchall.return_value = [mock_row]
    mock_session.execute.return_value = mock_result

    with patch("server.persistence.repositories.player_repository.get_session_maker") as mock_get_session:
        mock_get_session.return_value = MagicMock()
        mock_get_session.return_value.return_value.__aenter__ = AsyncMock(return_value=mock_session)
        mock_get_session.return_value.return_value.__aexit__ = AsyncMock(return_value=None)

        result = await player_repository.get_player_by_id(player_id)

        assert result is not None
        assert str(result.player_id) == str(player_id)


@pytest.mark.asyncio
async def test_get_player_by_id_not_found(player_repository):
    """Test get_player_by_id returns None when player not found."""
    player_id = uuid.uuid4()

    mock_session = AsyncMock()
    mock_result = MagicMock()
    mock_result.fetchall.return_value = []
    mock_session.execute.return_value = mock_result

    with patch("server.persistence.repositories.player_repository.get_session_maker") as mock_get_session:
        mock_get_session.return_value = MagicMock()
        mock_get_session.return_value.return_value.__aenter__ = AsyncMock(return_value=mock_session)
        mock_get_session.return_value.return_value.__aexit__ = AsyncMock(return_value=None)

        result = await player_repository.get_player_by_id(player_id)

        assert result is None


@pytest.mark.asyncio
async def test_get_players_by_user_id_success(player_repository):
    """Test get_players_by_user_id successfully retrieves players."""
    user_id = uuid.uuid4()
    mock_row1 = _make_mock_row(user_id=user_id, name="Player1")
    mock_row2 = _make_mock_row(user_id=user_id, name="Player2")

    mock_session = AsyncMock()
    mock_result = MagicMock()
    mock_result.fetchall.return_value = [mock_row1, mock_row2]
    mock_session.execute.return_value = mock_result

    with patch("server.persistence.repositories.player_repository.get_session_maker") as mock_get_session:
        mock_get_session.return_value = MagicMock()
        mock_get_session.return_value.return_value.__aenter__ = AsyncMock(return_value=mock_session)
        mock_get_session.return_value.return_value.__aexit__ = AsyncMock(return_value=None)

        result = await player_repository.get_players_by_user_id(str(user_id))

        assert len(result) == 2


@pytest.mark.asyncio
async def test_get_active_players_by_user_id_success(player_repository):
    """Test get_active_players_by_user_id successfully retrieves active players."""
    user_id = uuid.uuid4()
    mock_row = _make_mock_row(user_id=user_id)

    mock_session = AsyncMock()
    mock_result = MagicMock()
    mock_result.fetchall.return_value = [mock_row]
    mock_session.execute.return_value = mock_result

    with patch("server.persistence.repositories.player_repository.get_session_maker") as mock_get_session:
        mock_get_session.return_value = MagicMock()
        mock_get_session.return_value.return_value.__aenter__ = AsyncMock(return_value=mock_session)
        mock_get_session.return_value.return_value.__aexit__ = AsyncMock(return_value=None)

        result = await player_repository.get_active_players_by_user_id(str(user_id))

        assert len(result) == 1


@pytest.mark.asyncio
async def test_get_player_by_user_id_success(player_repository):
    """Test get_player_by_user_id returns first active player."""
    user_id = "user123"
    mock_player = MagicMock(spec=Player)

    with patch.object(player_repository, "get_active_players_by_user_id", return_value=[mock_player]):
        result = await player_repository.get_player_by_user_id(user_id)

        assert result == mock_player


@pytest.mark.asyncio
async def test_get_player_by_user_id_not_found(player_repository):
    """Test get_player_by_user_id returns None when no players."""
    user_id = "user123"

    with patch.object(player_repository, "get_active_players_by_user_id", return_value=[]):
        result = await player_repository.get_player_by_user_id(user_id)

        assert result is None


@pytest.mark.asyncio
async def test_get_players_in_room_success(player_repository):
    """Test get_players_in_room successfully retrieves players."""
    room_id = "arkham_square"
    mock_row = _make_mock_row()
    mock_row.current_room_id = room_id

    mock_session = AsyncMock()
    mock_result = MagicMock()
    mock_result.fetchall.return_value = [mock_row]
    mock_session.execute.return_value = mock_result

    with patch("server.persistence.repositories.player_repository.get_session_maker") as mock_get_session:
        mock_get_session.return_value = MagicMock()
        mock_get_session.return_value.return_value.__aenter__ = AsyncMock(return_value=mock_session)
        mock_get_session.return_value.return_value.__aexit__ = AsyncMock(return_value=None)

        result = await player_repository.get_players_in_room(room_id)

        assert len(result) == 1


@pytest.mark.asyncio
async def test_save_players_success(player_repository, mock_player):
    """Test save_players successfully saves multiple players."""
    mock_player2 = MagicMock(spec=Player)
    mock_player2.is_admin = False
    mock_player2.player_id = str(uuid.uuid4())
    mock_player2.user_id = str(uuid.uuid4())
    mock_player2.name = "Player2"
    mock_player2.inventory = "[]"
    mock_player2.status_effects = "[]"
    mock_player2.current_room_id = "arkham_square"
    mock_player2.respawn_room_id = "arkham_square"
    mock_player2.experience_points = 0
    mock_player2.level = 1
    mock_player2.profession_id = None
    mock_player2.created_at = datetime.now(UTC)
    mock_player2.last_active = datetime.now(UTC)
    mock_player2.stats = {}
    mock_player2.is_deleted = False
    mock_player2.deleted_at = None
    mock_player2.tutorial_instance_id = None
    mock_player2.get_inventory.return_value = []
    mock_player2.get_equipped_items.return_value = {}
    mock_player2.get_stats.return_value = {}
    players: list[Any] = [mock_player, mock_player2]

    mock_session = AsyncMock()
    mock_session.execute = AsyncMock()
    mock_session.commit = AsyncMock()

    with patch("server.persistence.repositories.player_repository.get_session_maker") as mock_get_session:
        mock_get_session.return_value = MagicMock()
        mock_get_session.return_value.return_value.__aenter__ = AsyncMock(return_value=mock_session)
        mock_get_session.return_value.return_value.__aexit__ = AsyncMock(return_value=None)

        await player_repository.save_players(players)

        assert mock_session.execute.await_count == 2
        mock_session.commit.assert_awaited_once()


@pytest.mark.asyncio
async def test_soft_delete_player_success(player_repository):
    """Test soft_delete_player successfully soft deletes player."""
    player_id = uuid.uuid4()

    mock_session = AsyncMock()
    mock_result = MagicMock()
    mock_result.scalar.return_value = True
    mock_session.execute.return_value = mock_result
    mock_session.commit = AsyncMock()

    with patch("server.persistence.repositories.player_repository.get_session_maker") as mock_get_session:
        mock_get_session.return_value = MagicMock()
        mock_get_session.return_value.return_value.__aenter__ = AsyncMock(return_value=mock_session)
        mock_get_session.return_value.return_value.__aexit__ = AsyncMock(return_value=None)

        result = await player_repository.soft_delete_player(player_id)

        assert result is True


@pytest.mark.asyncio
async def test_soft_delete_player_not_found(player_repository):
    """Test soft_delete_player returns False when player not found."""
    player_id = uuid.uuid4()

    mock_session = AsyncMock()
    mock_result = MagicMock()
    mock_result.scalar.return_value = False
    mock_session.execute.return_value = mock_result
    mock_session.commit = AsyncMock()

    with patch("server.persistence.repositories.player_repository.get_session_maker") as mock_get_session:
        mock_get_session.return_value = MagicMock()
        mock_get_session.return_value.return_value.__aenter__ = AsyncMock(return_value=mock_session)
        mock_get_session.return_value.return_value.__aexit__ = AsyncMock(return_value=None)

        result = await player_repository.soft_delete_player(player_id)

        assert result is False


@pytest.mark.asyncio
async def test_delete_player_success(player_repository):
    """Test delete_player successfully deletes player."""
    player_id = uuid.uuid4()

    mock_session = AsyncMock()
    mock_result = MagicMock()
    mock_result.scalar.return_value = True
    mock_session.execute.return_value = mock_result
    mock_session.commit = AsyncMock()

    with patch("server.persistence.repositories.player_repository.get_session_maker") as mock_get_session:
        mock_get_session.return_value = MagicMock()
        mock_get_session.return_value.return_value.__aenter__ = AsyncMock(return_value=mock_session)
        mock_get_session.return_value.return_value.__aexit__ = AsyncMock(return_value=None)

        result = await player_repository.delete_player(player_id)

        assert result is True
        mock_session.execute.assert_awaited()
        mock_session.commit.assert_awaited_once()


@pytest.mark.asyncio
async def test_delete_player_not_found(player_repository):
    """Test delete_player returns False when player not found."""
    player_id = uuid.uuid4()

    mock_session = AsyncMock()
    mock_result = MagicMock()
    mock_result.scalar.return_value = False
    mock_session.execute.return_value = mock_result
    mock_session.commit = AsyncMock()

    with patch("server.persistence.repositories.player_repository.get_session_maker") as mock_get_session:
        mock_get_session.return_value = MagicMock()
        mock_get_session.return_value.return_value.__aenter__ = AsyncMock(return_value=mock_session)
        mock_get_session.return_value.return_value.__aexit__ = AsyncMock(return_value=None)

        result = await player_repository.delete_player(player_id)

        assert result is False


@pytest.mark.asyncio
async def test_update_player_last_active_success(player_repository):
    """Test update_player_last_active successfully updates timestamp."""
    player_id = uuid.uuid4()

    mock_session = AsyncMock()
    mock_session.execute = AsyncMock()
    mock_session.commit = AsyncMock()

    with patch("server.persistence.repositories.player_repository.get_session_maker") as mock_get_session:
        mock_get_session.return_value = MagicMock()
        mock_get_session.return_value.return_value.__aenter__ = AsyncMock(return_value=mock_session)
        mock_get_session.return_value.return_value.__aexit__ = AsyncMock(return_value=None)

        await player_repository.update_player_last_active(player_id)

        mock_session.execute.assert_awaited_once()
        mock_session.commit.assert_awaited_once()


@pytest.mark.asyncio
async def test_update_player_last_active_with_timestamp(player_repository):
    """Test update_player_last_active with provided timestamp."""
    player_id = uuid.uuid4()
    last_active = datetime.now(UTC)

    mock_session = AsyncMock()
    mock_session.execute = AsyncMock()
    mock_session.commit = AsyncMock()

    with patch("server.persistence.repositories.player_repository.get_session_maker") as mock_get_session:
        mock_get_session.return_value = MagicMock()
        mock_get_session.return_value.return_value.__aenter__ = AsyncMock(return_value=mock_session)
        mock_get_session.return_value.return_value.__aexit__ = AsyncMock(return_value=None)

        await player_repository.update_player_last_active(player_id, last_active)

        mock_session.execute.assert_awaited_once()
        mock_session.commit.assert_awaited_once()


@pytest.mark.asyncio
async def test_get_players_batch_success(player_repository):
    """Test get_players_batch successfully retrieves multiple players."""
    player_ids = [uuid.uuid4(), uuid.uuid4()]
    mock_row1 = _make_mock_row(player_id=player_ids[0], name="Player1")
    mock_row2 = _make_mock_row(player_id=player_ids[1], name="Player2")

    mock_session = AsyncMock()
    mock_result = MagicMock()
    mock_result.fetchall.return_value = [mock_row1, mock_row2]
    mock_session.execute.return_value = mock_result

    with patch("server.persistence.repositories.player_repository.get_session_maker") as mock_get_session:
        mock_get_session.return_value = MagicMock()
        mock_get_session.return_value.return_value.__aenter__ = AsyncMock(return_value=mock_session)
        mock_get_session.return_value.return_value.__aexit__ = AsyncMock(return_value=None)

        result = await player_repository.get_players_batch(player_ids)

        assert len(result) == 2
