# server tests unit utils test

> 161 nodes

## Key Concepts

- **CommandFactory** (83 connections) — `server/utils/command_factories.py`
- **CommandParser** (19 connections) — `server/utils/command_parser.py`
- **._create_command_object()** (7 connections) — `server/utils/command_parser.py`
- **.parse_command()** (7 connections) — `server/utils/command_parser.py`
- **_build_command_factory()** (6 connections) — `server/utils/command_parser.py`
- **command_parser()** (4 connections) — `server/tests/unit/utils/test_command_parser_helpers.py`
- **_build_command_factory_part1()** (4 connections) — `server/utils/command_parser.py`
- **_build_command_factory_part2()** (4 connections) — `server/utils/command_parser.py`
- **._invoke_create_method()** (4 connections) — `server/utils/command_parser.py`
- **._parse_command_parts()** (4 connections) — `server/utils/command_parser.py`
- **Command** (4 connections)
- **.create_add_admin_command()** (3 connections) — `server/utils/command_factories.py`
- **.create_admin_command()** (3 connections) — `server/utils/command_factories.py`
- **.create_alias_command()** (3 connections) — `server/utils/command_factories.py`
- **.create_aliases_command()** (3 connections) — `server/utils/command_factories.py`
- **.create_attack_command()** (3 connections) — `server/utils/command_factories.py`
- **.create_cast_command()** (3 connections) — `server/utils/command_factories.py`
- **.create_channel_command()** (3 connections) — `server/utils/command_factories.py`
- **.create_drop_command()** (3 connections) — `server/utils/command_factories.py`
- **.create_emote_command()** (3 connections) — `server/utils/command_factories.py`
- **.create_equip_command()** (3 connections) — `server/utils/command_factories.py`
- **.create_flee_command()** (3 connections) — `server/utils/command_factories.py`
- **.create_follow_command()** (3 connections) — `server/utils/command_factories.py`
- **.create_following_command()** (3 connections) — `server/utils/command_factories.py`
- **.create_get_command()** (3 connections) — `server/utils/command_factories.py`
- *... and 136 more nodes in this community*

## Relationships

- [server models command](server_models_command.md) (65 shared connections)
- [server tests unit utils test](server_tests_unit_utils_test.md) (17 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (9 shared connections)
- [server exceptions rationale 179](server_exceptions_rationale_179.md) (1 shared connections)
- [server tests unit structured logging](server_tests_unit_structured_logging.md) (1 shared connections)

## Source Files

- `server/tests/unit/utils/test_command_parser_helpers.py`
- `server/utils/command_factories.py`
- `server/utils/command_parser.py`
- `server/utils/command_processor.py`

## Audit Trail

- EXTRACTED: 248 (94%)
- INFERRED: 16 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*