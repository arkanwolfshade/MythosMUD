# MutableHeaders

> 14 nodes

## Key Concepts

- **_add_additional_stats_lines()** (12 connections) — `server/commands/status_commands.py`
- **test_add_additional_stats_lines_with_stats()** (3 connections) — `server/tests/unit/commands/test_status_commands.py`
- **test_add_additional_stats_lines_zero_stats()** (3 connections) — `server/tests/unit/commands/test_status_commands.py`
- **test_add_additional_stats_lines_missing_stats()** (3 connections) — `server/tests/unit/commands/test_status_commands.py`
- **test_add_additional_stats_lines()** (3 connections) — `server/tests/unit/commands/test_status_commands_helpers.py`
- **test_add_additional_stats_lines_empty()** (3 connections) — `server/tests/unit/commands/test_status_commands_helpers.py`
- **test_add_additional_stats_lines_zero_values()** (3 connections) — `server/tests/unit/commands/test_status_commands_helpers.py`
- **Add additional stats lines to status lines if they have non-zero values.      Ar** (1 connections) — `server/commands/status_commands.py`
- **Test _add_additional_stats_lines adds stats when non-zero.** (1 connections) — `server/tests/unit/commands/test_status_commands.py`
- **Test _add_additional_stats_lines does nothing when stats are zero.** (1 connections) — `server/tests/unit/commands/test_status_commands.py`
- **Test _add_additional_stats_lines handles missing stats.** (1 connections) — `server/tests/unit/commands/test_status_commands.py`
- **Test _add_additional_stats_lines() adds additional stats.** (1 connections) — `server/tests/unit/commands/test_status_commands_helpers.py`
- **Test _add_additional_stats_lines() handles empty stats.** (1 connections) — `server/tests/unit/commands/test_status_commands_helpers.py`
- **Test _add_additional_stats_lines() ignores zero values.** (1 connections) — `server/tests/unit/commands/test_status_commands_helpers.py`

## Relationships

- [status commands](status_commands.md) (4 shared connections)
- [HallucinationFrequencyService](HallucinationFrequencyService.md) (4 shared connections)
- [logging utilities](logging_utilities.md) (3 shared connections)

## Source Files

- `server/commands/status_commands.py`
- `server/tests/unit/commands/test_status_commands.py`
- `server/tests/unit/commands/test_status_commands_helpers.py`

## Audit Trail

- EXTRACTED: 37 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*