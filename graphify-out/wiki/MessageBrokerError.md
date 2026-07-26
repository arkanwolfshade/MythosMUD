# MessageBrokerError

> 19 nodes · cohesion 0.12

## Key Concepts

- **MessageBrokerError** (13 connections) — `server/infrastructure/message_broker.py`
- **message_broker.py** (11 connections) — `server/infrastructure/message_broker.py`
- **RequestError** (9 connections) — `server/infrastructure/message_broker.py`
- **MessageBrokerConnectionError** (8 connections) — `server/infrastructure/message_broker.py`
- **__init__.py** (3 connections) — `server/infrastructure/__init__.py`
- **test_connect_failure()** (3 connections) — `server/tests/unit/infrastructure/test_nats_broker.py`
- **test_disconnect_error_handling()** (3 connections) — `server/tests/unit/infrastructure/test_nats_broker.py`
- **test_request_failure()** (3 connections) — `server/tests/unit/infrastructure/test_nats_broker.py`
- **test_request_not_connected()** (3 connections) — `server/tests/unit/infrastructure/test_nats_broker.py`
- **Infrastructure layer for MythosMUD.  This package contains abstractions for exte** (1 connections) — `server/infrastructure/__init__.py`
- **Exception** (1 connections)
- **Message Broker abstraction for MythosMUD.  This module defines the MessageBroker** (1 connections) — `server/infrastructure/message_broker.py`
- **Base exception for message broker errors.** (1 connections) — `server/infrastructure/message_broker.py`
- **Exception raised when connection to message broker fails.** (1 connections) — `server/infrastructure/message_broker.py`
- **Exception raised when request-reply fails.** (1 connections) — `server/infrastructure/message_broker.py`
- **Test disconnect() raises MessageBrokerError on disconnect failure.** (1 connections) — `server/tests/unit/infrastructure/test_nats_broker.py`
- **Test request() raises RequestError when not connected.** (1 connections) — `server/tests/unit/infrastructure/test_nats_broker.py`
- **Test request() raises RequestError on failure.** (1 connections) — `server/tests/unit/infrastructure/test_nats_broker.py`
- **Test connect() raises ConnectionError on failure.** (1 connections) — `server/tests/unit/infrastructure/test_nats_broker.py`

## Relationships

- [test_nats_broker.py](test_nats_broker.py.md) (8 shared connections)
- [CombatService](CombatService.md) (4 shared connections)
- [NATSMessageBroker](NATSMessageBroker.md) (4 shared connections)
- [UnsubscribeError](UnsubscribeError.md) (3 shared connections)
- [MessageBroker](MessageBroker.md) (2 shared connections)
- [PublishError](PublishError.md) (2 shared connections)
- [SubscribeError](SubscribeError.md) (2 shared connections)
- [.publish](publish.md) (1 shared connections)

## Source Files

- `server/infrastructure/__init__.py`
- `server/infrastructure/message_broker.py`
- `server/tests/unit/infrastructure/test_nats_broker.py`

## Audit Trail

- EXTRACTED: 55 (83%)
- INFERRED: 11 (17%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*