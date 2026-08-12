# Pylint Unique Findings

> 105 nodes

## Key Concepts

- **build_event()** (117 connections) — `server/realtime/envelope.py`
- **send_game_event()** (29 connections) — `server/realtime/connection_manager_api.py`
- **envelope.py** (28 connections) — `server/realtime/envelope.py`
- **test_envelope.py** (28 connections) — `server/tests/unit/realtime/test_envelope.py`
- **connection_manager_api.py** (16 connections) — `server/realtime/connection_manager_api.py`
- **connection_manager_utils.py** (15 connections) — `server/realtime/connection_manager_utils.py`
- **resolve_connection_manager()** (14 connections) — `server/realtime/connection_manager_utils.py`
- **rest_countdown_task.py** (12 connections) — `server/commands/rest_countdown_task.py`
- **broadcast_game_event()** (11 connections) — `server/realtime/connection_manager_api.py`
- **lazy_import_api_function()** (11 connections) — `server/realtime/connection_manager_utils.py`
- **UUIDEncoder** (8 connections) — `server/realtime/envelope.py`
- **create_rest_countdown_task()** (7 connections) — `server/commands/rest_countdown_task.py`
- **send_room_event()** (7 connections) — `server/realtime/connection_manager_api.py`
- **send_system_notification()** (7 connections) — `server/realtime/connection_manager_api.py`
- **send_player_status_update()** (7 connections) — `server/realtime/connection_manager_api.py`
- **send_room_description()** (7 connections) — `server/realtime/connection_manager_api.py`
- **get_next_sequence_impl()** (7 connections) — `server/realtime/connection_manager_methods.py`
- **UUID** (6 connections)
- **_send_countdown_message()** (6 connections) — `server/commands/rest_countdown_task.py`
- **_handle_countdown_loop()** (6 connections) — `server/commands/rest_countdown_task.py`
- **utc_now_z()** (6 connections) — `server/realtime/envelope.py`
- **_is_rest_interrupted()** (5 connections) — `server/commands/rest_countdown_task.py`
- **Any** (5 connections)
- **_disconnect_player_after_rest()** (5 connections) — `server/commands/rest_countdown_task.py`
- **__getattr__()** (5 connections) — `server/realtime/connection_manager.py`
- *... and 80 more nodes in this community*

## Relationships

- [Zone Schema Definition](Zone_Schema_Definition.md) (15 shared connections)
- [Container Exception Handlers](Container_Exception_Handlers.md) (12 shared connections)
- [Client Event Store](Client_Event_Store.md) (11 shared connections)
- [Archive Bug Fix](Archive_Bug_Fix.md) (10 shared connections)
- [Combat Attack Service](Combat_Attack_Service.md) (8 shared connections)
- [Character Creation E2E](Character_Creation_E2E.md) (8 shared connections)
- [Optimization Archive Modernization](Optimization_Archive_Modernization.md) (7 shared connections)
- [Health Check Models](Health_Check_Models.md) (6 shared connections)
- [WebSocket Request Context](WebSocket_Request_Context.md) (6 shared connections)
- [Legacy Error Sanitization](Legacy_Error_Sanitization.md) (5 shared connections)
- [Inventory Command Models](Inventory_Command_Models.md) (5 shared connections)
- [Combat Domain Events](Combat_Domain_Events.md) (5 shared connections)

## Source Files

- `server/commands/rest_countdown_task.py`
- `server/realtime/connection_manager.py`
- `server/realtime/connection_manager_api.py`
- `server/realtime/connection_manager_methods.py`
- `server/realtime/connection_manager_utils.py`
- `server/realtime/envelope.py`
- `server/tests/unit/realtime/test_envelope.py`

## Audit Trail

- EXTRACTED: 479 (93%)
- INFERRED: 38 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*