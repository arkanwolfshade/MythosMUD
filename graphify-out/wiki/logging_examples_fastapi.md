# logging examples fastapi

> 34 nodes

## Key Concepts

- **InstanceManager** (19 connections) — `server/game/instance_manager.py`
- **instance_manager.py** (12 connections) — `server/game/instance_manager.py`
- **.create_instance()** (7 connections) — `server/game/instance_manager.py`
- **._build_instance_rooms()** (6 connections) — `server/game/instance_manager.py`
- **.__init__()** (5 connections) — `server/game/instance_manager.py`
- **Room** (5 connections)
- **._stable_id_from_room()** (5 connections) — `server/game/instance_manager.py`
- **spawn_defaults.py** (4 connections) — `server/constants/spawn_defaults.py`
- **Instance** (4 connections) — `server/game/instance_manager.py`
- **._get_template_rooms()** (4 connections) — `server/game/instance_manager.py`
- **._remap_exits()** (4 connections) — `server/game/instance_manager.py`
- **._stable_id_from_target()** (3 connections) — `server/game/instance_manager.py`
- **.get_instance()** (3 connections) — `server/game/instance_manager.py`
- **.get_room_by_id()** (3 connections) — `server/game/instance_manager.py`
- **UUID** (2 connections)
- **.destroy_instance()** (2 connections) — `server/game/instance_manager.py`
- **.get_first_room_id()** (2 connections) — `server/game/instance_manager.py`
- **.get_exit_room_id()** (2 connections) — `server/game/instance_manager.py`
- **Shared spawn / respawn room identifiers used by gameplay and E2E seed scripts.** (1 connections) — `server/constants/spawn_defaults.py`
- **InstanceManager for MythosMUD.  Manages instanced rooms: creates, stores, and de** (1 connections) — `server/game/instance_manager.py`
- **An instanced set of rooms, unique per player or group.** (1 connections) — `server/game/instance_manager.py`
- **Manages instanced rooms: create from templates, destroy, and lookup.      Instan** (1 connections) — `server/game/instance_manager.py`
- **Initialize the instance manager.          Args:             room_cache: Shared r** (1 connections) — `server/game/instance_manager.py`
- **Create an instance from room templates with the given template_id.          Args** (1 connections) — `server/game/instance_manager.py`
- **Return template rooms matching instance_template_id.** (1 connections) — `server/game/instance_manager.py`
- *... and 9 more nodes in this community*

## Relationships

- [command inventory factories](command_inventory_factories.md) (4 shared connections)
- [uuid npc combat](uuid_npc_combat.md) (3 shared connections)
- [Error Conversion](Error_Conversion.md) (3 shared connections)
- [Realtime Subscribers](Realtime_Subscribers.md) (2 shared connections)
- [argon2 auth rationale](argon2_auth_rationale.md) (1 shared connections)
- [item models rationale](item_models_rationale.md) (1 shared connections)
- [room models instance](room_models_instance.md) (1 shared connections)
- [npc shopkeeper rationale](npc_shopkeeper_rationale.md) (1 shared connections)

## Source Files

- `server/constants/spawn_defaults.py`
- `server/game/instance_manager.py`

## Audit Trail

- EXTRACTED: 107 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*