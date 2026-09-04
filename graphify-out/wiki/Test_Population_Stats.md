# Test Population Stats

> 63 nodes

## Key Concepts

- **PopulationStats** (40 connections) — `server/npc/population_stats.py`
- **test_population_stats.py** (23 connections) — `server/tests/unit/npc/test_population_stats.py`
- **population_stats.py** (7 connections) — `server/npc/population_stats.py`
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
- *... and 38 more nodes in this community*

## Relationships

- [Test Population Control](Test_Population_Control.md) (7 shared connections)
- [NPC Behavior & Spawning](NPC_Behavior_&_Spawning.md) (5 shared connections)
- [Population Control](Population_Control.md) (2 shared connections)
- [Test Npc Utils](Test_Npc_Utils.md) (2 shared connections)
- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (2 shared connections)
- [Spawning Service](Spawning_Service.md) (1 shared connections)

## Source Files

- `server/npc/population_stats.py`
- `server/npc/spawning_service.py`
- `server/tests/unit/npc/test_population_control.py`
- `server/tests/unit/npc/test_population_stats.py`

## Audit Trail

- EXTRACTED: 99 (98%)
- INFERRED: 2 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*