# Cursor Skills Audit

> 6 nodes

## Key Concepts

- **test_inventory_service_helpers.py** (6 connections) — `server/tests/unit/commands/test_inventory_service_helpers.py`
- **_request_with_persistence()** (3 connections) — `server/tests/unit/commands/test_inventory_service_helpers.py`
- **test_get_shared_services_raises_without_async_persistence()** (2 connections) — `server/tests/unit/commands/test_inventory_service_helpers.py`
- **test_get_shared_services_initializes_and_reuses_singletons()** (2 connections) — `server/tests/unit/commands/test_inventory_service_helpers.py`
- **reset_shared_inventory_services_autouse()** (1 connections) — `server/tests/unit/commands/test_inventory_service_helpers.py`
- **Unit tests for inventory_service_helpers.get_shared_services.** (1 connections) — `server/tests/unit/commands/test_inventory_service_helpers.py`

## Relationships

- [Container Component Capacity](Container_Component_Capacity.md) (1 shared connections)

## Source Files

- `server/tests/unit/commands/test_inventory_service_helpers.py`

## Audit Trail

- EXTRACTED: 15 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*