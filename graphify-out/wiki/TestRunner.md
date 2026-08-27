# TestRunner

> 26 nodes

## Key Concepts

- **TestCommandNormalization** (12 connections) — `server/tests/unit/commands/test_command_input.py`
- **normalize_command()** (11 connections) — `server/command_handler/command_input.py`
- **clean_command_input()** (9 connections) — `server/command_handler/command_input.py`
- **.test_clean_command_input_basic()** (3 connections) — `server/tests/unit/commands/test_command_input.py`
- **.test_clean_command_input_leading_trailing_whitespace()** (3 connections) — `server/tests/unit/commands/test_command_input.py`
- **.test_clean_command_input_multiple_spaces()** (3 connections) — `server/tests/unit/commands/test_command_input.py`
- **.test_clean_command_input_tabs()** (3 connections) — `server/tests/unit/commands/test_command_input.py`
- **.test_normalize_command_empty()** (3 connections) — `server/tests/unit/commands/test_command_input.py`
- **.test_normalize_command_no_slash()** (3 connections) — `server/tests/unit/commands/test_command_input.py`
- **.test_normalize_command_slash_only()** (3 connections) — `server/tests/unit/commands/test_command_input.py`
- **.test_normalize_command_slash_with_spaces()** (3 connections) — `server/tests/unit/commands/test_command_input.py`
- **.test_normalize_command_whitespace_only()** (3 connections) — `server/tests/unit/commands/test_command_input.py`
- **.test_normalize_command_with_slash()** (3 connections) — `server/tests/unit/commands/test_command_input.py`
- **Clean and normalize command input by collapsing multiple spaces and stripping…** (1 connections) — `server/command_handler/command_input.py`
- **Normalize command input by removing optional slash prefix. Supports both…** (1 connections) — `server/command_handler/command_input.py`
- **Test command normalization functions.** (1 connections) — `server/tests/unit/commands/test_command_input.py`
- **Test clean_command_input() with normal command.** (1 connections) — `server/tests/unit/commands/test_command_input.py`
- **Test clean_command_input() collapses multiple spaces.** (1 connections) — `server/tests/unit/commands/test_command_input.py`
- **Test clean_command_input() strips leading/trailing whitespace.** (1 connections) — `server/tests/unit/commands/test_command_input.py`
- **Test clean_command_input() handles tabs.** (1 connections) — `server/tests/unit/commands/test_command_input.py`
- **Test normalize_command() with no slash prefix.** (1 connections) — `server/tests/unit/commands/test_command_input.py`
- **Test normalize_command() removes slash prefix.** (1 connections) — `server/tests/unit/commands/test_command_input.py`
- **Test normalize_command() with empty string.** (1 connections) — `server/tests/unit/commands/test_command_input.py`
- **Test normalize_command() with whitespace only.** (1 connections) — `server/tests/unit/commands/test_command_input.py`
- **Test normalize_command() with slash only.** (1 connections) — `server/tests/unit/commands/test_command_input.py`
- *... and 1 more nodes in this community*

## Relationships

- [generate_invites_db.py](generate_invites_db.py.md) (4 shared connections)
- [Structured Logging with Structlog Best Practices](Structured_Logging_with_Structlog_Best_Practices.md) (3 shared connections)
- [test_connection_statistics.py](test_connection_statistics.py.md) (2 shared connections)

## Source Files

- `server/command_handler/command_input.py`
- `server/tests/unit/commands/test_command_input.py`

## Audit Trail

- EXTRACTED: 40 (95%)
- INFERRED: 2 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*