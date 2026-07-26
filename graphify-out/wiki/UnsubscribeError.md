# UnsubscribeError

> 10 nodes · cohesion 0.20

## Key Concepts

- **UnsubscribeError** (8 connections) — `server/infrastructure/message_broker.py`
- **.disconnect()** (5 connections) — `server/infrastructure/nats_broker.py`
- **.unsubscribe()** (4 connections) — `server/infrastructure/nats_broker.py`
- **._stop_health_monitoring()** (3 connections) — `server/infrastructure/nats_broker.py`
- **test_unsubscribe_failure()** (3 connections) — `server/tests/unit/infrastructure/test_nats_broker.py`
- **Exception raised when unsubscribing from subject fails.** (1 connections) — `server/infrastructure/message_broker.py`
- **Disconnect from NATS server.** (1 connections) — `server/infrastructure/nats_broker.py`
- **Unsubscribe from NATS subject.          Args:             subscription_id: ID re** (1 connections) — `server/infrastructure/nats_broker.py`
- **Stop health check monitoring task.** (1 connections) — `server/infrastructure/nats_broker.py`
- **Test unsubscribe() raises UnsubscribeError on failure.** (1 connections) — `server/tests/unit/infrastructure/test_nats_broker.py`

## Relationships

- [NATSMessageBroker](NATSMessageBroker.md) (4 shared connections)
- [MessageBrokerError](MessageBrokerError.md) (3 shared connections)
- [test_nats_broker.py](test_nats_broker.py.md) (2 shared connections)
- [CombatService](CombatService.md) (1 shared connections)

## Source Files

- `server/infrastructure/message_broker.py`
- `server/infrastructure/nats_broker.py`
- `server/tests/unit/infrastructure/test_nats_broker.py`

## Audit Trail

- EXTRACTED: 25 (89%)
- INFERRED: 3 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*