# Playwright E2E Specs

> 81 nodes

## Key Concepts

- **test_connection_helpers_impl.py** (35 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **convert_uuids_to_strings()** (18 connections) — `server/realtime/connection_helpers.py`
- **send_personal_message_old_impl()** (13 connections) — `server/realtime/connection_helpers.py`
- **_optimize_payload()** (11 connections) — `server/realtime/connection_helpers.py`
- **_send_to_websockets()** (11 connections) — `server/realtime/connection_helpers.py`
- **Any** (10 connections)
- **test_connection_helpers.py** (9 connections) — `server/tests/unit/realtime/test_connection_helpers.py`
- **_update_delivery_status()** (8 connections) — `server/realtime/connection_helpers.py`
- **mark_player_seen_impl()** (8 connections) — `server/realtime/connection_helpers.py`
- **_queue_message_if_needed()** (6 connections) — `server/realtime/connection_helpers.py`
- **broadcast_room_event_impl()** (6 connections) — `server/realtime/connection_helpers.py`
- **broadcast_global_event_impl()** (6 connections) — `server/realtime/connection_helpers.py`
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
- **test_send_to_websockets_no_connections()** (3 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **test_queue_message_if_needed()** (3 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **test_update_delivery_status_success()** (3 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- *... and 56 more nodes in this community*

## Relationships

- [Client Event Store](Client_Event_Store.md) (12 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (4 shared connections)
- [Schemas Maps Map](Schemas_Maps_Map.md) (4 shared connections)
- [Combat Domain Events](Combat_Domain_Events.md) (3 shared connections)
- [Archive Bug Fix](Archive_Bug_Fix.md) (2 shared connections)
- [Pylint Unique Findings](Pylint_Unique_Findings.md) (2 shared connections)
- [Auth Token Utilities](Auth_Token_Utilities.md) (2 shared connections)

## Source Files

- `server/realtime/connection_helpers.py`
- `server/tests/unit/realtime/test_connection_helpers.py`
- `server/tests/unit/realtime/test_connection_helpers_impl.py`

## Audit Trail

- EXTRACTED: 263 (98%)
- INFERRED: 6 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*