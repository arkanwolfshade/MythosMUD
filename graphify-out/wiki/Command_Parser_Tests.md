# Command Parser Tests

> 66 nodes · cohesion 0.03

## Key Concepts

- **test_command_parser.py** (43 connections) — `server/tests/unit/utils/test_command_parser.py`
- **Test _create_command_object handles ValueError.** (4 connections) — `server/tests/unit/utils/test_command_parser.py`
- **test_create_command_object_re_raises_mythos_validation_error()** (4 connections) — `server/tests/unit/utils/test_command_parser.py`
- **Test _create_command_object handles 'w' alias.** (3 connections) — `server/tests/unit/utils/test_command_parser.py`
- **Test parse_command raises error for empty string.** (3 connections) — `server/tests/unit/utils/test_command_parser.py`
- **test_parse_command_global_function()** (3 connections) — `server/tests/unit/utils/test_command_parser.py`
- **test_parse_command_global_function_with_args()** (3 connections) — `server/tests/unit/utils/test_command_parser.py`
- **test_get_command_help_none()** (2 connections) — `server/tests/unit/utils/test_command_parser_helpers.py`
- **test_parse_command_parts_empty_raises()** (2 connections) — `server/tests/unit/utils/test_command_parser_helpers.py`
- **Test _normalize_command removes leading slash.** (2 connections) — `server/tests/unit/utils/test_command_parser.py`
- **Test get_command_help returns general help when command_name is None.** (2 connections) — `server/tests/unit/utils/test_command_parser.py`
- **test_command_parser_initialization()** (2 connections) — `server/tests/unit/utils/test_command_parser.py`
- **test_create_command_object_attribute_error()** (2 connections) — `server/tests/unit/utils/test_command_parser.py`
- **test_create_command_object_handles_alias_g()** (2 connections) — `server/tests/unit/utils/test_command_parser.py`
- **test_create_command_object_handles_alias_l()** (2 connections) — `server/tests/unit/utils/test_command_parser.py`
- **test_create_command_object_handles_alias_w()** (2 connections) — `server/tests/unit/utils/test_command_parser.py`
- **test_create_command_object_key_error()** (2 connections) — `server/tests/unit/utils/test_command_parser.py`
- **test_create_command_object_runtime_error()** (2 connections) — `server/tests/unit/utils/test_command_parser.py`
- **test_create_command_object_success()** (2 connections) — `server/tests/unit/utils/test_command_parser.py`
- **test_create_command_object_type_error()** (2 connections) — `server/tests/unit/utils/test_command_parser.py`
- **test_create_command_object_unsupported_command()** (2 connections) — `server/tests/unit/utils/test_command_parser.py`
- **test_create_command_object_value_error()** (2 connections) — `server/tests/unit/utils/test_command_parser.py`
- **test_get_command_help_case_insensitive()** (2 connections) — `server/tests/unit/utils/test_command_parser.py`
- **test_get_command_help_none()** (2 connections) — `server/tests/unit/utils/test_command_parser.py`
- **test_get_command_help_specific()** (2 connections) — `server/tests/unit/utils/test_command_parser.py`
- *... and 41 more nodes in this community*

## Relationships

- [[Command Parser]] (4 shared connections)
- [[NPC Admin API]] (3 shared connections)
- [[Alias Expansion Logic]] (3 shared connections)
- [[Command Parser Helpers]] (2 shared connections)
- [[Command Service Tests]] (1 shared connections)
- [[Command Input Utilities]] (1 shared connections)
- [[Pydantic Error Handlers]] (1 shared connections)

## Source Files

- `server/tests/unit/utils/test_command_parser.py`
- `server/tests/unit/utils/test_command_parser_helpers.py`

## Audit Trail

- EXTRACTED: 156 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
