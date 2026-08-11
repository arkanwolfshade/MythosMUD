# Catatonia Registry Service

> 68 nodes

## Key Concepts

- **CatatoniaRegistry** (43 connections) — `server/services/catatonia_registry.py`
- **TestCatatoniaRegistry** (26 connections) — `server/tests/unit/services/test_catatonia_registry.py`
- **catatonia_registry.py** (12 connections) — `server/services/catatonia_registry.py`
- **.initialize()** (7 connections) — `server/container/bundles/combat.py`
- **UUID** (6 connections)
- **datetime** (4 connections)
- **.is_catatonic()** (4 connections) — `server/services/catatonia_registry.py`
- **test_catatonia_registry.py** (4 connections) — `server/tests/unit/services/test_catatonia_registry.py`
- **.on_catatonia_entered()** (3 connections) — `server/services/catatonia_registry.py`
- **.on_catatonia_cleared()** (3 connections) — `server/services/catatonia_registry.py`
- **.should_trigger_sanitarium_failover()** (3 connections) — `server/services/catatonia_registry.py`
- **.get_snapshot()** (3 connections) — `server/services/catatonia_registry.py`
- **.test_init()** (3 connections) — `server/tests/unit/services/test_catatonia_registry.py`
- **.test_init_with_failover_callback()** (3 connections) — `server/tests/unit/services/test_catatonia_registry.py`
- **.test_should_trigger_sanitarium_failover_never_triggered()** (3 connections) — `server/tests/unit/services/test_catatonia_registry.py`
- **.test_should_trigger_sanitarium_failover_within_debounce_window()** (3 connections) — `server/tests/unit/services/test_catatonia_registry.py`
- **.test_on_sanitarium_failover_debounced_does_not_invoke_callback_twice()** (3 connections) — `server/tests/unit/services/test_catatonia_registry.py`
- **.test_on_catatonia_entered_with_uuid()** (3 connections) — `server/tests/unit/services/test_catatonia_registry.py`
- **.test_on_catatonia_entered_with_string()** (3 connections) — `server/tests/unit/services/test_catatonia_registry.py`
- **.test_on_catatonia_cleared_with_uuid()** (3 connections) — `server/tests/unit/services/test_catatonia_registry.py`
- **.test_on_catatonia_cleared_with_string()** (3 connections) — `server/tests/unit/services/test_catatonia_registry.py`
- **.test_on_catatonia_cleared_not_registered()** (3 connections) — `server/tests/unit/services/test_catatonia_registry.py`
- **.test_on_sanitarium_failover_with_uuid()** (3 connections) — `server/tests/unit/services/test_catatonia_registry.py`
- **.test_on_sanitarium_failover_with_string()** (3 connections) — `server/tests/unit/services/test_catatonia_registry.py`
- **.test_on_sanitarium_failover_with_sync_callback()** (3 connections) — `server/tests/unit/services/test_catatonia_registry.py`
- *... and 43 more nodes in this community*

## Relationships

- [User Manager Mute Tests](User_Manager_Mute_Tests.md) (4 shared connections)
- [WebSocket Code Review](WebSocket_Code_Review.md) (3 shared connections)
- [Player Domain Model](Player_Domain_Model.md) (3 shared connections)
- [Container Component Capacity](Container_Component_Capacity.md) (2 shared connections)
- [Enhanced Logging Exceptions](Enhanced_Logging_Exceptions.md) (2 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (2 shared connections)
- [NPC Services Bundle](NPC_Services_Bundle.md) (1 shared connections)
- [Zone Config Loader](Zone_Config_Loader.md) (1 shared connections)
- [Panel Layout Libraries Spec](Panel_Layout_Libraries_Spec.md) (1 shared connections)
- [Realtime Service Bundle](Realtime_Service_Bundle.md) (1 shared connections)
- [Catatonia Check Logic](Catatonia_Check_Logic.md) (1 shared connections)

## Source Files

- `server/container/bundles/combat.py`
- `server/services/catatonia_registry.py`
- `server/tests/unit/services/test_catatonia_registry.py`

## Audit Trail

- EXTRACTED: 216 (98%)
- INFERRED: 5 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*