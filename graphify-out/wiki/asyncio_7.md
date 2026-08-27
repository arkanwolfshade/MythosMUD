# asyncio

> 30 nodes

## Key Concepts

- **emit_loot_all_event()** (17 connections) — `server/api/container_events.py`
- **.test_emit_loot_all_event_emission_error()** (8 connections) — `server/tests/unit/api/test_container_events_loot.py`
- **.test_emit_loot_all_event_all_items_removed()** (7 connections) — `server/tests/unit/api/test_container_events_loot.py`
- **.test_emit_loot_all_event_calculates_items_removed()** (7 connections) — `server/tests/unit/api/test_container_events_loot.py`
- **.test_emit_loot_all_event_success()** (7 connections) — `server/tests/unit/api/test_container_events_loot.py`
- **.test_emit_loot_all_event_zero_items_removed()** (7 connections) — `server/tests/unit/api/test_container_events_loot.py`
- **asyncio** (7 connections)
- **ConnectionManager** (7 connections)
- **.test_emit_loot_all_event_no_connection_manager()** (6 connections) — `server/tests/unit/api/test_container_events_loot.py`
- **.test_emit_loot_all_event_no_room_id()** (6 connections) — `server/tests/unit/api/test_container_events_loot.py`
- **_diff_items_from_emit()** (5 connections) — `server/tests/unit/api/test_container_events_loot.py`
- **mock_connection_manager()** (5 connections) — `server/tests/unit/api/test_container_events_loot.py`
- **sample_container_component()** (5 connections) — `server/tests/unit/api/test_container_events_loot.py`
- **UUID** (5 connections)
- **ContainerComponent** (4 connections)
- **_assert_warning_once()** (3 connections) — `server/tests/unit/api/test_container_events_loot.py`
- **fixture** (3 connections)
- **ContainerComponent** (1 connections)
- **Emit WebSocket event for loot_all operation. Args: connection_manager:…** (1 connections) — `server/api/container_events.py`
- **Test emit_loot_all_event handles emission errors gracefully.** (1 connections) — `server/tests/unit/api/test_container_events_loot.py`
- **Test emit_loot_all_event correctly calculates items_removed in diff.** (1 connections) — `server/tests/unit/api/test_container_events_loot.py`
- **Test emit_loot_all_event handles case when all items are removed.** (1 connections) — `server/tests/unit/api/test_container_events_loot.py`
- **Assert patched logger.warning was called once (typed for basedpyright).** (1 connections) — `server/tests/unit/api/test_container_events_loot.py`
- **Test emit_loot_all_event handles case when no items are removed.** (1 connections) — `server/tests/unit/api/test_container_events_loot.py`
- **Extract diff['items'] from emit_container_updated await kwargs.** (1 connections) — `server/tests/unit/api/test_container_events_loot.py`
- *... and 5 more nodes in this community*

## Relationships

- [ValidationError](ValidationError.md) (18 shared connections)
- [lifespan_protocols.py](lifespan_protocols.py.md) (8 shared connections)
- [test_nats_service.py](test_nats_service.py.md) (3 shared connections)
- [test_inventory_helpers.py](test_inventory_helpers.py.md) (2 shared connections)
- [PopulationStats](PopulationStats.md) (1 shared connections)

## Source Files

- `server/api/container_events.py`
- `server/tests/unit/api/test_container_events_loot.py`

## Audit Trail

- EXTRACTED: 74 (96%)
- INFERRED: 3 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*