# TestCheckRateLimit

> 6 nodes

## Key Concepts

- **TestCheckRateLimit** (4 connections) — `server/tests/unit/commands/test_command_validation.py`
- **.test_check_rate_limit_allowed()** (3 connections) — `server/tests/unit/commands/test_command_validation.py`
- **.test_check_rate_limit_blocked()** (3 connections) — `server/tests/unit/commands/test_command_validation.py`
- **Test _check_rate_limit function.** (1 connections) — `server/tests/unit/commands/test_command_validation.py`
- **Test _check_rate_limit returns None when allowed.** (1 connections) — `server/tests/unit/commands/test_command_validation.py`
- **Test _check_rate_limit returns result when blocked.** (1 connections) — `server/tests/unit/commands/test_command_validation.py`

## Relationships

- [command_handler_unified.py](command_handler_unified.py.md) (2 shared connections)
- [catatonia_check.py](catatonia_check.py.md) (1 shared connections)

## Source Files

- `server/tests/unit/commands/test_command_validation.py`

## Audit Trail

- EXTRACTED: 8 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*