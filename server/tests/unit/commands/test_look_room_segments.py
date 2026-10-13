"""`look`'s "Also here: ..." line carries each NPC's name as a styled segment (#1036)."""

# pyright: reportAny=false, reportPrivateUsage=false
# The room, persistence and lifecycle manager are MagicMock/AsyncMock doubles, and look_room's helpers are private by
# design; attribute access on those doubles is Any by construction.

from typing import cast
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.commands.look_room import _handle_room_look, _npc_section_parts
from server.constants.message_segments import MessageSegment
from server.constants.npc_disposition import NpcDisposition, NpcOccupant

GOBLIN: NpcOccupant = {"name": "Goblin", "disposition": NpcDisposition.SHOPKEEPER}
RAT: NpcOccupant = {"name": "Rat", "disposition": NpcDisposition.AGGRESSIVE_MOB}


def _phantom_patches(name: str | None):
    """Patch the viewer's phantom roster: one phantom named ``name``, or none."""
    return (
        patch(
            "server.services.phantom_hostile_service.phantom_hostile_service.get_active_phantoms",
            return_value=["phantom_1"] if name else [],
        ),
        patch(
            "server.services.phantom_hostile_service.phantom_hostile_service.get_phantom_data",
            return_value={"phantom_id": "phantom_1", "room_id": "test_room", "name": name},
        ),
    )


@pytest.mark.asyncio
async def test_section_parts_style_each_name_by_disposition() -> None:
    with patch("server.commands.look_room._get_npc_occupants_in_room", new=AsyncMock(return_value=[GOBLIN, RAT])):
        parts = await _npc_section_parts("test_room")
    assert parts == [
        "Also here: ",
        {"text": "Goblin", "category": "npc.shopkeeper"},
        ", ",
        {"text": "Rat", "category": "npc.aggressive_mob"},
    ]


@pytest.mark.asyncio
async def test_a_phantom_is_tagged_exactly_like_a_real_hostile() -> None:
    """ADR-024: nothing in the line tells a hallucinated hostile from a real one."""
    patches = _phantom_patches("Shambling Horror")
    with (
        patch("server.commands.look_room._get_npc_occupants_in_room", new=AsyncMock(return_value=[RAT])),
        patches[0],
        patches[1],
    ):
        parts = await _npc_section_parts("test_room", "player-1")
    real, phantom = cast(MessageSegment, parts[1]), cast(MessageSegment, parts[3])
    assert real.get("category") == phantom.get("category") == "npc.aggressive_mob"


@pytest.mark.asyncio
async def test_section_parts_are_empty_without_npcs_or_a_room() -> None:
    with patch("server.commands.look_room._get_npc_occupants_in_room", new=AsyncMock(return_value=[])):
        assert await _npc_section_parts("test_room") == []
    assert await _npc_section_parts(None) == []


def _room() -> MagicMock:
    room = MagicMock(id="test_room", description="A damp cellar.", exits={"north": "room_north"})
    room.get_players = MagicMock(return_value=[])
    return room


def _persistence() -> AsyncMock:
    persistence = AsyncMock()
    persistence.get_containers_by_room_id = AsyncMock(return_value=[])
    persistence.get_player_by_id = AsyncMock(return_value=None)
    return persistence


@pytest.mark.asyncio
async def test_room_look_carries_segments_that_join_to_the_whole_result() -> None:
    with patch("server.commands.look_room._get_npc_occupants_in_room", new=AsyncMock(return_value=[GOBLIN, RAT])):
        result = await _handle_room_look(_room(), [], _persistence(), "TestPlayer")
    segments = cast(list[MessageSegment], result["segments"])
    assert "".join(segment["text"] for segment in segments) == result["result"]
    assert "Also here: Goblin, Rat" in result["result"]
    assert [s for s in segments if "category" in s] == [
        {"text": "Goblin", "category": "npc.shopkeeper"},
        {"text": "Rat", "category": "npc.aggressive_mob"},
    ]


@pytest.mark.asyncio
async def test_room_look_with_nobody_here_has_no_segments() -> None:
    with patch("server.commands.look_room._get_npc_occupants_in_room", new=AsyncMock(return_value=[])):
        result = await _handle_room_look(_room(), [], _persistence(), "TestPlayer")
    assert "segments" not in result
    assert "Also here" not in result["result"]
