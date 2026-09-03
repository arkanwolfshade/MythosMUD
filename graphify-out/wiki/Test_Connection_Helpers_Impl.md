# Test Connection Helpers Impl

> 85 nodes

## Key Concepts

- **test_connection_helpers_impl.py** (38 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **convert_uuids_to_strings()** (18 connections) — `server/realtime/connection_helpers.py`
- **send_personal_message_old_impl()** (12 connections) — `server/realtime/connection_helpers.py`
- **asyncio** (12 connections)
- **_send_to_websockets()** (11 connections) — `server/realtime/connection_helpers.py`
- **_optimize_payload()** (10 connections) — `server/realtime/connection_helpers.py`
- **Any** (10 connections)
- **test_connection_helpers.py** (9 connections) — `server/tests/unit/realtime/test_connection_helpers.py`
- **_update_delivery_status()** (8 connections) — `server/realtime/connection_helpers.py`
- **broadcast_global_event_impl()** (6 connections) — `server/realtime/connection_helpers.py`
- **broadcast_room_event_impl()** (6 connections) — `server/realtime/connection_helpers.py`
- **_queue_message_if_needed()** (6 connections) — `server/realtime/connection_helpers.py`
- **test_send_to_websockets_websocket_error()** (5 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **test_broadcast_global_event_impl()** (4 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **test_broadcast_room_event_impl()** (4 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **test_handle_new_login_impl()** (4 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **test_handle_new_login_impl_cancels_orphan_rest_countdown()** (4 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **test_optimize_payload_optimization_failure()** (4 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **test_send_personal_message_old_impl()** (4 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **test_send_personal_message_old_impl_no_connections()** (4 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **test_send_to_websockets()** (4 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **test_send_to_websockets_inactive_connection()** (4 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **test_send_to_websockets_no_connections()** (4 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **test_send_to_websockets_none_websocket()** (4 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **test_send_to_websockets_skips_disconnected_client_state()** (4 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- *... and 60 more nodes in this community*

## Relationships

- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (19 shared connections)
- [Test Envelope](Test_Envelope.md) (2 shared connections)
- [Test Combat Persistence Handler Persistence](Test_Combat_Persistence_Handler_Persistence.md) (2 shared connections)
- [Connection Manager Methods](Connection_Manager_Methods.md) (1 shared connections)
- [Test Payload Optimizer](Test_Payload_Optimizer.md) (1 shared connections)
- [Connection Manager](Connection_Manager.md) (1 shared connections)
- [Container Exception Handling](Container_Exception_Handling.md) (1 shared connections)

## Source Files

- `server/realtime/connection_helpers.py`
- `server/tests/unit/realtime/test_connection_helpers.py`
- `server/tests/unit/realtime/test_connection_helpers_impl.py`

## Audit Trail

- EXTRACTED: 159 (99%)
- INFERRED: 2 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*