# Command Processor Tests

> 83 nodes · cohesion 0.03

## Key Concepts

- **test_command_processor.py** (39 connections) — `server/tests/unit/utils/test_command_processor.py`
- **CommandProcessor** (15 connections) — `server/utils/command_processor.py`
- **get_command_processor()** (7 connections) — `server/utils/command_processor.py`
- **.extract_command_data()** (5 connections) — `server/utils/command_processor.py`
- **command_processor()** (4 connections) — `server/tests/unit/utils/test_command_processor.py`
- **test_get_command_processor()** (4 connections) — `server/tests/unit/utils/test_command_processor.py`
- **._extract_attributes()** (4 connections) — `server/utils/command_processor.py`
- **._is_combat_command()** (4 connections) — `server/utils/command_processor.py`
- **.process_command_string()** (4 connections) — `server/utils/command_processor.py`
- **test_get_command_help_attribute_error()** (3 connections) — `server/tests/unit/utils/test_command_processor.py`
- **test_process_command_string_attribute_error()** (3 connections) — `server/tests/unit/utils/test_command_processor.py`
- **test_process_command_string_pydantic_validation_error()** (3 connections) — `server/tests/unit/utils/test_command_processor.py`
- **.__init__()** (3 connections) — `server/utils/command_processor.py`
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
- *... and 58 more nodes in this community*

## Relationships

- [Admin Command Models](Admin_Command_Models.md) (8 shared connections)
- [Api Player Respawn](Api_Player_Respawn.md) (2 shared connections)
- [Connection Disconnection Cleanup](Connection_Disconnection_Cleanup.md) (2 shared connections)
- [Players API Endpoints](Players_API_Endpoints.md) (1 shared connections)
- [Realtime Message Formatters](Realtime_Message_Formatters.md) (1 shared connections)

## Source Files

- `server/tests/unit/utils/test_command_processor.py`
- `server/utils/command_processor.py`

## Audit Trail

- EXTRACTED: 191 (96%)
- INFERRED: 7 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*