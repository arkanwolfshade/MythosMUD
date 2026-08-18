# server game chat channel message

> 88 nodes

## Key Concepts

- **chat_service.py** (59 connections) — `server/game/chat_service.py`
- **chat_message_senders.py** (30 connections) — `server/game/chat_message_senders.py`
- **UUID** (28 connections)
- **send_local_message()** (18 connections) — `server/game/chat_message_senders.py`
- **send_predefined_emote()** (17 connections) — `server/game/chat_message_senders.py`
- **create_and_log_chat_message()** (14 connections) — `server/game/chat_message_helpers.py`
- **send_party_message()** (14 connections) — `server/game/chat_message_senders.py`
- **ChatLogger** (13 connections) — `server/game/chat_channel_message_senders.py`
- **ChatUserManager** (13 connections) — `server/game/chat_channel_message_senders.py`
- **chat_message_helpers.py** (13 connections) — `server/game/chat_message_helpers.py`
- **ChatRateLimiter** (12 connections) — `server/game/chat_channel_message_senders.py`
- **chat_validation_helpers.py** (12 connections) — `server/game/chat_validation_helpers.py`
- **test_chat_message_helpers.py** (12 connections) — `server/tests/unit/game/test_chat_message_helpers.py`
- **ChatPlayerService** (11 connections) — `server/game/chat_channel_message_senders.py`
- **store_message_in_room_history()** (11 connections) — `server/game/chat_message_helpers.py`
- **.send_say_message()** (11 connections) — `server/game/chat_service.py`
- **.send_emote_message()** (10 connections) — `server/game/chat_service.py`
- **check_channel_permissions()** (10 connections) — `server/game/chat_validation_helpers.py`
- **normalize_player_id()** (8 connections) — `server/game/chat_message_senders.py`
- **create_and_log_say_message()** (7 connections) — `server/game/chat_message_helpers.py`
- **validate_say_message()** (7 connections) — `server/game/chat_validation_helpers.py`
- **store_global_message_in_history()** (6 connections) — `server/game/chat_message_helpers.py`
- **_publish_room_chat()** (6 connections) — `server/game/chat_service.py`
- **check_say_permissions()** (6 connections) — `server/game/chat_validation_helpers.py`
- **Protocol** (6 connections)
- *... and 63 more nodes in this community*

## Relationships

- [chatresult](chatresult.md) (53 shared connections)
- [server game chat service chatservice](server_game_chat_service_chatservice.md) (33 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (14 shared connections)
- [server game chat message](server_game_chat_message.md) (12 shared connections)
- [server container bundles chat chatbundle](server_container_bundles_chat_chatbundle.md) (8 shared connections)
- [server game chat pose helpers](server_game_chat_pose_helpers.md) (5 shared connections)
- [server command handler command input](server_command_handler_command_input.md) (2 shared connections)
- [server game chat moderation chatmoderation](server_game_chat_moderation_chatmoderation.md) (2 shared connections)
- [server game chat pose manager](server_game_chat_pose_manager.md) (1 shared connections)
- [server game chat whisper tracker](server_game_chat_whisper_tracker.md) (1 shared connections)
- [server api players](server_api_players.md) (1 shared connections)
- [server game chat moderation rationale](server_game_chat_moderation_rationale.md) (1 shared connections)

## Source Files

- `server/game/chat_channel_message_senders.py`
- `server/game/chat_message_helpers.py`
- `server/game/chat_message_senders.py`
- `server/game/chat_service.py`
- `server/game/chat_validation_helpers.py`
- `server/tests/unit/game/test_chat_message_helpers.py`
- `vulture_allowlist.py`

## Audit Trail

- EXTRACTED: 282 (94%)
- INFERRED: 17 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*