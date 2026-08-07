# chat game message

> 59 nodes

## Key Concepts

- **chat_service.py** (49 connections) — `server/game/chat_service.py`
- **chat_message_senders.py** (27 connections) — `server/game/chat_message_senders.py`
- **test_chat_message_senders.py** (24 connections) — `server/tests/unit/game/test_chat_message_senders.py`
- **send_global_message()** (16 connections) — `server/game/chat_message_senders.py`
- **send_local_message()** (15 connections) — `server/game/chat_message_senders.py`
- **create_and_log_chat_message()** (13 connections) — `server/game/chat_message_helpers.py`
- **send_system_message()** (13 connections) — `server/game/chat_message_senders.py`
- **send_whisper_message()** (13 connections) — `server/game/chat_message_senders.py`
- **send_predefined_emote()** (13 connections) — `server/game/chat_message_senders.py`
- **normalize_player_id()** (11 connections) — `server/game/chat_message_senders.py`
- **send_party_message()** (11 connections) — `server/game/chat_message_senders.py`
- **chat_validation_helpers.py** (11 connections) — `server/game/chat_validation_helpers.py`
- **_player()** (11 connections) — `server/tests/unit/game/test_chat_message_senders.py`
- **.send_emote_message()** (10 connections) — `server/game/chat_service.py`
- **check_channel_permissions()** (9 connections) — `server/game/chat_validation_helpers.py`
- **Any** (7 connections)
- **UUID** (7 connections)
- **validate_say_message()** (7 connections) — `server/game/chat_validation_helpers.py`
- **ChatMessage** (6 connections)
- **Any** (6 connections)
- **check_say_permissions()** (6 connections) — `server/game/chat_validation_helpers.py`
- **validate_emote_action()** (5 connections) — `server/game/chat_validation_helpers.py`
- **validate_global_message()** (5 connections) — `server/game/chat_validation_helpers.py`
- **check_global_level_requirement()** (5 connections) — `server/game/chat_validation_helpers.py`
- **test_send_system_message_validation_and_auth()** (3 connections) — `server/tests/unit/game/test_chat_message_senders.py`
- *... and 34 more nodes in this community*

## Relationships

- [quest chat game](quest_chat_game.md) (27 shared connections)
- [alias command models](alias_command_models.md) (11 shared connections)
- [logging examples fastapi](logging_examples_fastapi.md) (10 shared connections)
- [chat service game](chat_service_game.md) (9 shared connections)
- [combat messaging service](combat_messaging_service.md) (5 shared connections)
- [websocket helpers realtime](websocket_helpers_realtime.md) (2 shared connections)
- [health monitor realtime](health_monitor_realtime.md) (2 shared connections)
- [aggro threat services](aggro_threat_services.md) (1 shared connections)
- [commands magic rationale](commands_magic_rationale.md) (1 shared connections)
- [NPC Definitions Admin](NPC_Definitions_Admin.md) (1 shared connections)
- [lucidity commands services](lucidity_commands_services.md) (1 shared connections)
- [combat services service](combat_services_service.md) (1 shared connections)

## Source Files

- `server/game/chat_message_helpers.py`
- `server/game/chat_message_senders.py`
- `server/game/chat_service.py`
- `server/game/chat_validation_helpers.py`
- `server/tests/unit/game/test_chat_message_senders.py`
- `vulture_allowlist.py`

## Audit Trail

- EXTRACTED: 360 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*