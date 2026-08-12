# LucidityService

> 94 nodes

## Key Concepts

- **LucidityService** (77 connections) — `server/services/lucidity_service.py`
- **lucidity_service.py** (50 connections) — `server/services/lucidity_service.py`
- **lucidity_helpers.py** (23 connections) — `server/services/lucidity_helpers.py`
- **lucidity_trigger_handlers.py** (18 connections) — `server/services/lucidity_trigger_handlers.py`
- **CatatoniaObserverProtocol** (17 connections) — `server/services/lucidity_helpers.py`
- **UUID** (12 connections)
- **decode_liabilities()** (11 connections) — `server/services/lucidity_helpers.py`
- **._finalize_lucidity_adjustment()** (10 connections) — `server/services/lucidity_service.py`
- **._send_lucidity_change_event_if_needed()** (10 connections) — `server/services/lucidity_service.py`
- **handle_catatonia_transitions()** (10 connections) — `server/services/lucidity_trigger_handlers.py`
- **LucidityUpdateResult** (9 connections) — `server/services/lucidity_helpers.py`
- **.apply_lucidity_adjustment()** (9 connections) — `server/services/lucidity_service.py`
- **encode_liabilities()** (8 connections) — `server/services/lucidity_helpers.py`
- **._apply_delta_to_record()** (8 connections) — `server/services/lucidity_service.py`
- **handle_delirium_and_sanitarium_triggers()** (8 connections) — `server/services/lucidity_trigger_handlers.py`
- **liability_types.py** (8 connections) — `server/utils/liability_types.py`
- **utc_now()** (7 connections) — `server/services/lucidity_helpers.py`
- **._calculate_max_lcd()** (7 connections) — `server/services/lucidity_service.py`
- **LucidityAdjustmentFinalizeContext** (6 connections) — `server/services/lucidity_helpers.py`
- **LucidityChangeEventContext** (6 connections) — `server/services/lucidity_helpers.py`
- **._add_liabilities_for_adjustment()** (6 connections) — `server/services/lucidity_service.py`
- **.add_liability()** (6 connections) — `server/services/lucidity_service.py`
- **handle_sanitarium_trigger()** (6 connections) — `server/services/lucidity_trigger_handlers.py`
- **worsened_tier()** (5 connections) — `server/services/lucidity_helpers.py`
- **.clear_liability()** (5 connections) — `server/services/lucidity_service.py`
- *... and 69 more nodes in this community*

## Relationships

- [Player](Player.md) (30 shared connections)
- [test_lucidity_event_dispatcher.py](test_lucidity_event_dispatcher.py.md) (15 shared connections)
- [get_logger](get_logger.md) (9 shared connections)
- [test_lucidity_recovery_commands.py](test_lucidity_recovery_commands.py.md) (8 shared connections)
- [PlayerRespawnService](PlayerRespawnService.md) (7 shared connections)
- [debrief_command.py](debrief_command.py.md) (6 shared connections)
- [HallucinationFrequencyService](HallucinationFrequencyService.md) (6 shared connections)
- [test_lucidity_service.py](test_lucidity_service.py.md) (6 shared connections)
- [coerce_int](coerce_int.md) (6 shared connections)
- [LucidityFluxService](LucidityFluxService.md) (5 shared connections)
- [rescue_service.py](rescue_service.py.md) (4 shared connections)
- [ActiveLucidityService](ActiveLucidityService.md) (3 shared connections)

## Source Files

- `server/container/bundles/combat.py`
- `server/services/lucidity_helpers.py`
- `server/services/lucidity_service.py`
- `server/services/lucidity_trigger_handlers.py`
- `server/utils/liability_types.py`

## Audit Trail

- EXTRACTED: 451 (94%)
- INFERRED: 28 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*