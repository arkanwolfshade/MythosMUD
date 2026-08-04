# command parser rationale

> 143 nodes

## Key Concepts

- **test_command_parser.py** (45 connections) — `server/tests/unit/utils/test_command_parser.py`
- **test_command_parser_helpers.py** (24 connections) — `server/tests/unit/utils/test_command_parser_helpers.py`
- **parse_command()** (24 connections) — `server/utils/command_parser.py`
- **CommandParser** (19 connections) — `server/utils/command_parser.py`
- **test_command_parser_smoke.py** (8 connections) — `server/tests/unit/test_command_parser_smoke.py`
- **.parse_command()** (7 connections) — `server/utils/command_parser.py`
- **._create_command_object()** (7 connections) — `server/utils/command_parser.py`
- **Command** (4 connections)
- **._parse_command_parts()** (4 connections) — `server/utils/command_parser.py`
- **._invoke_create_method()** (4 connections) — `server/utils/command_parser.py`
- **test_parse_command_basic()** (3 connections) — `server/tests/unit/test_command_parser_smoke.py`
- **test_parse_command_with_args()** (3 connections) — `server/tests/unit/test_command_parser_smoke.py`
- **test_parse_command_with_pipes()** (3 connections) — `server/tests/unit/test_command_parser_smoke.py`
- **command_parser()** (3 connections) — `server/tests/unit/utils/test_command_parser.py`
- **test_parse_command_empty_string()** (3 connections) — `server/tests/unit/utils/test_command_parser.py`
- **test_parse_command_whitespace_only()** (3 connections) — `server/tests/unit/utils/test_command_parser.py`
- **test_parse_command_too_long()** (3 connections) — `server/tests/unit/utils/test_command_parser.py`
- **test_parse_command_unknown_command()** (3 connections) — `server/tests/unit/utils/test_command_parser.py`
- **test_parse_command_valid_look()** (3 connections) — `server/tests/unit/utils/test_command_parser.py`
- **test_parse_command_valid_go()** (3 connections) — `server/tests/unit/utils/test_command_parser.py`
- **test_parse_command_with_slash_prefix()** (3 connections) — `server/tests/unit/utils/test_command_parser.py`
- **test_parse_command_spawn_alias()** (3 connections) — `server/tests/unit/utils/test_command_parser.py`
- **test_parse_command_alias_l()** (3 connections) — `server/tests/unit/utils/test_command_parser.py`
- **test_parse_command_alias_g()** (3 connections) — `server/tests/unit/utils/test_command_parser.py`
- **test_create_command_object_pydantic_validation_error()** (3 connections) — `server/tests/unit/utils/test_command_parser.py`
- *... and 118 more nodes in this community*

## Relationships

- [Loot Generation](Loot_Generation.md) (12 shared connections)
- [command factories create](command_factories_create.md) (5 shared connections)
- [Database Access Layer](Database_Access_Layer.md) (3 shared connections)
- [command processor rationale](command_processor_rationale.md) (3 shared connections)
- [commands admin mute](commands_admin_mute.md) (1 shared connections)
- [combat services initialization](combat_services_initialization.md) (1 shared connections)

## Source Files

- `server/tests/unit/test_command_parser_smoke.py`
- `server/tests/unit/utils/test_command_parser.py`
- `server/tests/unit/utils/test_command_parser_helpers.py`
- `server/utils/command_parser.py`

## Audit Trail

- EXTRACTED: 359 (99%)
- INFERRED: 2 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*