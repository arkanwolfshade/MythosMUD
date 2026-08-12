# Magic Command Handlers

> 60 nodes

## Key Concepts

- **test_container_websocket_events.py** (23 connections) — `server/tests/unit/services/test_container_websocket_events.py`
- **container_websocket_events.py** (17 connections) — `server/services/container_websocket_events.py`
- **emit_container_opened_events()** (16 connections) — `server/api/container_events.py`
- **emit_container_opened()** (14 connections) — `server/services/container_websocket_events.py`
- **emit_container_opened_to_room()** (12 connections) — `server/services/container_websocket_events.py`
- **emit_container_updated()** (10 connections) — `server/services/container_websocket_events.py`
- **emit_container_closed()** (9 connections) — `server/services/container_websocket_events.py`
- **emit_container_decayed()** (8 connections) — `server/services/container_websocket_events.py`
- **UUID** (6 connections)
- **Any** (5 connections)
- **datetime** (3 connections)
- **.test_emit_container_opened_events_success()** (3 connections) — `server/tests/unit/api/test_container_events.py`
- **.test_emit_container_opened_events_no_connection_manager()** (3 connections) — `server/tests/unit/api/test_container_events.py`
- **.test_emit_container_opened_events_no_room_id()** (3 connections) — `server/tests/unit/api/test_container_events.py`
- **.test_emit_container_opened_events_validation_error()** (3 connections) — `server/tests/unit/api/test_container_events.py`
- **.test_emit_container_opened_events_emission_error()** (3 connections) — `server/tests/unit/api/test_container_events.py`
- **.test_emit_container_opened_events_missing_mutation_token()** (3 connections) — `server/tests/unit/api/test_container_events.py`
- **.test_emit_container_opened_events_room_emission_error()** (3 connections) — `server/tests/unit/api/test_container_events.py`
- **test_emit_container_opened()** (3 connections) — `server/tests/unit/services/test_container_websocket_events.py`
- **test_emit_container_opened_with_owner()** (3 connections) — `server/tests/unit/services/test_container_websocket_events.py`
- **test_emit_container_opened_to_room()** (3 connections) — `server/tests/unit/services/test_container_websocket_events.py`
- **test_emit_container_closed()** (3 connections) — `server/tests/unit/services/test_container_websocket_events.py`
- **test_emit_container_opened_with_owner_id()** (3 connections) — `server/tests/unit/services/test_container_websocket_events.py`
- **test_emit_container_opened_to_room_with_owner()** (3 connections) — `server/tests/unit/services/test_container_websocket_events.py`
- **test_emit_container_updated()** (3 connections) — `server/tests/unit/services/test_container_websocket_events.py`
- *... and 35 more nodes in this community*

## Relationships

- [Combat Player Broadcasts](Combat_Player_Broadcasts.md) (20 shared connections)
- [NPC Service Tests](NPC_Service_Tests.md) (5 shared connections)
- [Pylint Unique Findings](Pylint_Unique_Findings.md) (3 shared connections)
- [Legacy Error Sanitization](Legacy_Error_Sanitization.md) (2 shared connections)
- [Client Event Store](Client_Event_Store.md) (2 shared connections)
- [Calendar NPC Schedule](Calendar_NPC_Schedule.md) (1 shared connections)
- [Legacy Cleanup Summary](Legacy_Cleanup_Summary.md) (1 shared connections)

## Source Files

- `server/api/container_events.py`
- `server/services/container_websocket_events.py`
- `server/tests/unit/api/test_container_events.py`
- `server/tests/unit/services/test_container_websocket_events.py`

## Audit Trail

- EXTRACTED: 212 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*