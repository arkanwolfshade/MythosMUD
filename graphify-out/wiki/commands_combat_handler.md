# commands combat handler

> 8 nodes

## Key Concepts

- **reset_async_persistence()** (6 connections) — `server/async_persistence.py`
- **test_get_async_persistence_creates_instance()** (4 connections) — `server/tests/unit/infrastructure/test_async_persistence_delegates.py`
- **test_get_async_persistence_returns_same_instance()** (4 connections) — `server/tests/unit/infrastructure/test_async_persistence_delegates.py`
- **test_reset_async_persistence()** (4 connections) — `server/tests/unit/infrastructure/test_async_persistence_delegates.py`
- **Reset the global async persistence instance for testing.      DEPRECATED: Use Ap** (1 connections) — `server/async_persistence.py`
- **Test get_async_persistence creates singleton instance.** (1 connections) — `server/tests/unit/infrastructure/test_async_persistence_delegates.py`
- **Test get_async_persistence returns same instance on multiple calls.** (1 connections) — `server/tests/unit/infrastructure/test_async_persistence_delegates.py`
- **Test reset_async_persistence resets the singleton.** (1 connections) — `server/tests/unit/infrastructure/test_async_persistence_delegates.py`

## Relationships

- [schemas invite user](schemas_invite_user.md) (4 shared connections)
- [realtime websocket initial](realtime_websocket_initial.md) (3 shared connections)
- [NPC Combat](NPC_Combat.md) (1 shared connections)

## Source Files

- `server/async_persistence.py`
- `server/tests/unit/infrastructure/test_async_persistence_delegates.py`

## Audit Trail

- EXTRACTED: 22 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*