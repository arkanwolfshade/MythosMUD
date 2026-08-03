# invite models create

> 6 nodes

## Key Concepts

- **conftest.py** (5 connections) — `server/tests/unit/infrastructure/conftest.py`
- **async_persistence_layer()** (3 connections) — `server/tests/unit/infrastructure/conftest.py`
- **mock_event_bus()** (2 connections) — `server/tests/unit/infrastructure/conftest.py`
- **Shared fixtures for unit tests in the infrastructure package.** (1 connections) — `server/tests/unit/infrastructure/conftest.py`
- **Create a mock event bus.** (1 connections) — `server/tests/unit/infrastructure/conftest.py`
- **Create an AsyncPersistenceLayer instance with skipped room cache.** (1 connections) — `server/tests/unit/infrastructure/conftest.py`

## Relationships

- [NPC Combat](NPC_Combat.md) (2 shared connections)
- [Database Config](Database_Config.md) (1 shared connections)

## Source Files

- `server/tests/unit/infrastructure/conftest.py`

## Audit Trail

- EXTRACTED: 13 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*