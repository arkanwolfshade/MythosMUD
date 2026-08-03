# lucidity services helpers

> 90 nodes

## Key Concepts

- **lucidity_service.py** (52 connections) — `server/services/lucidity_service.py`
- **lucidity_helpers.py** (24 connections) — `server/services/lucidity_helpers.py`
- **lucidity_trigger_handlers.py** (19 connections) — `server/services/lucidity_trigger_handlers.py`
- **CatatoniaObserverProtocol** (17 connections) — `server/services/lucidity_helpers.py`
- **test_lucidity_trigger_handlers.py** (17 connections) — `server/tests/unit/services/test_lucidity_trigger_handlers.py`
- **UUID** (14 connections)
- **handle_catatonia_transitions()** (13 connections) — `server/services/lucidity_trigger_handlers.py`
- **encode_liabilities()** (12 connections) — `server/services/lucidity_helpers.py`
- **decode_liabilities()** (11 connections) — `server/services/lucidity_helpers.py`
- **LucidityUpdateResult** (10 connections) — `server/services/lucidity_helpers.py`
- **._finalize_lucidity_adjustment()** (10 connections) — `server/services/lucidity_service.py`
- **handle_delirium_and_sanitarium_triggers()** (10 connections) — `server/services/lucidity_trigger_handlers.py`
- **UUID** (10 connections)
- **.apply_lucidity_adjustment()** (9 connections) — `server/services/lucidity_service.py`
- **handle_delirium_trigger()** (9 connections) — `server/services/lucidity_trigger_handlers.py`
- **handle_sanitarium_trigger()** (9 connections) — `server/services/lucidity_trigger_handlers.py`
- **._apply_delta_to_record()** (8 connections) — `server/services/lucidity_service.py`
- **utc_now()** (7 connections) — `server/services/lucidity_helpers.py`
- **Tier** (6 connections)
- **LucidityChangeEventContext** (6 connections) — `server/services/lucidity_helpers.py`
- **LucidityAdjustmentFinalizeContext** (6 connections) — `server/services/lucidity_helpers.py`
- **._add_liabilities_for_adjustment()** (6 connections) — `server/services/lucidity_service.py`
- **.add_liability()** (6 connections) — `server/services/lucidity_service.py`
- **worsened_tier()** (5 connections) — `server/services/lucidity_helpers.py`
- **UUID** (5 connections)
- *... and 65 more nodes in this community*

## Relationships

- [combat services persistence](combat_services_persistence.md) (27 shared connections)
- [aggro threat services](aggro_threat_services.md) (17 shared connections)
- [world models rationale](world_models_rationale.md) (11 shared connections)
- [combat models rationale](combat_models_rationale.md) (9 shared connections)
- [models npc rationale](models_npc_rationale.md) (7 shared connections)
- [models player rationale](models_player_rationale.md) (5 shared connections)
- [lucidity flux passive](lucidity_flux_passive.md) (5 shared connections)
- [lucidity models rationale](lucidity_models_rationale.md) (4 shared connections)
- [Async Query Helpers](Async_Query_Helpers.md) (4 shared connections)
- [movement monitor game](movement_monitor_game.md) (3 shared connections)
- [command helpers functions](command_helpers_functions.md) (2 shared connections)
- [catatonia registry services](catatonia_registry_services.md) (1 shared connections)

## Source Files

- `server/services/lucidity_helpers.py`
- `server/services/lucidity_service.py`
- `server/services/lucidity_trigger_handlers.py`
- `server/tests/unit/commands/test_admin_setlucidity_command.py`
- `server/tests/unit/services/test_lucidity_trigger_handlers.py`

## Audit Trail

- EXTRACTED: 414 (95%)
- INFERRED: 22 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*