# test_chat_message_senders.py

> 33 nodes

## Key Concepts

- **test_chat_message_senders.py** (27 connections) — `server/tests/unit/game/test_chat_message_senders.py`
- **send_local_message()** (17 connections) — `server/game/chat_message_senders.py`
- **send_predefined_emote()** (16 connections) — `server/game/chat_message_senders.py`
- **send_party_message()** (13 connections) — `server/game/chat_message_senders.py`
- **_attr()** (13 connections) — `server/tests/unit/game/test_chat_message_senders.py`
- **asyncio** (13 connections)
- **_ctx()** (11 connections) — `server/tests/unit/game/test_chat_message_senders.py`
- **_player()** (11 connections) — `server/tests/unit/game/test_chat_message_senders.py`
- **normalize_player_id()** (8 connections) — `server/game/chat_message_senders.py`
- **test_send_global_message_success()** (6 connections) — `server/tests/unit/game/test_chat_message_senders.py`
- **test_send_system_message_rate_limit_and_nats_fail()** (6 connections) — `server/tests/unit/game/test_chat_message_senders.py`
- **test_send_system_message_success()** (6 connections) — `server/tests/unit/game/test_chat_message_senders.py`
- **test_send_system_message_validation_and_auth()** (6 connections) — `server/tests/unit/game/test_chat_message_senders.py`
- **test_send_whisper_message_success()** (6 connections) — `server/tests/unit/game/test_chat_message_senders.py`
- **test_send_whisper_message_target_missing_and_rate_limit()** (6 connections) — `server/tests/unit/game/test_chat_message_senders.py`
- **test_send_local_message_player_not_in_room()** (5 connections) — `server/tests/unit/game/test_chat_message_senders.py`
- **test_send_local_message_success_with_echo_suppression()** (5 connections) — `server/tests/unit/game/test_chat_message_senders.py`
- **test_send_party_message_paths()** (5 connections) — `server/tests/unit/game/test_chat_message_senders.py`
- **test_send_predefined_emote_success()** (5 connections) — `server/tests/unit/game/test_chat_message_senders.py`
- **UUID** (5 connections)
- **test_send_global_message_player_not_found()** (4 connections) — `server/tests/unit/game/test_chat_message_senders.py`
- **test_send_predefined_emote_unknown()** (4 connections) — `server/tests/unit/game/test_chat_message_senders.py`
- **test_send_whisper_message_validation()** (4 connections) — `server/tests/unit/game/test_chat_message_senders.py`
- **ChatMessage** (3 connections)
- **test_normalize_player_id()** (2 connections) — `server/tests/unit/game/test_chat_message_senders.py`
- *... and 8 more nodes in this community*

## Relationships

- [chat_service.py](chat_service.py.md) (24 shared connections)
- [chat_channel_message_senders.py](chat_channel_message_senders.py.md) (12 shared connections)
- [test_chat_nats_publisher.py](test_chat_nats_publisher.py.md) (3 shared connections)
- [EmoteService](EmoteService.md) (1 shared connections)

## Source Files

- `server/game/chat_message_senders.py`
- `server/tests/unit/game/test_chat_message_senders.py`

## Audit Trail

- EXTRACTED: 128 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*