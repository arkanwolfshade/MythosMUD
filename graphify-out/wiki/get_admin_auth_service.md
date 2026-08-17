# get_admin_auth_service

> 164 nodes

## Key Concepts

- **get_admin_auth_service()** (44 connections) — `server/services/admin_auth_service.py`
- **validate_admin_permission()** (37 connections) — `server/api/admin/npc_router_core.py`
- **test_npc_definitions_api.py** (33 connections) — `server/tests/unit/api/test_npc_definitions_api.py`
- **npc_definitions_api.py** (32 connections) — `server/api/admin/npc_definitions_api.py`
- **npc_schemas.py** (25 connections) — `server/api/admin/npc_schemas.py`
- **test_npc_instances_api.py** (22 connections) — `server/tests/unit/api/test_npc_instances_api.py`
- **test_npc_spawn_rules_api.py** (18 connections) — `server/tests/unit/api/test_npc_spawn_rules_api.py`
- **_update_npc_definition_internal()** (16 connections) — `server/api/admin/npc_definitions_api.py`
- **get_npc_definitions()** (15 connections) — `server/api/admin/npc_definitions_api.py`
- **spawn_npc_instance()** (15 connections) — `server/api/admin/npc_instances_api.py`
- **create_npc_spawn_rule()** (15 connections) — `server/api/admin/npc_spawn_rules_api.py`
- **get_npc_spawn_rules()** (15 connections) — `server/api/admin/npc_spawn_rules_api.py`
- **test_npc_admin_mgmt_api.py** (15 connections) — `server/tests/unit/api/admin/test_npc_admin_mgmt_api.py`
- **test_npc_population_api.py** (15 connections) — `server/tests/unit/api/admin/test_npc_population_api.py`
- **create_npc_definition()** (14 connections) — `server/api/admin/npc_definitions_api.py`
- **get_npc_definition()** (14 connections) — `server/api/admin/npc_definitions_api.py`
- **get_npc_population_stats()** (14 connections) — `server/api/admin/npc_population_api.py`
- **get_admin_sessions()** (13 connections) — `server/api/admin/npc_admin_mgmt_api.py`
- **despawn_npc_instance()** (13 connections) — `server/api/admin/npc_instances_api.py`
- **move_npc_instance()** (13 connections) — `server/api/admin/npc_instances_api.py`
- **delete_npc_definition()** (12 connections) — `server/api/admin/npc_definitions_api.py`
- **get_npc_instances()** (12 connections) — `server/api/admin/npc_instances_api.py`
- **get_npc_stats()** (12 connections) — `server/api/admin/npc_instances_api.py`
- **get_npc_system_status()** (12 connections) — `server/api/admin/npc_population_api.py`
- **get_npc_zone_stats()** (12 connections) — `server/api/admin/npc_population_api.py`
- *... and 139 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (67 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (37 shared connections)
- [User](User.md) (19 shared connections)
- [get_npc_instance_service](get_npc_instance_service.md) (12 shared connections)
- [dialogue_definitions_api.py](dialogue_definitions_api.py.md) (11 shared connections)
- [schemas/admin/__init__.py](schemas-admin-__init__.py.md) (10 shared connections)
- [NPCDefinition](NPCDefinition.md) (6 shared connections)
- [pytest.md](pytest.md.md) (5 shared connections)
- [test_admin_auth_service.py](test_admin_auth_service.py.md) (4 shared connections)
- [npc_database.py](npc_database.py.md) (3 shared connections)
- [NPCDefinitionCRUDMixin](NPCDefinitionCRUDMixin.md) (2 shared connections)
- [_run_set_map_origin](_run_set_map_origin.md) (2 shared connections)

## Source Files

- `server/api/admin/npc_admin_mgmt_api.py`
- `server/api/admin/npc_definitions_api.py`
- `server/api/admin/npc_instances_api.py`
- `server/api/admin/npc_population_api.py`
- `server/api/admin/npc_router_core.py`
- `server/api/admin/npc_schemas.py`
- `server/api/admin/npc_spawn_rules_api.py`
- `server/services/admin_auth_service.py`
- `server/services/npc_service_models.py`
- `server/tests/unit/api/admin/test_npc_admin_mgmt_api.py`
- `server/tests/unit/api/admin/test_npc_population_api.py`
- `server/tests/unit/api/test_npc_definitions_api.py`
- `server/tests/unit/api/test_npc_instances_api.py`
- `server/tests/unit/api/test_npc_spawn_rules_api.py`

## Audit Trail

- EXTRACTED: 527 (94%)
- INFERRED: 36 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*