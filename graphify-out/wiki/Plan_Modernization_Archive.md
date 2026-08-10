# Plan Modernization Archive

> 18 nodes

## Key Concepts

- **get_occupant_names()** (11 connections) — `server/realtime/websocket_helpers.py`
- **prepare_room_data_with_occupants()** (9 connections) — `server/realtime/websocket_initial_state.py`
- **._prepare_room_data_for_respawn()** (7 connections) — `server/realtime/player_event_handlers_respawn.py`
- **_accumulate_valid_occupant_name()** (4 connections) — `server/realtime/websocket_helpers.py`
- **test_get_occupant_names_success()** (3 connections) — `server/tests/unit/realtime/test_websocket_helpers.py`
- **test_get_occupant_names_filters_uuid()** (3 connections) — `server/tests/unit/realtime/test_websocket_helpers.py`
- **test_get_occupant_names_empty()** (3 connections) — `server/tests/unit/realtime/test_websocket_helpers.py`
- **test_get_occupant_names_none()** (3 connections) — `server/tests/unit/realtime/test_websocket_helpers.py`
- **test_prepare_room_data_with_occupants()** (3 connections) — `server/tests/unit/realtime/test_websocket_initial_state.py`
- **Prepare room data with NPC and player names for a respawn event.** (1 connections) — `server/realtime/player_event_handlers_respawn.py`
- **Parse one occupant row: append display name or log when it looks like a UUID.** (1 connections) — `server/realtime/websocket_helpers.py`
- **Extract and validate occupant names from room occupants list.** (1 connections) — `server/realtime/websocket_helpers.py`
- **Prepare room data and get occupant names.** (1 connections) — `server/realtime/websocket_initial_state.py`
- **Test get_occupant_names() extracts valid occupant names.** (1 connections) — `server/tests/unit/realtime/test_websocket_helpers.py`
- **Test get_occupant_names() filters out UUID strings.** (1 connections) — `server/tests/unit/realtime/test_websocket_helpers.py`
- **Test get_occupant_names() returns empty list for empty occupants.** (1 connections) — `server/tests/unit/realtime/test_websocket_helpers.py`
- **Test get_occupant_names() handles None occupants.** (1 connections) — `server/tests/unit/realtime/test_websocket_helpers.py`
- **Test prepare_room_data_with_occupants() prepares room data and occupant names.** (1 connections) — `server/tests/unit/realtime/test_websocket_initial_state.py`

## Relationships

- [WebSocket Initial State](WebSocket_Initial_State.md) (7 shared connections)
- [Combat Aggro Threat](Combat_Aggro_Threat.md) (7 shared connections)
- [Restart Invalidating JWT](Restart_Invalidating_JWT.md) (5 shared connections)
- [Async Persistence Layer](Async_Persistence_Layer.md) (2 shared connections)

## Source Files

- `server/realtime/player_event_handlers_respawn.py`
- `server/realtime/websocket_helpers.py`
- `server/realtime/websocket_initial_state.py`
- `server/tests/unit/realtime/test_websocket_helpers.py`
- `server/tests/unit/realtime/test_websocket_initial_state.py`

## Audit Trail

- EXTRACTED: 55 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*