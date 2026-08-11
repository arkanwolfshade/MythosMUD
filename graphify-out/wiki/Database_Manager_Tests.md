# Database Manager Tests

> 96 nodes

## Key Concepts

- **test_container_websocket_events.py** (23 connections) — `server/tests/unit/services/test_container_websocket_events.py`
- **container_events.py** (21 connections) — `server/api/container_events.py`
- **emit_transfer_event()** (17 connections) — `server/api/container_events.py`
- **container_websocket_events.py** (17 connections) — `server/services/container_websocket_events.py`
- **emit_container_opened_events()** (16 connections) — `server/api/container_events.py`
- **_emit_close_container_event()** (14 connections) — `server/api/container_events.py`
- **emit_container_opened()** (14 connections) — `server/services/container_websocket_events.py`
- **emit_container_opened_to_room()** (12 connections) — `server/services/container_websocket_events.py`
- **emit_container_updated()** (10 connections) — `server/services/container_websocket_events.py`
- **emit_container_closed()** (9 connections) — `server/services/container_websocket_events.py`
- **emit_container_decayed()** (8 connections) — `server/services/container_websocket_events.py`
- **UUID** (6 connections)
- **UUID** (5 connections)
- **Any** (5 connections)
- **Any** (4 connections)
- **.test_emit_transfer_event_success()** (4 connections) — `server/tests/unit/api/test_container_events.py`
- **.test_emit_transfer_event_no_connection_manager()** (4 connections) — `server/tests/unit/api/test_container_events.py`
- **.test_emit_transfer_event_no_container_in_result()** (4 connections) — `server/tests/unit/api/test_container_events.py`
- **.test_emit_transfer_event_no_room_id()** (4 connections) — `server/tests/unit/api/test_container_events.py`
- **.test_emit_transfer_event_validation_error()** (4 connections) — `server/tests/unit/api/test_container_events.py`
- **.test_emit_transfer_event_emission_error()** (4 connections) — `server/tests/unit/api/test_container_events.py`
- **.test_emit_transfer_event_to_player_direction()** (4 connections) — `server/tests/unit/api/test_container_events.py`
- **.test_emit_transfer_event_to_container_direction()** (4 connections) — `server/tests/unit/api/test_container_events.py`
- **datetime** (3 connections)
- **.test_emit_container_opened_events_success()** (3 connections) — `server/tests/unit/api/test_container_events.py`
- *... and 71 more nodes in this community*

## Relationships

- [Combat Player Broadcasts](Combat_Player_Broadcasts.md) (37 shared connections)
- [Argon2 Password Hashing](Argon2_Password_Hashing.md) (11 shared connections)
- [Realtime Service Bundle](Realtime_Service_Bundle.md) (7 shared connections)
- [Client Event Store](Client_Event_Store.md) (4 shared connections)
- [Pylint Unique Findings](Pylint_Unique_Findings.md) (3 shared connections)
- [Command Alias Handling](Command_Alias_Handling.md) (2 shared connections)
- [Invite and User Schemas](Invite_and_User_Schemas.md) (1 shared connections)
- [Archive Npc Population](Archive_Npc_Population.md) (1 shared connections)

## Source Files

- `server/api/container_events.py`
- `server/services/container_websocket_events.py`
- `server/tests/unit/api/test_container_events.py`
- `server/tests/unit/services/test_container_websocket_events.py`

## Audit Trail

- EXTRACTED: 340 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*