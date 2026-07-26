# .publish

> 11 nodes · cohesion 0.20

## Key Concepts

- **.publish()** (6 connections) — `server/infrastructure/nats_broker.py`
- **.is_connected()** (5 connections) — `server/infrastructure/nats_broker.py`
- **.request()** (5 connections) — `server/infrastructure/nats_broker.py`
- **.subscribe()** (5 connections) — `server/infrastructure/nats_broker.py`
- **._configure_tls()** (4 connections) — `server/infrastructure/nats_broker.py`
- **Any** (3 connections)
- **Check if connected to NATS and healthy.          Returns:             bool: True** (1 connections) — `server/infrastructure/nats_broker.py`
- **Publish message to NATS subject.          Args:             subject: NATS subjec** (1 connections) — `server/infrastructure/nats_broker.py`
- **Subscribe to NATS subject with message handler.          Args:             subje** (1 connections) — `server/infrastructure/nats_broker.py`
- **Send request and wait for reply (request-reply pattern).          Args:** (1 connections) — `server/infrastructure/nats_broker.py`
- **Configure TLS settings for NATS connection (mirrors NATSService._configure_tls).** (1 connections) — `server/infrastructure/nats_broker.py`

## Relationships

- [NATSMessageBroker](NATSMessageBroker.md) (6 shared connections)
- [PublishError](PublishError.md) (1 shared connections)
- [test_nats_messages.py](test_nats_messages.py.md) (1 shared connections)
- [MessageBrokerError](MessageBrokerError.md) (1 shared connections)
- [SubscribeError](SubscribeError.md) (1 shared connections)
- [message_handler_factory.py](message_handler_factory.py.md) (1 shared connections)

## Source Files

- `server/infrastructure/nats_broker.py`

## Audit Trail

- EXTRACTED: 33 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*