# test_connection_statistics.py

> 61 nodes

## Key Concepts

- **command_handler_unified.py** (40 connections) — `server/command_handler_unified.py`
- **_prepare_command_for_processing()** (21 connections) — `server/command_handler_unified.py`
- **_check_casting_state()** (17 connections) — `server/command_handler_unified.py`
- **_handle_special_command_routing()** (17 connections) — `server/command_handler_unified.py`
- **process_command_unified()** (17 connections) — `server/command_handler_unified.py`
- **_check_all_command_blocks()** (16 connections) — `server/command_handler_unified.py`
- **_process_alias_expansion()** (16 connections) — `server/command_handler_unified.py`
- **test_command_handler_unified_helpers.py** (14 connections) — `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- **Any** (13 connections)
- **_ensure_alias_storage()** (12 connections) — `server/command_handler_unified.py`
- **test_command_handler_unified.py** (12 connections) — `server/tests/unit/commands/test_command_handler_unified.py`
- **_check_rate_limit()** (10 connections) — `server/command_handler_unified.py`
- **CommandExecutionRequest** (9 connections)
- **test_command_aliases.py** (9 connections) — `server/tests/unit/commands/test_command_aliases.py`
- **process_command()** (8 connections) — `server/command_handler_unified.py`
- **TestPrepareCommandForProcessing** (7 connections) — `server/tests/unit/commands/test_command_preparation.py`
- **AliasStorage** (6 connections)
- **TestEnsureAliasStorage** (5 connections) — `server/tests/unit/commands/test_command_aliases.py`
- **TestLegacyFunctions** (5 connections) — `server/tests/unit/commands/test_command_handler_unified.py`
- **_get_casting_block_result()** (5 connections) — `server/command_handler_unified.py`
- **get_help_content()** (5 connections) — `server/command_handler_unified.py`
- **test_command_preparation.py** (4 connections) — `server/tests/unit/commands/test_command_preparation.py`
- **.test_ensure_alias_storage_handles_error()** (3 connections) — `server/tests/unit/commands/test_command_aliases.py`
- **.test_ensure_alias_storage_initializes_new()** (3 connections) — `server/tests/unit/commands/test_command_aliases.py`
- **.test_ensure_alias_storage_returns_existing()** (3 connections) — `server/tests/unit/commands/test_command_aliases.py`
- *... and 36 more nodes in this community*

## Relationships

- [test_error_handling_middleware.py](test_error_handling_middleware.py.md) (27 shared connections)
- [ContainerTransferToMixin](ContainerTransferToMixin.md) (14 shared connections)
- [generate_invites_db.py](generate_invites_db.py.md) (13 shared connections)
- [run_flee_effect](run_flee_effect.md) (10 shared connections)
- [SQLAlchemy Best Practices (2.x Style)](SQLAlchemy_Best_Practices_2.x_Style.md) (9 shared connections)
- [test_message_handlers.py](test_message_handlers.py.md) (8 shared connections)
- [Second NPC Combat And Linkdead Findings](Second_NPC_Combat_And_Linkdead_Findings.md) (4 shared connections)
- [test_mp_regeneration_service.py](test_mp_regeneration_service.py.md) (4 shared connections)
- [ContainerComponent](ContainerComponent.md) (3 shared connections)
- [Call of Cthulhu Starter Set (source summary)](Call_of_Cthulhu_Starter_Set_source_summary.md) (2 shared connections)
- [TestRunner](TestRunner.md) (2 shared connections)
- [test_goto_helpers.py](test_goto_helpers.py.md) (2 shared connections)

## Source Files

- `server/command_handler_unified.py`
- `server/tests/unit/commands/test_command_aliases.py`
- `server/tests/unit/commands/test_command_handler_unified.py`
- `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- `server/tests/unit/commands/test_command_preparation.py`

## Audit Trail

- EXTRACTED: 213 (99%)
- INFERRED: 3 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*