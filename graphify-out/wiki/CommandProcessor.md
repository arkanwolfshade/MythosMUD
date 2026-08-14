# CommandProcessor

> 19 nodes

## Key Concepts

- **CommandProcessor** (14 connections) — `server/utils/command_processor.py`
- **.extract_command_data()** (5 connections) — `server/utils/command_processor.py`
- **._extract_attributes()** (4 connections) — `server/utils/command_processor.py`
- **._is_combat_command()** (4 connections) — `server/utils/command_processor.py`
- **.process_command_string()** (4 connections) — `server/utils/command_processor.py`
- **test_process_command_string_pydantic_validation_error()** (3 connections) — `server/tests/unit/utils/test_command_processor.py`
- **.__init__()** (3 connections) — `server/utils/command_processor.py`
- **Any** (3 connections)
- **.get_command_help()** (2 connections) — `server/utils/command_processor.py`
- **.validate_command_safety()** (2 connections) — `server/utils/command_processor.py`
- **Test process_command_string handles Pydantic validation errors.** (1 connections) — `server/tests/unit/utils/test_command_processor.py`
- **Extract attributes from validated command using a mapping configuration. Args:…** (1 connections) — `server/utils/command_processor.py`
- **Check if a command type is a combat command. Args: command_type: The command…** (1 connections) — `server/utils/command_processor.py`
- **Extract command data from a validated Pydantic command object. This method…** (1 connections) — `server/utils/command_processor.py`
- **Perform additional safety validation on command input. This provides an extra…** (1 connections) — `server/utils/command_processor.py`
- **Command processor that integrates Pydantic validation with existing command…** (1 connections) — `server/utils/command_processor.py`
- **Get help information for commands. Args: command_name: Specific command to get…** (1 connections) — `server/utils/command_processor.py`
- **Initialize the command processor.** (1 connections) — `server/utils/command_processor.py`
- **Process a raw command string through the new validation system. Args:…** (1 connections) — `server/utils/command_processor.py`

## Relationships

- [test_command_processor.py](test_command_processor.py.md) (3 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [CommandParser](CommandParser.md) (2 shared connections)
- [BaseCommand](BaseCommand.md) (1 shared connections)
- [parse_command](parse_command.md) (1 shared connections)

## Source Files

- `server/tests/unit/utils/test_command_processor.py`
- `server/utils/command_processor.py`

## Audit Trail

- EXTRACTED: 30 (97%)
- INFERRED: 1 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*