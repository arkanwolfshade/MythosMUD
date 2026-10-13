# Community 40

> 138 nodes

## Key Concepts

- **NPCPopulationController** (53 connections) — `server/npc/population_control.py`
- **test_npc_utils.py** (37 connections) — `server/tests/unit/npc/test_npc_utils.py`
- **get_zone_key_from_room_id()** (17 connections) — `server/npc/npc_utils.py`
- **extract_room_id_from_npc()** (15 connections) — `server/npc/npc_utils.py`
- **NPCBundle** (14 connections) — `server/container/bundles/npc.py`
- **npc_utils.py** (14 connections) — `server/npc/npc_utils.py`
- **extract_definition_id_from_npc()** (12 connections) — `server/npc/npc_utils.py`
- **extract_npc_metadata()** (12 connections) — `server/npc/npc_utils.py`
- **spawn_npc_via_population_controller()** (11 connections) — `server/npc/npc_utils.py`
- **._create_npc_services()** (10 connections) — `server/container/bundles/npc.py`
- **extract_room_id_from_lifecycle_record()** (8 connections) — `server/npc/npc_utils.py`
- **.despawn_npc()** (8 connections) — `server/npc/population_control.py`
- **._should_spawn_npc()** (8 connections) — `server/npc/population_control.py`
- **._check_spawn_requirements_for_room()** (7 connections) — `server/npc/population_control.py`
- **.__init__()** (7 connections) — `server/npc/population_control.py`
- **.initialize()** (6 connections) — `server/container/bundles/npc.py`
- **_resolve_despawn_room_id()** (6 connections) — `server/npc/lifecycle_despawn.py`
- **._get_active_npcs_from_lifecycle_manager()** (6 connections) — `server/npc/population_control.py`
- **._register_spawned_npc_in_population_stats()** (6 connections) — `server/npc/population_control.py`
- **._spawn_npc()** (6 connections) — `server/npc/population_control.py`
- **Any** (6 connections)
- **.cleanup_inactive_npcs()** (5 connections) — `server/npc/population_control.py`
- **._get_zone_key_from_room_id()** (5 connections) — `server/npc/population_control.py`
- **._handle_player_entered_room()** (5 connections) — `server/npc/population_control.py`
- **._should_remove_inactive_npc()** (5 connections) — `server/npc/population_control.py`
- *... and 113 more nodes in this community*

## Relationships

- [NPC Behavior Engine](NPC_Behavior_Engine.md) (25 shared connections)
- [Community 53](Community_53.md) (12 shared connections)
- [NPC Room Lifecycle](NPC_Room_Lifecycle.md) (8 shared connections)
- [NPC Population Stats](NPC_Population_Stats.md) (8 shared connections)
- [NPC Definition JSON](NPC_Definition_JSON.md) (5 shared connections)
- [Game Event Types](Game_Event_Types.md) (4 shared connections)
- [Magic Service Lifespan](Magic_Service_Lifespan.md) (3 shared connections)
- [Community 77](Community_77.md) (3 shared connections)
- [Community 536](Community_536.md) (3 shared connections)
- [Community 91](Community_91.md) (2 shared connections)
- [Community 48](Community_48.md) (2 shared connections)
- [Distributed Event Bus (NATS)](Distributed_Event_Bus_NATS.md) (2 shared connections)

## Source Files

- `server/container/bundles/npc.py`
- `server/models/npc.py`
- `server/npc/lifecycle_despawn.py`
- `server/npc/npc_utils.py`
- `server/npc/population_control.py`
- `server/tests/unit/npc/test_npc_utils.py`
- `server/tests/unit/npc/test_population_control.py`

## Audit Trail

- EXTRACTED: 269 (92%)
- INFERRED: 23 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*