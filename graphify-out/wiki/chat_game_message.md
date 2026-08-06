# chat game message

> 64 nodes

## Key Concepts

- **chat_service.py** (49 connections) — `server/game/chat_service.py`
- **chat_message_senders.py** (27 connections) — `server/game/chat_message_senders.py`
- **test_chat_message_senders.py** (24 connections) — `server/tests/unit/game/test_chat_message_senders.py`
- **send_global_message()** (16 connections) — `server/game/chat_message_senders.py`
- **Any** (16 connections)
- **send_local_message()** (15 connections) — `server/game/chat_message_senders.py`
- **send_system_message()** (13 connections) — `server/game/chat_message_senders.py`
- **send_whisper_message()** (13 connections) — `server/game/chat_message_senders.py`
- **send_predefined_emote()** (13 connections) — `server/game/chat_message_senders.py`
- **store_message_in_room_history()** (11 connections) — `server/game/chat_message_helpers.py`
- **normalize_player_id()** (11 connections) — `server/game/chat_message_senders.py`
- **send_party_message()** (11 connections) — `server/game/chat_message_senders.py`
- **chat_validation_helpers.py** (11 connections) — `server/game/chat_validation_helpers.py`
- **_player()** (11 connections) — `server/tests/unit/game/test_chat_message_senders.py`
- **.send_say_message()** (10 connections) — `server/game/chat_service.py`
- **.send_emote_message()** (10 connections) — `server/game/chat_service.py`
- **check_channel_permissions()** (9 connections) — `server/game/chat_validation_helpers.py`
- **Any** (7 connections)
- **UUID** (7 connections)
- **validate_say_message()** (7 connections) — `server/game/chat_validation_helpers.py`
- **ChatMessage** (6 connections)
- **Any** (6 connections)
- **check_say_permissions()** (6 connections) — `server/game/chat_validation_helpers.py`
- **._normalize_player_id()** (5 connections) — `server/game/chat_service.py`
- **validate_emote_action()** (5 connections) — `server/game/chat_validation_helpers.py`
- *... and 39 more nodes in this community*

## Relationships

- [services ascii map](services_ascii_map.md) (22 shared connections)
- [chat service game](chat_service_game.md) (20 shared connections)
- [alias command models](alias_command_models.md) (12 shared connections)
- [Error Conversion](Error_Conversion.md) (9 shared connections)
- [quest chat game](quest_chat_game.md) (5 shared connections)
- [combat messaging service](combat_messaging_service.md) (5 shared connections)
- [game chat whisper](game_chat_whisper.md) (5 shared connections)
- [chat moderation game](chat_moderation_game.md) (3 shared connections)
- [websocket helpers realtime](websocket_helpers_realtime.md) (2 shared connections)
- [catatonia registry services](catatonia_registry_services.md) (1 shared connections)
- [alias storage rationale](alias_storage_rationale.md) (1 shared connections)
- [NPC Definitions Admin](NPC_Definitions_Admin.md) (1 shared connections)

## Source Files

- `server/game/chat_message_helpers.py`
- `server/game/chat_message_senders.py`
- `server/game/chat_service.py`
- `server/game/chat_validation_helpers.py`
- `server/tests/unit/game/test_chat_message_senders.py`
- `vulture_allowlist.py`

## Audit Trail

- EXTRACTED: 391 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*