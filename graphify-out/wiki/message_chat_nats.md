# message chat nats

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

- [realtime nats message](realtime_nats_message.md) (15 shared connections)
- [message realtime nats](message_realtime_nats.md) (7 shared connections)
- [message chat realtime](message_chat_realtime.md) (5 shared connections)
- [game room service](game_room_service.md) (4 shared connections)
- [Item Instances](Item_Instances.md) (2 shared connections)
- [chat realtime nats](chat_realtime_nats.md) (2 shared connections)

## Source Files

- `server/tests/unit/realtime/test_nats_message_handler_chat.py`

## Audit Trail

- EXTRACTED: 53 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*