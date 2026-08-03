# lucidity services helpers

> 137 nodes

## Key Concepts

- **LucidityService** (78 connections) — `server/services/lucidity_service.py`
- **PlayerLucidity** (73 connections) — `server/models/lucidity.py`
- **lucidity_service.py** (50 connections) — `server/services/lucidity_service.py`
- **lucidity_helpers.py** (23 connections) — `server/services/lucidity_helpers.py`
- **lucidity_trigger_handlers.py** (18 connections) — `server/services/lucidity_trigger_handlers.py`
- **CatatoniaObserverProtocol** (17 connections) — `server/services/lucidity_helpers.py`
- **UUID** (14 connections)
- **decode_liabilities()** (11 connections) — `server/services/lucidity_helpers.py`
- **test_lucidity_service.py** (11 connections) — `server/tests/unit/services/test_lucidity_service.py`
- **._send_lucidity_change_event_if_needed()** (10 connections) — `server/services/lucidity_service.py`
- **._finalize_lucidity_adjustment()** (10 connections) — `server/services/lucidity_service.py`
- **handle_catatonia_transitions()** (10 connections) — `server/services/lucidity_trigger_handlers.py`
- **test_lucidity_round_trip.py** (10 connections) — `server/tests/integration/test_lucidity_round_trip.py`
- **.apply_lucidity_adjustment()** (9 connections) — `server/services/lucidity_service.py`
- **encode_liabilities()** (8 connections) — `server/services/lucidity_helpers.py`
- **._calculate_max_lcd()** (8 connections) — `server/services/lucidity_service.py`
- **._apply_delta_to_record()** (8 connections) — `server/services/lucidity_service.py`
- **handle_delirium_and_sanitarium_triggers()** (8 connections) — `server/services/lucidity_trigger_handlers.py`
- **liability_types.py** (8 connections) — `server/utils/liability_types.py`
- **utc_now()** (7 connections) — `server/services/lucidity_helpers.py`
- **LucidityUpdateResult** (7 connections) — `server/services/lucidity_helpers.py`
- **test_lucidity_adjustment_round_trip()** (7 connections) — `server/tests/integration/test_lucidity_round_trip.py`
- **LucidityChangeEventContext** (6 connections) — `server/services/lucidity_helpers.py`
- **LucidityAdjustmentFinalizeContext** (6 connections) — `server/services/lucidity_helpers.py`
- **._add_liabilities_for_adjustment()** (6 connections) — `server/services/lucidity_service.py`
- *... and 112 more nodes in this community*

## Relationships

- [lucidity models rationale](lucidity_models_rationale.md) (19 shared connections)
- [world models rationale](world_models_rationale.md) (18 shared connections)
- [commands admin mute](commands_admin_mute.md) (16 shared connections)
- [command inventory factories](command_inventory_factories.md) (16 shared connections)
- [Async Query Helpers](Async_Query_Helpers.md) (15 shared connections)
- [aggro threat services](aggro_threat_services.md) (15 shared connections)
- [command helpers functions](command_helpers_functions.md) (11 shared connections)
- [lucidity flux passive](lucidity_flux_passive.md) (9 shared connections)
- [rescue service services](rescue_service_services.md) (9 shared connections)
- [models lucidity rationale](models_lucidity_rationale.md) (7 shared connections)
- [models player rationale](models_player_rationale.md) (6 shared connections)
- [combat services persistence](combat_services_persistence.md) (6 shared connections)

## Source Files

- `server/models/lucidity.py`
- `server/services/active_lucidity_service.py`
- `server/services/lucidity_helpers.py`
- `server/services/lucidity_service.py`
- `server/services/lucidity_trigger_handlers.py`
- `server/tests/integration/test_lucidity_round_trip.py`
- `server/tests/unit/models/test_lucidity_models.py`
- `server/tests/unit/services/test_lucidity_service.py`
- `server/tests/unit/services/test_player_respawn_service.py`
- `server/tests/unit/test_lucidity_service_smoke.py`
- `server/utils/liability_types.py`

## Audit Trail

- EXTRACTED: 601 (90%)
- INFERRED: 65 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*