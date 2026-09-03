# Test Npc Utils

> 94 nodes

## Key Concepts

- **population_control.py** (42 connections) — `server/npc/population_control.py`
- **test_npc_utils.py** (37 connections) — `server/tests/unit/npc/test_npc_utils.py`
- **get_zone_key_from_room_id()** (17 connections) — `server/npc/npc_utils.py`
- **extract_room_id_from_npc()** (15 connections) — `server/npc/npc_utils.py`
- **npc_utils.py** (14 connections) — `server/npc/npc_utils.py`
- **extract_definition_id_from_npc()** (12 connections) — `server/npc/npc_utils.py`
- **extract_npc_metadata()** (11 connections) — `server/npc/npc_utils.py`
- **spawn_npc_via_population_controller()** (10 connections) — `server/npc/npc_utils.py`
- **extract_room_id_from_lifecycle_record()** (8 connections) — `server/npc/npc_utils.py`
- **.despawn_npc()** (8 connections) — `server/npc/population_control.py`
- **_PopulationLifecycleManager** (7 connections) — `server/npc/population_control.py`
- **._get_active_npcs_from_lifecycle_manager()** (6 connections) — `server/npc/population_control.py`
- **Any** (6 connections)
- **.cleanup_inactive_npcs()** (5 connections) — `server/npc/population_control.py`
- **_room_id_from_lifecycle_event()** (4 connections) — `server/npc/npc_utils.py`
- **._update_population_stats_for_despawn()** (4 connections) — `server/npc/population_control.py`
- **_stable_room_id_for_zone()** (3 connections) — `server/npc/npc_utils.py`
- **.get_zone_population_summary()** (3 connections) — `server/npc/population_control.py`
- **.spawn_npc()** (3 connections) — `server/npc/population_control.py`
- **test_extract_definition_id_from_npc_from_lifecycle_manager()** (3 connections) — `server/tests/unit/npc/test_npc_utils.py`
- **test_extract_definition_id_from_npc_has_definition_id()** (3 connections) — `server/tests/unit/npc/test_npc_utils.py`
- **test_extract_definition_id_from_npc_lifecycle_manager_no_definition()** (3 connections) — `server/tests/unit/npc/test_npc_utils.py`
- **test_extract_definition_id_from_npc_lifecycle_manager_no_record()** (3 connections) — `server/tests/unit/npc/test_npc_utils.py`
- **test_extract_definition_id_from_npc_no_manager()** (3 connections) — `server/tests/unit/npc/test_npc_utils.py`
- **test_extract_definition_id_from_npc_non_int()** (3 connections) — `server/tests/unit/npc/test_npc_utils.py`
- *... and 69 more nodes in this community*

## Relationships

- [Async Persistence & NPC Events](Async_Persistence_&_NPC_Events.md) (14 shared connections)
- [NPC Behavior & Spawning](NPC_Behavior_&_Spawning.md) (12 shared connections)
- [Test Zone Config Loader](Test_Zone_Config_Loader.md) (6 shared connections)
- [Npc Base](Npc_Base.md) (4 shared connections)
- [Population Control](Population_Control.md) (3 shared connections)
- [Test Lifecycle Periodic](Test_Lifecycle_Periodic.md) (3 shared connections)
- [Test Lifecycle Respawn](Test_Lifecycle_Respawn.md) (3 shared connections)
- [NPC Models](NPC_Models.md) (3 shared connections)
- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (3 shared connections)
- [Test Lifespan Startup](Test_Lifespan_Startup.md) (2 shared connections)
- [Test Population Stats](Test_Population_Stats.md) (2 shared connections)
- [Test Event Bus](Test_Event_Bus.md) (1 shared connections)

## Source Files

- `server/npc/npc_utils.py`
- `server/npc/population_control.py`
- `server/tests/unit/npc/test_npc_utils.py`

## Audit Trail

- EXTRACTED: 203 (100%)
- INFERRED: 1 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*