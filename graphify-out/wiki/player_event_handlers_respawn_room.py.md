# player_event_handlers_respawn_room.py

> 65 nodes · cohesion 0.05

## Key Concepts

- **test_connection_helpers_impl.py** (37 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **send_personal_message_old_impl()** (12 connections) — `server/realtime/connection_helpers.py`
- **asyncio** (12 connections)
- **_send_to_websockets()** (11 connections) — `server/realtime/connection_helpers.py`
- **_optimize_payload()** (10 connections) — `server/realtime/connection_helpers.py`
- **Any** (10 connections)
- **_update_delivery_status()** (8 connections) — `server/realtime/connection_helpers.py`
- **mark_player_seen_impl()** (7 connections) — `server/realtime/connection_helpers.py`
- **broadcast_global_event_impl()** (6 connections) — `server/realtime/connection_helpers.py`
- **broadcast_room_event_impl()** (6 connections) — `server/realtime/connection_helpers.py`
- **_queue_message_if_needed()** (6 connections) — `server/realtime/connection_helpers.py`
- **test_send_to_websockets_websocket_error()** (5 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **.mark_player_seen()** (4 connections) — `server/realtime/connection_manager.py`
- **test_broadcast_global_event_impl()** (4 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **test_broadcast_room_event_impl()** (4 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **test_handle_new_login_impl()** (4 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **test_handle_new_login_impl_cancels_orphan_rest_countdown()** (4 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **test_optimize_payload_optimization_failure()** (4 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **test_optimize_payload_too_large()** (4 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **test_send_personal_message_old_impl()** (4 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **test_send_personal_message_old_impl_no_connections()** (4 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **test_send_to_websockets()** (4 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **test_send_to_websockets_inactive_connection()** (4 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **test_send_to_websockets_no_connections()** (4 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **test_send_to_websockets_none_websocket()** (4 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- *... and 40 more nodes in this community*

## Relationships

- [Room](Room.md) (13 shared connections)
- [enum](enum.md) (7 shared connections)
- [ChatService](ChatService.md) (3 shared connections)
- [.publish_with_pool](publish_with_pool.md) (2 shared connections)
- [connection_initialization.py](connection_initialization.py.md) (2 shared connections)
- [security.ts](security.ts.md) (2 shared connections)
- [processing.py](processing.py.md) (1 shared connections)
- [test_lucidity_recovery_commands.py](test_lucidity_recovery_commands.py.md) (1 shared connections)

## Source Files

- `server/realtime/connection_helpers.py`
- `server/realtime/connection_manager.py`
- `server/tests/unit/realtime/test_connection_helpers_impl.py`

## Audit Trail

- EXTRACTED: 132 (98%)
- INFERRED: 3 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*