# test_lucidity_event_dispatcher.py

> 87 nodes

## Key Concepts

- **test_lucidity_event_dispatcher.py** (35 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **send_rescue_update_event()** (25 connections) — `server/services/lucidity_event_dispatcher.py`
- **asyncio** (25 connections)
- **lucidity_event_dispatcher.py** (22 connections) — `server/services/lucidity_event_dispatcher.py`
- **send_lucidity_change_event()** (19 connections) — `server/services/lucidity_event_dispatcher.py`
- **send_catatonia_event()** (14 connections) — `server/services/lucidity_event_dispatcher.py`
- **LucidityChangeEventExtras** (12 connections) — `server/services/lucidity_event_dispatcher.py`
- **_lucidity_change_payload_with_liabilities()** (11 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **_dispatch_player_event()** (10 connections) — `server/services/lucidity_event_dispatcher.py`
- **liability_types.py** (8 connections) — `server/utils/liability_types.py`
- **DecodeLiabilitiesFn** (6 connections) — `server/utils/liability_types.py`
- **EncodeLiabilitiesFn** (6 connections) — `server/utils/liability_types.py`
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
- *... and 62 more nodes in this community*

## Relationships

- [LucidityService](LucidityService.md) (17 shared connections)
- [test_combat_event_publisher.py](test_combat_event_publisher.py.md) (7 shared connections)
- [get_logger](get_logger.md) (5 shared connections)
- [rescue_commands.py](rescue_commands.py.md) (5 shared connections)
- [test_message_category_invariants.py](test_message_category_invariants.py.md) (3 shared connections)
- [magic_service.py](magic_service.py.md) (2 shared connections)
- [websocket_initial_state.py](websocket_initial_state.py.md) (2 shared connections)
- [test_rescue_service.py](test_rescue_service.py.md) (2 shared connections)
- [MessageCategory](MessageCategory.md) (2 shared connections)
- [_handle_admin_hallucinate_command](_handle_admin_hallucinate_command.md) (2 shared connections)

## Source Files

- `server/services/lucidity_event_dispatcher.py`
- `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- `server/utils/liability_types.py`

## Audit Trail

- EXTRACTED: 199 (97%)
- INFERRED: 6 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*