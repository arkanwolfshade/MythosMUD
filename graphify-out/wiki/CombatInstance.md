# CombatInstance

> 215 nodes · cohesion 0.01

## Key Concepts

- **NPCLifecycleManager** (71 connections) — `server/npc/lifecycle_manager.py`
- **NPCPopulationController** (60 connections) — `server/npc/population_control.py`
- **NPCEnteredRoom** (53 connections) — `server/events/event_types.py`
- **test_npc_instance_service.py** (53 connections) — `server/tests/unit/services/test_npc_instance_service.py`
- **lifecycle_manager.py** (49 connections) — `server/npc/lifecycle_manager.py`
- **population_control.py** (42 connections) — `server/npc/population_control.py`
- **event_bus.py** (40 connections) — `server/events/event_bus.py`
- **models/npc.py** (39 connections) — `server/models/npc.py`
- **npc_instance_service.py** (32 connections) — `server/services/npc_instance_service.py`
- **NPCInstanceService** (25 connections) — `server/services/npc_instance_service.py`
- **asyncio** (23 connections)
- **initialize_npc_instance_service()** (14 connections) — `server/services/npc_instance_service.py`
- **._spawn_npc_impl()** (12 connections) — `server/npc/lifecycle_manager.py`
- **._create_npc_services()** (10 connections) — `server/container/bundles/npc.py`
- **Any** (10 connections)
- **.__init__()** (8 connections) — `server/npc/lifecycle_manager.py`
- **.__init__()** (8 connections) — `server/npc/population_control.py`
- **._should_spawn_npc()** (8 connections) — `server/npc/population_control.py`
- **fixture** (8 connections)
- **._check_spawn_requirements_for_room()** (7 connections) — `server/npc/population_control.py`
- **_PopulationLifecycleManager** (7 connections) — `server/npc/population_control.py`
- **._finalize_spawn_record()** (6 connections) — `server/npc/lifecycle_manager.py`
- **._notify_room_and_threads()** (6 connections) — `server/npc/lifecycle_manager.py`
- **._register_spawned_npc_in_population_stats()** (6 connections) — `server/npc/population_control.py`
- **._spawn_npc()** (6 connections) — `server/npc/population_control.py`
- *... and 190 more nodes in this community*

## Relationships

- [ErrorType](ErrorType.md) (34 shared connections)
- [BaseEvent](BaseEvent.md) (31 shared connections)
- [RoomLoader](RoomLoader.md) (22 shared connections)
- [get_username_from_user](get_username_from_user.md) (19 shared connections)
- [ADR-023: Package Ownership (`game/` vs `services/` vs `npc/`) and Fan-Out Watch List](ADR-023-_Package_Ownership_`game-`_vs_`services-`_vs_`npc-`_and_Fan-Out_Watch_List.md) (19 shared connections)
- [Room](Room.md) (18 shared connections)
- [SpellLearningService](SpellLearningService.md) (17 shared connections)
- [aggro_threat.py](aggro_threat.py.md) (14 shared connections)
- [test_rescue_service.py](test_rescue_service.py.md) (14 shared connections)
- [command_parser.py](command_parser.py.md) (12 shared connections)
- [rescue_commands.py](rescue_commands.py.md) (10 shared connections)
- [test_message_handlers.py](test_message_handlers.py.md) (9 shared connections)

## Source Files

- `server/container/bundles/npc.py`
- `server/events/event_bus.py`
- `server/events/event_types.py`
- `server/models/npc.py`
- `server/models/room.py`
- `server/npc/lifecycle_manager.py`
- `server/npc/population_control.py`
- `server/services/npc_instance_service.py`
- `server/tests/unit/services/test_npc_instance_service.py`

## Audit Trail

- EXTRACTED: 610 (90%)
- INFERRED: 66 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*