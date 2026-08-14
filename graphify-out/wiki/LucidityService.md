# LucidityService

> 140 nodes

## Key Concepts

- **LucidityService** (87 connections) — `server/services/lucidity_service.py`
- **PlayerLucidity** (57 connections) — `server/models/lucidity.py`
- **lucidity_service.py** (52 connections) — `server/services/lucidity_service.py`
- **lucidity_helpers.py** (24 connections) — `server/services/lucidity_helpers.py`
- **test_lucidity_service.py** (24 connections) — `server/tests/unit/services/test_lucidity_service.py`
- **lucidity_trigger_handlers.py** (19 connections) — `server/services/lucidity_trigger_handlers.py`
- **CatatoniaObserverProtocol** (17 connections) — `server/services/lucidity_helpers.py`
- **handle_catatonia_transitions()** (13 connections) — `server/services/lucidity_trigger_handlers.py`
- **asyncio** (13 connections)
- **encode_liabilities()** (12 connections) — `server/services/lucidity_helpers.py`
- **UUID** (12 connections)
- **decode_liabilities()** (11 connections) — `server/services/lucidity_helpers.py`
- **._finalize_lucidity_adjustment()** (10 connections) — `server/services/lucidity_service.py`
- **._send_lucidity_change_event_if_needed()** (10 connections) — `server/services/lucidity_service.py`
- **handle_delirium_and_sanitarium_triggers()** (10 connections) — `server/services/lucidity_trigger_handlers.py`
- **test_lucidity_round_trip.py** (10 connections) — `server/tests/integration/test_lucidity_round_trip.py`
- **.apply_lucidity_adjustment()** (9 connections) — `server/services/lucidity_service.py`
- **handle_sanitarium_trigger()** (9 connections) — `server/services/lucidity_trigger_handlers.py`
- **._apply_delta_to_record()** (8 connections) — `server/services/lucidity_service.py`
- **test_lucidity_adjustment_round_trip()** (8 connections) — `server/tests/integration/test_lucidity_round_trip.py`
- **utc_now()** (7 connections) — `server/services/lucidity_helpers.py`
- **._calculate_max_lcd()** (7 connections) — `server/services/lucidity_service.py`
- **LucidityAdjustmentFinalizeContext** (6 connections) — `server/services/lucidity_helpers.py`
- **LucidityChangeEventContext** (6 connections) — `server/services/lucidity_helpers.py`
- **._add_liabilities_for_adjustment()** (6 connections) — `server/services/lucidity_service.py`
- *... and 115 more nodes in this community*

## Relationships

- [lucidity.py](lucidity.py.md) (28 shared connections)
- [service.py](service.py.md) (14 shared connections)
- [debrief_command.py](debrief_command.py.md) (14 shared connections)
- [test_lucidity_event_dispatcher.py](test_lucidity_event_dispatcher.py.md) (14 shared connections)
- [get_logger](get_logger.md) (13 shared connections)
- [test_lucidity_trigger_handlers.py](test_lucidity_trigger_handlers.py.md) (12 shared connections)
- [Player](Player.md) (11 shared connections)
- [PlayerRespawnService](PlayerRespawnService.md) (11 shared connections)
- [test_rescue_service.py](test_rescue_service.py.md) (8 shared connections)
- [test_hallucination_services.py](test_hallucination_services.py.md) (8 shared connections)
- [rescue_commands.py](rescue_commands.py.md) (6 shared connections)
- [coerce_int](coerce_int.md) (6 shared connections)

## Source Files

- `server/models/lucidity.py`
- `server/services/active_lucidity_service.py`
- `server/services/lucidity_helpers.py`
- `server/services/lucidity_service.py`
- `server/services/lucidity_trigger_handlers.py`
- `server/tests/integration/test_lucidity_round_trip.py`
- `server/tests/unit/services/test_lucidity_service.py`
- `server/tests/unit/test_lucidity_service_smoke.py`

## Audit Trail

- EXTRACTED: 407 (93%)
- INFERRED: 32 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*