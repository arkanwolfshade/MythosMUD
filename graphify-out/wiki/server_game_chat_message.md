# server game chat message

> 30 nodes

## Key Concepts

- **chat_message.py** (19 connections) — `server/game/chat_message.py`
- **create_and_log_chat_message()** (14 connections) — `server/game/chat_message_helpers.py`
- **chat_message_helpers.py** (13 connections) — `server/game/chat_message_helpers.py`
- **test_chat_message_helpers.py** (12 connections) — `server/tests/unit/game/test_chat_message_helpers.py`
- **store_message_in_room_history()** (11 connections) — `server/game/chat_message_helpers.py`
- **.send_say_message()** (11 connections) — `server/game/chat_service.py`
- **.send_emote_message()** (10 connections) — `server/game/chat_service.py`
- **create_and_log_say_message()** (7 connections) — `server/game/chat_message_helpers.py`
- **store_global_message_in_history()** (6 connections) — `server/game/chat_message_helpers.py`
- **_publish_room_chat()** (6 connections) — `server/game/chat_service.py`
- **._normalize_player_id()** (5 connections) — `server/game/chat_service.py`
- **_register_echo_suppression()** (3 connections) — `server/game/chat_service.py`
- **test_create_and_log_chat_message()** (3 connections) — `server/tests/unit/game/test_chat_message_helpers.py`
- **test_store_global_message_in_history_trims()** (3 connections) — `server/tests/unit/game/test_chat_message_helpers.py`
- **test_store_message_in_room_history_creates_and_trims()** (3 connections) — `server/tests/unit/game/test_chat_message_helpers.py`
- **.__init__()** (2 connections) — `server/game/chat_message.py`
- **_rate_limit_result()** (2 connections) — `server/game/chat_service.py`
- **test_create_and_log_say_message()** (2 connections) — `server/tests/unit/game/test_chat_message_helpers.py`
- **UUID** (2 connections)
- **ChatMessage** (1 connections)
- **Message creation and storage helpers for chat service.** (1 connections) — `server/game/chat_message_helpers.py`
- **Create chat message and log it.** (1 connections) — `server/game/chat_message_helpers.py`
- **Create say chat message and log it.** (1 connections) — `server/game/chat_message_helpers.py`
- **Store message in room history with limit management.** (1 connections) — `server/game/chat_message_helpers.py`
- **Store global message in history.** (1 connections) — `server/game/chat_message_helpers.py`
- *... and 5 more nodes in this community*

## Relationships

- [chatresult](chatresult.md) (22 shared connections)
- [server game chat message chatmessage](server_game_chat_message_chatmessage.md) (12 shared connections)
- [server game chat npc system](server_game_chat_npc_system.md) (7 shared connections)
- [server game chat service chatservice](server_game_chat_service_chatservice.md) (7 shared connections)
- [server game chat nats publisher](server_game_chat_nats_publisher.md) (5 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (3 shared connections)
- [server game chat pose helpers](server_game_chat_pose_helpers.md) (1 shared connections)

## Source Files

- `server/game/chat_message.py`
- `server/game/chat_message_helpers.py`
- `server/game/chat_service.py`
- `server/tests/unit/game/test_chat_message_helpers.py`

## Audit Trail

- EXTRACTED: 96 (95%)
- INFERRED: 5 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*