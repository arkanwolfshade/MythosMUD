# Community 131

> 86 nodes

## Key Concepts

- **NPCDefinition** (81 connections) — `server/models/npc.py`
- **should_spawn_npc()** (24 connections) — `server/npc/spawn_validator.py`
- **test_spawn_validator.py** (24 connections) — `server/tests/unit/npc/test_spawn_validator.py`
- **spawn_validator.py** (14 connections) — `server/npc/spawn_validator.py`
- **queries.py** (11 connections) — `server/services/npc_service/queries.py`
- **._should_spawn_npc()** (8 connections) — `server/npc/population_control.py`
- **_try_spawn_rules()** (8 connections) — `server/npc/spawn_validator.py`
- **NPCQueryMixin** (7 connections) — `server/services/npc_service/queries.py`
- **_row_to_npc_definition()** (7 connections) — `server/services/npc_service_models.py`
- **._notify_room_and_threads()** (6 connections) — `server/npc/lifecycle_manager.py`
- **_spawn_rule_passes()** (6 connections) — `server/npc/spawn_validator.py`
- **._queue_npc_thread_start()** (5 connections) — `server/npc/lifecycle_manager.py`
- **_population_allows_spawn()** (5 connections) — `server/npc/spawn_validator.py`
- **.get_npc_definitions_by_sub_zone()** (5 connections) — `server/services/npc_service/queries.py`
- **.get_npc_definitions_by_type()** (5 connections) — `server/services/npc_service/queries.py`
- **.get_system_statistics()** (5 connections) — `server/services/npc_service/queries.py`
- **.can_spawn_npc()** (4 connections) — `server/npc/lifecycle_manager.py`
- **._start_npc_thread_async()** (4 connections) — `server/npc/lifecycle_manager.py`
- **.__init__()** (4 connections) — `server/npc/spawning_models.py`
- **mock_zone_config()** (4 connections) — `server/tests/unit/npc/test_spawn_validator.py`
- **.npc_entered()** (3 connections) — `server/models/room.py`
- **.__init__()** (3 connections) — `server/npc/lifecycle_types.py`
- **.load_npc_definitions()** (3 connections) — `server/npc/population_control.py`
- **mock_npc_definition()** (3 connections) — `server/tests/unit/npc/test_spawn_validator.py`
- **mock_population_stats()** (3 connections) — `server/tests/unit/npc/test_spawn_validator.py`
- *... and 61 more nodes in this community*

## Relationships

- [Community 35](Community_35.md) (15 shared connections)
- [Community 241](Community_241.md) (14 shared connections)
- [Community 304](Community_304.md) (10 shared connections)
- [Community 563](Community_563.md) (9 shared connections)
- [Community 206](Community_206.md) (9 shared connections)
- [Aliases & Webhook/Schema Validation](Aliases_&_Webhook-Schema_Validation.md) (8 shared connections)
- [NPC Population Control](NPC_Population_Control.md) (7 shared connections)
- [Community 91](Community_91.md) (6 shared connections)
- [Community 162](Community_162.md) (6 shared connections)
- [Community 829](Community_829.md) (6 shared connections)
- [Community 757](Community_757.md) (4 shared connections)
- [Community 258](Community_258.md) (3 shared connections)

## Source Files

- `server/models/npc.py`
- `server/models/room.py`
- `server/npc/lifecycle_manager.py`
- `server/npc/lifecycle_types.py`
- `server/npc/population_control.py`
- `server/npc/spawn_validator.py`
- `server/npc/spawning_models.py`
- `server/services/npc_service/queries.py`
- `server/services/npc_service_models.py`
- `server/tests/unit/npc/test_spawn_validator.py`

## Audit Trail

- EXTRACTED: 222 (98%)
- INFERRED: 5 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*