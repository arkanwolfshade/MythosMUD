# Memory Leak Audit Report

> 15 nodes · cohesion 0.13

## Key Concepts

- **_mock_result_mappings_all()** (29 connections) — `server/tests/unit/services/test_npc_service.py`
- **test_create_spawn_rule_invalid_max_population()** (5 connections) — `server/tests/unit/services/test_npc_service.py`
- **test_get_npc_definition_by_name_case_insensitive()** (5 connections) — `server/tests/unit/services/test_npc_service.py`
- **test_update_npc_definition_invalid_probability()** (5 connections) — `server/tests/unit/services/test_npc_service.py`
- **test_create_spawn_rule_definition_not_found()** (4 connections) — `server/tests/unit/services/test_npc_service.py`
- **test_delete_spawn_rule_not_found()** (4 connections) — `server/tests/unit/services/test_npc_service.py`
- **test_get_npc_definition_not_found()** (4 connections) — `server/tests/unit/services/test_npc_service.py`
- **test_update_npc_definition_not_found()** (4 connections) — `server/tests/unit/services/test_npc_service.py`
- **Build mock result such that result.mappings().all() returns rows.** (1 connections) — `server/tests/unit/services/test_npc_service.py`
- **Test get_npc_definition_by_name() matches case-insensitively.** (1 connections) — `server/tests/unit/services/test_npc_service.py`
- **Test update_npc_definition() returns None when not found.** (1 connections) — `server/tests/unit/services/test_npc_service.py`
- **Test update_npc_definition() raises ValueError for invalid probability.** (1 connections) — `server/tests/unit/services/test_npc_service.py`
- **Test create_spawn_rule() raises ValueError when definition not found.** (1 connections) — `server/tests/unit/services/test_npc_service.py`
- **Test create_spawn_rule() raises ValueError when max < min.** (1 connections) — `server/tests/unit/services/test_npc_service.py`
- **Test delete_spawn_rule() returns False when not found.** (1 connections) — `server/tests/unit/services/test_npc_service.py`

## Relationships

- [cross-env](cross-env.md) (10 shared connections)
- [properties](properties.md) (10 shared connections)
- [fix_markdown_common_issues.py](fix_markdown_common_issues.py.md) (10 shared connections)
- [TRACK C · The interactive review — 8 decisions](TRACK_C_·_The_interactive_review_—_8_decisions.md) (5 shared connections)
- [test_handle_spell_command_success](test_handle_spell_command_success.md) (1 shared connections)
- [.__init__](__init__.md) (1 shared connections)
- [.stop_audit_scheduler](stop_audit_scheduler.md) (1 shared connections)

## Source Files

- `server/tests/unit/services/test_npc_service.py`

## Audit Trail

- EXTRACTED: 53 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*