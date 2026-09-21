# InstanceManager

> 56 nodes

## Key Concepts

- **InstanceManager** (27 connections) — `server/game/instance_manager.py`
- **test_instance_manager.py** (16 connections) — `server/tests/unit/game/test_instance_manager.py`
- **.create_instance()** (7 connections) — `server/game/instance_manager.py`
- **instance_manager()** (7 connections) — `server/tests/unit/game/test_instance_manager.py`
- **._build_instance_rooms()** (6 connections) — `server/game/instance_manager.py`
- **.__init__()** (5 connections) — `server/game/instance_manager.py`
- **._stable_id_from_room()** (5 connections) — `server/game/instance_manager.py`
- **room_cache()** (5 connections) — `server/tests/unit/game/test_instance_manager.py`
- **tutorial_room()** (5 connections) — `server/tests/unit/game/test_instance_manager.py`
- **Room** (5 connections)
- **Instance** (4 connections) — `server/game/instance_manager.py`
- **._get_template_rooms()** (4 connections) — `server/game/instance_manager.py`
- **._remap_exits()** (4 connections) — `server/game/instance_manager.py`
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
- **fixture** (3 connections)
- *... and 31 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (6 shared connections)
- [Room](Room.md) (4 shared connections)
- [PlayerPositionService](PlayerPositionService.md) (1 shared connections)
- [bundles/game.py](bundles-game.py.md) (1 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (1 shared connections)
- [EventBus](EventBus.md) (1 shared connections)
- [player_presence_tracker.py](player_presence_tracker.py.md) (1 shared connections)

## Source Files

- `server/game/instance_manager.py`
- `server/tests/unit/game/test_instance_manager.py`

## Audit Trail

- EXTRACTED: 81 (86%)
- INFERRED: 13 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*