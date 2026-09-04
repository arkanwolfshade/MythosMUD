"""Unit tests for coordinate generation helpers."""

import json
from unittest.mock import AsyncMock, MagicMock

import pytest

from server.services.coordinate_generator import CoordinateGenerator


@pytest.fixture
def generator():
    return CoordinateGenerator(MagicMock())


def test_get_next_coordinates_directions(generator):
    assert generator._get_next_coordinates(0, 0, "north") == (0, -1)
    assert generator._get_next_coordinates(0, 0, "south") == (0, 1)
    assert generator._get_next_coordinates(0, 0, "east") == (1, 0)
    assert generator._get_next_coordinates(0, 0, "west") == (-1, 0)
    assert generator._get_next_coordinates(2, 3, "up") == (2, 3)


def test_reverse_direction(generator):
    assert generator._reverse_direction("north") == "south"
    assert generator._reverse_direction("east") == "west"
    assert generator._reverse_direction("up") == "down"


def test_find_origin_room_prefers_map_origin_flag(generator):
    rooms = [
        {"id": "a", "map_origin_zone": False},
        {"id": "b", "map_origin_zone": True},
    ]
    assert generator._find_origin_room(rooms)["id"] == "b"


def test_find_origin_room_falls_back_to_first(generator):
    rooms = [{"id": "a"}, {"id": "b"}]
    assert generator._find_origin_room(rooms)["id"] == "a"


def test_assign_coordinates_bfs(generator):
    adjacency = {
        "origin": [("north_room", "north")],
        "north_room": [("origin", "south")],
    }
    coords = generator._assign_coordinates_bfs("origin", adjacency)
    assert coords["origin"] == (0, 0)
    assert coords["north_room"] == (0, -1)


def test_detect_coordinate_conflicts(generator):
    coords = {"room_a": (1, 1), "room_b": (1, 1), "room_c": (2, 2)}
    conflicts = generator._detect_coordinate_conflicts(coords)
    assert len(conflicts) == 1
    assert conflicts[0][:2] == ("room_a", "room_b")


@pytest.mark.asyncio
async def test_generate_coordinates_for_zone_empty_data(generator):
    generator._load_rooms_data = AsyncMock(return_value=[])
    result = await generator.generate_coordinates_for_zone("earth", "arkham")
    assert result["coordinates"] == {}
    assert result["conflicts"] == []


@pytest.mark.asyncio
async def test_generate_for_subzone_positions_linked_rooms(generator):
    rooms = [
        {
            "id": "origin",
            "map_origin_zone": True,
            "name": "Origin",
            "exits": {"north": "north_room"},
        },
        {
            "id": "north_room",
            "map_origin_zone": False,
            "name": "North",
            "exits": {"south": "origin"},
        },
    ]
    coords, conflicts, origin = await generator._generate_for_subzone(rooms)
    assert origin == "origin"
    assert coords["north_room"] == (0, -1)
    assert conflicts == []


def test_build_adjacency_list_adds_reverse_edges(generator):
    rooms = [
        {"id": "a", "exits": {"north": "b"}},
        {"id": "b", "exits": {"south": "a"}},
    ]
    adjacency = generator._build_adjacency_list(rooms)
    assert ("b", "north") in adjacency["a"]
    assert ("a", "south") in adjacency["b"]


def test_find_origin_room_empty_list(generator):
    assert generator._find_origin_room([]) is None


@pytest.mark.asyncio
async def test_generate_coordinates_for_zone_stores_results(generator):
    rooms = [
        {"id": "origin", "sub_zone": "default", "map_origin_zone": True, "exits": {}},
    ]
    generator._load_rooms_data = AsyncMock(return_value=rooms)
    generator._store_coordinates = AsyncMock()
    result = await generator.generate_coordinates_for_zone("earth", "arkham")
    assert "origin" in result["coordinates"]
    generator._store_coordinates.assert_awaited_once()


@pytest.mark.asyncio
async def test_store_coordinates_persists_values(generator):
    session = AsyncMock()
    session.commit = AsyncMock()
    gen = CoordinateGenerator(session)
    await gen._store_coordinates({"room_a": (1, 2)})
    session.execute.assert_awaited_once()
    session.commit.assert_awaited_once()


@pytest.mark.asyncio
async def test_store_coordinates_noop_on_empty():
    session = AsyncMock()
    gen = CoordinateGenerator(session)
    await gen._store_coordinates({})
    session.execute.assert_not_called()


@pytest.mark.asyncio
async def test_store_coordinates_sends_one_bulk_call_with_full_payload():
    session = AsyncMock()
    session.commit = AsyncMock()
    gen = CoordinateGenerator(session)
    await gen._store_coordinates({"room_a": (1, 2), "room_b": (-3, 4)})

    session.execute.assert_awaited_once()
    _, params = session.execute.await_args.args
    payload = json.loads(params["positions"])
    assert payload == [
        {"stable_id": "room_a", "map_x": 1.0, "map_y": 2.0},
        {"stable_id": "room_b", "map_x": -3.0, "map_y": 4.0},
    ]
