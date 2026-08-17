# test_connection_helpers_impl.py

> 97 nodes

## Key Concepts

- **test_connection_helpers_impl.py** (38 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **connection_helpers.py** (22 connections) — `server/realtime/connection_helpers.py`
- **convert_uuids_to_strings()** (18 connections) — `server/realtime/connection_helpers.py`
- **send_personal_message_old_impl()** (12 connections) — `server/realtime/connection_helpers.py`
- **asyncio** (12 connections)
- **_send_to_websockets()** (11 connections) — `server/realtime/connection_helpers.py`
- **handle_new_login_impl()** (10 connections) — `server/realtime/connection_helpers.py`
- **_optimize_payload()** (10 connections) — `server/realtime/connection_helpers.py`
- **Any** (10 connections)
- **test_connection_helpers.py** (9 connections) — `server/tests/unit/realtime/test_connection_helpers.py`
- **_update_delivery_status()** (8 connections) — `server/realtime/connection_helpers.py`
- **mark_player_seen_impl()** (7 connections) — `server/realtime/connection_helpers.py`
- **broadcast_global_event_impl()** (6 connections) — `server/realtime/connection_helpers.py`
- **broadcast_room_event_impl()** (6 connections) — `server/realtime/connection_helpers.py`
- **_queue_message_if_needed()** (6 connections) — `server/realtime/connection_helpers.py`
- **test_send_to_websockets_websocket_error()** (5 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **.handle_new_login()** (4 connections) — `server/realtime/connection_manager.py`
- **.mark_player_seen()** (4 connections) — `server/realtime/connection_manager.py`
- **.send_personal_message_old()** (4 connections) — `server/realtime/connection_manager.py`
- **test_broadcast_global_event_impl()** (4 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **test_broadcast_room_event_impl()** (4 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **test_handle_new_login_impl()** (4 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **test_handle_new_login_impl_cancels_orphan_rest_countdown()** (4 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **test_optimize_payload_optimization_failure()** (4 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **test_send_personal_message_old_impl()** (4 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- *... and 72 more nodes in this community*

## Relationships

- [ConnectionManager](ConnectionManager.md) (8 shared connections)
- [build_event](build_event.md) (3 shared connections)
- [UUID](UUID.md) (3 shared connections)
- [get_logger](get_logger.md) (3 shared connections)
- [AliasStorage](AliasStorage.md) (2 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (2 shared connections)
- [PayloadOptimizer](PayloadOptimizer.md) (2 shared connections)
- [AttributeError](AttributeError.md) (2 shared connections)
- [connection_manager_methods.py](connection_manager_methods.py.md) (1 shared connections)
- [DatabaseError](DatabaseError.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/realtime/connection_helpers.py`
- `server/realtime/connection_manager.py`
- `server/tests/unit/realtime/test_connection_helpers.py`
- `server/tests/unit/realtime/test_connection_helpers_impl.py`

## Audit Trail

- EXTRACTED: 188 (99%)
- INFERRED: 2 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*