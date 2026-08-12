# Commands Look Item

> 12 nodes

## Key Concepts

- **_check_rate_limit()** (10 connections) — `server/command_handler_unified.py`
- **TestCheckRateLimit** (4 connections) — `server/tests/unit/commands/test_command_validation.py`
- **.test_check_rate_limit_allowed()** (3 connections) — `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- **.test_check_rate_limit_blocked()** (3 connections) — `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- **.test_check_rate_limit_allowed()** (3 connections) — `server/tests/unit/commands/test_command_validation.py`
- **.test_check_rate_limit_blocked()** (3 connections) — `server/tests/unit/commands/test_command_validation.py`
- **Check if player is rate limited. Returns result dict if blocked, None if allowed** (1 connections) — `server/command_handler_unified.py`
- **Test _check_rate_limit returns None when allowed.** (1 connections) — `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- **Test _check_rate_limit returns result when blocked.** (1 connections) — `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- **Test _check_rate_limit function.** (1 connections) — `server/tests/unit/commands/test_command_validation.py`
- **Test _check_rate_limit returns None when allowed.** (1 connections) — `server/tests/unit/commands/test_command_validation.py`
- **Test _check_rate_limit returns result when blocked.** (1 connections) — `server/tests/unit/commands/test_command_validation.py`

## Relationships

- [Room Exploration API](Room_Exploration_API.md) (3 shared connections)
- [Catatonia Check Logic](Catatonia_Check_Logic.md) (2 shared connections)
- [Admin Teleport Commands](Admin_Teleport_Commands.md) (2 shared connections)
- [Load E 2 E Analysis](Load_E_2_E_Analysis.md) (1 shared connections)

## Source Files

- `server/command_handler_unified.py`
- `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- `server/tests/unit/commands/test_command_validation.py`

## Audit Trail

- EXTRACTED: 32 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*