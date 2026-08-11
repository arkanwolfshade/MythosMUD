# Health Endpoint Spec

> 14 nodes

## Key Concepts

- **Any** (9 connections)
- **send_predefined_emote()** (9 connections) — `server/game/chat_message_senders.py`
- **_publish_room_chat_response()** (9 connections) — `server/game/chat_message_senders.py`
- **_publish_predefined_emote()** (8 connections) — `server/game/chat_message_senders.py`
- **_resolve_predefined_emote_sender()** (5 connections) — `server/game/chat_message_senders.py`
- **_log_predefined_emote_message()** (5 connections) — `server/game/chat_message_senders.py`
- **ChatMessage** (3 connections)
- **_register_echo_suppression()** (3 connections) — `server/game/chat_message_senders.py`
- **Validate emote sender; return error dict or (player, room_id).** (1 connections) — `server/game/chat_message_senders.py`
- **Log emote chat payload for AI processing.** (1 connections) — `server/game/chat_message_senders.py`
- **Format, log, and NATS-publish a predefined emote; return API payload.** (1 connections) — `server/game/chat_message_senders.py`
- **Send a predefined emote message using the EmoteService.      This function use** (1 connections) — `server/game/chat_message_senders.py`
- **Register message id for sender echo suppression; tolerate import cycles.** (1 connections) — `server/game/chat_message_senders.py`
- **Publish chat message to NATS and build the API success payload.** (1 connections) — `server/game/chat_message_senders.py`

## Relationships

- [Chat Message Helpers](Chat_Message_Helpers.md) (16 shared connections)
- [Who Command Tests](Who_Command_Tests.md) (4 shared connections)
- [Async Persistence Types](Async_Persistence_Types.md) (1 shared connections)

## Source Files

- `server/game/chat_message_senders.py`

## Audit Trail

- EXTRACTED: 57 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*