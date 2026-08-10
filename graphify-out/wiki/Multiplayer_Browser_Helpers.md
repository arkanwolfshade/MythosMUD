# Multiplayer Browser Helpers

> 23 nodes

## Key Concepts

- **nats_broker.py** (17 connections) — `server/infrastructure/nats_broker.py`
- **MessageBrokerError** (13 connections) — `server/infrastructure/message_broker.py`
- **message_broker.py** (11 connections) — `server/infrastructure/message_broker.py`
- **RequestError** (9 connections) — `server/infrastructure/message_broker.py`
- **MessageBrokerConnectionError** (8 connections) — `server/infrastructure/message_broker.py`
- **UnsubscribeError** (8 connections) — `server/infrastructure/message_broker.py`
- **test_connect_failure()** (3 connections) — `server/tests/unit/infrastructure/test_nats_broker.py`
- **test_disconnect_error_handling()** (3 connections) — `server/tests/unit/infrastructure/test_nats_broker.py`
- **test_unsubscribe_failure()** (3 connections) — `server/tests/unit/infrastructure/test_nats_broker.py`
- **test_request_not_connected()** (3 connections) — `server/tests/unit/infrastructure/test_nats_broker.py`
- **test_request_failure()** (3 connections) — `server/tests/unit/infrastructure/test_nats_broker.py`
- **Exception** (1 connections)
- **Message Broker abstraction for MythosMUD.  This module defines the MessageBroker** (1 connections) — `server/infrastructure/message_broker.py`
- **Base exception for message broker errors.** (1 connections) — `server/infrastructure/message_broker.py`
- **Exception raised when connection to message broker fails.** (1 connections) — `server/infrastructure/message_broker.py`
- **Exception raised when unsubscribing from subject fails.** (1 connections) — `server/infrastructure/message_broker.py`
- **Exception raised when request-reply fails.** (1 connections) — `server/infrastructure/message_broker.py`
- **NATS implementation of MessageBroker protocol.  This module provides a concret** (1 connections) — `server/infrastructure/nats_broker.py`
- **Test connect() raises ConnectionError on failure.** (1 connections) — `server/tests/unit/infrastructure/test_nats_broker.py`
- **Test disconnect() raises MessageBrokerError on disconnect failure.** (1 connections) — `server/tests/unit/infrastructure/test_nats_broker.py`
- **Test unsubscribe() raises UnsubscribeError on failure.** (1 connections) — `server/tests/unit/infrastructure/test_nats_broker.py`
- **Test request() raises RequestError when not connected.** (1 connections) — `server/tests/unit/infrastructure/test_nats_broker.py`
- **Test request() raises RequestError on failure.** (1 connections) — `server/tests/unit/infrastructure/test_nats_broker.py`

## Relationships

- [Combat Monitoring Service](Combat_Monitoring_Service.md) (11 shared connections)
- [Realtime Event Delegation](Realtime_Event_Delegation.md) (6 shared connections)
- [Services Combat Persistence](Services_Combat_Persistence.md) (4 shared connections)
- [Realtime Maintenance Connection](Realtime_Maintenance_Connection.md) (3 shared connections)
- [Infrastructure Message Broker](Infrastructure_Message_Broker.md) (2 shared connections)
- [Cursor Skills Mythosmud](Cursor_Skills_Mythosmud.md) (2 shared connections)
- [Game Service Bundle](Game_Service_Bundle.md) (2 shared connections)
- [Combat Service Bundle](Combat_Service_Bundle.md) (1 shared connections)
- [Inventory Command Models](Inventory_Command_Models.md) (1 shared connections)
- [NATS Message Schemas](NATS_Message_Schemas.md) (1 shared connections)
- [Cursor Rules Docker](Cursor_Rules_Docker.md) (1 shared connections)
- [NATS Subject Exceptions](NATS_Subject_Exceptions.md) (1 shared connections)

## Source Files

- `server/infrastructure/message_broker.py`
- `server/infrastructure/nats_broker.py`
- `server/tests/unit/infrastructure/test_nats_broker.py`

## Audit Trail

- EXTRACTED: 79 (85%)
- INFERRED: 14 (15%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*