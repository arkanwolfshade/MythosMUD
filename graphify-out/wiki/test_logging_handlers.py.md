# test_logging_handlers.py

> 107 nodes · cohesion 0.04

## Key Concepts

- **container_events.py** (26 connections) — `server/api/container_events.py`
- **test_container_events.py** (24 connections) — `server/tests/unit/api/test_container_events.py`
- **asyncio** (20 connections)
- **ConnectionManager** (18 connections)
- **emit_loot_all_event()** (17 connections) — `server/api/container_events.py`
- **emit_container_opened_events()** (16 connections) — `server/api/container_events.py`
- **emit_transfer_event()** (16 connections) — `server/api/container_events.py`
- **test_container_events_loot.py** (16 connections) — `server/tests/unit/api/test_container_events_loot.py`
- **emit_close_container_event()** (15 connections) — `server/api/container_events.py`
- **TestEmitLootAllEvent** (13 connections) — `server/tests/unit/api/test_container_events_loot.py`
- **TestEmitTransferEvent** (12 connections) — `server/tests/unit/api/test_container_events.py`
- **TestEmitCloseContainerEvent** (11 connections) — `server/tests/unit/api/test_container_events.py`
- **_assert_warning_once()** (10 connections) — `server/tests/unit/api/test_container_events.py`
- **TestEmitContainerOpenedEvents** (9 connections) — `server/tests/unit/api/test_container_events.py`
- **.test_emit_loot_all_event_emission_error()** (8 connections) — `server/tests/unit/api/test_container_events_loot.py`
- **.test_emit_transfer_event_emission_error()** (8 connections) — `server/tests/unit/api/test_container_events.py`
- **.test_emit_transfer_event_passes_updated_container()** (8 connections) — `server/tests/unit/api/test_container_events.py`
- **asyncio** (7 connections)
- **ConnectionManager** (7 connections)
- **.test_emit_loot_all_event_all_items_removed()** (7 connections) — `server/tests/unit/api/test_container_events_loot.py`
- **.test_emit_loot_all_event_calculates_items_removed()** (7 connections) — `server/tests/unit/api/test_container_events_loot.py`
- **.test_emit_loot_all_event_success()** (7 connections) — `server/tests/unit/api/test_container_events_loot.py`
- **.test_emit_loot_all_event_zero_items_removed()** (7 connections) — `server/tests/unit/api/test_container_events_loot.py`
- **.test_emit_transfer_event_success()** (7 connections) — `server/tests/unit/api/test_container_events.py`
- **.test_emit_transfer_event_validation_error()** (7 connections) — `server/tests/unit/api/test_container_events.py`
- *... and 82 more nodes in this community*

## Relationships

- [connection_manager_methods.py](connection_manager_methods.py.md) (27 shared connections)
- [test_look_player.py](test_look_player.py.md) (18 shared connections)
- [CombatParticipant](CombatParticipant.md) (14 shared connections)
- [ChatService](ChatService.md) (11 shared connections)
- [RoomNodeData](RoomNodeData.md) (10 shared connections)
- [Room](Room.md) (4 shared connections)
- [test_party_service.py](test_party_service.py.md) (4 shared connections)
- [generate_arkham_grid.py](generate_arkham_grid.py.md) (4 shared connections)
- [connection_initialization.py](connection_initialization.py.md) (3 shared connections)

## Source Files

- `server/api/container_events.py`
- `server/tests/unit/api/test_container_events.py`
- `server/tests/unit/api/test_container_events_loot.py`

## Audit Trail

- EXTRACTED: 281 (92%)
- INFERRED: 25 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*