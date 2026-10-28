# intersection_schema.json

> 10 nodes · cohesion 0.20

## Key Concepts

- **test_database.py** (7 connections) — `server/tests/unit/infrastructure/test_database.py`
- **test_database_manager_initial_state()** (5 connections) — `server/tests/unit/infrastructure/test_database.py`
- **test_database_manager_reset_instance()** (5 connections) — `server/tests/unit/infrastructure/test_database.py`
- **test_database_manager_singleton()** (5 connections) — `server/tests/unit/infrastructure/test_database.py`
- **test_database_manager_direct_init_raises()** (4 connections) — `server/tests/unit/infrastructure/test_database.py`
- **Unit tests for database initialization.** (1 connections) — `server/tests/unit/infrastructure/test_database.py`
- **Test that DatabaseManager is a singleton.** (1 connections) — `server/tests/unit/infrastructure/test_database.py`
- **Test resetting the singleton instance.** (1 connections) — `server/tests/unit/infrastructure/test_database.py`
- **Test that direct initialization raises RuntimeError when instance exists.** (1 connections) — `server/tests/unit/infrastructure/test_database.py`
- **Test initial state of database manager.** (1 connections) — `server/tests/unit/infrastructure/test_database.py`

## Relationships

- [resolve_lazy_attr](resolve_lazy_attr.md) (7 shared connections)
- [InventoryPanel.tsx](InventoryPanel.tsx.md) (5 shared connections)
- [combat_taunt.py](combat_taunt.py.md) (1 shared connections)

## Source Files

- `server/tests/unit/infrastructure/test_database.py`

## Audit Trail

- EXTRACTED: 19 (86%)
- INFERRED: 3 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*