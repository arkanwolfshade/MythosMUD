# test_inventory_service_helpers.py

> 9 nodes

## Key Concepts

- **test_inventory_service_helpers.py** (7 connections) — `server/tests/unit/commands/test_inventory_service_helpers.py`
- **reset_shared_inventory_services_for_tests()** (3 connections) — `server/commands/inventory_service_helpers.py`
- **_request_with_persistence()** (3 connections) — `server/tests/unit/commands/test_inventory_service_helpers.py`
- **reset_shared_inventory_services_autouse()** (3 connections) — `server/tests/unit/commands/test_inventory_service_helpers.py`
- **test_get_shared_services_initializes_and_reuses_singletons()** (3 connections) — `server/tests/unit/commands/test_inventory_service_helpers.py`
- **test_get_shared_services_raises_without_async_persistence()** (3 connections) — `server/tests/unit/commands/test_inventory_service_helpers.py`
- **fixture** (1 connections)
- **Clear lazy singletons so each test gets a fresh init path. For unit tests only;…** (1 connections) — `server/commands/inventory_service_helpers.py`
- **Unit tests for inventory_service_helpers.get_shared_services.** (1 connections) — `server/tests/unit/commands/test_inventory_service_helpers.py`

## Relationships

- [inventory_command_helpers.py](inventory_command_helpers.py.md) (2 shared connections)
- [test_container_helpers_inventory_find.py](test_container_helpers_inventory_find.py.md) (2 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/commands/inventory_service_helpers.py`
- `server/tests/unit/commands/test_inventory_service_helpers.py`

## Audit Trail

- EXTRACTED: 15 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*