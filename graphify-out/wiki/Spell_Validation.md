# Spell Validation

> 39 nodes

## Key Concepts

- **lucidity_trigger_handlers.py** (19 connections) — `server/services/lucidity_trigger_handlers.py`
- **CatatoniaObserverProtocol** (17 connections) — `server/services/lucidity_helpers.py`
- **test_lucidity_trigger_handlers.py** (17 connections) — `server/tests/unit/services/test_lucidity_trigger_handlers.py`
- **handle_catatonia_transitions()** (13 connections) — `server/services/lucidity_trigger_handlers.py`
- **handle_delirium_and_sanitarium_triggers()** (10 connections) — `server/services/lucidity_trigger_handlers.py`
- **UUID** (10 connections)
- **handle_delirium_trigger()** (9 connections) — `server/services/lucidity_trigger_handlers.py`
- **handle_sanitarium_trigger()** (9 connections) — `server/services/lucidity_trigger_handlers.py`
- **utc_now()** (7 connections) — `server/services/lucidity_helpers.py`
- **UUID** (5 connections)
- **UUID** (5 connections)
- **datetime** (4 connections)
- **.on_catatonia_entered()** (4 connections) — `server/services/lucidity_helpers.py`
- **.on_catatonia_cleared()** (4 connections) — `server/services/lucidity_helpers.py`
- **.on_sanitarium_failover()** (3 connections) — `server/services/lucidity_helpers.py`
- **.should_trigger_sanitarium_failover()** (3 connections) — `server/services/lucidity_helpers.py`
- **test_handle_catatonia_transitions_enters_catatonia()** (3 connections) — `server/tests/unit/services/test_lucidity_trigger_handlers.py`
- **test_handle_catatonia_transitions_resolves_catatonia()** (3 connections) — `server/tests/unit/services/test_lucidity_trigger_handlers.py`
- **test_handle_delirium_trigger_sends_event()** (3 connections) — `server/tests/unit/services/test_lucidity_trigger_handlers.py`
- **test_handle_delirium_trigger_skips_when_not_crossing_threshold()** (3 connections) — `server/tests/unit/services/test_lucidity_trigger_handlers.py`
- **test_handle_delirium_trigger_debounced()** (3 connections) — `server/tests/unit/services/test_lucidity_trigger_handlers.py`
- **test_handle_sanitarium_trigger_invokes_observer()** (3 connections) — `server/tests/unit/services/test_lucidity_trigger_handlers.py`
- **test_handle_sanitarium_trigger_skips_without_observer()** (3 connections) — `server/tests/unit/services/test_lucidity_trigger_handlers.py`
- **test_handle_delirium_and_sanitarium_triggers_combined()** (3 connections) — `server/tests/unit/services/test_lucidity_trigger_handlers.py`
- **player_id()** (2 connections) — `server/tests/unit/services/test_lucidity_trigger_handlers.py`
- *... and 14 more nodes in this community*

## Relationships

- [player room realtime](player_room_realtime.md) (18 shared connections)
- [lucidity services helpers](lucidity_services_helpers.md) (7 shared connections)
- [Error Conversion](Error_Conversion.md) (3 shared connections)
- [auth endpoints rationale](auth_endpoints_rationale.md) (1 shared connections)
- [catatonia registry services](catatonia_registry_services.md) (1 shared connections)
- [command parser rationale](command_parser_rationale.md) (1 shared connections)

## Source Files

- `server/services/lucidity_helpers.py`
- `server/services/lucidity_trigger_handlers.py`
- `server/tests/unit/services/test_lucidity_trigger_handlers.py`

## Audit Trail

- EXTRACTED: 178 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*