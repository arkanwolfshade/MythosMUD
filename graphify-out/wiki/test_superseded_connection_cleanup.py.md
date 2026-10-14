# test_superseded_connection_cleanup.py

> 17 nodes

## Key Concepts

- **test_superseded_connection_cleanup.py** (12 connections) — `server/tests/unit/realtime/test_superseded_connection_cleanup.py`
- **_cleanup()** (10 connections) — `server/tests/unit/realtime/test_superseded_connection_cleanup.py`
- **_FakeManager** (9 connections) — `server/tests/unit/realtime/test_superseded_connection_cleanup.py`
- **cleanup_websocket_connection()** (8 connections) — `server/realtime/websocket_handler_connection.py`
- **test_a_handler_with_no_live_socket_left_still_cleans_up()** (5 connections) — `server/tests/unit/realtime/test_superseded_connection_cleanup.py`
- **test_a_handler_whose_own_socket_is_still_registered_tears_the_player_down()** (4 connections) — `server/tests/unit/realtime/test_superseded_connection_cleanup.py`
- **test_a_superseded_handler_leaves_the_live_session_alone()** (4 connections) — `server/tests/unit/realtime/test_superseded_connection_cleanup.py`
- **test_callers_without_a_connection_id_keep_the_legacy_behaviour()** (4 connections) — `server/tests/unit/realtime/test_superseded_connection_cleanup.py`
- **asyncio** (4 connections)
- **UUID** (4 connections)
- **.has_websocket_connection()** (2 connections) — `server/tests/unit/realtime/test_superseded_connection_cleanup.py`
- **.__init__()** (2 connections) — `server/tests/unit/realtime/test_superseded_connection_cleanup.py`
- **Clean up connection, follow state, and party state on disconnect.…** (1 connections) — `server/realtime/websocket_handler_connection.py`
- **A WebSocket handler that ends after a newer session has replaced its socket…** (1 connections) — `server/tests/unit/realtime/test_superseded_connection_cleanup.py`
- **Just the surface cleanup consults, with real dictionary semantics (a MagicMock…** (1 connections) — `server/tests/unit/realtime/test_superseded_connection_cleanup.py`
- **Run the real cleanup against the fake manager; return the follow and party…** (1 connections) — `server/tests/unit/realtime/test_superseded_connection_cleanup.py`
- **Nothing newer exists, so this is an ordinary disconnect and must run the usual…** (1 connections) — `server/tests/unit/realtime/test_superseded_connection_cleanup.py`

## Relationships

- [websocket_initial_state.py](websocket_initial_state.py.md) (4 shared connections)
- [ConnectionManager](ConnectionManager.md) (2 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (1 shared connections)
- [websocket_handler.py](websocket_handler.py.md) (1 shared connections)
- [get_logger](get_logger.md) (1 shared connections)

## Source Files

- `server/realtime/websocket_handler_connection.py`
- `server/tests/unit/realtime/test_superseded_connection_cleanup.py`

## Audit Trail

- EXTRACTED: 39 (95%)
- INFERRED: 2 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*