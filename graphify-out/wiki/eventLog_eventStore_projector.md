# eventLog eventStore projector

> 10 nodes

## Key Concepts

- **_spawn_rule_row()** (6 connections) — `server/tests/unit/services/test_npc_service.py`
- **test_create_spawn_rule_success()** (5 connections) — `server/tests/unit/services/test_npc_service.py`
- **test_get_spawn_rules_success()** (4 connections) — `server/tests/unit/services/test_npc_service.py`
- **test_get_spawn_rule_found()** (4 connections) — `server/tests/unit/services/test_npc_service.py`
- **test_delete_spawn_rule_success()** (4 connections) — `server/tests/unit/services/test_npc_service.py`
- **Build procedure result row for NPCSpawnRule.** (1 connections) — `server/tests/unit/services/test_npc_service.py`
- **Test get_spawn_rules() successfully retrieves rules.** (1 connections) — `server/tests/unit/services/test_npc_service.py`
- **Test get_spawn_rule() returns rule when found.** (1 connections) — `server/tests/unit/services/test_npc_service.py`
- **Test create_spawn_rule() successfully creates rule.** (1 connections) — `server/tests/unit/services/test_npc_service.py`
- **Test delete_spawn_rule() successfully deletes rule.** (1 connections) — `server/tests/unit/services/test_npc_service.py`

## Relationships

- [npc service services](npc_service_services.md) (5 shared connections)
- [commands lucidity recovery](commands_lucidity_recovery.md) (4 shared connections)
- [models lucidity rationale](models_lucidity_rationale.md) (1 shared connections)

## Source Files

- `server/tests/unit/services/test_npc_service.py`

## Audit Trail

- EXTRACTED: 28 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*