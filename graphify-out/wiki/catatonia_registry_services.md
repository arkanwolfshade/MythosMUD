# catatonia registry services

> 66 nodes

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
- *... and 41 more nodes in this community*

## Relationships

- [player death service](player_death_service.md) (3 shared connections)
- [NPC Definitions Admin](NPC_Definitions_Admin.md) (3 shared connections)
- [container helpers endpoints](container_helpers_endpoints.md) (2 shared connections)
- [lucidity services helpers](lucidity_services_helpers.md) (2 shared connections)
- [Loot Generation](Loot_Generation.md) (2 shared connections)
- [NPC Combat](NPC_Combat.md) (2 shared connections)
- [npc shopkeeper rationale](npc_shopkeeper_rationale.md) (1 shared connections)
- [nats services service](nats_services_service.md) (1 shared connections)
- [command validation commands](command_validation_commands.md) (1 shared connections)

## Source Files

- `server/services/catatonia_registry.py`
- `server/tests/unit/services/test_catatonia_registry.py`

## Audit Trail

- EXTRACTED: 208 (98%)
- INFERRED: 5 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*