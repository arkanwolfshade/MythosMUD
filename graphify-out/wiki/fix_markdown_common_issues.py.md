# fix_markdown_common_issues.py

> 14 nodes · cohesion 0.15

## Key Concepts

- **asyncio** (35 connections)
- **test_get_npc_definitions_by_type()** (5 connections) — `server/tests/unit/services/test_npc_service.py`
- **test_delete_npc_definition_not_found()** (4 connections) — `server/tests/unit/services/test_npc_service.py`
- **test_get_npc_definitions_database_error()** (4 connections) — `server/tests/unit/services/test_npc_service.py`
- **test_get_npc_definitions_empty()** (4 connections) — `server/tests/unit/services/test_npc_service.py`
- **test_create_npc_definition_invalid_max_population()** (3 connections) — `server/tests/unit/services/test_npc_service.py`
- **test_create_npc_definition_invalid_type()** (3 connections) — `server/tests/unit/services/test_npc_service.py`
- **test_get_npc_definition_error()** (3 connections) — `server/tests/unit/services/test_npc_service.py`
- **Test get_npc_definitions() returns empty list when no definitions.** (1 connections) — `server/tests/unit/services/test_npc_service.py`
- **Test get_npc_definitions() handles database errors.** (1 connections) — `server/tests/unit/services/test_npc_service.py`
- **Test get_npc_definition() handles errors.** (1 connections) — `server/tests/unit/services/test_npc_service.py`
- **Test create_npc_definition() raises ValueError for invalid type.** (1 connections) — `server/tests/unit/services/test_npc_service.py`
- **Test delete_npc_definition() returns False when not found.** (1 connections) — `server/tests/unit/services/test_npc_service.py`
- **Test get_npc_definitions_by_type() filters by type.** (1 connections) — `server/tests/unit/services/test_npc_service.py`

## Relationships

- [cross-env](cross-env.md) (12 shared connections)
- [Memory Leak Audit Report](Memory_Leak_Audit_Report.md) (10 shared connections)
- [properties](properties.md) (8 shared connections)
- [TRACK C · The interactive review — 8 decisions](TRACK_C_·_The_interactive_review_—_8_decisions.md) (5 shared connections)
- [test_handle_spell_command_success](test_handle_spell_command_success.md) (1 shared connections)
- [.__init__](__init__.md) (1 shared connections)
- [Improve Copy Systematically](Improve_Copy_Systematically.md) (1 shared connections)
- [.stop_audit_scheduler](stop_audit_scheduler.md) (1 shared connections)
- [LoggingPatternLinter](LoggingPatternLinter.md) (1 shared connections)

## Source Files

- `server/tests/unit/services/test_npc_service.py`

## Audit Trail

- EXTRACTED: 53 (98%)
- INFERRED: 1 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*