# schemas validator rationale

> 33 nodes

## Key Concepts

- **EmoteService** (21 connections) — `server/game/emote_service.py`
- **test_emote_service.py** (15 connections) — `server/tests/unit/game/test_emote_service.py`
- **_service_with_emotes()** (10 connections) — `server/tests/unit/game/test_emote_service.py`
- **EmoteDefinition** (7 connections) — `server/game/emote_service.py`
- **.format_emote_messages()** (5 connections) — `server/game/emote_service.py`
- **._load_emotes()** (4 connections) — `server/game/emote_service.py`
- **._async_load_emotes()** (4 connections) — `server/game/emote_service.py`
- **.get_emote_definition()** (4 connections) — `server/game/emote_service.py`
- **.__init__()** (3 connections) — `server/game/emote_service.py`
- **.reload_emotes()** (3 connections) — `server/game/emote_service.py`
- **._validate_emote_payload()** (3 connections) — `server/game/emote_service.py`
- **test_format_emote_messages_unknown_raises()** (3 connections) — `server/tests/unit/game/test_emote_service.py`
- **.is_emote_alias()** (2 connections) — `server/game/emote_service.py`
- **.list_available_emotes()** (2 connections) — `server/game/emote_service.py`
- **test_emote_service_init_loads_via_mock()** (2 connections) — `server/tests/unit/game/test_emote_service.py`
- **test_is_emote_alias_and_get_definition()** (2 connections) — `server/tests/unit/game/test_emote_service.py`
- **test_format_emote_messages()** (2 connections) — `server/tests/unit/game/test_emote_service.py`
- **test_list_available_emotes()** (2 connections) — `server/tests/unit/game/test_emote_service.py`
- **test_reload_emotes_calls_load()** (2 connections) — `server/tests/unit/game/test_emote_service.py`
- **test_validate_emote_payload_no_validator()** (2 connections) — `server/tests/unit/game/test_emote_service.py`
- **test_validate_emote_payload_with_validator()** (2 connections) — `server/tests/unit/game/test_emote_service.py`
- **Public emote payload returned by EmoteService lookups.** (1 connections) — `server/game/emote_service.py`
- **Service for managing predefined emote actions and their messages.** (1 connections) — `server/game/emote_service.py`
- **Initialize the EmoteService.          Args:             emote_file_path: DEPRECA** (1 connections) — `server/game/emote_service.py`
- **Load emote definitions from PostgreSQL database.** (1 connections) — `server/game/emote_service.py`
- *... and 8 more nodes in this community*

## Relationships

- [commands recovery lucidity](commands_recovery_lucidity.md) (8 shared connections)
- [Database Access Layer](Database_Access_Layer.md) (3 shared connections)
- [command commands handler](command_commands_handler.md) (2 shared connections)
- [commands emote rationale](commands_emote_rationale.md) (2 shared connections)
- [chat game message](chat_game_message.md) (2 shared connections)
- [rate lucidity services](rate_lucidity_services.md) (1 shared connections)
- [Database Config](Database_Config.md) (1 shared connections)
- [Loot Generation](Loot_Generation.md) (1 shared connections)

## Source Files

- `server/game/emote_service.py`
- `server/tests/unit/game/test_emote_service.py`

## Audit Trail

- EXTRACTED: 108 (96%)
- INFERRED: 4 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*