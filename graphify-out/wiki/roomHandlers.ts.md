# roomHandlers.ts

> 34 nodes

## Key Concepts

- **test_connection_disconnection_websockets.py** (26 connections) — `server/tests/unit/realtime/test_connection_disconnection_websockets.py`
- **disconnect_connection_by_id_impl()** (12 connections) — `server/realtime/connection_disconnection.py`
- **_cleanup_fully_disconnected_player()** (10 connections) — `server/realtime/connection_disconnection.py`
- **asyncio** (8 connections)
- **_session_cleanup_manager()** (5 connections) — `server/tests/unit/realtime/test_connection_disconnection_websockets.py`
- **test_cleanup_websocket_disconnect_clears_session_tracking()** (5 connections) — `server/tests/unit/realtime/test_connection_disconnection_websockets.py`
- **test_disconnect_connection_by_id_impl_websocket()** (5 connections) — `server/tests/unit/realtime/test_connection_disconnection_websockets.py`
- **mock_manager()** (4 connections) — `server/tests/unit/realtime/test_connection_disconnection_websockets.py`
- **test_cleanup_fully_disconnected_player_clears_session_tracking()** (4 connections) — `server/tests/unit/realtime/test_connection_disconnection_websockets.py`
- **test_cleanup_fully_disconnected_player_keeps_session_while_connected()** (4 connections) — `server/tests/unit/realtime/test_connection_disconnection_websockets.py`
- **test_cleanup_websocket_disconnect_continues_after_close_error()** (4 connections) — `server/tests/unit/realtime/test_connection_disconnection_websockets.py`
- **test_disconnect_connection_by_id_impl_not_found()** (4 connections) — `server/tests/unit/realtime/test_connection_disconnection_websockets.py`
- **test_safe_close_websocket_swallows_websocket_disconnect()** (4 connections) — `server/tests/unit/realtime/test_connection_disconnection_websockets.py`
- **testdisconnect_all_websockets_impl_continues_after_none_websocket()** (4 connections) — `server/tests/unit/realtime/test_connection_disconnection_websockets.py`
- **testdisconnect_all_websockets_impl_empty_list()** (4 connections) — `server/tests/unit/realtime/test_connection_disconnection_websockets.py`
- **testdisconnect_all_websockets_impl_idempotent_second_pass()** (4 connections) — `server/tests/unit/realtime/test_connection_disconnection_websockets.py`
- **mock_safe_close_websocket()** (3 connections) — `server/tests/unit/realtime/test_connection_disconnection_websockets.py`
- **fixture** (2 connections)
- **UUID** (2 connections)
- **Remove player-scoped tracking when no websocket connections remain.** (1 connections) — `server/realtime/connection_disconnection.py`
- **Disconnect a specific connection by its ID. Args: connection_id: The connection…** (1 connections) — `server/realtime/connection_disconnection.py`
- **Unit tests for connection disconnection websocket functions. Tests the…** (1 connections) — `server/tests/unit/realtime/test_connection_disconnection_websockets.py`
- **Test disconnect_connection_by_id_impl() disconnects websocket connection.** (1 connections) — `server/tests/unit/realtime/test_connection_disconnection_websockets.py`
- **Regression: e2e logout hit WebSocketDisconnect on close and aborted leave…** (1 connections) — `server/tests/unit/realtime/test_connection_disconnection_websockets.py`
- **Close failures must not skip intentional leave tracking / room cleanup.** (1 connections) — `server/tests/unit/realtime/test_connection_disconnection_websockets.py`
- *... and 9 more nodes in this community*

## Relationships

- [FeatureFlagService](FeatureFlagService.md) (18 shared connections)
- [generate_invites_db.py](generate_invites_db.py.md) (3 shared connections)
- [NATSRetryHandler](NATSRetryHandler.md) (2 shared connections)
- [chat_service.py](chat_service.py.md) (2 shared connections)
- [_parse_env_list](_parse_env_list.md) (2 shared connections)
- [PopulationStats](PopulationStats.md) (1 shared connections)
- [ContainerComponent](ContainerComponent.md) (1 shared connections)

## Source Files

- `server/realtime/connection_disconnection.py`
- `server/tests/unit/realtime/test_connection_disconnection_websockets.py`

## Audit Trail

- EXTRACTED: 77 (97%)
- INFERRED: 2 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*