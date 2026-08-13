# LucidityService

> 132 nodes

## Key Concepts

- **LucidityService** (77 connections) — `server/services/lucidity_service.py`
- **PlayerLucidity** (55 connections) — `server/models/lucidity.py`
- **lucidity_service.py** (50 connections) — `server/services/lucidity_service.py`
- **lucidity.py** (33 connections) — `server/models/lucidity.py`
- **lucidity_helpers.py** (23 connections) — `server/services/lucidity_helpers.py`
- **lucidity_trigger_handlers.py** (18 connections) — `server/services/lucidity_trigger_handlers.py`
- **CatatoniaObserverProtocol** (17 connections) — `server/services/lucidity_helpers.py`
- **UUID** (12 connections)
- **decode_liabilities()** (11 connections) — `server/services/lucidity_helpers.py`
- **._apply_sanitarium_liability_update()** (11 connections) — `server/services/player_respawn_service.py`
- **test_lucidity_service.py** (11 connections) — `server/tests/unit/services/test_lucidity_service.py`
- **._finalize_lucidity_adjustment()** (10 connections) — `server/services/lucidity_service.py`
- **._send_lucidity_change_event_if_needed()** (10 connections) — `server/services/lucidity_service.py`
- **handle_catatonia_transitions()** (10 connections) — `server/services/lucidity_trigger_handlers.py`
- **test_lucidity_round_trip.py** (10 connections) — `server/tests/integration/test_lucidity_round_trip.py`
- **LucidityUpdateResult** (9 connections) — `server/services/lucidity_helpers.py`
- **.apply_lucidity_adjustment()** (9 connections) — `server/services/lucidity_service.py`
- **encode_liabilities()** (8 connections) — `server/services/lucidity_helpers.py`
- **resolve_tier()** (8 connections) — `server/services/lucidity_helpers.py`
- **._apply_delta_to_record()** (8 connections) — `server/services/lucidity_service.py`
- **handle_delirium_and_sanitarium_triggers()** (8 connections) — `server/services/lucidity_trigger_handlers.py`
- **test_lucidity_adjustment_round_trip()** (8 connections) — `server/tests/integration/test_lucidity_round_trip.py`
- **liability_types.py** (8 connections) — `server/utils/liability_types.py`
- **utc_now()** (7 connections) — `server/services/lucidity_helpers.py`
- **._calculate_max_lcd()** (7 connections) — `server/services/lucidity_service.py`
- *... and 107 more nodes in this community*

## Relationships

- [test_lucidity_models.py](test_lucidity_models.py.md) (24 shared connections)
- [log_and_raise](log_and_raise.md) (18 shared connections)
- [test_lucidity_event_dispatcher.py](test_lucidity_event_dispatcher.py.md) (15 shared connections)
- [get_logger](get_logger.md) (13 shared connections)
- [LucidityFluxService](LucidityFluxService.md) (12 shared connections)
- [test_lucidity_recovery_commands.py](test_lucidity_recovery_commands.py.md) (12 shared connections)
- [PlayerRespawnService](PlayerRespawnService.md) (11 shared connections)
- [test_rescue_service.py](test_rescue_service.py.md) (10 shared connections)
- [rescue_commands.py](rescue_commands.py.md) (8 shared connections)
- [debrief_command.py](debrief_command.py.md) (7 shared connections)
- [hallucinations.py](hallucinations.py.md) (7 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (6 shared connections)

## Source Files

- `server/models/lucidity.py`
- `server/services/lucidity_helpers.py`
- `server/services/lucidity_service.py`
- `server/services/lucidity_trigger_handlers.py`
- `server/services/player_respawn_service.py`
- `server/tests/integration/test_lucidity_round_trip.py`
- `server/tests/unit/services/test_lucidity_service.py`
- `server/tests/unit/test_lucidity_service_smoke.py`
- `server/utils/liability_types.py`

## Audit Trail

- EXTRACTED: 396 (92%)
- INFERRED: 34 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*