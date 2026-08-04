# chat game message

> 100 nodes

## Key Concepts

- **chat_service.py** (49 connections) — `server/game/chat_service.py`
- **ChatMessage** (41 connections) — `server/game/chat_message.py`
- **chat_npc_system.py** (33 connections) — `server/game/chat_npc_system.py`
- **publish_chat_message_to_nats()** (30 connections) — `server/game/chat_nats_publisher.py`
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
- **send_personal_system_message()** (11 connections) — `server/game/chat_npc_system.py`
- **chat_validation_helpers.py** (11 connections) — `server/game/chat_validation_helpers.py`
- **_player()** (11 connections) — `server/tests/unit/game/test_chat_message_senders.py`
- **.send_say_message()** (10 connections) — `server/game/chat_service.py`
- **.send_emote_message()** (10 connections) — `server/game/chat_service.py`
- **check_channel_permissions()** (9 connections) — `server/game/chat_validation_helpers.py`
- **create_and_log_say_message()** (7 connections) — `server/game/chat_message_helpers.py`
- *... and 75 more nodes in this community*

## Relationships

- [quest chat game](quest_chat_game.md) (27 shared connections)
- [chat service game](chat_service_game.md) (21 shared connections)
- [alias command models](alias_command_models.md) (20 shared connections)
- [NPC Combat](NPC_Combat.md) (16 shared connections)
- [combat messaging service](combat_messaging_service.md) (10 shared connections)
- [app tick game](app_tick_game.md) (6 shared connections)
- [calendar models rationale](calendar_models_rationale.md) (4 shared connections)
- [Realtime Subscribers](Realtime_Subscribers.md) (3 shared connections)
- [commands recovery lucidity](commands_recovery_lucidity.md) (2 shared connections)
- [Error Conversion](Error_Conversion.md) (2 shared connections)
- [game chat whisper](game_chat_whisper.md) (2 shared connections)
- [nats exceptions services](nats_exceptions_services.md) (1 shared connections)

## Source Files

- `server/game/chat_message.py`
- `server/game/chat_message_helpers.py`
- `server/game/chat_message_senders.py`
- `server/game/chat_nats_publisher.py`
- `server/game/chat_npc_system.py`
- `server/game/chat_service.py`
- `server/game/chat_validation_helpers.py`
- `server/tests/unit/game/test_chat_message_helpers.py`
- `server/tests/unit/game/test_chat_message_senders.py`
- `vulture_allowlist.py`

## Audit Trail

- EXTRACTED: 604 (99%)
- INFERRED: 7 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*