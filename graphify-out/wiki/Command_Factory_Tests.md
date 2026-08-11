# Command Factory Tests

> 83 nodes

## Key Concepts

- **GameBundle** (45 connections) — `server/container/bundles/game.py`
- **InstanceManager** (19 connections) — `server/game/instance_manager.py`
- **MythosTickScheduler** (18 connections) — `server/time/tick_scheduler.py`
- **._init_player_quest_layer()** (16 connections) — `server/container/bundles/game.py`
- **LevelService** (13 connections) — `server/game/level_service.py`
- **._init_movement_layer()** (11 connections) — `server/container/bundles/game.py`
- **.initialize()** (11 connections) — `server/container/bundles/game.py`
- **._initialize_item_services()** (10 connections) — `server/container/bundles/game.py`
- **._init_temporal_layer()** (9 connections) — `server/container/bundles/game.py`
- **._init_quest_service()** (7 connections) — `server/container/bundles/game.py`
- **.create_instance()** (7 connections) — `server/game/instance_manager.py`
- **._initialize_caching_services()** (6 connections) — `server/container/bundles/game.py`
- **._build_instance_rooms()** (6 connections) — `server/game/instance_manager.py`
- **._build_prototype_payload()** (5 connections) — `server/container/bundles/game.py`
- **.__init__()** (5 connections) — `server/game/instance_manager.py`
- **Room** (5 connections)
- **._stable_id_from_room()** (5 connections) — `server/game/instance_manager.py`
- **._run()** (5 connections) — `server/time/tick_scheduler.py`
- **._emit_pending_ticks()** (5 connections) — `server/time/tick_scheduler.py`
- **._publish_tick()** (5 connections) — `server/time/tick_scheduler.py`
- **._require_core_services()** (4 connections) — `server/container/bundles/game.py`
- **._wire_user_manager_after_init()** (4 connections) — `server/container/bundles/game.py`
- **._handle_item_prototypes_db_error()** (4 connections) — `server/container/bundles/game.py`
- **Instance** (4 connections) — `server/game/instance_manager.py`
- **._get_template_rooms()** (4 connections) — `server/game/instance_manager.py`
- *... and 58 more nodes in this community*

## Relationships

- [WebSocket Code Review](WebSocket_Code_Review.md) (14 shared connections)
- [Optimization Archive Modernization](Optimization_Archive_Modernization.md) (10 shared connections)
- [User Manager Mute Tests](User_Manager_Mute_Tests.md) (8 shared connections)
- [Code Review Archive](Code_Review_Archive.md) (5 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (4 shared connections)
- [Player Occupant Processor](Player_Occupant_Processor.md) (4 shared connections)
- [Test Modernization Plan](Test_Modernization_Plan.md) (3 shared connections)
- [E 2 E Testing Guide](E_2_E_Testing_Guide.md) (2 shared connections)
- [Structured Concurrency Patterns](Structured_Concurrency_Patterns.md) (2 shared connections)
- [Combat Aggro Threat](Combat_Aggro_Threat.md) (2 shared connections)
- [Npc Services Combat](Npc_Services_Combat.md) (2 shared connections)
- [App Creation Flow Screens](App_Creation_Flow_Screens.md) (2 shared connections)

## Source Files

- `server/container/bundles/game.py`
- `server/game/instance_manager.py`
- `server/game/level_service.py`
- `server/time/tick_scheduler.py`

## Audit Trail

- EXTRACTED: 287 (89%)
- INFERRED: 37 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*