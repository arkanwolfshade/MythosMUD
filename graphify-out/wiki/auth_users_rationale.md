# auth users rationale

> 27 nodes

## Key Concepts

- **npc_spawn_rules_api.py** (23 connections) — `server/api/admin/npc_spawn_rules_api.py`
- **test_npc_spawn_rules_api.py** (16 connections) — `server/tests/unit/api/test_npc_spawn_rules_api.py`
- **get_npc_spawn_rules()** (14 connections) — `server/api/admin/npc_spawn_rules_api.py`
- **create_npc_spawn_rule()** (14 connections) — `server/api/admin/npc_spawn_rules_api.py`
- **delete_npc_spawn_rule()** (11 connections) — `server/api/admin/npc_spawn_rules_api.py`
- **NPCSpawnRuleResponse** (7 connections) — `server/api/admin/npc_schemas.py`
- **.from_orm()** (6 connections) — `server/api/admin/npc_schemas.py`
- **NPCSpawnRuleCreate** (5 connections) — `server/api/admin/npc_schemas.py`
- **Request** (3 connections)
- **AsyncSession** (3 connections)
- **test_get_npc_spawn_rules_generic_error()** (3 connections) — `server/tests/unit/api/test_npc_spawn_rules_api.py`
- **test_create_npc_spawn_rule_rolls_back()** (3 connections) — `server/tests/unit/api/test_npc_spawn_rules_api.py`
- **test_delete_npc_spawn_rule_not_found()** (3 connections) — `server/tests/unit/api/test_npc_spawn_rules_api.py`
- **test_get_npc_spawn_rules_success()** (2 connections) — `server/tests/unit/api/test_npc_spawn_rules_api.py`
- **test_get_npc_spawn_rules_http_exception_propagates()** (2 connections) — `server/tests/unit/api/test_npc_spawn_rules_api.py`
- **test_create_npc_spawn_rule_success()** (2 connections) — `server/tests/unit/api/test_npc_spawn_rules_api.py`
- **test_delete_npc_spawn_rule_success()** (2 connections) — `server/tests/unit/api/test_npc_spawn_rules_api.py`
- **Model for creating NPC spawn rules.** (1 connections) — `server/api/admin/npc_schemas.py`
- **Model for NPC spawn rule responses.** (1 connections) — `server/api/admin/npc_schemas.py`
- **Create response from ORM object.** (1 connections) — `server/api/admin/npc_schemas.py`
- **NPC spawn rule admin endpoints.  Split out from server.api.admin.npc to keep fil** (1 connections) — `server/api/admin/npc_spawn_rules_api.py`
- **Get all NPC spawn rules.** (1 connections) — `server/api/admin/npc_spawn_rules_api.py`
- **Create a new NPC spawn rule.** (1 connections) — `server/api/admin/npc_spawn_rules_api.py`
- **Delete an NPC spawn rule.** (1 connections) — `server/api/admin/npc_spawn_rules_api.py`
- **mock_user()** (1 connections) — `server/tests/unit/api/test_npc_spawn_rules_api.py`
- *... and 2 more nodes in this community*

## Relationships

- [player preferences services](player_preferences_services.md) (12 shared connections)
- [Exception Containers](Exception_Containers.md) (8 shared connections)
- [persistence container rationale](persistence_container_rationale.md) (6 shared connections)
- [player requests schemas](player_requests_schemas.md) (6 shared connections)
- [Loot Generation](Loot_Generation.md) (2 shared connections)
- [NPC Combat](NPC_Combat.md) (2 shared connections)
- [container events rationale](container_events_rationale.md) (1 shared connections)
- [game models enums](game_models_enums.md) (1 shared connections)
- [command player state](command_player_state.md) (1 shared connections)

## Source Files

- `server/api/admin/npc_schemas.py`
- `server/api/admin/npc_spawn_rules_api.py`
- `server/tests/unit/api/test_npc_spawn_rules_api.py`

## Audit Trail

- EXTRACTED: 126 (98%)
- INFERRED: 3 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*