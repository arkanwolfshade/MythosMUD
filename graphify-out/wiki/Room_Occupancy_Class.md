# Room Occupancy Class

> 151 nodes

## Key Concepts

- **get_admin_auth_service()** (39 connections) — `server/services/admin_auth_service.py`
- **validate_admin_permission()** (31 connections) — `server/api/admin/npc_router_core.py`
- **npc_definitions_api.py** (29 connections) — `server/api/admin/npc_definitions_api.py`
- **npc_instances_api.py** (26 connections) — `server/api/admin/npc_instances_api.py`
- **npc_population_api.py** (22 connections) — `server/api/admin/npc_population_api.py`
- **npc_spawn_rules_api.py** (22 connections) — `server/api/admin/npc_spawn_rules_api.py`
- **npc_schemas.py** (21 connections) — `server/api/admin/npc_schemas.py`
- **npc_admin_mgmt_api.py** (20 connections) — `server/api/admin/npc_admin_mgmt_api.py`
- **admin_auth_service.py** (19 connections) — `server/services/admin_auth_service.py`
- **npc_router_core.py** (15 connections) — `server/api/admin/npc_router_core.py`
- **npc_admin.py** (15 connections) — `server/schemas/admin/npc_admin.py`
- **AdminAction** (15 connections) — `server/services/admin_auth_service.py`
- **update_room_position()** (14 connections) — `server/api/rooms.py`
- **AdminSession** (14 connections) — `server/schemas/admin/admin_data.py`
- **AuditLogEntry** (14 connections) — `server/schemas/admin/admin_data.py`
- **_update_npc_definition_internal()** (13 connections) — `server/api/admin/npc_definitions_api.py`
- **__init__.py** (13 connections) — `server/schemas/admin/__init__.py`
- **create_npc_definition()** (11 connections) — `server/api/admin/npc_definitions_api.py`
- **BaseModel** (11 connections)
- **create_npc_spawn_rule()** (11 connections) — `server/api/admin/npc_spawn_rules_api.py`
- **NPCDefinitionUpdateParams** (11 connections) — `server/services/npc_service_models.py`
- **get_npc_definitions()** (10 connections) — `server/api/admin/npc_definitions_api.py`
- **get_npc_definition()** (10 connections) — `server/api/admin/npc_definitions_api.py`
- **spawn_npc_instance()** (10 connections) — `server/api/admin/npc_instances_api.py`
- **move_npc_instance()** (10 connections) — `server/api/admin/npc_instances_api.py`
- *... and 126 more nodes in this community*

## Relationships

- [Game Service Bundle](Game_Service_Bundle.md) (54 shared connections)
- [Aggressive Mob NPC](Aggressive_Mob_NPC.md) (30 shared connections)
- [Combat Command Handler](Combat_Command_Handler.md) (23 shared connections)
- [Level and XP Curve](Level_and_XP_Curve.md) (13 shared connections)
- [Dead Code Cleanup Plan](Dead_Code_Cleanup_Plan.md) (13 shared connections)
- [Command Parser Tests](Command_Parser_Tests.md) (9 shared connections)
- [Health Endpoint Spec](Health_Endpoint_Spec.md) (6 shared connections)
- [Player Name Validation](Player_Name_Validation.md) (3 shared connections)
- [Inventory Service Helpers](Inventory_Service_Helpers.md) (3 shared connections)
- [Player Model Inventory](Player_Model_Inventory.md) (3 shared connections)
- [Realtime Errors Error](Realtime_Errors_Error.md) (2 shared connections)
- [Postgres Adapter Infrastructure](Postgres_Adapter_Infrastructure.md) (1 shared connections)

## Source Files

- `server/api/admin/npc.py`
- `server/api/admin/npc_admin_mgmt_api.py`
- `server/api/admin/npc_definitions_api.py`
- `server/api/admin/npc_instances_api.py`
- `server/api/admin/npc_population_api.py`
- `server/api/admin/npc_router_core.py`
- `server/api/admin/npc_schemas.py`
- `server/api/admin/npc_spawn_rules_api.py`
- `server/api/rooms.py`
- `server/schemas/admin/__init__.py`
- `server/schemas/admin/admin_data.py`
- `server/schemas/admin/npc_admin.py`
- `server/services/admin_auth_service.py`
- `server/services/npc_service_models.py`

## Audit Trail

- EXTRACTED: 831 (95%)
- INFERRED: 42 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*