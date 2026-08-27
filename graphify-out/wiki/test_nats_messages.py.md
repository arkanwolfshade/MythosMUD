# test_nats_messages.py

> 55 nodes

## Key Concepts

- **lucidity_helpers.py** (24 connections) — `server/services/lucidity_helpers.py`
- **lucidity_trigger_handlers.py** (19 connections) — `server/services/lucidity_trigger_handlers.py`
- **test_lucidity_trigger_handlers.py** (18 connections) — `server/tests/unit/services/test_lucidity_trigger_handlers.py`
- **CatatoniaObserverProtocol** (13 connections) — `server/services/lucidity_helpers.py`
- **handle_catatonia_transitions()** (11 connections) — `server/services/lucidity_trigger_handlers.py`
- **UUID** (10 connections)
- **handle_delirium_trigger()** (9 connections) — `server/services/lucidity_trigger_handlers.py`
- **handle_sanitarium_trigger()** (9 connections) — `server/services/lucidity_trigger_handlers.py`
- **handle_delirium_and_sanitarium_triggers()** (8 connections) — `server/services/lucidity_trigger_handlers.py`
- **asyncio** (8 connections)
- **utc_now()** (5 connections) — `server/services/lucidity_helpers.py`
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
- **.on_sanitarium_failover()** (3 connections) — `server/services/lucidity_helpers.py`
- *... and 30 more nodes in this community*

## Relationships

- [ContainerComponent](ContainerComponent.md) (9 shared connections)
- [test_npc_service.py](test_npc_service.py.md) (7 shared connections)
- [generate_invites_db.py](generate_invites_db.py.md) (3 shared connections)
- [disconnect_grace_period.py](disconnect_grace_period.py.md) (2 shared connections)
- [logging_file_setup.py](logging_file_setup.py.md) (2 shared connections)
- [test_connection_establishment.py](test_connection_establishment.py.md) (2 shared connections)
- [look_command.py](look_command.py.md) (1 shared connections)
- [RoomSubscriptionManager](RoomSubscriptionManager.md) (1 shared connections)
- [test_npc_combat_handlers.py](test_npc_combat_handlers.py.md) (1 shared connections)
- [NATSMetrics](NATSMetrics.md) (1 shared connections)

## Source Files

- `server/services/lucidity_helpers.py`
- `server/services/lucidity_trigger_handlers.py`
- `server/tests/unit/services/test_lucidity_trigger_handlers.py`

## Audit Trail

- EXTRACTED: 128 (98%)
- INFERRED: 3 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*