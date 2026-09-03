# Test Websocket Initial State

> 115 nodes

## Key Concepts

- **test_websocket_initial_state.py** (46 connections) — `server/tests/unit/realtime/test_websocket_initial_state.py`
- **websocket_initial_state.py** (41 connections) — `server/realtime/websocket_initial_state.py`
- **asyncio** (21 connections)
- **get_container_async_persistence()** (19 connections) — `server/container/async_persistence_access.py`
- **send_initial_room_state()** (18 connections) — `server/realtime/websocket_initial_state.py`
- **send_initial_game_state()** (14 connections) — `server/realtime/websocket_initial_state.py`
- **check_and_send_death_notification()** (12 connections) — `server/realtime/websocket_initial_state.py`
- **get_event_handler_for_initial_state()** (10 connections) — `server/realtime/websocket_initial_state.py`
- **send_game_state_event_safely()** (10 connections) — `server/realtime/websocket_initial_state.py`
- **prepare_room_data_with_occupants()** (9 connections) — `server/realtime/websocket_initial_state.py`
- **send_occupants_snapshot_if_needed()** (9 connections) — `server/realtime/websocket_initial_state.py`
- **Protocol** (9 connections)
- **add_npc_occupants_to_list()** (8 connections) — `server/realtime/websocket_initial_state.py`
- **UUID** (7 connections)
- **_RealTimeEventHandlerForInitialState** (6 connections) — `server/realtime/websocket_initial_state.py`
- **_get_event_handler_from_app_host()** (5 connections) — `server/realtime/websocket_initial_state.py`
- **_get_player_for_death_check()** (5 connections) — `server/realtime/websocket_initial_state.py`
- **prepare_initial_room_data()** (5 connections) — `server/realtime/websocket_initial_state.py`
- **test_check_and_send_death_notification_in_limbo()** (5 connections) — `server/tests/unit/realtime/test_websocket_initial_state.py`
- **test_check_and_send_death_notification_player_alive()** (5 connections) — `server/tests/unit/realtime/test_websocket_initial_state.py`
- **test_check_and_send_death_notification_player_dead()** (5 connections) — `server/tests/unit/realtime/test_websocket_initial_state.py`
- **test_send_game_state_event_safely_close_message_sent()** (5 connections) — `server/tests/unit/realtime/test_websocket_initial_state.py`
- **test_send_initial_game_state_success()** (5 connections) — `server/tests/unit/realtime/test_websocket_initial_state.py`
- **test_send_initial_room_state_handles_exception()** (5 connections) — `server/tests/unit/realtime/test_websocket_initial_state.py`
- **WebSocket** (5 connections)
- *... and 90 more nodes in this community*

## Relationships

- [Test Websocket Helpers](Test_Websocket_Helpers.md) (14 shared connections)
- [Player Event Handlers Respawn Room](Player_Event_Handlers_Respawn_Room.md) (8 shared connections)
- [Player Model & Migrations](Player_Model_&_Migrations.md) (8 shared connections)
- [Test Websocket Helpers Player](Test_Websocket_Helpers_Player.md) (5 shared connections)
- [Async Persistence](Async_Persistence.md) (5 shared connections)
- [Real Time](Real_Time.md) (3 shared connections)
- [Test Websocket Handler Validation Errors](Test_Websocket_Handler_Validation_Errors.md) (3 shared connections)
- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (3 shared connections)
- [Test Combat Attack Handler](Test_Combat_Attack_Handler.md) (2 shared connections)
- [Correlation Middleware](Correlation_Middleware.md) (2 shared connections)
- [Async Persistence & NPC Events](Async_Persistence_&_NPC_Events.md) (2 shared connections)
- [Test Inventory Command Coercion](Test_Inventory_Command_Coercion.md) (1 shared connections)

## Source Files

- `server/container/async_persistence_access.py`
- `server/realtime/websocket_initial_state.py`
- `server/tests/unit/infrastructure/test_async_persistence_delegates.py`
- `server/tests/unit/realtime/test_websocket_initial_state.py`

## Audit Trail

- EXTRACTED: 253 (96%)
- INFERRED: 10 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*