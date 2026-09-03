# Test Envelope

> 56 nodes

## Key Concepts

- **build_event()** (79 connections) — `server/realtime/envelope.py`
- **envelope.py** (30 connections) — `server/realtime/envelope.py`
- **test_envelope.py** (29 connections) — `server/tests/unit/realtime/test_envelope.py`
- **UUIDEncoder** (8 connections) — `server/realtime/envelope.py`
- **utc_now_z()** (6 connections) — `server/realtime/envelope.py`
- **_SupportsEventSequence** (4 connections) — `server/realtime/envelope.py`
- **test_build_event_json_serializable()** (4 connections) — `server/tests/unit/realtime/test_envelope.py`
- **test_build_event_sequence_priority()** (4 connections) — `server/tests/unit/realtime/test_envelope.py`
- **test_build_event_with_connection_manager()** (4 connections) — `server/tests/unit/realtime/test_envelope.py`
- **test_uuid_encoder_handles_other_types()** (4 connections) — `server/tests/unit/realtime/test_envelope.py`
- **_get_next_global_sequence()** (3 connections) — `server/realtime/envelope.py`
- **test_build_event_all_parameters()** (3 connections) — `server/tests/unit/realtime/test_envelope.py`
- **test_build_event_basic()** (3 connections) — `server/tests/unit/realtime/test_envelope.py`
- **test_build_event_empty_data()** (3 connections) — `server/tests/unit/realtime/test_envelope.py`
- **test_build_event_no_data_parameter()** (3 connections) — `server/tests/unit/realtime/test_envelope.py`
- **test_build_event_optional_parameters_none()** (3 connections) — `server/tests/unit/realtime/test_envelope.py`
- **test_build_event_timestamp_format()** (3 connections) — `server/tests/unit/realtime/test_envelope.py`
- **test_build_event_uses_global_sequence_when_no_manager()** (3 connections) — `server/tests/unit/realtime/test_envelope.py`
- **test_build_event_with_player_id_string()** (3 connections) — `server/tests/unit/realtime/test_envelope.py`
- **test_build_event_with_player_id_uuid()** (3 connections) — `server/tests/unit/realtime/test_envelope.py`
- **test_build_event_with_room_id()** (3 connections) — `server/tests/unit/realtime/test_envelope.py`
- **test_build_event_with_sequence_number()** (3 connections) — `server/tests/unit/realtime/test_envelope.py`
- **test_utc_now_z_format()** (3 connections) — `server/tests/unit/realtime/test_envelope.py`
- **test_utc_now_z_is_utc()** (3 connections) — `server/tests/unit/realtime/test_envelope.py`
- **test_uuid_encoder_handles_uuid()** (3 connections) — `server/tests/unit/realtime/test_envelope.py`
- *... and 31 more nodes in this community*

## Relationships

- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (20 shared connections)
- [Connection Manager Api](Connection_Manager_Api.md) (4 shared connections)
- [Message Broadcaster](Message_Broadcaster.md) (4 shared connections)
- [Websocket Handler Commands](Websocket_Handler_Commands.md) (4 shared connections)
- [Game Tick Processing](Game_Tick_Processing.md) (3 shared connections)
- [Test Admin Summon Command](Test_Admin_Summon_Command.md) (3 shared connections)
- [Test Teleport Helpers](Test_Teleport_Helpers.md) (3 shared connections)
- [Game State Provider](Game_State_Provider.md) (3 shared connections)
- [Player Connection Setup](Player_Connection_Setup.md) (3 shared connections)
- [Player Event Handlers Room](Player_Event_Handlers_Room.md) (3 shared connections)
- [Websocket Handler Connection](Websocket_Handler_Connection.md) (3 shared connections)
- [Test Container Websocket Events](Test_Container_Websocket_Events.md) (3 shared connections)

## Source Files

- `server/realtime/envelope.py`
- `server/tests/unit/realtime/test_envelope.py`

## Audit Trail

- EXTRACTED: 165 (97%)
- INFERRED: 5 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*