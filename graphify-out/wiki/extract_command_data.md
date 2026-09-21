# .extract_command_data

> 9 nodes

## Key Concepts

- **.extract_command_data()** (5 connections) — `server/utils/command_processor.py`
- **._extract_attributes()** (4 connections) — `server/utils/command_processor.py`
- **._is_combat_command()** (4 connections) — `server/utils/command_processor.py`
- **.process_command_string()** (4 connections) — `server/utils/command_processor.py`
- **Any** (3 connections)
- **Extract attributes from validated command using a mapping configuration. Args:…** (1 connections) — `server/utils/command_processor.py`
- **Check if a command type is a combat command. Args: command_type: The command…** (1 connections) — `server/utils/command_processor.py`
- **Extract command data from a validated Pydantic command object. This method…** (1 connections) — `server/utils/command_processor.py`
- **Process a raw command string through the new validation system. Args:…** (1 connections) — `server/utils/command_processor.py`

## Relationships

- [CommandProcessor](CommandProcessor.md) (4 shared connections)
- [command.py](command.py.md) (1 shared connections)
- [test_command_parser.py](test_command_parser.py.md) (1 shared connections)

## Source Files

- `server/utils/command_processor.py`

## Audit Trail

- EXTRACTED: 15 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*