# GameBundle

> 77 nodes

## Key Concepts

- **GameBundle** (45 connections) — `server/container/bundles/game.py`
- **InstanceManager** (19 connections) — `server/game/instance_manager.py`
- **MythosTickScheduler** (18 connections) — `server/time/tick_scheduler.py`
- **._init_player_quest_layer()** (16 connections) — `server/container/bundles/game.py`
- **._init_movement_layer()** (11 connections) — `server/container/bundles/game.py`
- **.initialize()** (11 connections) — `server/container/bundles/game.py`
- **._init_temporal_layer()** (9 connections) — `server/container/bundles/game.py`
- **._initialize_item_services()** (8 connections) — `server/container/bundles/game.py`
- **._init_quest_service()** (7 connections) — `server/container/bundles/game.py`
- **.create_instance()** (7 connections) — `server/game/instance_manager.py`
- **._initialize_caching_services()** (6 connections) — `server/container/bundles/game.py`
- **._build_instance_rooms()** (6 connections) — `server/game/instance_manager.py`
- **._build_prototype_payload()** (5 connections) — `server/container/bundles/game.py`
- **.__init__()** (5 connections) — `server/game/instance_manager.py`
- **._stable_id_from_room()** (5 connections) — `server/game/instance_manager.py`
- **._emit_pending_ticks()** (5 connections) — `server/time/tick_scheduler.py`
- **._publish_tick()** (5 connections) — `server/time/tick_scheduler.py`
- **._run()** (5 connections) — `server/time/tick_scheduler.py`
- **Room** (5 connections)
- **Instance** (4 connections) — `server/game/instance_manager.py`
- **._handle_item_prototypes_db_error()** (4 connections) — `server/container/bundles/game.py`
- **._require_core_services()** (4 connections) — `server/container/bundles/game.py`
- **._wire_user_manager_after_init()** (4 connections) — `server/container/bundles/game.py`
- **._get_template_rooms()** (4 connections) — `server/game/instance_manager.py`
- **._remap_exits()** (4 connections) — `server/game/instance_manager.py`
- *... and 52 more nodes in this community*

## Relationships

- [ApplicationContainer](ApplicationContainer.md) (12 shared connections)
- [server/exceptions.py](server-exceptions.py.md) (8 shared connections)
- [bundles/game.py](bundles-game.py.md) (7 shared connections)
- [Room](Room.md) (5 shared connections)
- [ScheduleService](ScheduleService.md) (4 shared connections)
- [EventBus](EventBus.md) (4 shared connections)
- [ProfessionCacheService](ProfessionCacheService.md) (2 shared connections)
- [RoomCacheService](RoomCacheService.md) (2 shared connections)
- [MovementService](MovementService.md) (2 shared connections)
- [ExplorationService](ExplorationService.md) (2 shared connections)
- [PlayerEnteredRoom](PlayerEnteredRoom.md) (2 shared connections)
- [PlayerPositionService](PlayerPositionService.md) (2 shared connections)

## Source Files

- `server/container/bundles/game.py`
- `server/game/instance_manager.py`
- `server/time/tick_scheduler.py`

## Audit Trail

- EXTRACTED: 160 (83%)
- INFERRED: 33 (17%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*