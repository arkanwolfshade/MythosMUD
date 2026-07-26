# get_admin_auth_service

> 45 nodes · cohesion 0.09

## Key Concepts

- **get_admin_auth_service()** (39 connections) — `server/services/admin_auth_service.py`
- **validate_admin_permission()** (31 connections) — `server/api/admin/npc_router_core.py`
- **npc_instances_api.py** (26 connections) — `server/api/admin/npc_instances_api.py`
- **npc_population_api.py** (22 connections) — `server/api/admin/npc_population_api.py`
- **npc_admin_mgmt_api.py** (20 connections) — `server/api/admin/npc_admin_mgmt_api.py`
- **npc_router_core.py** (15 connections) — `server/api/admin/npc_router_core.py`
- **move_npc_instance()** (10 connections) — `server/api/admin/npc_instances_api.py`
- **spawn_npc_instance()** (10 connections) — `server/api/admin/npc_instances_api.py`
- **npc.py** (9 connections) — `server/api/admin/npc.py`
- **despawn_npc_instance()** (9 connections) — `server/api/admin/npc_instances_api.py`
- **get_npc_stats()** (9 connections) — `server/api/admin/npc_instances_api.py`
- **get_npc_population_stats()** (9 connections) — `server/api/admin/npc_population_api.py`
- **get_npc_system_status()** (9 connections) — `server/api/admin/npc_population_api.py`
- **get_npc_zone_stats()** (9 connections) — `server/api/admin/npc_population_api.py`
- **cleanup_admin_sessions()** (8 connections) — `server/api/admin/npc_admin_mgmt_api.py`
- **get_admin_sessions()** (8 connections) — `server/api/admin/npc_admin_mgmt_api.py`
- **get_npc_instances()** (8 connections) — `server/api/admin/npc_instances_api.py`
- **get_admin_audit_log()** (7 connections) — `server/api/admin/npc_admin_mgmt_api.py`
- **Any** (5 connections)
- **Request** (5 connections)
- **__init__.py** (4 connections) — `server/api/admin/__init__.py`
- **admin_auth_service()** (4 connections) — `server/tests/unit/services/test_admin_auth_service.py`
- **Request** (3 connections)
- **Request** (3 connections)
- **Admin API module for MythosMUD.  This module provides administrative API endpoin** (1 connections) — `server/api/admin/__init__.py`
- *... and 20 more nodes in this community*

## Relationships

- [npc_admin.py](npc_admin.py.md) (20 shared connections)
- [get_logger](get_logger.md) (20 shared connections)
- [npc_definitions_api.py](npc_definitions_api.py.md) (18 shared connections)
- [User](User.md) (16 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (14 shared connections)
- [admin_auth_service.py](admin_auth_service.py.md) (13 shared connections)
- [npc_spawn_rules_api.py](npc_spawn_rules_api.py.md) (10 shared connections)
- [exceptions.py](exceptions.py.md) (4 shared connections)
- [ExplorationService](ExplorationService.md) (3 shared connections)
- [rooms.py](rooms.py.md) (3 shared connections)
- [test_admin_auth_service.py](test_admin_auth_service.py.md) (2 shared connections)
- [subject_controller.py](subject_controller.py.md) (1 shared connections)

## Source Files

- `server/api/admin/__init__.py`
- `server/api/admin/npc.py`
- `server/api/admin/npc_admin_mgmt_api.py`
- `server/api/admin/npc_instances_api.py`
- `server/api/admin/npc_population_api.py`
- `server/api/admin/npc_router_core.py`
- `server/services/admin_auth_service.py`
- `server/tests/unit/services/test_admin_auth_service.py`

## Audit Trail

- EXTRACTED: 301 (99%)
- INFERRED: 2 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*