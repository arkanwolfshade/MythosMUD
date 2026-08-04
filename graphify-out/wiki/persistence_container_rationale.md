# persistence container rationale

> 51 nodes

## Key Concepts

- **test_npc_definitions_api.py** (31 connections) — `server/tests/unit/api/test_npc_definitions_api.py`
- **npc_definitions_api.py** (30 connections) — `server/api/admin/npc_definitions_api.py`
- **npc_schemas.py** (23 connections) — `server/api/admin/npc_schemas.py`
- **_update_npc_definition_internal()** (16 connections) — `server/api/admin/npc_definitions_api.py`
- **get_npc_definitions()** (14 connections) — `server/api/admin/npc_definitions_api.py`
- **create_npc_definition()** (13 connections) — `server/api/admin/npc_definitions_api.py`
- **get_npc_definition()** (13 connections) — `server/api/admin/npc_definitions_api.py`
- **_admin_user()** (12 connections) — `server/tests/unit/api/test_npc_definitions_api.py`
- **delete_npc_definition()** (11 connections) — `server/api/admin/npc_definitions_api.py`
- **BaseModel** (11 connections)
- **NPCDefinitionUpdate** (10 connections) — `server/api/admin/npc_schemas.py`
- **NPCDefinitionResponse** (10 connections) — `server/api/admin/npc_schemas.py`
- **.from_orm()** (10 connections) — `server/api/admin/npc_schemas.py`
- **update_npc_definition()** (8 connections) — `server/api/admin/npc_definitions_api.py`
- **test_create_npc_definition()** (8 connections) — `server/tests/unit/api/test_npc_definitions_api.py`
- **NPCDefinitionCreate** (7 connections) — `server/api/admin/npc_schemas.py`
- **Request** (6 connections)
- **NPCBaseStatsModel** (6 connections) — `server/api/admin/npc_schemas.py`
- **NPCBehaviorConfigModel** (6 connections) — `server/api/admin/npc_schemas.py`
- **NPCAIIntegrationModel** (6 connections) — `server/api/admin/npc_schemas.py`
- **build_update_params_from_model()** (6 connections) — `server/api/admin/npc_schemas.py`
- **AsyncSession** (5 connections)
- **_mock_definition()** (5 connections) — `server/tests/unit/api/test_npc_definitions_api.py`
- **test_update_npc_definition_internal()** (5 connections) — `server/tests/unit/api/test_npc_definitions_api.py`
- **test_update_npc_definition_not_found()** (5 connections) — `server/tests/unit/api/test_npc_definitions_api.py`
- *... and 26 more nodes in this community*

## Relationships

- [player preferences services](player_preferences_services.md) (16 shared connections)
- [player requests schemas](player_requests_schemas.md) (12 shared connections)
- [Exception Containers](Exception_Containers.md) (11 shared connections)
- [container events rationale](container_events_rationale.md) (9 shared connections)
- [logging setup structured](logging_setup_structured.md) (6 shared connections)
- [auth users rationale](auth_users_rationale.md) (6 shared connections)
- [player effects endpoints](player_effects_endpoints.md) (3 shared connections)
- [Loot Generation](Loot_Generation.md) (2 shared connections)
- [NPC Combat](NPC_Combat.md) (2 shared connections)
- [game models enums](game_models_enums.md) (1 shared connections)
- [command player state](command_player_state.md) (1 shared connections)

## Source Files

- `server/api/admin/npc_definitions_api.py`
- `server/api/admin/npc_schemas.py`
- `server/tests/unit/api/test_npc_definitions_api.py`

## Audit Trail

- EXTRACTED: 321 (99%)
- INFERRED: 4 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*