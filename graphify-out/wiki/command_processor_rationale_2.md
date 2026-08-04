# command processor rationale

> 77 nodes

## Key Concepts

- **test_command_processor.py** (39 connections) — `server/tests/unit/utils/test_command_processor.py`
- **CommandProcessor** (15 connections) — `server/utils/command_processor.py`
- **.extract_command_data()** (5 connections) — `server/utils/command_processor.py`
- **command_processor()** (4 connections) — `server/tests/unit/utils/test_command_processor.py`
- **test_get_command_processor()** (4 connections) — `server/tests/unit/utils/test_command_processor.py`
- **.process_command_string()** (4 connections) — `server/utils/command_processor.py`
- **._extract_attributes()** (4 connections) — `server/utils/command_processor.py`
- **._is_combat_command()** (4 connections) — `server/utils/command_processor.py`
- **test_process_command_string_pydantic_validation_error()** (3 connections) — `server/tests/unit/utils/test_command_processor.py`
- **.__init__()** (3 connections) — `server/utils/command_processor.py`
- **Any** (3 connections)
- **test_command_processor_initialization()** (2 connections) — `server/tests/unit/utils/test_command_processor.py`
- **test_process_command_string_success()** (2 connections) — `server/tests/unit/utils/test_command_processor.py`
- **test_process_command_string_value_error()** (2 connections) — `server/tests/unit/utils/test_command_processor.py`
- **test_process_command_string_type_error()** (2 connections) — `server/tests/unit/utils/test_command_processor.py`
- **test_process_command_string_key_error()** (2 connections) — `server/tests/unit/utils/test_command_processor.py`
- **test_process_command_string_runtime_error()** (2 connections) — `server/tests/unit/utils/test_command_processor.py`
- **test_extract_attributes_basic()** (2 connections) — `server/tests/unit/utils/test_command_processor.py`
- **test_extract_attributes_missing_attribute()** (2 connections) — `server/tests/unit/utils/test_command_processor.py`
- **test_is_combat_command_attack()** (2 connections) — `server/tests/unit/utils/test_command_processor.py`
- **test_is_combat_command_punch()** (2 connections) — `server/tests/unit/utils/test_command_processor.py`
- **test_is_combat_command_kick()** (2 connections) — `server/tests/unit/utils/test_command_processor.py`
- **test_is_combat_command_strike()** (2 connections) — `server/tests/unit/utils/test_command_processor.py`
- **test_is_combat_command_non_combat()** (2 connections) — `server/tests/unit/utils/test_command_processor.py`
- **test_extract_command_data_basic()** (2 connections) — `server/tests/unit/utils/test_command_processor.py`
- *... and 52 more nodes in this community*

## Relationships

- [Loot Generation](Loot_Generation.md) (7 shared connections)
- [command parser rationale](command_parser_rationale.md) (3 shared connections)
- [Database Access Layer](Database_Access_Layer.md) (2 shared connections)
- [command factories create](command_factories_create.md) (2 shared connections)
- [websocket helpers realtime](websocket_helpers_realtime.md) (2 shared connections)

## Source Files

- `server/tests/unit/utils/test_command_processor.py`
- `server/utils/command_processor.py`

## Audit Trail

- EXTRACTED: 178 (98%)
- INFERRED: 4 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*