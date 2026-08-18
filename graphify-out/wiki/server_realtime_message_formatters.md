# server realtime message formatters

> 110 nodes

## Key Concepts

- **NATSError** (70 connections) — `server/services/nats_exceptions.py`
- **nats_exceptions.py** (37 connections) — `server/services/nats_exceptions.py`
- **NATSPublishError** (34 connections) — `server/services/nats_exceptions.py`
- **NATSSubscribeError** (23 connections) — `server/services/nats_exceptions.py`
- **format_message_content()** (18 connections) — `server/realtime/message_formatters.py`
- **nats_message_handler_broadcast.py** (16 connections) — `server/realtime/nats_message_handler_broadcast.py`
- **combat_persistence_handler.py** (16 connections) — `server/services/combat_persistence_handler.py`
- **test_message_formatters.py** (16 connections) — `server/tests/unit/realtime/test_message_formatters.py`
- **NATSConnectionError** (14 connections) — `server/services/nats_exceptions.py`
- **test_nats_exceptions.py** (14 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- **NATSHealthCheckError** (13 connections) — `server/services/nats_exceptions.py`
- **TestExceptionHierarchy** (11 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- **message_formatters.py** (9 connections) — `server/realtime/message_formatters.py`
- **TestNATSConnectionError** (8 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- **TestNATSHealthCheckError** (8 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- **TestNATSPublishError** (8 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- **TestNATSSubscribeError** (8 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- **.__init__()** (7 connections) — `server/services/nats_exceptions.py`
- **.test_all_errors_inherit_from_exception()** (6 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- **.test_all_errors_inherit_from_nats_error()** (6 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- **Exception** (6 connections)
- **TestNATSError** (5 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- **test_format_message_content_nats_error()** (4 connections) — `server/tests/unit/realtime/test_message_formatters.py`
- **.__init__()** (3 connections) — `server/services/nats_exceptions.py`
- **.__init__()** (3 connections) — `server/services/nats_exceptions.py`
- *... and 85 more nodes in this community*

## Relationships

- [server tests unit realtime test](server_tests_unit_realtime_test.md) (27 shared connections)
- [server events combat events](server_events_combat_events.md) (21 shared connections)
- [server realtime event handlers](server_realtime_event_handlers.md) (19 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (14 shared connections)
- [server services nats exceptions natsrequesterror](server_services_nats_exceptions_natsrequesterror.md) (13 shared connections)
- [server events combat events combatendedevent](server_events_combat_events_combatendedevent.md) (7 shared connections)
- [server tests unit services test](server_tests_unit_services_test.md) (6 shared connections)
- [server game chat message](server_game_chat_message.md) (6 shared connections)
- [msg](msg.md) (5 shared connections)
- [server services aggro threat](server_services_aggro_threat.md) (4 shared connections)
- [server services aggro threat clear](server_services_aggro_threat_clear.md) (4 shared connections)
- [server services nats service natsservice](server_services_nats_service_natsservice.md) (3 shared connections)

## Source Files

- `server/realtime/message_formatters.py`
- `server/realtime/nats_message_handler_broadcast.py`
- `server/services/combat_persistence_handler.py`
- `server/services/nats_exceptions.py`
- `server/tests/unit/realtime/test_message_formatters.py`
- `server/tests/unit/services/test_nats_exceptions.py`

## Audit Trail

- EXTRACTED: 269 (83%)
- INFERRED: 56 (17%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*