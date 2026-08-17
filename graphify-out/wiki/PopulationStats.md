# PopulationStats

> 61 nodes

## Key Concepts

- **PopulationStats** (40 connections) — `server/npc/population_stats.py`
- **test_population_stats.py** (23 connections) — `server/tests/unit/npc/test_population_stats.py`
- **.to_dict()** (3 connections) — `server/npc/population_stats.py`
- **.get_population_stats()** (3 connections) — `server/npc/spawning_service.py`
- **test_clear_population_stats()** (3 connections) — `server/tests/unit/npc/test_population_control.py`
- **test_despawn_npc_success()** (3 connections) — `server/tests/unit/npc/test_population_control.py`
- **test_get_population_stats_existing()** (3 connections) — `server/tests/unit/npc/test_population_control.py`
- **test_get_zone_population_summary_with_stats()** (3 connections) — `server/tests/unit/npc/test_population_control.py`
- **test_add_npc_multiple_same_room()** (3 connections) — `server/tests/unit/npc/test_population_stats.py`
- **test_add_npc_multiple_same_type()** (3 connections) — `server/tests/unit/npc/test_population_stats.py`
- **test_add_npc_optional()** (3 connections) — `server/tests/unit/npc/test_population_stats.py`
- **test_add_npc_required()** (3 connections) — `server/tests/unit/npc/test_population_stats.py`
- **test_add_npc_updates_timestamp()** (3 connections) — `server/tests/unit/npc/test_population_stats.py`
- **test_add_npc_without_definition_id()** (3 connections) — `server/tests/unit/npc/test_population_stats.py`
- **test_mixed_required_optional()** (3 connections) — `server/tests/unit/npc/test_population_stats.py`
- **test_multiple_definitions_same_type()** (3 connections) — `server/tests/unit/npc/test_population_stats.py`
- **test_population_stats_init()** (3 connections) — `server/tests/unit/npc/test_population_stats.py`
- **test_remove_npc_different_definition()** (3 connections) — `server/tests/unit/npc/test_population_stats.py`
- **test_remove_npc_not_found()** (3 connections) — `server/tests/unit/npc/test_population_stats.py`
- **test_remove_npc_optional()** (3 connections) — `server/tests/unit/npc/test_population_stats.py`
- **test_remove_npc_partial()** (3 connections) — `server/tests/unit/npc/test_population_stats.py`
- **test_remove_npc_prevents_negative()** (3 connections) — `server/tests/unit/npc/test_population_stats.py`
- **test_remove_npc_required()** (3 connections) — `server/tests/unit/npc/test_population_stats.py`
- **test_remove_npc_updates_timestamp()** (3 connections) — `server/tests/unit/npc/test_population_stats.py`
- **test_remove_npc_without_definition_id()** (3 connections) — `server/tests/unit/npc/test_population_stats.py`
- *... and 36 more nodes in this community*

## Relationships

- [ConnectionManager](ConnectionManager.md) (9 shared connections)
- [NPCLifecycleManager](NPCLifecycleManager.md) (3 shared connections)
- [EventBus](EventBus.md) (3 shared connections)
- [ZoneConfiguration](ZoneConfiguration.md) (1 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (1 shared connections)

## Source Files

- `server/npc/population_stats.py`
- `server/npc/spawning_service.py`
- `server/tests/unit/npc/test_population_control.py`
- `server/tests/unit/npc/test_population_stats.py`

## Audit Trail

- EXTRACTED: 70 (73%)
- INFERRED: 26 (27%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*