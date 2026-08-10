# Status Effect Model

> 54 nodes

## Key Concepts

- **InstanceManager** (19 connections) — `server/game/instance_manager.py`
- **test_instance_manager.py** (15 connections) — `server/tests/unit/game/test_instance_manager.py`
- **._init_movement_layer()** (11 connections) — `server/container/bundles/game.py`
- **.create_instance()** (7 connections) — `server/game/instance_manager.py`
- **._build_instance_rooms()** (6 connections) — `server/game/instance_manager.py`
- **.__init__()** (5 connections) — `server/game/instance_manager.py`
- **Room** (5 connections)
- **._stable_id_from_room()** (5 connections) — `server/game/instance_manager.py`
- **Instance** (4 connections) — `server/game/instance_manager.py`
- **._get_template_rooms()** (4 connections) — `server/game/instance_manager.py`
- **._remap_exits()** (4 connections) — `server/game/instance_manager.py`
- **instance_manager()** (4 connections) — `server/tests/unit/game/test_instance_manager.py`
- **._stable_id_from_target()** (3 connections) — `server/game/instance_manager.py`
- **.get_instance()** (3 connections) — `server/game/instance_manager.py`
- **.get_room_by_id()** (3 connections) — `server/game/instance_manager.py`
- **tutorial_room()** (3 connections) — `server/tests/unit/game/test_instance_manager.py`
- **UUID** (2 connections)
- **.destroy_instance()** (2 connections) — `server/game/instance_manager.py`
- **.get_first_room_id()** (2 connections) — `server/game/instance_manager.py`
- **.get_exit_room_id()** (2 connections) — `server/game/instance_manager.py`
- **room_cache()** (2 connections) — `server/tests/unit/game/test_instance_manager.py`
- **test_create_instance()** (2 connections) — `server/tests/unit/game/test_instance_manager.py`
- **test_create_instance_raises_when_no_templates()** (2 connections) — `server/tests/unit/game/test_instance_manager.py`
- **test_destroy_instance()** (2 connections) — `server/tests/unit/game/test_instance_manager.py`
- **test_get_first_room_id()** (2 connections) — `server/tests/unit/game/test_instance_manager.py`
- *... and 29 more nodes in this community*

## Relationships

- [Level and XP Curve](Level_and_XP_Curve.md) (6 shared connections)
- [Cache and NPC Cache](Cache_and_NPC_Cache.md) (3 shared connections)
- [Game Service Bundle](Game_Service_Bundle.md) (3 shared connections)
- [Dependency Injection Tests](Dependency_Injection_Tests.md) (2 shared connections)
- [User Manager Mute Tests](User_Manager_Mute_Tests.md) (1 shared connections)
- [NPC Utility Functions](NPC_Utility_Functions.md) (1 shared connections)
- [Combat Client Crash Report](Combat_Client_Crash_Report.md) (1 shared connections)
- [Combat DP Persistence Tests](Combat_DP_Persistence_Tests.md) (1 shared connections)
- [NPC Event Handler Tests](NPC_Event_Handler_Tests.md) (1 shared connections)
- [Commands Container Inventory](Commands_Container_Inventory.md) (1 shared connections)
- [NATS Message Broker](NATS_Message_Broker.md) (1 shared connections)

## Source Files

- `server/container/bundles/game.py`
- `server/game/instance_manager.py`
- `server/tests/unit/game/test_instance_manager.py`

## Audit Trail

- EXTRACTED: 148 (98%)
- INFERRED: 3 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*