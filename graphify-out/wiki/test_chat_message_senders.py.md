# test_chat_message_senders.py

> 47 nodes

## Key Concepts

- **test_chat_message_senders.py** (32 connections) — `server/tests/unit/game/test_chat_message_senders.py`
- **_ctx()** (21 connections) — `server/tests/unit/game/test_chat_message_senders.py`
- **_attr()** (18 connections) — `server/tests/unit/game/test_chat_message_senders.py`
- **asyncio** (18 connections)
- **send_local_message()** (16 connections) — `server/game/chat_message_senders.py`
- **send_predefined_emote()** (16 connections) — `server/game/chat_message_senders.py`
- **_player()** (16 connections) — `server/tests/unit/game/test_chat_message_senders.py`
- **send_party_message()** (14 connections) — `server/game/chat_message_senders.py`
- **_publish_chat_or_unavailable()** (9 connections) — `server/game/chat_message_senders.py`
- **normalize_player_id()** (8 connections) — `server/game/chat_message_senders.py`
- **test_send_predefined_emote_format_error()** (8 connections) — `server/tests/unit/game/test_chat_message_senders.py`
- **test_send_global_message_success()** (7 connections) — `server/tests/unit/game/test_chat_message_senders.py`
- **test_send_local_message_nats_failure()** (7 connections) — `server/tests/unit/game/test_chat_message_senders.py`
- **test_send_local_message_permission_denied()** (7 connections) — `server/tests/unit/game/test_chat_message_senders.py`
- **test_send_local_message_success_with_echo_suppression()** (7 connections) — `server/tests/unit/game/test_chat_message_senders.py`
- **test_send_predefined_emote_nats_failure()** (7 connections) — `server/tests/unit/game/test_chat_message_senders.py`
- **test_send_predefined_emote_player_muted_in_say()** (7 connections) — `server/tests/unit/game/test_chat_message_senders.py`
- **test_send_system_message_rate_limit_and_nats_fail()** (7 connections) — `server/tests/unit/game/test_chat_message_senders.py`
- **test_send_system_message_success()** (7 connections) — `server/tests/unit/game/test_chat_message_senders.py`
- **test_send_system_message_validation_and_auth()** (7 connections) — `server/tests/unit/game/test_chat_message_senders.py`
- **test_send_whisper_message_success()** (7 connections) — `server/tests/unit/game/test_chat_message_senders.py`
- **test_send_local_message_player_not_in_room()** (6 connections) — `server/tests/unit/game/test_chat_message_senders.py`
- **test_send_predefined_emote_success()** (6 connections) — `server/tests/unit/game/test_chat_message_senders.py`
- **test_send_whisper_message_target_missing_and_rate_limit()** (6 connections) — `server/tests/unit/game/test_chat_message_senders.py`
- **test_send_party_message_paths()** (5 connections) — `server/tests/unit/game/test_chat_message_senders.py`
- *... and 22 more nodes in this community*

## Relationships

- [chat_channel_message_senders.py](chat_channel_message_senders.py.md) (31 shared connections)
- [ChatMessage](ChatMessage.md) (17 shared connections)
- [test_chat_nats_publisher.py](test_chat_nats_publisher.py.md) (2 shared connections)
- [ValueError](ValueError.md) (1 shared connections)

## Source Files

- `server/game/chat_message_senders.py`
- `server/tests/unit/game/test_chat_message_senders.py`

## Audit Trail

- EXTRACTED: 163 (90%)
- INFERRED: 18 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*