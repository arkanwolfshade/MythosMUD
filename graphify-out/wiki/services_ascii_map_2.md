# services ascii map

> 41 nodes

## Key Concepts

- **ChatMessage** (41 connections) — `server/game/chat_message.py`
- **chat_message.py** (17 connections) — `server/game/chat_message.py`
- **create_and_log_chat_message()** (13 connections) — `server/game/chat_message_helpers.py`
- **chat_message_helpers.py** (12 connections) — `server/game/chat_message_helpers.py`
- **test_chat_message_helpers.py** (12 connections) — `server/tests/unit/game/test_chat_message_helpers.py`
- **create_and_log_say_message()** (7 connections) — `server/game/chat_message_helpers.py`
- **store_global_message_in_history()** (6 connections) — `server/game/chat_message_helpers.py`
- **test_get_room_messages()** (4 connections) — `server/tests/unit/game/test_chat_service.py`
- **.to_dict()** (3 connections) — `server/game/chat_message.py`
- **test_create_and_log_chat_message()** (3 connections) — `server/tests/unit/game/test_chat_message_helpers.py`
- **test_store_message_in_room_history_creates_and_trims()** (3 connections) — `server/tests/unit/game/test_chat_message_helpers.py`
- **test_store_global_message_in_history_trims()** (3 connections) — `server/tests/unit/game/test_chat_message_helpers.py`
- **test_chat_message_to_dict_includes_speaker_kind()** (3 connections) — `server/tests/unit/game/test_chat_npc_system.py`
- **test_chat_message_init()** (3 connections) — `server/tests/unit/game/test_chat_service.py`
- **test_chat_message_init_with_target()** (3 connections) — `server/tests/unit/game/test_chat_service.py`
- **test_chat_message_to_dict()** (3 connections) — `server/tests/unit/game/test_chat_service.py`
- **test_chat_message_to_dict_with_target()** (3 connections) — `server/tests/unit/game/test_chat_service.py`
- **test_chat_message_log_message()** (3 connections) — `server/tests/unit/game/test_chat_service.py`
- **test_chat_message_to_dict_with_echo_sent()** (3 connections) — `server/tests/unit/game/test_chat_service.py`
- **.__init__()** (2 connections) — `server/game/chat_message.py`
- **UUID** (2 connections)
- **.log_message()** (2 connections) — `server/game/chat_message.py`
- **test_create_and_log_say_message()** (2 connections) — `server/tests/unit/game/test_chat_message_helpers.py`
- **Any** (1 connections)
- **Chat message model for MythosMUD.  This module provides the ChatMessage class wh** (1 connections) — `server/game/chat_message.py`
- *... and 16 more nodes in this community*

## Relationships

- [chat game message](chat_game_message.md) (22 shared connections)
- [quest chat game](quest_chat_game.md) (12 shared connections)
- [chat service game](chat_service_game.md) (11 shared connections)
- [alias command models](alias_command_models.md) (5 shared connections)
- [app tick game](app_tick_game.md) (5 shared connections)
- [Error Conversion](Error_Conversion.md) (3 shared connections)
- [combat messaging service](combat_messaging_service.md) (3 shared connections)

## Source Files

- `server/game/chat_message.py`
- `server/game/chat_message_helpers.py`
- `server/tests/unit/game/test_chat_message_helpers.py`
- `server/tests/unit/game/test_chat_npc_system.py`
- `server/tests/unit/game/test_chat_service.py`

## Audit Trail

- EXTRACTED: 165 (96%)
- INFERRED: 6 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*