# get_admin_auth_service

> 112 nodes

## Key Concepts

- **get_admin_auth_service()** (44 connections) — `server/services/admin_auth_service.py`
- **validate_admin_permission()** (37 connections) — `server/api/admin/npc_router_core.py`
- **test_npc_definitions_api.py** (31 connections) — `server/tests/unit/api/test_npc_definitions_api.py`
- **npc_definitions_api.py** (30 connections) — `server/api/admin/npc_definitions_api.py`
- **npc_schemas.py** (23 connections) — `server/api/admin/npc_schemas.py`
- **_update_npc_definition_internal()** (16 connections) — `server/api/admin/npc_definitions_api.py`
- **test_npc_spawn_rules_api.py** (16 connections) — `server/tests/unit/api/test_npc_spawn_rules_api.py`
- **get_npc_definitions()** (15 connections) — `server/api/admin/npc_definitions_api.py`
- **create_npc_spawn_rule()** (15 connections) — `server/api/admin/npc_spawn_rules_api.py`
- **get_npc_spawn_rules()** (15 connections) — `server/api/admin/npc_spawn_rules_api.py`
- **create_npc_definition()** (14 connections) — `server/api/admin/npc_definitions_api.py`
- **get_npc_definition()** (14 connections) — `server/api/admin/npc_definitions_api.py`
- **get_admin_sessions()** (13 connections) — `server/api/admin/npc_admin_mgmt_api.py`
- **test_npc_admin_mgmt_api.py** (13 connections) — `server/tests/unit/api/admin/test_npc_admin_mgmt_api.py`
- **delete_npc_definition()** (12 connections) — `server/api/admin/npc_definitions_api.py`
- **delete_npc_spawn_rule()** (12 connections) — `server/api/admin/npc_spawn_rules_api.py`
- **_admin_user()** (12 connections) — `server/tests/unit/api/test_npc_definitions_api.py`
- **cleanup_admin_sessions()** (11 connections) — `server/api/admin/npc_admin_mgmt_api.py`
- **_run_coordinate_recalculation()** (11 connections) — `server/api/maps.py`
- **BaseModel** (11 connections)
- **NPCDefinitionResponse** (10 connections) — `server/api/admin/npc_schemas.py`
- **NPCDefinitionUpdate** (10 connections) — `server/api/admin/npc_schemas.py`
- **get_admin_audit_log()** (10 connections) — `server/api/admin/npc_admin_mgmt_api.py`
- **.from_orm()** (10 connections) — `server/api/admin/npc_schemas.py`
- **test_create_npc_definition()** (10 connections) — `server/tests/unit/api/test_npc_definitions_api.py`
- *... and 87 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (42 shared connections)
- [server/schemas/__init__.py](server-schemas-__init__.py.md) (21 shared connections)
- [User](User.md) (17 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (16 shared connections)
- [DialogueDefinitionRepository](DialogueDefinitionRepository.md) (11 shared connections)
- [get_npc_population_stats](get_npc_population_stats.md) (6 shared connections)
- [EventBus](EventBus.md) (4 shared connections)
- [test_maps.py](test_maps.py.md) (4 shared connections)
- [npc_database.py](npc_database.py.md) (3 shared connections)
- [NPCSpawnRule](NPCSpawnRule.md) (2 shared connections)
- [test_rooms_api.py](test_rooms_api.py.md) (2 shared connections)
- [get_npc_instance_service](get_npc_instance_service.md) (2 shared connections)

## Source Files

- `server/api/admin/npc_admin_mgmt_api.py`
- `server/api/admin/npc_definitions_api.py`
- `server/api/admin/npc_router_core.py`
- `server/api/admin/npc_schemas.py`
- `server/api/admin/npc_spawn_rules_api.py`
- `server/api/maps.py`
- `server/services/admin_auth_service.py`
- `server/tests/unit/api/admin/test_npc_admin_mgmt_api.py`
- `server/tests/unit/api/test_npc_definitions_api.py`
- `server/tests/unit/api/test_npc_spawn_rules_api.py`

## Audit Trail

- EXTRACTED: 404 (100%)
- INFERRED: 1 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*