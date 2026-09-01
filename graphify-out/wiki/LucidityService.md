# LucidityService

> 166 nodes

## Key Concepts

- **LucidityService** (81 connections) — `server/services/lucidity_service.py`
- **PlayerLucidity** (71 connections) — `server/models/lucidity.py`
- **lucidity_service.py** (52 connections) — `server/services/lucidity_service.py`
- **test_lucidity_service.py** (27 connections) — `server/tests/unit/services/test_lucidity_service.py`
- **lucidity_helpers.py** (24 connections) — `server/services/lucidity_helpers.py`
- **lucidity_trigger_handlers.py** (19 connections) — `server/services/lucidity_trigger_handlers.py`
- **test_lucidity_trigger_handlers.py** (18 connections) — `server/tests/unit/services/test_lucidity_trigger_handlers.py`
- **CatatoniaObserverProtocol** (17 connections) — `server/services/lucidity_helpers.py`
- **asyncio** (15 connections)
- **handle_catatonia_transitions()** (13 connections) — `server/services/lucidity_trigger_handlers.py`
- **LucidityUpdateResult** (12 connections) — `server/services/lucidity_helpers.py`
- **encode_liabilities()** (12 connections) — `server/services/lucidity_helpers.py`
- **UUID** (12 connections)
- **decode_liabilities()** (11 connections) — `server/services/lucidity_helpers.py`
- **._finalize_lucidity_adjustment()** (10 connections) — `server/services/lucidity_service.py`
- **._send_lucidity_change_event_if_needed()** (10 connections) — `server/services/lucidity_service.py`
- **handle_delirium_and_sanitarium_triggers()** (10 connections) — `server/services/lucidity_trigger_handlers.py`
- **hallucination_frequency_service.py** (10 connections) — `server/services/hallucination_frequency_service.py`
- **UUID** (10 connections)
- **.apply_lucidity_adjustment()** (9 connections) — `server/services/lucidity_service.py`
- **handle_delirium_trigger()** (9 connections) — `server/services/lucidity_trigger_handlers.py`
- **handle_sanitarium_trigger()** (9 connections) — `server/services/lucidity_trigger_handlers.py`
- **test_lucidity_adjustment_round_trip()** (9 connections) — `server/tests/integration/test_lucidity_round_trip.py`
- **resolve_tier()** (8 connections) — `server/services/lucidity_helpers.py`
- **._apply_delta_to_record()** (8 connections) — `server/services/lucidity_service.py`
- *... and 141 more nodes in this community*

## Relationships

- [Player](Player.md) (33 shared connections)
- [test_player_respawn_service.py](test_player_respawn_service.py.md) (20 shared connections)
- [test_lucidity_event_dispatcher.py](test_lucidity_event_dispatcher.py.md) (15 shared connections)
- [.state](state.md) (10 shared connections)
- [debrief_command.py](debrief_command.py.md) (10 shared connections)
- [test_rescue_service.py](test_rescue_service.py.md) (9 shared connections)
- [test_lucidity_models.py](test_lucidity_models.py.md) (7 shared connections)
- [LucidityFluxService](LucidityFluxService.md) (7 shared connections)
- [test_admin_setlucidity_command.py](test_admin_setlucidity_command.py.md) (7 shared connections)
- [test_hallucination_services.py](test_hallucination_services.py.md) (7 shared connections)
- [coerce_int](coerce_int.md) (6 shared connections)
- [get_logger](get_logger.md) (6 shared connections)

## Source Files

- `server/models/lucidity.py`
- `server/services/active_lucidity_service.py`
- `server/services/hallucination_frequency_service.py`
- `server/services/lucidity_helpers.py`
- `server/services/lucidity_service.py`
- `server/services/lucidity_trigger_handlers.py`
- `server/tests/integration/test_lucidity_round_trip.py`
- `server/tests/unit/services/test_lucidity_service.py`
- `server/tests/unit/services/test_lucidity_trigger_handlers.py`
- `server/tests/unit/test_lucidity_service_smoke.py`

## Audit Trail

- EXTRACTED: 438 (86%)
- INFERRED: 70 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*