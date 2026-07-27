# Lucidity Event Dispatcher

> 60 nodes · cohesion 0.06

## Key Concepts

- **test_lucidity_event_dispatcher.py** (33 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **LucidityChangeEventExtras** (24 connections) — `server/services/lucidity_event_dispatcher.py`
- **lucidity_event_dispatcher.py** (17 connections) — `server/services/lucidity_event_dispatcher.py`
- **send_lucidity_change_event()** (17 connections) — `server/services/lucidity_event_dispatcher.py`
- **send_catatonia_event()** (12 connections) — `server/services/lucidity_event_dispatcher.py`
- **_dispatch_player_event()** (11 connections) — `server/services/lucidity_event_dispatcher.py`
- **_lucidity_change_payload_with_liabilities()** (11 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **send_hallucination_event()** (7 connections) — `server/services/lucidity_event_dispatcher.py`
- **UUID** (6 connections) — `server/services/lucidity_event_dispatcher.py`
- **LiabilityStackEntry** (4 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **_format_liabilities()** (4 connections) — `server/services/lucidity_event_dispatcher.py`
- **test_send_lucidity_change_event_with_liabilities()** (4 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **test_send_lucidity_change_event_with_max_lcd()** (4 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **test_send_lucidity_change_event_with_metadata()** (4 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **test_send_lucidity_change_event_with_reason_and_source()** (4 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **Test send_lucidity_change_event with basic parameters.** (3 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **test_dispatch_player_event_import_error()** (3 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **test_dispatch_player_event_uuid_conversion()** (3 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **test_format_liabilities_empty()** (3 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **test_format_liabilities_empty_code()** (3 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **test_format_liabilities_invalid_stacks()** (3 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **test_format_liabilities_multiple_entries()** (3 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **test_format_liabilities_multiple_stacks()** (3 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **test_format_liabilities_single()** (3 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **test_send_catatonia_event_basic()** (3 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- *... and 35 more nodes in this community*

## Relationships

- [[Lucidity Rescue Helpers]] (14 shared connections)
- [[Lucidity State Models]] (13 shared connections)
- [[Hallucination Trigger Service]] (3 shared connections)
- [[Liability . Call ()]] (2 shared connections)
- [[Combat Player Broadcasts]] (2 shared connections)
- [[NPC Admin API]] (2 shared connections)
- [[Alias Expansion Logic]] (1 shared connections)
- [[Active Lucidity Service]] (1 shared connections)

## Source Files

- `server/services/lucidity_event_dispatcher.py`
- `server/tests/unit/services/test_lucidity_event_dispatcher.py`

## Audit Trail

- EXTRACTED: 229 (94%)
- INFERRED: 15 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
