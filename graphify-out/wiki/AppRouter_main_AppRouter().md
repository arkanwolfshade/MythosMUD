# AppRouter main AppRouter()

> 56 nodes

## Key Concepts

- **get_npc_instance_service()** (79 connections) — `server/services/npc_instance_service.py`
- **npc_admin.py** (15 connections) — `server/schemas/admin/npc_admin.py`
- **AdminSession** (14 connections) — `server/schemas/admin/admin_data.py`
- **AuditLogEntry** (14 connections) — `server/schemas/admin/admin_data.py`
- **get_npc_population_stats()** (13 connections) — `server/api/admin/npc_population_api.py`
- **__init__.py** (13 connections) — `server/schemas/admin/__init__.py`
- **test_npc_population_api.py** (13 connections) — `server/tests/unit/api/admin/test_npc_population_api.py`
- **get_npc_zone_stats()** (11 connections) — `server/api/admin/npc_population_api.py`
- **get_npc_system_status()** (11 connections) — `server/api/admin/npc_population_api.py`
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
- **.get_npc_instance()** (4 connections) — `server/commands/combat_handler.py`
- **admin_data.py** (4 connections) — `server/schemas/admin/admin_data.py`
- **Request** (3 connections)
- **test_get_npc_population_stats_generic_error()** (3 connections) — `server/tests/unit/api/admin/test_npc_population_api.py`
- **test_get_npc_instance_service_not_initialized()** (3 connections) — `server/tests/unit/services/test_npc_instance_service.py`
- *... and 31 more nodes in this community*

## Relationships

- [admin auth service](admin_auth_service.md) (22 shared connections)
- [commands npc admin](commands_npc_admin.md) (13 shared connections)
- [profession game service](profession_game_service.md) (11 shared connections)
- [map layout useMapLayout](map_layout_useMapLayout.md) (9 shared connections)
- [Exception Containers](Exception_Containers.md) (8 shared connections)
- [Realtime Subscribers](Realtime_Subscribers.md) (6 shared connections)
- [models npc rationale](models_npc_rationale.md) (6 shared connections)
- [websocket helpers realtime](websocket_helpers_realtime.md) (5 shared connections)
- [look helpers commands](look_helpers_commands.md) (4 shared connections)
- [NPC Combat](NPC_Combat.md) (3 shared connections)
- [level game curve](level_game_curve.md) (3 shared connections)
- [services service hallucination](services_service_hallucination.md) (3 shared connections)

## Source Files

- `server/api/admin/npc_population_api.py`
- `server/commands/combat_handler.py`
- `server/schemas/admin/__init__.py`
- `server/schemas/admin/admin_data.py`
- `server/schemas/admin/npc_admin.py`
- `server/services/npc_instance_service.py`
- `server/tests/unit/api/admin/test_npc_population_api.py`
- `server/tests/unit/services/test_npc_instance_service.py`

## Audit Trail

- EXTRACTED: 297 (88%)
- INFERRED: 41 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*