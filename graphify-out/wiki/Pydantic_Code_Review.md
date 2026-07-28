# Pydantic Code Review

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

- [Command Input Utilities](Command_Input_Utilities.md) (8 shared connections)
- [NPC Combat Lifecycle](NPC_Combat_Lifecycle.md) (4 shared connections)
- [Message Broker Errors](Message_Broker_Errors.md) (4 shared connections)
- [Coverage Disconnect Grace](Coverage_Disconnect_Grace.md) (3 shared connections)
- [Infrastructure Message Broker](Infrastructure_Message_Broker.md) (2 shared connections)
- [E 2 E Results Scenario](E_2_E_Results_Scenario.md) (2 shared connections)
- [Infrastructure Postgres Sql](Infrastructure_Postgres_Sql.md) (2 shared connections)
- [Archive Planning E 2 E](Archive_Planning_E_2_E.md) (1 shared connections)

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