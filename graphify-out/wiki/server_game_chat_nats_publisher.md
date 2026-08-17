# server game chat nats publisher

> 55 nodes

## Key Concepts

- **test_chat_nats_publisher.py** (36 connections) — `server/tests/unit/game/test_chat_nats_publisher.py`
- **chat_nats_publisher.py** (32 connections) — `server/game/chat_nats_publisher.py`
- **publish_chat_message_to_nats()** (29 connections) — `server/game/chat_nats_publisher.py`
- **_message()** (24 connections) — `server/tests/unit/game/test_chat_nats_publisher.py`
- **build_nats_subject()** (13 connections) — `server/game/chat_nats_publisher.py`
- **_build_legacy_subject()** (11 connections) — `server/game/chat_nats_publisher.py`
- **_build_standardized_subject()** (8 connections) — `server/game/chat_nats_publisher.py`
- **_nats_service_ready()** (8 connections) — `server/game/chat_nats_publisher.py`
- **Any** (8 connections)
- **_extract_subzone_from_room()** (7 connections) — `server/game/chat_nats_publisher.py`
- **_build_nats_message_data()** (6 connections) — `server/game/chat_nats_publisher.py`
- **_subject_system_standardized()** (5 connections) — `server/game/chat_nats_publisher.py`
- **_subject_whisper_standardized()** (5 connections) — `server/game/chat_nats_publisher.py`
- **test_publish_chat_message_to_nats_handles_publish_error()** (5 connections) — `server/tests/unit/game/test_chat_nats_publisher.py`
- **asyncio** (5 connections)
- **_log_nats_publish_error()** (4 connections) — `server/game/chat_nats_publisher.py`
- **_log_nats_unexpected_error()** (4 connections) — `server/game/chat_nats_publisher.py`
- **_subject_party_standardized()** (4 connections) — `server/game/chat_nats_publisher.py`
- **test_publish_chat_message_to_nats_room_access_failure()** (4 connections) — `server/tests/unit/game/test_chat_nats_publisher.py`
- **test_publish_chat_message_to_nats_success()** (4 connections) — `server/tests/unit/game/test_chat_nats_publisher.py`
- **test_publish_chat_message_to_nats_unexpected_error()** (4 connections) — `server/tests/unit/game/test_chat_nats_publisher.py`
- **test_publish_chat_message_to_nats_validation_failure()** (4 connections) — `server/tests/unit/game/test_chat_nats_publisher.py`
- **test_build_legacy_subject_global()** (3 connections) — `server/tests/unit/game/test_chat_nats_publisher.py`
- **test_build_legacy_subject_local_uses_subzone()** (3 connections) — `server/tests/unit/game/test_chat_nats_publisher.py`
- **test_build_legacy_subject_party_with_id()** (3 connections) — `server/tests/unit/game/test_chat_nats_publisher.py`
- *... and 30 more nodes in this community*

## Relationships

- [chatresult](chatresult.md) (8 shared connections)
- [server realtime message formatters](server_realtime_message_formatters.md) (6 shared connections)
- [server game chat message chatmessage](server_game_chat_message_chatmessage.md) (6 shared connections)
- [server game chat nats publisher](server_game_chat_nats_publisher.md) (5 shared connections)
- [server game chat npc system](server_game_chat_npc_system.md) (4 shared connections)
- [server game chat pose helpers](server_game_chat_pose_helpers.md) (3 shared connections)
- [server game chat message](server_game_chat_message.md) (3 shared connections)
- [server tests unit utils test](server_tests_unit_utils_test.md) (2 shared connections)
- [server services nats subject manager](server_services_nats_subject_manager.md) (2 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (2 shared connections)
- [characterinfo](characterinfo.md) (1 shared connections)

## Source Files

- `server/game/chat_nats_publisher.py`
- `server/tests/unit/game/test_chat_nats_publisher.py`

## Audit Trail

- EXTRACTED: 167 (99%)
- INFERRED: 2 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*