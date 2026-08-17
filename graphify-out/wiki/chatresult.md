# chatresult

> 87 nodes

## Key Concepts

- **chat_service.py** (59 connections) — `server/game/chat_service.py`
- **chat_channel_message_senders.py** (39 connections) — `server/game/chat_channel_message_senders.py`
- **chat_message_senders.py** (30 connections) — `server/game/chat_message_senders.py`
- **ChatSendServices** (20 connections) — `server/game/chat_channel_message_senders.py`
- **send_whisper_message()** (17 connections) — `server/game/chat_channel_message_senders.py`
- **send_system_message()** (16 connections) — `server/game/chat_channel_message_senders.py`
- **send_global_message()** (14 connections) — `server/game/chat_channel_message_senders.py`
- **ChatLogger** (13 connections) — `server/game/chat_channel_message_senders.py`
- **ChatUserManager** (13 connections) — `server/game/chat_channel_message_senders.py`
- **ChatRateLimiter** (12 connections) — `server/game/chat_channel_message_senders.py`
- **chat_validation_helpers.py** (12 connections) — `server/game/chat_validation_helpers.py`
- **ChatPlayerService** (11 connections) — `server/game/chat_channel_message_senders.py`
- **send_party_message()** (11 connections) — `server/game/chat_channel_message_senders.py`
- **check_channel_permissions()** (10 connections) — `server/game/chat_validation_helpers.py`
- **ChatResult** (10 connections)
- **ChatPlayerView** (9 connections) — `server/game/chat_channel_message_senders.py`
- **_publish_chat_or_unavailable()** (9 connections) — `server/game/chat_channel_message_senders.py`
- **WhisperTracker** (8 connections) — `server/game/chat_channel_message_senders.py`
- **_log_and_store_whisper_message()** (8 connections) — `server/game/chat_channel_message_senders.py`
- **_authorize_global_sender()** (7 connections) — `server/game/chat_channel_message_senders.py`
- **_log_and_store_system_message()** (7 connections) — `server/game/chat_channel_message_senders.py`
- **normalize_player_id()** (7 connections) — `server/game/chat_channel_message_senders.py`
- **validate_say_message()** (7 connections) — `server/game/chat_validation_helpers.py`
- **ChatMessage** (7 connections)
- **_append_channel_history()** (6 connections) — `server/game/chat_channel_message_senders.py`
- *... and 62 more nodes in this community*

## Relationships

- [server game chat message chatmessage](server_game_chat_message_chatmessage.md) (43 shared connections)
- [server game chat message](server_game_chat_message.md) (22 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (14 shared connections)
- [server game chat service chatservice](server_game_chat_service_chatservice.md) (10 shared connections)
- [server game chat nats publisher](server_game_chat_nats_publisher.md) (8 shared connections)
- [server game chat pose helpers](server_game_chat_pose_helpers.md) (5 shared connections)
- [server game chat npc system](server_game_chat_npc_system.md) (3 shared connections)
- [server game chat moderation chatmoderation](server_game_chat_moderation_chatmoderation.md) (2 shared connections)
- [server game emote service emotedefinition](server_game_emote_service_emotedefinition.md) (1 shared connections)
- [server game chat pose manager](server_game_chat_pose_manager.md) (1 shared connections)
- [server game chat whisper tracker](server_game_chat_whisper_tracker.md) (1 shared connections)
- [server api players](server_api_players.md) (1 shared connections)

## Source Files

- `server/game/chat_channel_message_senders.py`
- `server/game/chat_message_senders.py`
- `server/game/chat_service.py`
- `server/game/chat_validation_helpers.py`
- `vulture_allowlist.py`

## Audit Trail

- EXTRACTED: 275 (92%)
- INFERRED: 25 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*