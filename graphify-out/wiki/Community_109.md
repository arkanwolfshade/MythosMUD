# Community 109

> 93 nodes

## Key Concepts

- **chat_service.py** (61 connections) — `server/game/chat_service.py`
- **chat_message_senders.py** (30 connections) — `server/game/chat_message_senders.py`
- **chat_message.py** (19 connections) — `server/game/chat_message.py`
- **send_local_message()** (18 connections) — `server/game/chat_message_senders.py`
- **send_predefined_emote()** (17 connections) — `server/game/chat_message_senders.py`
- **send_party_message()** (14 connections) — `server/game/chat_message_senders.py`
- **ChatLogger** (13 connections) — `server/game/chat_channel_message_senders.py`
- **ChatUserManager** (13 connections) — `server/game/chat_channel_message_senders.py`
- **chat_message_helpers.py** (13 connections) — `server/game/chat_message_helpers.py`
- **ChatRateLimiter** (12 connections) — `server/game/chat_channel_message_senders.py`
- **create_and_log_chat_message()** (12 connections) — `server/game/chat_message_helpers.py`
- **chat_validation_helpers.py** (12 connections) — `server/game/chat_validation_helpers.py`
- **test_chat_message_helpers.py** (12 connections) — `server/tests/unit/game/test_chat_message_helpers.py`
- **ChatPlayerService** (11 connections) — `server/game/chat_channel_message_senders.py`
- **.send_say_message()** (11 connections) — `server/game/chat_service.py`
- **.send_emote_message()** (10 connections) — `server/game/chat_service.py`
- **check_channel_permissions()** (10 connections) — `server/game/chat_validation_helpers.py`
- **ChatEmoteService** (9 connections) — `server/game/chat_channel_message_senders.py`
- **store_message_in_room_history()** (9 connections) — `server/game/chat_message_helpers.py`
- **normalize_player_id()** (8 connections) — `server/game/chat_message_senders.py`
- **create_and_log_say_message()** (7 connections) — `server/game/chat_message_helpers.py`
- **validate_say_message()** (7 connections) — `server/game/chat_validation_helpers.py`
- **Protocol** (7 connections)
- **store_global_message_in_history()** (6 connections) — `server/game/chat_message_helpers.py`
- **_publish_room_chat()** (6 connections) — `server/game/chat_service.py`
- *... and 68 more nodes in this community*

## Relationships

- [Community 446](Community_446.md) (32 shared connections)
- [Community 414](Community_414.md) (26 shared connections)
- [Community 50](Community_50.md) (15 shared connections)
- [Aliases & Webhook/Schema Validation](Aliases_&_Webhook-Schema_Validation.md) (15 shared connections)
- [Community 291](Community_291.md) (10 shared connections)
- [Community 160](Community_160.md) (6 shared connections)
- [Community 629](Community_629.md) (6 shared connections)
- [Community 156](Community_156.md) (3 shared connections)
- [Community 604](Community_604.md) (2 shared connections)
- [DI Containers & API Bootstrap](DI_Containers_&_API_Bootstrap.md) (2 shared connections)
- [Community 169](Community_169.md) (1 shared connections)
- [Community 1005](Community_1005.md) (1 shared connections)

## Source Files

- `server/game/chat_channel_message_senders.py`
- `server/game/chat_message.py`
- `server/game/chat_message_helpers.py`
- `server/game/chat_message_senders.py`
- `server/game/chat_service.py`
- `server/game/chat_validation_helpers.py`
- `server/tests/unit/game/test_chat_message_helpers.py`
- `vulture_allowlist.py`

## Audit Trail

- EXTRACTED: 275 (94%)
- INFERRED: 19 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*