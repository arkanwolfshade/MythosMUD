# server api container endpoints loot

> 50 nodes

## Key Concepts

- **loot_all_items()** (34 connections) — `server/api/container_endpoints_loot.py`
- **TestLootAllItems** (16 connections) — `server/tests/unit/api/test_container_endpoints_loot.py`
- **TestRegisterLootEndpoints** (14 connections) — `server/tests/unit/api/test_container_endpoints_loot_register.py`
- **test_container_endpoints_loot.py** (13 connections) — `server/tests/unit/api/test_container_endpoints_loot.py`
- **asyncio** (9 connections)
- **.test_loot_all_items_capacity_error()** (7 connections) — `server/tests/unit/api/test_container_endpoints_loot.py`
- **.test_loot_all_items_container_not_found()** (7 connections) — `server/tests/unit/api/test_container_endpoints_loot.py`
- **.test_loot_all_items_locked_error()** (7 connections) — `server/tests/unit/api/test_container_endpoints_loot.py`
- **asyncio** (7 connections)
- **register_loot_endpoints()** (6 connections) — `server/api/container_endpoints_loot.py`
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
- **.test_register_loot_endpoints()** (3 connections) — `server/tests/unit/api/test_container_endpoints_loot_register.py`
- *... and 25 more nodes in this community*

## Relationships

- [server api container helpers get](server_api_container_helpers_get.md) (24 shared connections)
- [docs examples logging fastapi integration](docs_examples_logging_fastapi_integration.md) (14 shared connections)
- [server api players](server_api_players.md) (10 shared connections)
- [server models container containercomponent](server_models_container_containercomponent.md) (9 shared connections)
- [server services container service](server_services_container_service.md) (4 shared connections)
- [server api container events](server_api_container_events.md) (2 shared connections)
- [server api container exception handlers](server_api_container_exception_handlers.md) (1 shared connections)
- [claude rules pytest](claude_rules_pytest.md) (1 shared connections)
- [claude rules sqlalchemy](claude_rules_sqlalchemy.md) (1 shared connections)

## Source Files

- `server/api/container_endpoints_loot.py`
- `server/tests/unit/api/test_container_endpoints_loot.py`
- `server/tests/unit/api/test_container_endpoints_loot_register.py`

## Audit Trail

- EXTRACTED: 130 (90%)
- INFERRED: 15 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*