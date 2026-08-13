# move_npc_instance

> 17 nodes

## Key Concepts

- **move_npc_instance()** (11 connections) — `server/api/admin/npc_instances_api.py`
- **spawn_npc_instance()** (11 connections) — `server/api/admin/npc_instances_api.py`
- **despawn_npc_instance()** (10 connections) — `server/api/admin/npc_instances_api.py`
- **get_npc_stats()** (10 connections) — `server/api/admin/npc_instances_api.py`
- **get_npc_instances()** (9 connections) — `server/api/admin/npc_instances_api.py`
- **Any** (5 connections)
- **Request** (5 connections)
- **get** (2 connections)
- **delete** (1 connections)
- **NPCSpawnRequest** (1 connections)
- **post** (1 connections)
- **put** (1 connections)
- **Despawn an NPC instance.** (1 connections) — `server/api/admin/npc_instances_api.py`
- **Move an NPC instance to a different room.** (1 connections) — `server/api/admin/npc_instances_api.py`
- **Get stats for a specific NPC instance.** (1 connections) — `server/api/admin/npc_instances_api.py`
- **Get all active NPC instances.** (1 connections) — `server/api/admin/npc_instances_api.py`
- **Spawn a new NPC instance.** (1 connections) — `server/api/admin/npc_instances_api.py`

## Relationships

- [get_admin_auth_service](get_admin_auth_service.md) (16 shared connections)
- [EventBus](EventBus.md) (5 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (5 shared connections)
- [npc_admin.py](npc_admin.py.md) (4 shared connections)

## Source Files

- `server/api/admin/npc_instances_api.py`

## Audit Trail

- EXTRACTED: 51 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*