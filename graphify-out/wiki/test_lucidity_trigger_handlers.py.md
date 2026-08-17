# test_lucidity_trigger_handlers.py

> 24 nodes

## Key Concepts

- **test_lucidity_trigger_handlers.py** (18 connections) — `server/tests/unit/services/test_lucidity_trigger_handlers.py`
- **handle_catatonia_transitions()** (13 connections) — `server/services/lucidity_trigger_handlers.py`
- **handle_delirium_and_sanitarium_triggers()** (10 connections) — `server/services/lucidity_trigger_handlers.py`
- **UUID** (10 connections)
- **handle_delirium_trigger()** (9 connections) — `server/services/lucidity_trigger_handlers.py`
- **handle_sanitarium_trigger()** (9 connections) — `server/services/lucidity_trigger_handlers.py`
- **asyncio** (8 connections)
- **UUID** (5 connections)
- **test_handle_catatonia_transitions_enters_catatonia()** (4 connections) — `server/tests/unit/services/test_lucidity_trigger_handlers.py`
- **test_handle_catatonia_transitions_resolves_catatonia()** (4 connections) — `server/tests/unit/services/test_lucidity_trigger_handlers.py`
- **test_handle_delirium_and_sanitarium_triggers_combined()** (4 connections) — `server/tests/unit/services/test_lucidity_trigger_handlers.py`
- **test_handle_delirium_trigger_debounced()** (4 connections) — `server/tests/unit/services/test_lucidity_trigger_handlers.py`
- **test_handle_delirium_trigger_sends_event()** (4 connections) — `server/tests/unit/services/test_lucidity_trigger_handlers.py`
- **test_handle_delirium_trigger_skips_when_not_crossing_threshold()** (4 connections) — `server/tests/unit/services/test_lucidity_trigger_handlers.py`
- **test_handle_sanitarium_trigger_invokes_observer()** (4 connections) — `server/tests/unit/services/test_lucidity_trigger_handlers.py`
- **test_handle_sanitarium_trigger_skips_without_observer()** (4 connections) — `server/tests/unit/services/test_lucidity_trigger_handlers.py`
- **player_id()** (3 connections) — `server/tests/unit/services/test_lucidity_trigger_handlers.py`
- **lucidity_record()** (2 connections) — `server/tests/unit/services/test_lucidity_trigger_handlers.py`
- **fixture** (2 connections)
- **Handle delirium respawn and sanitarium failover triggers.** (1 connections) — `server/services/lucidity_trigger_handlers.py`
- **Handle catatonia entry and exit transitions.** (1 connections) — `server/services/lucidity_trigger_handlers.py`
- **Handle delirium respawn threshold (LCD crosses -10); debounced.** (1 connections) — `server/services/lucidity_trigger_handlers.py`
- **Handle sanitarium failover (LCD crosses -100); uses observer debounce if…** (1 connections) — `server/services/lucidity_trigger_handlers.py`
- **Unit tests for lucidity trigger handlers.** (1 connections) — `server/tests/unit/services/test_lucidity_trigger_handlers.py`

## Relationships

- [ApplicationContainer](ApplicationContainer.md) (15 shared connections)
- [test_lucidity_event_dispatcher.py](test_lucidity_event_dispatcher.py.md) (4 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/services/lucidity_trigger_handlers.py`
- `server/tests/unit/services/test_lucidity_trigger_handlers.py`

## Audit Trail

- EXTRACTED: 70 (96%)
- INFERRED: 3 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*