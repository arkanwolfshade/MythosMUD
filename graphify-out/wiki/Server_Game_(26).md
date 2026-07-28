# Server Game (26)

> 36 nodes

## Key Concepts

- **InstanceManager** (19 connections) — `server/game/instance_manager.py`
- **instance_manager.py** (7 connections) — `server/game/instance_manager.py`
- **.create_instance()** (7 connections) — `server/game/instance_manager.py`
- **._build_instance_rooms()** (6 connections) — `server/game/instance_manager.py`
- **spawn_defaults.py** (4 connections) — `server/constants/spawn_defaults.py`
- **Instance** (4 connections) — `server/game/instance_manager.py`
- **._stable_id_from_room()** (4 connections) — `server/game/instance_manager.py`
- **._remap_exits()** (4 connections) — `server/game/instance_manager.py`
- **instance_manager()** (4 connections) — `server/tests/unit/game/test_instance_manager.py`
- **.__init__()** (3 connections) — `server/game/instance_manager.py`
- **._get_template_rooms()** (3 connections) — `server/game/instance_manager.py`
- **._stable_id_from_target()** (3 connections) — `server/game/instance_manager.py`
- **.get_instance()** (3 connections) — `server/game/instance_manager.py`
- **UUID** (2 connections)
- **.destroy_instance()** (2 connections) — `server/game/instance_manager.py`
- **.get_first_room_id()** (2 connections) — `server/game/instance_manager.py`
- **.get_exit_room_id()** (2 connections) — `server/game/instance_manager.py`
- **.get_room_by_id()** (2 connections) — `server/game/instance_manager.py`
- **Shared spawn / respawn room identifiers used by gameplay and E2E seed scripts.** (1 connections) — `server/constants/spawn_defaults.py`
- **EventBus** (1 connections)
- **InstanceManager for MythosMUD.  Manages instanced rooms: creates, stores, and de** (1 connections) — `server/game/instance_manager.py`
- **An instanced set of rooms, unique per player or group.** (1 connections) — `server/game/instance_manager.py`
- **Manages instanced rooms: create from templates, destroy, and lookup.      Instan** (1 connections) — `server/game/instance_manager.py`
- **Initialize the instance manager.          Args:             room_cache: Shared r** (1 connections) — `server/game/instance_manager.py`
- **Create an instance from room templates with the given template_id.          Args** (1 connections) — `server/game/instance_manager.py`
- *... and 11 more nodes in this community*

## Relationships

- [Server Game (31)](Server_Game_%2831%29.md) (3 shared connections)
- [Server Container](Server_Container.md) (3 shared connections)
- [Scripts (51)](Scripts_%2851%29.md) (1 shared connections)
- [Server Services](Server_Services.md) (1 shared connections)
- [Server Npc (6)](Server_Npc_%286%29.md) (1 shared connections)
- [Client Components (2)](Client_Components_%282%29.md) (1 shared connections)
- [Server Realtime (3)](Server_Realtime_%283%29.md) (1 shared connections)

## Source Files

- `server/constants/spawn_defaults.py`
- `server/game/instance_manager.py`
- `server/tests/unit/game/test_instance_manager.py`

## Audit Trail

- EXTRACTED: 97 (98%)
- INFERRED: 2 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*