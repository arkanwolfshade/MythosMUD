"""`_get_npc_occupants_in_room`: the room's live NPCs as {name, disposition} (#1036)."""

# pyright: reportAny=false
# NPC instances and the lifecycle manager are MagicMock doubles (the production code duck-types them), so attribute
# access on those doubles is Any by construction.

from unittest.mock import MagicMock, patch

import pytest

from server.commands.look_npc import _get_npc_occupants_in_room, _get_npcs_in_room
from server.constants.npc_disposition import NpcDisposition


def _npc(name: str | None, npc_type: object, room: str = "room-1", *, alive: bool = True) -> MagicMock:
    npc = MagicMock(current_room_id=room, current_room=None, is_alive=alive, npc_type=npc_type)
    npc.name = name
    return npc


def _lifecycle(**npcs: MagicMock) -> MagicMock:
    return MagicMock(active_npcs=dict(npcs))


@pytest.mark.asyncio
async def test_lists_each_live_npc_in_the_room_with_its_disposition() -> None:
    lifecycle = _lifecycle(
        a=_npc("Merchant", "shopkeeper"),
        b=_npc("Rat", "aggressive_mob"),
        c=_npc("Elsewhere", "passive_mob", room="room-2"),
    )
    with patch("server.commands.look_npc._get_lifecycle_manager", return_value=lifecycle):
        npcs = await _get_npc_occupants_in_room("room-1")
    assert npcs == [
        {"name": "Merchant", "disposition": NpcDisposition.SHOPKEEPER},
        {"name": "Rat", "disposition": NpcDisposition.AGGRESSIVE_MOB},
    ]


@pytest.mark.asyncio
async def test_skips_the_dead_and_the_unnamed() -> None:
    lifecycle = _lifecycle(
        dead=_npc("Corpse", "aggressive_mob", alive=False),
        nameless=_npc(None, "passive_mob"),
        live=_npc("Pigeon", "passive_mob"),
    )
    with patch("server.commands.look_npc._get_lifecycle_manager", return_value=lifecycle):
        npcs = await _get_npc_occupants_in_room("room-1")
    assert [npc["name"] for npc in npcs] == ["Pigeon"]


@pytest.mark.asyncio
async def test_an_unrecognised_type_is_listed_as_a_passive_mob() -> None:
    """One bad definition row must not drop an NPC from the room."""
    lifecycle = _lifecycle(odd=_npc("Mystery", "friendly"))
    with patch("server.commands.look_npc._get_lifecycle_manager", return_value=lifecycle):
        npcs = await _get_npc_occupants_in_room("room-1")
    assert npcs == [{"name": "Mystery", "disposition": NpcDisposition.PASSIVE_MOB}]


@pytest.mark.asyncio
async def test_no_lifecycle_manager_means_no_npcs() -> None:
    with patch("server.commands.look_npc._get_lifecycle_manager", return_value=None):
        assert await _get_npc_occupants_in_room("room-1") == []


@pytest.mark.asyncio
async def test_the_names_helper_is_the_same_list_without_dispositions() -> None:
    lifecycle = _lifecycle(a=_npc("Merchant", "shopkeeper"), b=_npc("Rat", "aggressive_mob"))
    with patch("server.commands.look_npc._get_lifecycle_manager", return_value=lifecycle):
        assert await _get_npcs_in_room("room-1") == ["Merchant", "Rat"]
