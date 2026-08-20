# InstanceManager

> 32 nodes

## Key Concepts

- **InstanceManager** (19 connections) — `server/game/instance_manager.py`
- **._init_movement_layer()** (11 connections) — `server/container/bundles/game.py`
- **.create_instance()** (7 connections) — `server/game/instance_manager.py`
- **._build_instance_rooms()** (6 connections) — `server/game/instance_manager.py`
- **.__init__()** (5 connections) — `server/game/instance_manager.py`
- **._stable_id_from_room()** (5 connections) — `server/game/instance_manager.py`
- **Room** (5 connections)
- **Instance** (4 connections) — `server/game/instance_manager.py`
- **._get_template_rooms()** (4 connections) — `server/game/instance_manager.py`
- **._remap_exits()** (4 connections) — `server/game/instance_manager.py`
- **.get_instance()** (3 connections) — `server/game/instance_manager.py`
- **.get_room_by_id()** (3 connections) — `server/game/instance_manager.py`
- **._stable_id_from_target()** (3 connections) — `server/game/instance_manager.py`
- **.destroy_instance()** (2 connections) — `server/game/instance_manager.py`
- **.get_exit_room_id()** (2 connections) — `server/game/instance_manager.py`
- **.get_first_room_id()** (2 connections) — `server/game/instance_manager.py`
- **UUID** (2 connections)
- **Wire exploration, movement, follow, and party services.** (1 connections) — `server/container/bundles/game.py`
- **Return template rooms matching instance_template_id.** (1 connections) — `server/game/instance_manager.py`
- **Clone template rooms into instance-scoped rooms with remapped exits.** (1 connections) — `server/game/instance_manager.py`
- **Extract stable_id from room - use room.id if it looks like a full path.** (1 connections) — `server/game/instance_manager.py`
- **Remap exit targets: same-instance rooms use instance IDs, outside exits use…** (1 connections) — `server/game/instance_manager.py`
- **Extract stable_id from a room ID (may be full path or short form).** (1 connections) — `server/game/instance_manager.py`
- **Return the instance if it exists.** (1 connections) — `server/game/instance_manager.py`
- **Remove the instance from the store.** (1 connections) — `server/game/instance_manager.py`
- *... and 7 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (4 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (3 shared connections)
- [bundles/game.py](bundles-game.py.md) (2 shared connections)
- [test_instance_manager.py](test_instance_manager.py.md) (2 shared connections)
- [ExplorationService](ExplorationService.md) (1 shared connections)
- [MovementService](MovementService.md) (1 shared connections)
- [PlayerPositionService](PlayerPositionService.md) (1 shared connections)
- [test_follow_service.py](test_follow_service.py.md) (1 shared connections)
- [PartyService](PartyService.md) (1 shared connections)
- [AliasStorage](AliasStorage.md) (1 shared connections)
- [EventBus](EventBus.md) (1 shared connections)

## Source Files

- `server/container/bundles/game.py`
- `server/game/instance_manager.py`

## Audit Trail

- EXTRACTED: 57 (95%)
- INFERRED: 3 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*