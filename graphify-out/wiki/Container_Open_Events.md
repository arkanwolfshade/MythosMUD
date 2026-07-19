# Container Open Events

> 67 nodes · cohesion 0.04

## Key Concepts

- **test_container_websocket_events.py** (21 connections) — `server/tests/unit/services/test_container_websocket_events.py`
- **test_container_events.py** (19 connections) — `server/tests/unit/api/test_container_events.py`
- **emit_container_opened_events()** (16 connections) — `server/api/container_events.py`
- **emit_container_opened()** (14 connections) — `server/services/container_websocket_events.py`
- **emit_container_opened_to_room()** (12 connections) — `server/services/container_websocket_events.py`
- **TestEmitContainerOpenedEvents** (11 connections) — `server/tests/unit/api/test_container_events.py`
- **emit_container_closed()** (9 connections) — `server/services/container_websocket_events.py`
- **TestEmitContainerOpenedEventsEdgeCases** (8 connections) — `server/tests/unit/api/test_container_events.py`
- **emit_container_decayed()** (8 connections) — `server/services/container_websocket_events.py`
- **UUID** (6 connections) — `server/services/container_websocket_events.py`
- **Any** (5 connections) — `server/services/container_websocket_events.py`
- **.test_emit_container_opened_events_emission_error()** (4 connections) — `server/tests/unit/api/test_container_events.py`
- **.test_emit_container_opened_events_room_emission_error()** (4 connections) — `server/tests/unit/api/test_container_events.py`
- **Test emit_container_opened_events handles validation errors gracefully.** (3 connections) — `server/tests/unit/api/test_container_events.py`
- **.test_emit_container_opened_events_no_connection_manager()** (3 connections) — `server/tests/unit/api/test_container_events.py`
- **.test_emit_container_opened_events_no_room_id()** (3 connections) — `server/tests/unit/api/test_container_events.py`
- **.test_emit_container_opened_events_success()** (3 connections) — `server/tests/unit/api/test_container_events.py`
- **.test_emit_container_opened_events_validation_error()** (3 connections) — `server/tests/unit/api/test_container_events.py`
- **.test_emit_container_opened_events_missing_mutation_token()** (3 connections) — `server/tests/unit/api/test_container_events.py`
- **datetime** (3 connections) — `server/services/container_websocket_events.py`
- **Test emit_container_opened handles container with owner.** (3 connections) — `server/tests/unit/services/test_container_websocket_events.py`
- **test_emit_container_closed()** (3 connections) — `server/tests/unit/services/test_container_websocket_events.py`
- **test_emit_container_closed_returns_stats()** (3 connections) — `server/tests/unit/services/test_container_websocket_events.py`
- **test_emit_container_decayed()** (3 connections) — `server/tests/unit/services/test_container_websocket_events.py`
- **test_emit_container_opened()** (3 connections) — `server/tests/unit/services/test_container_websocket_events.py`
- *... and 42 more nodes in this community*

## Relationships

- [[Container API Endpoints]] (23 shared connections)
- [[Combat Player Broadcasts]] (7 shared connections)
- [[Loot All Endpoint]] (4 shared connections)
- [[Container Component Capacity]] (4 shared connections)
- [[Inventory Service Helpers]] (3 shared connections)
- [[Database Manager Tests]] (2 shared connections)
- [[Game Tick Processing]] (2 shared connections)

## Source Files

- `server/api/container_events.py`
- `server/services/container_websocket_events.py`
- `server/tests/unit/api/test_container_events.py`
- `server/tests/unit/services/test_container_websocket_events.py`

## Audit Trail

- EXTRACTED: 229 (96%)
- INFERRED: 10 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
