# TestEmitLootAllEvent

> 29 nodes

## Key Concepts

- **TestEmitLootAllEvent** (13 connections) — `server/tests/unit/api/test_container_events_loot.py`
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
- **sample_container_component()** (4 connections) — `server/tests/unit/api/test_container_events_loot.py`
- **sample_container_data()** (4 connections) — `server/tests/unit/api/test_container_events_loot.py`
- **_assert_warning_once()** (3 connections) — `server/tests/unit/api/test_container_events_loot.py`
- **fixture** (3 connections)
- **Test emit_loot_all_event handles emission errors gracefully.** (1 connections) — `server/tests/unit/api/test_container_events_loot.py`
- **Test emit_loot_all_event correctly calculates items_removed in diff.** (1 connections) — `server/tests/unit/api/test_container_events_loot.py`
- **Test emit_loot_all_event handles case when all items are removed.** (1 connections) — `server/tests/unit/api/test_container_events_loot.py`
- **Assert patched logger.warning was called once (typed for basedpyright).** (1 connections) — `server/tests/unit/api/test_container_events_loot.py`
- **Test emit_loot_all_event handles case when no items are removed.** (1 connections) — `server/tests/unit/api/test_container_events_loot.py`
- **Extract diff['items'] from emit_container_updated await kwargs.** (1 connections) — `server/tests/unit/api/test_container_events_loot.py`
- **Create a mock connection manager.** (1 connections) — `server/tests/unit/api/test_container_events_loot.py`
- **Create sample container data for testing.** (1 connections) — `server/tests/unit/api/test_container_events_loot.py`
- **Create a ContainerComponent from sample data.** (1 connections) — `server/tests/unit/api/test_container_events_loot.py`
- *... and 4 more nodes in this community*

## Relationships

- [TransferContainerRequest](TransferContainerRequest.md) (13 shared connections)
- [LootAllRequest](LootAllRequest.md) (8 shared connections)
- [ContainerComponent](ContainerComponent.md) (7 shared connections)
- [ConnectionManager](ConnectionManager.md) (2 shared connections)

## Source Files

- `server/tests/unit/api/test_container_events_loot.py`

## Audit Trail

- EXTRACTED: 64 (90%)
- INFERRED: 7 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*