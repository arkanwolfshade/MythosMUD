# Test Player Event Handlers State

> 70 nodes

## Key Concepts

- **PlayerDPUpdated** (38 connections) — `server/events/event_types.py`
- **PlayerStateEventHandler** (34 connections) — `server/realtime/player_event_handlers_state.py`
- **test_player_event_handlers_state.py** (34 connections) — `server/tests/unit/realtime/test_player_event_handlers_state.py`
- **player_event_handlers.py** (27 connections) — `server/realtime/player_event_handlers.py`
- **PlayerXPAwardEvent** (25 connections) — `server/events/event_types.py`
- **asyncio** (21 connections)
- **player_event_handlers_utils.py** (16 connections) — `server/realtime/player_event_handlers_utils.py`
- **player_name_utils.py** (13 connections) — `server/realtime/player_name_utils.py`
- **player_state_event_handler()** (5 connections) — `server/tests/unit/realtime/test_player_event_handlers_state.py`
- **test_handle_player_dp_updated_error_handling()** (5 connections) — `server/tests/unit/realtime/test_player_event_handlers_state.py`
- **test_handle_player_dp_updated_includes_posture_message_on_posture_change()** (5 connections) — `server/tests/unit/realtime/test_player_event_handlers_state.py`
- **test_handle_player_dp_updated_no_connection_manager()** (5 connections) — `server/tests/unit/realtime/test_player_event_handlers_state.py`
- **test_handle_player_dp_updated_player_no_get_stats()** (5 connections) — `server/tests/unit/realtime/test_player_event_handlers_state.py`
- **test_handle_player_dp_updated_player_not_found()** (5 connections) — `server/tests/unit/realtime/test_player_event_handlers_state.py`
- **test_handle_player_dp_updated_success()** (5 connections) — `server/tests/unit/realtime/test_player_event_handlers_state.py`
- **test_handle_player_xp_awarded_error_handling()** (5 connections) — `server/tests/unit/realtime/test_player_event_handlers_state.py`
- **test_handle_player_xp_awarded_no_connection_manager()** (5 connections) — `server/tests/unit/realtime/test_player_event_handlers_state.py`
- **test_handle_player_xp_awarded_player_no_current_room_id()** (5 connections) — `server/tests/unit/realtime/test_player_event_handlers_state.py`
- **test_handle_player_xp_awarded_player_not_found()** (5 connections) — `server/tests/unit/realtime/test_player_event_handlers_state.py`
- **test_handle_player_xp_awarded_success()** (5 connections) — `server/tests/unit/realtime/test_player_event_handlers_state.py`
- **.handle_player_dp_updated()** (4 connections) — `server/realtime/player_event_handlers_state.py`
- **mock_utils()** (4 connections) — `server/tests/unit/realtime/test_player_event_handlers_state.py`
- **test_handle_player_died_error_handling()** (4 connections) — `server/tests/unit/realtime/test_player_event_handlers_state.py`
- **test_handle_player_died_invalid_player_id()** (4 connections) — `server/tests/unit/realtime/test_player_event_handlers_state.py`
- **test_handle_player_died_no_connection_manager()** (4 connections) — `server/tests/unit/realtime/test_player_event_handlers_state.py`
- *... and 45 more nodes in this community*

## Relationships

- [Player Event Handlers State](Player_Event_Handlers_State.md) (13 shared connections)
- [Test Event Handler](Test_Event_Handler.md) (10 shared connections)
- [Async Persistence & NPC Events](Async_Persistence_&_NPC_Events.md) (9 shared connections)
- [Test Player Event Handlers](Test_Player_Event_Handlers.md) (6 shared connections)
- [Player Event Handlers](Player_Event_Handlers.md) (6 shared connections)
- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (6 shared connections)
- [Test Combat Persistence Handler Events](Test_Combat_Persistence_Handler_Events.md) (4 shared connections)
- [Test Player Name Utils](Test_Player_Name_Utils.md) (4 shared connections)
- [Test Magic Healing Events](Test_Magic_Healing_Events.md) (3 shared connections)
- [Experience Repository](Experience_Repository.md) (3 shared connections)
- [Player Event Handlers Room](Player_Event_Handlers_Room.md) (3 shared connections)
- [Player Event Handlers Utils](Player_Event_Handlers_Utils.md) (3 shared connections)

## Source Files

- `server/events/event_types.py`
- `server/realtime/player_event_handlers.py`
- `server/realtime/player_event_handlers_state.py`
- `server/realtime/player_event_handlers_utils.py`
- `server/realtime/player_name_utils.py`
- `server/tests/unit/realtime/test_player_event_handlers_state.py`

## Audit Trail

- EXTRACTED: 198 (84%)
- INFERRED: 37 (16%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*