# ChatMessage

> 62 nodes

## Key Concepts

- **chat_service.py** (49 connections) — `server/game/chat_service.py`
- **ChatMessage** (32 connections) — `server/game/chat_message.py`
- **chat_message_senders.py** (26 connections) — `server/game/chat_message_senders.py`
- **publish_chat_message_to_nats()** (24 connections) — `server/game/chat_nats_publisher.py`
- **chat_message.py** (14 connections) — `server/game/chat_message.py`
- **send_global_message()** (13 connections) — `server/game/chat_message_senders.py`
- **send_local_message()** (12 connections) — `server/game/chat_message_senders.py`
- **chat_message_helpers.py** (11 connections) — `server/game/chat_message_helpers.py`
- **create_and_log_chat_message()** (11 connections) — `server/game/chat_message_helpers.py`
- **chat_validation_helpers.py** (11 connections) — `server/game/chat_validation_helpers.py`
- **send_predefined_emote()** (10 connections) — `server/game/chat_message_senders.py`
- **.send_say_message()** (10 connections) — `server/game/chat_service.py`
- **.send_emote_message()** (10 connections) — `server/game/chat_service.py`
- **store_message_in_room_history()** (9 connections) — `server/game/chat_message_helpers.py`
- **normalize_player_id()** (9 connections) — `server/game/chat_message_senders.py`
- **send_system_message()** (9 connections) — `server/game/chat_message_senders.py`
- **send_whisper_message()** (9 connections) — `server/game/chat_message_senders.py`
- **send_party_message()** (9 connections) — `server/game/chat_message_senders.py`
- **check_channel_permissions()** (9 connections) — `server/game/chat_validation_helpers.py`
- **Any** (7 connections)
- **UUID** (7 connections)
- **validate_say_message()** (7 connections) — `server/game/chat_validation_helpers.py`
- **ChatMessage** (6 connections)
- **Any** (6 connections)
- **check_say_permissions()** (6 connections) — `server/game/chat_validation_helpers.py`
- *... and 37 more nodes in this community*

## Relationships

- [ChatService](ChatService.md) (21 shared connections)
- [.initialize()](initialize%28%29.md) (19 shared connections)
- [. init ()](_init_%28%29.md) (17 shared connections)
- [TerminalButtonProps](TerminalButtonProps.md) (15 shared connections)
- [get mythos time()](get_mythos_time%28%29.md) (10 shared connections)
- [PlayerIdCarrier](PlayerIdCarrier.md) (2 shared connections)
- [player preferences service](player_preferences_service.md) (2 shared connections)
- [add request context()](add_request_context%28%29.md) (1 shared connections)
- [NPCLifecycleManager](NPCLifecycleManager.md) (1 shared connections)
- [test magic commands](test_magic_commands.md) (1 shared connections)
- [chat moderation](chat_moderation.md) (1 shared connections)

## Source Files

- `server/game/chat_message.py`
- `server/game/chat_message_helpers.py`
- `server/game/chat_message_senders.py`
- `server/game/chat_nats_publisher.py`
- `server/game/chat_service.py`
- `server/game/chat_validation_helpers.py`
- `vulture_allowlist.py`

## Audit Trail

- EXTRACTED: 383 (99%)
- INFERRED: 3 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*