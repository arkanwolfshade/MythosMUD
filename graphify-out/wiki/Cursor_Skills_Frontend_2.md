# Cursor Skills Frontend

> 8 nodes

## Key Concepts

- **TestGetContainer** (6 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **.test_get_container_success()** (3 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **.test_get_container_missing_raises_runtime_error()** (3 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **.test_get_container_no_state_attribute()** (3 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **Tests for get_container dependency function.** (1 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **Test get_container returns container when present.** (1 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **Test get_container raises RuntimeError when container not in app.state.** (1 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **Test get_container raises RuntimeError when app.state doesn't exist.** (1 connections) — `server/tests/unit/infrastructure/test_dependencies.py`

## Relationships

- [Player Domain Model](Player_Domain_Model.md) (4 shared connections)
- [Dead Code Cleanup Plan](Dead_Code_Cleanup_Plan.md) (1 shared connections)

## Source Files

- `server/tests/unit/infrastructure/test_dependencies.py`

## Audit Trail

- EXTRACTED: 18 (95%)
- INFERRED: 1 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*