# NPC Definition Admin API

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

- [Cursor CLI Documentation](Cursor_CLI_Documentation.md) (20 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (20 shared connections)
- [Player Respawn Service](Player_Respawn_Service.md) (18 shared connections)
- [Argon2 Password Hashing](Argon2_Password_Hashing.md) (16 shared connections)
- [Container API Endpoints](Container_API_Endpoints.md) (14 shared connections)
- [Admin Auth Service Tests](Admin_Auth_Service_Tests.md) (13 shared connections)
- [Api Admin Npc](Api_Admin_Npc.md) (10 shared connections)
- [Players API Endpoints](Players_API_Endpoints.md) (4 shared connections)
- [ASCII Map API](ASCII_Map_API.md) (3 shared connections)
- [Room Exploration API](Room_Exploration_API.md) (3 shared connections)
- [Chat Message Filtering](Chat_Message_Filtering.md) (2 shared connections)
- [WebSocket Coverage Gaps](WebSocket_Coverage_Gaps.md) (1 shared connections)

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