"""Unit tests for PlayerRespawnWrapper."""

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
async def test_respawn_from_delirium_player_not_found() -> None:
    wrapper = PlayerRespawnWrapper(MagicMock())
    session = MagicMock()
    session.execute = AsyncMock(return_value=MagicMock(scalar_one_or_none=MagicMock(return_value=None)))
    with pytest.raises(ValidationError):
        await wrapper.respawn_player_from_delirium_by_user_id("user-1", session, MagicMock(), MagicMock())


@pytest.mark.asyncio
async def test_respawn_from_delirium_not_delirious() -> None:
    wrapper = PlayerRespawnWrapper(MagicMock())
    player = MagicMock(player_id=uuid.uuid4())
    session = MagicMock()
    session.execute = AsyncMock(return_value=MagicMock(scalar_one_or_none=MagicMock(return_value=player)))
    lucidity = MagicMock(current_lcd=50)
    session.get = AsyncMock(return_value=lucidity)
    with pytest.raises(ValidationError):
        await wrapper.respawn_player_from_delirium_by_user_id("user-1", session, MagicMock(), MagicMock())


@pytest.mark.asyncio
async def test_respawn_from_delirium_success() -> None:
    wrapper = PlayerRespawnWrapper(MagicMock())
    player = _dead_player("Delirious")
    session = MagicMock()
    session.execute = AsyncMock(return_value=MagicMock(scalar_one_or_none=MagicMock(return_value=player)))
    lucidity = MagicMock(current_lcd=-15)
    session.get = AsyncMock(return_value=lucidity)
    session.refresh = AsyncMock()
    respawn_service = MagicMock()
    respawn_service.respawn_player_from_delirium = AsyncMock(return_value=True)
    persistence = MagicMock()
    persistence.get_room_by_id.return_value = None
    result = await wrapper.respawn_player_from_delirium_by_user_id("user-1", session, respawn_service, persistence)
    assert result["success"] is True
    assert "lucidity" in result["player"]
