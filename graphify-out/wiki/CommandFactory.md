# CommandFactory

> 229 nodes · cohesion 0.01

## Key Concepts

- **command_parser.py** (52 connections) — `server/utils/command_parser.py`
- **test_command_parser.py** (51 connections) — `server/tests/unit/utils/test_command_parser.py`
- **parse_command()** (38 connections) — `server/utils/command_parser.py`
- **test_command_processor.py** (32 connections) — `server/tests/unit/utils/test_command_processor.py`
- **test_assist_wiring.py** (25 connections) — `server/tests/unit/commands/test_assist_wiring.py`
- **test_protect_wiring.py** (24 connections) — `server/tests/unit/commands/test_protect_wiring.py`
- **CommandParser** (22 connections) — `server/utils/command_parser.py`
- **test_command_parser_helpers.py** (21 connections) — `server/tests/unit/utils/test_command_parser_helpers.py`
- **CommandProcessor** (20 connections) — `server/utils/command_processor.py`
- **command_processor.py** (16 connections) — `server/utils/command_processor.py`
- **._create_command_object()** (7 connections) — `server/utils/command_parser.py`
- **.parse_command()** (7 connections) — `server/utils/command_parser.py`
- **get_command_processor()** (7 connections) — `server/utils/command_processor.py`
- **command_processor()** (5 connections) — `server/tests/unit/utils/test_command_processor.py`
- **.extract_command_data()** (5 connections) — `server/utils/command_processor.py`
- **test_the_combat_handler_exposes_the_party_service_it_was_given()** (4 connections) — `server/tests/unit/commands/test_assist_wiring.py`
- **test_the_topic_survives_extraction_from_the_parsed_command()** (4 connections) — `server/tests/unit/commands/test_help_commands.py`
- **command_parser()** (4 connections) — `server/tests/unit/utils/test_command_parser.py`
- **command_parser()** (4 connections) — `server/tests/unit/utils/test_command_parser_helpers.py`
- **test_create_command_object_value_error()** (4 connections) — `server/tests/unit/utils/test_command_parser_helpers.py`
- **test_create_command_object_pydantic_validation_error()** (4 connections) — `server/tests/unit/utils/test_command_parser.py`
- **test_parse_command_empty_string()** (4 connections) — `server/tests/unit/utils/test_command_parser.py`
- **test_parse_command_too_long()** (4 connections) — `server/tests/unit/utils/test_command_parser.py`
- **test_parse_command_unknown_command()** (4 connections) — `server/tests/unit/utils/test_command_parser.py`
- **test_parse_command_use_and_its_aliases()** (4 connections) — `server/tests/unit/utils/test_command_parser.py`
- *... and 204 more nodes in this community*

## Relationships

- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (29 shared connections)
- [command_parser.py](command_parser.py.md) (14 shared connections)
- [ContainerComponent](ContainerComponent.md) (8 shared connections)
- [MemoryMonitor](MemoryMonitor.md) (6 shared connections)
- [lifespan_startup.py](lifespan_startup.py.md) (6 shared connections)
- [Room](Room.md) (6 shared connections)
- [AttributeError](AttributeError.md) (6 shared connections)
- [NPCCombatIntegration](NPCCombatIntegration.md) (6 shared connections)
- [Communities (10 total, 2 thin omitted)](Communities_10_total,_2_thin_omitted.md) (5 shared connections)
- [SecureBaseModel](SecureBaseModel.md) (5 shared connections)
- [corpse_service](corpse_service.md) (5 shared connections)
- [HeaderBar.tsx](HeaderBar.tsx.md) (4 shared connections)

## Source Files

- `server/tests/unit/commands/test_assist_wiring.py`
- `server/tests/unit/commands/test_help_commands.py`
- `server/tests/unit/commands/test_protect_wiring.py`
- `server/tests/unit/utils/test_command_parser.py`
- `server/tests/unit/utils/test_command_parser_helpers.py`
- `server/tests/unit/utils/test_command_processor.py`
- `server/utils/command_parser.py`
- `server/utils/command_processor.py`

## Audit Trail

- EXTRACTED: 400 (93%)
- INFERRED: 32 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*