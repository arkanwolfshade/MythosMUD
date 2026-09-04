# Conftest

> 7 nodes

## Key Concepts

- **infrastructure/conftest.py** (6 connections) — `server/tests/unit/infrastructure/conftest.py`
- **async_persistence_layer()** (4 connections) — `server/tests/unit/infrastructure/conftest.py`
- **mock_event_bus()** (3 connections) — `server/tests/unit/infrastructure/conftest.py`
- **fixture** (2 connections)
- **Shared fixtures for unit tests in the infrastructure package.** (1 connections) — `server/tests/unit/infrastructure/conftest.py`
- **Create a mock event bus.** (1 connections) — `server/tests/unit/infrastructure/conftest.py`
- **Create an AsyncPersistenceLayer instance with skipped room cache.** (1 connections) — `server/tests/unit/infrastructure/conftest.py`

## Relationships

- [Async Persistence](Async_Persistence.md) (2 shared connections)
- [Container Exception Handling](Container_Exception_Handling.md) (1 shared connections)
- [Async Persistence & NPC Events](Async_Persistence_&_NPC_Events.md) (1 shared connections)

## Source Files

- `server/tests/unit/infrastructure/conftest.py`

## Audit Trail

- EXTRACTED: 11 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*