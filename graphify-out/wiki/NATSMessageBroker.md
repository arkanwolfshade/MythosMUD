# NATSMessageBroker

> 52 nodes

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
- **._handle_reconnect_async()** (4 connections) — `server/infrastructure/nats_broker.py`
- **._health_check_loop()** (4 connections) — `server/infrastructure/nats_broker.py`
- **.unsubscribe()** (4 connections) — `server/infrastructure/nats_broker.py`
- **._validate_publish_subject()** (4 connections) — `server/infrastructure/nats_broker.py`
- **._perform_health_check()** (3 connections) — `server/infrastructure/nats_broker.py`
- *... and 27 more nodes in this community*

## Relationships

- [test_nats_broker.py](test_nats_broker.py.md) (20 shared connections)
- [get_logger](get_logger.md) (5 shared connections)
- [._error_callback](_error_callback.md) (2 shared connections)
- [._disconnected_callback](_disconnected_callback.md) (2 shared connections)
- [NATSSubjectManager](NATSSubjectManager.md) (2 shared connections)
- [NATSConfig](NATSConfig.md) (2 shared connections)
- [test_nats_messages.py](test_nats_messages.py.md) (2 shared connections)
- [MessageBroker](MessageBroker.md) (2 shared connections)
- [nats_broker](nats_broker.md) (1 shared connections)
- [message_handler_factory.py](message_handler_factory.py.md) (1 shared connections)
- [test_validation.py](test_validation.py.md) (1 shared connections)
- [config/models/__init__.py](config-models-__init__.py.md) (1 shared connections)

## Source Files

- `server/infrastructure/message_broker.py`
- `server/infrastructure/nats_broker.py`

## Audit Trail

- EXTRACTED: 118 (87%)
- INFERRED: 18 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*