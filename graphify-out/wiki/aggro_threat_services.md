# aggro threat services

> 71 nodes

## Key Concepts

- **test_lucidity_event_dispatcher.py** (34 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **lucidity_event_dispatcher.py** (18 connections) — `server/services/lucidity_event_dispatcher.py`
- **send_rescue_update_event()** (18 connections) — `server/services/lucidity_event_dispatcher.py`
- **send_lucidity_change_event()** (17 connections) — `server/services/lucidity_event_dispatcher.py`
- **LucidityChangeEventExtras** (12 connections) — `server/services/lucidity_event_dispatcher.py`
- **send_catatonia_event()** (12 connections) — `server/services/lucidity_event_dispatcher.py`
- **_dispatch_player_event()** (11 connections) — `server/services/lucidity_event_dispatcher.py`
- **_lucidity_change_payload_with_liabilities()** (11 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **UUID** (6 connections)
- **_format_liabilities()** (4 connections) — `server/services/lucidity_event_dispatcher.py`
- **test_send_lucidity_change_event_with_max_lcd()** (4 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **test_send_lucidity_change_event_with_liabilities()** (4 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **test_send_lucidity_change_event_with_reason_and_source()** (4 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **test_send_lucidity_change_event_with_metadata()** (4 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **test_format_liabilities_empty()** (3 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **test_format_liabilities_single()** (3 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **test_format_liabilities_multiple_stacks()** (3 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **test_format_liabilities_multiple_entries()** (3 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **test_format_liabilities_invalid_stacks()** (3 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **test_format_liabilities_empty_code()** (3 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **test_send_lucidity_change_event_basic()** (3 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **test_send_lucidity_change_event_string_player_id()** (3 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **test_send_lucidity_change_event_dispatch_error()** (3 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **test_send_catatonia_event_basic()** (3 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **test_send_catatonia_event_with_current_lcd()** (3 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- *... and 46 more nodes in this community*

## Relationships

- [lucidity services helpers](lucidity_services_helpers.md) (15 shared connections)
- [command helpers functions](command_helpers_functions.md) (5 shared connections)
- [services service phantom](services_service_phantom.md) (3 shared connections)
- [connection manager realtime](connection_manager_realtime.md) (2 shared connections)
- [command inventory factories](command_inventory_factories.md) (2 shared connections)
- [rescue service services](rescue_service_services.md) (2 shared connections)
- [Async Query Helpers](Async_Query_Helpers.md) (1 shared connections)

## Source Files

- `server/services/lucidity_event_dispatcher.py`
- `server/tests/unit/services/test_lucidity_event_dispatcher.py`

## Audit Trail

- EXTRACTED: 256 (99%)
- INFERRED: 2 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*