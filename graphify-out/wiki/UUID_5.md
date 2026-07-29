# UUID

> 36 nodes

## Key Concepts

- **send_rescue_update_event()** (18 connections) — `server/services/lucidity_event_dispatcher.py`
- **lucidity_trigger_handlers.py** (18 connections) — `server/services/lucidity_trigger_handlers.py`
- **CatatoniaObserverProtocol** (17 connections) — `server/services/lucidity_helpers.py`
- **handle_catatonia_transitions()** (10 connections) — `server/services/lucidity_trigger_handlers.py`
- **handle_delirium_and_sanitarium_triggers()** (8 connections) — `server/services/lucidity_trigger_handlers.py`
- **utc_now()** (7 connections) — `server/services/lucidity_helpers.py`
- **handle_sanitarium_trigger()** (6 connections) — `server/services/lucidity_trigger_handlers.py`
- **UUID** (5 connections)
- **UUID** (5 connections)
- **handle_delirium_trigger()** (5 connections) — `server/services/lucidity_trigger_handlers.py`
- **datetime** (4 connections)
- **.on_catatonia_entered()** (4 connections) — `server/services/lucidity_helpers.py`
- **.on_catatonia_cleared()** (4 connections) — `server/services/lucidity_helpers.py`
- **.on_sanitarium_failover()** (3 connections) — `server/services/lucidity_helpers.py`
- **.should_trigger_sanitarium_failover()** (3 connections) — `server/services/lucidity_helpers.py`
- **test_send_rescue_update_event_basic()** (3 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **test_send_rescue_update_event_with_all_fields()** (3 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **test_send_rescue_update_event_with_progress_only()** (3 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **test_send_rescue_update_event_dispatch_error()** (3 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **Send rescue progress/status updates to either participant.** (1 connections) — `server/services/lucidity_event_dispatcher.py`
- **Protocol** (1 connections)
- **Return naive UTC timestamp suitable for PostgreSQL TIMESTAMP WITHOUT TIME ZONE.** (1 connections) — `server/services/lucidity_helpers.py`
- **Protocol for observers interested in catatonia state changes.** (1 connections) — `server/services/lucidity_helpers.py`
- **Handle a player crossing into catatonia.** (1 connections) — `server/services/lucidity_helpers.py`
- **Handle a player returning from catatonia.** (1 connections) — `server/services/lucidity_helpers.py`
- *... and 11 more nodes in this community*

## Relationships

- [LiabilityStackEntry](LiabilityStackEntry.md) (23 shared connections)
- [rescue commands](rescue_commands.md) (4 shared connections)
- [. init ()](_init_%28%29.md) (4 shared connections)
- [main()](main%28%29.md) (3 shared connections)
- [datetime](datetime.md) (2 shared connections)
- [AsyncSessionFactory](AsyncSessionFactory.md) (1 shared connections)
- [HallucinationFrequencyService](HallucinationFrequencyService.md) (1 shared connections)
- [CatatoniaRegistry](CatatoniaRegistry.md) (1 shared connections)
- [config](config.md) (1 shared connections)

## Source Files

- `server/services/lucidity_event_dispatcher.py`
- `server/services/lucidity_helpers.py`
- `server/services/lucidity_trigger_handlers.py`
- `server/tests/unit/services/test_lucidity_event_dispatcher.py`

## Audit Trail

- EXTRACTED: 145 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*