# test room sync service

> 133 nodes

## Key Concepts

- **test_command_parser.py** (45 connections) — `server/tests/unit/utils/test_command_parser.py`
- **test_command_parser_helpers.py** (24 connections) — `server/tests/unit/utils/test_command_parser_helpers.py`
- **CommandParser** (19 connections) — `server/utils/command_parser.py`
- **.parse_command()** (7 connections) — `server/utils/command_parser.py`
- **._create_command_object()** (7 connections) — `server/utils/command_parser.py`
- **Command** (4 connections)
- **._parse_command_parts()** (4 connections) — `server/utils/command_parser.py`
- **._invoke_create_method()** (4 connections) — `server/utils/command_parser.py`
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
- **test_parse_command_global_function()** (3 connections) — `server/tests/unit/utils/test_command_parser.py`
- **test_parse_command_global_function_with_args()** (3 connections) — `server/tests/unit/utils/test_command_parser.py`
- **command_parser()** (3 connections) — `server/tests/unit/utils/test_command_parser_helpers.py`
- **._normalize_command()** (3 connections) — `server/utils/command_parser.py`
- **._resolve_command_alias()** (3 connections) — `server/utils/command_parser.py`
- *... and 108 more nodes in this community*

## Relationships

- [Spell Targeting](Spell_Targeting.md) (24 shared connections)
- [real time](real_time.md) (2 shared connections)
- [.initialize()](initialize%28%29.md) (2 shared connections)
- [test command processor](test_command_processor.md) (2 shared connections)
- [NATS](NATS.md) (1 shared connections)

## Source Files

- `server/tests/unit/utils/test_command_parser.py`
- `server/tests/unit/utils/test_command_parser_helpers.py`
- `server/utils/command_parser.py`

## Audit Trail

- EXTRACTED: 313 (99%)
- INFERRED: 2 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*