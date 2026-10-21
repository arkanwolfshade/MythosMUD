# test_monitoring_endpoints.py

> 123 nodes · cohesion 0.03

## Key Concepts

- **chat_service.py** (60 connections) — `server/game/chat_service.py`
- **chat_channel_message_senders.py** (40 connections) — `server/game/chat_channel_message_senders.py`
- **chat_message_senders.py** (37 connections) — `server/game/chat_message_senders.py`
- **ChatSendServices** (26 connections) — `server/game/chat_channel_message_senders.py`
- **chat_message.py** (23 connections) — `server/game/chat_message.py`
- **send_local_message()** (16 connections) — `server/game/chat_message_senders.py`
- **send_predefined_emote()** (16 connections) — `server/game/chat_message_senders.py`
- **send_global_message()** (14 connections) — `server/game/chat_channel_message_senders.py`
- **create_and_log_chat_message()** (14 connections) — `server/game/chat_message_helpers.py`
- **send_party_message()** (14 connections) — `server/game/chat_message_senders.py`
- **ChatPlayerView** (13 connections) — `server/game/chat_channel_message_senders.py`
- **chat_message_helpers.py** (13 connections) — `server/game/chat_message_helpers.py`
- **ChatLogger** (12 connections) — `server/game/chat_channel_message_senders.py`
- **chat_validation_helpers.py** (12 connections) — `server/game/chat_validation_helpers.py`
- **test_chat_message_helpers.py** (12 connections) — `server/tests/unit/game/test_chat_message_helpers.py`
- **ChatUserManager** (11 connections) — `server/game/chat_channel_message_senders.py`
- **store_message_in_room_history()** (11 connections) — `server/game/chat_message_helpers.py`
- **.send_say_message()** (11 connections) — `server/game/chat_service.py`
- **ChatEmoteService** (10 connections) — `server/game/chat_channel_message_senders.py`
- **ChatRateLimiter** (10 connections) — `server/game/chat_channel_message_senders.py`
- **check_channel_permissions()** (10 connections) — `server/game/chat_validation_helpers.py`
- **ChatPlayerService** (9 connections) — `server/game/chat_channel_message_senders.py`
- **_build_and_log_emote_message()** (9 connections) — `server/game/chat_message_senders.py`
- **_publish_chat_or_unavailable()** (9 connections) — `server/game/chat_message_senders.py`
- **_log_and_store_whisper_message()** (8 connections) — `server/game/chat_channel_message_senders.py`
- *... and 98 more nodes in this community*

## Relationships

- [test_skill_service_graded.py](test_skill_service_graded.py.md) (72 shared connections)
- [ContainerData](ContainerData.md) (21 shared connections)
- [Room](Room.md) (17 shared connections)
- [connection_cleanup_methods.py](connection_cleanup_methods.py.md) (11 shared connections)
- [test_database_helpers.py](test_database_helpers.py.md) (10 shared connections)
- [test_lint_raw_sql_in_python.py](test_lint_raw_sql_in_python.py.md) (6 shared connections)
- [UUID](UUID.md) (3 shared connections)
- [look_container.py](look_container.py.md) (2 shared connections)
- [magic_service.py](magic_service.py.md) (2 shared connections)
- [deque](deque.md) (2 shared connections)
- [Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Berlin - The Wicked City  (2026-08-11)](Graph_Report_-_C-_Users_arkan_Proton_Drive_arkanwolfshade_My_files_Chaosium_Berlin_-_The_Wicked_City__2026-08-11.md) (2 shared connections)
- [container_endpoints_basic.py](container_endpoints_basic.py.md) (2 shared connections)

## Source Files

- `server/game/chat_channel_message_senders.py`
- `server/game/chat_message.py`
- `server/game/chat_message_helpers.py`
- `server/game/chat_message_senders.py`
- `server/game/chat_service.py`
- `server/game/chat_validation_helpers.py`
- `server/tests/unit/game/test_chat_message_helpers.py`

## Audit Trail

- EXTRACTED: 378 (93%)
- INFERRED: 30 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*