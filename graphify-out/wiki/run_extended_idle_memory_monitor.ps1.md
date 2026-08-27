# run_extended_idle_memory_monitor.ps1

> 5 nodes

## Key Concepts

- **_ConnectionManagerUtilsModule** (3 connections) — `server/api/real_time.py`
- **_WebSocketHandlerModule** (2 connections) — `server/api/real_time.py`
- **.resolve_connection_manager()** (2 connections) — `server/api/real_time.py`
- **Protocol** (2 connections)
- **Resolve the connection manager singleton (or optional candidate).** (1 connections) — `server/api/real_time.py`

## Relationships

- [test_combat_validator.py](test_combat_validator.py.md) (2 shared connections)

## Source Files

- `server/api/real_time.py`

## Audit Trail

- EXTRACTED: 6 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*