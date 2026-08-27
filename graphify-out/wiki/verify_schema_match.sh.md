# verify_schema_match.sh

> 5 nodes

## Key Concepts

- **user_manager()** (6 connections) — `server/tests/unit/services/test_user_manager.py`
- **mock_data_dir()** (3 connections) — `server/tests/unit/services/test_user_manager.py`
- **fixture** (2 connections)
- **Create a temporary data directory.** (1 connections) — `server/tests/unit/services/test_user_manager.py`
- **Create a UserManager instance.** (1 connections) — `server/tests/unit/services/test_user_manager.py`

## Relationships

- [server/models/game.py](server-models-game.py.md) (2 shared connections)
- [container_persistence.py](container_persistence.py.md) (1 shared connections)
- [test_error_logging.py](test_error_logging.py.md) (1 shared connections)
- [App.tsx](App.tsx.md) (1 shared connections)

## Source Files

- `server/tests/unit/services/test_user_manager.py`

## Audit Trail

- EXTRACTED: 6 (67%)
- INFERRED: 3 (33%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*