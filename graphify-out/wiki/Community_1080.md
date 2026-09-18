# Community 1080

> 12 nodes

## Key Concepts

- **_check_rate_limit()** (9 connections) — `server/command_handler_unified.py`
- **TestCheckRateLimit** (4 connections) — `server/tests/unit/commands/test_command_validation.py`
- **.test_check_rate_limit_allowed()** (3 connections) — `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- **.test_check_rate_limit_blocked()** (3 connections) — `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- **.test_check_rate_limit_allowed()** (3 connections) — `server/tests/unit/commands/test_command_validation.py`
- **.test_check_rate_limit_blocked()** (3 connections) — `server/tests/unit/commands/test_command_validation.py`
- **Check if player is rate limited. Returns result dict if blocked, None if…** (1 connections) — `server/command_handler_unified.py`
- **Test _check_rate_limit returns None when allowed.** (1 connections) — `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- **Test _check_rate_limit returns result when blocked.** (1 connections) — `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- **Test _check_rate_limit function.** (1 connections) — `server/tests/unit/commands/test_command_validation.py`
- **Test _check_rate_limit returns None when allowed.** (1 connections) — `server/tests/unit/commands/test_command_validation.py`
- **Test _check_rate_limit returns result when blocked.** (1 connections) — `server/tests/unit/commands/test_command_validation.py`

## Relationships

- [Catatonia Status Checks](Catatonia_Status_Checks.md) (2 shared connections)
- [Community 360](Community_360.md) (2 shared connections)
- [Community 726](Community_726.md) (1 shared connections)
- [Community 256](Community_256.md) (1 shared connections)
- [Character Creation & Auth Dependencies](Character_Creation_&_Auth_Dependencies.md) (1 shared connections)

## Source Files

- `server/command_handler_unified.py`
- `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- `server/tests/unit/commands/test_command_validation.py`

## Audit Trail

- EXTRACTED: 19 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*