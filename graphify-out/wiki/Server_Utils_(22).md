# Server Utils (22)

> 23 nodes

## Key Concepts

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
- **.validate_command_safety()** (2 connections) — `server/utils/command_processor.py`
- **.get_command_help()** (2 connections) — `server/utils/command_processor.py`
- **Create a CommandProcessor instance.** (1 connections) — `server/tests/unit/utils/test_command_processor.py`
- **Test process_command_string handles Pydantic validation errors.** (1 connections) — `server/tests/unit/utils/test_command_processor.py`
- **Test get_command_processor returns global instance.** (1 connections) — `server/tests/unit/utils/test_command_processor.py`
- **Command processor that integrates Pydantic validation with existing command infr** (1 connections) — `server/utils/command_processor.py`
- **Initialize the command processor.** (1 connections) — `server/utils/command_processor.py`
- **Process a raw command string through the new validation system.          Args:** (1 connections) — `server/utils/command_processor.py`
- **Extract attributes from validated command using a mapping configuration.** (1 connections) — `server/utils/command_processor.py`
- **Check if a command type is a combat command.          Args:             command_** (1 connections) — `server/utils/command_processor.py`
- **Extract command data from a validated Pydantic command object.          This met** (1 connections) — `server/utils/command_processor.py`
- **Perform additional safety validation on command input.          This provides an** (1 connections) — `server/utils/command_processor.py`
- **Get help information for commands.          Args:             command_name: Spec** (1 connections) — `server/utils/command_processor.py`

## Relationships

- [Server Utils (12)](Server_Utils_%2812%29.md) (4 shared connections)
- [Server Commands (5)](Server_Commands_%285%29.md) (3 shared connections)
- [Server Utils (21)](Server_Utils_%2821%29.md) (2 shared connections)
- [Server Commands](Server_Commands.md) (2 shared connections)
- [Server Models](Server_Models.md) (1 shared connections)

## Source Files

- `server/tests/unit/utils/test_command_processor.py`
- `server/utils/command_processor.py`

## Audit Trail

- EXTRACTED: 60 (94%)
- INFERRED: 4 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*