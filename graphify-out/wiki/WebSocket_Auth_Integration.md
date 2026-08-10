# WebSocket Auth Integration

> 49 nodes

## Key Concepts

- **WebSocketRequestContext** (26 connections) — `server/realtime/request_context.py`
- **test_request_context.py** (16 connections) — `server/tests/unit/realtime/test_request_context.py`
- **command_execution_request.py** (9 connections) — `server/command_handler/command_execution_request.py`
- **request_context.py** (9 connections) — `server/realtime/request_context.py`
- **test_command_execution_request.py** (8 connections) — `server/tests/unit/command_handler/test_command_execution_request.py`
- **Any** (7 connections)
- **.set_app_state_services()** (4 connections) — `server/realtime/request_context.py`
- **.get_event_bus()** (4 connections) — `server/realtime/request_context.py`
- **.get_alias_storage()** (4 connections) — `server/realtime/request_context.py`
- **test_command_request_app_state_from_websocket_request_context()** (4 connections) — `server/tests/unit/command_handler/test_command_execution_request.py`
- **test_create_websocket_request_context()** (4 connections) — `server/tests/unit/realtime/test_request_context.py`
- **test_create_websocket_request_context_no_user()** (4 connections) — `server/tests/unit/realtime/test_request_context.py`
- **.__init__()** (3 connections) — `server/realtime/request_context.py`
- **.set_alias_storage()** (3 connections) — `server/realtime/request_context.py`
- **.get_persistence()** (3 connections) — `server/realtime/request_context.py`
- **test_websocket_request_context_init()** (3 connections) — `server/tests/unit/realtime/test_request_context.py`
- **test_websocket_request_context_init_no_user()** (3 connections) — `server/tests/unit/realtime/test_request_context.py`
- **test_websocket_request_context_set_alias_storage()** (3 connections) — `server/tests/unit/realtime/test_request_context.py`
- **test_websocket_request_context_set_app_state_services()** (3 connections) — `server/tests/unit/realtime/test_request_context.py`
- **test_websocket_request_context_set_app_state_services_none()** (3 connections) — `server/tests/unit/realtime/test_request_context.py`
- **test_websocket_request_context_get_persistence()** (3 connections) — `server/tests/unit/realtime/test_request_context.py`
- **test_websocket_request_context_get_event_bus()** (3 connections) — `server/tests/unit/realtime/test_request_context.py`
- **test_websocket_request_context_get_event_bus_none()** (3 connections) — `server/tests/unit/realtime/test_request_context.py`
- **test_websocket_request_context_get_alias_storage()** (3 connections) — `server/tests/unit/realtime/test_request_context.py`
- **test_websocket_request_context_get_alias_storage_not_set()** (3 connections) — `server/tests/unit/realtime/test_request_context.py`
- *... and 24 more nodes in this community*

## Relationships

- [Logout and Quit Commands](Logout_and_Quit_Commands.md) (6 shared connections)
- [Investigations Sessions Session](Investigations_Sessions_Session.md) (5 shared connections)
- [Client Event Store](Client_Event_Store.md) (3 shared connections)
- [Game Service Bundle](Game_Service_Bundle.md) (2 shared connections)
- [Player Combat XP](Player_Combat_XP.md) (2 shared connections)
- [Test Refactoring Summary](Test_Refactoring_Summary.md) (1 shared connections)
- [Cursor Skills Harden](Cursor_Skills_Harden.md) (1 shared connections)
- [Who Command Tests](Who_Command_Tests.md) (1 shared connections)
- [Commands Container Inventory](Commands_Container_Inventory.md) (1 shared connections)

## Source Files

- `server/command_handler/command_execution_request.py`
- `server/realtime/request_context.py`
- `server/tests/unit/command_handler/test_command_execution_request.py`
- `server/tests/unit/realtime/test_request_context.py`

## Audit Trail

- EXTRACTED: 155 (96%)
- INFERRED: 7 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*