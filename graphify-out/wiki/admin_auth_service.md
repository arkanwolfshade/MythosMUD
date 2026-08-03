# admin auth service

> 258 nodes

## Key Concepts

- **test_admin_auth_service.py** (54 connections) — `server/tests/unit/services/test_admin_auth_service.py`
- **get_admin_auth_service()** (44 connections) — `server/services/admin_auth_service.py`
- **validate_admin_permission()** (37 connections) — `server/api/admin/npc_router_core.py`
- **npc_definitions_api.py** (29 connections) — `server/api/admin/npc_definitions_api.py`
- **dialogue_definitions_api.py** (27 connections) — `server/api/admin/dialogue_definitions_api.py`
- **npc_instances_api.py** (26 connections) — `server/api/admin/npc_instances_api.py`
- **npc_population_api.py** (22 connections) — `server/api/admin/npc_population_api.py`
- **npc_spawn_rules_api.py** (22 connections) — `server/api/admin/npc_spawn_rules_api.py`
- **npc_schemas.py** (21 connections) — `server/api/admin/npc_schemas.py`
- **npc_admin_mgmt_api.py** (20 connections) — `server/api/admin/npc_admin_mgmt_api.py`
- **admin_auth_service.py** (20 connections) — `server/services/admin_auth_service.py`
- **npc_router_core.py** (16 connections) — `server/api/admin/npc_router_core.py`
- **AdminAction** (16 connections) — `server/services/admin_auth_service.py`
- **npc_admin.py** (15 connections) — `server/schemas/admin/npc_admin.py`
- **AdminSession** (14 connections) — `server/schemas/admin/admin_data.py`
- **AuditLogEntry** (14 connections) — `server/schemas/admin/admin_data.py`
- **create_dialogue_definition()** (13 connections) — `server/api/admin/dialogue_definitions_api.py`
- **_update_npc_definition_internal()** (13 connections) — `server/api/admin/npc_definitions_api.py`
- **__init__.py** (13 connections) — `server/schemas/admin/__init__.py`
- **upsert_dialogue_definition()** (11 connections) — `server/api/admin/dialogue_definitions_api.py`
- **create_npc_definition()** (11 connections) — `server/api/admin/npc_definitions_api.py`
- **BaseModel** (11 connections)
- **create_npc_spawn_rule()** (11 connections) — `server/api/admin/npc_spawn_rules_api.py`
- **test_dialogue_definitions_api.py** (11 connections) — `server/tests/unit/api/test_dialogue_definitions_api.py`
- **_to_response()** (10 connections) — `server/api/admin/dialogue_definitions_api.py`
- *... and 233 more nodes in this community*

## Relationships

- [auth users rationale](auth_users_rationale.md) (44 shared connections)
- [Exception Containers](Exception_Containers.md) (30 shared connections)
- [Realtime Subscribers](Realtime_Subscribers.md) (20 shared connections)
- [NATS Messaging](NATS_Messaging.md) (17 shared connections)
- [services admin auth](services_admin_auth.md) (13 shared connections)
- [Player Stats](Player_Stats.md) (11 shared connections)
- [command inventory factories](command_inventory_factories.md) (7 shared connections)
- [dialogue definition persistence](dialogue_definition_persistence.md) (7 shared connections)
- [Database Access Layer](Database_Access_Layer.md) (7 shared connections)
- [dialogue service game](dialogue_service_game.md) (5 shared connections)
- [maps handle ascii](maps_handle_ascii.md) (5 shared connections)
- [respawn player handlers](respawn_player_handlers.md) (5 shared connections)

## Source Files

- `server/api/admin/__init__.py`
- `server/api/admin/dialogue_definitions_api.py`
- `server/api/admin/dialogue_schemas.py`
- `server/api/admin/npc.py`
- `server/api/admin/npc_admin_mgmt_api.py`
- `server/api/admin/npc_definitions_api.py`
- `server/api/admin/npc_instances_api.py`
- `server/api/admin/npc_population_api.py`
- `server/api/admin/npc_router_core.py`
- `server/api/admin/npc_schemas.py`
- `server/api/admin/npc_spawn_rules_api.py`
- `server/schemas/admin/__init__.py`
- `server/schemas/admin/admin_data.py`
- `server/schemas/admin/npc_admin.py`
- `server/services/admin_auth_service.py`
- `server/tests/unit/api/test_dialogue_definitions_api.py`
- `server/tests/unit/services/test_admin_auth_service.py`

## Audit Trail

- EXTRACTED: 1132 (96%)
- INFERRED: 45 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*