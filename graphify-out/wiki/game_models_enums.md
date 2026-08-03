# game models enums

> 6 nodes

## Key Concepts

- **SubscribeError** (9 connections) — `server/infrastructure/message_broker.py`
- **test_subscribe_not_connected()** (3 connections) — `server/tests/unit/infrastructure/test_nats_broker.py`
- **test_subscribe_failure()** (3 connections) — `server/tests/unit/infrastructure/test_nats_broker.py`
- **Exception raised when subscribing to subject fails.** (1 connections) — `server/infrastructure/message_broker.py`
- **Test subscribe() raises SubscribeError when not connected.** (1 connections) — `server/tests/unit/infrastructure/test_nats_broker.py`
- **Test subscribe() raises SubscribeError on failure.** (1 connections) — `server/tests/unit/infrastructure/test_nats_broker.py`

## Relationships

- [broker infrastructure nats](broker_infrastructure_nats.md) (3 shared connections)
- [command factories communication](command_factories_communication.md) (2 shared connections)
- [infrastructure nats broker](infrastructure_nats_broker.md) (2 shared connections)
- [NATS Messaging](NATS_Messaging.md) (1 shared connections)

## Source Files

- `server/infrastructure/message_broker.py`
- `server/tests/unit/infrastructure/test_nats_broker.py`

## Audit Trail

- EXTRACTED: 13 (72%)
- INFERRED: 5 (28%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*