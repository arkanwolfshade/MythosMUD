# Assist Wiring Tests

> 189 nodes

## Key Concepts

- **test_command_parser.py** (51 connections) — `server/tests/unit/utils/test_command_parser.py`
- **parse_command()** (38 connections) — `server/utils/command_parser.py`
- **test_command_processor.py** (32 connections) — `server/tests/unit/utils/test_command_processor.py`
- **test_assist_wiring.py** (25 connections) — `server/tests/unit/commands/test_assist_wiring.py`
- **test_protect_wiring.py** (24 connections) — `server/tests/unit/commands/test_protect_wiring.py`
- **CommandParser** (22 connections) — `server/utils/command_parser.py`
- **CommandProcessor** (20 connections) — `server/utils/command_processor.py`
- **command_processor.py** (16 connections) — `server/utils/command_processor.py`
- **._create_command_object()** (7 connections) — `server/utils/command_parser.py`
- **.parse_command()** (7 connections) — `server/utils/command_parser.py`
- **get_command_processor()** (7 connections) — `server/utils/command_processor.py`
- **command_processor()** (5 connections) — `server/tests/unit/utils/test_command_processor.py`
- **.extract_command_data()** (5 connections) — `server/utils/command_processor.py`
- **test_the_topic_survives_extraction_from_the_parsed_command()** (4 connections) — `server/tests/unit/commands/test_help_commands.py`
- **command_parser()** (4 connections) — `server/tests/unit/utils/test_command_parser.py`
- **test_create_command_object_pydantic_validation_error()** (4 connections) — `server/tests/unit/utils/test_command_parser.py`
- **test_parse_command_empty_string()** (4 connections) — `server/tests/unit/utils/test_command_parser.py`
- **test_parse_command_too_long()** (4 connections) — `server/tests/unit/utils/test_command_parser.py`
- **test_parse_command_unknown_command()** (4 connections) — `server/tests/unit/utils/test_command_parser.py`
- **test_parse_command_use_and_its_aliases()** (4 connections) — `server/tests/unit/utils/test_command_parser.py`
- **test_parse_command_use_requires_an_item()** (4 connections) — `server/tests/unit/utils/test_command_parser.py`
- **test_parse_command_whitespace_only()** (4 connections) — `server/tests/unit/utils/test_command_parser.py`
- **test_get_command_processor()** (4 connections) — `server/tests/unit/utils/test_command_processor.py`
- **._invoke_create_method()** (4 connections) — `server/utils/command_parser.py`
- **._parse_command_parts()** (4 connections) — `server/utils/command_parser.py`
- *... and 164 more nodes in this community*

## Relationships

- [Schema Validation & Channels](Schema_Validation_&_Channels.md) (24 shared connections)
- [Channel Commands](Channel_Commands.md) (8 shared connections)
- [Event Bus & Persistence Core](Event_Bus_&_Persistence_Core.md) (6 shared connections)
- [Community 262](Community_262.md) (6 shared connections)
- [Community 415](Community_415.md) (6 shared connections)
- [Community 179](Community_179.md) (6 shared connections)
- [Community 49](Community_49.md) (5 shared connections)
- [Inventory Commands](Inventory_Commands.md) (5 shared connections)
- [Community 263](Community_263.md) (5 shared connections)
- [Community 751](Community_751.md) (4 shared connections)
- [Community 59](Community_59.md) (4 shared connections)
- [Community 42](Community_42.md) (3 shared connections)

## Source Files

- `server/tests/unit/commands/test_assist_wiring.py`
- `server/tests/unit/commands/test_help_commands.py`
- `server/tests/unit/commands/test_protect_wiring.py`
- `server/tests/unit/utils/test_command_parser.py`
- `server/tests/unit/utils/test_command_processor.py`
- `server/utils/command_parser.py`
- `server/utils/command_processor.py`

## Audit Trail

- EXTRACTED: 315 (94%)
- INFERRED: 21 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*