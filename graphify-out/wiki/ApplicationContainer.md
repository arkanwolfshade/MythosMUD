# ApplicationContainer

> 170 nodes · cohesion 0.02

## Key Concepts

- **CorpseLifecycleService** (71 connections) — `server/services/corpse_lifecycle_service.py`
- **test_corpse_lifecycle_service.py** (61 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **test_corpse_lifecycle_decay.py** (28 connections) — `server/tests/unit/services/test_corpse_lifecycle_decay.py`
- **asyncio** (18 connections)
- **CorpseServiceError** (16 connections) — `server/services/corpse_lifecycle_service.py`
- **asyncio** (16 connections)
- **UUID** (13 connections)
- **_get_enum_value()** (10 connections) — `server/services/corpse_lifecycle_service.py`
- **.create_corpse_on_death()** (9 connections) — `server/services/corpse_lifecycle_service.py`
- **_corpse_component()** (9 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **_dying_player()** (9 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **.cleanup_decayed_corpse()** (8 connections) — `server/services/corpse_lifecycle_service.py`
- **._persist_corpse()** (8 connections) — `server/services/corpse_lifecycle_service.py`
- **._require_corpse_container()** (8 connections) — `server/services/corpse_lifecycle_service.py`
- **_stack()** (8 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **test_create_corpse_on_death_logs_but_does_not_raise_when_clearing_the_player_fails()** (8 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **test_create_corpse_on_death_nests_worn_container_contents_and_deletes_its_row()** (8 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **test_create_corpse_on_death_spills_past_the_slot_limit_onto_extra_corpses()** (8 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **._collect_death_items()** (7 connections) — `server/services/corpse_lifecycle_service.py`
- **CorpseNotFoundError** (7 connections) — `server/services/corpse_lifecycle_service.py`
- **_DyingPlayer** (7 connections) — `server/services/corpse_lifecycle_service.py`
- **_filter_container_data()** (7 connections) — `server/services/corpse_lifecycle_service.py`
- **_async_attr()** (7 connections) — `server/tests/unit/services/test_corpse_lifecycle_decay.py`
- **_RecordingRoom** (7 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **test_create_corpse_on_death_ignores_worn_rows_for_other_items_and_non_equipment()** (7 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- *... and 145 more nodes in this community*

## Relationships

- [connection_manager_methods.py](connection_manager_methods.py.md) (59 shared connections)
- [CombatService](CombatService.md) (8 shared connections)
- [test_npc_combat_integration_join.py](test_npc_combat_integration_join.py.md) (4 shared connections)
- [endpoints.py](endpoints.py.md) (4 shared connections)
- [test_analyze_idle_memory_samples.py](test_analyze_idle_memory_samples.py.md) (4 shared connections)
- [test_lucidity_recovery_commands.py](test_lucidity_recovery_commands.py.md) (1 shared connections)
- [AttributeError](AttributeError.md) (1 shared connections)
- [inventory_item_matching.py](inventory_item_matching.py.md) (1 shared connections)

## Source Files

- `server/services/corpse_lifecycle_service.py`
- `server/tests/unit/services/test_corpse_lifecycle_decay.py`
- `server/tests/unit/services/test_corpse_lifecycle_service.py`

## Audit Trail

- EXTRACTED: 360 (88%)
- INFERRED: 50 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*