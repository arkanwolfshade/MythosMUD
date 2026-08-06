# persistence container rationale

> 351 nodes

## Key Concepts

- **__init__.py** (70 connections) — `server/schemas/__init__.py`
- **user.py** (63 connections) — `server/models/user.py`
- **maps.py** (53 connections) — `server/api/maps.py`
- **get_admin_auth_service()** (44 connections) — `server/services/admin_auth_service.py`
- **validate_admin_permission()** (37 connections) — `server/api/admin/npc_router_core.py`
- **rooms.py** (36 connections) — `server/api/rooms.py`
- **test_npc_definitions_api.py** (31 connections) — `server/tests/unit/api/test_npc_definitions_api.py`
- **npc_definitions_api.py** (30 connections) — `server/api/admin/npc_definitions_api.py`
- **npc_instances_api.py** (27 connections) — `server/api/admin/npc_instances_api.py`
- **game.py** (25 connections) — `server/api/game.py`
- **admin_auth_service.py** (24 connections) — `server/services/admin_auth_service.py`
- **test_auth_dependencies.py** (24 connections) — `server/tests/unit/auth/test_auth_dependencies.py`
- **npc_population_api.py** (23 connections) — `server/api/admin/npc_population_api.py`
- **npc_schemas.py** (23 connections) — `server/api/admin/npc_schemas.py`
- **npc_spawn_rules_api.py** (23 connections) — `server/api/admin/npc_spawn_rules_api.py`
- **npc_admin_mgmt_api.py** (21 connections) — `server/api/admin/npc_admin_mgmt_api.py`
- **test_npc_instances_api.py** (21 connections) — `server/tests/unit/api/test_npc_instances_api.py`
- **test_game.py** (20 connections) — `server/tests/unit/api/test_game.py`
- **dependencies.py** (18 connections) — `server/auth/dependencies.py`
- **_update_npc_definition_internal()** (16 connections) — `server/api/admin/npc_definitions_api.py`
- **npc_router_core.py** (16 connections) — `server/api/admin/npc_router_core.py`
- **AdminAction** (16 connections) — `server/services/admin_auth_service.py`
- **test_npc_spawn_rules_api.py** (16 connections) — `server/tests/unit/api/test_npc_spawn_rules_api.py`
- **npc_admin.py** (15 connections) — `server/schemas/admin/npc_admin.py`
- **MythosTimeResponse** (15 connections) — `server/schemas/game/game.py`
- *... and 326 more nodes in this community*

## Relationships

- [player requests schemas](player_requests_schemas.md) (69 shared connections)
- [services inventory mutation](services_inventory_mutation.md) (62 shared connections)
- [commands shutdown process](commands_shutdown_process.md) (32 shared connections)
- [Error Conversion](Error_Conversion.md) (32 shared connections)
- [maps handle ascii](maps_handle_ascii.md) (22 shared connections)
- [inventory schemas schema](inventory_schemas_schema.md) (17 shared connections)
- [player preferences services](player_preferences_services.md) (16 shared connections)
- [auth users rationale](auth_users_rationale.md) (13 shared connections)
- [room game service](room_game_service.md) (13 shared connections)
- [Exception Containers](Exception_Containers.md) (12 shared connections)
- [commands npc admin](commands_npc_admin.md) (12 shared connections)
- [player service game](player_service_game.md) (12 shared connections)

## Source Files

- `server/api/__init__.py`
- `server/api/admin/__init__.py`
- `server/api/admin/npc.py`
- `server/api/admin/npc_admin_mgmt_api.py`
- `server/api/admin/npc_definitions_api.py`
- `server/api/admin/npc_instances_api.py`
- `server/api/admin/npc_population_api.py`
- `server/api/admin/npc_router_core.py`
- `server/api/admin/npc_schemas.py`
- `server/api/admin/npc_spawn_rules_api.py`
- `server/api/base.py`
- `server/api/game.py`
- `server/api/maps.py`
- `server/api/rooms.py`
- `server/auth/dependencies.py`
- `server/models/user.py`
- `server/schemas/__init__.py`
- `server/schemas/admin/__init__.py`
- `server/schemas/admin/admin_data.py`
- `server/schemas/admin/npc_admin.py`

## Audit Trail

- EXTRACTED: 1852 (95%)
- INFERRED: 91 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*