# description

> 5 nodes

## Key Concepts

- **nats_broker()** (4 connections) — `server/tests/unit/infrastructure/test_nats_broker.py`
- **nats_config()** (4 connections) — `server/tests/unit/infrastructure/test_nats_broker.py`
- **fixture** (2 connections)
- **Create a NATSConfig instance.** (1 connections) — `server/tests/unit/infrastructure/test_nats_broker.py`
- **Create a NATSMessageBroker instance.** (1 connections) — `server/tests/unit/infrastructure/test_nats_broker.py`

## Relationships

- [LucidityFluxService](LucidityFluxService.md) (2 shared connections)
- [gen_arena_migration_sql.py](gen_arena_migration_sql.py.md) (1 shared connections)
- [PrototypeRegistryError](PrototypeRegistryError.md) (1 shared connections)

## Source Files

- `server/tests/unit/infrastructure/test_nats_broker.py`

## Audit Trail

- EXTRACTED: 7 (88%)
- INFERRED: 1 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*