# NATSMessageBroker

> 54 nodes

## Key Concepts

- **NATSMessageBroker** (32 connections) — `server/infrastructure/nats_broker.py`
- **nats_broker.py** (17 connections) — `server/infrastructure/nats_broker.py`
- **MessageBrokerError** (12 connections) — `server/infrastructure/message_broker.py`
- **message_broker.py** (11 connections) — `server/infrastructure/message_broker.py`
- **PublishError** (9 connections) — `server/infrastructure/message_broker.py`
- **MessageBrokerConnectionError** (7 connections) — `server/infrastructure/message_broker.py`
- **RequestError** (7 connections) — `server/infrastructure/message_broker.py`
- **SubscribeError** (7 connections) — `server/infrastructure/message_broker.py`
- **UnsubscribeError** (7 connections) — `server/infrastructure/message_broker.py`
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
- **._handle_reconnect_async()** (4 connections) — `server/infrastructure/nats_broker.py`
- **._health_check_loop()** (4 connections) — `server/infrastructure/nats_broker.py`
- **.unsubscribe()** (4 connections) — `server/infrastructure/nats_broker.py`
- **._validate_publish_subject()** (4 connections) — `server/infrastructure/nats_broker.py`
- **._disconnected_callback()** (3 connections) — `server/infrastructure/nats_broker.py`
- **._handle_disconnect_async()** (3 connections) — `server/infrastructure/nats_broker.py`
- *... and 29 more nodes in this community*

## Relationships

- [test_nats_broker.py](test_nats_broker.py.md) (10 shared connections)
- [NATSConfig](NATSConfig.md) (3 shared connections)
- [._error_callback](_error_callback.md) (2 shared connections)
- [test_nats_messages.py](test_nats_messages.py.md) (2 shared connections)
- [MessageBroker](MessageBroker.md) (2 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [message_handler_factory.py](message_handler_factory.py.md) (1 shared connections)
- [NATSService](NATSService.md) (1 shared connections)
- [SubjectValidator](SubjectValidator.md) (1 shared connections)
- [NATSSubjectManager](NATSSubjectManager.md) (1 shared connections)

## Source Files

- `server/infrastructure/message_broker.py`
- `server/infrastructure/nats_broker.py`

## Audit Trail

- EXTRACTED: 115 (95%)
- INFERRED: 6 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*