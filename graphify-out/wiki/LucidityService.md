# LucidityService

> 139 nodes

## Key Concepts

- **LucidityService** (79 connections) — `server/services/lucidity_service.py`
- **PlayerLucidity** (69 connections) — `server/models/lucidity.py`
- **lucidity_service.py** (52 connections) — `server/services/lucidity_service.py`
- **test_lucidity_service.py** (25 connections) — `server/tests/unit/services/test_lucidity_service.py`
- **lucidity_helpers.py** (24 connections) — `server/services/lucidity_helpers.py`
- **lucidity_trigger_handlers.py** (19 connections) — `server/services/lucidity_trigger_handlers.py`
- **CatatoniaObserverProtocol** (17 connections) — `server/services/lucidity_helpers.py`
- **handle_catatonia_transitions()** (13 connections) — `server/services/lucidity_trigger_handlers.py`
- **asyncio** (13 connections)
- **LucidityUpdateResult** (12 connections) — `server/services/lucidity_helpers.py`
- **encode_liabilities()** (12 connections) — `server/services/lucidity_helpers.py`
- **UUID** (12 connections)
- **decode_liabilities()** (11 connections) — `server/services/lucidity_helpers.py`
- **test_lucidity_round_trip.py** (11 connections) — `server/tests/integration/test_lucidity_round_trip.py`
- **._finalize_lucidity_adjustment()** (10 connections) — `server/services/lucidity_service.py`
- **._send_lucidity_change_event_if_needed()** (10 connections) — `server/services/lucidity_service.py`
- **handle_delirium_and_sanitarium_triggers()** (10 connections) — `server/services/lucidity_trigger_handlers.py`
- **.apply_lucidity_adjustment()** (9 connections) — `server/services/lucidity_service.py`
- **handle_sanitarium_trigger()** (9 connections) — `server/services/lucidity_trigger_handlers.py`
- **test_lucidity_adjustment_round_trip()** (9 connections) — `server/tests/integration/test_lucidity_round_trip.py`
- **._apply_delta_to_record()** (8 connections) — `server/services/lucidity_service.py`
- **utc_now()** (7 connections) — `server/services/lucidity_helpers.py`
- **._calculate_max_lcd()** (7 connections) — `server/services/lucidity_service.py`
- **test_lucidity_service_smoke.py** (7 connections) — `server/tests/unit/test_lucidity_service_smoke.py`
- **LucidityAdjustmentFinalizeContext** (6 connections) — `server/services/lucidity_helpers.py`
- *... and 114 more nodes in this community*

## Relationships

- [lucidity.py](lucidity.py.md) (30 shared connections)
- [test_lucidity_event_dispatcher.py](test_lucidity_event_dispatcher.py.md) (14 shared connections)
- [service.py](service.py.md) (13 shared connections)
- [test_lucidity_trigger_handlers.py](test_lucidity_trigger_handlers.py.md) (12 shared connections)
- [test_player_respawn_service.py](test_player_respawn_service.py.md) (11 shared connections)
- [.state](state.md) (10 shared connections)
- [test_rescue_service.py](test_rescue_service.py.md) (9 shared connections)
- [Player](Player.md) (8 shared connections)
- [PlayerRespawnService](PlayerRespawnService.md) (8 shared connections)
- [test_hallucination_services.py](test_hallucination_services.py.md) (8 shared connections)
- [test_admin_setlucidity_command.py](test_admin_setlucidity_command.py.md) (7 shared connections)
- [debrief_command.py](debrief_command.py.md) (6 shared connections)

## Source Files

- `server/models/lucidity.py`
- `server/services/lucidity_helpers.py`
- `server/services/lucidity_service.py`
- `server/services/lucidity_trigger_handlers.py`
- `server/tests/integration/test_lucidity_round_trip.py`
- `server/tests/unit/services/test_lucidity_service.py`
- `server/tests/unit/test_lucidity_service_smoke.py`

## Audit Trail

- EXTRACTED: 380 (85%)
- INFERRED: 69 (15%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*