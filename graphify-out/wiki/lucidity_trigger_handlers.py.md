# lucidity_trigger_handlers.py

> 38 nodes

## Key Concepts

- **lucidity_trigger_handlers.py** (19 connections) — `server/services/lucidity_trigger_handlers.py`
- **CatatoniaObserverProtocol** (17 connections) — `server/services/lucidity_helpers.py`
- **test_lucidity_trigger_handlers.py** (17 connections) — `server/tests/unit/services/test_lucidity_trigger_handlers.py`
- **handle_catatonia_transitions()** (13 connections) — `server/services/lucidity_trigger_handlers.py`
- **handle_delirium_and_sanitarium_triggers()** (10 connections) — `server/services/lucidity_trigger_handlers.py`
- **UUID** (10 connections)
- **handle_delirium_trigger()** (9 connections) — `server/services/lucidity_trigger_handlers.py`
- **handle_sanitarium_trigger()** (9 connections) — `server/services/lucidity_trigger_handlers.py`
- **asyncio** (8 connections)
- **UUID** (5 connections)
- **UUID** (5 connections)
- **.on_catatonia_cleared()** (4 connections) — `server/services/lucidity_helpers.py`
- **.on_catatonia_entered()** (4 connections) — `server/services/lucidity_helpers.py`
- **test_handle_catatonia_transitions_enters_catatonia()** (4 connections) — `server/tests/unit/services/test_lucidity_trigger_handlers.py`
- **test_handle_catatonia_transitions_resolves_catatonia()** (4 connections) — `server/tests/unit/services/test_lucidity_trigger_handlers.py`
- **test_handle_delirium_and_sanitarium_triggers_combined()** (4 connections) — `server/tests/unit/services/test_lucidity_trigger_handlers.py`
- **test_handle_delirium_trigger_debounced()** (4 connections) — `server/tests/unit/services/test_lucidity_trigger_handlers.py`
- **test_handle_delirium_trigger_sends_event()** (4 connections) — `server/tests/unit/services/test_lucidity_trigger_handlers.py`
- **test_handle_delirium_trigger_skips_when_not_crossing_threshold()** (4 connections) — `server/tests/unit/services/test_lucidity_trigger_handlers.py`
- **test_handle_sanitarium_trigger_invokes_observer()** (4 connections) — `server/tests/unit/services/test_lucidity_trigger_handlers.py`
- **test_handle_sanitarium_trigger_skips_without_observer()** (4 connections) — `server/tests/unit/services/test_lucidity_trigger_handlers.py`
- **.on_sanitarium_failover()** (3 connections) — `server/services/lucidity_helpers.py`
- **.should_trigger_sanitarium_failover()** (3 connections) — `server/services/lucidity_helpers.py`
- **player_id()** (3 connections) — `server/tests/unit/services/test_lucidity_trigger_handlers.py`
- **lucidity_record()** (2 connections) — `server/tests/unit/services/test_lucidity_trigger_handlers.py`
- *... and 13 more nodes in this community*

## Relationships

- [Player](Player.md) (18 shared connections)
- [test_lucidity_event_dispatcher.py](test_lucidity_event_dispatcher.py.md) (7 shared connections)
- [get_logger](get_logger.md) (3 shared connections)
- [test_lucidity_recovery_commands.py](test_lucidity_recovery_commands.py.md) (1 shared connections)
- [LucidityFluxService](LucidityFluxService.md) (1 shared connections)
- [CatatoniaRegistry](CatatoniaRegistry.md) (1 shared connections)

## Source Files

- `server/services/lucidity_helpers.py`
- `server/services/lucidity_trigger_handlers.py`
- `server/tests/unit/services/test_lucidity_trigger_handlers.py`

## Audit Trail

- EXTRACTED: 105 (96%)
- INFERRED: 4 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*