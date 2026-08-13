# nats_broker

> 5 nodes

## Key Concepts

- **nats_broker()** (4 connections) — `server/tests/unit/infrastructure/test_nats_broker.py`
- **nats_config()** (4 connections) — `server/tests/unit/infrastructure/test_nats_broker.py`
- **fixture** (2 connections)
- **Create a NATSConfig instance.** (1 connections) — `server/tests/unit/infrastructure/test_nats_broker.py`
- **Create a NATSMessageBroker instance.** (1 connections) — `server/tests/unit/infrastructure/test_nats_broker.py`

## Relationships

- [test_nats_broker.py](test_nats_broker.py.md) (2 shared connections)
- [NATSMessageBroker](NATSMessageBroker.md) (1 shared connections)
- [AppConfig](AppConfig.md) (1 shared connections)

## Source Files

- `server/tests/unit/infrastructure/test_nats_broker.py`

## Audit Trail

- EXTRACTED: 8 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*