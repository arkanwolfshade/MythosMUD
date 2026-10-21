# container_helpers_inventory_ops.py

> 37 nodes · cohesion 0.12

## Key Concepts

- **InstanceFlushService** (29 connections) — `server/services/instance_flush_service.py`
- **test_instance_flush_service.py** (26 connections) — `server/tests/unit/services/test_instance_flush_service.py`
- **FakeBankPersistence** (16 connections) — `server/tests/unit/services/test_instance_flush_service.py`
- **_instance_manager()** (11 connections) — `server/tests/unit/services/test_instance_flush_service.py`
- **test_flush_never_evicts_from_a_full_box()** (9 connections) — `server/tests/unit/services/test_instance_flush_service.py`
- **asyncio** (8 connections)
- **_stack()** (8 connections) — `server/tests/unit/services/test_instance_flush_service.py`
- **test_flush_appends_to_an_existing_box()** (8 connections) — `server/tests/unit/services/test_instance_flush_service.py`
- **test_flush_of_an_unknown_instance_with_leftover_drops_loses_them_without_raising()** (8 connections) — `server/tests/unit/services/test_instance_flush_service.py`
- **test_flush_survives_database_errors()** (8 connections) — `server/tests/unit/services/test_instance_flush_service.py`
- **test_flush_all_flushes_every_live_instance_into_each_owners_box()** (7 connections) — `server/tests/unit/services/test_instance_flush_service.py`
- **test_flush_sends_only_that_instances_drops_to_its_owners_box_then_destroys_it()** (7 connections) — `server/tests/unit/services/test_instance_flush_service.py`
- **test_flush_with_a_malformed_owner_id_loses_the_items_without_raising()** (7 connections) — `server/tests/unit/services/test_instance_flush_service.py`
- **test_flush_with_empty_floor_only_destroys()** (6 connections) — `server/tests/unit/services/test_instance_flush_service.py`
- **.__init__()** (5 connections) — `server/services/instance_flush_service.py`
- **RoomDropStore** (5 connections) — `server/services/instance_flush_service.py`
- **.flush()** (4 connections) — `server/services/instance_flush_service.py`
- **_box()** (4 connections) — `server/tests/unit/services/test_instance_flush_service.py`
- **UUID** (4 connections)
- **.flush_all()** (3 connections) — `server/services/instance_flush_service.py`
- **.create_container()** (3 connections) — `server/tests/unit/services/test_instance_flush_service.py`
- **.get_bank_container()** (3 connections) — `server/tests/unit/services/test_instance_flush_service.py`
- **.pop_room_drops_with_prefix()** (2 connections) — `server/services/instance_flush_service.py`
- **.__init__()** (2 connections) — `server/tests/unit/services/test_instance_flush_service.py`
- **.update_container()** (2 connections) — `server/tests/unit/services/test_instance_flush_service.py`
- *... and 12 more nodes in this community*

## Relationships

- [test_container_persistence_extended_row_helpers.py](test_container_persistence_extended_row_helpers.py.md) (10 shared connections)
- [test_container_persistence_async_helpers.py](test_container_persistence_async_helpers.py.md) (10 shared connections)
- [test_npc_event_handlers.py](test_npc_event_handlers.py.md) (6 shared connections)
- [test_message_handlers.py](test_message_handlers.py.md) (4 shared connections)
- [✅ Phase 2 Async Persistence Migration - COMPLETE](✅_Phase_2_Async_Persistence_Migration_-_COMPLETE.md) (4 shared connections)
- [.profession_to_dict](profession_to_dict.md) (3 shared connections)
- [LoggingPatternLinter](LoggingPatternLinter.md) (3 shared connections)
- [test_combat_monitoring_service.py](test_combat_monitoring_service.py.md) (2 shared connections)
- [connection_initialization.py](connection_initialization.py.md) (1 shared connections)
- [BaseEvent](BaseEvent.md) (1 shared connections)
- [AttributeError](AttributeError.md) (1 shared connections)

## Source Files

- `server/services/instance_flush_service.py`
- `server/tests/unit/services/test_instance_flush_service.py`

## Audit Trail

- EXTRACTED: 102 (81%)
- INFERRED: 24 (19%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*