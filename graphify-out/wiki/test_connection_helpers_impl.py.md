# test_connection_helpers_impl.py

> 82 nodes · cohesion 0.04

## Key Concepts

- **test_connection_helpers_impl.py** (35 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **connection_helpers.py** (21 connections) — `server/realtime/connection_helpers.py`
- **send_personal_message_old_impl()** (13 connections) — `server/realtime/connection_helpers.py`
- **_optimize_payload()** (11 connections) — `server/realtime/connection_helpers.py`
- **_send_to_websockets()** (11 connections) — `server/realtime/connection_helpers.py`
- **Any** (10 connections)
- **handle_new_login_impl()** (9 connections) — `server/realtime/connection_helpers.py`
- **mark_player_seen_impl()** (8 connections) — `server/realtime/connection_helpers.py`
- **_update_delivery_status()** (8 connections) — `server/realtime/connection_helpers.py`
- **PayloadOptimizer** (8 connections) — `server/realtime/payload_optimizer.py`
- **get_payload_optimizer()** (7 connections) — `server/realtime/payload_optimizer.py`
- **broadcast_global_event_impl()** (6 connections) — `server/realtime/connection_helpers.py`
- **broadcast_room_event_impl()** (6 connections) — `server/realtime/connection_helpers.py`
- **_queue_message_if_needed()** (6 connections) — `server/realtime/connection_helpers.py`
- **.send_personal_message_old()** (5 connections) — `server/realtime/connection_manager.py`
- **.optimize_payload()** (5 connections) — `server/realtime/payload_optimizer.py`
- **.handle_new_login()** (4 connections) — `server/realtime/connection_manager.py`
- **.mark_player_seen()** (4 connections) — `server/realtime/connection_manager.py`
- **.compress_payload()** (4 connections) — `server/realtime/payload_optimizer.py`
- **.get_payload_size()** (4 connections) — `server/realtime/payload_optimizer.py`
- **Any** (4 connections)
- **test_optimize_payload_optimization_failure()** (4 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **test_send_to_websockets_websocket_error()** (4 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **.create_incremental_update()** (3 connections) — `server/realtime/payload_optimizer.py`
- **test_broadcast_global_event_impl()** (3 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- *... and 57 more nodes in this community*

## Relationships

- [convert_uuids_to_strings](convert_uuids_to_strings.md) (9 shared connections)
- [ConnectionManager](ConnectionManager.md) (8 shared connections)
- [DatabaseError](DatabaseError.md) (6 shared connections)
- [get_logger](get_logger.md) (5 shared connections)
- [connection_manager.py](connection_manager.py.md) (4 shared connections)
- [UUID](UUID.md) (4 shared connections)
- [CombatService](CombatService.md) (2 shared connections)
- [exceptions.py](exceptions.py.md) (1 shared connections)
- [PersonalMessageSender](PersonalMessageSender.md) (1 shared connections)

## Source Files

- `server/realtime/connection_helpers.py`
- `server/realtime/connection_manager.py`
- `server/realtime/payload_optimizer.py`
- `server/tests/unit/realtime/test_connection_helpers_impl.py`

## Audit Trail

- EXTRACTED: 285 (98%)
- INFERRED: 7 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*