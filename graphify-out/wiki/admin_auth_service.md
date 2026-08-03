# admin auth service

> 82 nodes

## Key Concepts

- **user.py** (63 connections) — `server/models/user.py`
- **users.py** (49 connections) — `server/auth/users.py`
- **get_admin_auth_service()** (44 connections) — `server/services/admin_auth_service.py`
- **validate_admin_permission()** (37 connections) — `server/api/admin/npc_router_core.py`
- **test_npc_definitions_api.py** (31 connections) — `server/tests/unit/api/test_npc_definitions_api.py`
- **npc_definitions_api.py** (30 connections) — `server/api/admin/npc_definitions_api.py`
- **dialogue_definitions_api.py** (27 connections) — `server/api/admin/dialogue_definitions_api.py`
- **npc_instances_api.py** (27 connections) — `server/api/admin/npc_instances_api.py`
- **admin_auth_service.py** (24 connections) — `server/services/admin_auth_service.py`
- **npc_population_api.py** (23 connections) — `server/api/admin/npc_population_api.py`
- **npc_schemas.py** (23 connections) — `server/api/admin/npc_schemas.py`
- **npc_spawn_rules_api.py** (23 connections) — `server/api/admin/npc_spawn_rules_api.py`
- **npc_admin_mgmt_api.py** (21 connections) — `server/api/admin/npc_admin_mgmt_api.py`
- **_update_npc_definition_internal()** (16 connections) — `server/api/admin/npc_definitions_api.py`
- **npc_router_core.py** (16 connections) — `server/api/admin/npc_router_core.py`
- **AdminAction** (16 connections) — `server/services/admin_auth_service.py`
- **get_npc_definitions()** (14 connections) — `server/api/admin/npc_definitions_api.py`
- **create_npc_definition()** (13 connections) — `server/api/admin/npc_definitions_api.py`
- **get_npc_definition()** (13 connections) — `server/api/admin/npc_definitions_api.py`
- **_admin_user()** (12 connections) — `server/tests/unit/api/test_npc_definitions_api.py`
- **delete_npc_definition()** (11 connections) — `server/api/admin/npc_definitions_api.py`
- **BaseModel** (11 connections)
- **NPCDefinitionUpdate** (10 connections) — `server/api/admin/npc_schemas.py`
- **NPCDefinitionResponse** (10 connections) — `server/api/admin/npc_schemas.py`
- **.from_orm()** (10 connections) — `server/api/admin/npc_schemas.py`
- *... and 57 more nodes in this community*

## Relationships

- [Exception Containers](Exception_Containers.md) (43 shared connections)
- [models npc rationale](models_npc_rationale.md) (31 shared connections)
- [map layout useMapLayout](map_layout_useMapLayout.md) (23 shared connections)
- [AppRouter main AppRouter()](AppRouter_main_AppRouter%28%29.md) (22 shared connections)
- [player preferences services](player_preferences_services.md) (20 shared connections)
- [room validator path](room_validator_path.md) (15 shared connections)
- [commands party examples](commands_party_examples.md) (13 shared connections)
- [command inventory factories](command_inventory_factories.md) (11 shared connections)
- [auth users rationale](auth_users_rationale.md) (11 shared connections)
- [level game curve](level_game_curve.md) (10 shared connections)
- [maps handle ascii](maps_handle_ascii.md) (8 shared connections)
- [player requests schemas](player_requests_schemas.md) (8 shared connections)

## Source Files

- `server/api/admin/__init__.py`
- `server/api/admin/dialogue_definitions_api.py`
- `server/api/admin/npc.py`
- `server/api/admin/npc_admin_mgmt_api.py`
- `server/api/admin/npc_definitions_api.py`
- `server/api/admin/npc_instances_api.py`
- `server/api/admin/npc_population_api.py`
- `server/api/admin/npc_router_core.py`
- `server/api/admin/npc_schemas.py`
- `server/api/admin/npc_spawn_rules_api.py`
- `server/auth/users.py`
- `server/models/user.py`
- `server/services/admin_auth_service.py`
- `server/tests/unit/api/test_npc_definitions_api.py`

## Audit Trail

- EXTRACTED: 725 (99%)
- INFERRED: 5 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*