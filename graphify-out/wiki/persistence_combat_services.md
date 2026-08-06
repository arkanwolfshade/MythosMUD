# persistence combat services

> 26 nodes

## Key Concepts

- **_ChatMessageFields** (8 connections) — `server/realtime/nats_message_handler_processing.py`
- **_ValidatedChatFields** (8 connections) — `server/realtime/nats_message_handler_processing.py`
- **._process_single_message()** (8 connections) — `server/realtime/nats_message_handler_processing.py`
- **._handle_nats_message()** (6 connections) — `server/realtime/nats_message_handler_processing.py`
- **._process_message_with_retry()** (5 connections) — `server/realtime/nats_message_handler_processing.py`
- **._extract_chat_message_fields()** (5 connections) — `server/realtime/nats_message_handler_processing.py`
- **._validate_chat_message_fields()** (5 connections) — `server/realtime/nats_message_handler_processing.py`
- **._build_chat_event()** (5 connections) — `server/realtime/nats_message_handler_processing.py`
- **._broadcast_by_channel_type()** (5 connections) — `server/realtime/nats_message_handler_processing.py`
- **_optional_str()** (4 connections) — `server/realtime/nats_message_handler_processing.py`
- **_str_field()** (4 connections) — `server/realtime/nats_message_handler_processing.py`
- **._convert_ids_to_uuids()** (4 connections) — `server/realtime/nats_message_handler_processing.py`
- **UUID** (3 connections)
- **TypedDict** (2 connections)
- **Extracted chat fields before required-field validation.** (1 connections) — `server/realtime/nats_message_handler_processing.py`
- **Chat fields after required string fields are validated.** (1 connections) — `server/realtime/nats_message_handler_processing.py`
- **Narrow a message field to str | None.** (1 connections) — `server/realtime/nats_message_handler_processing.py`
- **Narrow a message field to str with a default.** (1 connections) — `server/realtime/nats_message_handler_processing.py`
- **Handle incoming NATS message with error boundaries.          Wraps message proce** (1 connections) — `server/realtime/nats_message_handler_processing.py`
- **Process message with retry logic.          Attempts message processing with expo** (1 connections) — `server/realtime/nats_message_handler_processing.py`
- **Process a single NATS message (original logic, can raise exceptions).          A** (1 connections) — `server/realtime/nats_message_handler_processing.py`
- **Extract and normalize chat message fields from message data.          Args:** (1 connections) — `server/realtime/nats_message_handler_processing.py`
- **Validate that all required chat message fields are present.          Args:** (1 connections) — `server/realtime/nats_message_handler_processing.py`
- **Build a WebSocket chat event from chat fields and formatted message.          Ar** (1 connections) — `server/realtime/nats_message_handler_processing.py`
- **Convert string IDs to UUIDs for broadcasting.          Args:             sender_** (1 connections) — `server/realtime/nats_message_handler_processing.py`
- *... and 1 more nodes in this community*

## Relationships

- [follow game service](follow_game_service.md) (10 shared connections)
- [Error Conversion](Error_Conversion.md) (5 shared connections)
- [message broadcast realtime](message_broadcast_realtime.md) (4 shared connections)
- [websocket handler realtime](websocket_handler_realtime.md) (2 shared connections)
- [game chat service](game_chat_service.md) (2 shared connections)
- [schemas nats messages](schemas_nats_messages.md) (1 shared connections)
- [npc lifecycle combat](npc_lifecycle_combat.md) (1 shared connections)
- [combat services messaging](combat_services_messaging.md) (1 shared connections)

## Source Files

- `server/realtime/nats_message_handler_processing.py`

## Audit Trail

- EXTRACTED: 76 (90%)
- INFERRED: 8 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*