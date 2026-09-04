"""
Unit tests for _build_room_objects' rest_location promotion (#297).

Split out from test_async_persistence_room_loading.py to keep that file under the
file-nloc limit rather than growing an already-split file further.
"""

# pylint: disable=protected-access  # Reason: Test file - accessing protected members for unit testing
# pylint: disable=redefined-outer-name  # Reason: pytest fixture parameter names must match fixture names

# pyright: reportPrivateUsage=false
from typing import cast
from unittest.mock import MagicMock, patch

from server.async_persistence import AsyncPersistenceLayer
from server.async_persistence_room_loader import ProcessedRoomData, RoomInitPayload, RoomLoadResult


def test_build_room_objects_promotes_rest_location_from_attributes(async_persistence_layer: AsyncPersistenceLayer):
    """#297: rest_location lives in the JSONB attributes column (DML), not a top-level DB
    column -- _build_room_objects must promote it the same way it promotes environment, or
    Room.rest_location (which reads only the top-level key) silently stays False."""
    room_data_list: list[ProcessedRoomData] = [
        {
            "room_id": "earth_arkhamcity_sanitarium_room_foyer_001",
            "stable_id": "room_foyer_001",
            "name": "Main Foyer",
            "description": "A grand entrance hall.",
            "attributes": {"environment": "indoors", "rest_location": True},
            "plane": "earth",
            "zone": "arkhamcity",
            "sub_zone": "sanitarium",
        }
    ]
    exits_by_room: dict[str, dict[str, str]] = {}
    result_container: RoomLoadResult = {"rooms": {}}

    with patch("server.models.room.Room") as mock_room_class:
        mock_room_class.return_value = MagicMock()
        async_persistence_layer._build_room_objects(room_data_list, exits_by_room, result_container)

    room_init: RoomInitPayload = cast(RoomInitPayload, mock_room_class.call_args[0][0])
    assert room_init.get("rest_location") is True


def test_build_room_objects_defaults_rest_location_false(async_persistence_layer: AsyncPersistenceLayer):
    """A room with no rest_location attribute must not silently become a rest location."""
    room_data_list: list[ProcessedRoomData] = [
        {
            "room_id": "earth_arkhamcity_subzone_room_001",
            "stable_id": "room_001",
            "name": "Test Room",
            "description": "A test room",
            "attributes": {"environment": "outdoors"},
            "plane": "earth",
            "zone": "arkhamcity",
            "sub_zone": "subzone",
        }
    ]
    exits_by_room: dict[str, dict[str, str]] = {}
    result_container: RoomLoadResult = {"rooms": {}}

    with patch("server.models.room.Room") as mock_room_class:
        mock_room_class.return_value = MagicMock()
        async_persistence_layer._build_room_objects(room_data_list, exits_by_room, result_container)

    room_init: RoomInitPayload = cast(RoomInitPayload, mock_room_class.call_args[0][0])
    assert room_init.get("rest_location") is False
