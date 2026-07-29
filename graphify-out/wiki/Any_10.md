# Any

> 49 nodes

## Key Concepts

- **NATSMessageHandler** (24 connections) — `server/realtime/nats_message_handler.py`
- **RealtimeBundle** (17 connections) — `server/container/bundles/realtime.py`
- **NATSMessageProcessingMixin** (15 connections) — `server/realtime/nats_message_handler_processing.py`
- **realtime.py** (12 connections) — `server/container/bundles/realtime.py`
- **._process_single_message()** (9 connections) — `server/realtime/nats_message_handler_processing.py`
- **.initialize()** (8 connections) — `server/container/bundles/realtime.py`
- **Any** (7 connections)
- **._setup_nats_dependent_services()** (6 connections) — `server/container/bundles/realtime.py`
- **._handle_nats_message()** (6 connections) — `server/realtime/nats_message_handler_processing.py`
- **._broadcast_by_channel_type()** (6 connections) — `server/realtime/nats_message_handler_processing.py`
- **._connect_nats()** (5 connections) — `server/container/bundles/realtime.py`
- **._subscribe_to_standardized_chat_subjects()** (5 connections) — `server/realtime/nats_message_handler.py`
- **._build_chat_event()** (5 connections) — `server/realtime/nats_message_handler_processing.py`
- **._require_core_services()** (4 connections) — `server/container/bundles/realtime.py`
- **.start()** (4 connections) — `server/realtime/nats_message_handler.py`
- **.stop()** (4 connections) — `server/realtime/nats_message_handler.py`
- **._subscribe_to_chat_subjects()** (4 connections) — `server/realtime/nats_message_handler.py`
- **._subscribe_to_subject()** (4 connections) — `server/realtime/nats_message_handler.py`
- **._unsubscribe_from_subject()** (4 connections) — `server/realtime/nats_message_handler.py`
- **._process_message_with_retry()** (4 connections) — `server/realtime/nats_message_handler_processing.py`
- **._extract_chat_message_fields()** (4 connections) — `server/realtime/nats_message_handler_processing.py`
- **._validate_chat_message_fields()** (4 connections) — `server/realtime/nats_message_handler_processing.py`
- **._convert_ids_to_uuids()** (4 connections) — `server/realtime/nats_message_handler_processing.py`
- **UUID** (3 connections)
- **nats_message_handler()** (3 connections) — `server/tests/unit/realtime/conftest.py`
- *... and 24 more nodes in this community*

## Relationships

- [. init ()](_init_%28%29.md) (9 shared connections)
- [.initialize()](initialize%28%29.md) (6 shared connections)
- [.shutdown()](shutdown%28%29.md) (5 shared connections)
- [UUID](UUID.md) (5 shared connections)
- [Player](Player.md) (4 shared connections)
- [DeadLetterMessage](DeadLetterMessage.md) (4 shared connections)
- [Any](Any.md) (3 shared connections)
- [event publisher()](event_publisher%28%29.md) (3 shared connections)
- [NATS](NATS.md) (3 shared connections)
- [message formatters](message_formatters.md) (3 shared connections)
- [main()](main%28%29.md) (2 shared connections)
- [circuit breaker](circuit_breaker.md) (2 shared connections)

## Source Files

- `server/container/bundles/realtime.py`
- `server/realtime/nats_message_handler.py`
- `server/realtime/nats_message_handler_processing.py`
- `server/tests/unit/realtime/conftest.py`

## Audit Trail

- EXTRACTED: 167 (86%)
- INFERRED: 28 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*