# command factories communication

> 29 nodes

## Key Concepts

- **MessageBrokerError** (13 connections) — `server/infrastructure/message_broker.py`
- **message_broker.py** (11 connections) — `server/infrastructure/message_broker.py`
- **PublishError** (9 connections) — `server/infrastructure/message_broker.py`
- **MessageBrokerConnectionError** (8 connections) — `server/infrastructure/message_broker.py`
- **UnsubscribeError** (8 connections) — `server/infrastructure/message_broker.py`
- **.disconnect()** (5 connections) — `server/infrastructure/nats_broker.py`
- **.unsubscribe()** (4 connections) — `server/infrastructure/nats_broker.py`
- **__init__.py** (3 connections) — `server/infrastructure/__init__.py`
- **._stop_health_monitoring()** (3 connections) — `server/infrastructure/nats_broker.py`
- **test_connect_failure()** (3 connections) — `server/tests/unit/infrastructure/test_nats_broker.py`
- **test_disconnect_error_handling()** (3 connections) — `server/tests/unit/infrastructure/test_nats_broker.py`
- **test_publish_not_connected()** (3 connections) — `server/tests/unit/infrastructure/test_nats_broker.py`
- **test_publish_failure()** (3 connections) — `server/tests/unit/infrastructure/test_nats_broker.py`
- **test_unsubscribe_failure()** (3 connections) — `server/tests/unit/infrastructure/test_nats_broker.py`
- **Infrastructure layer for MythosMUD.  This package contains abstractions for exte** (1 connections) — `server/infrastructure/__init__.py`
- **Exception** (1 connections)
- **Message Broker abstraction for MythosMUD.  This module defines the MessageBroker** (1 connections) — `server/infrastructure/message_broker.py`
- **Base exception for message broker errors.** (1 connections) — `server/infrastructure/message_broker.py`
- **Exception raised when connection to message broker fails.** (1 connections) — `server/infrastructure/message_broker.py`
- **Exception raised when publishing message fails.** (1 connections) — `server/infrastructure/message_broker.py`
- **Exception raised when unsubscribing from subject fails.** (1 connections) — `server/infrastructure/message_broker.py`
- **Disconnect from NATS server.** (1 connections) — `server/infrastructure/nats_broker.py`
- **Unsubscribe from NATS subject.          Args:             subscription_id: ID re** (1 connections) — `server/infrastructure/nats_broker.py`
- **Stop health check monitoring task.** (1 connections) — `server/infrastructure/nats_broker.py`
- **Test connect() raises ConnectionError on failure.** (1 connections) — `server/tests/unit/infrastructure/test_nats_broker.py`
- *... and 4 more nodes in this community*

## Relationships

- [broker infrastructure nats](broker_infrastructure_nats.md) (10 shared connections)
- [infrastructure nats broker](infrastructure_nats_broker.md) (9 shared connections)
- [NATS Messaging](NATS_Messaging.md) (5 shared connections)
- [infrastructure message broker](infrastructure_message_broker.md) (2 shared connections)
- [message handlers realtime](message_handlers_realtime.md) (2 shared connections)
- [game models enums](game_models_enums.md) (2 shared connections)

## Source Files

- `server/infrastructure/__init__.py`
- `server/infrastructure/message_broker.py`
- `server/infrastructure/nats_broker.py`
- `server/tests/unit/infrastructure/test_nats_broker.py`

## Audit Trail

- EXTRACTED: 80 (85%)
- INFERRED: 14 (15%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*