# ChatMessage

> 43 nodes

## Key Concepts

- **ChatMessage** (59 connections) — `server/game/chat_message.py`
- **test_chat_message_senders.py** (28 connections) — `server/tests/unit/game/test_chat_message_senders.py`
- **_attr()** (13 connections) — `server/tests/unit/game/test_chat_message_senders.py`
- **asyncio** (13 connections)
- **_ctx()** (12 connections) — `server/tests/unit/game/test_chat_message_senders.py`
- **_player()** (11 connections) — `server/tests/unit/game/test_chat_message_senders.py`
- **test_send_global_message_success()** (7 connections) — `server/tests/unit/game/test_chat_message_senders.py`
- **test_send_system_message_rate_limit_and_nats_fail()** (7 connections) — `server/tests/unit/game/test_chat_message_senders.py`
- **test_send_system_message_success()** (7 connections) — `server/tests/unit/game/test_chat_message_senders.py`
- **test_send_system_message_validation_and_auth()** (7 connections) — `server/tests/unit/game/test_chat_message_senders.py`
- **test_send_whisper_message_success()** (7 connections) — `server/tests/unit/game/test_chat_message_senders.py`
- **test_send_local_message_success_with_echo_suppression()** (6 connections) — `server/tests/unit/game/test_chat_message_senders.py`
- **test_send_whisper_message_target_missing_and_rate_limit()** (6 connections) — `server/tests/unit/game/test_chat_message_senders.py`
- **test_send_local_message_player_not_in_room()** (5 connections) — `server/tests/unit/game/test_chat_message_senders.py`
- **test_send_party_message_paths()** (5 connections) — `server/tests/unit/game/test_chat_message_senders.py`
- **test_send_predefined_emote_success()** (5 connections) — `server/tests/unit/game/test_chat_message_senders.py`
- **test_send_whisper_message_validation()** (5 connections) — `server/tests/unit/game/test_chat_message_senders.py`
- **test_send_global_message_player_not_found()** (4 connections) — `server/tests/unit/game/test_chat_message_senders.py`
- **test_send_predefined_emote_unknown()** (4 connections) — `server/tests/unit/game/test_chat_message_senders.py`
- **.to_dict()** (3 connections) — `server/game/chat_message.py`
- **test_chat_message_to_dict_includes_speaker_kind()** (3 connections) — `server/tests/unit/game/test_chat_npc_system.py`
- **test_chat_message_init()** (3 connections) — `server/tests/unit/game/test_chat_service.py`
- **test_chat_message_init_with_target()** (3 connections) — `server/tests/unit/game/test_chat_service.py`
- **test_chat_message_log_message()** (3 connections) — `server/tests/unit/game/test_chat_service.py`
- **test_chat_message_to_dict()** (3 connections) — `server/tests/unit/game/test_chat_service.py`
- *... and 18 more nodes in this community*

## Relationships

- [chat_service.py](chat_service.py.md) (22 shared connections)
- [chat_channel_message_senders.py](chat_channel_message_senders.py.md) (20 shared connections)
- [ChatService](ChatService.md) (10 shared connections)
- [test_chat_npc_system.py](test_chat_npc_system.py.md) (7 shared connections)
- [test_chat_validator.py](test_chat_validator.py.md) (6 shared connections)
- [test_chat_nats_publisher.py](test_chat_nats_publisher.py.md) (3 shared connections)
- [test_chat_pose_helpers.py](test_chat_pose_helpers.py.md) (2 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/game/chat_message.py`
- `server/tests/unit/game/test_chat_message_senders.py`
- `server/tests/unit/game/test_chat_npc_system.py`
- `server/tests/unit/game/test_chat_service.py`

## Audit Trail

- EXTRACTED: 141 (87%)
- INFERRED: 21 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*