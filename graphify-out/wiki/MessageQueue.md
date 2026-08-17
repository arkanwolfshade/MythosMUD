# MessageQueue

> 249 nodes

## Key Concepts

- **MessageQueue** (60 connections) — `server/realtime/message_queue.py`
- **RoomSubscriptionManager** (52 connections) — `server/realtime/room_subscription_manager.py`
- **test_connection_disconnection.py** (40 connections) — `server/tests/unit/realtime/test_connection_disconnection.py`
- **connection_disconnection.py** (35 connections) — `server/realtime/connection_disconnection.py`
- **_DisconnectConnectionManager** (26 connections) — `server/realtime/connection_disconnection.py`
- **test_connection_disconnection_websockets.py** (26 connections) — `server/tests/unit/realtime/test_connection_disconnection_websockets.py`
- **test_connection_initialization.py** (18 connections) — `server/tests/unit/realtime/test_connection_initialization.py`
- **UUID** (16 connections)
- **cleanup_websocket_disconnect()** (15 connections) — `server/realtime/connection_disconnection.py`
- **asyncio** (14 connections)
- **test_room_subscription_manager_npcs.py** (14 connections) — `server/tests/unit/realtime/test_room_subscription_manager_npcs.py`
- **disconnect_all_websockets_impl()** (13 connections) — `server/realtime/connection_disconnection.py`
- **disconnect_connection_by_id_impl()** (13 connections) — `server/realtime/connection_disconnection.py`
- **initialize_core_components()** (13 connections) — `server/realtime/connection_initialization.py`
- **safe_close_websocket_impl()** (13 connections) — `server/realtime/connection_websocket_close.py`
- **._canonical_room_id()** (13 connections) — `server/realtime/room_subscription_manager.py`
- **Any** (13 connections)
- **_cleanup_room_subscriptions()** (12 connections) — `server/realtime/connection_disconnection.py`
- **_track_disconnect_if_needed()** (12 connections) — `server/realtime/connection_disconnection.py`
- **.__init__()** (12 connections) — `server/realtime/connection_manager.py`
- **_cleanup_fully_disconnected_player()** (10 connections) — `server/realtime/connection_disconnection.py`
- **force_disconnect_player_impl()** (10 connections) — `server/realtime/connection_disconnection.py`
- **_apply_disconnect_side_effects()** (9 connections) — `server/realtime/connection_disconnection.py`
- **_cleanup_player_data()** (9 connections) — `server/realtime/connection_disconnection.py`
- **initialize_connection_state()** (9 connections) — `server/realtime/connection_initialization.py`
- *... and 224 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (54 shared connections)
- [test_message_queue.py](test_message_queue.py.md) (22 shared connections)
- [deque](deque.md) (15 shared connections)
- [RateLimiter](RateLimiter.md) (9 shared connections)
- [test_connection_session_management.py](test_connection_session_management.py.md) (8 shared connections)
- [ConnectionManager](ConnectionManager.md) (8 shared connections)
- [connection_manager_methods.py](connection_manager_methods.py.md) (6 shared connections)
- [connection_establishment.py](connection_establishment.py.md) (4 shared connections)
- [pytest.md](pytest.md.md) (3 shared connections)
- [GameStateProvider](GameStateProvider.md) (2 shared connections)
- [test_room_subscription_manager_helpers.py](test_room_subscription_manager_helpers.py.md) (2 shared connections)
- [MessageBroadcaster](MessageBroadcaster.md) (2 shared connections)

## Source Files

- `server/realtime/connection_disconnection.py`
- `server/realtime/connection_initialization.py`
- `server/realtime/connection_manager.py`
- `server/realtime/connection_websocket_close.py`
- `server/realtime/message_queue.py`
- `server/realtime/room_subscription_manager.py`
- `server/tests/unit/realtime/test_connection_disconnection.py`
- `server/tests/unit/realtime/test_connection_disconnection_websockets.py`
- `server/tests/unit/realtime/test_connection_initialization.py`
- `server/tests/unit/realtime/test_connection_manager_methods.py`
- `server/tests/unit/realtime/test_room_subscription_manager_npcs.py`

## Audit Trail

- EXTRACTED: 520 (90%)
- INFERRED: 57 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*