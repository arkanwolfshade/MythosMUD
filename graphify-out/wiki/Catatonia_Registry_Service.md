# Catatonia Registry Service

> 62 nodes · cohesion 0.05

## Key Concepts

- **CatatoniaRegistry** (44 connections) — `server/services/catatonia_registry.py`
- **TestCatatoniaRegistry** (26 connections) — `server/tests/unit/services/test_catatonia_registry.py`
- **UUID** (7 connections) — `server/services/catatonia_registry.py`
- **datetime** (5 connections) — `server/services/catatonia_registry.py`
- **.get_snapshot()** (3 connections) — `server/services/catatonia_registry.py`
- **.is_catatonic()** (3 connections) — `server/services/catatonia_registry.py`
- **.on_catatonia_cleared()** (3 connections) — `server/services/catatonia_registry.py`
- **.on_catatonia_entered()** (3 connections) — `server/services/catatonia_registry.py`
- **.should_trigger_sanitarium_failover()** (3 connections) — `server/services/catatonia_registry.py`
- **test_catatonia_registry.py** (3 connections) — `server/tests/unit/services/test_catatonia_registry.py`
- **Test on_sanitarium_failover with synchronous callback.** (3 connections) — `server/tests/unit/services/test_catatonia_registry.py`
- **.test_get_snapshot_empty()** (3 connections) — `server/tests/unit/services/test_catatonia_registry.py`
- **.test_get_snapshot_is_copy()** (3 connections) — `server/tests/unit/services/test_catatonia_registry.py`
- **.test_get_snapshot_with_players()** (3 connections) — `server/tests/unit/services/test_catatonia_registry.py`
- **.test_init()** (3 connections) — `server/tests/unit/services/test_catatonia_registry.py`
- **.test_init_with_failover_callback()** (3 connections) — `server/tests/unit/services/test_catatonia_registry.py`
- **.test_is_catatonic_after_cleared()** (3 connections) — `server/tests/unit/services/test_catatonia_registry.py`
- **.test_is_catatonic_with_string()** (3 connections) — `server/tests/unit/services/test_catatonia_registry.py`
- **.test_is_catatonic_with_uuid()** (3 connections) — `server/tests/unit/services/test_catatonia_registry.py`
- **.test_multiple_players_catatonic()** (3 connections) — `server/tests/unit/services/test_catatonia_registry.py`
- **.test_on_catatonia_cleared_not_registered()** (3 connections) — `server/tests/unit/services/test_catatonia_registry.py`
- **.test_on_catatonia_cleared_with_string()** (3 connections) — `server/tests/unit/services/test_catatonia_registry.py`
- **.test_on_catatonia_cleared_with_uuid()** (3 connections) — `server/tests/unit/services/test_catatonia_registry.py`
- **.test_on_catatonia_entered_with_string()** (3 connections) — `server/tests/unit/services/test_catatonia_registry.py`
- **.test_on_catatonia_entered_with_uuid()** (3 connections) — `server/tests/unit/services/test_catatonia_registry.py`
- *... and 37 more nodes in this community*

## Relationships

- [[NPC Admin API]] (5 shared connections)
- [[Combat Service Bundle]] (4 shared connections)
- [[Active Lucidity Service]] (3 shared connections)
- [[Lifespan Startup Hooks]] (2 shared connections)
- [[Inventory Service Helpers]] (1 shared connections)

## Source Files

- `server/services/catatonia_registry.py`
- `server/tests/unit/services/test_catatonia_registry.py`

## Audit Trail

- EXTRACTED: 196 (97%)
- INFERRED: 7 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
