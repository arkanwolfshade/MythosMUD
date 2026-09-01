# NPCDefinition

> 99 nodes

## Key Concepts

- **NPCDefinition** (110 connections) — `server/models/npc.py`
- **test_npc_models.py** (33 connections) — `server/tests/unit/models/test_npc_models.py`
- **NPCRelationship** (9 connections) — `server/models/npc.py`
- **._evaluate_spawn_requirements()** (8 connections) — `server/npc/spawning_service.py`
- **._evaluate_spawn_rules()** (7 connections) — `server/npc/spawning_service.py`
- **._register_spawned_npc_in_population_stats()** (6 connections) — `server/npc/population_control.py`
- **._spawn_npc()** (6 connections) — `server/npc/population_control.py`
- **._calculate_spawn_priority()** (6 connections) — `server/npc/spawning_service.py`
- **._maybe_add_required_npc_request()** (6 connections) — `server/npc/spawning_service.py`
- **NPCSpawnRequest** (5 connections)
- **_set_default_if_missing()** (4 connections) — `server/models/npc.py`
- **.can_spawn_npc()** (4 connections) — `server/npc/lifecycle_manager.py`
- **.__init__()** (4 connections) — `server/npc/spawning_models.py`
- **.__init__()** (3 connections) — `server/models/npc.py`
- **.create_npc_instance()** (3 connections) — `server/npc/lifecycle_manager.py`
- **.__init__()** (3 connections) — `server/npc/lifecycle_types.py`
- **.from_dict()** (3 connections) — `server/npc/npc_base.py`
- **.load_npc_definitions()** (3 connections) — `server/npc/population_control.py`
- **.spawn_npc()** (3 connections) — `server/npc/population_control.py`
- **test_npc_definition_can_spawn()** (3 connections) — `server/tests/unit/models/test_npc_models.py`
- **test_npc_definition_creation()** (3 connections) — `server/tests/unit/models/test_npc_models.py`
- **test_npc_definition_defaults()** (3 connections) — `server/tests/unit/models/test_npc_models.py`
- **test_npc_definition_get_ai_integration_stub()** (3 connections) — `server/tests/unit/models/test_npc_models.py`
- **test_npc_definition_get_base_stats()** (3 connections) — `server/tests/unit/models/test_npc_models.py`
- **test_npc_definition_get_base_stats_empty()** (3 connections) — `server/tests/unit/models/test_npc_models.py`
- *... and 74 more nodes in this community*

## Relationships

- [EventBus](EventBus.md) (30 shared connections)
- [NPCSpawnRule](NPCSpawnRule.md) (22 shared connections)
- [event_types.py](event_types.py.md) (14 shared connections)
- [NPCDefinitionCRUDMixin](NPCDefinitionCRUDMixin.md) (8 shared connections)
- [test_spawn_validator.py](test_spawn_validator.py.md) (7 shared connections)
- [migrate_combat_data.py](migrate_combat_data.py.md) (7 shared connections)
- [_JSONDict](_JSONDict.md) (6 shared connections)
- [._execute_wander_movement](_execute_wander_movement.md) (4 shared connections)
- [test_lifecycle_periodic.py](test_lifecycle_periodic.py.md) (3 shared connections)
- [ZoneConfiguration](ZoneConfiguration.md) (3 shared connections)
- [test_npc_definitions_api.py](test_npc_definitions_api.py.md) (2 shared connections)
- [Player](Player.md) (2 shared connections)

## Source Files

- `server/models/npc.py`
- `server/npc/lifecycle_manager.py`
- `server/npc/lifecycle_types.py`
- `server/npc/npc_base.py`
- `server/npc/population_control.py`
- `server/npc/spawning_models.py`
- `server/npc/spawning_service.py`
- `server/tests/unit/models/test_npc_models.py`

## Audit Trail

- EXTRACTED: 238 (100%)
- INFERRED: 1 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*