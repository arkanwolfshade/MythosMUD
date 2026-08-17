# test_nats_broker.py

> 146 nodes

## Key Concepts

- **test_nats_broker.py** (57 connections) — `server/tests/unit/infrastructure/test_nats_broker.py`
- **asyncio** (35 connections)
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
- *... and 121 more nodes in this community*

## Relationships

- [NATSService](NATSService.md) (4 shared connections)
- [test_nats_messages.py](test_nats_messages.py.md) (3 shared connections)
- [get_logger](get_logger.md) (3 shared connections)
- [NATSSubjectManager](NATSSubjectManager.md) (3 shared connections)
- [MessageBroker](MessageBroker.md) (2 shared connections)
- [config/models/__init__.py](config-models-__init__.py.md) (2 shared connections)
- [message_handler_factory.py](message_handler_factory.py.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/infrastructure/message_broker.py`
- `server/infrastructure/nats_broker.py`
- `server/tests/unit/infrastructure/test_nats_broker.py`

## Audit Trail

- EXTRACTED: 246 (93%)
- INFERRED: 18 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*