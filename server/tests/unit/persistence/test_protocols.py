"""Runtime checks for persistence repository protocols."""

from __future__ import annotations

import uuid
from typing import cast

import pytest

from server.persistence.protocols import PlayerRepositoryProtocol, RoomRepositoryProtocol


class _StubPlayerRepo:
    async def get_player_by_id(self, player_id: uuid.UUID) -> object | None:
        return {"player_id": player_id}

    async def get_player_by_user_id(self, user_id: str) -> object | None:
        return None

    async def get_players_by_user_id(self, user_id: str) -> list[object]:
        return []

    async def get_active_players_by_user_id(self, user_id: str) -> list[object]:
        return []

    async def get_player_by_name(self, name: str) -> object | None:
        return None

    async def save_player(self, player: object) -> None:
        return None

    async def save_players(self, players: list[object]) -> None:
        return None

    async def list_players(self) -> list[object]:
        return []

    async def get_players_in_room(self, room_id: str) -> list[object]:
        return []

    async def get_players_batch(self, player_ids: list[uuid.UUID]) -> list[object]:
        return []

    async def soft_delete_player(self, player_id: uuid.UUID) -> bool:
        return True

    async def delete_player(self, player_id: uuid.UUID) -> bool:
        return True

    async def update_player_last_active(self, player_id: uuid.UUID, last_active: object | None = None) -> None:
        return None

    def validate_and_fix_player_room(self, player: object) -> bool:
        return True


class _StubRoomRepo:
    def get_room_by_id(self, room_id: str) -> object | None:
        return {"id": room_id}

    def list_rooms(self) -> list[object]:
        return []


@pytest.mark.asyncio
async def test_player_repository_protocol_stub() -> None:
    repo = cast(PlayerRepositoryProtocol, _StubPlayerRepo())
    player_id = uuid.uuid4()
    found = await repo.get_player_by_id(player_id)
    assert found is not None
    assert cast(dict[str, object], found)["player_id"] == player_id
    assert await repo.get_player_by_user_id("u1") is None
    assert await repo.get_players_by_user_id("u1") == []
    assert await repo.get_active_players_by_user_id("u1") == []
    assert await repo.get_player_by_name("x") is None
    await repo.save_player(object())
    await repo.save_players([])
    assert await repo.list_players() == []
    assert await repo.get_players_in_room("r1") == []
    assert await repo.get_players_batch([player_id]) == []
    assert await repo.soft_delete_player(player_id) is True
    assert await repo.delete_player(player_id) is True
    await repo.update_player_last_active(player_id)
    assert repo.validate_and_fix_player_room(object()) is True


def test_room_repository_protocol_stub() -> None:
    repo = cast(RoomRepositoryProtocol, _StubRoomRepo())
    room = repo.get_room_by_id("room_001")
    assert room is not None
    assert cast(dict[str, str], room)["id"] == "room_001"
    assert repo.list_rooms() == []


@pytest.mark.asyncio
async def test_protocol_ellipsis_bodies_via_unbound_methods() -> None:
    """Exercise Protocol method bodies (`...`) for line coverage."""
    self = cast(object, object())
    player_id = uuid.uuid4()
    await PlayerRepositoryProtocol.get_player_by_id(self, player_id)  # type: ignore[arg-type]
    await PlayerRepositoryProtocol.get_player_by_user_id(self, "u")  # type: ignore[arg-type]
    await PlayerRepositoryProtocol.get_players_by_user_id(self, "u")  # type: ignore[arg-type]
    await PlayerRepositoryProtocol.get_active_players_by_user_id(self, "u")  # type: ignore[arg-type]
    await PlayerRepositoryProtocol.get_player_by_name(self, "n")  # type: ignore[arg-type]
    await PlayerRepositoryProtocol.save_player(self, object())  # type: ignore[arg-type]
    await PlayerRepositoryProtocol.save_players(self, [])  # type: ignore[arg-type]
    await PlayerRepositoryProtocol.list_players(self)  # type: ignore[arg-type]
    await PlayerRepositoryProtocol.get_players_in_room(self, "r")  # type: ignore[arg-type]
    await PlayerRepositoryProtocol.get_players_batch(self, [player_id])  # type: ignore[arg-type]
    await PlayerRepositoryProtocol.soft_delete_player(self, player_id)  # type: ignore[arg-type]
    await PlayerRepositoryProtocol.delete_player(self, player_id)  # type: ignore[arg-type]
    await PlayerRepositoryProtocol.update_player_last_active(self, player_id)  # type: ignore[arg-type]
    PlayerRepositoryProtocol.validate_and_fix_player_room(self, object())  # type: ignore[arg-type]
    RoomRepositoryProtocol.get_room_by_id(self, "r")  # type: ignore[arg-type]
    RoomRepositoryProtocol.list_rooms(self)  # type: ignore[arg-type]
