# nats_broker.py

> 21 nodes

## Key Concepts

- **nats_broker.py** (21 connections) — `server/infrastructure/nats_broker.py`
- **MessageBrokerError** (13 connections) — `server/infrastructure/message_broker.py`
- **message_broker.py** (11 connections) — `server/infrastructure/message_broker.py`
- **RequestError** (9 connections) — `server/infrastructure/message_broker.py`
- **SubscribeError** (9 connections) — `server/infrastructure/message_broker.py`
- **MessageBrokerConnectionError** (8 connections) — `server/infrastructure/message_broker.py`
- **UnsubscribeError** (8 connections) — `server/infrastructure/message_broker.py`
- **.disconnect()** (5 connections) — `server/infrastructure/nats_broker.py`
- **.unsubscribe()** (4 connections) — `server/infrastructure/nats_broker.py`
- **._stop_health_monitoring()** (3 connections) — `server/infrastructure/nats_broker.py`
- **Exception** (1 connections)
- **Message Broker abstraction for MythosMUD. This module defines the MessageBroker…** (1 connections) — `server/infrastructure/message_broker.py`
- **Base exception for message broker errors.** (1 connections) — `server/infrastructure/message_broker.py`
- **Exception raised when connection to message broker fails.** (1 connections) — `server/infrastructure/message_broker.py`
- **Exception raised when subscribing to subject fails.** (1 connections) — `server/infrastructure/message_broker.py`
- **Exception raised when unsubscribing from subject fails.** (1 connections) — `server/infrastructure/message_broker.py`
- **Exception raised when request-reply fails.** (1 connections) — `server/infrastructure/message_broker.py`
- **NATS implementation of MessageBroker protocol. This module provides a concrete…** (1 connections) — `server/infrastructure/nats_broker.py`
- **Disconnect from NATS server.** (1 connections) — `server/infrastructure/nats_broker.py`
- **Unsubscribe from NATS subject. Args: subscription_id: ID returned from…** (1 connections) — `server/infrastructure/nats_broker.py`
- **Stop health check monitoring task.** (1 connections) — `server/infrastructure/nats_broker.py`

## Relationships

- [NATSMessageBroker](NATSMessageBroker.md) (15 shared connections)
- [test_nats_broker.py](test_nats_broker.py.md) (14 shared connections)
- [get_logger](get_logger.md) (4 shared connections)
- [NATSSubjectManager](NATSSubjectManager.md) (3 shared connections)
- [MessageBroker](MessageBroker.md) (2 shared connections)
- [event_types.py](event_types.py.md) (1 shared connections)
- [NATSService](NATSService.md) (1 shared connections)
- [test_nats_messages.py](test_nats_messages.py.md) (1 shared connections)
- [realtime/realtime.py](realtime-realtime.py.md) (1 shared connections)

## Source Files

- `server/infrastructure/message_broker.py`
- `server/infrastructure/nats_broker.py`

## Audit Trail

- EXTRACTED: 60 (83%)
- INFERRED: 12 (17%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*