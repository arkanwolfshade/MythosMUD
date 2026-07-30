# lifespan shutdown

> 12 nodes

## Key Concepts

- **test_command_helpers.py** (27 connections) — `server/tests/unit/utils/test_command_helpers.py`
- **get_command_help()** (12 connections) — `server/utils/command_helpers.py`
- **test_get_command_help_no_command()** (3 connections) — `server/tests/unit/utils/test_command_helpers.py`
- **test_get_command_help_specific_commands()** (3 connections) — `server/tests/unit/utils/test_command_helpers.py`
- **test_get_command_help_unknown_command()** (3 connections) — `server/tests/unit/utils/test_command_helpers.py`
- **test_get_command_help_case_insensitive()** (3 connections) — `server/tests/unit/utils/test_command_helpers.py`
- **Unit tests for command helper utilities.  Tests helper functions for command par** (1 connections) — `server/tests/unit/utils/test_command_helpers.py`
- **Test get_command_help with no command (general help).** (1 connections) — `server/tests/unit/utils/test_command_helpers.py`
- **Test get_command_help with specific command types.** (1 connections) — `server/tests/unit/utils/test_command_helpers.py`
- **Test get_command_help with unknown command.** (1 connections) — `server/tests/unit/utils/test_command_helpers.py`
- **Test get_command_help is case insensitive.** (1 connections) — `server/tests/unit/utils/test_command_helpers.py`
- **Get help text for commands.      Args:         command_type: Specific command to** (1 connections) — `server/utils/command_helpers.py`

## Relationships

- [. get persistence from app()](_get_persistence_from_app%28%29.md) (21 shared connections)
- [Spell Targeting](Spell_Targeting.md) (4 shared connections)
- [real time](real_time.md) (1 shared connections)
- [.initialize()](initialize%28%29.md) (1 shared connections)

## Source Files

- `server/tests/unit/utils/test_command_helpers.py`
- `server/utils/command_helpers.py`

## Audit Trail

- EXTRACTED: 57 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*