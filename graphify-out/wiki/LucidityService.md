# LucidityService

> 165 nodes

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
- **test_lucidity_round_trip.py** (11 connections) — `server/tests/integration/test_lucidity_round_trip.py`
- **._finalize_lucidity_adjustment()** (10 connections) — `server/services/lucidity_service.py`
- **._send_lucidity_change_event_if_needed()** (10 connections) — `server/services/lucidity_service.py`
- **handle_delirium_and_sanitarium_triggers()** (10 connections) — `server/services/lucidity_trigger_handlers.py`
- **UUID** (10 connections)
- **.apply_lucidity_adjustment()** (9 connections) — `server/services/lucidity_service.py`
- **handle_delirium_trigger()** (9 connections) — `server/services/lucidity_trigger_handlers.py`
- **handle_sanitarium_trigger()** (9 connections) — `server/services/lucidity_trigger_handlers.py`
- **test_lucidity_adjustment_round_trip()** (9 connections) — `server/tests/integration/test_lucidity_round_trip.py`
- **._apply_delta_to_record()** (8 connections) — `server/services/lucidity_service.py`
- **._calculate_max_lcd()** (8 connections) — `server/services/lucidity_service.py`
- *... and 140 more nodes in this community*

## Relationships

- [lucidity.py](lucidity.py.md) (30 shared connections)
- [test_lucidity_event_dispatcher.py](test_lucidity_event_dispatcher.py.md) (15 shared connections)
- [service.py](service.py.md) (13 shared connections)
- [test_player_respawn_service.py](test_player_respawn_service.py.md) (12 shared connections)
- [.state](state.md) (10 shared connections)
- [PlayerRespawnService](PlayerRespawnService.md) (10 shared connections)
- [test_rescue_service.py](test_rescue_service.py.md) (9 shared connections)
- [test_hallucination_services.py](test_hallucination_services.py.md) (8 shared connections)
- [test_admin_setlucidity_command.py](test_admin_setlucidity_command.py.md) (7 shared connections)
- [get_logger](get_logger.md) (7 shared connections)
- [pytest.md](pytest.md.md) (7 shared connections)
- [debrief_command.py](debrief_command.py.md) (6 shared connections)

## Source Files

- `server/models/lucidity.py`
- `server/services/active_lucidity_service.py`
- `server/services/lucidity_helpers.py`
- `server/services/lucidity_service.py`
- `server/services/lucidity_trigger_handlers.py`
- `server/tests/integration/test_lucidity_round_trip.py`
- `server/tests/unit/services/test_lucidity_service.py`
- `server/tests/unit/services/test_lucidity_trigger_handlers.py`
- `server/tests/unit/test_lucidity_service_smoke.py`
- `server/utils/liability_types.py`

## Audit Trail

- EXTRACTED: 441 (87%)
- INFERRED: 67 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*