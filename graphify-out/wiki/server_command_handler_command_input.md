# server command handler command input

> 89 nodes

## Key Concepts

- **emote_service.py** (21 connections) — `server/game/emote_service.py`
- **EmoteService** (20 connections) — `server/game/emote_service.py`
- **test_emote_service.py** (16 connections) — `server/tests/unit/game/test_emote_service.py`
- **command_input.py** (15 connections) — `server/command_handler/command_input.py`
- **TestCommandNormalization** (12 connections) — `server/tests/unit/commands/test_command_input.py`
- **normalize_command()** (12 connections) — `server/command_handler/command_input.py`
- **clean_command_input()** (10 connections) — `server/command_handler/command_input.py`
- **should_treat_as_emote()** (10 connections) — `server/command_handler/command_input.py`
- **_service_with_emotes()** (10 connections) — `server/tests/unit/game/test_emote_service.py`
- **TestEmoteDetection** (8 connections) — `server/tests/unit/commands/test_command_input.py`
- **_is_predefined_emote()** (8 connections) — `server/command_handler/command_input.py`
- **test_command_input.py** (8 connections) — `server/tests/unit/commands/test_command_input.py`
- **EmoteDefinition** (6 connections) — `server/game/emote_service.py`
- **patch** (5 connections)
- **._async_load_emotes()** (4 connections) — `server/game/emote_service.py`
- **.format_emote_messages()** (4 connections) — `server/game/emote_service.py`
- **.get_emote_definition()** (4 connections) — `server/game/emote_service.py`
- **._load_emotes()** (4 connections) — `server/game/emote_service.py`
- **_get_emote_validator()** (4 connections) — `server/game/emote_service.py`
- **.test_is_predefined_emote_false()** (4 connections) — `server/tests/unit/commands/test_command_input.py`
- **.test_is_predefined_emote_handles_error()** (4 connections) — `server/tests/unit/commands/test_command_input.py`
- **.test_is_predefined_emote_true()** (4 connections) — `server/tests/unit/commands/test_command_input.py`
- **.test_should_treat_as_emote_predefined_emote()** (4 connections) — `server/tests/unit/commands/test_command_input.py`
- **.test_should_treat_as_emote_unknown_word()** (4 connections) — `server/tests/unit/commands/test_command_input.py`
- **_EmoteLoadResult** (3 connections) — `server/game/emote_service.py`
- *... and 64 more nodes in this community*

## Relationships

- [claude rules sqlalchemy](claude_rules_sqlalchemy.md) (6 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (6 shared connections)
- [server command handler alias expansion](server_command_handler_alias_expansion.md) (4 shared connections)
- [server command handler command execution](server_command_handler_command_execution.md) (4 shared connections)
- [schemas validator](schemas_validator.md) (4 shared connections)
- [mythosvalidationerror](mythosvalidationerror.md) (3 shared connections)
- [aliaspayload](aliaspayload.md) (2 shared connections)
- [server game chat channel message](server_game_chat_channel_message.md) (2 shared connections)
- [server command handler unified check](server_command_handler_unified_check.md) (2 shared connections)
- [server database config helpers get](server_database_config_helpers_get.md) (2 shared connections)
- [server config init](server_config_init.md) (2 shared connections)
- [server tests unit validators test](server_tests_unit_validators_test.md) (2 shared connections)

## Source Files

- `server/command_handler/command_input.py`
- `server/game/emote_service.py`
- `server/tests/unit/commands/test_command_input.py`
- `server/tests/unit/game/test_emote_service.py`

## Audit Trail

- EXTRACTED: 173 (99%)
- INFERRED: 2 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*