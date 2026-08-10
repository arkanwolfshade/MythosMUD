# Chat Message Helpers

> 62 nodes

## Key Concepts

- **chat_service.py** (45 connections) — `server/game/chat_service.py`
- **ChatMessage** (26 connections) — `server/game/chat_message.py`
- **chat_message_senders.py** (26 connections) — `server/game/chat_message_senders.py`
- **publish_chat_message_to_nats()** (18 connections) — `server/game/chat_nats_publisher.py`
- **send_global_message()** (13 connections) — `server/game/chat_message_senders.py`
- **chat_message.py** (12 connections) — `server/game/chat_message.py`
- **send_local_message()** (12 connections) — `server/game/chat_message_senders.py`
- **chat_validation_helpers.py** (11 connections) — `server/game/chat_validation_helpers.py`
- **chat_message_helpers.py** (10 connections) — `server/game/chat_message_helpers.py`
- **send_predefined_emote()** (10 connections) — `server/game/chat_message_senders.py`
- **.send_say_message()** (10 connections) — `server/game/chat_service.py`
- **.send_emote_message()** (10 connections) — `server/game/chat_service.py`
- **create_and_log_chat_message()** (9 connections) — `server/game/chat_message_helpers.py`
- **normalize_player_id()** (9 connections) — `server/game/chat_message_senders.py`
- **send_system_message()** (9 connections) — `server/game/chat_message_senders.py`
- **send_whisper_message()** (9 connections) — `server/game/chat_message_senders.py`
- **send_party_message()** (9 connections) — `server/game/chat_message_senders.py`
- **check_channel_permissions()** (9 connections) — `server/game/chat_validation_helpers.py`
- **store_message_in_room_history()** (7 connections) — `server/game/chat_message_helpers.py`
- **Any** (7 connections)
- **UUID** (7 connections)
- **validate_say_message()** (7 connections) — `server/game/chat_validation_helpers.py`
- **ChatMessage** (6 connections)
- **Any** (6 connections)
- **check_say_permissions()** (6 connections) — `server/game/chat_validation_helpers.py`
- *... and 37 more nodes in this community*

## Relationships

- [Game Service Bundle](Game_Service_Bundle.md) (14 shared connections)
- [NPC Definition Admin API](NPC_Definition_Admin_API.md) (11 shared connections)
- [Player Effects API](Player_Effects_API.md) (10 shared connections)
- [Chat Mute Admin API](Chat_Mute_Admin_API.md) (10 shared connections)
- [Monitoring API Endpoints](Monitoring_API_Endpoints.md) (7 shared connections)
- [E 2 E Timeout Analysis](E_2_E_Timeout_Analysis.md) (4 shared connections)
- [Command Parser Helpers](Command_Parser_Helpers.md) (2 shared connections)
- [Chat Moderation Service](Chat_Moderation_Service.md) (2 shared connections)
- [React Node Upgrade Summary](React_Node_Upgrade_Summary.md) (2 shared connections)
- [Room Toolkit Validator](Room_Toolkit_Validator.md) (1 shared connections)
- [MP Regeneration Service](MP_Regeneration_Service.md) (1 shared connections)
- [Client Event Store](Client_Event_Store.md) (1 shared connections)

## Source Files

- `server/game/chat_message.py`
- `server/game/chat_message_helpers.py`
- `server/game/chat_message_senders.py`
- `server/game/chat_nats_publisher.py`
- `server/game/chat_service.py`
- `server/game/chat_validation_helpers.py`
- `vulture_allowlist.py`

## Audit Trail

- EXTRACTED: 359 (100%)
- INFERRED: 1 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*