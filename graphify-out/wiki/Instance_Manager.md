# Instance Manager

> 59 nodes

## Key Concepts

- **InstanceManager** (27 connections) — `server/game/instance_manager.py`
- **test_instance_manager.py** (16 connections) — `server/tests/unit/game/test_instance_manager.py`
- **instance_manager.py** (10 connections) — `server/game/instance_manager.py`
- **.create_instance()** (7 connections) — `server/game/instance_manager.py`
- **._build_instance_rooms()** (6 connections) — `server/game/instance_manager.py`
- **instance_manager()** (6 connections) — `server/tests/unit/game/test_instance_manager.py`
- **._stable_id_from_room()** (5 connections) — `server/game/instance_manager.py`
- **Room** (5 connections)
- **Instance** (4 connections) — `server/game/instance_manager.py`
- **._get_template_rooms()** (4 connections) — `server/game/instance_manager.py`
- **.__init__()** (4 connections) — `server/game/instance_manager.py`
- **._remap_exits()** (4 connections) — `server/game/instance_manager.py`
- **room_cache()** (4 connections) — `server/tests/unit/game/test_instance_manager.py`
- **tutorial_room()** (4 connections) — `server/tests/unit/game/test_instance_manager.py`
- **.get_instance()** (3 connections) — `server/game/instance_manager.py`
- **.get_room_by_id()** (3 connections) — `server/game/instance_manager.py`
- **._stable_id_from_target()** (3 connections) — `server/game/instance_manager.py`
- **test_create_instance()** (3 connections) — `server/tests/unit/game/test_instance_manager.py`
- **test_create_instance_clones_rest_location_flag()** (3 connections) — `server/tests/unit/game/test_instance_manager.py`
- **test_create_instance_raises_when_no_templates()** (3 connections) — `server/tests/unit/game/test_instance_manager.py`
- **test_destroy_instance()** (3 connections) — `server/tests/unit/game/test_instance_manager.py`
- **test_get_exit_room_id()** (3 connections) — `server/tests/unit/game/test_instance_manager.py`
- **test_get_first_room_id()** (3 connections) — `server/tests/unit/game/test_instance_manager.py`
- **test_get_room_by_id_returns_none_for_non_instance()** (3 connections) — `server/tests/unit/game/test_instance_manager.py`
- **test_get_room_by_id_returns_room_when_in_instance()** (3 connections) — `server/tests/unit/game/test_instance_manager.py`
- *... and 34 more nodes in this community*

## Relationships

- [Async Persistence & NPC Events](Async_Persistence_&_NPC_Events.md) (3 shared connections)
- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (2 shared connections)
- [Test Player Position Service](Test_Player_Position_Service.md) (1 shared connections)
- [Application Container Bundles](Application_Container_Bundles.md) (1 shared connections)
- [Test Container Bundles](Test_Container_Bundles.md) (1 shared connections)
- [Test Player Presence Tracker](Test_Player_Presence_Tracker.md) (1 shared connections)
- [Test Player Respawn Service](Test_Player_Respawn_Service.md) (1 shared connections)
- [Container Exception Handling](Container_Exception_Handling.md) (1 shared connections)

## Source Files

- `server/game/instance_manager.py`
- `server/tests/unit/game/test_instance_manager.py`

## Audit Trail

- EXTRACTED: 86 (90%)
- INFERRED: 10 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*