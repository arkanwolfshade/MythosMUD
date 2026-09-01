# get_admin_auth_service

> 160 nodes

## Key Concepts

- **get_admin_auth_service()** (54 connections) — `server/services/admin_auth_service.py`
- **validate_admin_permission()** (37 connections) — `server/api/admin/npc_router_core.py`
- **npc_instances_api.py** (29 connections) — `server/api/admin/npc_instances_api.py`
- **admin_auth_service.py** (27 connections) — `server/services/admin_auth_service.py`
- **npc_population_api.py** (25 connections) — `server/api/admin/npc_population_api.py`
- **npc_spawn_rules_api.py** (25 connections) — `server/api/admin/npc_spawn_rules_api.py`
- **npc_admin_mgmt_api.py** (23 connections) — `server/api/admin/npc_admin_mgmt_api.py`
- **test_npc_instances_api.py** (22 connections) — `server/tests/unit/api/test_npc_instances_api.py`
- **test_npc_spawn_rules_api.py** (18 connections) — `server/tests/unit/api/test_npc_spawn_rules_api.py`
- **npc_router_core.py** (17 connections) — `server/api/admin/npc_router_core.py`
- **schemas/admin/__init__.py** (16 connections) — `server/schemas/admin/__init__.py`
- **npc_admin.py** (16 connections) — `server/schemas/admin/npc_admin.py`
- **spawn_npc_instance()** (15 connections) — `server/api/admin/npc_instances_api.py`
- **create_npc_spawn_rule()** (15 connections) — `server/api/admin/npc_spawn_rules_api.py`
- **get_npc_spawn_rules()** (15 connections) — `server/api/admin/npc_spawn_rules_api.py`
- **test_npc_admin_mgmt_api.py** (15 connections) — `server/tests/unit/api/admin/test_npc_admin_mgmt_api.py`
- **test_npc_population_api.py** (15 connections) — `server/tests/unit/api/admin/test_npc_population_api.py`
- **get_npc_population_stats()** (14 connections) — `server/api/admin/npc_population_api.py`
- **get_admin_sessions()** (13 connections) — `server/api/admin/npc_admin_mgmt_api.py`
- **despawn_npc_instance()** (13 connections) — `server/api/admin/npc_instances_api.py`
- **move_npc_instance()** (13 connections) — `server/api/admin/npc_instances_api.py`
- **get_npc_instances()** (12 connections) — `server/api/admin/npc_instances_api.py`
- **get_npc_stats()** (12 connections) — `server/api/admin/npc_instances_api.py`
- **get_npc_system_status()** (12 connections) — `server/api/admin/npc_population_api.py`
- **get_npc_zone_stats()** (12 connections) — `server/api/admin/npc_population_api.py`
- *... and 135 more nodes in this community*

## Relationships

- [LoggedHTTPException](LoggedHTTPException.md) (34 shared connections)
- [User](User.md) (31 shared connections)
- [test_npc_definitions_api.py](test_npc_definitions_api.py.md) (27 shared connections)
- [get_logger](get_logger.md) (22 shared connections)
- [test_admin_auth_service.py](test_admin_auth_service.py.md) (15 shared connections)
- [dialogue_definitions_api.py](dialogue_definitions_api.py.md) (13 shared connections)
- [server/schemas/__init__.py](server-schemas-__init__.py.md) (11 shared connections)
- [get_npc_instance_service](get_npc_instance_service.md) (10 shared connections)
- [players/__init__.py](players-__init__.py.md) (8 shared connections)
- [pydantic.md](pydantic.md.md) (6 shared connections)
- [ExplorationService](ExplorationService.md) (4 shared connections)
- [pytest.md](pytest.md.md) (4 shared connections)

## Source Files

- `server/api/admin/npc.py`
- `server/api/admin/npc_admin_mgmt_api.py`
- `server/api/admin/npc_instances_api.py`
- `server/api/admin/npc_population_api.py`
- `server/api/admin/npc_router_core.py`
- `server/api/admin/npc_schemas.py`
- `server/api/admin/npc_spawn_rules_api.py`
- `server/schemas/admin/__init__.py`
- `server/schemas/admin/admin_data.py`
- `server/schemas/admin/npc_admin.py`
- `server/services/admin_auth_service.py`
- `server/tests/unit/api/admin/test_npc_admin_mgmt_api.py`
- `server/tests/unit/api/admin/test_npc_population_api.py`
- `server/tests/unit/api/test_npc_instances_api.py`
- `server/tests/unit/api/test_npc_spawn_rules_api.py`

## Audit Trail

- EXTRACTED: 522 (96%)
- INFERRED: 19 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*