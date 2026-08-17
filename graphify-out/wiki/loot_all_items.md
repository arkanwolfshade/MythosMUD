# loot_all_items

> 43 nodes

## Key Concepts

- **loot_all_items()** (34 connections) — `server/api/container_endpoints_loot.py`
- **TestLootAllItems** (16 connections) — `server/tests/unit/api/test_container_endpoints_loot.py`
- **TestRegisterLootEndpoints** (14 connections) — `server/tests/unit/api/test_container_endpoints_loot_register.py`
- **asyncio** (9 connections)
- **.test_loot_all_items_capacity_error()** (7 connections) — `server/tests/unit/api/test_container_endpoints_loot.py`
- **.test_loot_all_items_container_not_found()** (7 connections) — `server/tests/unit/api/test_container_endpoints_loot.py`
- **.test_loot_all_items_locked_error()** (7 connections) — `server/tests/unit/api/test_container_endpoints_loot.py`
- **asyncio** (7 connections)
- **.test_loot_all_items_emit_event_failure()** (6 connections) — `server/tests/unit/api/test_container_endpoints_loot_register.py`
- **.test_loot_all_items_generic_exception()** (6 connections) — `server/tests/unit/api/test_container_endpoints_loot.py`
- **.test_loot_all_items_player_not_found()** (6 connections) — `server/tests/unit/api/test_container_endpoints_loot.py`
- **.test_loot_all_items_rate_limit_error()** (6 connections) — `server/tests/unit/api/test_container_endpoints_loot.py`
- **.test_loot_all_items_validation_error()** (6 connections) — `server/tests/unit/api/test_container_endpoints_loot.py`
- **.test_loot_all_items_all_items_looted()** (5 connections) — `server/tests/unit/api/test_container_endpoints_loot_register.py`
- **.test_loot_all_items_audit_log_error_handled()** (5 connections) — `server/tests/unit/api/test_container_endpoints_loot_register.py`
- **.test_loot_all_items_calculates_items_looted_correctly()** (5 connections) — `server/tests/unit/api/test_container_endpoints_loot_register.py`
- **.test_loot_all_items_different_source_types()** (5 connections) — `server/tests/unit/api/test_container_endpoints_loot_register.py`
- **.test_loot_all_items_empty_container()** (5 connections) — `server/tests/unit/api/test_container_endpoints_loot_register.py`
- **.test_loot_all_items_logger_info_called()** (5 connections) — `server/tests/unit/api/test_container_endpoints_loot_register.py`
- **.test_loot_all_items_final_container_none()** (5 connections) — `server/tests/unit/api/test_container_endpoints_loot.py`
- **.test_loot_all_items_success()** (5 connections) — `server/tests/unit/api/test_container_endpoints_loot.py`
- **_audit_loot_all()** (4 connections) — `server/api/container_endpoints_loot.py`
- **Any** (3 connections)
- **Request** (1 connections)
- **Loot all eligible items from a container.** (1 connections) — `server/api/container_endpoints_loot.py`
- *... and 18 more nodes in this community*

## Relationships

- [LootAllRequest](LootAllRequest.md) (22 shared connections)
- [get_logger](get_logger.md) (11 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (10 shared connections)
- [container_endpoints_basic.py](container_endpoints_basic.py.md) (6 shared connections)
- [ContainerComponent](ContainerComponent.md) (4 shared connections)
- [register_loot_endpoints](register_loot_endpoints.md) (1 shared connections)
- [handle_transfer_items_exceptions](handle_transfer_items_exceptions.md) (1 shared connections)
- [emit_loot_all_event](emit_loot_all_event.md) (1 shared connections)

## Source Files

- `server/api/container_endpoints_loot.py`
- `server/tests/unit/api/test_container_endpoints_loot.py`
- `server/tests/unit/api/test_container_endpoints_loot_register.py`

## Audit Trail

- EXTRACTED: 113 (89%)
- INFERRED: 14 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*