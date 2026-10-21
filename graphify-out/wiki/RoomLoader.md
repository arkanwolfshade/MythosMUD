# RoomLoader

> 112 nodes · cohesion 0.03

## Key Concepts

- **NPCSpawningService** (69 connections) — `server/npc/spawning_service.py`
- **test_spawning_modules.py** (47 connections) — `server/tests/unit/npc/test_spawning_modules.py`
- **spawning_service.py** (40 connections) — `server/npc/spawning_service.py`
- **spawning_request_execution.py** (21 connections) — `server/npc/spawning_request_execution.py`
- **create_npc_instance()** (19 connections) — `server/npc/spawning_instance_factory.py`
- **NPCSpawnRequest** (19 connections) — `server/npc/spawning_models.py`
- **SimpleNPCDefinition** (19 connections) — `server/npc/spawning_models.py`
- **spawn_npc_from_request()** (18 connections) — `server/npc/spawning_request_execution.py`
- **NPCSpawnResult** (15 connections) — `server/npc/spawning_models.py`
- **spawning_models.py** (14 connections) — `server/npc/spawning_models.py`
- **generate_npc_id()** (10 connections) — `server/npc/spawning_instance_factory.py`
- **_spawn_success()** (8 connections) — `server/npc/spawning_request_execution.py`
- **._evaluate_spawn_requirements()** (8 connections) — `server/npc/spawning_service.py`
- **.__init__()** (8 connections) — `server/npc/spawning_service.py`
- **._evaluate_spawn_rules()** (7 connections) — `server/npc/spawning_service.py`
- **_room_from_persistence()** (6 connections) — `server/npc/spawning_request_execution.py`
- **._calculate_spawn_priority()** (6 connections) — `server/npc/spawning_service.py`
- **._create_npc_instance()** (6 connections) — `server/npc/spawning_service.py`
- **._maybe_add_required_npc_request()** (6 connections) — `server/npc/spawning_service.py`
- **._spawn_npc_from_request()** (6 connections) — `server/npc/spawning_service.py`
- **_coerce_simple_definition()** (5 connections) — `server/npc/spawning_instance_factory.py`
- **._check_spawn_requirements_for_room()** (5 connections) — `server/npc/spawning_service.py`
- **._generate_npc_id()** (5 connections) — `server/npc/spawning_service.py`
- **.get_spawn_statistics()** (5 connections) — `server/npc/spawning_service.py`
- **NPCSpawnRequest** (5 connections)
- *... and 87 more nodes in this community*

## Relationships

- [BaseEvent](BaseEvent.md) (44 shared connections)
- [get_username_from_user](get_username_from_user.md) (27 shared connections)
- [CombatInstance](CombatInstance.md) (22 shared connections)
- [ErrorType](ErrorType.md) (17 shared connections)
- [PlayerEventHandlerUtils](PlayerEventHandlerUtils.md) (5 shared connections)
- [ValidationError](ValidationError.md) (5 shared connections)
- [Room](Room.md) (5 shared connections)
- [ADR-023: Package Ownership (`game/` vs `services/` vs `npc/`) and Fan-Out Watch List](ADR-023-_Package_Ownership_`game-`_vs_`services-`_vs_`npc-`_and_Fan-Out_Watch_List.md) (5 shared connections)
- [aggro_threat.py](aggro_threat.py.md) (5 shared connections)
- [test_message_handlers.py](test_message_handlers.py.md) (4 shared connections)
- [rescue_commands.py](rescue_commands.py.md) (3 shared connections)
- [test_message_category_invariants.py](test_message_category_invariants.py.md) (3 shared connections)

## Source Files

- `server/npc/spawning_instance_factory.py`
- `server/npc/spawning_models.py`
- `server/npc/spawning_request_execution.py`
- `server/npc/spawning_service.py`
- `server/tests/unit/npc/test_spawning_modules.py`

## Audit Trail

- EXTRACTED: 320 (89%)
- INFERRED: 39 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*