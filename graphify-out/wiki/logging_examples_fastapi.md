# logging examples fastapi

> 32 nodes

## Key Concepts

- **InstanceManager** (19 connections) — `server/game/instance_manager.py`
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
- **UUID** (2 connections)
- **.destroy_instance()** (2 connections) — `server/game/instance_manager.py`
- **.get_first_room_id()** (2 connections) — `server/game/instance_manager.py`
- **.get_exit_room_id()** (2 connections) — `server/game/instance_manager.py`
- **An instanced set of rooms, unique per player or group.** (1 connections) — `server/game/instance_manager.py`
- **Manages instanced rooms: create from templates, destroy, and lookup.      Instan** (1 connections) — `server/game/instance_manager.py`
- **Initialize the instance manager.          Args:             room_cache: Shared r** (1 connections) — `server/game/instance_manager.py`
- **Create an instance from room templates with the given template_id.          Args** (1 connections) — `server/game/instance_manager.py`
- **Return template rooms matching instance_template_id.** (1 connections) — `server/game/instance_manager.py`
- **Clone template rooms into instance-scoped rooms with remapped exits.** (1 connections) — `server/game/instance_manager.py`
- **Extract stable_id from room - use room.id if it looks like a full path.** (1 connections) — `server/game/instance_manager.py`
- **Remap exit targets: same-instance rooms use instance IDs, outside exits use fixe** (1 connections) — `server/game/instance_manager.py`
- *... and 7 more nodes in this community*

## Relationships

- [Realtime Subscribers](Realtime_Subscribers.md) (6 shared connections)
- [websocket realtime handler](websocket_realtime_handler.md) (1 shared connections)
- [nats services service](nats_services_service.md) (1 shared connections)
- [time service rationale](time_service_rationale.md) (1 shared connections)
- [Loot Generation](Loot_Generation.md) (1 shared connections)
- [player presence tracker](player_presence_tracker.md) (1 shared connections)

## Source Files

- `server/game/instance_manager.py`
- `server/tests/unit/game/test_instance_manager.py`

## Audit Trail

- EXTRACTED: 93 (98%)
- INFERRED: 2 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*