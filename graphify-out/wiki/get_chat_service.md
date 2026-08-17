# get_chat_service

> 8 nodes

## Key Concepts

- **get_chat_service()** (7 connections) — `server/dependencies.py`
- **TestGetChatService** (4 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **.test_get_chat_service_none_raises_runtime_error()** (3 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **.test_get_chat_service_success()** (3 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **Get a ChatService instance with dependency injection. Args: request: The…** (1 connections) — `server/dependencies.py`
- **Tests for get_chat_service dependency function.** (1 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **Test get_chat_service returns service when present.** (1 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **Test get_chat_service raises RuntimeError when service is None.** (1 connections) — `server/tests/unit/infrastructure/test_dependencies.py`

## Relationships

- [test_dependencies.py](test_dependencies.py.md) (2 shared connections)
- [get_container](get_container.md) (1 shared connections)
- [Request](Request.md) (1 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (1 shared connections)

## Source Files

- `server/dependencies.py`
- `server/tests/unit/infrastructure/test_dependencies.py`

## Audit Trail

- EXTRACTED: 13 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*