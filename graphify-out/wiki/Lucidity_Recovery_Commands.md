# Lucidity Recovery Commands

> 63 nodes

## Key Concepts

- **PopulationStats** (42 connections) — `server/npc/population_stats.py`
- **test_population_stats.py** (23 connections) — `server/tests/unit/npc/test_population_stats.py`
- **population_stats.py** (7 connections) — `server/npc/population_stats.py`
- **test_should_spawn_npc()** (5 connections) — `server/tests/unit/npc/test_population_control.py`
- **.to_dict()** (3 connections) — `server/npc/population_stats.py`
- **test_get_population_stats_existing()** (3 connections) — `server/tests/unit/npc/test_population_control.py`
- **test_clear_population_stats()** (3 connections) — `server/tests/unit/npc/test_population_control.py`
- **test_get_zone_population_summary_with_stats()** (3 connections) — `server/tests/unit/npc/test_population_control.py`
- **test_despawn_npc_success()** (3 connections) — `server/tests/unit/npc/test_population_control.py`
- **test_population_stats_init()** (3 connections) — `server/tests/unit/npc/test_population_stats.py`
- **test_add_npc_required()** (3 connections) — `server/tests/unit/npc/test_population_stats.py`
- **test_add_npc_optional()** (3 connections) — `server/tests/unit/npc/test_population_stats.py`
- **test_add_npc_multiple_same_type()** (3 connections) — `server/tests/unit/npc/test_population_stats.py`
- **test_add_npc_multiple_same_room()** (3 connections) — `server/tests/unit/npc/test_population_stats.py`
- **test_add_npc_without_definition_id()** (3 connections) — `server/tests/unit/npc/test_population_stats.py`
- **test_add_npc_updates_timestamp()** (3 connections) — `server/tests/unit/npc/test_population_stats.py`
- **test_remove_npc_required()** (3 connections) — `server/tests/unit/npc/test_population_stats.py`
- **test_remove_npc_optional()** (3 connections) — `server/tests/unit/npc/test_population_stats.py`
- **test_remove_npc_partial()** (3 connections) — `server/tests/unit/npc/test_population_stats.py`
- **test_remove_npc_not_found()** (3 connections) — `server/tests/unit/npc/test_population_stats.py`
- **test_remove_npc_prevents_negative()** (3 connections) — `server/tests/unit/npc/test_population_stats.py`
- **test_remove_npc_without_definition_id()** (3 connections) — `server/tests/unit/npc/test_population_stats.py`
- **test_remove_npc_updates_timestamp()** (3 connections) — `server/tests/unit/npc/test_population_stats.py`
- **test_to_dict()** (3 connections) — `server/tests/unit/npc/test_population_stats.py`
- **test_to_dict_copies()** (3 connections) — `server/tests/unit/npc/test_population_stats.py`
- *... and 38 more nodes in this community*

## Relationships

- [Commands Look Item](Commands_Look_Item.md) (9 shared connections)
- [Client Event Store](Client_Event_Store.md) (6 shared connections)
- [Whisper Remediation Plan](Whisper_Remediation_Plan.md) (4 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (2 shared connections)
- [Container Data Models](Container_Data_Models.md) (1 shared connections)
- [NPC Admin API](NPC_Admin_API.md) (1 shared connections)

## Source Files

- `server/npc/population_stats.py`
- `server/tests/unit/npc/test_population_control.py`
- `server/tests/unit/npc/test_population_stats.py`

## Audit Trail

- EXTRACTED: 182 (97%)
- INFERRED: 5 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*