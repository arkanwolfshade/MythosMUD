"""Unit tests for PlayerRespawnWrapper."""

# pyright: reportAny=false
# Reason: unittest.mock.MagicMock/AsyncMock inherit Any in typeshed (NonCallableMock(Base, Any)); these tests
# drive the code through mocked sessions, services and connection managers, so mock attribute access is Any.

import datetime
import uuid
from unittest.mock import AsyncMock, MagicMock

import pytest

from server.exceptions import ValidationError
from server.game.player_respawn_wrapper import PlayerRespawnWrapper
from server.services.player_respawn_service import LIMBO_ROOM_ID


def _dead_player(name: str = "Corpse") -> MagicMock:
    p = MagicMock()
    p.name = name
    p.player_id = uuid.uuid4()
    p.user_id = "user-1"
    p.current_room_id = LIMBO_ROOM_ID
    p.last_active = datetime.datetime.now(datetime.UTC)
    p.is_dead.return_value = True
    p.get_stats.return_value = {"current_dp": -10, "max_dp": 100}
    return p


@pytest.mark.asyncio
async def test_respawn_player_by_user_id_no_players() -> None:
    wrapper = PlayerRespawnWrapper(MagicMock())
    session = MagicMock()
    session.execute = AsyncMock(
        return_value=MagicMock(scalars=MagicMock(return_value=MagicMock(all=MagicMock(return_value=[]))))
    )
    with pytest.raises(ValidationError):
        await wrapper.respawn_player_by_user_id("user-1", session, MagicMock(), MagicMock())


@pytest.mark.asyncio
async def test_respawn_player_by_user_id_not_dead() -> None:
    wrapper = PlayerRespawnWrapper(MagicMock())
    alive = MagicMock(is_dead=MagicMock(return_value=False), current_room_id="room-a")
    alive.get_stats.return_value = {"current_dp": 50}
    session = MagicMock()
    session.execute = AsyncMock(
        return_value=MagicMock(scalars=MagicMock(return_value=MagicMock(all=MagicMock(return_value=[alive]))))
    )
    with pytest.raises(ValidationError):
        await wrapper.respawn_player_by_user_id("user-1", session, MagicMock(), MagicMock())


@pytest.mark.asyncio
async def test_respawn_player_by_user_id_success() -> None:
    wrapper = PlayerRespawnWrapper(MagicMock())
    player = _dead_player()
    session = MagicMock()
    session.execute = AsyncMock(
        return_value=MagicMock(scalars=MagicMock(return_value=MagicMock(all=MagicMock(return_value=[player]))))
    )
    respawn_service = MagicMock()
    respawn_service.respawn_player = AsyncMock(return_value=True)
    room = MagicMock()
    room.to_dict.return_value = {"id": "room-spawn", "name": "Arkham"}
    persistence = MagicMock()
    persistence.get_room_by_id.return_value = room
    result = await wrapper.respawn_player_by_user_id("user-1", session, respawn_service, persistence)
    assert result["success"] is True
    assert result["player"]["name"] == "Corpse"


@pytest.mark.asyncio
async def test_respawn_player_by_user_id_multiple_dead_picks_most_recent() -> None:
    wrapper = PlayerRespawnWrapper(MagicMock())
    older = _dead_player("Older")
    older.last_active = datetime.datetime(2020, 1, 1, tzinfo=datetime.UTC)
    newer = _dead_player("Newer")
    newer.last_active = datetime.datetime(2025, 1, 1, tzinfo=datetime.UTC)
    session = MagicMock()
    session.execute = AsyncMock(
        return_value=MagicMock(scalars=MagicMock(return_value=MagicMock(all=MagicMock(return_value=[older, newer]))))
    )
    respawn_service = MagicMock()
    respawn_service.respawn_player = AsyncMock(return_value=True)
    persistence = MagicMock()
    # Reason: TEST_MOCK - persistence is a MagicMock; attribute access is inherently Any.
    # Appropriate because: same unsuppressed mock convention as the other tests in this file.
    persistence.get_room_by_id.return_value = None
    result = await wrapper.respawn_player_by_user_id("user-1", session, respawn_service, persistence)
    assert result["player"]["name"] == "Newer"


def _session_with_characters(*characters: tuple[MagicMock, int | None]) -> MagicMock:
    """A session whose user owns the players of ``characters`` ((player, current_lcd) pairs)."""
    session = MagicMock()
    session.execute = AsyncMock(
        return_value=MagicMock(
            scalars=MagicMock(return_value=MagicMock(all=MagicMock(return_value=[p for p, _ in characters])))
        )
    )
    return session


def _respawn_service(*characters: tuple[MagicMock, int | None]) -> MagicMock:
    """A respawn service whose registry-backed ``current_lcd`` answers each character's LCD (None: no such player)."""
    lcd_by_player = {str(p.player_id): lcd for p, lcd in characters}

    async def current_lcd(player_id: uuid.UUID) -> int | None:
        return lcd_by_player.get(str(player_id))

    service = MagicMock()
    service.current_lcd = AsyncMock(side_effect=current_lcd)
    service.respawn_player_from_delirium = AsyncMock(return_value=True)
    return service


@pytest.mark.asyncio
async def test_respawn_from_delirium_player_not_found() -> None:
    wrapper = PlayerRespawnWrapper(MagicMock())
    with pytest.raises(ValidationError):
        _ = await wrapper.respawn_player_from_delirium_by_user_id(
            "user-1", _session_with_characters(), _respawn_service(), MagicMock()
        )


@pytest.mark.asyncio
async def test_respawn_from_delirium_not_delirious() -> None:
    wrapper = PlayerRespawnWrapper(MagicMock())
    characters = ((_dead_player("Fine"), 50), (_dead_player("NoRecord"), None))
    session = _session_with_characters(*characters)
    with pytest.raises(ValidationError):
        _ = await wrapper.respawn_player_from_delirium_by_user_id(
            "user-1", session, _respawn_service(*characters), MagicMock()
        )


@pytest.mark.asyncio
async def test_respawn_from_delirium_picks_the_delirious_character_among_several() -> None:
    """Regression: an account with two characters made the lookup raise "Multiple rows were found"."""
    wrapper = PlayerRespawnWrapper(MagicMock())
    fine, delirious = _dead_player("Fine"), _dead_player("Delirious")
    session = _session_with_characters((fine, 70), (delirious, -10))
    respawn_service = _respawn_service((fine, 70), (delirious, -10))
    persistence = MagicMock()
    persistence.get_room_by_id.return_value = None

    result = await wrapper.respawn_player_from_delirium_by_user_id("user-1", session, respawn_service, persistence)

    respawn_service.respawn_player_from_delirium.assert_awaited_once_with(delirious.player_id, session)
    assert result["player"]["name"] == "Delirious"


@pytest.mark.asyncio
async def test_respawn_from_delirium_prefers_the_most_recently_active_delirious_character() -> None:
    wrapper = PlayerRespawnWrapper(MagicMock())
    older, newer = _dead_player("Older"), _dead_player("Newer")
    older.last_active = datetime.datetime(2026, 1, 1, tzinfo=datetime.UTC)
    newer.last_active = datetime.datetime(2026, 6, 1, tzinfo=datetime.UTC)
    session = _session_with_characters((older, -12), (newer, -10))
    respawn_service = _respawn_service((older, -12), (newer, -10))
    persistence = MagicMock()
    persistence.get_room_by_id.return_value = None

    result = await wrapper.respawn_player_from_delirium_by_user_id("user-1", session, respawn_service, persistence)

    assert result["player"]["name"] == "Newer"


@pytest.mark.asyncio
async def test_respawn_from_delirium_success() -> None:
    wrapper = PlayerRespawnWrapper(MagicMock())
    player = _dead_player("Delirious")
    session = _session_with_characters((player, -15))
    respawn_service = _respawn_service((player, -15))
    persistence = MagicMock()
    persistence.get_room_by_id.return_value = None
    result = await wrapper.respawn_player_from_delirium_by_user_id("user-1", session, respawn_service, persistence)
    assert result["success"] is True
    assert "lucidity" in result["player"]
