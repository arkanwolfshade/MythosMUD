# Loot All Endpoint

> 76 nodes · cohesion 0.05

## Key Concepts

- **LootAllRequest** (80 connections) — `server/api/container_models.py`
- **loot_all_items()** (37 connections) — `server/api/container_endpoints_loot.py`
- **TestLootAllItems** (19 connections) — `server/tests/unit/api/test_container_endpoints_loot.py`
- **TestRegisterLootEndpoints** (14 connections) — `server/tests/unit/api/test_container_endpoints_loot_register.py`
- **TestGetContainerAndPlayerForLootAll** (14 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **TestEmitLootAllEvent** (13 connections) — `server/tests/unit/api/test_container_events.py`
- **test_container_endpoints_loot_register.py** (9 connections) — `server/tests/unit/api/test_container_endpoints_loot_register.py`
- **register_loot_endpoints()** (6 connections) — `server/api/container_endpoints_loot.py`
- **.test_loot_all_items_emit_event_failure()** (6 connections) — `server/tests/unit/api/test_container_endpoints_loot_register.py`
- **.test_loot_all_items_capacity_error()** (6 connections) — `server/tests/unit/api/test_container_endpoints_loot.py`
- **.test_loot_all_items_container_not_found()** (6 connections) — `server/tests/unit/api/test_container_endpoints_loot.py`
- **.test_loot_all_items_generic_exception()** (6 connections) — `server/tests/unit/api/test_container_endpoints_loot.py`
- **.test_loot_all_items_locked_error()** (6 connections) — `server/tests/unit/api/test_container_endpoints_loot.py`
- **.test_loot_all_items_player_not_found()** (5 connections) — `server/tests/unit/api/test_container_endpoints_loot.py`
- **.test_loot_all_items_rate_limit_error()** (5 connections) — `server/tests/unit/api/test_container_endpoints_loot.py`
- **.test_loot_all_items_validation_error()** (5 connections) — `server/tests/unit/api/test_container_endpoints_loot.py`
- **.test_emit_loot_all_event_emission_error()** (5 connections) — `server/tests/unit/api/test_container_events.py`
- **.test_loot_all_items_all_items_looted()** (4 connections) — `server/tests/unit/api/test_container_endpoints_loot_register.py`
- **.test_loot_all_items_audit_log_error_handled()** (4 connections) — `server/tests/unit/api/test_container_endpoints_loot_register.py`
- **.test_loot_all_items_calculates_items_looted_correctly()** (4 connections) — `server/tests/unit/api/test_container_endpoints_loot_register.py`
- **.test_loot_all_items_different_source_types()** (4 connections) — `server/tests/unit/api/test_container_endpoints_loot_register.py`
- **.test_loot_all_items_empty_container()** (4 connections) — `server/tests/unit/api/test_container_endpoints_loot_register.py`
- **.test_loot_all_items_logger_info_called()** (4 connections) — `server/tests/unit/api/test_container_endpoints_loot_register.py`
- **.test_loot_all_items_final_container_none()** (4 connections) — `server/tests/unit/api/test_container_endpoints_loot.py`
- **.test_loot_all_items_success()** (4 connections) — `server/tests/unit/api/test_container_endpoints_loot.py`
- *... and 51 more nodes in this community*

## Relationships

- [[Container API Endpoints]] (45 shared connections)
- [[Container Exception Handlers]] (24 shared connections)
- [[Container Loot Helpers]] (16 shared connections)
- [[Inventory Service Helpers]] (5 shared connections)
- [[Container Component Capacity]] (5 shared connections)
- [[Container Open Events]] (4 shared connections)
- [[Database Manager Tests]] (3 shared connections)
- [[NPC Admin API]] (2 shared connections)
- [[Standardized Error Responses]] (2 shared connections)
- [[Admin NPC Schemas]] (1 shared connections)
- [[API Test Fixtures]] (1 shared connections)

## Source Files

- `server/api/container_endpoints_loot.py`
- `server/api/container_models.py`
- `server/tests/unit/api/test_container_endpoints_loot.py`
- `server/tests/unit/api/test_container_endpoints_loot_register.py`
- `server/tests/unit/api/test_container_events.py`
- `server/tests/unit/api/test_container_helpers_loot.py`

## Audit Trail

- EXTRACTED: 299 (82%)
- INFERRED: 67 (18%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
