# map layout useMapLayout

> 28 nodes

## Key Concepts

- **test_npc_instances_api.py** (21 connections) — `server/tests/unit/api/test_npc_instances_api.py`
- **spawn_npc_instance()** (13 connections) — `server/api/admin/npc_instances_api.py`
- **despawn_npc_instance()** (12 connections) — `server/api/admin/npc_instances_api.py`
- **move_npc_instance()** (12 connections) — `server/api/admin/npc_instances_api.py`
- **get_npc_instances()** (11 connections) — `server/api/admin/npc_instances_api.py`
- **get_npc_stats()** (11 connections) — `server/api/admin/npc_instances_api.py`
- **NPCSpawnRequest** (7 connections) — `server/api/admin/npc_schemas.py`
- **NPCMoveRequest** (7 connections) — `server/api/admin/npc_schemas.py`
- **Request** (5 connections)
- **Any** (5 connections)
- **test_spawn_npc_instance_not_found()** (4 connections) — `server/tests/unit/api/test_npc_instances_api.py`
- **test_spawn_npc_instance_success()** (3 connections) — `server/tests/unit/api/test_npc_instances_api.py`
- **test_move_npc_instance_success()** (3 connections) — `server/tests/unit/api/test_npc_instances_api.py`
- **test_get_npc_instances_server_error()** (3 connections) — `server/tests/unit/api/test_npc_instances_api.py`
- **test_despawn_npc_instance_not_found()** (3 connections) — `server/tests/unit/api/test_npc_instances_api.py`
- **test_get_npc_instances_success()** (2 connections) — `server/tests/unit/api/test_npc_instances_api.py`
- **test_despawn_npc_instance_success()** (2 connections) — `server/tests/unit/api/test_npc_instances_api.py`
- **test_get_npc_stats_success()** (2 connections) — `server/tests/unit/api/test_npc_instances_api.py`
- **NPCSpawnRequest** (1 connections)
- **Get all active NPC instances.** (1 connections) — `server/api/admin/npc_instances_api.py`
- **Spawn a new NPC instance.** (1 connections) — `server/api/admin/npc_instances_api.py`
- **Despawn an NPC instance.** (1 connections) — `server/api/admin/npc_instances_api.py`
- **Move an NPC instance to a different room.** (1 connections) — `server/api/admin/npc_instances_api.py`
- **Get stats for a specific NPC instance.** (1 connections) — `server/api/admin/npc_instances_api.py`
- **Model for NPC spawn requests.** (1 connections) — `server/api/admin/npc_schemas.py`
- *... and 3 more nodes in this community*

## Relationships

- [admin auth service](admin_auth_service.md) (23 shared connections)
- [Exception Containers](Exception_Containers.md) (9 shared connections)
- [AppRouter main AppRouter()](AppRouter_main_AppRouter%28%29.md) (9 shared connections)
- [command inventory factories](command_inventory_factories.md) (1 shared connections)

## Source Files

- `server/api/admin/npc_instances_api.py`
- `server/api/admin/npc_schemas.py`
- `server/tests/unit/api/test_npc_instances_api.py`

## Audit Trail

- EXTRACTED: 133 (98%)
- INFERRED: 3 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*