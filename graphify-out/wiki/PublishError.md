# PublishError

> 6 nodes · cohesion 0.33

## Key Concepts

- **PublishError** (9 connections) — `server/infrastructure/message_broker.py`
- **test_publish_failure()** (3 connections) — `server/tests/unit/infrastructure/test_nats_broker.py`
- **test_publish_not_connected()** (3 connections) — `server/tests/unit/infrastructure/test_nats_broker.py`
- **Exception raised when publishing message fails.** (1 connections) — `server/infrastructure/message_broker.py`
- **Test publish() raises PublishError when not connected.** (1 connections) — `server/tests/unit/infrastructure/test_nats_broker.py`
- **Test publish() raises PublishError on failure.** (1 connections) — `server/tests/unit/infrastructure/test_nats_broker.py`

## Relationships

- [test_nats_broker.py](test_nats_broker.py.md) (3 shared connections)
- [MessageBrokerError](MessageBrokerError.md) (2 shared connections)
- [CombatService](CombatService.md) (1 shared connections)
- [NATSMessageBroker](NATSMessageBroker.md) (1 shared connections)
- [.publish](publish.md) (1 shared connections)

## Source Files

- `server/infrastructure/message_broker.py`
- `server/tests/unit/infrastructure/test_nats_broker.py`

## Audit Trail

- EXTRACTED: 13 (72%)
- INFERRED: 5 (28%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*