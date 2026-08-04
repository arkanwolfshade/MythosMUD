# logging setup structured

> 71 nodes

## Key Concepts

- **get_npc_instance_service()** (79 connections) — `server/services/npc_instance_service.py`
- **npc_instances_api.py** (27 connections) — `server/api/admin/npc_instances_api.py`
- **test_npc_instances_api.py** (21 connections) — `server/tests/unit/api/test_npc_instances_api.py`
- **npc_admin.py** (15 connections) — `server/schemas/admin/npc_admin.py`
- **AdminSession** (14 connections) — `server/schemas/admin/admin_data.py`
- **AuditLogEntry** (14 connections) — `server/schemas/admin/admin_data.py`
- **spawn_npc_instance()** (13 connections) — `server/api/admin/npc_instances_api.py`
- **__init__.py** (13 connections) — `server/schemas/admin/__init__.py`
- **despawn_npc_instance()** (12 connections) — `server/api/admin/npc_instances_api.py`
- **move_npc_instance()** (12 connections) — `server/api/admin/npc_instances_api.py`
- **get_npc_instances()** (11 connections) — `server/api/admin/npc_instances_api.py`
- **get_npc_stats()** (11 connections) — `server/api/admin/npc_instances_api.py`
- **BaseModel** (10 connections)
- **NPCSpawnResponse** (9 connections) — `server/schemas/admin/npc_admin.py`
- **NPCDespawnResponse** (9 connections) — `server/schemas/admin/npc_admin.py`
- **NPCMoveResponse** (9 connections) — `server/schemas/admin/npc_admin.py`
- **NPCStatsResponse** (9 connections) — `server/schemas/admin/npc_admin.py`
- **NPCPopulationStatsResponse** (9 connections) — `server/schemas/admin/npc_admin.py`
- **NPCZoneStatsResponse** (9 connections) — `server/schemas/admin/npc_admin.py`
- **NPCSystemStatusResponse** (9 connections) — `server/schemas/admin/npc_admin.py`
- **AdminSessionsResponse** (9 connections) — `server/schemas/admin/npc_admin.py`
- **AdminAuditLogResponse** (9 connections) — `server/schemas/admin/npc_admin.py`
- **AdminCleanupSessionsResponse** (9 connections) — `server/schemas/admin/npc_admin.py`
- **NPCSpawnRequest** (7 connections) — `server/api/admin/npc_schemas.py`
- **NPCMoveRequest** (7 connections) — `server/api/admin/npc_schemas.py`
- *... and 46 more nodes in this community*

## Relationships

- [player preferences services](player_preferences_services.md) (26 shared connections)
- [commands npc admin](commands_npc_admin.md) (13 shared connections)
- [Exception Containers](Exception_Containers.md) (11 shared connections)
- [Player Stats](Player_Stats.md) (11 shared connections)
- [Realtime Subscribers](Realtime_Subscribers.md) (10 shared connections)
- [persistence container rationale](persistence_container_rationale.md) (6 shared connections)
- [NPC Combat](NPC_Combat.md) (6 shared connections)
- [countdown rest task](countdown_rest_task.md) (6 shared connections)
- [npc look commands](npc_look_commands.md) (4 shared connections)
- [command models moderation](command_models_moderation.md) (4 shared connections)
- [npc event handlers](npc_event_handlers.md) (3 shared connections)
- [event bus events](event_bus_events.md) (3 shared connections)

## Source Files

- `server/api/admin/npc_instances_api.py`
- `server/api/admin/npc_schemas.py`
- `server/commands/combat_handler.py`
- `server/schemas/admin/__init__.py`
- `server/schemas/admin/admin_data.py`
- `server/schemas/admin/npc_admin.py`
- `server/services/npc_instance_service.py`
- `server/tests/unit/api/test_npc_instances_api.py`
- `server/tests/unit/services/test_npc_instance_service.py`

## Audit Trail

- EXTRACTED: 392 (90%)
- INFERRED: 43 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*