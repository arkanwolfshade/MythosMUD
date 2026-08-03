# conftest BoundLogger rationale

> 3 nodes

## Key Concepts

- **test_logger()** (4 connections) — `server/tests/conftest.py`
- **BoundLogger** (1 connections)
- **Provide a logger for tests.** (1 connections) — `server/tests/conftest.py`

## Relationships

- [NATS Messaging](NATS_Messaging.md) (1 shared connections)
- [conftest rationale Item](conftest_rationale_Item.md) (1 shared connections)

## Source Files

- `server/tests/conftest.py`

## Audit Trail

- EXTRACTED: 6 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*