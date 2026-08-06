# persistence container rationale

> 368 nodes

## Key Concepts

- **__init__.py** (70 connections) — `server/schemas/__init__.py`
- **user.py** (63 connections) — `server/models/user.py`
- **test_admin_auth_service.py** (54 connections) — `server/tests/unit/services/test_admin_auth_service.py`
- **get_admin_auth_service()** (44 connections) — `server/services/admin_auth_service.py`
- **validate_admin_permission()** (37 connections) — `server/api/admin/npc_router_core.py`
- **test_npc_definitions_api.py** (31 connections) — `server/tests/unit/api/test_npc_definitions_api.py`
- **npc_definitions_api.py** (30 connections) — `server/api/admin/npc_definitions_api.py`
- **dialogue_definitions_api.py** (27 connections) — `server/api/admin/dialogue_definitions_api.py`
- **npc_instances_api.py** (27 connections) — `server/api/admin/npc_instances_api.py`
- **test_dialogue_definitions_api.py** (26 connections) — `server/tests/unit/api/test_dialogue_definitions_api.py`
- **admin_auth_service.py** (24 connections) — `server/services/admin_auth_service.py`
- **npc_population_api.py** (23 connections) — `server/api/admin/npc_population_api.py`
- **npc_schemas.py** (23 connections) — `server/api/admin/npc_schemas.py`
- **npc_spawn_rules_api.py** (23 connections) — `server/api/admin/npc_spawn_rules_api.py`
- **npc_admin_mgmt_api.py** (21 connections) — `server/api/admin/npc_admin_mgmt_api.py`
- **test_npc_instances_api.py** (21 connections) — `server/tests/unit/api/test_npc_instances_api.py`
- **DialogueTree** (19 connections) — `server/schemas/dialogue/dialogue_tree.py`
- **AdminAuthService** (19 connections) — `server/services/admin_auth_service.py`
- **_update_npc_definition_internal()** (16 connections) — `server/api/admin/npc_definitions_api.py`
- **npc_router_core.py** (16 connections) — `server/api/admin/npc_router_core.py`
- **AdminAction** (16 connections) — `server/services/admin_auth_service.py`
- **test_npc_spawn_rules_api.py** (16 connections) — `server/tests/unit/api/test_npc_spawn_rules_api.py`
- **npc_admin.py** (15 connections) — `server/schemas/admin/npc_admin.py`
- **get_npc_definitions()** (14 connections) — `server/api/admin/npc_definitions_api.py`
- **get_npc_spawn_rules()** (14 connections) — `server/api/admin/npc_spawn_rules_api.py`
- *... and 343 more nodes in this community*

## Relationships

- [services inventory mutation](services_inventory_mutation.md) (53 shared connections)
- [player requests schemas](player_requests_schemas.md) (45 shared connections)
- [logging examples fastapi](logging_examples_fastapi.md) (17 shared connections)
- [maps handle ascii](maps_handle_ascii.md) (13 shared connections)
- [Error Handling Core](Error_Handling_Core.md) (12 shared connections)
- [tick game processing](tick_game_processing.md) (12 shared connections)
- [NPC Combat](NPC_Combat.md) (11 shared connections)
- [dialogue service game](dialogue_service_game.md) (11 shared connections)
- [Exception Containers](Exception_Containers.md) (10 shared connections)
- [websocket handler realtime](websocket_handler_realtime.md) (9 shared connections)
- [Player Stats](Player_Stats.md) (9 shared connections)
- [metrics schemas rationale](metrics_schemas_rationale.md) (8 shared connections)

## Source Files

- `server/api/admin/__init__.py`
- `server/api/admin/dialogue_definitions_api.py`
- `server/api/admin/dialogue_schemas.py`
- `server/api/admin/npc.py`
- `server/api/admin/npc_admin_mgmt_api.py`
- `server/api/admin/npc_definitions_api.py`
- `server/api/admin/npc_instances_api.py`
- `server/api/admin/npc_population_api.py`
- `server/api/admin/npc_router_core.py`
- `server/api/admin/npc_schemas.py`
- `server/api/admin/npc_spawn_rules_api.py`
- `server/models/user.py`
- `server/schemas/__init__.py`
- `server/schemas/admin/__init__.py`
- `server/schemas/admin/admin_data.py`
- `server/schemas/admin/npc_admin.py`
- `server/schemas/dialogue/dialogue_tree.py`
- `server/services/admin_auth_service.py`
- `server/tests/unit/api/admin/test_npc_admin_mgmt_api.py`
- `server/tests/unit/api/admin/test_npc_population_api.py`

## Audit Trail

- EXTRACTED: 1761 (96%)
- INFERRED: 69 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*