# Infrastructure Postgres Sql

> 6 nodes · cohesion 0.33

## Key Concepts

- **SubscribeError** (9 connections) — `server/infrastructure/message_broker.py`
- **test_subscribe_failure()** (3 connections) — `server/tests/unit/infrastructure/test_nats_broker.py`
- **test_subscribe_not_connected()** (3 connections) — `server/tests/unit/infrastructure/test_nats_broker.py`
- **Exception raised when subscribing to subject fails.** (1 connections) — `server/infrastructure/message_broker.py`
- **Test subscribe() raises SubscribeError when not connected.** (1 connections) — `server/tests/unit/infrastructure/test_nats_broker.py`
- **Test subscribe() raises SubscribeError on failure.** (1 connections) — `server/tests/unit/infrastructure/test_nats_broker.py`

## Relationships

- [Command Input Utilities](Command_Input_Utilities.md) (3 shared connections)
- [Pydantic Code Review](Pydantic_Code_Review.md) (2 shared connections)
- [NPC Combat Lifecycle](NPC_Combat_Lifecycle.md) (1 shared connections)
- [Message Broker Errors](Message_Broker_Errors.md) (1 shared connections)
- [Archive Planning E 2 E](Archive_Planning_E_2_E.md) (1 shared connections)

## Source Files

- `server/infrastructure/message_broker.py`
- `server/tests/unit/infrastructure/test_nats_broker.py`

## Audit Trail

- EXTRACTED: 13 (72%)
- INFERRED: 5 (28%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*