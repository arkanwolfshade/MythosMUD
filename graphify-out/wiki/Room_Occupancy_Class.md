# Room Occupancy Class

> 192 nodes

## Key Concepts

- **__init__.py** (70 connections) — `server/schemas/__init__.py`
- **get_admin_auth_service()** (39 connections) — `server/services/admin_auth_service.py`
- **rooms.py** (35 connections) — `server/api/rooms.py`
- **validate_admin_permission()** (31 connections) — `server/api/admin/npc_router_core.py`
- **npc_definitions_api.py** (29 connections) — `server/api/admin/npc_definitions_api.py`
- **npc_instances_api.py** (26 connections) — `server/api/admin/npc_instances_api.py`
- **npc_population_api.py** (22 connections) — `server/api/admin/npc_population_api.py`
- **npc_spawn_rules_api.py** (22 connections) — `server/api/admin/npc_spawn_rules_api.py`
- **npc_schemas.py** (21 connections) — `server/api/admin/npc_schemas.py`
- **room_service.py** (21 connections) — `server/game/room_service.py`
- **npc_admin_mgmt_api.py** (20 connections) — `server/api/admin/npc_admin_mgmt_api.py`
- **admin_auth_service.py** (19 connections) — `server/services/admin_auth_service.py`
- **exploration_service.py** (16 connections) — `server/services/exploration_service.py`
- **npc_router_core.py** (15 connections) — `server/api/admin/npc_router_core.py`
- **npc_admin.py** (15 connections) — `server/schemas/admin/npc_admin.py`
- **AdminAction** (15 connections) — `server/services/admin_auth_service.py`
- **update_room_position()** (14 connections) — `server/api/rooms.py`
- **AdminSession** (14 connections) — `server/schemas/admin/admin_data.py`
- **AuditLogEntry** (14 connections) — `server/schemas/admin/admin_data.py`
- **_update_npc_definition_internal()** (13 connections) — `server/api/admin/npc_definitions_api.py`
- **_apply_exploration_filter_if_needed()** (13 connections) — `server/api/rooms.py`
- **__init__.py** (13 connections) — `server/schemas/admin/__init__.py`
- **test_rooms_exploration_filter.py** (12 connections) — `server/tests/unit/api/test_rooms_exploration_filter.py`
- **create_npc_definition()** (11 connections) — `server/api/admin/npc_definitions_api.py`
- **BaseModel** (11 connections)
- *... and 167 more nodes in this community*

## Relationships

- [Aggressive Mob NPC](Aggressive_Mob_NPC.md) (30 shared connections)
- [NPC Combat Lifecycle](NPC_Combat_Lifecycle.md) (27 shared connections)
- [Client Event Store](Client_Event_Store.md) (25 shared connections)
- [Communication Command Flows](Communication_Command_Flows.md) (16 shared connections)
- [Combat Command Handler](Combat_Command_Handler.md) (15 shared connections)
- [Minimap Fallback Helpers](Minimap_Fallback_Helpers.md) (15 shared connections)
- [Container Persistence Ops](Container_Persistence_Ops.md) (14 shared connections)
- [Inventory Service Helpers](Inventory_Service_Helpers.md) (13 shared connections)
- [Player Model Inventory](Player_Model_Inventory.md) (12 shared connections)
- [Schemas Maps Map](Schemas_Maps_Map.md) (8 shared connections)
- [Combat Flee Command](Combat_Flee_Command.md) (6 shared connections)
- [NATS Metrics API](NATS_Metrics_API.md) (6 shared connections)

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
- `server/game/room_service.py`
- `server/schemas/__init__.py`
- `server/schemas/admin/__init__.py`
- `server/schemas/admin/admin_data.py`
- `server/schemas/admin/npc_admin.py`
- `server/schemas/rooms/__init__.py`
- `server/schemas/rooms/room.py`
- `server/schemas/rooms/room_data.py`
- `server/services/admin_auth_service.py`
- `server/services/exploration_service.py`
- `server/tests/unit/api/test_rooms_exploration_filter.py`

## Audit Trail

- EXTRACTED: 1088 (95%)
- INFERRED: 56 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*