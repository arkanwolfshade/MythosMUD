# server tests unit realtime test

> 17 nodes

## Key Concepts

- **asyncio** (16 connections)
- **test_echo_message_to_sender_exception()** (4 connections) — `server/tests/unit/realtime/test_nats_message_handler_chat.py`
- **test_apply_dampening_and_send_message_blocked()** (3 connections) — `server/tests/unit/realtime/test_nats_message_handler_chat.py`
- **test_apply_dampening_and_send_message_exception()** (3 connections) — `server/tests/unit/realtime/test_nats_message_handler_chat.py`
- **test_get_player_lucidity_tier()** (3 connections) — `server/tests/unit/realtime/test_nats_message_handler_chat.py`
- **test_get_player_lucidity_tier_default()** (3 connections) — `server/tests/unit/realtime/test_nats_message_handler_chat.py`
- **test_get_player_lucidity_tier_exception_in_processing()** (3 connections) — `server/tests/unit/realtime/test_nats_message_handler_chat.py`
- **test_send_messages_to_players_invalid_player_id()** (3 connections) — `server/tests/unit/realtime/test_nats_message_handler_chat.py`
- **test_send_messages_to_players_no_original_content()** (3 connections) — `server/tests/unit/realtime/test_nats_message_handler_chat.py`
- **Test _get_player_lucidity_tier returns default on error.** (1 connections) — `server/tests/unit/realtime/test_nats_message_handler_chat.py`
- **Test _send_messages_to_players handles missing original_content.** (1 connections) — `server/tests/unit/realtime/test_nats_message_handler_chat.py`
- **Test _send_messages_to_players handles invalid player_id.** (1 connections) — `server/tests/unit/realtime/test_nats_message_handler_chat.py`
- **Test _echo_message_to_sender handles exceptions.** (1 connections) — `server/tests/unit/realtime/test_nats_message_handler_chat.py`
- **Test _apply_dampening_and_send_message handles blocked messages.** (1 connections) — `server/tests/unit/realtime/test_nats_message_handler_chat.py`
- **Test _apply_dampening_and_send_message handles exceptions.** (1 connections) — `server/tests/unit/realtime/test_nats_message_handler_chat.py`
- **Test _get_player_lucidity_tier handles exceptions during processing.** (1 connections) — `server/tests/unit/realtime/test_nats_message_handler_chat.py`
- **Test _get_player_lucidity_tier gets tier.** (1 connections) — `server/tests/unit/realtime/test_nats_message_handler_chat.py`

## Relationships

- [server tests unit realtime test](server_tests_unit_realtime_test.md) (16 shared connections)
- [server realtime message formatters](server_realtime_message_formatters.md) (1 shared connections)

## Source Files

- `server/tests/unit/realtime/test_nats_message_handler_chat.py`

## Audit Trail

- EXTRACTED: 32 (97%)
- INFERRED: 1 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*