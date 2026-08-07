# room look commands

> 225 nodes

## Key Concepts

- **NPCDefinition** (121 connections) — `server/models/npc.py`
- **NPCSpawnRule** (55 connections) — `server/models/npc.py`
- **npc.py** (38 connections) — `server/models/npc.py`
- **test_npc_models.py** (33 connections) — `server/tests/unit/models/test_npc_models.py`
- **spawning_instance_factory.py** (25 connections) — `server/npc/spawning_instance_factory.py`
- **test_spawn_validator.py** (24 connections) — `server/tests/unit/npc/test_spawn_validator.py`
- **should_spawn_npc()** (22 connections) — `server/npc/spawn_validator.py`
- **SimpleNPCDefinition** (17 connections) — `server/npc/spawning_models.py`
- **create_npc_instance()** (16 connections) — `server/npc/spawning_instance_factory.py`
- **npc_startup_service.py** (16 connections) — `server/services/npc_startup_service.py`
- **._spawn_npc_impl()** (14 connections) — `server/npc/lifecycle_manager.py`
- **spawning_models.py** (13 connections) — `server/npc/spawning_models.py`
- **combat_schema.py** (13 connections) — `server/schemas/combat/combat_schema.py`
- **spawn_validator.py** (11 connections) — `server/npc/spawn_validator.py`
- **_JSONDict** (10 connections)
- **generate_npc_id()** (10 connections) — `server/npc/spawning_instance_factory.py`
- **_instantiate_by_type()** (10 connections) — `server/npc/spawning_instance_factory.py`
- **NPCRelationship** (9 connections) — `server/models/npc.py`
- **_build_aggressive()** (9 connections) — `server/npc/spawning_instance_factory.py`
- **_loads_json_dict()** (7 connections) — `server/models/npc.py`
- **._evaluate_spawn_rules()** (7 connections) — `server/npc/spawning_service.py`
- **Base** (6 connections) — `server/models/npc.py`
- **.get_base_stats()** (6 connections) — `server/models/npc.py`
- **._check_dict_condition()** (6 connections) — `server/models/npc.py`
- **._spawn_value_allows_spawn()** (6 connections) — `server/models/npc.py`
- *... and 200 more nodes in this community*

## Relationships

- [Error Conversion](Error_Conversion.md) (75 shared connections)
- [commands inventory command](commands_inventory_command.md) (25 shared connections)
- [container events rationale](container_events_rationale.md) (13 shared connections)
- [logging examples fastapi](logging_examples_fastapi.md) (12 shared connections)
- [services nats service](services_nats_service.md) (11 shared connections)
- [lucidity event services](lucidity_event_services.md) (10 shared connections)
- [admin auth service](admin_auth_service.md) (9 shared connections)
- [spell game magic](spell_game_magic.md) (8 shared connections)
- [inventory mutation guard](inventory_mutation_guard.md) (7 shared connections)
- [persistence container rationale](persistence_container_rationale.md) (6 shared connections)
- [auth rationale access](auth_rationale_access.md) (6 shared connections)
- [player room realtime](player_room_realtime.md) (5 shared connections)

## Source Files

- `server/models/npc.py`
- `server/models/room.py`
- `server/npc/lifecycle_manager.py`
- `server/npc/lifecycle_types.py`
- `server/npc/population_control.py`
- `server/npc/spawn_validator.py`
- `server/npc/spawning_instance_factory.py`
- `server/npc/spawning_models.py`
- `server/npc/spawning_service.py`
- `server/schemas/combat/combat_schema.py`
- `server/services/npc_startup_service.py`
- `server/tests/unit/models/test_npc_models.py`
- `server/tests/unit/npc/test_spawn_validator.py`
- `server/tests/unit/npc/test_spawning_modules.py`
- `server/tests/unit/services/test_npc_instance_service.py`

## Audit Trail

- EXTRACTED: 866 (94%)
- INFERRED: 53 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*