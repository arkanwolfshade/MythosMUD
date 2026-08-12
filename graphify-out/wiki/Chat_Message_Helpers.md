# Chat Message Helpers

> 66 nodes

## Key Concepts

- **chat_message_senders.py** (34 connections) — `server/game/chat_message_senders.py`
- **chat_channel_message_senders.py** (21 connections) — `server/game/chat_channel_message_senders.py`
- **send_global_message()** (13 connections) — `server/game/chat_channel_message_senders.py`
- **send_emote_message()** (13 connections) — `server/game/chat_message_senders.py`
- **normalize_player_id()** (12 connections) — `server/game/chat_channel_message_senders.py`
- **send_local_message()** (12 connections) — `server/game/chat_message_senders.py`
- **send_say_message()** (12 connections) — `server/game/chat_message_senders.py`
- **chat_validation_helpers.py** (11 connections) — `server/game/chat_validation_helpers.py`
- **chat_message_helpers.py** (10 connections) — `server/game/chat_message_helpers.py`
- **send_system_message()** (9 connections) — `server/game/chat_channel_message_senders.py`
- **send_whisper_message()** (9 connections) — `server/game/chat_channel_message_senders.py`
- **send_party_message()** (9 connections) — `server/game/chat_channel_message_senders.py`
- **create_and_log_chat_message()** (9 connections) — `server/game/chat_message_helpers.py`
- **Any** (9 connections)
- **send_predefined_emote()** (9 connections) — `server/game/chat_message_senders.py`
- **_publish_room_chat_response()** (9 connections) — `server/game/chat_message_senders.py`
- **check_channel_permissions()** (9 connections) — `server/game/chat_validation_helpers.py`
- **_publish_predefined_emote()** (8 connections) — `server/game/chat_message_senders.py`
- **_resolve_room_chat_sender()** (7 connections) — `server/game/chat_message_senders.py`
- **check_say_permissions()** (7 connections) — `server/game/chat_validation_helpers.py`
- **store_message_in_room_history()** (6 connections) — `server/game/chat_message_helpers.py`
- **Any** (6 connections)
- **Any** (5 connections)
- **UUID** (5 connections)
- **_resolve_predefined_emote_sender()** (5 connections) — `server/game/chat_message_senders.py`
- *... and 41 more nodes in this community*

## Relationships

- [Who Command Tests](Who_Command_Tests.md) (26 shared connections)
- [Client Event Store](Client_Event_Store.md) (7 shared connections)
- [Async Persistence Types](Async_Persistence_Types.md) (2 shared connections)

## Source Files

- `server/game/chat_channel_message_senders.py`
- `server/game/chat_message_helpers.py`
- `server/game/chat_message_senders.py`
- `server/game/chat_validation_helpers.py`

## Audit Trail

- EXTRACTED: 337 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*