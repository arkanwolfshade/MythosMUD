"""Unit tests for connection_manager_lazy's lazy attribute resolver."""

import pytest

from server.realtime import connection_manager_api
from server.realtime.connection_manager_lazy import resolve_lazy_attr


@pytest.mark.parametrize(
    "name",
    [
        "broadcast_game_event",
        "send_game_event",
        "send_player_status_update",
        "send_room_description",
        "send_room_event",
        "send_system_notification",
    ],
)
def test_resolve_lazy_attr_returns_api_function(name: str) -> None:
    """Each known lazy attribute resolves to the matching connection_manager_api export."""
    result = resolve_lazy_attr(name, "server.realtime.connection_manager")
    assert result is getattr(connection_manager_api, name)


def test_resolve_lazy_attr_unknown_name_raises_attribute_error() -> None:
    """An unrecognized attribute name raises AttributeError naming the module and attribute."""
    with pytest.raises(AttributeError, match="module 'server.realtime.connection_manager' has no attribute 'bogus'"):
        _ = resolve_lazy_attr("bogus", "server.realtime.connection_manager")
