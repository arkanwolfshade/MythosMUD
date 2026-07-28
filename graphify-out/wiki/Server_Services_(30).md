# Server Services (30)

> 63 nodes

## Key Concepts

- **CatatoniaRegistry** (43 connections) — `server/services/catatonia_registry.py`
- **TestCatatoniaRegistry** (26 connections) — `server/tests/unit/services/test_catatonia_registry.py`
- **catatonia_registry.py** (12 connections) — `server/services/catatonia_registry.py`
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
- **.test_on_sanitarium_failover_with_async_callback()** (3 connections) — `server/tests/unit/services/test_catatonia_registry.py`
- *... and 38 more nodes in this community*

## Relationships

- [Server App](Server_App.md) (3 shared connections)
- [Server Infrastructure](Server_Infrastructure.md) (3 shared connections)
- [Server Api](Server_Api.md) (2 shared connections)
- [Server Services](Server_Services.md) (2 shared connections)
- [Server Commands](Server_Commands.md) (2 shared connections)
- [Server App (2)](Server_App_%282%29.md) (2 shared connections)
- [Server Npc (6)](Server_Npc_%286%29.md) (1 shared connections)
- [Server Services (62)](Server_Services_%2862%29.md) (1 shared connections)
- [Server Command Handler](Server_Command_Handler.md) (1 shared connections)

## Source Files

- `server/services/catatonia_registry.py`
- `server/tests/unit/services/test_catatonia_registry.py`

## Audit Trail

- EXTRACTED: 208 (98%)
- INFERRED: 5 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*