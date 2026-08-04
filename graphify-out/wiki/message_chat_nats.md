# message chat nats

> 10 nodes

## Key Concepts

- **test_nats_message_handler_chat.py** (40 connections) — `server/tests/unit/realtime/test_nats_message_handler_chat.py`
- **test_validate_chat_message_fields_missing()** (2 connections) — `server/tests/unit/realtime/test_nats_message_handler_chat.py`
- **test_convert_ids_to_uuids()** (2 connections) — `server/tests/unit/realtime/test_nats_message_handler_chat.py`
- **test_apply_dampening_and_send_message_blocked()** (2 connections) — `server/tests/unit/realtime/test_nats_message_handler_chat.py`
- **test_get_player_lucidity_tier_exception_in_processing()** (2 connections) — `server/tests/unit/realtime/test_nats_message_handler_chat.py`
- **Unit tests for NATS message handler chat and messaging.  Tests chat field extrac** (1 connections) — `server/tests/unit/realtime/test_nats_message_handler_chat.py`
- **Test _validate_chat_message_fields raises error when fields missing.** (1 connections) — `server/tests/unit/realtime/test_nats_message_handler_chat.py`
- **Test _convert_ids_to_uuids converts IDs.** (1 connections) — `server/tests/unit/realtime/test_nats_message_handler_chat.py`
- **Test _apply_dampening_and_send_message handles blocked messages.** (1 connections) — `server/tests/unit/realtime/test_nats_message_handler_chat.py`
- **Test _get_player_lucidity_tier handles exceptions during processing.** (1 connections) — `server/tests/unit/realtime/test_nats_message_handler_chat.py`

## Relationships

- [room infrastructure persistence](room_infrastructure_persistence.md) (18 shared connections)
- [infrastructure persistence room](infrastructure_persistence_room.md) (10 shared connections)
- [room cache infrastructure](room_cache_infrastructure.md) (5 shared connections)
- [NPC Combat](NPC_Combat.md) (1 shared connections)
- [commands communication say](commands_communication_say.md) (1 shared connections)

## Source Files

- `server/tests/unit/realtime/test_nats_message_handler_chat.py`

## Audit Trail

- EXTRACTED: 53 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*