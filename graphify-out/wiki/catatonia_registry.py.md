# catatonia_registry.py

> 13 nodes

## Key Concepts

- **catatonia_registry.py** (12 connections) — `server/services/catatonia_registry.py`
- **UUID** (6 connections)
- **.is_catatonic()** (4 connections) — `server/services/catatonia_registry.py`
- **datetime** (4 connections)
- **.get_snapshot()** (3 connections) — `server/services/catatonia_registry.py`
- **.on_catatonia_cleared()** (3 connections) — `server/services/catatonia_registry.py`
- **.on_catatonia_entered()** (3 connections) — `server/services/catatonia_registry.py`
- **.should_trigger_sanitarium_failover()** (3 connections) — `server/services/catatonia_registry.py`
- **.on_sanitarium_failover()** (2 connections) — `server/services/catatonia_registry.py`
- **In-memory registry tracking catatonic investigators.** (1 connections) — `server/services/catatonia_registry.py`
- **Return True if the player is currently registered as catatonic.** (1 connections) — `server/services/catatonia_registry.py`
- **Return a shallow copy of the current registry for diagnostics.** (1 connections) — `server/services/catatonia_registry.py`
- **Return True if we should trigger sanitarium failover for this player (not…** (1 connections) — `server/services/catatonia_registry.py`

## Relationships

- [CatatoniaRegistry](CatatoniaRegistry.md) (7 shared connections)
- [get_logger](get_logger.md) (3 shared connections)
- [catatonia_check.py](catatonia_check.py.md) (1 shared connections)
- [server/services/__init__.py](server-services-__init__.py.md) (1 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (1 shared connections)
- [server/dependencies.py](server-dependencies.py.md) (1 shared connections)
- [LucidityService](LucidityService.md) (1 shared connections)
- [test_catatonia_registry.py](test_catatonia_registry.py.md) (1 shared connections)

## Source Files

- `server/services/catatonia_registry.py`

## Audit Trail

- EXTRACTED: 29 (97%)
- INFERRED: 1 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*