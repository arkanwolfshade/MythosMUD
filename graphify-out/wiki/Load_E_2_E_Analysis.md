# Load E 2 E Analysis

> 24 nodes

## Key Concepts

- **_prepare_command_for_processing()** (21 connections) — `server/command_handler_unified.py`
- **TestPrepareCommandForProcessing** (7 connections) — `server/tests/unit/commands/test_command_preparation.py`
- **test_command_preparation.py** (4 connections) — `server/tests/unit/commands/test_command_preparation.py`
- **.test_prepare_command_for_processing_rate_limited()** (3 connections) — `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- **.test_prepare_command_for_processing_validation_failed()** (3 connections) — `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- **.test_prepare_command_for_processing_empty_after_cleaning()** (3 connections) — `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- **.test_prepare_command_for_processing_success()** (3 connections) — `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- **.test_prepare_command_rate_limited()** (3 connections) — `server/tests/unit/commands/test_command_preparation.py`
- **.test_prepare_command_validation_failed()** (3 connections) — `server/tests/unit/commands/test_command_preparation.py`
- **.test_prepare_command_empty_after_cleaning()** (3 connections) — `server/tests/unit/commands/test_command_preparation.py`
- **.test_prepare_command_empty_after_normalization()** (3 connections) — `server/tests/unit/commands/test_command_preparation.py`
- **.test_prepare_command_success()** (3 connections) — `server/tests/unit/commands/test_command_preparation.py`
- **Prepare command for processing. Returns (command_line, cmd, args, alias_storage,** (1 connections) — `server/command_handler_unified.py`
- **Test _prepare_command_for_processing returns rate limit result.** (1 connections) — `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- **Test _prepare_command_for_processing returns validation result.** (1 connections) — `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- **Test _prepare_command_for_processing returns empty result after cleaning.** (1 connections) — `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- **Test _prepare_command_for_processing successfully prepares command.** (1 connections) — `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- **Unit tests for command preparation.  Tests command preparation and processing pi** (1 connections) — `server/tests/unit/commands/test_command_preparation.py`
- **Test _prepare_command_for_processing function.** (1 connections) — `server/tests/unit/commands/test_command_preparation.py`
- **Test _prepare_command_for_processing returns rate limit result when rate limited** (1 connections) — `server/tests/unit/commands/test_command_preparation.py`
- **Test _prepare_command_for_processing returns validation result when validation f** (1 connections) — `server/tests/unit/commands/test_command_preparation.py`
- **Test _prepare_command_for_processing handles empty command after cleaning.** (1 connections) — `server/tests/unit/commands/test_command_preparation.py`
- **Test _prepare_command_for_processing handles empty command after normalization.** (1 connections) — `server/tests/unit/commands/test_command_preparation.py`
- **Test _prepare_command_for_processing successfully prepares command.** (1 connections) — `server/tests/unit/commands/test_command_preparation.py`

## Relationships

- [Room Exploration API](Room_Exploration_API.md) (6 shared connections)
- [Admin Teleport Commands](Admin_Teleport_Commands.md) (4 shared connections)
- [FastAPI Auth Integration](FastAPI_Auth_Integration.md) (2 shared connections)
- [Player Schema Converter](Player_Schema_Converter.md) (1 shared connections)
- [Commands Look Item](Commands_Look_Item.md) (1 shared connections)
- [Game Magic Spell](Game_Magic_Spell.md) (1 shared connections)

## Source Files

- `server/command_handler_unified.py`
- `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- `server/tests/unit/commands/test_command_preparation.py`

## Audit Trail

- EXTRACTED: 71 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*