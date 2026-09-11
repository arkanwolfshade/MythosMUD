# CatatoniaObserverProtocol

> 15 nodes

## Key Concepts

- **CatatoniaObserverProtocol** (19 connections) — `server/services/lucidity_helpers.py`
- **UUID** (5 connections)
- **.on_catatonia_cleared()** (4 connections) — `server/services/lucidity_helpers.py`
- **.on_catatonia_entered()** (4 connections) — `server/services/lucidity_helpers.py`
- **.__init__()** (4 connections) — `server/services/lucidity_service.py`
- **datetime** (4 connections)
- **.on_sanitarium_failover()** (3 connections) — `server/services/lucidity_helpers.py`
- **.should_trigger_sanitarium_failover()** (3 connections) — `server/services/lucidity_helpers.py`
- **Protocol** (1 connections)
- **AsyncSession** (1 connections)
- **Handle a player returning from catatonia.** (1 connections) — `server/services/lucidity_helpers.py`
- **Handle a player requiring sanitarium failover.** (1 connections) — `server/services/lucidity_helpers.py`
- **Return False to suppress failover (debounce); True allows failover handling.** (1 connections) — `server/services/lucidity_helpers.py`
- **Protocol for observers interested in catatonia state changes.** (1 connections) — `server/services/lucidity_helpers.py`
- **Handle a player crossing into catatonia.** (1 connections) — `server/services/lucidity_helpers.py`

## Relationships

- [Player](Player.md) (5 shared connections)
- [test_lucidity_event_dispatcher.py](test_lucidity_event_dispatcher.py.md) (3 shared connections)
- [test_admin_setlucidity_command.py](test_admin_setlucidity_command.py.md) (2 shared connections)
- [test_lucidity_trigger_handlers.py](test_lucidity_trigger_handlers.py.md) (2 shared connections)
- [LucidityService](LucidityService.md) (2 shared connections)
- [test_lucidity_recovery_commands.py](test_lucidity_recovery_commands.py.md) (1 shared connections)
- [passive_lucidity_flux/service.py](passive_lucidity_flux-service.py.md) (1 shared connections)
- [CatatoniaRegistry](CatatoniaRegistry.md) (1 shared connections)

## Source Files

- `server/services/lucidity_helpers.py`
- `server/services/lucidity_service.py`

## Audit Trail

- EXTRACTED: 31 (89%)
- INFERRED: 4 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*