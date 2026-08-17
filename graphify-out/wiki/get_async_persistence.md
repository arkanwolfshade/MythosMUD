# get_async_persistence

> 8 nodes

## Key Concepts

- **get_async_persistence()** (9 connections) — `server/dependencies.py`
- **TestGetAsyncPersistence** (4 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **.test_get_async_persistence_none_raises_runtime_error()** (3 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **.test_get_async_persistence_success()** (3 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **Get an AsyncPersistenceLayer instance with dependency injection. This function…** (1 connections) — `server/dependencies.py`
- **Tests for get_async_persistence dependency function.** (1 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **Test get_async_persistence returns service when present.** (1 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **Test get_async_persistence raises RuntimeError when service is None.** (1 connections) — `server/tests/unit/infrastructure/test_dependencies.py`

## Relationships

- [test_dependencies.py](test_dependencies.py.md) (2 shared connections)
- [get_container](get_container.md) (1 shared connections)
- [api/character_creation.py](api-character_creation.py.md) (1 shared connections)
- [container_endpoints_basic.py](container_endpoints_basic.py.md) (1 shared connections)
- [Request](Request.md) (1 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (1 shared connections)

## Source Files

- `server/dependencies.py`
- `server/tests/unit/infrastructure/test_dependencies.py`

## Audit Trail

- EXTRACTED: 15 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*