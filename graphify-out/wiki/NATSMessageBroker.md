# NATSMessageBroker

> 35 nodes

## Key Concepts

- **NATSMessageBroker** (33 connections) — `server/infrastructure/nats_broker.py`
- **PublishError** (11 connections) — `server/infrastructure/message_broker.py`
- **.publish()** (7 connections) — `server/infrastructure/nats_broker.py`
- **.connect()** (5 connections) — `server/infrastructure/nats_broker.py`
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
- **._validate_publish_subject()** (4 connections) — `server/infrastructure/nats_broker.py`
- **._disconnected_callback()** (3 connections) — `server/infrastructure/nats_broker.py`
- **._handle_disconnect_async()** (3 connections) — `server/infrastructure/nats_broker.py`
- **._perform_health_check()** (3 connections) — `server/infrastructure/nats_broker.py`
- **._reconnected_callback()** (3 connections) — `server/infrastructure/nats_broker.py`
- **Exception raised when publishing message fails.** (1 connections) — `server/infrastructure/message_broker.py`
- **Connect to NATS server. Returns: bool: True if connection successful, False…** (1 connections) — `server/infrastructure/nats_broker.py`
- **Check if connected to NATS and healthy. Returns: bool: True if connected and…** (1 connections) — `server/infrastructure/nats_broker.py`
- **Publish message to NATS subject.** (1 connections) — `server/infrastructure/nats_broker.py`
- **Subscribe to NATS subject with message handler.** (1 connections) — `server/infrastructure/nats_broker.py`
- **Send request and wait for reply (request-reply pattern). Args: subject: NATS…** (1 connections) — `server/infrastructure/nats_broker.py`
- *... and 10 more nodes in this community*

## Relationships

- [nats_broker.py](nats_broker.py.md) (15 shared connections)
- [test_nats_broker.py](test_nats_broker.py.md) (6 shared connections)
- [._error_callback](_error_callback.md) (2 shared connections)
- [nats_broker](nats_broker.md) (1 shared connections)
- [get_logger](get_logger.md) (1 shared connections)
- [NATSSubjectManager](NATSSubjectManager.md) (1 shared connections)
- [NATSService](NATSService.md) (1 shared connections)
- [test_message_handlers.py](test_message_handlers.py.md) (1 shared connections)
- [test_nats_messages.py](test_nats_messages.py.md) (1 shared connections)

## Source Files

- `server/infrastructure/message_broker.py`
- `server/infrastructure/nats_broker.py`

## Audit Trail

- EXTRACTED: 71 (87%)
- INFERRED: 11 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*