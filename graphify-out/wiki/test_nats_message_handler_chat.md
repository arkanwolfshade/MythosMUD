# test nats message handler chat

> 10 nodes

## Key Concepts

- **test_nats_message_handler_chat.py** (40 connections) — `server/tests/unit/realtime/test_nats_message_handler_chat.py`
- **test_validate_chat_message_fields_missing()** (2 connections) — `server/tests/unit/realtime/test_nats_message_handler_chat.py`
- **test_convert_ids_to_uuids()** (2 connections) — `server/tests/unit/realtime/test_nats_message_handler_chat.py`
- **test_apply_dampening_and_send_message_exception()** (2 connections) — `server/tests/unit/realtime/test_nats_message_handler_chat.py`
- **test_get_player_lucidity_tier_exception_in_processing()** (2 connections) — `server/tests/unit/realtime/test_nats_message_handler_chat.py`
- **Unit tests for NATS message handler chat and messaging.  Tests chat field extrac** (1 connections) — `server/tests/unit/realtime/test_nats_message_handler_chat.py`
- **Test _validate_chat_message_fields raises error when fields missing.** (1 connections) — `server/tests/unit/realtime/test_nats_message_handler_chat.py`
- **Test _convert_ids_to_uuids converts IDs.** (1 connections) — `server/tests/unit/realtime/test_nats_message_handler_chat.py`
- **Test _apply_dampening_and_send_message handles exceptions.** (1 connections) — `server/tests/unit/realtime/test_nats_message_handler_chat.py`
- **Test _get_player_lucidity_tier handles exceptions during processing.** (1 connections) — `server/tests/unit/realtime/test_nats_message_handler_chat.py`

## Relationships

- [Test parse exits json with](Test_parse_exits_json_with.md) (3 shared connections)
- [Any](Any.md) (2 shared connections)
- [Test generate room id from](Test_generate_room_id_from.md) (2 shared connections)
- [test_apply_dampening_and_send_message_blocked](test_apply_dampening_and_send_message_blocked.md) (1 shared connections)
- [.is unlocked()](is_unlocked%28%29.md) (1 shared connections)
- [.can hold()](can_hold%28%29.md) (1 shared connections)
- [Test load room cache async](Test_load_room_cache_async.md) (1 shared connections)
- [.get used slots()](get_used_slots%28%29.md) (1 shared connections)
- [Migration 019 Verification](Migration_019_Verification.md) (1 shared connections)
- [Test get players batch with](Test_get_players_batch_with.md) (1 shared connections)
- [Hash password using Argon2 instead](Hash_password_using_Argon2_instead.md) (1 shared connections)
- [Verify password using Argon2 instead](Verify_password_using_Argon2_instead.md) (1 shared connections)

## Source Files

- `server/tests/unit/realtime/test_nats_message_handler_chat.py`

## Audit Trail

- EXTRACTED: 53 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*