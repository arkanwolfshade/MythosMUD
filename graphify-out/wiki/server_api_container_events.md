# server api container events

> 115 nodes

## Key Concepts

- **models/container.py** (34 connections) — `server/models/container.py`
- **container_events.py** (26 connections) — `server/api/container_events.py`
- **test_container_events.py** (26 connections) — `server/tests/unit/api/test_container_events.py`
- **asyncio** (21 connections)
- **ConnectionManager** (19 connections)
- **emit_loot_all_event()** (17 connections) — `server/api/container_events.py`
- **emit_transfer_event()** (17 connections) — `server/api/container_events.py`
- **test_container_events_loot.py** (17 connections) — `server/tests/unit/api/test_container_events_loot.py`
- **emit_container_opened_events()** (16 connections) — `server/api/container_events.py`
- **emit_close_container_event()** (15 connections) — `server/api/container_events.py`
- **TestEmitLootAllEvent** (13 connections) — `server/tests/unit/api/test_container_events_loot.py`
- **TestEmitTransferEvent** (12 connections) — `server/tests/unit/api/test_container_events.py`
- **TestEmitCloseContainerEvent** (11 connections) — `server/tests/unit/api/test_container_events.py`
- **_assert_warning_once()** (10 connections) — `server/tests/unit/api/test_container_events.py`
- **TestEmitContainerOpenedEvents** (9 connections) — `server/tests/unit/api/test_container_events.py`
- **.test_emit_loot_all_event_emission_error()** (8 connections) — `server/tests/unit/api/test_container_events_loot.py`
- **.test_emit_transfer_event_emission_error()** (8 connections) — `server/tests/unit/api/test_container_events.py`
- **.test_emit_transfer_event_to_container_direction()** (8 connections) — `server/tests/unit/api/test_container_events.py`
- **.test_emit_transfer_event_to_player_direction()** (8 connections) — `server/tests/unit/api/test_container_events.py`
- **TestEmitTransferEventDirections** (7 connections) — `server/tests/unit/api/test_container_events.py`
- **.test_emit_loot_all_event_all_items_removed()** (7 connections) — `server/tests/unit/api/test_container_events_loot.py`
- **.test_emit_loot_all_event_calculates_items_removed()** (7 connections) — `server/tests/unit/api/test_container_events_loot.py`
- **.test_emit_loot_all_event_success()** (7 connections) — `server/tests/unit/api/test_container_events_loot.py`
- **.test_emit_loot_all_event_zero_items_removed()** (7 connections) — `server/tests/unit/api/test_container_events_loot.py`
- **.test_emit_transfer_event_success()** (7 connections) — `server/tests/unit/api/test_container_events.py`
- *... and 90 more nodes in this community*

## Relationships

- [docs examples logging fastapi integration](docs_examples_logging_fastapi_integration.md) (27 shared connections)
- [server models container containercomponent](server_models_container_containercomponent.md) (23 shared connections)
- [server realtime connection error methods](server_realtime_connection_error_methods.md) (14 shared connections)
- [server api container helpers get](server_api_container_helpers_get.md) (14 shared connections)
- [server services container websocket events](server_services_container_websocket_events.md) (12 shared connections)
- [server services container service](server_services_container_service.md) (5 shared connections)
- [server async persistence asyncpersistencelayer](server_async_persistence_asyncpersistencelayer.md) (4 shared connections)
- [server api container endpoints loot](server_api_container_endpoints_loot.md) (2 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (2 shared connections)
- [server async persistence](server_async_persistence.md) (2 shared connections)
- [abstractcontextmanager](abstractcontextmanager.md) (2 shared connections)
- [server services corpse lifecycle service](server_services_corpse_lifecycle_service.md) (2 shared connections)

## Source Files

- `server/api/container_events.py`
- `server/models/container.py`
- `server/tests/unit/api/test_container_events.py`
- `server/tests/unit/api/test_container_events_loot.py`

## Audit Trail

- EXTRACTED: 326 (93%)
- INFERRED: 25 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*