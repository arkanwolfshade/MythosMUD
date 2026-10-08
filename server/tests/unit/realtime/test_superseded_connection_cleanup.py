"""
A WebSocket handler that ends after a newer session has replaced its socket must not tear the player down (#610).

Teardown (`disconnect_websocket`) is player-scoped: it closes every socket the player has registered and starts a
disconnect grace period. When a replaced session's old handler finished after the new socket registered, it closed
the new socket and later removed a connected player from their room.
"""

import uuid
from typing import cast
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.realtime.connection_manager import ConnectionManager
from server.realtime.websocket_handler_connection import cleanup_websocket_connection


class _FakeManager:
    """Just the surface cleanup consults, with real dictionary semantics (a MagicMock answers 'truthy' to all)."""

    def __init__(self, player_websockets: dict[uuid.UUID, list[str]]) -> None:
        self.player_websockets: dict[uuid.UUID, list[str]] = player_websockets
        self.disconnect_websocket: AsyncMock = AsyncMock()

    def has_websocket_connection(self, player_id: uuid.UUID) -> bool:
        return bool(self.player_websockets.get(player_id))


async def _cleanup(
    manager: _FakeManager, player_id: uuid.UUID, connection_id: str | None
) -> tuple[MagicMock, MagicMock]:
    """Run the real cleanup against the fake manager; return the follow and party services it may notify."""
    follow_hook, party_hook = MagicMock(), MagicMock()
    container = MagicMock(
        follow_service=MagicMock(on_player_disconnect=follow_hook),
        party_service=MagicMock(on_player_disconnect=party_hook),
    )
    with patch("server.container.get_container", return_value=container):
        await cleanup_websocket_connection(
            player_id, str(player_id), cast(ConnectionManager, cast(object, manager)), connection_id
        )
    return follow_hook, party_hook


@pytest.mark.asyncio
async def test_a_superseded_handler_leaves_the_live_session_alone() -> None:
    player_id = uuid.uuid4()
    manager = _FakeManager({player_id: ["new-connection"]})

    follow_hook, party_hook = await _cleanup(manager, player_id, "old-connection")

    manager.disconnect_websocket.assert_not_awaited()
    follow_hook.assert_not_called()
    party_hook.assert_not_called()


@pytest.mark.asyncio
async def test_a_handler_whose_own_socket_is_still_registered_tears_the_player_down() -> None:
    player_id = uuid.uuid4()
    manager = _FakeManager({player_id: ["conn-1"]})

    follow_hook, party_hook = await _cleanup(manager, player_id, "conn-1")

    manager.disconnect_websocket.assert_awaited_once_with(player_id)
    follow_hook.assert_called_once_with(player_id)
    party_hook.assert_called_once_with(player_id)


@pytest.mark.asyncio
async def test_a_handler_with_no_live_socket_left_still_cleans_up() -> None:
    """Nothing newer exists, so this is an ordinary disconnect and must run the usual cleanup."""
    player_id = uuid.uuid4()
    manager = _FakeManager({})

    _ = await _cleanup(manager, player_id, "old-connection")

    manager.disconnect_websocket.assert_awaited_once_with(player_id)


@pytest.mark.asyncio
async def test_callers_without_a_connection_id_keep_the_legacy_behaviour() -> None:
    player_id = uuid.uuid4()
    manager = _FakeManager({player_id: ["some-connection"]})

    _ = await _cleanup(manager, player_id, None)

    manager.disconnect_websocket.assert_awaited_once_with(player_id)
