# server tests unit test dependency

> 8 nodes

## Key Concepts

- **TestGetContainer** (5 connections) — `server/tests/unit/test_dependency_injection.py`
- **.test_get_container_missing()** (3 connections) — `server/tests/unit/test_dependency_injection.py`
- **.test_get_container_no_app_state()** (3 connections) — `server/tests/unit/test_dependency_injection.py`
- **.test_get_container_success()** (3 connections) — `server/tests/unit/test_dependency_injection.py`
- **Test get_container() function.** (1 connections) — `server/tests/unit/test_dependency_injection.py`
- **Test get_container() returns container from app state.** (1 connections) — `server/tests/unit/test_dependency_injection.py`
- **Test get_container() raises error when container missing.** (1 connections) — `server/tests/unit/test_dependency_injection.py`
- **Test get_container() raises error when app.state missing.** (1 connections) — `server/tests/unit/test_dependency_injection.py`

## Relationships

- [server dependencies](server_dependencies.md) (4 shared connections)

## Source Files

- `server/tests/unit/test_dependency_injection.py`

## Audit Trail

- EXTRACTED: 11 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*