"""Unit tests for container_helpers_inventory_find (search and room container lookup)."""

from __future__ import annotations

import uuid
from types import SimpleNamespace
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.commands.container_helpers_inventory_find import (
    check_item_matches_target,
    create_wearable_container,
    find_container_in_room,
    find_item_in_inventory,
    find_matching_equipped_containers,
    find_wearable_container,
    find_wearable_container_for_put,
    try_inner_container,
    try_inner_container_by_id,
    try_wearable_container_service,
    try_wearable_container_service_by_instance_id,
    try_wearable_container_service_by_name,
)


def test_find_item_in_inventory_by_index() -> None:
    inv = [
        {"item_name": "a"},
        {"name": "b"},
    ]
    item, idx = find_item_in_inventory(inv, "2")
    assert idx == 1
    assert item == {"name": "b"}


def test_find_item_in_inventory_by_name_substring() -> None:
    inv = [{"item_name": "Iron Sword"}]
    item, idx = find_item_in_inventory(inv, "sword")
    assert idx == 0
    assert item == inv[0]


def test_find_item_in_inventory_miss() -> None:
    inv = [{"item_name": "a"}]
    assert find_item_in_inventory(inv, "99") == (None, None)
    assert find_item_in_inventory(inv, "zzz") == (None, None)


def test_find_item_in_inventory_index_zero_invalid() -> None:
    inv = [{"item_name": "only"}]
    assert find_item_in_inventory(inv, "0") == (None, None)


def test_find_item_in_inventory_non_numeric_token_name_search() -> None:
    """ValueError from int() falls through to case-insensitive substring match."""
    inv = [{"item_name": "Lantern"}]
    item, idx = find_item_in_inventory(inv, "lan")
    assert idx == 0
    assert item == inv[0]


def test_find_item_in_inventory_uppercase_query() -> None:
    inv = [{"item_name": "rusty key"}]
    item, idx = find_item_in_inventory(inv, "KEY")
    assert idx == 0
    assert item == inv[0]


def test_check_item_matches_target_partial_name() -> None:
    """Substring match in item_name (player-typed targets)."""
    item = {"item_name": "Hiking Pack", "name": "x"}
    nm, sm = check_item_matches_target(item, "back", "hik")
    assert nm is True
    assert sm is False


def test_check_item_matches_target() -> None:
    item = {"item_name": "Backpack", "name": "x"}
    nm, sm = check_item_matches_target(item, "Back", "back")
    assert nm is True
    assert sm is True


def test_find_matching_equipped_containers_by_name() -> None:
    equipped = {
        "slot1": {"item_name": "Satchel", "item_id": "p1"},
    }
    out = find_matching_equipped_containers(equipped, "satchel")
    assert len(out) == 1
    assert out[0][0] == "slot1"


def test_find_matching_equipped_containers_inner_without_name_match() -> None:
    equipped = {"s": {"item_name": "Other", "inner_container": str(uuid.uuid4())}}
    out = find_matching_equipped_containers(equipped, "box")
    assert out == []


def test_try_inner_container_by_id_none() -> None:
    pers = MagicMock()
    assert try_inner_container_by_id(pers, None, "hand", "p") == (None, None)


def test_try_inner_container_by_id_resolves() -> None:
    cid = uuid.uuid4()
    pers = MagicMock()
    pers.get_container = MagicMock(return_value={"container_id": str(cid), "items": []})
    data, uid = try_inner_container_by_id(pers, str(cid), "hand", "player1")
    assert uid == cid
    assert data is not None
    assert data.get("items") == []


def test_find_container_in_room_with_metadata_name() -> None:
    rm = MagicMock()
    cid = uuid.uuid4()
    rm.get_containers = MagicMock(
        return_value=[
            {
                "container_id": str(cid),
                "metadata": {"name": "Wooden Chest"},
            },
        ],
    )
    c, uid = find_container_in_room(rm, "room1", "chest")
    assert uid == cid
    assert c is not None


def test_find_container_in_room_no_match() -> None:
    rm = MagicMock()
    rm.get_containers = MagicMock(return_value=[])
    assert find_container_in_room(rm, "room1", "x") == (None, None)


def test_find_container_in_room_non_dict_entries_skipped() -> None:
    rm = MagicMock()
    rm.get_containers = MagicMock(return_value=["bad", 1])
    assert find_container_in_room(rm, "room1", "x") == (None, None)


def test_find_container_in_room_get_containers_not_callable() -> None:
    rm = object()
    assert find_container_in_room(rm, "room1", "x") == (None, None)


def test_find_container_in_room_non_list_returns_empty() -> None:
    rm = MagicMock()
    rm.get_containers = MagicMock(return_value={"not": "list"})
    assert find_container_in_room(rm, "room1", "chest") == (None, None)


def test_check_item_matches_target_name_miss_slot_exact() -> None:
    item = {"item_name": "Battle Axe"}
    nm, sm = check_item_matches_target(item, "hand", "hand")
    assert nm is False
    assert sm is True


def test_find_matching_equipped_containers_prototype_and_item_id() -> None:
    eq1 = {"s1": {"item_name": "x", "prototype_id": "unique_gem_v2"}}
    out1 = find_matching_equipped_containers(eq1, "gem")
    assert len(out1) == 1
    eq2 = {"s2": {"item_name": "y", "item_id": "scroll_fire"}}
    out2 = find_matching_equipped_containers(eq2, "fire")
    assert len(out2) == 1


def test_find_matching_equipped_containers_inner_with_name_match() -> None:
    cid = str(uuid.uuid4())
    equipped = {"belt": {"item_name": "Bag", "inner_container": cid}}
    out = find_matching_equipped_containers(equipped, "bag")
    assert len(out) == 1
    assert out[0][0] == "belt"


def test_try_inner_container_by_id_invalid_uuid() -> None:
    assert try_inner_container_by_id(MagicMock(), "not-uuid", "s", "p") == (None, None)


def _player_for_wearable(equipped: dict[str, object]) -> MagicMock:
    p = MagicMock()
    p.player_id = uuid.uuid4()
    p.name = "hero"
    p.get_equipped_items = MagicMock(return_value=equipped)
    return p


@pytest.mark.asyncio
async def test_try_inner_container_resolves() -> None:
    cid = uuid.uuid4()
    pers = MagicMock()
    pers.get_container = MagicMock(return_value={"items": []})
    data, uid = await try_inner_container(pers, {"inner_container": str(cid)})
    assert uid == cid
    assert data == {"items": []}


@pytest.mark.asyncio
async def test_try_inner_container_missing_inner() -> None:
    assert await try_inner_container(MagicMock(), {}) == (None, None)


@pytest.mark.asyncio
async def test_try_inner_container_bad_inner_uuid() -> None:
    out = await try_inner_container(MagicMock(), {"inner_container": "not-a-uuid"})
    assert out == (None, None)


@pytest.mark.asyncio
async def test_try_inner_container_get_container_returns_none() -> None:
    cid = uuid.uuid4()
    pers = MagicMock()
    pers.get_container = MagicMock(return_value=None)
    assert await try_inner_container(pers, {"inner_container": str(cid)}) == (None, None)


@pytest.mark.asyncio
@patch("server.commands.container_helpers_inventory_find.get_shared_services")
async def test_try_wearable_container_service_finds_component(mock_gs: MagicMock) -> None:
    cid = uuid.uuid4()
    pers = MagicMock()
    pers.get_container = MagicMock(return_value={"data": True})
    comp = SimpleNamespace(
        metadata={"name": "field pack", "slot": "back"},
        container_id=str(cid),
    )
    wsvc = MagicMock()
    wsvc.get_wearable_containers_for_player = AsyncMock(return_value=[comp])
    mock_gs.return_value = (MagicMock(), wsvc, MagicMock())
    player = _player_for_wearable({})
    data, uid = await try_wearable_container_service(pers, MagicMock(), player, "back", "pack")
    assert uid == cid
    assert data == {"data": True}


@pytest.mark.asyncio
@patch(
    "server.commands.container_helpers_inventory_find.get_shared_services",
    side_effect=ValueError("no persistence"),
)
async def test_try_wearable_container_service_swallows_service_error(_mock_gs: MagicMock) -> None:
    player = _player_for_wearable({})
    assert await try_wearable_container_service(MagicMock(), MagicMock(), player, "b", "x") == (None, None)


@pytest.mark.asyncio
@patch("server.commands.container_helpers_inventory_find.get_shared_services")
async def test_create_wearable_container_uses_equip_dict_branch(mock_gs: MagicMock) -> None:
    cid = uuid.uuid4()
    wsvc = MagicMock()
    wsvc.handle_equip_wearable_container = AsyncMock(return_value={"container_id": str(cid)})
    mock_gs.return_value = (MagicMock(), wsvc, MagicMock())
    pers = MagicMock()
    pers.get_container = MagicMock(return_value={"from_db": True})
    player = _player_for_wearable({})
    data, uid = await create_wearable_container(pers, MagicMock(), player, "back", {"item_name": "Satchel"})
    assert uid == cid
    assert data == {"from_db": True}


@pytest.mark.asyncio
@patch("server.commands.container_helpers_inventory_find.get_shared_services")
async def test_create_wearable_container_fallback_when_equip_returns_non_dict(mock_gs: MagicMock) -> None:
    cid = uuid.uuid4()
    wsvc = MagicMock()
    wsvc.handle_equip_wearable_container = AsyncMock(return_value="noop")
    mock_gs.return_value = (MagicMock(), wsvc, MagicMock())
    pers = MagicMock()
    pers.create_container = MagicMock(return_value={"container_id": str(cid), "items": []})
    player = _player_for_wearable({})
    data, uid = await create_wearable_container(
        pers, MagicMock(), player, "back", {"item_name": "Pack", "item_id": "p1"}
    )
    assert uid == cid
    assert data == {"container_id": str(cid), "items": []}


@pytest.mark.asyncio
async def test_find_wearable_container_for_put_hits_inner_container() -> None:
    cid = uuid.uuid4()
    pers = MagicMock()
    pers.get_container = MagicMock(return_value={"inner": True})
    player = _player_for_wearable({"back": {"item_name": "Hiking Pack", "inner_container": str(cid)}})
    data, uid = await find_wearable_container_for_put(pers, MagicMock(), player, "pack")
    assert uid == cid
    assert data == {"inner": True}


@pytest.mark.asyncio
@patch("server.commands.container_helpers_inventory_find.get_shared_services")
async def test_find_wearable_container_for_put_creates_on_slot_only_match(
    mock_gs: MagicMock,
) -> None:
    cid = uuid.uuid4()
    wsvc = MagicMock()
    wsvc.handle_equip_wearable_container = AsyncMock(return_value=None)
    wsvc.get_wearable_containers_for_player = AsyncMock(return_value=[])
    mock_gs.return_value = (MagicMock(), wsvc, MagicMock())
    pers = MagicMock()
    pers.create_container = MagicMock(return_value={"container_id": str(cid), "items": []})
    player = _player_for_wearable(
        {"back": {"item_name": "Quiver", "item_id": "q1"}},
    )
    data, uid = await find_wearable_container_for_put(pers, MagicMock(), player, "back")
    assert uid == cid
    assert data is not None


@pytest.mark.asyncio
async def test_find_wearable_container_no_match_returns_none() -> None:
    player = _player_for_wearable({"hand": {"item_name": "Stick"}})
    assert await find_wearable_container(MagicMock(), MagicMock(), player, "missing") == (None, None)


@pytest.mark.asyncio
async def test_find_wearable_container_inner_id_short_circuits() -> None:
    cid = uuid.uuid4()
    pers = MagicMock()
    pers.get_container = MagicMock(return_value={"ok": True})
    player = _player_for_wearable(
        {"shoulder": {"item_name": "Messenger Bag", "inner_container": str(cid)}},
    )
    data, uid = await find_wearable_container(pers, MagicMock(), player, "bag")
    assert uid == cid
    assert data == {"ok": True}


@pytest.mark.asyncio
@patch("server.commands.container_helpers_inventory_find.get_shared_services")
async def test_find_wearable_container_resolves_via_wearable_instance_id(
    mock_gs: MagicMock,
) -> None:
    iid = uuid.uuid4()
    cid = uuid.uuid4()
    pers = MagicMock()
    pers.get_container = MagicMock(return_value={"svc": True})
    comp = SimpleNamespace(
        metadata={"item_instance_id": str(iid)},
        container_id=str(cid),
    )
    wsvc = MagicMock()
    wsvc.get_wearable_containers_for_player = AsyncMock(return_value=[comp])
    mock_gs.return_value = (MagicMock(), wsvc, MagicMock())
    player = _player_for_wearable(
        {"belt": {"item_name": "Pouch", "item_instance_id": str(iid)}},
    )
    data, uid = await find_wearable_container(pers, MagicMock(), player, "pouch")
    assert uid == cid
    assert data == {"svc": True}


@pytest.mark.asyncio
@patch("server.commands.container_helpers_inventory_find.get_shared_services")
async def test_find_wearable_container_falls_back_to_name_slot_match(
    mock_gs: MagicMock,
) -> None:
    iid = uuid.uuid4()
    cid = uuid.uuid4()
    pers = MagicMock()
    pers.get_container = MagicMock(return_value={"named": True})
    no_match = SimpleNamespace(metadata={"item_instance_id": "other"}, container_id=str(uuid.uuid4()))
    match = SimpleNamespace(
        metadata={"item_name": "Winter Cloak", "slot": "shoulder"},
        container_id=str(cid),
    )
    wsvc = MagicMock()
    wsvc.get_wearable_containers_for_player = AsyncMock(return_value=[no_match, match])
    mock_gs.return_value = (MagicMock(), wsvc, MagicMock())
    player = _player_for_wearable(
        {"shoulder": {"item_name": "Winter Cloak", "item_instance_id": str(iid)}},
    )
    data, uid = await find_wearable_container(pers, MagicMock(), player, "cloak")
    assert uid == cid
    assert data == {"named": True}


@pytest.mark.asyncio
@patch("server.commands.container_helpers_inventory_find.get_shared_services", side_effect=RuntimeError("boom"))
async def test_find_wearable_container_wearable_raises_returns_none(
    _mock_gs: MagicMock,
) -> None:
    pers = MagicMock()
    pers.get_container = MagicMock(return_value=None)
    player = _player_for_wearable(
        {"back": {"item_name": "Knapsack", "item_instance_id": str(uuid.uuid4())}},
    )
    assert await find_wearable_container(pers, MagicMock(), player, "knap") == (None, None)


@pytest.mark.asyncio
async def test_try_wearable_by_instance_id_match() -> None:
    iid = uuid.uuid4()
    cid = uuid.uuid4()
    pers = MagicMock()
    pers.get_container = MagicMock(return_value={"hit": 1})
    comp = SimpleNamespace(metadata={"item_instance_id": str(iid)}, container_id=str(cid))
    data, uid = await try_wearable_container_service_by_instance_id(pers, [comp], str(iid), "hero")
    assert uid == cid
    assert data == {"hit": 1}


@pytest.mark.asyncio
async def test_try_wearable_by_instance_id_empty_id() -> None:
    assert await try_wearable_container_service_by_instance_id(MagicMock(), [], "", "p") == (None, None)


@pytest.mark.asyncio
async def test_try_wearable_by_instance_id_no_components() -> None:
    assert await try_wearable_container_service_by_instance_id(MagicMock(), [], uuid.uuid4(), "p") == (None, None)


@pytest.mark.asyncio
async def test_try_wearable_by_name_slot_metadata() -> None:
    cid = uuid.uuid4()
    pers = MagicMock()
    # _get_container_pair treats empty dict as missing (`if not data`).
    pers.get_container = MagicMock(return_value={"items": []})
    comp = SimpleNamespace(
        metadata={"item_name": "Cloak", "slot": "shoulder"},
        container_id=str(cid),
    )
    data, uid = await try_wearable_container_service_by_name(pers, [comp], "shoulder", "cloak", "hero")
    assert uid == cid
    assert data == {"items": []}
