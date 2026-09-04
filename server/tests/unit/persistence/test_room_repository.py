"""Unit tests for RoomRepository."""

from unittest.mock import MagicMock

from server.persistence.repositories.room_repository import RoomRepository


def test_get_room_by_id_from_cache() -> None:
    room = MagicMock()
    room.id = "room-1"
    repo = RoomRepository({"room-1": room})
    assert repo.get_room_by_id("room-1") is room
    assert repo.get_room_by_id("missing") is None


def test_list_rooms_returns_cache_values() -> None:
    room_a = MagicMock()
    room_b = MagicMock()
    repo = RoomRepository({"a": room_a, "b": room_b})
    assert repo.list_rooms() == [room_a, room_b]


def test_save_room_updates_cache() -> None:
    repo = RoomRepository({})
    room = MagicMock()
    room.id = "room-1"
    repo.save_room(room)
    assert repo.get_room_by_id("room-1") is room


def test_save_rooms_updates_cache() -> None:
    repo = RoomRepository({})
    room_a = MagicMock()
    room_a.id = "a"
    room_b = MagicMock()
    room_b.id = "b"
    repo.save_rooms([room_a, room_b])
    assert repo.get_room_by_id("a") is room_a
    assert repo.get_room_by_id("b") is room_b
