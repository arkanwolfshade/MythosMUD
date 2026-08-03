# chat game message

> 88 nodes

## Key Concepts

- **chat_service.py** (49 connections) — `server/game/chat_service.py`
- **ChatMessage** (41 connections) — `server/game/chat_message.py`
- **chat_message_senders.py** (27 connections) — `server/game/chat_message_senders.py`
- **test_chat_message_senders.py** (24 connections) — `server/tests/unit/game/test_chat_message_senders.py`
- **chat_message.py** (17 connections) — `server/game/chat_message.py`
- **send_global_message()** (16 connections) — `server/game/chat_message_senders.py`
- **send_local_message()** (15 connections) — `server/game/chat_message_senders.py`
- **create_and_log_chat_message()** (13 connections) — `server/game/chat_message_helpers.py`
- **send_system_message()** (13 connections) — `server/game/chat_message_senders.py`
- **send_whisper_message()** (13 connections) — `server/game/chat_message_senders.py`
- **send_predefined_emote()** (13 connections) — `server/game/chat_message_senders.py`
- **chat_message_helpers.py** (12 connections) — `server/game/chat_message_helpers.py`
- **test_chat_message_helpers.py** (12 connections) — `server/tests/unit/game/test_chat_message_helpers.py`
- **store_message_in_room_history()** (11 connections) — `server/game/chat_message_helpers.py`
- **normalize_player_id()** (11 connections) — `server/game/chat_message_senders.py`
- **send_party_message()** (11 connections) — `server/game/chat_message_senders.py`
- **chat_validation_helpers.py** (11 connections) — `server/game/chat_validation_helpers.py`
- **_player()** (11 connections) — `server/tests/unit/game/test_chat_message_senders.py`
- **.send_say_message()** (10 connections) — `server/game/chat_service.py`
- **.send_emote_message()** (10 connections) — `server/game/chat_service.py`
- **check_channel_permissions()** (9 connections) — `server/game/chat_validation_helpers.py`
- **create_and_log_say_message()** (7 connections) — `server/game/chat_message_helpers.py`
- **Any** (7 connections)
- **UUID** (7 connections)
- **validate_say_message()** (7 connections) — `server/game/chat_validation_helpers.py`
- *... and 63 more nodes in this community*

## Relationships

- [chat service game](chat_service_game.md) (21 shared connections)
- [alias command models](alias_command_models.md) (17 shared connections)
- [quest chat game](quest_chat_game.md) (17 shared connections)
- [models npc rationale](models_npc_rationale.md) (13 shared connections)
- [combat messaging service](combat_messaging_service.md) (8 shared connections)
- [app tick game](app_tick_game.md) (5 shared connections)
- [schemas validator rationale](schemas_validator_rationale.md) (2 shared connections)
- [game chat whisper](game_chat_whisper.md) (2 shared connections)
- [Magic Spell Service](Magic_Spell_Service.md) (1 shared connections)
- [commands magic rationale](commands_magic_rationale.md) (1 shared connections)
- [NPC Definitions Admin](NPC_Definitions_Admin.md) (1 shared connections)
- [services ascii map](services_ascii_map.md) (1 shared connections)

## Source Files

- `server/game/chat_message.py`
- `server/game/chat_message_helpers.py`
- `server/game/chat_message_senders.py`
- `server/game/chat_service.py`
- `server/game/chat_validation_helpers.py`
- `server/tests/unit/game/test_chat_message_helpers.py`
- `server/tests/unit/game/test_chat_message_senders.py`
- `vulture_allowlist.py`

## Audit Trail

- EXTRACTED: 507 (99%)
- INFERRED: 6 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*