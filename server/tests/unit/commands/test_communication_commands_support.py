"""Unit tests for communication_commands_support helpers."""

from types import SimpleNamespace
from unittest.mock import MagicMock

import pytest

from server.commands.communication_commands_support import (
    app_from_request,
    chat_result_map,
    get_pose_persistence,
    get_services_from_container,
    message_id_from_result,
    primary_id,
)


def test_app_from_request_none():
    assert app_from_request(None) is None


def test_app_from_request_with_app():
    app_obj: object = object()
    req = SimpleNamespace(app=app_obj)
    assert app_from_request(req) is app_obj


def test_primary_id_prefers_id():
    ent = MagicMock()
    ent.id = "a"
    ent.player_id = "b"
    assert primary_id(ent) == "a"


def test_primary_id_falls_back_to_player_id():
    ent = MagicMock()
    ent.id = None
    ent.player_id = "pid"
    assert primary_id(ent) == "pid"


def test_get_services_from_container_no_app():
    assert get_services_from_container(None) == (None, None, None)


def test_get_services_from_container_via_container():
    container = SimpleNamespace(player_service="ps", chat_service="cs", user_manager="um")
    state = SimpleNamespace(container=container)
    app = SimpleNamespace(state=state)
    ps, cs, um = get_services_from_container(app)
    assert ps == "ps"
    assert cs == "cs"
    assert um == "um"


def test_get_services_from_container_state_fallback():
    st = SimpleNamespace(
        container=None,
        player_service="ps2",
        chat_service="cs2",
        user_manager="um2",
    )
    app = SimpleNamespace(state=st)
    ps, cs, um = get_services_from_container(app)
    assert ps == "ps2"
    assert cs == "cs2"
    assert um == "um2"


def test_get_pose_persistence_from_container():
    container = SimpleNamespace(async_persistence="ap")
    state = SimpleNamespace(container=container)
    app = SimpleNamespace(state=state)
    assert get_pose_persistence(app) == "ap"


def test_get_pose_persistence_state_fallback():
    state = SimpleNamespace(container=None, persistence="pers")
    app = SimpleNamespace(state=state)
    assert get_pose_persistence(app) == "pers"


def test_chat_result_map_dict():
    m = chat_result_map({"ok": True})
    assert m.get("ok") is True


def test_chat_result_map_non_dict():
    m = chat_result_map("nope")
    assert m == {}


def test_message_id_from_result_nested():
    mid = message_id_from_result({"message": {"id": "x"}})
    assert mid == "x"


@pytest.mark.parametrize("payload", [{"message": "text"}, {}])
def test_message_id_from_result_no_id(payload: dict[str, object]):
    assert message_id_from_result(payload) is None
