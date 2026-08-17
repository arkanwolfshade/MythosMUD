# server services lucidity event dispatcher

> 53 nodes

## Key Concepts

- **test_lucidity_event_dispatcher.py** (35 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **asyncio** (24 connections)
- **send_lucidity_change_event()** (17 connections) — `server/services/lucidity_event_dispatcher.py`
- **LucidityChangeEventExtras** (12 connections) — `server/services/lucidity_event_dispatcher.py`
- **_lucidity_change_payload_with_liabilities()** (11 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **test_send_lucidity_change_event_with_liabilities()** (5 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **test_send_lucidity_change_event_with_max_lcd()** (5 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **test_send_lucidity_change_event_with_metadata()** (5 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **test_send_lucidity_change_event_with_reason_and_source()** (5 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **test_dispatch_player_event_import_error()** (4 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **test_dispatch_player_event_uuid_conversion()** (4 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **test_format_liabilities_empty()** (4 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **test_format_liabilities_empty_code()** (4 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **test_format_liabilities_invalid_stacks()** (4 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **test_format_liabilities_multiple_entries()** (4 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **test_format_liabilities_multiple_stacks()** (4 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **test_format_liabilities_single()** (4 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **test_send_catatonia_event_basic()** (4 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **test_send_catatonia_event_dispatch_error()** (4 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **test_send_catatonia_event_with_current_lcd()** (4 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **test_send_catatonia_event_with_message()** (4 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **test_send_catatonia_event_with_rescuer_and_target()** (4 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **test_send_lucidity_change_event_basic()** (4 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **test_send_lucidity_change_event_dispatch_error()** (4 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **test_send_lucidity_change_event_string_player_id()** (4 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- *... and 28 more nodes in this community*

## Relationships

- [server services lucidity event dispatcher](server_services_lucidity_event_dispatcher.md) (21 shared connections)
- [server commands admin setlucidity command](server_commands_admin_setlucidity_command.md) (5 shared connections)
- [characterinfo](characterinfo.md) (1 shared connections)
- [server utils liability types](server_utils_liability_types.md) (1 shared connections)
- [server tests unit services test](server_tests_unit_services_test.md) (1 shared connections)

## Source Files

- `server/services/lucidity_event_dispatcher.py`
- `server/tests/unit/services/test_lucidity_event_dispatcher.py`

## Audit Trail

- EXTRACTED: 120 (95%)
- INFERRED: 6 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*