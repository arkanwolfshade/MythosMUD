# NPCLifecycleManager

> 193 nodes

## Key Concepts

- **NPCLifecycleManager** (75 connections) — `server/npc/lifecycle_manager.py`
- **NPCPopulationController** (62 connections) — `server/npc/population_control.py`
- **test_npc_instance_service.py** (53 connections) — `server/tests/unit/services/test_npc_instance_service.py`
- **npc_instance_service.py** (32 connections) — `server/services/npc_instance_service.py`
- **NPCInstanceService** (24 connections) — `server/services/npc_instance_service.py`
- **asyncio** (23 connections)
- **bundles/npc.py** (15 connections) — `server/container/bundles/npc.py`
- **initialize_npc_instance_service()** (14 connections) — `server/services/npc_instance_service.py`
- **._spawn_npc_impl()** (12 connections) — `server/npc/lifecycle_manager.py`
- **load_zone_configurations()** (9 connections) — `server/npc/zone_config_loader.py`
- **._create_npc_services()** (8 connections) — `server/container/bundles/npc.py`
- **.__init__()** (8 connections) — `server/npc/lifecycle_manager.py`
- **Any** (8 connections)
- **fixture** (8 connections)
- **._check_spawn_requirements_for_room()** (7 connections) — `server/npc/population_control.py`
- **.__init__()** (7 connections) — `server/npc/population_control.py`
- **._finalize_spawn_record()** (6 connections) — `server/npc/lifecycle_manager.py`
- **._notify_room_and_threads()** (6 connections) — `server/npc/lifecycle_manager.py`
- **.__init__()** (6 connections) — `server/services/npc_instance_service.py`
- **.get_lifecycle_statistics()** (5 connections) — `server/npc/lifecycle_manager.py`
- **._handle_spawn_service_failure()** (5 connections) — `server/npc/lifecycle_manager.py`
- **._queue_npc_thread_start()** (5 connections) — `server/npc/lifecycle_manager.py`
- **._handle_player_entered_room()** (5 connections) — `server/npc/population_control.py`
- **.npc_entered()** (4 connections) — `server/models/room.py`
- **.can_spawn_npc()** (4 connections) — `server/npc/lifecycle_manager.py`
- *... and 168 more nodes in this community*

## Relationships

- [EventBus](EventBus.md) (46 shared connections)
- [lifecycle_manager.py](lifecycle_manager.py.md) (26 shared connections)
- [event_types.py](event_types.py.md) (14 shared connections)
- [CombatService](CombatService.md) (12 shared connections)
- [population_control.py](population_control.py.md) (12 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (10 shared connections)
- [get_npc_instance_service](get_npc_instance_service.md) (9 shared connections)
- [lifespan_startup.py](lifespan_startup.py.md) (8 shared connections)
- [get_logger](get_logger.md) (6 shared connections)
- [ZoneConfiguration](ZoneConfiguration.md) (6 shared connections)
- [test_population_control.py](test_population_control.py.md) (4 shared connections)
- [test_zone_config_loader.py](test_zone_config_loader.py.md) (4 shared connections)

## Source Files

- `server/container/bundles/npc.py`
- `server/models/room.py`
- `server/npc/lifecycle_manager.py`
- `server/npc/population_control.py`
- `server/npc/zone_config_loader.py`
- `server/services/npc_instance_service.py`
- `server/tests/unit/services/test_npc_instance_service.py`

## Audit Trail

- EXTRACTED: 423 (91%)
- INFERRED: 41 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*