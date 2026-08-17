# server realtime message formatters

> 114 nodes

## Key Concepts

- **NATSError** (66 connections) — `server/services/nats_exceptions.py`
- **nats_exceptions.py** (37 connections) — `server/services/nats_exceptions.py`
- **nats_message_handler_processing.py** (24 connections) — `server/realtime/nats_message_handler_processing.py`
- **NATSPublishError** (23 connections) — `server/services/nats_exceptions.py`
- **format_message_content()** (18 connections) — `server/realtime/message_formatters.py`
- **NATSSubscribeError** (17 connections) — `server/services/nats_exceptions.py`
- **nats_message_handler_broadcast.py** (16 connections) — `server/realtime/nats_message_handler_broadcast.py`
- **test_message_formatters.py** (16 connections) — `server/tests/unit/realtime/test_message_formatters.py`
- **NATSConnectionError** (14 connections) — `server/services/nats_exceptions.py`
- **test_nats_exceptions.py** (14 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- **NATSHealthCheckError** (13 connections) — `server/services/nats_exceptions.py`
- **TestExceptionHierarchy** (11 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- **nats_message_handler_subscriptions.py** (10 connections) — `server/realtime/nats_message_handler_subscriptions.py`
- **message_formatters.py** (9 connections) — `server/realtime/message_formatters.py`
- **TestNATSConnectionError** (8 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- **TestNATSHealthCheckError** (8 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- **TestNATSPublishError** (8 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- **TestNATSSubscribeError** (8 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- **.__init__()** (7 connections) — `server/services/nats_exceptions.py`
- **NATSUnsubscribeError** (6 connections) — `server/services/nats_exceptions.py`
- **.test_all_errors_inherit_from_exception()** (6 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- **.test_all_errors_inherit_from_nats_error()** (6 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- **Exception** (6 connections)
- **TestNATSError** (5 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- **NATSRequestError** (4 connections) — `server/services/nats_exceptions.py`
- *... and 89 more nodes in this community*

## Relationships

- [server tests unit realtime test](server_tests_unit_realtime_test.md) (29 shared connections)
- [server realtime event handlers](server_realtime_event_handlers.md) (22 shared connections)
- [server events combat events](server_events_combat_events.md) (12 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (11 shared connections)
- [server app game tick counter](server_app_game_tick_counter.md) (9 shared connections)
- [server game chat nats publisher](server_game_chat_nats_publisher.md) (6 shared connections)
- [server services aggro threat](server_services_aggro_threat.md) (4 shared connections)
- [server services combat persistence handler](server_services_combat_persistence_handler.md) (3 shared connections)
- [server tests unit services test](server_tests_unit_services_test.md) (3 shared connections)
- [server realtime nats message handler](server_realtime_nats_message_handler.md) (3 shared connections)
- [server realtime circuit breaker](server_realtime_circuit_breaker.md) (2 shared connections)
- [server realtime dead letter queue](server_realtime_dead_letter_queue.md) (2 shared connections)

## Source Files

- `server/realtime/message_formatters.py`
- `server/realtime/nats_message_handler_broadcast.py`
- `server/realtime/nats_message_handler_processing.py`
- `server/realtime/nats_message_handler_subscriptions.py`
- `server/services/nats_exceptions.py`
- `server/tests/unit/realtime/test_message_formatters.py`
- `server/tests/unit/services/test_nats_exceptions.py`

## Audit Trail

- EXTRACTED: 273 (85%)
- INFERRED: 49 (15%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*