# get_container

> 18 nodes

## Key Concepts

- **get_container()** (40 connections) — `server/dependencies.py`
- **TestGetContainer** (5 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **TestGetContainer** (5 connections) — `server/tests/unit/test_dependency_injection.py`
- **.test_get_container_missing_raises_runtime_error()** (3 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **.test_get_container_no_state_attribute()** (3 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **.test_get_container_success()** (3 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **.test_get_container_missing()** (3 connections) — `server/tests/unit/test_dependency_injection.py`
- **.test_get_container_no_app_state()** (3 connections) — `server/tests/unit/test_dependency_injection.py`
- **.test_get_container_success()** (3 connections) — `server/tests/unit/test_dependency_injection.py`
- **Get the application container from request state. This is the base dependency…** (1 connections) — `server/dependencies.py`
- **Tests for get_container dependency function.** (1 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **Test get_container returns container when present.** (1 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **Test get_container raises RuntimeError when container not in app.state.** (1 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **Test get_container raises RuntimeError when app.state doesn't exist.** (1 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **Test get_container() function.** (1 connections) — `server/tests/unit/test_dependency_injection.py`
- **Test get_container() returns container from app state.** (1 connections) — `server/tests/unit/test_dependency_injection.py`
- **Test get_container() raises error when container missing.** (1 connections) — `server/tests/unit/test_dependency_injection.py`
- **Test get_container() raises error when app.state missing.** (1 connections) — `server/tests/unit/test_dependency_injection.py`

## Relationships

- [ApplicationContainer](ApplicationContainer.md) (5 shared connections)
- [Request](Request.md) (4 shared connections)
- [test_dependencies.py](test_dependencies.py.md) (2 shared connections)
- [get_async_persistence](get_async_persistence.md) (1 shared connections)
- [get_catatonia_registry](get_catatonia_registry.md) (1 shared connections)
- [get_chat_service](get_chat_service.md) (1 shared connections)
- [get_combat_service](get_combat_service.md) (1 shared connections)
- [get_connection_manager](get_connection_manager.md) (1 shared connections)
- [get_exploration_service](get_exploration_service.md) (1 shared connections)
- [get_mp_regeneration_service](get_mp_regeneration_service.md) (1 shared connections)
- [get_mythos_time_consumer](get_mythos_time_consumer.md) (1 shared connections)
- [get_nats_message_handler](get_nats_message_handler.md) (1 shared connections)

## Source Files

- `server/dependencies.py`
- `server/tests/unit/infrastructure/test_dependencies.py`
- `server/tests/unit/test_dependency_injection.py`

## Audit Trail

- EXTRACTED: 56 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*