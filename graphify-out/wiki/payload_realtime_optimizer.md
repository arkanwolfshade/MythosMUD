# payload realtime optimizer

> 132 nodes

## Key Concepts

- **test_command_parser.py** (45 connections) — `server/tests/unit/utils/test_command_parser.py`
- **parse_command()** (24 connections) — `server/utils/command_parser.py`
- **CommandParser** (19 connections) — `server/utils/command_parser.py`
- **CommandProcessor** (15 connections) — `server/utils/command_processor.py`
- **command_processor.py** (13 connections) — `server/utils/command_processor.py`
- **test_command_parser_smoke.py** (8 connections) — `server/tests/unit/test_command_parser_smoke.py`
- **.parse_command()** (7 connections) — `server/utils/command_parser.py`
- **._create_command_object()** (7 connections) — `server/utils/command_parser.py`
- **get_command_processor()** (7 connections) — `server/utils/command_processor.py`
- **.extract_command_data()** (5 connections) — `server/utils/command_processor.py`
- **command_processor()** (4 connections) — `server/tests/unit/utils/test_command_processor.py`
- **test_get_command_processor()** (4 connections) — `server/tests/unit/utils/test_command_processor.py`
- **Command** (4 connections)
- **._parse_command_parts()** (4 connections) — `server/utils/command_parser.py`
- **._invoke_create_method()** (4 connections) — `server/utils/command_parser.py`
- **.process_command_string()** (4 connections) — `server/utils/command_processor.py`
- **._extract_attributes()** (4 connections) — `server/utils/command_processor.py`
- **._is_combat_command()** (4 connections) — `server/utils/command_processor.py`
- **test_parse_command_basic()** (3 connections) — `server/tests/unit/test_command_parser_smoke.py`
- **test_parse_command_with_args()** (3 connections) — `server/tests/unit/test_command_parser_smoke.py`
- **test_parse_command_with_pipes()** (3 connections) — `server/tests/unit/test_command_parser_smoke.py`
- **command_parser()** (3 connections) — `server/tests/unit/utils/test_command_parser.py`
- **test_parse_command_empty_string()** (3 connections) — `server/tests/unit/utils/test_command_parser.py`
- **test_parse_command_whitespace_only()** (3 connections) — `server/tests/unit/utils/test_command_parser.py`
- **test_parse_command_too_long()** (3 connections) — `server/tests/unit/utils/test_command_parser.py`
- *... and 107 more nodes in this community*

## Relationships

- [command inventory factories](command_inventory_factories.md) (7 shared connections)
- [command processor rationale](command_processor_rationale.md) (7 shared connections)
- [dialogue definition persistence](dialogue_definition_persistence.md) (5 shared connections)
- [spell game magic](spell_game_magic.md) (3 shared connections)
- [Error Handling Core](Error_Handling_Core.md) (2 shared connections)
- [command inventory models](command_inventory_models.md) (2 shared connections)
- [schedule services service](schedule_services_service.md) (2 shared connections)
- [combat attack handler](combat_attack_handler.md) (2 shared connections)
- [logging examples fastapi](logging_examples_fastapi.md) (2 shared connections)
- [character creation service](character_creation_service.md) (1 shared connections)
- [combat services initialization](combat_services_initialization.md) (1 shared connections)

## Source Files

- `server/tests/unit/test_command_parser_smoke.py`
- `server/tests/unit/utils/test_command_parser.py`
- `server/tests/unit/utils/test_command_parser_helpers.py`
- `server/tests/unit/utils/test_command_processor.py`
- `server/utils/command_parser.py`
- `server/utils/command_processor.py`

## Audit Trail

- EXTRACTED: 361 (98%)
- INFERRED: 7 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*