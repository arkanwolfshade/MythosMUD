# parse_command

> 32 nodes

## Key Concepts

- **parse_command()** (24 connections) — `server/utils/command_parser.py`
- **test_parse_command_basic()** (3 connections) — `server/tests/unit/test_command_parser_smoke.py`
- **test_parse_command_with_args()** (3 connections) — `server/tests/unit/test_command_parser_smoke.py`
- **test_parse_command_with_pipes()** (3 connections) — `server/tests/unit/test_command_parser_smoke.py`
- **test_parse_command_alias_g()** (3 connections) — `server/tests/unit/utils/test_command_parser.py`
- **test_parse_command_alias_l()** (3 connections) — `server/tests/unit/utils/test_command_parser.py`
- **test_parse_command_empty_string()** (3 connections) — `server/tests/unit/utils/test_command_parser.py`
- **test_parse_command_global_function()** (3 connections) — `server/tests/unit/utils/test_command_parser.py`
- **test_parse_command_global_function_with_args()** (3 connections) — `server/tests/unit/utils/test_command_parser.py`
- **test_parse_command_spawn_alias()** (3 connections) — `server/tests/unit/utils/test_command_parser.py`
- **test_parse_command_too_long()** (3 connections) — `server/tests/unit/utils/test_command_parser.py`
- **test_parse_command_unknown_command()** (3 connections) — `server/tests/unit/utils/test_command_parser.py`
- **test_parse_command_valid_go()** (3 connections) — `server/tests/unit/utils/test_command_parser.py`
- **test_parse_command_valid_look()** (3 connections) — `server/tests/unit/utils/test_command_parser.py`
- **test_parse_command_whitespace_only()** (3 connections) — `server/tests/unit/utils/test_command_parser.py`
- **test_parse_command_with_slash_prefix()** (3 connections) — `server/tests/unit/utils/test_command_parser.py`
- **Test basic command parsing.** (1 connections) — `server/tests/unit/test_command_parser_smoke.py`
- **Test command parsing with arguments.** (1 connections) — `server/tests/unit/test_command_parser_smoke.py`
- **Test command parsing with pipes.** (1 connections) — `server/tests/unit/test_command_parser_smoke.py`
- **Test parse_command handles 'g' alias for global/system.** (1 connections) — `server/tests/unit/utils/test_command_parser.py`
- **Test parse_command raises error for empty string.** (1 connections) — `server/tests/unit/utils/test_command_parser.py`
- **Test parse_command raises error for whitespace-only string.** (1 connections) — `server/tests/unit/utils/test_command_parser.py`
- **Test parse_command global function uses global parser.** (1 connections) — `server/tests/unit/utils/test_command_parser.py`
- **Test parse_command global function handles arguments.** (1 connections) — `server/tests/unit/utils/test_command_parser.py`
- **Test parse_command raises error for command exceeding max length.** (1 connections) — `server/tests/unit/utils/test_command_parser.py`
- *... and 7 more nodes in this community*

## Relationships

- [test_command_parser.py](test_command_parser.py.md) (13 shared connections)
- [BaseCommand](BaseCommand.md) (4 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [CommandService](CommandService.md) (1 shared connections)
- [CommandProcessor](CommandProcessor.md) (1 shared connections)
- [AliasStorage](AliasStorage.md) (1 shared connections)
- [CommandParser](CommandParser.md) (1 shared connections)

## Source Files

- `server/tests/unit/test_command_parser_smoke.py`
- `server/tests/unit/utils/test_command_parser.py`
- `server/utils/command_parser.py`

## Audit Trail

- EXTRACTED: 54 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*