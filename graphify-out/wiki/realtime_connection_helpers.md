# realtime connection helpers

> 91 nodes

## Key Concepts

- **test_connection_helpers_impl.py** (35 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **connection_helpers.py** (21 connections) — `server/realtime/connection_helpers.py`
- **convert_uuids_to_strings()** (18 connections) — `server/realtime/connection_helpers.py`
- **send_personal_message_old_impl()** (13 connections) — `server/realtime/connection_helpers.py`
- **_optimize_payload()** (11 connections) — `server/realtime/connection_helpers.py`
- **_send_to_websockets()** (11 connections) — `server/realtime/connection_helpers.py`
- **Any** (10 connections)
- **handle_new_login_impl()** (9 connections) — `server/realtime/connection_helpers.py`
- **test_connection_helpers.py** (9 connections) — `server/tests/unit/realtime/test_connection_helpers.py`
- **_update_delivery_status()** (8 connections) — `server/realtime/connection_helpers.py`
- **mark_player_seen_impl()** (8 connections) — `server/realtime/connection_helpers.py`
- **_queue_message_if_needed()** (6 connections) — `server/realtime/connection_helpers.py`
- **broadcast_room_event_impl()** (6 connections) — `server/realtime/connection_helpers.py`
- **broadcast_global_event_impl()** (6 connections) — `server/realtime/connection_helpers.py`
- **.mark_player_seen()** (4 connections) — `server/realtime/connection_manager.py`
- **.send_personal_message_old()** (4 connections) — `server/realtime/connection_manager.py`
- **.handle_new_login()** (4 connections) — `server/realtime/connection_manager.py`
- **test_send_to_websockets_websocket_error()** (4 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **test_optimize_payload_optimization_failure()** (4 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **test_convert_uuids_to_strings_uuid()** (3 connections) — `server/tests/unit/realtime/test_connection_helpers.py`
- **test_convert_uuids_to_strings_dict()** (3 connections) — `server/tests/unit/realtime/test_connection_helpers.py`
- **test_convert_uuids_to_strings_list()** (3 connections) — `server/tests/unit/realtime/test_connection_helpers.py`
- **test_convert_uuids_to_strings_nested()** (3 connections) — `server/tests/unit/realtime/test_connection_helpers.py`
- **test_convert_uuids_to_strings_string()** (3 connections) — `server/tests/unit/realtime/test_connection_helpers.py`
- **test_convert_uuids_to_strings_int()** (3 connections) — `server/tests/unit/realtime/test_connection_helpers.py`
- *... and 66 more nodes in this community*

## Relationships

- [Room Broadcast](Room_Broadcast.md) (12 shared connections)
- [commands shutdown process](commands_shutdown_process.md) (6 shared connections)
- [room look commands](room_look_commands.md) (3 shared connections)
- [models npc rationale](models_npc_rationale.md) (2 shared connections)
- [npc event handlers](npc_event_handlers.md) (2 shared connections)
- [NPC Combat](NPC_Combat.md) (2 shared connections)
- [websocket helpers realtime](websocket_helpers_realtime.md) (2 shared connections)
- [Loot Generation](Loot_Generation.md) (1 shared connections)

## Source Files

- `server/realtime/connection_helpers.py`
- `server/realtime/connection_manager.py`
- `server/tests/unit/realtime/test_connection_helpers.py`
- `server/tests/unit/realtime/test_connection_helpers_impl.py`

## Audit Trail

- EXTRACTED: 309 (98%)
- INFERRED: 7 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*