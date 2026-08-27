# lucidity_trigger_handlers.py

> 45 nodes

## Key Concepts

- **lucidity_trigger_handlers.py** (19 connections) — `server/services/lucidity_trigger_handlers.py`
- **test_lucidity_trigger_handlers.py** (18 connections) — `server/tests/unit/services/test_lucidity_trigger_handlers.py`
- **CatatoniaObserverProtocol** (17 connections) — `server/services/lucidity_helpers.py`
- **handle_catatonia_transitions()** (13 connections) — `server/services/lucidity_trigger_handlers.py`
- **handle_delirium_and_sanitarium_triggers()** (10 connections) — `server/services/lucidity_trigger_handlers.py`
- **UUID** (10 connections)
- **handle_delirium_trigger()** (9 connections) — `server/services/lucidity_trigger_handlers.py`
- **handle_sanitarium_trigger()** (9 connections) — `server/services/lucidity_trigger_handlers.py`
- **asyncio** (8 connections)
- **utc_now()** (7 connections) — `server/services/lucidity_helpers.py`
- **.__init__()** (7 connections) — `server/services/passive_lucidity_flux/service.py`
- **normalize_environment_config()** (5 connections) — `server/services/passive_lucidity_flux/config.py`
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
- **datetime** (4 connections)
- *... and 20 more nodes in this community*

## Relationships

- [models/player.py](models-player.py.md) (19 shared connections)
- [test_lucidity_event_dispatcher.py](test_lucidity_event_dispatcher.py.md) (7 shared connections)
- [PassiveFluxContext](PassiveFluxContext.md) (2 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [test_lucidity_recovery_commands.py](test_lucidity_recovery_commands.py.md) (1 shared connections)
- [CatatoniaRegistry](CatatoniaRegistry.md) (1 shared connections)
- [test_rate_overrides.py](test_rate_overrides.py.md) (1 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (1 shared connections)
- [PerformanceMonitor](PerformanceMonitor.md) (1 shared connections)
- [LucidityFluxService](LucidityFluxService.md) (1 shared connections)
- [time.py](time.py.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/services/lucidity_helpers.py`
- `server/services/lucidity_trigger_handlers.py`
- `server/services/passive_lucidity_flux/config.py`
- `server/services/passive_lucidity_flux/service.py`
- `server/tests/unit/services/test_lucidity_trigger_handlers.py`

## Audit Trail

- EXTRACTED: 122 (97%)
- INFERRED: 4 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*