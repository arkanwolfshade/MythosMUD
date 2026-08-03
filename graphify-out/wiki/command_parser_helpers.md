# command parser helpers

> 20 nodes

## Key Concepts

- **test_command_parser_helpers.py** (24 connections) — `server/tests/unit/utils/test_command_parser_helpers.py`
- **test_normalize_command_removes_slash_prefix()** (2 connections) — `server/tests/unit/utils/test_command_parser_helpers.py`
- **test_normalize_command_no_slash()** (2 connections) — `server/tests/unit/utils/test_command_parser_helpers.py`
- **test_parse_command_parts_empty_raises()** (2 connections) — `server/tests/unit/utils/test_command_parser_helpers.py`
- **test_parse_command_parts_whitespace_only_raises()** (2 connections) — `server/tests/unit/utils/test_command_parser_helpers.py`
- **test_get_command_help_unknown_command()** (2 connections) — `server/tests/unit/utils/test_command_parser_helpers.py`
- **test_get_command_help_none()** (2 connections) — `server/tests/unit/utils/test_command_parser_helpers.py`
- **test_create_command_object_with_alias_l()** (2 connections) — `server/tests/unit/utils/test_command_parser_helpers.py`
- **test_create_command_object_pydantic_validation_error()** (2 connections) — `server/tests/unit/utils/test_command_parser_helpers.py`
- **test_create_command_object_value_error()** (2 connections) — `server/tests/unit/utils/test_command_parser_helpers.py`
- **Unit tests for command_parser helper methods.  Tests the helper methods in Comma** (1 connections) — `server/tests/unit/utils/test_command_parser_helpers.py`
- **Test _normalize_command() removes leading slash.** (1 connections) — `server/tests/unit/utils/test_command_parser_helpers.py`
- **Test _normalize_command() handles command without slash.** (1 connections) — `server/tests/unit/utils/test_command_parser_helpers.py`
- **Test _parse_command_parts() raises error for empty command.** (1 connections) — `server/tests/unit/utils/test_command_parser_helpers.py`
- **Test _parse_command_parts() raises error for whitespace-only.** (1 connections) — `server/tests/unit/utils/test_command_parser_helpers.py`
- **Test get_command_help() returns error for unknown command.** (1 connections) — `server/tests/unit/utils/test_command_parser_helpers.py`
- **Test get_command_help() returns general help when None.** (1 connections) — `server/tests/unit/utils/test_command_parser_helpers.py`
- **Test _create_command_object() handles 'l' alias.** (1 connections) — `server/tests/unit/utils/test_command_parser_helpers.py`
- **Test _create_command_object() handles PydanticValidationError.** (1 connections) — `server/tests/unit/utils/test_command_parser_helpers.py`
- **Test _create_command_object() handles ValueError.** (1 connections) — `server/tests/unit/utils/test_command_parser_helpers.py`

## Relationships

- [infrastructure persistence room](infrastructure_persistence_room.md) (6 shared connections)
- [room infrastructure persistence](room_infrastructure_persistence.md) (3 shared connections)
- [Database Config](Database_Config.md) (1 shared connections)
- [command inventory models](command_inventory_models.md) (1 shared connections)
- [infrastructure persistence core](infrastructure_persistence_core.md) (1 shared connections)
- [command factories create](command_factories_create.md) (1 shared connections)
- [player effects endpoints](player_effects_endpoints.md) (1 shared connections)

## Source Files

- `server/tests/unit/utils/test_command_parser_helpers.py`

## Audit Trail

- EXTRACTED: 52 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*