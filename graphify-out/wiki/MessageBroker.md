# MessageBroker

> 20 nodes

## Key Concepts

- **MessageBroker** (11 connections) — `server/infrastructure/message_broker.py`
- **.publish()** (3 connections) — `server/infrastructure/message_broker.py`
- **.request()** (3 connections) — `server/infrastructure/message_broker.py`
- **.subscribe()** (3 connections) — `server/infrastructure/message_broker.py`
- **server/infrastructure/__init__.py** (3 connections) — `server/infrastructure/__init__.py`
- **.connect()** (2 connections) — `server/infrastructure/message_broker.py`
- **.disconnect()** (2 connections) — `server/infrastructure/message_broker.py`
- **.is_connected()** (2 connections) — `server/infrastructure/message_broker.py`
- **.unsubscribe()** (2 connections) — `server/infrastructure/message_broker.py`
- **Any** (2 connections)
- **Protocol** (1 connections)
- **Infrastructure layer for MythosMUD. This package contains abstractions for…** (1 connections) — `server/infrastructure/__init__.py`
- **Send a request and wait for a reply (request-reply pattern). Args: subject:…** (1 connections) — `server/infrastructure/message_broker.py`
- **Protocol defining the message broker interface. This abstract interface allows…** (1 connections) — `server/infrastructure/message_broker.py`
- **Connect to the message broker. Returns: bool: True if connection successful,…** (1 connections) — `server/infrastructure/message_broker.py`
- **Disconnect from the message broker. Closes all subscriptions and releases…** (1 connections) — `server/infrastructure/message_broker.py`
- **Check if connected to the message broker. Returns: bool: True if connected,…** (1 connections) — `server/infrastructure/message_broker.py`
- **Publish a message to a subject/topic. Args: subject: Subject/topic to publish…** (1 connections) — `server/infrastructure/message_broker.py`
- **Subscribe to a subject/topic with a message handler. Args: subject:…** (1 connections) — `server/infrastructure/message_broker.py`
- **Unsubscribe from a subject/topic. Args: subscription_id: ID returned from…** (1 connections) — `server/infrastructure/message_broker.py`

## Relationships

- [NATSMessageBroker](NATSMessageBroker.md) (2 shared connections)
- [test_message_handler_factory.py](test_message_handler_factory.py.md) (1 shared connections)

## Source Files

- `server/infrastructure/__init__.py`
- `server/infrastructure/message_broker.py`

## Audit Trail

- EXTRACTED: 23 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*