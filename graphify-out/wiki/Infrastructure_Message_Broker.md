# Infrastructure Message Broker

> 19 nodes · cohesion 0.11

## Key Concepts

- **MessageBroker** (11 connections) — `server/infrastructure/message_broker.py`
- **.publish()** (3 connections) — `server/infrastructure/message_broker.py`
- **.request()** (3 connections) — `server/infrastructure/message_broker.py`
- **.subscribe()** (3 connections) — `server/infrastructure/message_broker.py`
- **__init__.py** (3 connections) — `server/infrastructure/__init__.py`
- **.connect()** (2 connections) — `server/infrastructure/message_broker.py`
- **.disconnect()** (2 connections) — `server/infrastructure/message_broker.py`
- **.is_connected()** (2 connections) — `server/infrastructure/message_broker.py`
- **.unsubscribe()** (2 connections) — `server/infrastructure/message_broker.py`
- **Any** (2 connections) — `server/infrastructure/message_broker.py`
- **Send a request and wait for a reply (request-reply pattern).          Args:** (1 connections) — `server/infrastructure/message_broker.py`
- **Protocol defining the message broker interface.      This abstract interface all** (1 connections) — `server/infrastructure/message_broker.py`
- **Connect to the message broker.          Returns:             bool: True if conne** (1 connections) — `server/infrastructure/message_broker.py`
- **Disconnect from the message broker.          Closes all subscriptions and releas** (1 connections) — `server/infrastructure/message_broker.py`
- **Check if connected to the message broker.          Returns:             bool: Tr** (1 connections) — `server/infrastructure/message_broker.py`
- **Publish a message to a subject/topic.          Args:             subject: Subjec** (1 connections) — `server/infrastructure/message_broker.py`
- **Subscribe to a subject/topic with a message handler.          Args:** (1 connections) — `server/infrastructure/message_broker.py`
- **Unsubscribe from a subject/topic.          Args:             subscription_id: ID** (1 connections) — `server/infrastructure/message_broker.py`
- **Infrastructure layer for MythosMUD.  This package contains abstractions for exte** (1 connections) — `server/infrastructure/__init__.py`

## Relationships

- [[Message Broker Errors]] (3 shared connections)
- [[Player Combat XP]] (1 shared connections)

## Source Files

- `server/infrastructure/__init__.py`
- `server/infrastructure/message_broker.py`

## Audit Trail

- EXTRACTED: 42 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
