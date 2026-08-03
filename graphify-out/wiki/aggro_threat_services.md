# aggro threat services

> 77 nodes

## Key Concepts

- **test_lucidity_event_dispatcher.py** (34 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **lucidity_event_dispatcher.py** (18 connections) — `server/services/lucidity_event_dispatcher.py`
- **send_rescue_update_event()** (18 connections) — `server/services/lucidity_event_dispatcher.py`
- **send_lucidity_change_event()** (17 connections) — `server/services/lucidity_event_dispatcher.py`
- **LucidityChangeEventExtras** (12 connections) — `server/services/lucidity_event_dispatcher.py`
- **send_catatonia_event()** (12 connections) — `server/services/lucidity_event_dispatcher.py`
- **_dispatch_player_event()** (11 connections) — `server/services/lucidity_event_dispatcher.py`
- **_lucidity_change_payload_with_liabilities()** (11 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **._send_lucidity_change_event_if_needed()** (10 connections) — `server/services/lucidity_service.py`
- **liability_types.py** (8 connections) — `server/utils/liability_types.py`
- **send_hallucination_event()** (7 connections) — `server/services/lucidity_event_dispatcher.py`
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
- *... and 52 more nodes in this community*

## Relationships

- [lucidity services helpers](lucidity_services_helpers.md) (17 shared connections)
- [command helpers functions](command_helpers_functions.md) (7 shared connections)
- [services service phantom](services_service_phantom.md) (3 shared connections)
- [Async Query Helpers](Async_Query_Helpers.md) (3 shared connections)
- [combat services messaging](combat_services_messaging.md) (2 shared connections)
- [models npc rationale](models_npc_rationale.md) (2 shared connections)
- [combat services persistence](combat_services_persistence.md) (2 shared connections)
- [combat models rationale](combat_models_rationale.md) (2 shared connections)

## Source Files

- `server/services/lucidity_event_dispatcher.py`
- `server/services/lucidity_service.py`
- `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- `server/utils/liability_types.py`

## Audit Trail

- EXTRACTED: 284 (99%)
- INFERRED: 2 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*