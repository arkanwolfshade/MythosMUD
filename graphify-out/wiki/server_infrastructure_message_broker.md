# server infrastructure message broker

> 61 nodes

## Key Concepts

- **NATSMessageBroker** (33 connections) — `server/infrastructure/nats_broker.py`
- **nats_broker.py** (21 connections) — `server/infrastructure/nats_broker.py`
- **MessageBrokerError** (13 connections) — `server/infrastructure/message_broker.py`
- **PublishError** (11 connections) — `server/infrastructure/message_broker.py`
- **message_broker.py** (11 connections) — `server/infrastructure/message_broker.py`
- **RequestError** (9 connections) — `server/infrastructure/message_broker.py`
- **SubscribeError** (9 connections) — `server/infrastructure/message_broker.py`
- **MessageBrokerConnectionError** (8 connections) — `server/infrastructure/message_broker.py`
- **UnsubscribeError** (8 connections) — `server/infrastructure/message_broker.py`
- **.publish()** (7 connections) — `server/infrastructure/nats_broker.py`
- **.connect()** (5 connections) — `server/infrastructure/nats_broker.py`
- **.disconnect()** (5 connections) — `server/infrastructure/nats_broker.py`
- **.__init__()** (5 connections) — `server/infrastructure/nats_broker.py`
- **.is_connected()** (5 connections) — `server/infrastructure/nats_broker.py`
- **.request()** (5 connections) — `server/infrastructure/nats_broker.py`
- **._start_health_monitoring()** (5 connections) — `server/infrastructure/nats_broker.py`
- **.subscribe()** (5 connections) — `server/infrastructure/nats_broker.py`
- **._validate_publish_message()** (5 connections) — `server/infrastructure/nats_broker.py`
- **Any** (5 connections)
- **._configure_tls()** (4 connections) — `server/infrastructure/nats_broker.py`
- **._error_callback()** (4 connections) — `server/infrastructure/nats_broker.py`
- **._handle_error_async()** (4 connections) — `server/infrastructure/nats_broker.py`
- **._handle_reconnect_async()** (4 connections) — `server/infrastructure/nats_broker.py`
- **._health_check_loop()** (4 connections) — `server/infrastructure/nats_broker.py`
- **.unsubscribe()** (4 connections) — `server/infrastructure/nats_broker.py`
- *... and 36 more nodes in this community*

## Relationships

- [server tests unit infrastructure test](server_tests_unit_infrastructure_test.md) (21 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (4 shared connections)
- [server schemas realtime init](server_schemas_realtime_init.md) (3 shared connections)
- [server services combat event publisher](server_services_combat_event_publisher.md) (2 shared connections)
- [server config models nats natsconfig](server_config_models_nats_natsconfig.md) (2 shared connections)
- [server infrastructure init](server_infrastructure_init.md) (2 shared connections)
- [server config init](server_config_init.md) (2 shared connections)
- [server services nats subject manager](server_services_nats_subject_manager.md) (2 shared connections)
- [server realtime message handler factory](server_realtime_message_handler_factory.md) (1 shared connections)

## Source Files

- `server/infrastructure/message_broker.py`
- `server/infrastructure/nats_broker.py`

## Audit Trail

- EXTRACTED: 126 (88%)
- INFERRED: 18 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*