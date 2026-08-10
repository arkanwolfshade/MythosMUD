# NATS Connection State Machine

> 14 nodes

## Key Concepts

- **TestPrepareCommandForProcessing** (7 connections) — `server/tests/unit/commands/test_command_preparation.py`
- **test_command_preparation.py** (4 connections) — `server/tests/unit/commands/test_command_preparation.py`
- **.test_prepare_command_rate_limited()** (3 connections) — `server/tests/unit/commands/test_command_preparation.py`
- **.test_prepare_command_validation_failed()** (3 connections) — `server/tests/unit/commands/test_command_preparation.py`
- **.test_prepare_command_empty_after_cleaning()** (3 connections) — `server/tests/unit/commands/test_command_preparation.py`
- **.test_prepare_command_empty_after_normalization()** (3 connections) — `server/tests/unit/commands/test_command_preparation.py`
- **.test_prepare_command_success()** (3 connections) — `server/tests/unit/commands/test_command_preparation.py`
- **Unit tests for command preparation.  Tests command preparation and processing pi** (1 connections) — `server/tests/unit/commands/test_command_preparation.py`
- **Test _prepare_command_for_processing function.** (1 connections) — `server/tests/unit/commands/test_command_preparation.py`
- **Test _prepare_command_for_processing returns rate limit result when rate limited** (1 connections) — `server/tests/unit/commands/test_command_preparation.py`
- **Test _prepare_command_for_processing returns validation result when validation f** (1 connections) — `server/tests/unit/commands/test_command_preparation.py`
- **Test _prepare_command_for_processing handles empty command after cleaning.** (1 connections) — `server/tests/unit/commands/test_command_preparation.py`
- **Test _prepare_command_for_processing handles empty command after normalization.** (1 connections) — `server/tests/unit/commands/test_command_preparation.py`
- **Test _prepare_command_for_processing successfully prepares command.** (1 connections) — `server/tests/unit/commands/test_command_preparation.py`

## Relationships

- [Investigations Sessions Session](Investigations_Sessions_Session.md) (6 shared connections)
- [Client Event Store](Client_Event_Store.md) (1 shared connections)

## Source Files

- `server/tests/unit/commands/test_command_preparation.py`

## Audit Trail

- EXTRACTED: 33 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*