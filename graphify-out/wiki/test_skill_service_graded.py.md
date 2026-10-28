# test_skill_service_graded.py

> 69 nodes · cohesion 0.07

## Key Concepts

- **ChatMessage** (65 connections) — `server/game/chat_message.py`
- **test_chat_message_senders.py** (32 connections) — `server/tests/unit/game/test_chat_message_senders.py`
- **_ctx()** (21 connections) — `server/tests/unit/game/test_chat_message_senders.py`
- **_attr()** (18 connections) — `server/tests/unit/game/test_chat_message_senders.py`
- **asyncio** (18 connections)
- **send_whisper_message()** (17 connections) — `server/game/chat_channel_message_senders.py`
- **send_system_message()** (16 connections) — `server/game/chat_channel_message_senders.py`
- **_player()** (16 connections) — `server/tests/unit/game/test_chat_message_senders.py`
- **send_party_message()** (11 connections) — `server/game/chat_channel_message_senders.py`
- **ChatResult** (10 connections)
- **_publish_chat_or_unavailable()** (9 connections) — `server/game/chat_channel_message_senders.py`
- **test_send_predefined_emote_format_error()** (8 connections) — `server/tests/unit/game/test_chat_message_senders.py`
- **normalize_player_id()** (7 connections) — `server/game/chat_channel_message_senders.py`
- **ChatMessage** (7 connections)
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
- **UUID** (6 connections)
- *... and 44 more nodes in this community*

## Relationships

- [test_monitoring_endpoints.py](test_monitoring_endpoints.py.md) (72 shared connections)
- [test_database_helpers.py](test_database_helpers.py.md) (9 shared connections)
- [ContainerData](ContainerData.md) (9 shared connections)
- [connection_cleanup_methods.py](connection_cleanup_methods.py.md) (5 shared connections)
- [deque](deque.md) (4 shared connections)
- [magic_service.py](magic_service.py.md) (3 shared connections)
- [test_lint_raw_sql_in_python.py](test_lint_raw_sql_in_python.py.md) (2 shared connections)
- [test_lucidity_recovery_commands.py](test_lucidity_recovery_commands.py.md) (1 shared connections)

## Source Files

- `server/game/chat_channel_message_senders.py`
- `server/game/chat_message.py`
- `server/tests/unit/game/test_chat_message_senders.py`
- `server/tests/unit/game/test_chat_npc_system.py`
- `server/tests/unit/game/test_chat_service.py`

## Audit Trail

- EXTRACTED: 243 (91%)
- INFERRED: 24 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*