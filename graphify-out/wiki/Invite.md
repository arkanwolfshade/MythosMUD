# Invite

> 108 nodes

## Key Concepts

- **NPCSpawningService** (61 connections) — `server/npc/spawning_service.py`
- **test_spawning_modules.py** (41 connections) — `server/tests/unit/npc/test_spawning_modules.py`
- **spawning_instance_factory.py** (25 connections) — `server/npc/spawning_instance_factory.py`
- **NPCSpawnRequest** (19 connections) — `server/npc/spawning_models.py`
- **spawn_npc_from_request()** (18 connections) — `server/npc/spawning_request_execution.py`
- **SimpleNPCDefinition** (16 connections) — `server/npc/spawning_models.py`
- **create_npc_instance()** (16 connections) — `server/npc/spawning_instance_factory.py`
- **NPCSpawnResult** (15 connections) — `server/npc/spawning_models.py`
- **generate_npc_id()** (10 connections) — `server/npc/spawning_instance_factory.py`
- **_instantiate_by_type()** (10 connections) — `server/npc/spawning_instance_factory.py`
- **_build_aggressive()** (8 connections) — `server/npc/spawning_instance_factory.py`
- **_spawn_success()** (8 connections) — `server/npc/spawning_request_execution.py`
- **._evaluate_spawn_requirements()** (8 connections) — `server/npc/spawning_service.py`
- **._evaluate_spawn_rules()** (7 connections) — `server/npc/spawning_service.py`
- **.__init__()** (7 connections) — `server/npc/spawning_service.py`
- **_build_passive()** (6 connections) — `server/npc/spawning_instance_factory.py`
- **_build_shopkeeper()** (6 connections) — `server/npc/spawning_instance_factory.py`
- **_room_from_persistence()** (6 connections) — `server/npc/spawning_request_execution.py`
- **._calculate_spawn_priority()** (6 connections) — `server/npc/spawning_service.py`
- **._create_npc_instance()** (6 connections) — `server/npc/spawning_service.py`
- **._maybe_add_required_npc_request()** (6 connections) — `server/npc/spawning_service.py`
- **._spawn_npc_from_request()** (6 connections) — `server/npc/spawning_service.py`
- **_coerce_simple_definition()** (5 connections) — `server/npc/spawning_instance_factory.py`
- **._check_spawn_requirements_for_room()** (5 connections) — `server/npc/spawning_service.py`
- **._generate_npc_id()** (5 connections) — `server/npc/spawning_service.py`
- *... and 83 more nodes in this community*

## Relationships

- [NPCDefinition](NPCDefinition.md) (52 shared connections)
- [NPCLifecycleManager](NPCLifecycleManager.md) (27 shared connections)
- [test_combat_monitoring_service.py](test_combat_monitoring_service.py.md) (10 shared connections)
- [test_movement_monitor.py](test_movement_monitor.py.md) (6 shared connections)
- [container_endpoints_basic.py](container_endpoints_basic.py.md) (6 shared connections)
- [RoomLoader](RoomLoader.md) (4 shared connections)
- [test_combat_attack_handler.py](test_combat_attack_handler.py.md) (3 shared connections)
- [test_channel_commands.py](test_channel_commands.py.md) (3 shared connections)
- [test_async_persistence_delegates.py](test_async_persistence_delegates.py.md) (3 shared connections)
- [generate_invites_db.py](generate_invites_db.py.md) (3 shared connections)
- [MetricsCollector](MetricsCollector.md) (2 shared connections)
- [dialogue_definitions_api.py](dialogue_definitions_api.py.md) (1 shared connections)

## Source Files

- `server/npc/spawning_instance_factory.py`
- `server/npc/spawning_models.py`
- `server/npc/spawning_request_execution.py`
- `server/npc/spawning_service.py`
- `server/tests/unit/npc/test_spawning_modules.py`

## Audit Trail

- EXTRACTED: 271 (85%)
- INFERRED: 47 (15%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*