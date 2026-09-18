# Admin NPC Management API

> 214 nodes

## Key Concepts

- **get_admin_auth_service()** (54 connections) — `server/services/admin_auth_service.py`
- **validate_admin_permission()** (37 connections) — `server/api/admin/npc_router_core.py`
- **test_npc_definitions_api.py** (35 connections) — `server/tests/unit/api/test_npc_definitions_api.py`
- **npc_definitions_api.py** (31 connections) — `server/api/admin/npc_definitions_api.py`
- **npc_instances_api.py** (28 connections) — `server/api/admin/npc_instances_api.py`
- **npc_population_api.py** (24 connections) — `server/api/admin/npc_population_api.py`
- **npc_spawn_rules_api.py** (24 connections) — `server/api/admin/npc_spawn_rules_api.py`
- **test_npc_instances_api.py** (24 connections) — `server/tests/unit/api/test_npc_instances_api.py`
- **npc_admin_mgmt_api.py** (22 connections) — `server/api/admin/npc_admin_mgmt_api.py`
- **npc_schemas.py** (22 connections) — `server/api/admin/npc_schemas.py`
- **npc_service/__init__.py** (22 connections) — `server/services/npc_service/__init__.py`
- **test_npc_spawn_rules_api.py** (21 connections) — `server/tests/unit/api/test_npc_spawn_rules_api.py`
- **_update_npc_definition_internal()** (16 connections) — `server/api/admin/npc_definitions_api.py`
- **npc_router_core.py** (16 connections) — `server/api/admin/npc_router_core.py`
- **schemas/admin/__init__.py** (16 connections) — `server/schemas/admin/__init__.py`
- **get_npc_definitions()** (15 connections) — `server/api/admin/npc_definitions_api.py`
- **spawn_npc_instance()** (15 connections) — `server/api/admin/npc_instances_api.py`
- **create_npc_spawn_rule()** (15 connections) — `server/api/admin/npc_spawn_rules_api.py`
- **get_npc_spawn_rules()** (15 connections) — `server/api/admin/npc_spawn_rules_api.py`
- **npc_admin.py** (15 connections) — `server/schemas/admin/npc_admin.py`
- **create_npc_definition()** (14 connections) — `server/api/admin/npc_definitions_api.py`
- **get_npc_definition()** (14 connections) — `server/api/admin/npc_definitions_api.py`
- **get_npc_population_stats()** (14 connections) — `server/api/admin/npc_population_api.py`
- **get_admin_sessions()** (13 connections) — `server/api/admin/npc_admin_mgmt_api.py`
- **despawn_npc_instance()** (13 connections) — `server/api/admin/npc_instances_api.py`
- *... and 189 more nodes in this community*

## Relationships

- [User Manager & Character Info](User_Manager_&_Character_Info.md) (41 shared connections)
- [Character Creation & Auth Dependencies](Character_Creation_&_Auth_Dependencies.md) (34 shared connections)
- [Aliases & Webhook/Schema Validation](Aliases_&_Webhook-Schema_Validation.md) (30 shared connections)
- [Community 45](Community_45.md) (18 shared connections)
- [DI Containers & API Bootstrap](DI_Containers_&_API_Bootstrap.md) (14 shared connections)
- [Player Effects (Corruption/Fear/Lucidity)](Player_Effects_Corruption-Fear-Lucidity.md) (14 shared connections)
- [Community 33](Community_33.md) (13 shared connections)
- [Community 100](Community_100.md) (13 shared connections)
- [NPC Population Control](NPC_Population_Control.md) (9 shared connections)
- [Community 304](Community_304.md) (5 shared connections)
- [Community 79](Community_79.md) (3 shared connections)
- [Community 422](Community_422.md) (3 shared connections)

## Source Files

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
- `server/services/npc_service/__init__.py`
- `server/tests/unit/api/admin/test_npc_admin_mgmt_api.py`
- `server/tests/unit/api/admin/test_npc_population_api.py`
- `server/tests/unit/api/test_npc_definitions_api.py`
- `server/tests/unit/api/test_npc_instances_api.py`
- `server/tests/unit/api/test_npc_spawn_rules_api.py`

## Audit Trail

- EXTRACTED: 689 (95%)
- INFERRED: 40 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*