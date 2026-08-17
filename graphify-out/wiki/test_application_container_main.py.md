# test_application_container_main.py

> 22 nodes

## Key Concepts

- **test_application_container_main.py** (18 connections) — `server/tests/unit/container/test_application_container_main.py`
- **_flatten_bundle()** (7 connections) — `server/container/main.py`
- **.initialize()** (5 connections) — `server/container/main.py`
- **._initialize_secondary_bundles()** (5 connections) — `server/container/main.py`
- **asyncio** (4 connections)
- **.get_service()** (3 connections) — `server/container/main.py`
- **test_get_service_unknown_and_none()** (3 connections) — `server/tests/unit/container/test_application_container_main.py`
- **test_initialize_skips_when_already_initialized()** (3 connections) — `server/tests/unit/container/test_application_container_main.py`
- **test_initialize_success_with_mocked_bundles()** (3 connections) — `server/tests/unit/container/test_application_container_main.py`
- **test_shutdown_calls_bundles()** (3 connections) — `server/tests/unit/container/test_application_container_main.py`
- **test_shutdown_logs_runtime_error()** (3 connections) — `server/tests/unit/container/test_application_container_main.py`
- **Any** (3 connections)
- **._link_cross_bundle_services()** (2 connections) — `server/container/main.py`
- **test_decode_and_normalize_delegates()** (2 connections) — `server/tests/unit/container/test_application_container_main.py`
- **test_flatten_bundle_copies_existing_attrs()** (2 connections) — `server/tests/unit/container/test_application_container_main.py`
- **test_get_project_root_caches()** (2 connections) — `server/tests/unit/container/test_application_container_main.py`
- **test_get_service_not_initialized()** (2 connections) — `server/tests/unit/container/test_application_container_main.py`
- **test_is_initialized_property()** (2 connections) — `server/tests/unit/container/test_application_container_main.py`
- **Copy bundle attributes onto container for backward compatibility.** (1 connections) — `server/container/main.py`
- **Initialize all services via domain bundles in dependency order.** (1 connections) — `server/container/main.py`
- **Get a service by name.** (1 connections) — `server/container/main.py`
- **Gap coverage for ApplicationContainer main module accessors.** (1 connections) — `server/tests/unit/container/test_application_container_main.py`

## Relationships

- [ApplicationContainer](ApplicationContainer.md) (16 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (6 shared connections)
- [test_application_container.py](test_application_container.py.md) (2 shared connections)
- [test_container_helpers_inventory_ops.py](test_container_helpers_inventory_ops.py.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/container/main.py`
- `server/tests/unit/container/test_application_container_main.py`

## Audit Trail

- EXTRACTED: 41 (80%)
- INFERRED: 10 (20%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*