# Redis to NATS Migration

> 26 nodes

## Key Concepts

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
- **Protocol** (1 connections)
- **Return naive UTC timestamp suitable for PostgreSQL TIMESTAMP WITHOUT TIME ZONE.** (1 connections) — `server/services/lucidity_helpers.py`
- **Protocol for observers interested in catatonia state changes.** (1 connections) — `server/services/lucidity_helpers.py`
- **Handle a player crossing into catatonia.** (1 connections) — `server/services/lucidity_helpers.py`
- **Handle a player returning from catatonia.** (1 connections) — `server/services/lucidity_helpers.py`
- **Handle a player requiring sanitarium failover.** (1 connections) — `server/services/lucidity_helpers.py`
- **Return False to suppress failover (debounce); True allows failover handling.** (1 connections) — `server/services/lucidity_helpers.py`
- **Catatonia, delirium, and sanitarium trigger handling for lucidity changes.** (1 connections) — `server/services/lucidity_trigger_handlers.py`
- **Handle catatonia entry and exit transitions.** (1 connections) — `server/services/lucidity_trigger_handlers.py`
- **Handle delirium respawn threshold (LCD crosses -10); debounced.** (1 connections) — `server/services/lucidity_trigger_handlers.py`
- **Handle sanitarium failover (LCD crosses -100); uses observer debounce if availab** (1 connections) — `server/services/lucidity_trigger_handlers.py`
- *... and 1 more nodes in this community*

## Relationships

- [Enhanced Logging Exceptions](Enhanced_Logging_Exceptions.md) (16 shared connections)
- [Command Factory Tests](Command_Factory_Tests.md) (7 shared connections)
- [Client Event Store](Client_Event_Store.md) (3 shared connections)
- [Client Memory Leak Detector](Client_Memory_Leak_Detector.md) (2 shared connections)
- [Catatonia Registry Service](Catatonia_Registry_Service.md) (1 shared connections)
- [Performance Monitor Metrics](Performance_Monitor_Metrics.md) (1 shared connections)
- [Logging Correct Patterns](Logging_Correct_Patterns.md) (1 shared connections)

## Source Files

- `server/services/lucidity_helpers.py`
- `server/services/lucidity_trigger_handlers.py`

## Audit Trail

- EXTRACTED: 110 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*