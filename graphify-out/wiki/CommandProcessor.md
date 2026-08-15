# CommandProcessor

> 15 nodes

## Key Concepts

- **CommandProcessor** (15 connections) — `server/utils/command_processor.py`
- **command_processor()** (5 connections) — `server/tests/unit/utils/test_command_processor.py`
- **test_get_command_processor()** (4 connections) — `server/tests/unit/utils/test_command_processor.py`
- **test_process_command_string_pydantic_validation_error()** (3 connections) — `server/tests/unit/utils/test_command_processor.py`
- **.__init__()** (3 connections) — `server/utils/command_processor.py`
- **.get_command_help()** (2 connections) — `server/utils/command_processor.py`
- **.validate_command_safety()** (2 connections) — `server/utils/command_processor.py`
- **fixture** (1 connections)
- **Create a CommandProcessor instance.** (1 connections) — `server/tests/unit/utils/test_command_processor.py`
- **Test get_command_processor returns global instance.** (1 connections) — `server/tests/unit/utils/test_command_processor.py`
- **Test process_command_string handles Pydantic validation errors.** (1 connections) — `server/tests/unit/utils/test_command_processor.py`
- **Perform additional safety validation on command input. This provides an extra…** (1 connections) — `server/utils/command_processor.py`
- **Command processor that integrates Pydantic validation with existing command…** (1 connections) — `server/utils/command_processor.py`
- **Get help information for commands. Args: command_name: Specific command to get…** (1 connections) — `server/utils/command_processor.py`
- **Initialize the command processor.** (1 connections) — `server/utils/command_processor.py`

## Relationships

- [test_command_processor.py](test_command_processor.py.md) (4 shared connections)
- [get_logger](get_logger.md) (4 shared connections)
- [.extract_command_data](extract_command_data.md) (4 shared connections)
- [test_command_parser.py](test_command_parser.py.md) (2 shared connections)

## Source Files

- `server/tests/unit/utils/test_command_processor.py`
- `server/utils/command_processor.py`

## Audit Trail

- EXTRACTED: 23 (82%)
- INFERRED: 5 (18%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*