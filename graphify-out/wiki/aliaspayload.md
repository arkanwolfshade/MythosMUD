# aliaspayload

> 71 nodes

## Key Concepts

- **alias_storage.py** (75 connections) — `server/alias_storage.py`
- **handle_emote_command()** (15 connections) — `server/commands/emote_commands.py`
- **emote_commands.py** (14 connections) — `server/commands/emote_commands.py`
- **.get_player_aliases()** (10 connections) — `server/alias_storage.py`
- **.get_alias_file_path()** (9 connections) — `server/alias_storage.py`
- **._load_alias_data()** (9 connections) — `server/alias_storage.py`
- **alias_graph.py** (8 connections) — `server/utils/alias_graph.py`
- **._save_alias_data()** (7 connections) — `server/alias_storage.py`
- **.save_player_aliases()** (7 connections) — `server/alias_storage.py`
- **._validate_alias_payload()** (7 connections) — `server/alias_storage.py`
- **test_emote_commands.py** (7 connections) — `server/tests/unit/commands/test_emote_commands.py`
- **.add_alias()** (6 connections) — `server/alias_storage.py`
- **Path** (6 connections)
- **_apply_alias_timestamps()** (5 connections) — `server/alias_storage.py`
- **_get_emote_services()** (5 connections) — `server/commands/emote_commands.py`
- **AliasPayload** (5 connections)
- **Any** (5 connections)
- **_AliasValidatorCache** (4 connections) — `server/alias_storage.py`
- **.backup_aliases()** (4 connections) — `server/alias_storage.py`
- **.get_alias()** (4 connections) — `server/alias_storage.py`
- **.remove_alias()** (4 connections) — `server/alias_storage.py`
- **_as_alias_payload()** (4 connections) — `server/alias_storage.py`
- **_get_alias_validator()** (4 connections) — `server/alias_storage.py`
- **_extract_emote_action()** (4 connections) — `server/commands/emote_commands.py`
- **_format_emote_messages()** (4 connections) — `server/commands/emote_commands.py`
- *... and 46 more nodes in this community*

## Relationships

- [server alias storage aliasstorage](server_alias_storage_aliasstorage.md) (22 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (10 shared connections)
- [server models alias](server_models_alias.md) (6 shared connections)
- [schemas validator](schemas_validator.md) (5 shared connections)
- [server commands admin commands](server_commands_admin_commands.md) (5 shared connections)
- [server command handler alias expansion](server_command_handler_alias_expansion.md) (4 shared connections)
- [dropresolved](dropresolved.md) (4 shared connections)
- [server commands npc admin behavior](server_commands_npc_admin_behavior.md) (3 shared connections)
- [server models command alias aliascommand](server_models_command_alias_aliascommand.md) (2 shared connections)
- [server command handler command input](server_command_handler_command_input.md) (2 shared connections)
- [server commands rescue commands](server_commands_rescue_commands.md) (2 shared connections)
- [server commands utility commands](server_commands_utility_commands.md) (2 shared connections)

## Source Files

- `server/alias_storage.py`
- `server/commands/emote_commands.py`
- `server/tests/unit/commands/test_emote_commands.py`
- `server/utils/alias_graph.py`

## Audit Trail

- EXTRACTED: 204 (99%)
- INFERRED: 3 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*