# Chat Message Helpers

> 58 nodes · cohesion 0.08

## Key Concepts

- **chat_service.py** (49 connections) — `server/game/chat_service.py`
- **ChatMessage** (31 connections) — `server/game/chat_message.py`
- **chat_message_senders.py** (26 connections) — `server/game/chat_message_senders.py`
- **publish_chat_message_to_nats()** (24 connections) — `server/game/chat_nats_publisher.py`
- **chat_message.py** (14 connections) — `server/game/chat_message.py`
- **send_global_message()** (13 connections) — `server/game/chat_message_senders.py`
- **send_local_message()** (12 connections) — `server/game/chat_message_senders.py`
- **chat_message_helpers.py** (11 connections) — `server/game/chat_message_helpers.py`
- **create_and_log_chat_message()** (11 connections) — `server/game/chat_message_helpers.py`
- **chat_validation_helpers.py** (11 connections) — `server/game/chat_validation_helpers.py`
- **send_predefined_emote()** (10 connections) — `server/game/chat_message_senders.py`
- **.send_emote_message()** (10 connections) — `server/game/chat_service.py`
- **.send_say_message()** (10 connections) — `server/game/chat_service.py`
- **store_message_in_room_history()** (9 connections) — `server/game/chat_message_helpers.py`
- **normalize_player_id()** (9 connections) — `server/game/chat_message_senders.py`
- **send_party_message()** (9 connections) — `server/game/chat_message_senders.py`
- **send_system_message()** (9 connections) — `server/game/chat_message_senders.py`
- **send_whisper_message()** (9 connections) — `server/game/chat_message_senders.py`
- **check_channel_permissions()** (9 connections) — `server/game/chat_validation_helpers.py`
- **Any** (7 connections)
- **UUID** (7 connections)
- **validate_say_message()** (7 connections) — `server/game/chat_validation_helpers.py`
- **ChatMessage** (6 connections)
- **check_say_permissions()** (6 connections) — `server/game/chat_validation_helpers.py`
- **Any** (6 connections)
- *... and 33 more nodes in this community*

## Relationships

- [Command Factory Creators](Command_Factory_Creators.md) (14 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (13 shared connections)
- [Logging Migration Complete](Logging_Migration_Complete.md) (10 shared connections)
- [Chat NATS Publisher](Chat_NATS_Publisher.md) (9 shared connections)
- [Chat Mute Admin API](Chat_Mute_Admin_API.md) (7 shared connections)
- [Edge Creation Modal](Edge_Creation_Modal.md) (2 shared connections)
- [Chat Moderation Service](Chat_Moderation_Service.md) (2 shared connections)
- [Dual Connection API Reference](Dual_Connection_API_Reference.md) (2 shared connections)
- [Command Integration Summary](Command_Integration_Summary.md) (2 shared connections)
- [Community 1711](Community_1711.md) (1 shared connections)
- [Admin Set Lucidity Command](Admin_Set_Lucidity_Command.md) (1 shared connections)
- [Dependency Injection Tests](Dependency_Injection_Tests.md) (1 shared connections)

## Source Files

- `server/game/chat_message.py`
- `server/game/chat_message_helpers.py`
- `server/game/chat_message_senders.py`
- `server/game/chat_nats_publisher.py`
- `server/game/chat_service.py`
- `server/game/chat_validation_helpers.py`
- `vulture_allowlist.py`

## Audit Trail

- EXTRACTED: 379 (99%)
- INFERRED: 2 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*