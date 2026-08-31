# InstanceManager

> 55 nodes

## Key Concepts

- **InstanceManager** (19 connections) — `server/game/instance_manager.py`
- **test_instance_manager.py** (16 connections) — `server/tests/unit/game/test_instance_manager.py`
- **._init_movement_layer()** (11 connections) — `server/container/bundles/game.py`
- **.create_instance()** (7 connections) — `server/game/instance_manager.py`
- **._build_instance_rooms()** (6 connections) — `server/game/instance_manager.py`
- **.__init__()** (5 connections) — `server/game/instance_manager.py`
- **._stable_id_from_room()** (5 connections) — `server/game/instance_manager.py`
- **instance_manager()** (5 connections) — `server/tests/unit/game/test_instance_manager.py`
- **Room** (5 connections)
- **Instance** (4 connections) — `server/game/instance_manager.py`
- **._get_template_rooms()** (4 connections) — `server/game/instance_manager.py`
- **._remap_exits()** (4 connections) — `server/game/instance_manager.py`
- **tutorial_room()** (4 connections) — `server/tests/unit/game/test_instance_manager.py`
- **.get_instance()** (3 connections) — `server/game/instance_manager.py`
- **.get_room_by_id()** (3 connections) — `server/game/instance_manager.py`
- **._stable_id_from_target()** (3 connections) — `server/game/instance_manager.py`
- **room_cache()** (3 connections) — `server/tests/unit/game/test_instance_manager.py`
- **fixture** (3 connections)
- **.destroy_instance()** (2 connections) — `server/game/instance_manager.py`
- **.get_exit_room_id()** (2 connections) — `server/game/instance_manager.py`
- **.get_first_room_id()** (2 connections) — `server/game/instance_manager.py`
- **test_create_instance()** (2 connections) — `server/tests/unit/game/test_instance_manager.py`
- **test_create_instance_raises_when_no_templates()** (2 connections) — `server/tests/unit/game/test_instance_manager.py`
- **test_destroy_instance()** (2 connections) — `server/tests/unit/game/test_instance_manager.py`
- **test_get_exit_room_id()** (2 connections) — `server/tests/unit/game/test_instance_manager.py`
- *... and 30 more nodes in this community*

## Relationships

- [event_types.py](event_types.py.md) (6 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (2 shared connections)
- [Room](Room.md) (2 shared connections)
- [ExplorationService](ExplorationService.md) (1 shared connections)
- [MovementService](MovementService.md) (1 shared connections)
- [PlayerPositionService](PlayerPositionService.md) (1 shared connections)
- [PartyService](PartyService.md) (1 shared connections)
- [.initialize](initialize.md) (1 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (1 shared connections)
- [Alias](Alias.md) (1 shared connections)
- [EventBus](EventBus.md) (1 shared connections)

## Source Files

- `server/container/bundles/game.py`
- `server/game/instance_manager.py`
- `server/tests/unit/game/test_instance_manager.py`

## Audit Trail

- EXTRACTED: 85 (94%)
- INFERRED: 5 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*