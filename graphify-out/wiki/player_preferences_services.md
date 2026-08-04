# player preferences services

> 71 nodes

## Key Concepts

- **get_admin_auth_service()** (44 connections) — `server/services/admin_auth_service.py`
- **validate_admin_permission()** (37 connections) — `server/api/admin/npc_router_core.py`
- **dialogue_definitions_api.py** (27 connections) — `server/api/admin/dialogue_definitions_api.py`
- **test_dialogue_definitions_api.py** (26 connections) — `server/tests/unit/api/test_dialogue_definitions_api.py`
- **admin_auth_service.py** (24 connections) — `server/services/admin_auth_service.py`
- **npc_population_api.py** (23 connections) — `server/api/admin/npc_population_api.py`
- **npc_admin_mgmt_api.py** (21 connections) — `server/api/admin/npc_admin_mgmt_api.py`
- **npc_router_core.py** (16 connections) — `server/api/admin/npc_router_core.py`
- **AdminAction** (16 connections) — `server/services/admin_auth_service.py`
- **list_dialogue_definitions()** (13 connections) — `server/api/admin/dialogue_definitions_api.py`
- **upsert_dialogue_definition()** (13 connections) — `server/api/admin/dialogue_definitions_api.py`
- **create_dialogue_definition()** (13 connections) — `server/api/admin/dialogue_definitions_api.py`
- **test_npc_admin_mgmt_api.py** (13 connections) — `server/tests/unit/api/admin/test_npc_admin_mgmt_api.py`
- **get_dialogue_definition()** (12 connections) — `server/api/admin/dialogue_definitions_api.py`
- **get_admin_sessions()** (12 connections) — `server/api/admin/npc_admin_mgmt_api.py`
- **delete_dialogue_definition()** (11 connections) — `server/api/admin/dialogue_definitions_api.py`
- **to_response()** (10 connections) — `server/api/admin/dialogue_definitions_api.py`
- **cleanup_admin_sessions()** (10 connections) — `server/api/admin/npc_admin_mgmt_api.py`
- **DialogueDefinitionResponse** (9 connections) — `server/api/admin/dialogue_schemas.py`
- **npc.py** (9 connections) — `server/api/admin/npc.py`
- **get_admin_audit_log()** (9 connections) — `server/api/admin/npc_admin_mgmt_api.py`
- **dialogue_schemas.py** (7 connections) — `server/api/admin/dialogue_schemas.py`
- **DialogueDefinitionCreate** (7 connections) — `server/api/admin/dialogue_schemas.py`
- **DialogueDefinitionUpdate** (7 connections) — `server/api/admin/dialogue_schemas.py`
- **__init__.py** (5 connections) — `server/api/admin/__init__.py`
- *... and 46 more nodes in this community*

## Relationships

- [logging setup structured](logging_setup_structured.md) (26 shared connections)
- [player requests schemas](player_requests_schemas.md) (20 shared connections)
- [Exception Containers](Exception_Containers.md) (19 shared connections)
- [persistence container rationale](persistence_container_rationale.md) (16 shared connections)
- [commands inventory helpers](commands_inventory_helpers.md) (13 shared connections)
- [auth users rationale](auth_users_rationale.md) (12 shared connections)
- [NPC Combat](NPC_Combat.md) (10 shared connections)
- [countdown rest task](countdown_rest_task.md) (10 shared connections)
- [message broadcaster realtime](message_broadcaster_realtime.md) (6 shared connections)
- [dialogue service game](dialogue_service_game.md) (6 shared connections)
- [Loot Generation](Loot_Generation.md) (5 shared connections)
- [maps handle ascii](maps_handle_ascii.md) (5 shared connections)

## Source Files

- `server/api/admin/__init__.py`
- `server/api/admin/dialogue_definitions_api.py`
- `server/api/admin/dialogue_schemas.py`
- `server/api/admin/npc.py`
- `server/api/admin/npc_admin_mgmt_api.py`
- `server/api/admin/npc_population_api.py`
- `server/api/admin/npc_router_core.py`
- `server/services/admin_auth_service.py`
- `server/tests/unit/api/admin/test_npc_admin_mgmt_api.py`
- `server/tests/unit/api/test_dialogue_definitions_api.py`

## Audit Trail

- EXTRACTED: 472 (99%)
- INFERRED: 6 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*