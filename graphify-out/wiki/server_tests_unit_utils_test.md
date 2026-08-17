# server tests unit utils test

> 80 nodes

## Key Concepts

- **test_command_processor.py** (41 connections) — `server/tests/unit/utils/test_command_processor.py`
- **CommandProcessor** (15 connections) — `server/utils/command_processor.py`
- **command_processor.py** (14 connections) — `server/utils/command_processor.py`
- **get_command_processor()** (7 connections) — `server/utils/command_processor.py`
- **command_processor()** (5 connections) — `server/tests/unit/utils/test_command_processor.py`
- **.extract_command_data()** (5 connections) — `server/utils/command_processor.py`
- **test_get_command_processor()** (4 connections) — `server/tests/unit/utils/test_command_processor.py`
- **._extract_attributes()** (4 connections) — `server/utils/command_processor.py`
- **._is_combat_command()** (4 connections) — `server/utils/command_processor.py`
- **.process_command_string()** (4 connections) — `server/utils/command_processor.py`
- **test_process_command_string_pydantic_validation_error()** (3 connections) — `server/tests/unit/utils/test_command_processor.py`
- **Any** (3 connections)
- **test_command_processor_initialization()** (2 connections) — `server/tests/unit/utils/test_command_processor.py`
- **test_extract_attributes_basic()** (2 connections) — `server/tests/unit/utils/test_command_processor.py`
- **test_extract_attributes_missing_attribute()** (2 connections) — `server/tests/unit/utils/test_command_processor.py`
- **test_extract_command_data_basic()** (2 connections) — `server/tests/unit/utils/test_command_processor.py`
- **test_extract_command_data_combat_target()** (2 connections) — `server/tests/unit/utils/test_command_processor.py`
- **test_extract_command_data_multiple_attributes()** (2 connections) — `server/tests/unit/utils/test_command_processor.py`
- **test_extract_command_data_player_name()** (2 connections) — `server/tests/unit/utils/test_command_processor.py`
- **test_extract_command_data_with_target()** (2 connections) — `server/tests/unit/utils/test_command_processor.py`
- **test_get_command_help_key_error()** (2 connections) — `server/tests/unit/utils/test_command_processor.py`
- **test_get_command_help_none()** (2 connections) — `server/tests/unit/utils/test_command_processor.py`
- **test_get_command_help_runtime_error()** (2 connections) — `server/tests/unit/utils/test_command_processor.py`
- **test_get_command_help_success()** (2 connections) — `server/tests/unit/utils/test_command_processor.py`
- **test_get_command_help_type_error()** (2 connections) — `server/tests/unit/utils/test_command_processor.py`
- *... and 55 more nodes in this community*

## Relationships

- [server tests unit utils test](server_tests_unit_utils_test.md) (5 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (5 shared connections)
- [server models command](server_models_command.md) (3 shared connections)
- [server command handler processing](server_command_handler_processing.md) (2 shared connections)
- [server exceptions rationale 179](server_exceptions_rationale_179.md) (2 shared connections)
- [claude rules fastapi](claude_rules_fastapi.md) (2 shared connections)
- [attributeerror](attributeerror.md) (2 shared connections)
- [characterinfo](characterinfo.md) (1 shared connections)
- [mythosvalidationerror](mythosvalidationerror.md) (1 shared connections)

## Source Files

- `server/tests/unit/utils/test_command_processor.py`
- `server/utils/command_processor.py`

## Audit Trail

- EXTRACTED: 109 (96%)
- INFERRED: 5 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*