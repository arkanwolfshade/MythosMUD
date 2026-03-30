"""Unit tests for container_helpers_inventory_ops (extract, parse, validate, find in container)."""

from __future__ import annotations

import json
import uuid
from types import SimpleNamespace
from typing import cast, final
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.commands.container_helpers_inventory_ops import (
    _coerce_transfer_quantity,
    _int_transfer_qty,
    extract_items_from_container,
    filter_valid_items,
    find_item_in_container,
    parse_container_items,
    parse_json_string_items,
    resolve_container_id,
    transfer_item_from_container,
    transfer_item_to_container,
    validate_get_command_inputs,
    validate_put_command_inputs,
)


def test_coerce_transfer_quantity_int_and_str() -> None:
    assert _coerce_transfer_quantity(7) == 7
    assert _coerce_transfer_quantity("  14  ") == 14
    assert _coerce_transfer_quantity("") == 1
    assert _coerce_transfer_quantity("   ") == 1
    assert _coerce_transfer_quantity("not-a-number") == 1


def test_coerce_transfer_quantity_bool_is_one() -> None:
    """JSON/bools must not use int(True)==1 for game quantities; treat as default 1."""
    assert _coerce_transfer_quantity(True) == 1
    assert _coerce_transfer_quantity(False) == 1


def test_coerce_transfer_quantity_float_truncates_toward_zero() -> None:
    assert _coerce_transfer_quantity(3.9) == 3
    assert _coerce_transfer_quantity(-2.1) == -2


def test_coerce_transfer_quantity_unknown_type_defaults() -> None:
    assert _coerce_transfer_quantity([]) == 1
    assert _coerce_transfer_quantity({"q": 3}) == 1


def test_int_transfer_qty_uses_explicit_quantity_over_item() -> None:
    item = {"quantity": 99}
    assert _int_transfer_qty("5", item) == 5
    assert _int_transfer_qty(2, item) == 2


def test_int_transfer_qty_falsy_quantity_falls_back_to_item() -> None:
    """Empty string is falsy: use item quantity (untyped JSON often uses str)."""
    assert _int_transfer_qty("", {"quantity": "3"}) == 3


def test_int_transfer_qty_zero_quantity_falls_back_to_item() -> None:
    """0 is falsy in `quantity if quantity`; coercer still maps to item line."""
    assert _int_transfer_qty(0, {"quantity": 4}) == 4


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


def _player_with_inventory(player_id: uuid.UUID) -> MagicMock:
    player = MagicMock()
    player.player_id = player_id
    player.name = "hero"
    player.get_inventory = MagicMock(return_value=[])
    player.set_inventory = MagicMock()
    return player


@pytest.mark.asyncio
async def test_transfer_item_to_container_success_uses_token_from_service() -> None:
    cid = uuid.uuid4()
    pid = uuid.uuid4()
    player = _player_with_inventory(pid)
    token = object()
    transfer_to = AsyncMock(return_value={"ok": True})
    container_service = MagicMock()
    container_service.get_container_token = MagicMock(return_value=token)
    container_service.transfer_to_container = transfer_to
    persistence = MagicMock()
    iid = uuid.uuid4()
    prototype = uuid.uuid4()
    item_found: dict[str, object] = {
        "item_instance_id": iid,
        "prototype_id": prototype,
        "quantity": 3,
    }
    result = await transfer_item_to_container(container_service, persistence, player, cid, item_found, None)
    assert result == {"success": True, "transfer_quantity": 3}
    transfer_to.assert_awaited_once()
    ensure_mock: MagicMock = cast(MagicMock, persistence.ensure_item_instance)
    ensure_mock.assert_called_once()


@pytest.mark.asyncio
async def test_transfer_item_to_container_coerces_string_quantity() -> None:
    cid = uuid.uuid4()
    pid = uuid.uuid4()
    player = _player_with_inventory(pid)
    transfer_to = AsyncMock(return_value=True)
    container_service = MagicMock()
    container_service.get_container_token = MagicMock(return_value=object())
    container_service.transfer_to_container = transfer_to
    item_found: dict[str, object] = {
        "item_instance_id": uuid.uuid4(),
        "item_id": uuid.uuid4(),
        "quantity": 1,
    }
    result = await transfer_item_to_container(
        container_service,
        MagicMock(),
        player,
        cid,
        item_found,
        " 14 ",
    )
    assert result["success"] is True
    assert result["transfer_quantity"] == 14


@pytest.mark.asyncio
async def test_transfer_item_to_container_missing_item_identifiers() -> None:
    cid = uuid.uuid4()
    player = _player_with_inventory(uuid.uuid4())
    container_service = MagicMock()
    container_service.get_container_token = MagicMock(return_value=object())
    result = await transfer_item_to_container(
        container_service,
        MagicMock(),
        player,
        cid,
        {"quantity": 1},
        None,
    )
    assert result == {"error": "Error: Item is missing required identification fields."}


@pytest.mark.asyncio
async def test_transfer_item_to_container_open_container_when_no_token() -> None:
    cid = uuid.uuid4()
    pid = uuid.uuid4()
    player = _player_with_inventory(pid)
    token = object()

    async def open_container(_cid: object, _pid: object) -> dict[str, object]:
        return {"mutation_token": token}

    container_service = MagicMock()
    container_service.get_container_token = MagicMock(return_value=None)
    container_service.open_container = open_container
    container_service.transfer_to_container = AsyncMock(return_value=None)

    item_found: dict[str, object] = {
        "item_instance_id": uuid.uuid4(),
        "item_id": uuid.uuid4(),
    }
    result = await transfer_item_to_container(container_service, MagicMock(), player, cid, item_found, None)
    assert result["success"] is True


@pytest.mark.asyncio
async def test_transfer_item_to_container_service_unavailable_no_open() -> None:
    cid = uuid.uuid4()
    player = _player_with_inventory(uuid.uuid4())
    container_service = MagicMock()
    container_service.get_container_token = MagicMock(return_value=None)
    container_service.open_container = None
    result = await transfer_item_to_container(
        container_service,
        MagicMock(),
        player,
        cid,
        {"item_instance_id": uuid.uuid4(), "item_id": uuid.uuid4()},
        None,
    )
    assert result == {"error": "Cannot access container: service unavailable"}


@final
class _ContainerSvcTokenOnly:
    """Stub with get_container_token but no transfer_to_container (not MagicMock: children are callable by default)."""

    def __init__(self, token: object) -> None:
        self._token = token

    def get_container_token(self, *_a: object, **_k: object) -> object:
        return self._token


@pytest.mark.asyncio
async def test_transfer_item_to_container_no_transfer_to_method() -> None:
    cid = uuid.uuid4()
    player = _player_with_inventory(uuid.uuid4())
    container_service = _ContainerSvcTokenOnly(object())
    result = await transfer_item_to_container(
        container_service,
        MagicMock(),
        player,
        cid,
        {"item_instance_id": uuid.uuid4(), "item_id": uuid.uuid4()},
        None,
    )
    assert result == {"error": "Container transfer is unavailable."}


@pytest.mark.asyncio
async def test_transfer_item_to_container_transfer_raises() -> None:
    cid = uuid.uuid4()
    player = _player_with_inventory(uuid.uuid4())

    async def boom(**_kwargs: object) -> None:
        raise RuntimeError("dup detected")

    container_service = MagicMock()
    container_service.get_container_token = MagicMock(return_value=object())
    container_service.transfer_to_container = boom
    result = await transfer_item_to_container(
        container_service,
        MagicMock(),
        player,
        cid,
        {"item_instance_id": uuid.uuid4(), "item_id": uuid.uuid4()},
        None,
    )
    assert result == {"error": "dup detected"}


@pytest.mark.asyncio
@patch("server.commands.inventory_command_helpers.persist_player", new_callable=AsyncMock)
async def test_transfer_item_from_container_success_updates_inventory(
    mock_persist: AsyncMock,
) -> None:
    cid = uuid.uuid4()
    pid = uuid.uuid4()
    player = _player_with_inventory(pid)
    new_rows = [{"item_name": "gem", "quantity": 1}]
    transfer_from = AsyncMock(return_value={"player_inventory": new_rows})
    container_service = MagicMock()
    container_service.get_container_token = MagicMock(return_value=object())
    container_service.transfer_from_container = transfer_from
    mock_persist.return_value = None
    item_found: dict[str, object] = {"item_name": "gem", "quantity": 1, "item_id": uuid.uuid4()}
    result = await transfer_item_from_container(container_service, MagicMock(), player, cid, item_found, "2")
    assert result["success"] is True
    assert result["transfer_quantity"] == 2
    assert result["item_display_name"] == "gem"
    set_inv: MagicMock = cast(MagicMock, player.set_inventory)
    set_inv.assert_called_once_with(new_rows)
    mock_persist.assert_awaited_once()


@pytest.mark.asyncio
@patch("server.commands.inventory_command_helpers.persist_player", new_callable=AsyncMock)
async def test_transfer_item_from_container_persist_failure_returns_error(
    mock_persist: AsyncMock,
) -> None:
    cid = uuid.uuid4()
    pid = uuid.uuid4()
    player = _player_with_inventory(pid)
    container_service = MagicMock()
    container_service.get_container_token = MagicMock(return_value=object())
    container_service.transfer_from_container = AsyncMock(return_value={"player_inventory": []})
    mock_persist.return_value = {"result": "save failed"}
    item_found: dict[str, object] = {"item_instance_id": uuid.uuid4(), "item_id": uuid.uuid4()}
    result = await transfer_item_from_container(container_service, MagicMock(), player, cid, item_found, None)
    assert result == {"result": "save failed"}


@pytest.mark.asyncio
async def test_transfer_item_from_container_no_transfer_from() -> None:
    cid = uuid.uuid4()
    player = _player_with_inventory(uuid.uuid4())
    container_service = _ContainerSvcTokenOnly(object())
    result = await transfer_item_from_container(
        container_service,
        MagicMock(),
        player,
        cid,
        {"item_instance_id": uuid.uuid4(), "item_id": uuid.uuid4()},
        None,
    )
    assert result == {"error": "Container transfer is unavailable."}


@pytest.mark.asyncio
async def test_transfer_item_from_container_transfer_raises() -> None:
    cid = uuid.uuid4()
    player = _player_with_inventory(uuid.uuid4())

    async def boom(**_kwargs: object) -> None:
        raise ValueError("svc")

    container_service = MagicMock()
    container_service.get_container_token = MagicMock(return_value=object())
    container_service.transfer_from_container = boom
    with patch(
        "server.commands.inventory_command_helpers.persist_player",
        new_callable=AsyncMock,
    ) as mock_persist:
        mock_persist.return_value = None
        result = await transfer_item_from_container(
            container_service,
            MagicMock(),
            player,
            cid,
            {"item_instance_id": uuid.uuid4(), "item_id": uuid.uuid4()},
            None,
        )
    assert result == {"error": "svc"}


@pytest.mark.asyncio
async def test_transfer_item_from_container_inventory_rows_fallback_non_dict_result() -> None:
    """Non-dict transfer result uses existing inventory list for set_inventory."""
    cid = uuid.uuid4()
    pid = uuid.uuid4()
    player = _player_with_inventory(pid)
    fallback = [{"item_name": "keep"}]
    player.get_inventory = MagicMock(return_value=fallback)
    container_service = MagicMock()
    container_service.get_container_token = MagicMock(return_value=object())
    container_service.transfer_from_container = AsyncMock(return_value="not-a-dict")
    with patch(
        "server.commands.inventory_command_helpers.persist_player",
        new_callable=AsyncMock,
    ) as mock_persist:
        mock_persist.return_value = None
        result = await transfer_item_from_container(
            container_service,
            MagicMock(),
            player,
            cid,
            {"item_name": "x", "item_id": uuid.uuid4()},
            None,
        )
    assert result["success"] is True
    set_inv_fb: MagicMock = cast(MagicMock, player.set_inventory)
    set_inv_fb.assert_called_once_with(fallback)
