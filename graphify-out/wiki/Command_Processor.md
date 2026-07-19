# Command Processor

> 18 nodes · cohesion 0.14

## Key Concepts

- **CommandProcessor** (13 connections) — `server/utils/command_processor.py`
- **.extract_command_data()** (5 connections) — `server/utils/command_processor.py`
- **Any** (4 connections) — `server/utils/command_processor.py`
- **._extract_attributes()** (4 connections) — `server/utils/command_processor.py`
- **._is_combat_command()** (4 connections) — `server/utils/command_processor.py`
- **.process_command_string()** (4 connections) — `server/utils/command_processor.py`
- **.__init__()** (3 connections) — `server/utils/command_processor.py`
- **CommandType** (2 connections) — `server/utils/command_processor.py`
- **.get_command_help()** (2 connections) — `server/utils/command_processor.py`
- **.validate_command_safety()** (2 connections) — `server/utils/command_processor.py`
- **Extract attributes from validated command using a mapping configuration.** (1 connections) — `server/utils/command_processor.py`
- **Check if a command type is a combat command.          Args:             command_** (1 connections) — `server/utils/command_processor.py`
- **Extract command data from a validated Pydantic command object.          This met** (1 connections) — `server/utils/command_processor.py`
- **Perform additional safety validation on command input.          This provides an** (1 connections) — `server/utils/command_processor.py`
- **Command processor that integrates Pydantic validation with existing command infr** (1 connections) — `server/utils/command_processor.py`
- **Get help information for commands.          Args:             command_name: Spec** (1 connections) — `server/utils/command_processor.py`
- **Initialize the command processor.** (1 connections) — `server/utils/command_processor.py`
- **Process a raw command string through the new validation system.          Args:** (1 connections) — `server/utils/command_processor.py`

## Relationships

- [[Command Parser]] (4 shared connections)
- [[Alias Expansion Logic]] (3 shared connections)
- [[Command Processor Tests]] (1 shared connections)
- [[Command Processor]] (1 shared connections)

## Source Files

- `server/utils/command_processor.py`

## Audit Trail

- EXTRACTED: 47 (92%)
- INFERRED: 4 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
