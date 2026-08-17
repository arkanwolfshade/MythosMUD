# server api container events emit

> 63 nodes

## Key Concepts

- **asyncio** (21 connections)
- **ConnectionManager** (19 connections)
- **emit_transfer_event()** (17 connections) — `server/api/container_events.py`
- **emit_container_opened_events()** (16 connections) — `server/api/container_events.py`
- **emit_close_container_event()** (15 connections) — `server/api/container_events.py`
- **TestEmitTransferEvent** (12 connections) — `server/tests/unit/api/test_container_events.py`
- **TestEmitCloseContainerEvent** (11 connections) — `server/tests/unit/api/test_container_events.py`
- **_assert_warning_once()** (10 connections) — `server/tests/unit/api/test_container_events.py`
- **TestEmitContainerOpenedEvents** (9 connections) — `server/tests/unit/api/test_container_events.py`
- **.test_emit_transfer_event_emission_error()** (8 connections) — `server/tests/unit/api/test_container_events.py`
- **.test_emit_transfer_event_to_container_direction()** (8 connections) — `server/tests/unit/api/test_container_events.py`
- **.test_emit_transfer_event_to_player_direction()** (8 connections) — `server/tests/unit/api/test_container_events.py`
- **.test_emit_transfer_event_success()** (7 connections) — `server/tests/unit/api/test_container_events.py`
- **.test_emit_transfer_event_validation_error()** (7 connections) — `server/tests/unit/api/test_container_events.py`
- **.test_emit_close_container_event_emission_error()** (6 connections) — `server/tests/unit/api/test_container_events.py`
- **.test_emit_close_container_event_persistence_error()** (6 connections) — `server/tests/unit/api/test_container_events.py`
- **.test_emit_container_opened_events_emission_error()** (6 connections) — `server/tests/unit/api/test_container_events.py`
- **.test_emit_container_opened_events_validation_error()** (6 connections) — `server/tests/unit/api/test_container_events.py`
- **.test_emit_container_opened_events_missing_mutation_token()** (6 connections) — `server/tests/unit/api/test_container_events.py`
- **.test_emit_container_opened_events_room_emission_error()** (6 connections) — `server/tests/unit/api/test_container_events.py`
- **.test_emit_transfer_event_no_connection_manager()** (6 connections) — `server/tests/unit/api/test_container_events.py`
- **.test_emit_transfer_event_no_container_in_result()** (6 connections) — `server/tests/unit/api/test_container_events.py`
- **.test_emit_transfer_event_no_room_id()** (6 connections) — `server/tests/unit/api/test_container_events.py`
- **ContainerComponent** (6 connections)
- **TestEmitContainerOpenedEventsEdgeCases** (5 connections) — `server/tests/unit/api/test_container_events.py`
- *... and 38 more nodes in this community*

## Relationships

- [abstractcontextmanager](abstractcontextmanager.md) (19 shared connections)
- [server api container helpers handle](server_api_container_helpers_handle.md) (10 shared connections)
- [docs examples logging fastapi integration](docs_examples_logging_fastapi_integration.md) (6 shared connections)
- [playercombatservice](playercombatservice.md) (4 shared connections)
- [server services container websocket events](server_services_container_websocket_events.md) (4 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (4 shared connections)
- [server async persistence asyncpersistencelayer](server_async_persistence_asyncpersistencelayer.md) (2 shared connections)

## Source Files

- `server/api/container_events.py`
- `server/tests/unit/api/test_container_events.py`

## Audit Trail

- EXTRACTED: 168 (94%)
- INFERRED: 11 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*