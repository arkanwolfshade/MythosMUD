# test_npc_service.py

> 72 nodes

## Key Concepts

- **test_lucidity_event_dispatcher.py** (35 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **asyncio** (24 connections)
- **send_rescue_update_event()** (18 connections) — `server/services/lucidity_event_dispatcher.py`
- **lucidity_event_dispatcher.py** (18 connections) — `server/services/lucidity_event_dispatcher.py`
- **send_lucidity_change_event()** (15 connections) — `server/services/lucidity_event_dispatcher.py`
- **send_catatonia_event()** (12 connections) — `server/services/lucidity_event_dispatcher.py`
- **_dispatch_player_event()** (11 connections) — `server/services/lucidity_event_dispatcher.py`
- **_lucidity_change_payload_with_liabilities()** (11 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **LucidityChangeEventExtras** (9 connections) — `server/services/lucidity_event_dispatcher.py`
- **UUID** (6 connections)
- **test_send_lucidity_change_event_with_liabilities()** (5 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **test_send_lucidity_change_event_with_max_lcd()** (5 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **test_send_lucidity_change_event_with_metadata()** (5 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **test_send_lucidity_change_event_with_reason_and_source()** (5 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **_format_liabilities()** (4 connections) — `server/services/lucidity_event_dispatcher.py`
- **send_hallucination_event()** (4 connections) — `server/services/lucidity_event_dispatcher.py`
- **test_dispatch_player_event_import_error()** (4 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **test_dispatch_player_event_uuid_conversion()** (4 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **test_format_liabilities_empty()** (4 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **test_format_liabilities_empty_code()** (4 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **test_format_liabilities_invalid_stacks()** (4 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **test_format_liabilities_multiple_entries()** (4 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **test_format_liabilities_multiple_stacks()** (4 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **test_format_liabilities_single()** (4 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **test_send_catatonia_event_basic()** (4 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- *... and 47 more nodes in this community*

## Relationships

- [test_nats_messages.py](test_nats_messages.py.md) (7 shared connections)
- [MemoryProfiler](MemoryProfiler.md) (5 shared connections)
- [ContainerComponent](ContainerComponent.md) (4 shared connections)
- [NPCDefinition](NPCDefinition.md) (2 shared connections)
- [SchemaValidator](SchemaValidator.md) (2 shared connections)
- [generate_invites_db.py](generate_invites_db.py.md) (2 shared connections)

## Source Files

- `server/services/lucidity_event_dispatcher.py`
- `server/tests/unit/services/test_lucidity_event_dispatcher.py`

## Audit Trail

- EXTRACTED: 161 (98%)
- INFERRED: 4 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*