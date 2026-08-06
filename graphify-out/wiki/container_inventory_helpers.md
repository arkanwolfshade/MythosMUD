# container inventory helpers

> 43 nodes

## Key Concepts

- **test_container_helpers_inventory_ops.py** (52 connections) — `server/tests/unit/commands/test_container_helpers_inventory_ops.py`
- **transfer_item_to_container()** (20 connections) — `server/commands/container_helpers_inventory_ops.py`
- **transfer_item_from_container()** (18 connections) — `server/commands/container_helpers_inventory_ops.py`
- **_player_with_inventory()** (17 connections) — `server/tests/unit/commands/test_container_helpers_inventory_ops.py`
- **_coerce_transfer_quantity()** (8 connections) — `server/commands/container_helpers_inventory_ops.py`
- **_int_transfer_qty()** (8 connections) — `server/commands/container_helpers_inventory_ops.py`
- **_ensure_mutation_token()** (6 connections) — `server/commands/container_helpers_inventory_ops.py`
- **_ContainerSvcTokenOnly** (6 connections) — `server/tests/unit/commands/test_container_helpers_inventory_ops.py`
- **test_transfer_item_to_container_no_transfer_to_method()** (4 connections) — `server/tests/unit/commands/test_container_helpers_inventory_ops.py`
- **test_transfer_item_from_container_no_transfer_from()** (4 connections) — `server/tests/unit/commands/test_container_helpers_inventory_ops.py`
- **test_transfer_item_from_container_inventory_rows_fallback_non_dict_result()** (4 connections) — `server/tests/unit/commands/test_container_helpers_inventory_ops.py`
- **test_coerce_transfer_quantity_bool_is_one()** (3 connections) — `server/tests/unit/commands/test_container_helpers_inventory_ops.py`
- **test_int_transfer_qty_empty_string_uses_default_quantity()** (3 connections) — `server/tests/unit/commands/test_container_helpers_inventory_ops.py`
- **test_int_transfer_qty_zero_quantity_keeps_explicit_zero()** (3 connections) — `server/tests/unit/commands/test_container_helpers_inventory_ops.py`
- **test_transfer_item_to_container_success_uses_token_from_service()** (3 connections) — `server/tests/unit/commands/test_container_helpers_inventory_ops.py`
- **test_transfer_item_to_container_awaits_async_ensure_item_instance()** (3 connections) — `server/tests/unit/commands/test_container_helpers_inventory_ops.py`
- **test_transfer_item_to_container_coerces_string_quantity()** (3 connections) — `server/tests/unit/commands/test_container_helpers_inventory_ops.py`
- **test_transfer_item_to_container_missing_item_identifiers()** (3 connections) — `server/tests/unit/commands/test_container_helpers_inventory_ops.py`
- **test_transfer_item_to_container_rejects_non_positive_quantity()** (3 connections) — `server/tests/unit/commands/test_container_helpers_inventory_ops.py`
- **test_transfer_item_to_container_open_container_when_no_token()** (3 connections) — `server/tests/unit/commands/test_container_helpers_inventory_ops.py`
- **test_transfer_item_to_container_service_unavailable_no_open()** (3 connections) — `server/tests/unit/commands/test_container_helpers_inventory_ops.py`
- **test_transfer_item_to_container_transfer_raises()** (3 connections) — `server/tests/unit/commands/test_container_helpers_inventory_ops.py`
- **test_transfer_item_from_container_success_updates_inventory()** (3 connections) — `server/tests/unit/commands/test_container_helpers_inventory_ops.py`
- **test_transfer_item_from_container_rejects_non_positive_quantity()** (3 connections) — `server/tests/unit/commands/test_container_helpers_inventory_ops.py`
- **test_transfer_item_from_container_persist_failure_returns_error()** (3 connections) — `server/tests/unit/commands/test_container_helpers_inventory_ops.py`
- *... and 18 more nodes in this community*

## Relationships

- [mythosApp useMythosAppState useStatsRoll](mythosApp_useMythosAppState_useStatsRoll.md) (36 shared connections)
- [task registry app](task_registry_app.md) (3 shared connections)
- [monitoring endpoints rationale](monitoring_endpoints_rationale.md) (3 shared connections)

## Source Files

- `server/commands/container_helpers_inventory_ops.py`
- `server/tests/unit/commands/test_container_helpers_inventory_ops.py`

## Audit Trail

- EXTRACTED: 209 (98%)
- INFERRED: 5 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*