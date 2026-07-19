# Unified Command Handler

> 61 nodes · cohesion 0.05

## Key Concepts

- **_prepare_command_for_processing()** (21 connections) — `server/command_handler_unified.py`
- **process_command_unified()** (19 connections) — `server/command_handler_unified.py`
- **_handle_special_command_routing()** (18 connections) — `server/command_handler_unified.py`
- **Any** (14 connections) — `server/command_handler_unified.py`
- **CommandRequest** (11 connections) — `server/command_handler_unified.py`
- **CommandExecutionRequest** (11 connections) — `server/command_handler_unified.py`
- **test_command_handler_unified.py** (10 connections) — `server/tests/unit/commands/test_command_handler_unified.py`
- **_check_rate_limit()** (10 connections) — `server/command_handler_unified.py`
- **handle_command()** (10 connections) — `server/command_handler_unified.py`
- **process_command()** (9 connections) — `server/command_handler_unified.py`
- **TestProcessCommandUnified** (7 connections) — `server/tests/unit/commands/test_command_handler_unified.py`
- **TestPrepareCommandForProcessing** (7 connections) — `server/tests/unit/commands/test_command_preparation.py`
- **_get_grace_check_context()** (7 connections) — `server/command_handler_unified.py`
- **AliasStorage** (7 connections) — `server/command_handler_unified.py`
- **TestLegacyFunctions** (6 connections) — `server/tests/unit/commands/test_command_handler_unified.py`
- **get_help_content()** (6 connections) — `server/command_handler_unified.py`
- **TestHandleCommand** (5 connections) — `server/tests/unit/commands/test_command_handler_unified.py`
- **.test_handle_command_success()** (4 connections) — `server/tests/unit/commands/test_command_handler_unified.py`
- **.test_handle_command_unauthorized()** (4 connections) — `server/tests/unit/commands/test_command_handler_unified.py`
- **test_command_preparation.py** (4 connections) — `server/tests/unit/commands/test_command_preparation.py`
- **.test_get_help_content()** (3 connections) — `server/tests/unit/commands/test_command_handler_unified.py`
- **.test_get_help_content_none()** (3 connections) — `server/tests/unit/commands/test_command_handler_unified.py`
- **.test_process_command_legacy()** (3 connections) — `server/tests/unit/commands/test_command_handler_unified.py`
- **.test_process_command_unified_blocked()** (3 connections) — `server/tests/unit/commands/test_command_handler_unified.py`
- **.test_process_command_unified_normal_processing()** (3 connections) — `server/tests/unit/commands/test_command_handler_unified.py`
- *... and 36 more nodes in this community*

## Relationships

- [[Alias Expansion Logic]] (19 shared connections)
- [[Command Alias Handling]] (16 shared connections)
- [[Commands Command Handler]] (7 shared connections)
- [[Command Request App State]] (5 shared connections)
- [[Command Commands Validation]] (5 shared connections)
- [[Grace Period Blocking Tests]] (3 shared connections)
- [[Command Input Utilities]] (3 shared connections)
- [[Commands Command Validation]] (2 shared connections)
- [[Command Helper Utilities]] (2 shared connections)
- [[WebSocket Command Handler]] (2 shared connections)
- [[Catatonia Check Logic]] (1 shared connections)
- [[Admin NPC Schemas]] (1 shared connections)

## Source Files

- `server/command_handler_unified.py`
- `server/tests/unit/commands/test_command_handler_unified.py`
- `server/tests/unit/commands/test_command_preparation.py`

## Audit Trail

- EXTRACTED: 244 (95%)
- INFERRED: 13 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
