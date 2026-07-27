# Command Parser Helpers

> 33 nodes · cohesion 0.06

## Key Concepts

- **test_command_parser_helpers.py** (23 connections) — `server/tests/unit/utils/test_command_parser_helpers.py`
- **get_command_help()** (12 connections) — `server/utils/command_helpers.py`
- **test_get_command_help_unknown_command()** (3 connections) — `server/tests/unit/utils/test_command_helpers_functions.py`
- **Test get_command_help() returns error for unknown command.** (2 connections) — `server/tests/unit/utils/test_command_parser_helpers.py`
- **test_create_command_object_unsupported_command()** (2 connections) — `server/tests/unit/utils/test_command_parser_helpers.py`
- **test_create_command_object_value_error()** (2 connections) — `server/tests/unit/utils/test_command_parser_helpers.py`
- **test_create_command_object_with_alias_g()** (2 connections) — `server/tests/unit/utils/test_command_parser_helpers.py`
- **test_create_command_object_with_alias_l()** (2 connections) — `server/tests/unit/utils/test_command_parser_helpers.py`
- **test_create_command_object_with_alias_w()** (2 connections) — `server/tests/unit/utils/test_command_parser_helpers.py`
- **test_get_command_help_specific_command()** (2 connections) — `server/tests/unit/utils/test_command_parser_helpers.py`
- **test_get_command_help_unknown_command()** (2 connections) — `server/tests/unit/utils/test_command_parser_helpers.py`
- **test_normalize_command_cleans_whitespace()** (2 connections) — `server/tests/unit/utils/test_command_parser_helpers.py`
- **test_normalize_command_no_slash()** (2 connections) — `server/tests/unit/utils/test_command_parser_helpers.py`
- **test_normalize_command_removes_slash_prefix()** (2 connections) — `server/tests/unit/utils/test_command_parser_helpers.py`
- **test_normalize_command_strips_whitespace()** (2 connections) — `server/tests/unit/utils/test_command_parser_helpers.py`
- **test_parse_command_parts_lowercases_command()** (2 connections) — `server/tests/unit/utils/test_command_parser_helpers.py`
- **test_parse_command_parts_simple()** (2 connections) — `server/tests/unit/utils/test_command_parser_helpers.py`
- **test_parse_command_parts_with_args()** (2 connections) — `server/tests/unit/utils/test_command_parser_helpers.py`
- **Get help text for commands.      Args:         command_type: Specific command to** (1 connections) — `server/utils/command_helpers.py`
- **Unit tests for command_parser helper methods.  Tests the helper methods in Comma** (1 connections) — `server/tests/unit/utils/test_command_parser_helpers.py`
- **Test _create_command_object() handles 'l' alias.** (1 connections) — `server/tests/unit/utils/test_command_parser_helpers.py`
- **Test _create_command_object() handles 'g' alias.** (1 connections) — `server/tests/unit/utils/test_command_parser_helpers.py`
- **Test _create_command_object() handles 'w' alias.** (1 connections) — `server/tests/unit/utils/test_command_parser_helpers.py`
- **Test _create_command_object() raises error for unsupported command.** (1 connections) — `server/tests/unit/utils/test_command_parser_helpers.py`
- **Test _create_command_object() handles ValueError.** (1 connections) — `server/tests/unit/utils/test_command_parser_helpers.py`
- *... and 8 more nodes in this community*

## Relationships

- [[Command Helper Utilities]] (9 shared connections)
- [[Command Parser]] (4 shared connections)
- [[NPC Admin API]] (3 shared connections)
- [[Command Parser Tests]] (2 shared connections)
- [[Alias Expansion Logic]] (1 shared connections)

## Source Files

- `server/tests/unit/utils/test_command_helpers_functions.py`
- `server/tests/unit/utils/test_command_parser_helpers.py`
- `server/utils/command_helpers.py`

## Audit Trail

- EXTRACTED: 83 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
