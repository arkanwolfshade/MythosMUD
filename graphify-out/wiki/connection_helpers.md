# connection helpers

> 82 nodes

## Key Concepts

- **test_connection_helpers_impl.py** (35 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **connection_helpers.py** (20 connections) — `server/realtime/connection_helpers.py`
- **convert_uuids_to_strings()** (16 connections) — `server/realtime/connection_helpers.py`
- **_optimize_payload()** (11 connections) — `server/realtime/connection_helpers.py`
- **_send_to_websockets()** (11 connections) — `server/realtime/connection_helpers.py`
- **send_personal_message_old_impl()** (11 connections) — `server/realtime/connection_helpers.py`
- **Any** (10 connections)
- **test_connection_helpers.py** (9 connections) — `server/tests/unit/realtime/test_connection_helpers.py`
- **_update_delivery_status()** (8 connections) — `server/realtime/connection_helpers.py`
- **handle_new_login_impl()** (7 connections) — `server/realtime/connection_helpers.py`
- **get_payload_optimizer()** (7 connections) — `server/realtime/payload_optimizer.py`
- **_queue_message_if_needed()** (6 connections) — `server/realtime/connection_helpers.py`
- **broadcast_room_event_impl()** (6 connections) — `server/realtime/connection_helpers.py`
- **broadcast_global_event_impl()** (6 connections) — `server/realtime/connection_helpers.py`
- **mark_player_seen_impl()** (6 connections) — `server/realtime/connection_helpers.py`
- **test_send_to_websockets_websocket_error()** (4 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **test_optimize_payload_optimization_failure()** (4 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **test_convert_uuids_to_strings_uuid()** (3 connections) — `server/tests/unit/realtime/test_connection_helpers.py`
- **test_convert_uuids_to_strings_dict()** (3 connections) — `server/tests/unit/realtime/test_connection_helpers.py`
- **test_convert_uuids_to_strings_list()** (3 connections) — `server/tests/unit/realtime/test_connection_helpers.py`
- **test_convert_uuids_to_strings_nested()** (3 connections) — `server/tests/unit/realtime/test_connection_helpers.py`
- **test_convert_uuids_to_strings_string()** (3 connections) — `server/tests/unit/realtime/test_connection_helpers.py`
- **test_convert_uuids_to_strings_int()** (3 connections) — `server/tests/unit/realtime/test_connection_helpers.py`
- **test_optimize_payload()** (3 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **test_send_to_websockets()** (3 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- *... and 57 more nodes in this community*

## Relationships

- [main()](main%28%29.md) (11 shared connections)
- [UUID](UUID.md) (3 shared connections)
- [initialize nats and combat services()](initialize_nats_and_combat_services%28%29.md) (2 shared connections)
- [AttributeError](AttributeError.md) (2 shared connections)
- [PersonalMessageSender](PersonalMessageSender.md) (1 shared connections)
- [PayloadOptimizer](PayloadOptimizer.md) (1 shared connections)

## Source Files

- `server/realtime/connection_helpers.py`
- `server/realtime/payload_optimizer.py`
- `server/tests/unit/realtime/test_connection_helpers.py`
- `server/tests/unit/realtime/test_connection_helpers_impl.py`

## Audit Trail

- EXTRACTED: 293 (98%)
- INFERRED: 7 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*