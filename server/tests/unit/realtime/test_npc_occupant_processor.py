"""Unit tests for NPCOccupantProcessor."""

from unittest.mock import MagicMock, patch

import pytest

from server.realtime.npc_occupant_processor import NPCOccupantProcessor
from server.realtime.room_id_utils import RoomIDUtils


@pytest.fixture
def processor() -> NPCOccupantProcessor:
    cm = MagicMock()
    cm._get_npcs_batch = MagicMock(return_value={"npc-1": "Deep One"})
    return NPCOccupantProcessor(connection_manager=cm, room_id_utils=RoomIDUtils(cm))


def test_get_npc_room_id_prefers_current_room(processor: NPCOccupantProcessor) -> None:
    npc = MagicMock(current_room="room-a", current_room_id="room-b")
    assert processor._get_npc_room_id(npc) == "room-a"


def test_should_include_npc_dead(processor: NPCOccupantProcessor) -> None:
    npc = MagicMock(is_alive=False)
    include, room_id = processor._should_include_npc_in_room("npc-1", npc, "room-a", "room-a")
    assert include is False
    assert room_id is None


def test_should_include_npc_matching_room(processor: NPCOccupantProcessor) -> None:
    npc = MagicMock(is_alive=True, current_room="room-a", name="Mob")
    with patch.object(processor.room_id_utils, "get_canonical_room_id", return_value="room-a"):
        with patch.object(processor.room_id_utils, "check_npc_room_match", return_value=True):
            include, room_id = processor._should_include_npc_in_room("npc-1", npc, "room-a", "room-a")
    assert include is True
    assert room_id == "room-a"


def test_scan_active_npcs_for_room(processor: NPCOccupantProcessor) -> None:
    npc = MagicMock(is_alive=True, current_room="room-a", name="Mob")
    active = {"npc-1": npc}
    with patch.object(processor, "_should_include_npc_in_room", return_value=(True, "room-a")):
        ids = processor._scan_active_npcs_for_room(active, "room-a", "room-a")
    assert ids == ["npc-1"]


@pytest.mark.asyncio
async def test_query_npcs_for_room_uses_lifecycle_manager(processor: NPCOccupantProcessor) -> None:
    lifecycle = MagicMock()
    npc = MagicMock(is_alive=True, current_room="room-a", name="Mob")
    lifecycle.active_npcs = {"npc-1": npc}
    with patch.object(processor, "_get_npc_lifecycle_manager", return_value=lifecycle):
        with patch.object(processor, "_scan_active_npcs_for_room", return_value=["npc-1"]) as scan:
            result = await processor.query_npcs_for_room("room-a", MagicMock())
    assert result == ["npc-1"]
    scan.assert_called_once()


@pytest.mark.asyncio
async def test_query_npcs_fallback_to_room(processor: NPCOccupantProcessor) -> None:
    room = MagicMock()
    room.get_npcs.return_value = ["npc-fallback"]
    with patch.object(processor, "_get_npc_lifecycle_manager", return_value=None):
        with patch.object(processor, "_filter_fallback_npcs", return_value=["npc-fallback"]):
            result = await processor.query_npcs_for_room("room-a", room)
    assert result == ["npc-fallback"]


def test_process_npcs_for_occupants(processor: NPCOccupantProcessor) -> None:
    occupants = processor.process_npcs_for_occupants(["npc-1"])
    assert occupants[0]["npc_name"] == "Deep One"
    assert occupants[0]["type"] == "npc"


def test_filter_fallback_npcs_dead(processor: NPCOccupantProcessor) -> None:
    lifecycle = MagicMock()
    lifecycle.active_npcs = {"npc-1": MagicMock(is_alive=False)}
    with patch.object(processor, "_get_lifecycle_manager_for_filtering", return_value=lifecycle):
        result = processor._filter_fallback_npcs(["npc-1"], "room-a")
    assert result == []


def test_get_npc_lifecycle_manager_unavailable(processor: NPCOccupantProcessor) -> None:
    with patch("server.services.npc_instance_service.get_npc_instance_service", return_value=None):
        assert processor._get_npc_lifecycle_manager("room-a") is None


def test_get_npc_lifecycle_manager_no_active_npcs(processor: NPCOccupantProcessor) -> None:
    lifecycle = MagicMock()
    del lifecycle.active_npcs
    service = MagicMock(lifecycle_manager=lifecycle)
    with patch("server.services.npc_instance_service.get_npc_instance_service", return_value=service):
        assert processor._get_npc_lifecycle_manager("room-a") is None


@pytest.mark.asyncio
async def test_query_npcs_handles_exception(processor: NPCOccupantProcessor) -> None:
    room = MagicMock()
    room.get_npcs.return_value = ["npc-fallback"]
    with patch.object(processor.room_id_utils, "get_canonical_room_id", side_effect=ValueError("bad")):
        with patch.object(processor, "_get_fallback_npcs", return_value=["npc-fallback"]) as fallback:
            result = await processor.query_npcs_for_room("room-a", room)
    assert result == ["npc-fallback"]
    fallback.assert_called_once()
