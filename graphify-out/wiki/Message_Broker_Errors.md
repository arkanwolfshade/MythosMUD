# Message Broker Errors

> 60 nodes · cohesion 0.08

## Key Concepts

- **NATSMessageBroker** (31 connections) — `server/infrastructure/nats_broker.py`
- **MessageBrokerError** (17 connections) — `server/infrastructure/message_broker.py`
- **nats_broker.py** (17 connections) — `server/infrastructure/nats_broker.py`
- **MessageBrokerConnectionError** (12 connections) — `server/infrastructure/message_broker.py`
- **PublishError** (12 connections) — `server/infrastructure/message_broker.py`
- **RequestError** (12 connections) — `server/infrastructure/message_broker.py`
- **SubscribeError** (12 connections) — `server/infrastructure/message_broker.py`
- **UnsubscribeError** (12 connections) — `server/infrastructure/message_broker.py`
- **message_broker.py** (10 connections) — `server/infrastructure/message_broker.py`
- **Any** (10 connections) — `server/infrastructure/nats_broker.py`
- **Exception** (9 connections) — `server/infrastructure/nats_broker.py`
- **MessageHandler** (9 connections) — `server/infrastructure/nats_broker.py`
- **NATSConfig** (8 connections) — `server/infrastructure/nats_broker.py`
- **NATSSubjectManager** (8 connections) — `server/infrastructure/nats_broker.py`
- **MessageHandler** (7 connections) — `server/infrastructure/message_broker.py`
- **.publish()** (6 connections) — `server/infrastructure/nats_broker.py`
- **.connect()** (5 connections) — `server/infrastructure/nats_broker.py`
- **.disconnect()** (5 connections) — `server/infrastructure/nats_broker.py`
- **.__init__()** (5 connections) — `server/infrastructure/nats_broker.py`
- **.is_connected()** (5 connections) — `server/infrastructure/nats_broker.py`
- **.request()** (5 connections) — `server/infrastructure/nats_broker.py`
- **._start_health_monitoring()** (5 connections) — `server/infrastructure/nats_broker.py`
- **.subscribe()** (5 connections) — `server/infrastructure/nats_broker.py`
- **._configure_tls()** (4 connections) — `server/infrastructure/nats_broker.py`
- **._error_callback()** (4 connections) — `server/infrastructure/nats_broker.py`
- *... and 35 more nodes in this community*

## Relationships

- [[NATS Message Broker]] (9 shared connections)
- [[Infrastructure Message Broker]] (3 shared connections)
- [[NPC Admin API]] (3 shared connections)
- [[Combat Domain Events]] (2 shared connections)
- [[NATS Message Schemas]] (2 shared connections)
- [[Application Config Settings]] (1 shared connections)
- [[NATS Subject Exceptions]] (1 shared connections)
- [[NATS Subject Manager]] (1 shared connections)

## Source Files

- `server/infrastructure/message_broker.py`
- `server/infrastructure/nats_broker.py`

## Audit Trail

- EXTRACTED: 210 (71%)
- INFERRED: 84 (29%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
