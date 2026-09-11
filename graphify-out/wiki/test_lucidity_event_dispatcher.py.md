# test_lucidity_event_dispatcher.py

> 83 nodes

## Key Concepts

- **test_lucidity_event_dispatcher.py** (34 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **asyncio** (24 connections)
- **lucidity_trigger_handlers.py** (19 connections) — `server/services/lucidity_trigger_handlers.py`
- **send_rescue_update_event()** (18 connections) — `server/services/lucidity_event_dispatcher.py`
- **lucidity_event_dispatcher.py** (18 connections) — `server/services/lucidity_event_dispatcher.py`
- **send_lucidity_change_event()** (17 connections) — `server/services/lucidity_event_dispatcher.py`
- **handle_catatonia_transitions()** (13 connections) — `server/services/lucidity_trigger_handlers.py`
- **LucidityChangeEventExtras** (12 connections) — `server/services/lucidity_event_dispatcher.py`
- **send_catatonia_event()** (12 connections) — `server/services/lucidity_event_dispatcher.py`
- **_lucidity_change_payload_with_liabilities()** (11 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **_dispatch_player_event()** (10 connections) — `server/services/lucidity_event_dispatcher.py`
- **._send_lucidity_change_event_if_needed()** (10 connections) — `server/services/lucidity_service.py`
- **liability_types.py** (8 connections) — `server/utils/liability_types.py`
- **utc_now()** (7 connections) — `server/services/lucidity_helpers.py`
- **UUID** (6 connections)
- **test_send_lucidity_change_event_with_liabilities()** (5 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **test_send_lucidity_change_event_with_max_lcd()** (5 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **test_send_lucidity_change_event_with_metadata()** (5 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **test_send_lucidity_change_event_with_reason_and_source()** (5 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **_format_liabilities()** (4 connections) — `server/services/lucidity_event_dispatcher.py`
- **test_dispatch_player_event_import_error()** (4 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **test_dispatch_player_event_uuid_conversion()** (4 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **test_format_liabilities_empty()** (4 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **test_format_liabilities_empty_code()** (4 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **test_format_liabilities_invalid_stacks()** (4 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- *... and 58 more nodes in this community*

## Relationships

- [Player](Player.md) (24 shared connections)
- [test_lucidity_trigger_handlers.py](test_lucidity_trigger_handlers.py.md) (11 shared connections)
- [LucidityService](LucidityService.md) (6 shared connections)
- [get_logger](get_logger.md) (4 shared connections)
- [CatatoniaObserverProtocol](CatatoniaObserverProtocol.md) (3 shared connections)
- [test_rescue_service.py](test_rescue_service.py.md) (2 shared connections)
- [hallucinations.py](hallucinations.py.md) (2 shared connections)
- [DecodeLiabilitiesFn](DecodeLiabilitiesFn.md) (2 shared connections)
- [PlayerRespawnService](PlayerRespawnService.md) (1 shared connections)
- [event_types.py](event_types.py.md) (1 shared connections)

## Source Files

- `server/services/lucidity_event_dispatcher.py`
- `server/services/lucidity_helpers.py`
- `server/services/lucidity_service.py`
- `server/services/lucidity_trigger_handlers.py`
- `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- `server/utils/liability_types.py`

## Audit Trail

- EXTRACTED: 206 (97%)
- INFERRED: 6 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*