# Schedule Service Loader

> 34 nodes

## Key Concepts

- **parse_command()** (24 connections) — `server/utils/command_parser.py`
- **test_command_parser_smoke.py** (8 connections) — `server/tests/unit/test_command_parser_smoke.py`
- **test_parse_command_basic()** (3 connections) — `server/tests/unit/test_command_parser_smoke.py`
- **test_parse_command_with_args()** (3 connections) — `server/tests/unit/test_command_parser_smoke.py`
- **test_parse_command_with_pipes()** (3 connections) — `server/tests/unit/test_command_parser_smoke.py`
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
- **test_parse_command_global_function()** (3 connections) — `server/tests/unit/utils/test_command_parser.py`
- **test_parse_command_global_function_with_args()** (3 connections) — `server/tests/unit/utils/test_command_parser.py`
- **Smoke test for command parser.** (1 connections) — `server/tests/unit/test_command_parser_smoke.py`
- **Test basic command parsing.** (1 connections) — `server/tests/unit/test_command_parser_smoke.py`
- **Test command parsing with arguments.** (1 connections) — `server/tests/unit/test_command_parser_smoke.py`
- **Test command parsing with pipes.** (1 connections) — `server/tests/unit/test_command_parser_smoke.py`
- **Test parse_command raises error for empty string.** (1 connections) — `server/tests/unit/utils/test_command_parser.py`
- **Test parse_command raises error for whitespace-only string.** (1 connections) — `server/tests/unit/utils/test_command_parser.py`
- **Test parse_command raises error for command exceeding max length.** (1 connections) — `server/tests/unit/utils/test_command_parser.py`
- **Test parse_command raises error for unknown command.** (1 connections) — `server/tests/unit/utils/test_command_parser.py`
- *... and 9 more nodes in this community*

## Relationships

- [Command Parser](Command_Parser.md) (13 shared connections)
- [Client Event Store](Client_Event_Store.md) (4 shared connections)
- [Emote Schema Validator](Emote_Schema_Validator.md) (2 shared connections)
- [Cursor Plans Login](Cursor_Plans_Login.md) (1 shared connections)
- [Game Service Bundle](Game_Service_Bundle.md) (1 shared connections)
- [Async Room Loading Tests](Async_Room_Loading_Tests.md) (1 shared connections)

## Source Files

- `server/tests/unit/test_command_parser_smoke.py`
- `server/tests/unit/utils/test_command_parser.py`
- `server/utils/command_parser.py`

## Audit Trail

- EXTRACTED: 94 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*