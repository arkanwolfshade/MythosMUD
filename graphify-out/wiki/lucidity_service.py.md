# lucidity_service.py

> 138 nodes · cohesion 0.03

## Key Concepts

- **lucidity_service.py** (50 connections) — `server/services/lucidity_service.py`
- **test_lucidity_event_dispatcher.py** (34 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **lucidity_helpers.py** (23 connections) — `server/services/lucidity_helpers.py`
- **lucidity_event_dispatcher.py** (18 connections) — `server/services/lucidity_event_dispatcher.py`
- **send_rescue_update_event()** (18 connections) — `server/services/lucidity_event_dispatcher.py`
- **lucidity_trigger_handlers.py** (18 connections) — `server/services/lucidity_trigger_handlers.py`
- **send_lucidity_change_event()** (17 connections) — `server/services/lucidity_event_dispatcher.py`
- **CatatoniaObserverProtocol** (17 connections) — `server/services/lucidity_helpers.py`
- **LucidityChangeEventExtras** (12 connections) — `server/services/lucidity_event_dispatcher.py`
- **send_catatonia_event()** (12 connections) — `server/services/lucidity_event_dispatcher.py`
- **_dispatch_player_event()** (11 connections) — `server/services/lucidity_event_dispatcher.py`
- **decode_liabilities()** (11 connections) — `server/services/lucidity_helpers.py`
- **_lucidity_change_payload_with_liabilities()** (11 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **._finalize_lucidity_adjustment()** (10 connections) — `server/services/lucidity_service.py`
- **._send_lucidity_change_event_if_needed()** (10 connections) — `server/services/lucidity_service.py`
- **handle_catatonia_transitions()** (10 connections) — `server/services/lucidity_trigger_handlers.py`
- **.apply_lucidity_adjustment()** (9 connections) — `server/services/lucidity_service.py`
- **encode_liabilities()** (8 connections) — `server/services/lucidity_helpers.py`
- **resolve_tier()** (8 connections) — `server/services/lucidity_helpers.py`
- **._apply_delta_to_record()** (8 connections) — `server/services/lucidity_service.py`
- **handle_delirium_and_sanitarium_triggers()** (8 connections) — `server/services/lucidity_trigger_handlers.py`
- **liability_types.py** (8 connections) — `server/utils/liability_types.py`
- **LucidityUpdateResult** (7 connections) — `server/services/lucidity_helpers.py`
- **utc_now()** (7 connections) — `server/services/lucidity_helpers.py`
- **UUID** (6 connections)
- *... and 113 more nodes in this community*

## Relationships

- [LucidityService](LucidityService.md) (28 shared connections)
- [PlayerLucidity](PlayerLucidity.md) (14 shared connections)
- [get_logger](get_logger.md) (8 shared connections)
- [test_lucidity_models.py](test_lucidity_models.py.md) (8 shared connections)
- [._prepare_sanitarium_respawn](_prepare_sanitarium_respawn.md) (8 shared connections)
- [lucidity.py](lucidity.py.md) (6 shared connections)
- [coerce_int](coerce_int.md) (5 shared connections)
- [hallucinations.py](hallucinations.py.md) (3 shared connections)
- [PassiveLucidityFluxService](PassiveLucidityFluxService.md) (3 shared connections)
- [Player](Player.md) (3 shared connections)
- [send_game_event](send_game_event.md) (2 shared connections)
- [CatatoniaRegistry](CatatoniaRegistry.md) (2 shared connections)

## Source Files

- `server/services/lucidity_event_dispatcher.py`
- `server/services/lucidity_helpers.py`
- `server/services/lucidity_service.py`
- `server/services/lucidity_trigger_handlers.py`
- `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- `server/utils/liability_types.py`

## Audit Trail

- EXTRACTED: 570 (97%)
- INFERRED: 18 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*