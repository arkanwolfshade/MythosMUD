# test_lucidity_event_dispatcher.py

> 74 nodes

## Key Concepts

- **test_lucidity_event_dispatcher.py** (35 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **send_game_event()** (29 connections) — `server/realtime/connection_manager_api.py`
- **asyncio** (24 connections)
- **send_rescue_update_event()** (18 connections) — `server/services/lucidity_event_dispatcher.py`
- **lucidity_event_dispatcher.py** (18 connections) — `server/services/lucidity_event_dispatcher.py`
- **send_lucidity_change_event()** (17 connections) — `server/services/lucidity_event_dispatcher.py`
- **LucidityChangeEventExtras** (12 connections) — `server/services/lucidity_event_dispatcher.py`
- **send_catatonia_event()** (12 connections) — `server/services/lucidity_event_dispatcher.py`
- **_dispatch_player_event()** (11 connections) — `server/services/lucidity_event_dispatcher.py`
- **_lucidity_change_payload_with_liabilities()** (11 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **liability_types.py** (8 connections) — `server/utils/liability_types.py`
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
- **test_format_liabilities_multiple_entries()** (4 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **test_format_liabilities_multiple_stacks()** (4 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **test_format_liabilities_single()** (4 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- *... and 49 more nodes in this community*

## Relationships

- [LucidityService](LucidityService.md) (16 shared connections)
- [resolve_lazy_attr](resolve_lazy_attr.md) (7 shared connections)
- [command_service.py](command_service.py.md) (5 shared connections)
- [test_follow_service.py](test_follow_service.py.md) (4 shared connections)
- [get_logger](get_logger.md) (4 shared connections)
- [PhantomHostileService](PhantomHostileService.md) (3 shared connections)
- [test_magic_healing_events.py](test_magic_healing_events.py.md) (2 shared connections)
- [magic_service.py](magic_service.py.md) (2 shared connections)
- [Spell](Spell.md) (2 shared connections)
- [test_lucidity_trigger_handlers.py](test_lucidity_trigger_handlers.py.md) (2 shared connections)
- [DecodeLiabilitiesFn](DecodeLiabilitiesFn.md) (2 shared connections)
- [MPRegenerationService](MPRegenerationService.md) (1 shared connections)

## Source Files

- `server/realtime/connection_manager_api.py`
- `server/services/lucidity_event_dispatcher.py`
- `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- `server/utils/liability_types.py`

## Audit Trail

- EXTRACTED: 194 (97%)
- INFERRED: 6 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*