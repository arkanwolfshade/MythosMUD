# NPC Definition Schemas

> 138 nodes · cohesion 0.02

## Key Concepts

- **NPCDefinition** (53 connections) — `server/models/npc.py`
- **NPCSpawnRule** (36 connections) — `server/models/npc.py`
- **test_npc_models.py** (32 connections) — `server/tests/unit/models/test_npc_models.py`
- **npc_schemas.py** (21 connections) — `server/api/admin/npc_schemas.py`
- **lifecycle_periodic.py** (16 connections) — `server/npc/lifecycle_periodic.py`
- **_JSONDict** (10 connections) — `server/models/npc.py`
- **NPCRelationship** (9 connections) — `server/models/npc.py`
- **Any** (9 connections) — `server/npc/lifecycle_periodic.py`
- **check_optional_npc_spawns_impl()** (8 connections) — `server/npc/lifecycle_periodic.py`
- **_loads_json_dict()** (7 connections) — `server/models/npc.py`
- **run_periodic_maintenance_impl()** (7 connections) — `server/npc/lifecycle_periodic.py`
- **Base** (6 connections) — `server/models/npc.py`
- **._check_dict_condition()** (6 connections) — `server/models/npc.py`
- **._spawn_value_allows_spawn()** (6 connections) — `server/models/npc.py`
- **cleanup_old_records_impl()** (6 connections) — `server/npc/lifecycle_periodic.py`
- **.get_base_stats()** (5 connections) — `server/models/npc.py`
- **.get_spawn_conditions()** (5 connections) — `server/models/npc.py`
- **._single_spawn_condition_ok()** (5 connections) — `server/models/npc.py`
- **_attempt_optional_npc_spawn()** (5 connections) — `server/npc/lifecycle_periodic.py`
- **get_spawn_room_for_definition()** (5 connections) — `server/npc/lifecycle_periodic.py`
- **get_zone_key_for_definition()** (5 connections) — `server/npc/lifecycle_periodic.py`
- **.get_ai_integration_stub()** (4 connections) — `server/models/npc.py`
- **.get_behavior_config()** (4 connections) — `server/models/npc.py`
- **.check_spawn_conditions()** (4 connections) — `server/models/npc.py`
- **_check_spawn_conditions_for_optional_npc()** (4 connections) — `server/npc/lifecycle_periodic.py`
- *... and 113 more nodes in this community*

## Relationships

- [[NPC Admin API]] (10 shared connections)
- [[NPC Death Lifecycle]] (10 shared connections)
- [[NPC Definition Admin API]] (9 shared connections)
- [[Aggressive Mob NPC]] (9 shared connections)
- [[NPC Services Bundle]] (6 shared connections)
- [[Api Admin Npc]] (4 shared connections)
- [[SQLAlchemy Model Base]] (4 shared connections)
- [[Distributed Event Bus]] (3 shared connections)
- [[NPC Database Sessions]] (3 shared connections)
- [[NPC Admin Commands]] (2 shared connections)
- [[Validation Rule Base]] (2 shared connections)
- [[Zone Config Loader]] (2 shared connections)

## Source Files

- `server/api/admin/npc_schemas.py`
- `server/models/npc.py`
- `server/npc/lifecycle_manager.py`
- `server/npc/lifecycle_periodic.py`
- `server/tests/unit/models/test_npc_models.py`

## Audit Trail

- EXTRACTED: 473 (99%)
- INFERRED: 3 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
