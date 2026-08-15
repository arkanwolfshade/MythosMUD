# get_admin_auth_service

> 92 nodes

## Key Concepts

- **get_admin_auth_service()** (44 connections) — `server/services/admin_auth_service.py`
- **validate_admin_permission()** (37 connections) — `server/api/admin/npc_router_core.py`
- **dialogue_definitions_api.py** (27 connections) — `server/api/admin/dialogue_definitions_api.py`
- **test_dialogue_definitions_api.py** (26 connections) — `server/tests/unit/api/test_dialogue_definitions_api.py`
- **npc_admin_mgmt_api.py** (22 connections) — `server/api/admin/npc_admin_mgmt_api.py`
- **create_dialogue_definition()** (14 connections) — `server/api/admin/dialogue_definitions_api.py`
- **list_dialogue_definitions()** (14 connections) — `server/api/admin/dialogue_definitions_api.py`
- **upsert_dialogue_definition()** (14 connections) — `server/api/admin/dialogue_definitions_api.py`
- **get_npc_population_stats()** (14 connections) — `server/api/admin/npc_population_api.py`
- **get_dialogue_definition()** (13 connections) — `server/api/admin/dialogue_definitions_api.py`
- **get_admin_sessions()** (13 connections) — `server/api/admin/npc_admin_mgmt_api.py`
- **test_npc_admin_mgmt_api.py** (13 connections) — `server/tests/unit/api/admin/test_npc_admin_mgmt_api.py`
- **test_npc_population_api.py** (13 connections) — `server/tests/unit/api/admin/test_npc_population_api.py`
- **delete_dialogue_definition()** (12 connections) — `server/api/admin/dialogue_definitions_api.py`
- **get_npc_system_status()** (12 connections) — `server/api/admin/npc_population_api.py`
- **get_npc_zone_stats()** (12 connections) — `server/api/admin/npc_population_api.py`
- **cleanup_admin_sessions()** (11 connections) — `server/api/admin/npc_admin_mgmt_api.py`
- **to_response()** (10 connections) — `server/api/admin/dialogue_definitions_api.py`
- **get_admin_audit_log()** (10 connections) — `server/api/admin/npc_admin_mgmt_api.py`
- **DialogueDefinitionResponse** (9 connections) — `server/api/admin/dialogue_schemas.py`
- **dialogue_schemas.py** (8 connections) — `server/api/admin/dialogue_schemas.py`
- **asyncio** (8 connections)
- **DialogueDefinitionCreate** (7 connections) — `server/api/admin/dialogue_schemas.py`
- **DialogueDefinitionUpdate** (7 connections) — `server/api/admin/dialogue_schemas.py`
- **api/admin/__init__.py** (6 connections) — `server/api/admin/__init__.py`
- *... and 67 more nodes in this community*

## Relationships

- [npc_instances_api.py](npc_instances_api.py.md) (22 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (21 shared connections)
- [get_logger](get_logger.md) (20 shared connections)
- [User](User.md) (14 shared connections)
- [npc_definitions_api.py](npc_definitions_api.py.md) (12 shared connections)
- [test_admin_auth_service.py](test_admin_auth_service.py.md) (10 shared connections)
- [DatabaseError](DatabaseError.md) (8 shared connections)
- [DialogueDefinitionRepository](DialogueDefinitionRepository.md) (6 shared connections)
- [test_npc_spawn_rules_api.py](test_npc_spawn_rules_api.py.md) (6 shared connections)
- [maps.py](maps.py.md) (3 shared connections)
- [RoomService](RoomService.md) (3 shared connections)
- [talk_command.py](talk_command.py.md) (3 shared connections)

## Source Files

- `server/api/admin/__init__.py`
- `server/api/admin/dialogue_definitions_api.py`
- `server/api/admin/dialogue_schemas.py`
- `server/api/admin/npc_admin_mgmt_api.py`
- `server/api/admin/npc_population_api.py`
- `server/api/admin/npc_router_core.py`
- `server/services/admin_auth_service.py`
- `server/tests/unit/api/admin/test_npc_admin_mgmt_api.py`
- `server/tests/unit/api/admin/test_npc_population_api.py`
- `server/tests/unit/api/test_dialogue_definitions_api.py`

## Audit Trail

- EXTRACTED: 313 (95%)
- INFERRED: 16 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*