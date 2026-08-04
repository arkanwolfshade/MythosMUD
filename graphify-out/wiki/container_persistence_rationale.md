# container persistence rationale

> 112 nodes

## Key Concepts

- **DeadLetterQueue** (37 connections) — `server/realtime/dead_letter_queue.py`
- **test_dead_letter_queue.py** (28 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **DeadLetterMessage** (27 connections) — `server/realtime/dead_letter_queue.py`
- **NATSMessageHandlerMixinBase** (19 connections) — `server/realtime/nats_message_handler_base.py`
- **NATSMessageProcessingMixin** (15 connections) — `server/realtime/nats_message_handler_processing.py`
- **_ChatMessageFields** (8 connections) — `server/realtime/nats_message_handler_processing.py`
- **_ValidatedChatFields** (8 connections) — `server/realtime/nats_message_handler_processing.py`
- **._process_single_message()** (8 connections) — `server/realtime/nats_message_handler_processing.py`
- **Any** (7 connections)
- **.from_dict()** (6 connections) — `server/realtime/dead_letter_queue.py`
- **._handle_nats_message()** (6 connections) — `server/realtime/nats_message_handler_processing.py`
- **.to_dict()** (5 connections) — `server/realtime/dead_letter_queue.py`
- **.enqueue_async()** (5 connections) — `server/realtime/dead_letter_queue.py`
- **Path** (5 connections)
- **.enqueue()** (5 connections) — `server/realtime/dead_letter_queue.py`
- **._process_message_with_retry()** (5 connections) — `server/realtime/nats_message_handler_processing.py`
- **._extract_chat_message_fields()** (5 connections) — `server/realtime/nats_message_handler_processing.py`
- **._validate_chat_message_fields()** (5 connections) — `server/realtime/nats_message_handler_processing.py`
- **._build_chat_event()** (5 connections) — `server/realtime/nats_message_handler_processing.py`
- **._broadcast_by_channel_type()** (5 connections) — `server/realtime/nats_message_handler_processing.py`
- **.__init__()** (4 connections) — `server/realtime/dead_letter_queue.py`
- **.replay_message()** (4 connections) — `server/realtime/dead_letter_queue.py`
- **_optional_str()** (4 connections) — `server/realtime/nats_message_handler_processing.py`
- **_str_field()** (4 connections) — `server/realtime/nats_message_handler_processing.py`
- **._convert_ids_to_uuids()** (4 connections) — `server/realtime/nats_message_handler_processing.py`
- *... and 87 more nodes in this community*

## Relationships

- [NPC Combat](NPC_Combat.md) (17 shared connections)
- [commands communication say](commands_communication_say.md) (8 shared connections)
- [config rationale config()](config_rationale_config%28%29.md) (3 shared connections)
- [logging structured utilities](logging_structured_utilities.md) (2 shared connections)
- [models npc rationale](models_npc_rationale.md) (1 shared connections)
- [websocket handler realtime](websocket_handler_realtime.md) (1 shared connections)
- [follow game service](follow_game_service.md) (1 shared connections)
- [circuit breaker realtime](circuit_breaker_realtime.md) (1 shared connections)
- [persistence core infrastructure](persistence_core_infrastructure.md) (1 shared connections)
- [schemas nats messages](schemas_nats_messages.md) (1 shared connections)
- [room look commands](room_look_commands.md) (1 shared connections)

## Source Files

- `server/realtime/dead_letter_queue.py`
- `server/realtime/nats_message_handler_base.py`
- `server/realtime/nats_message_handler_processing.py`
- `server/tests/unit/realtime/test_dead_letter_queue.py`

## Audit Trail

- EXTRACTED: 367 (93%)
- INFERRED: 28 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*