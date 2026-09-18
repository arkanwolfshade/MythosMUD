# Community 451

> 39 nodes

## Key Concepts

- **NATSMessageHandlerMixinBase** (17 connections) — `server/realtime/nats_message_handler_base.py`
- **NATSMessageProcessingMixin** (15 connections) — `server/realtime/nats_message_handler_processing.py`
- **._process_single_message()** (8 connections) — `server/realtime/nats_message_handler_processing.py`
- **test_nats_message_handler_base.py** (6 connections) — `server/tests/unit/realtime/test_nats_message_handler_base.py`
- **_ChatMessageFields** (5 connections) — `server/realtime/nats_message_handler_processing.py`
- **_ValidatedChatFields** (5 connections) — `server/realtime/nats_message_handler_processing.py`
- **_Handler** (5 connections) — `server/tests/unit/realtime/test_nats_message_handler_base.py`
- **._build_chat_event()** (5 connections) — `server/realtime/nats_message_handler_processing.py`
- **._extract_chat_message_fields()** (5 connections) — `server/realtime/nats_message_handler_processing.py`
- **._handle_nats_message()** (5 connections) — `server/realtime/nats_message_handler_processing.py`
- **._process_message_with_retry()** (5 connections) — `server/realtime/nats_message_handler_processing.py`
- **._validate_chat_message_fields()** (5 connections) — `server/realtime/nats_message_handler_processing.py`
- **._broadcast_by_channel_type()** (4 connections) — `server/realtime/nats_message_handler_processing.py`
- **._convert_ids_to_uuids()** (4 connections) — `server/realtime/nats_message_handler_processing.py`
- **_optional_str()** (4 connections) — `server/realtime/nats_message_handler_processing.py`
- **_str_field()** (4 connections) — `server/realtime/nats_message_handler_processing.py`
- **test_subscribe_stub_returns_false()** (3 connections) — `server/tests/unit/realtime/test_nats_message_handler_base.py`
- **test_unsubscribe_stub_returns_false()** (3 connections) — `server/tests/unit/realtime/test_nats_message_handler_base.py`
- **UUID** (3 connections)
- **TypedDict** (2 connections)
- **asyncio** (2 connections)
- **._subscribe_to_subject()** (1 connections) — `server/realtime/nats_message_handler_base.py`
- **._unsubscribe_from_subject()** (1 connections) — `server/realtime/nats_message_handler_base.py`
- **Attrs/methods provided by NATSMessageHandler when mixed in.** (1 connections) — `server/realtime/nats_message_handler_base.py`
- **Process message with retry logic. Attempts message processing with exponential…** (1 connections) — `server/realtime/nats_message_handler_processing.py`
- *... and 14 more nodes in this community*

## Relationships

- [Realtime Message Filtering & Formatting](Realtime_Message_Filtering_&_Formatting.md) (13 shared connections)
- [Community 153](Community_153.md) (4 shared connections)
- [Community 127](Community_127.md) (2 shared connections)
- [Community 427](Community_427.md) (1 shared connections)
- [Community 292](Community_292.md) (1 shared connections)
- [Community 233](Community_233.md) (1 shared connections)
- [Community 335](Community_335.md) (1 shared connections)
- [Community 132](Community_132.md) (1 shared connections)
- [Community 87](Community_87.md) (1 shared connections)
- [Community 62](Community_62.md) (1 shared connections)
- [Community 293](Community_293.md) (1 shared connections)

## Source Files

- `server/realtime/nats_message_handler_base.py`
- `server/realtime/nats_message_handler_processing.py`
- `server/tests/unit/realtime/test_nats_message_handler_base.py`

## Audit Trail

- EXTRACTED: 73 (91%)
- INFERRED: 7 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*