"""Unit tests for container_helpers_inventory_ops (extract, parse, validate, find in container)."""

from __future__ import annotations

import json
import uuid
from types import SimpleNamespace
from unittest.mock import MagicMock

import pytest

from server.commands.container_helpers_inventory_ops import (
    extract_items_from_container,
    filter_valid_items,
    find_item_in_container,
    parse_container_items,
    parse_json_string_items,
    resolve_container_id,
    validate_get_command_inputs,
    validate_put_command_inputs,
)


def test_extract_items_from_container_dict() -> None:
    cid = uuid.uuid4()
    items, out_cid = extract_items_from_container(
        {"items": [{"item_name": "x"}], "container_id": str(cid)},
        None,
    )
    assert out_cid == cid
    assert items == [{"item_name": "x"}]


def test_extract_items_from_container_items_json_attr() -> None:
    cid = uuid.uuid4()
    obj = SimpleNamespace(items_json=[{"n": 1}], container_instance_id=cid)
    items, out_cid = extract_items_from_container(obj, None)
    assert out_cid == cid
    assert items == [{"n": 1}]


def test_parse_json_string_items_valid() -> None:
    player = MagicMock()
    player.name = "p"
    raw = json.dumps([{"item_name": "a"}])
    out = parse_json_string_items(raw, None, player)
    assert out is not None
    parsed, _ = out
    assert parsed == [{"item_name": "a"}]


def test_parse_json_string_items_invalid_returns_none() -> None:
    player = MagicMock()
    player.name = "p"
    assert parse_json_string_items("{bad", None, player) is None


def test_filter_valid_items_drops_non_dict() -> None:
    player = MagicMock()
    player.name = "p"
    cid = uuid.uuid4()
    out = filter_valid_items([{"ok": True}, "no", 3], cid, player)
    assert len(out) == 1
    assert out[0] == {"ok": True}


def test_parse_container_items_full_pipeline() -> None:
    player = MagicMock()
    player.name = "p"
    cid = uuid.uuid4()
    items, out_cid = parse_container_items(
        {"items": [{"item_name": "Gem"}], "container_id": str(cid)},
        None,
        player,
    )
    assert out_cid == cid
    assert len(items) == 1


def test_resolve_container_id_explicit() -> None:
    c = uuid.uuid4()
    assert resolve_container_id({}, c) == c


def test_resolve_container_id_from_dict() -> None:
    u = uuid.uuid4()
    assert resolve_container_id({"container_id": str(u)}, None) == u


def test_find_item_in_container_by_index_and_name() -> None:
    rows = [{"item_name": "Apple"}, {"name": "Berry"}]
    a, i = find_item_in_container(rows, "1", MagicMock(), None)
    assert i == 0
    assert a == rows[0]
    berry_row, j = find_item_in_container(rows, "berry", MagicMock(), None)
    assert j == 1
    assert berry_row == rows[1]


@pytest.mark.asyncio
async def test_validate_put_command_inputs_missing_usage() -> None:
    player = MagicMock()
    player.name = "hero"
    player.get_inventory = MagicMock(return_value=[])
    cm = MagicMock()
    req = MagicMock()
    out = await validate_put_command_inputs({"item": "", "container": "bag"}, req, cm, player)
    assert isinstance(out, dict)
    assert "Usage" in out["result"]


@pytest.mark.asyncio
async def test_validate_put_command_inputs_no_container_service() -> None:
    player = MagicMock()
    player.name = "hero"
    player.get_inventory = MagicMock(return_value=[{"item_name": "rock"}])
    req = MagicMock()
    app = MagicMock()
    state = MagicMock()
    state.container_service = None
    app.state = state
    req.app = app
    cm = MagicMock()
    cm.room_manager = MagicMock()
    out = await validate_put_command_inputs(
        {"item": "rock", "container": "bag"},
        req,
        cm,
        player,
    )
    assert out == {"result": "Container service is unavailable."}


@pytest.mark.asyncio
async def test_validate_get_command_inputs_room_keyword() -> None:
    room_manager = object()
    cm = SimpleNamespace(room_manager=room_manager)
    out = await validate_get_command_inputs(
        {"item": "x", "container": "room"},
        MagicMock(),
        cm,
    )
    assert isinstance(out, tuple)
    item, cname, _, svc, rm = out
    assert item == "x"
    assert cname == "room"
    assert svc is None
    assert rm is room_manager
