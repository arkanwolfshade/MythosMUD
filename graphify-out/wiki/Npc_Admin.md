# Npc Admin

> 177 nodes

## Key Concepts

- **server/schemas/__init__.py** (70 connections) — `server/schemas/__init__.py`
- **get_admin_auth_service()** (53 connections) — `server/services/admin_auth_service.py`
- **validate_admin_permission()** (37 connections) — `server/api/admin/npc_router_core.py`
- **npc_instances_api.py** (29 connections) — `server/api/admin/npc_instances_api.py`
- **dialogue_definitions_api.py** (28 connections) — `server/api/admin/dialogue_definitions_api.py`
- **test_dialogue_definitions_api.py** (28 connections) — `server/tests/unit/api/test_dialogue_definitions_api.py`
- **admin_auth_service.py** (26 connections) — `server/services/admin_auth_service.py`
- **npc_population_api.py** (25 connections) — `server/api/admin/npc_population_api.py`
- **npc_spawn_rules_api.py** (25 connections) — `server/api/admin/npc_spawn_rules_api.py`
- **npc_admin_mgmt_api.py** (23 connections) — `server/api/admin/npc_admin_mgmt_api.py`
- **npc_router_core.py** (17 connections) — `server/api/admin/npc_router_core.py`
- **schemas/admin/__init__.py** (16 connections) — `server/schemas/admin/__init__.py`
- **npc_admin.py** (16 connections) — `server/schemas/admin/npc_admin.py`
- **test_npc_admin_mgmt_api.py** (15 connections) — `server/tests/unit/api/admin/test_npc_admin_mgmt_api.py`
- **test_npc_population_api.py** (15 connections) — `server/tests/unit/api/admin/test_npc_population_api.py`
- **create_dialogue_definition()** (14 connections) — `server/api/admin/dialogue_definitions_api.py`
- **list_dialogue_definitions()** (14 connections) — `server/api/admin/dialogue_definitions_api.py`
- **upsert_dialogue_definition()** (14 connections) — `server/api/admin/dialogue_definitions_api.py`
- **get_npc_population_stats()** (14 connections) — `server/api/admin/npc_population_api.py`
- **get_dialogue_definition()** (13 connections) — `server/api/admin/dialogue_definitions_api.py`
- **get_admin_sessions()** (13 connections) — `server/api/admin/npc_admin_mgmt_api.py`
- **delete_dialogue_definition()** (12 connections) — `server/api/admin/dialogue_definitions_api.py`
- **spawn_npc_instance()** (12 connections) — `server/api/admin/npc_instances_api.py`
- **get_npc_system_status()** (12 connections) — `server/api/admin/npc_population_api.py`
- **get_npc_zone_stats()** (12 connections) — `server/api/admin/npc_population_api.py`
- *... and 152 more nodes in this community*

## Relationships

- [NPC Definitions API](NPC_Definitions_API.md) (44 shared connections)
- [Container Exception Handling](Container_Exception_Handling.md) (41 shared connections)
- [Test Auth Dependencies](Test_Auth_Dependencies.md) (33 shared connections)
- [Test Admin Auth Service](Test_Admin_Auth_Service.md) (15 shared connections)
- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (14 shared connections)
- [Character Creation API](Character_Creation_API.md) (14 shared connections)
- [Test Npc Admin Commands](Test_Npc_Admin_Commands.md) (10 shared connections)
- [Test Player Requests](Test_Player_Requests.md) (8 shared connections)
- [Error Handling & Exceptions](Error_Handling_&_Exceptions.md) (8 shared connections)
- [Dialogue Definition Repository](Dialogue_Definition_Repository.md) (7 shared connections)
- [Test Player Schemas](Test_Player_Schemas.md) (7 shared connections)
- [Metrics](Metrics.md) (6 shared connections)

## Source Files

- `server/api/admin/__init__.py`
- `server/api/admin/dialogue_definitions_api.py`
- `server/api/admin/dialogue_schemas.py`
- `server/api/admin/npc.py`
- `server/api/admin/npc_admin_mgmt_api.py`
- `server/api/admin/npc_instances_api.py`
- `server/api/admin/npc_population_api.py`
- `server/api/admin/npc_router_core.py`
- `server/api/admin/npc_spawn_rules_api.py`
- `server/schemas/__init__.py`
- `server/schemas/admin/__init__.py`
- `server/schemas/admin/admin_data.py`
- `server/schemas/admin/npc_admin.py`
- `server/services/admin_auth_service.py`
- `server/tests/unit/api/admin/test_dialogue_schemas.py`
- `server/tests/unit/api/admin/test_npc_admin_mgmt_api.py`
- `server/tests/unit/api/admin/test_npc_population_api.py`
- `server/tests/unit/api/test_dialogue_definitions_api.py`

## Audit Trail

- EXTRACTED: 633 (97%)
- INFERRED: 22 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*