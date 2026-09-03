# Test Catatonia Registry

> 66 nodes

## Key Concepts

- **CatatoniaRegistry** (42 connections) — `server/services/catatonia_registry.py`
- **TestCatatoniaRegistry** (26 connections) — `server/tests/unit/services/test_catatonia_registry.py`
- **.initialize()** (8 connections) — `server/container/bundles/combat.py`
- **UUID** (6 connections)
- **test_catatonia_registry.py** (6 connections) — `server/tests/unit/services/test_catatonia_registry.py`
- **.is_catatonic()** (4 connections) — `server/services/catatonia_registry.py`
- **.test_on_sanitarium_failover_with_async_callback()** (4 connections) — `server/tests/unit/services/test_catatonia_registry.py`
- **datetime** (4 connections)
- **.get_snapshot()** (3 connections) — `server/services/catatonia_registry.py`
- **.on_catatonia_cleared()** (3 connections) — `server/services/catatonia_registry.py`
- **.on_catatonia_entered()** (3 connections) — `server/services/catatonia_registry.py`
- **.should_trigger_sanitarium_failover()** (3 connections) — `server/services/catatonia_registry.py`
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
- *... and 41 more nodes in this community*

## Relationships

- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (4 shared connections)
- [Test Lifespan Startup](Test_Lifespan_Startup.md) (2 shared connections)
- [Application Container Bundles](Application_Container_Bundles.md) (2 shared connections)
- [Lucidity Helpers & Catatonia](Lucidity_Helpers_&_Catatonia.md) (2 shared connections)
- [Test Container Bundles](Test_Container_Bundles.md) (2 shared connections)
- [Dependency Injection (FastAPI)](Dependency_Injection_FastAPI.md) (1 shared connections)
- [Equipment & Inventory Helpers](Equipment_&_Inventory_Helpers.md) (1 shared connections)
- [Test Player Combat Service](Test_Player_Combat_Service.md) (1 shared connections)
- [Test Player Death Service](Test_Player_Death_Service.md) (1 shared connections)
- [Service](Service.md) (1 shared connections)
- [Catatonia Check](Catatonia_Check.md) (1 shared connections)
- [Container Exception Handling](Container_Exception_Handling.md) (1 shared connections)

## Source Files

- `server/container/bundles/combat.py`
- `server/services/catatonia_registry.py`
- `server/tests/unit/services/test_catatonia_registry.py`

## Audit Trail

- EXTRACTED: 112 (97%)
- INFERRED: 4 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*